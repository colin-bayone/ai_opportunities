"""
Fetch meeting transcripts from Microsoft Teams via Graph API.

Implements the 5-step transcript retrieval flow:
  1. Get join URL from meeting event
  2. Get online meeting ID from join URL
  3. List transcripts for that meeting
  4. Fetch VTT content
  5. Parse and format

Usage:
    from graph_client import GraphClient
    from transcript_fetcher import TranscriptFetcher

    client = GraphClient(env_file="/path/to/.env")
    fetcher = TranscriptFetcher(client)

    result = fetcher.fetch(join_url="https://teams.microsoft.com/l/meetup-join/...")
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from graph_client import GraphClient, get_output_dir
from vtt_parser import VTTParser
from transcript_formatter import TranscriptFormatter


class TranscriptNotAvailable(Exception):
    """Raised when no transcript exists for a meeting."""
    pass


class TranscriptFetcher:
    """Fetch and save meeting transcripts from Teams."""

    def __init__(self, client: GraphClient, output_dir: str = None):
        self.client = client
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = get_output_dir(client.env_file)

    def fetch(self, join_url: str, event_date: str = None) -> dict:
        """
        Fetch transcript for a meeting by its join URL.

        For recurring meetings, multiple transcripts exist under the same
        online meeting ID. The event_date is used to match the correct
        transcript by comparing against each transcript's createdDateTime.

        Args:
            join_url: Teams meeting join URL
            event_date: The calendar event's start date (YYYY-MM-DD) for
                        matching the correct transcript in recurring series.
                        If None, returns the most recent transcript.

        Returns dict with:
          - raw_vtt: str (raw VTT content)
          - formatted_text: str (readable conversation format)
          - parser: VTTParser instance
          - speakers: list of speaker names
          - utterance_count: int
          - word_count: int
          - duration_seconds: float

        Raises:
          TranscriptNotAvailable: If no transcript exists
          Exception: On API errors
        """
        prefix = self.client._get_endpoint_prefix()

        # Step 1: Get online meeting ID from join URL
        filter_url = f"{prefix}/onlineMeetings?$filter=JoinWebUrl eq '{join_url}'"
        meetings_response = self.client.get(filter_url)

        if not meetings_response["success"]:
            error = meetings_response.get("error", "Unknown error")
            raise Exception(f"Failed to find online meeting: {error}")

        meetings = meetings_response["data"].get("value", [])
        if not meetings:
            raise TranscriptNotAvailable(
                "No online meeting found for this join URL. "
                "The meeting may have been deleted or the URL is invalid."
            )

        online_meeting_id = meetings[0].get("id")
        if not online_meeting_id:
            raise Exception("Online meeting found but has no ID.")

        # Step 2: List transcripts for this online meeting
        transcripts_endpoint = f"{prefix}/onlineMeetings/{online_meeting_id}/transcripts"
        transcripts_response = self.client.get(transcripts_endpoint)

        if not transcripts_response["success"]:
            error = transcripts_response.get("error", "Unknown error")
            raise Exception(f"Failed to list transcripts: {error}")

        transcripts = transcripts_response["data"].get("value", [])
        if not transcripts:
            raise TranscriptNotAvailable(
                "No transcripts available for this meeting. "
                "Transcription must be enabled during the Teams meeting."
            )

        # Step 3: Match the correct transcript for this event date.
        # Recurring meetings share one onlineMeetingId but have multiple
        # transcripts, each with a unique createdDateTime.
        transcript_entry = self._match_transcript_by_date(transcripts, event_date)
        if not transcript_entry:
            raise TranscriptNotAvailable(
                f"No transcript found for event date {event_date}. "
                f"There are {len(transcripts)} transcript(s) for this recurring "
                f"meeting series, but none match this date."
            )

        transcript_id = transcript_entry["id"]
        content_endpoint = (
            f"{prefix}/onlineMeetings/{online_meeting_id}"
            f"/transcripts/{transcript_id}/content?$format=text/vtt"
        )
        content_response = self.client.get(content_endpoint, return_binary=True)

        if not content_response["success"]:
            error = content_response.get("error", "Unknown error")
            raise Exception(f"Failed to fetch transcript content: {error}")

        # Step 4: Decode and parse VTT
        vtt_bytes = content_response["data"]
        if isinstance(vtt_bytes, bytes):
            raw_vtt = vtt_bytes.decode("utf-8")
        elif isinstance(vtt_bytes, str):
            raw_vtt = vtt_bytes
        else:
            raise Exception(f"Unexpected content type: {type(vtt_bytes)}")

        if not raw_vtt or len(raw_vtt) < 10:
            raise TranscriptNotAvailable("Received empty transcript content.")

        parser = VTTParser(raw_vtt)
        parser.parse()

        # Step 5: Format
        formatter = TranscriptFormatter(parser.utterances)
        formatted_text = formatter.to_text(
            include_timestamps=True, include_speakers=True, merge_consecutive=True
        )

        return {
            "raw_vtt": raw_vtt,
            "formatted_text": formatted_text,
            "parser": parser,
            "speakers": parser.get_speakers(),
            "utterance_count": len(parser),
            "word_count": sum(u.word_count for u in parser.utterances),
            "duration_seconds": parser.get_duration(),
        }

    def is_already_downloaded(
        self, meeting_info: dict, person_name: str = None, sequence_num: int = 1
    ) -> str | None:
        """
        Check if a transcript has already been downloaded for this meeting.

        Returns the folder path if found, None if not downloaded yet.
        """
        date_str, _ = self._parse_meeting_datetime(
            meeting_info.get("start_datetime", "")
        )

        if person_name:
            person_slug = self._slugify(person_name)
        else:
            person_slug = self._slugify(meeting_info.get("subject", "meeting"))

        subject_slug = self._slugify(meeting_info.get("subject", "meeting"))
        seq = f"{sequence_num:02d}"

        folder = self.output_dir / person_slug / date_str
        txt_path = folder / f"{subject_slug}_{seq}.txt"

        if txt_path.exists():
            return str(folder)
        return None

    def save_transcript(
        self,
        transcript_data: dict,
        meeting_info: dict,
        person_name: str = None,
        sequence_num: int = 1,
    ) -> dict:
        """
        Save transcript and metadata to organized folder structure.

        Args:
            transcript_data: Result from fetch()
            meeting_info: Event info dict from CalendarSearch
            person_name: Person's name for folder naming (None = use subject slug)
            sequence_num: Number for same-day meetings (1, 2, 3...)

        Returns:
            Dict with file paths created
        """
        # Determine date from meeting info
        date_str, time_str = self._parse_meeting_datetime(
            meeting_info.get("start_datetime", "")
        )

        # Build folder: person_slug/YYYY-MM-DD/ or subject_slug/YYYY-MM-DD/
        if person_name:
            person_slug = self._slugify(person_name)
        else:
            person_slug = self._slugify(meeting_info.get("subject", "meeting"))

        folder = self.output_dir / person_slug / date_str
        folder.mkdir(parents=True, exist_ok=True)

        # Build file base name: subject-slug_NN
        subject_slug = self._slugify(meeting_info.get("subject", "meeting"))
        seq = f"{sequence_num:02d}"
        base_name = f"{subject_slug}_{seq}"

        # Save formatted transcript
        txt_path = folder / f"{base_name}.txt"
        txt_path.write_text(transcript_data["formatted_text"], encoding="utf-8")

        # Save raw VTT
        vtt_path = folder / f"{base_name}.vtt"
        vtt_path.write_text(transcript_data["raw_vtt"], encoding="utf-8")

        # Build and save metadata
        _, end_time_str = self._parse_meeting_datetime(
            meeting_info.get("end_datetime", "")
        )

        metadata = {
            "meeting_subject": meeting_info.get("subject", ""),
            "date": date_str,
            "start_time": time_str,
            "end_time": end_time_str,
            "duration_minutes": meeting_info.get("duration_minutes", 0),
            "organizer": meeting_info.get("organizer_email", ""),
            "attendees": [
                a.get("email", "") for a in meeting_info.get("attendees", [])
            ],
            "online_meeting_url": meeting_info.get("join_url", ""),
            "transcript_fetched_at": datetime.now(timezone.utc).isoformat(),
            "utterance_count": transcript_data["utterance_count"],
            "speakers": transcript_data["speakers"],
            "word_count": transcript_data["word_count"],
            "duration_seconds": transcript_data["duration_seconds"],
            "speaker_stats": {},
        }

        # Add speaker stats if available
        if transcript_data.get("parser"):
            metadata["speaker_stats"] = transcript_data["parser"].get_speaker_stats()

        meta_path = folder / f"{base_name}_meta.json"
        meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

        return {
            "transcript_file": str(txt_path),
            "vtt_file": str(vtt_path),
            "metadata_file": str(meta_path),
            "folder": str(folder),
        }

    def check_transcript_timing(self, meeting_info: dict) -> Optional[str]:
        """
        Check if a missing transcript might be due to processing delay.

        Returns a user-friendly message if the meeting is recent,
        or None if the meeting is old enough that transcription was not enabled.
        """
        end_dt_str = meeting_info.get("end_datetime", "")
        if not end_dt_str:
            return None

        try:
            cleaned = end_dt_str.rstrip("Z")
            if "." in cleaned:
                base, frac = cleaned.split(".", 1)
                cleaned = f"{base}.{frac[:6]}"
            end_dt = datetime.fromisoformat(cleaned)
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)

            now = datetime.now(timezone.utc)
            minutes_since = (now - end_dt).total_seconds() / 60

            if minutes_since < 30:
                return (
                    f"This meeting ended {int(minutes_since)} minutes ago. "
                    "If transcription was enabled, the transcript may still be processing. "
                    "Try again in 15-20 minutes."
                )
            elif minutes_since < 90:
                return (
                    f"This meeting ended about {int(minutes_since)} minutes ago. "
                    "If transcription was enabled, it should appear soon. "
                    "Try again shortly."
                )
            else:
                hours = minutes_since / 60
                return (
                    f"This meeting ended {hours:.1f} hours ago. "
                    "Transcription was likely not enabled for this meeting."
                )
        except (ValueError, TypeError):
            return None

    def _match_transcript_by_date(
        self, transcripts: list[dict], event_date: str = None
    ) -> dict | None:
        """
        Match the correct transcript from a list by comparing the
        transcript's createdDateTime against the calendar event date.

        For recurring meetings, the /transcripts endpoint returns all
        transcripts across all instances. Each has a unique createdDateTime
        corresponding to when that specific meeting instance occurred.

        Args:
            transcripts: List of transcript entries from Graph API
            event_date: YYYY-MM-DD of the calendar event. If None,
                        returns the most recent transcript (index 0).

        Returns:
            The matching transcript dict, or None if no match.
        """
        if not transcripts:
            return None

        # No date filter — return most recent (API returns newest first)
        if not event_date:
            return transcripts[0]

        # Match by date: find the transcript whose createdDateTime
        # falls on the same calendar date as the event
        for t in transcripts:
            created = t.get("createdDateTime", "")
            if not created:
                continue
            # Extract just the date portion (YYYY-MM-DD) from the ISO string
            transcript_date = created[:10]
            if transcript_date == event_date:
                return t

        return None

    def _parse_meeting_datetime(self, dt_string: str) -> tuple[str, str]:
        """
        Parse a datetime string from Graph API into (date_str, time_str).
        Handles trailing Z and microsecond formats that Python 3.10
        fromisoformat doesn't support.

        Returns:
            Tuple of (YYYY-MM-DD, HH:MM:SS). Falls back to today/00:00:00.
        """
        if not dt_string:
            return datetime.now().strftime("%Y-%m-%d"), "00:00:00"

        # Strip trailing Z and truncate microseconds beyond 6 digits
        cleaned = dt_string.rstrip("Z")
        if "." in cleaned:
            base, frac = cleaned.split(".", 1)
            cleaned = f"{base}.{frac[:6]}"

        try:
            dt = datetime.fromisoformat(cleaned)
            return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M:%S")
        except (ValueError, TypeError):
            return datetime.now().strftime("%Y-%m-%d"), "00:00:00"

    def _slugify(self, text: str) -> str:
        """Convert text to a filename-safe slug."""
        text = text.lower().strip()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text[:50].strip("-")
