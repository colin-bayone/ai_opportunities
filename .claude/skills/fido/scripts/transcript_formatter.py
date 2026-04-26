"""
Transcript Formatter.
Ported from communications/transcript_services/transcript_formatter.py.

Converts parsed VTT utterances to clean, readable text formats.
Zero external dependencies beyond vtt_parser.py.

Usage:
    from vtt_parser import VTTParser
    from transcript_formatter import TranscriptFormatter

    parser = VTTParser(vtt_content)
    parser.parse()

    formatter = TranscriptFormatter(parser.utterances)
    text = formatter.to_text(include_timestamps=True, merge_consecutive=True)
"""
from typing import List
from vtt_parser import Utterance


class TranscriptFormatter:
    """Format utterances into readable text."""

    def __init__(self, utterances: List[Utterance]):
        self.utterances = utterances

    def format_timestamp(self, seconds: float) -> str:
        """Format seconds as [HH:MM:SS]."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"[{hours:02d}:{minutes:02d}:{secs:02d}]"

    def to_text(
        self,
        include_timestamps: bool = True,
        include_speakers: bool = True,
        merge_consecutive: bool = True,
    ) -> str:
        """
        Convert utterances to conversation format.

        Output example:
            [00:01:30] Colin Moore: Hello, how's it going?

            [00:01:35] Ambar Singh: Good, thanks for joining.
        """
        if not self.utterances:
            return ""

        lines = []
        last_speaker = None
        current_text = []
        current_timestamp = None

        for utt in self.utterances:
            if merge_consecutive and utt.speaker == last_speaker:
                current_text.append(utt.text)
            else:
                if current_text:
                    line_parts = []
                    if include_timestamps and current_timestamp is not None:
                        line_parts.append(self.format_timestamp(current_timestamp))
                    if include_speakers and last_speaker:
                        line_parts.append(f"{last_speaker}:")
                    line_parts.append(" ".join(current_text))
                    lines.append(" ".join(line_parts))

                current_text = [utt.text]
                current_timestamp = utt.start_time
                last_speaker = utt.speaker

        if current_text:
            line_parts = []
            if include_timestamps and current_timestamp is not None:
                line_parts.append(self.format_timestamp(current_timestamp))
            if include_speakers and last_speaker:
                line_parts.append(f"{last_speaker}:")
            line_parts.append(" ".join(current_text))
            lines.append(" ".join(line_parts))

        return "\n\n".join(lines)

    def to_markdown(self) -> str:
        """Format as Markdown with ## Speaker headers."""
        if not self.utterances:
            return ""

        lines = []
        last_speaker = None
        current_text = []

        for utt in self.utterances:
            if utt.speaker != last_speaker:
                if current_text:
                    lines.append(f"## {last_speaker}\n")
                    lines.append(" ".join(current_text) + "\n")

                current_text = [utt.text]
                last_speaker = utt.speaker
            else:
                current_text.append(utt.text)

        if current_text:
            lines.append(f"## {last_speaker}\n")
            lines.append(" ".join(current_text) + "\n")

        return "\n".join(lines)

    def to_timestamped_entries(self) -> List[str]:
        """Format as list of individual timestamped entries."""
        entries = []
        for utt in self.utterances:
            timestamp = self.format_timestamp(utt.start_time)
            entry = f"{timestamp} {utt.speaker}: {utt.text}"
            entries.append(entry)
        return entries

    def get_text_only(self) -> str:
        """Plain text without speakers or timestamps."""
        return self.to_text(
            include_timestamps=False,
            include_speakers=False,
            merge_consecutive=True,
        )

    def __len__(self) -> int:
        return len(self.utterances)
