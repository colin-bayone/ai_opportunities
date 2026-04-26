"""
Calendar search — find meetings by person, date range, or all.
Uses Graph API calendarView endpoint.

Usage:
    from calendar_search import CalendarSearch
    from graph_client import GraphClient

    client = GraphClient(env_file="/path/to/.env")
    search = CalendarSearch(client)

    # Find meetings with a specific person
    meetings = search.find_meetings_with_person(
        email="ambar@bayone.com",
        start_date="2026-04-01",
        end_date="2026-04-16"
    )

    # Find all meetings in a date range
    meetings = search.find_meetings_in_range("2026-04-10", "2026-04-16")

    # List meetings (metadata only, for display)
    table = search.list_meetings("2026-04-10", "2026-04-16")
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from graph_client import GraphClient


class CalendarSearch:
    """Search calendar events via Microsoft Graph API."""

    def __init__(self, client: GraphClient):
        self.client = client

    def _parse_date(self, date_str: str) -> datetime:
        """Parse a date string into a timezone-aware datetime."""
        if isinstance(date_str, datetime):
            if date_str.tzinfo is None:
                return date_str.replace(tzinfo=timezone.utc)
            return date_str

        # Support various formats
        for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z"):
            try:
                dt = datetime.strptime(date_str, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt
            except ValueError:
                continue

        raise ValueError(f"Cannot parse date: {date_str}")

    def _get_calendar_events(
        self, start_date: str, end_date: str, limit: int = 200
    ) -> list[dict]:
        """Fetch calendar events from Graph API."""
        start_dt = self._parse_date(start_date)
        # Set end date to end of day
        end_dt = self._parse_date(end_date)
        if end_dt.hour == 0 and end_dt.minute == 0:
            end_dt = end_dt.replace(hour=23, minute=59, second=59)

        prefix = self.client._get_endpoint_prefix()
        endpoint = f"{prefix}/calendarView"

        params = {
            "startDateTime": start_dt.isoformat(),
            "endDateTime": end_dt.isoformat(),
            "$top": limit,
            "$orderby": "start/dateTime",
            "$select": (
                "subject,start,end,organizer,attendees,location,"
                "isAllDay,webLink,bodyPreview,id,onlineMeeting,"
                "isOnlineMeeting"
            ),
        }

        result = self.client.get(endpoint, params=params)

        if not result["success"]:
            error = result.get("error", "Unknown error")
            print(f"ERROR: Failed to fetch calendar events: {error}", file=sys.stderr)
            return []

        return result["data"].get("value", [])

    def _get_all_participant_emails(self, event: dict) -> set[str]:
        """Get all participant emails (organizer + attendees) as a lowercase set."""
        emails = set()

        organizer = event.get("organizer", {}).get("emailAddress", {})
        org_email = organizer.get("address", "").lower()
        if org_email:
            emails.add(org_email)

        for attendee in event.get("attendees", []):
            att_email = attendee.get("emailAddress", {}).get("address", "").lower()
            if att_email:
                emails.add(att_email)

        return emails

    def _event_has_attendee(self, event: dict, email: str) -> bool:
        """Check if an event has a specific attendee (by email)."""
        return email.lower() in self._get_all_participant_emails(event)

    def _event_is_exclusive(self, event: dict, my_email: str, person_email: str) -> bool:
        """
        Check if a meeting is ONLY between the specified people.
        Returns True if the only participants are my_email and person_email.
        """
        participants = self._get_all_participant_emails(event)
        allowed = {my_email.lower(), person_email.lower()}
        return participants.issubset(allowed) and len(participants) >= 2

    def _extract_event_info(self, event: dict) -> dict:
        """Extract relevant info from a Graph API event."""
        start = event.get("start", {})
        end = event.get("end", {})

        start_dt = start.get("dateTime", "")
        end_dt = end.get("dateTime", "")

        # Calculate duration (handle Graph API's 7-digit microseconds + trailing Z)
        duration_minutes = 0
        try:
            s_clean = start_dt.rstrip("Z")
            e_clean = end_dt.rstrip("Z")
            if "." in s_clean:
                base, frac = s_clean.split(".", 1)
                s_clean = f"{base}.{frac[:6]}"
            if "." in e_clean:
                base, frac = e_clean.split(".", 1)
                e_clean = f"{base}.{frac[:6]}"
            s = datetime.fromisoformat(s_clean)
            e = datetime.fromisoformat(e_clean)
            duration_minutes = int((e - s).total_seconds() / 60)
        except (ValueError, TypeError):
            pass

        # Get join URL
        online_meeting = event.get("onlineMeeting", {}) or {}
        join_url = online_meeting.get("joinUrl", "")

        # Get organizer
        organizer = event.get("organizer", {}).get("emailAddress", {})

        # Get attendees
        attendees = []
        for att in event.get("attendees", []):
            email_obj = att.get("emailAddress", {})
            attendees.append({
                "name": email_obj.get("name", ""),
                "email": email_obj.get("address", ""),
            })

        return {
            "event_id": event.get("id", ""),
            "subject": event.get("subject", "(No subject)"),
            "start_datetime": start_dt,
            "end_datetime": end_dt,
            "start_timezone": start.get("timeZone", "UTC"),
            "duration_minutes": duration_minutes,
            "organizer_name": organizer.get("name", ""),
            "organizer_email": organizer.get("address", ""),
            "attendees": attendees,
            "is_online_meeting": event.get("isOnlineMeeting", False),
            "join_url": join_url,
            "location": event.get("location", {}).get("displayName", ""),
            "is_all_day": event.get("isAllDay", False),
            "web_link": event.get("webLink", ""),
        }

    def find_meetings_with_person(
        self, email: str, start_date: str, end_date: str,
        exclusive: bool = False, my_email: str = None,
    ) -> list[dict]:
        """
        Find meetings with a specific person in a date range.

        Args:
            email: The other person's email
            start_date: Start of range
            end_date: End of range
            exclusive: If True, only return meetings where the ONLY
                       participants are you and this person (1:1s).
                       Requires my_email to be set.
            my_email: Your email (needed for exclusive mode)
        """
        events = self._get_calendar_events(start_date, end_date)

        matches = []
        for event in events:
            if not self._event_has_attendee(event, email):
                continue
            if exclusive:
                if not my_email:
                    raise ValueError("my_email is required for exclusive mode")
                if not self._event_is_exclusive(event, my_email, email):
                    continue
            matches.append(self._extract_event_info(event))

        return sorted(matches, key=lambda e: e["start_datetime"])

    def find_recent_meeting(
        self, email: str, days_back: int = 30,
        exclusive: bool = False, my_email: str = None,
    ) -> Optional[dict]:
        """Find the most recent meeting with a specific person."""
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=days_back)

        meetings = self.find_meetings_with_person(
            email=email,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            exclusive=exclusive,
            my_email=my_email,
        )

        if not meetings:
            return None

        # Return the most recent (last in sorted list)
        return meetings[-1]

    def find_meetings_by_subject(
        self, query: str, start_date: str, end_date: str
    ) -> list[dict]:
        """
        Find meetings whose subject contains the query string (case-insensitive).

        Args:
            query: Search term to match against meeting subjects
            start_date: Start of range
            end_date: End of range

        Returns:
            List of matching event info dicts, sorted by start time
        """
        events = self._get_calendar_events(start_date, end_date)
        query_lower = query.lower()

        matches = []
        for event in events:
            subject = event.get("subject", "")
            if query_lower in subject.lower():
                matches.append(self._extract_event_info(event))

        return sorted(matches, key=lambda e: e["start_datetime"])

    def find_meetings_in_range(
        self, start_date: str, end_date: str, online_only: bool = True
    ) -> list[dict]:
        """Find all meetings in a date range, optionally filtered to online meetings only."""
        events = self._get_calendar_events(start_date, end_date)

        results = []
        for event in events:
            info = self._extract_event_info(event)
            if online_only and not info["is_online_meeting"]:
                continue
            results.append(info)

        return sorted(results, key=lambda e: e["start_datetime"])

    def list_meetings(self, start_date: str, end_date: str) -> list[dict]:
        """List all meetings (both online and in-person) for display."""
        events = self._get_calendar_events(start_date, end_date)

        results = []
        for event in events:
            results.append(self._extract_event_info(event))

        return sorted(results, key=lambda e: e["start_datetime"])

    def format_meetings_table(self, meetings: list[dict]) -> str:
        """Format meetings as a readable table string."""
        if not meetings:
            return "No meetings found in this date range."

        lines = []
        lines.append(f"{'Date':<12} {'Time':<8} {'Dur':<6} {'Subject':<40} {'Attendees':<30} {'Online'}")
        lines.append("-" * 110)

        for m in meetings:
            date_str, time_str = self._parse_dt_clean(m["start_datetime"])

            dur = f"{m['duration_minutes']}m"
            subject = m["subject"][:38] + ".." if len(m["subject"]) > 40 else m["subject"]

            attendee_names = [a["name"] or a["email"] for a in m["attendees"][:3]]
            attendees_str = ", ".join(attendee_names)
            if len(m["attendees"]) > 3:
                attendees_str += f" +{len(m['attendees']) - 3}"
            attendees_str = attendees_str[:28] + ".." if len(attendees_str) > 30 else attendees_str

            online = "Yes" if m["is_online_meeting"] else "No"

            lines.append(f"{date_str:<12} {time_str:<8} {dur:<6} {subject:<40} {attendees_str:<30} {online}")

        lines.append(f"\nTotal: {len(meetings)} meetings")
        return "\n".join(lines)

    def _parse_dt_clean(self, dt_string: str) -> tuple[str, str]:
        """Parse Graph API datetime to (date, time) strings. Python 3.10 safe."""
        try:
            cleaned = dt_string.rstrip("Z")
            if "." in cleaned:
                base, frac = cleaned.split(".", 1)
                cleaned = f"{base}.{frac[:6]}"
            dt = datetime.fromisoformat(cleaned)
            return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M")
        except (ValueError, TypeError):
            return "?", "?"

    def format_meetings_csv(self, meetings: list[dict]) -> str:
        """Format meetings as CSV content."""
        lines = ["Date,Time,Duration (min),Subject,Organizer,Attendees,Online,Join URL"]

        for m in meetings:
            date_str, time_str = self._parse_dt_clean(m["start_datetime"])
            subject = m["subject"].replace('"', '""')
            organizer = m.get("organizer_email", "")
            attendees = "; ".join(
                a.get("email", "") for a in m.get("attendees", [])
            )
            online = "Yes" if m.get("is_online_meeting") else "No"
            join_url = m.get("join_url", "")

            lines.append(
                f'{date_str},{time_str},{m["duration_minutes"]},"{subject}",'
                f'{organizer},"{attendees}",{online},"{join_url}"'
            )

        return "\n".join(lines)

    def format_meetings_markdown(self, meetings: list[dict]) -> str:
        """Format meetings as a markdown table."""
        lines = [
            "| Date | Time | Duration | Subject | Attendees | Online |",
            "|------|------|----------|---------|-----------|--------|",
        ]

        for m in meetings:
            date_str, time_str = self._parse_dt_clean(m["start_datetime"])
            subject = m["subject"]
            attendee_names = [a["name"] or a["email"] for a in m.get("attendees", [])[:5]]
            attendees_str = ", ".join(attendee_names)
            if len(m.get("attendees", [])) > 5:
                attendees_str += f" +{len(m['attendees']) - 5}"
            online = "Yes" if m.get("is_online_meeting") else "No"

            lines.append(
                f"| {date_str} | {time_str} | {m['duration_minutes']}m | {subject} | {attendees_str} | {online} |"
            )

        lines.append(f"\n*{len(meetings)} meetings total*")
        return "\n".join(lines)

    def compute_stats(self, meetings: list[dict]) -> dict:
        """
        Compute summary statistics for a list of meetings.

        Returns dict with:
          - total_meetings: int
          - total_hours: float
          - online_meetings: int
          - in_person_meetings: int
          - all_day_events: int
          - unique_attendees: dict (name -> count)
          - top_attendees: list of (name, email, count) sorted by frequency
          - by_day_of_week: dict (Monday->count, ...)
          - avg_duration_minutes: float
        """
        from collections import Counter

        stats = {
            "total_meetings": len(meetings),
            "total_hours": 0.0,
            "online_meetings": 0,
            "in_person_meetings": 0,
            "all_day_events": 0,
            "avg_duration_minutes": 0,
            "unique_attendees": {},
            "top_attendees": [],
            "by_day_of_week": {
                "Monday": 0, "Tuesday": 0, "Wednesday": 0,
                "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0,
            },
        }

        if not meetings:
            return stats

        attendee_counter = Counter()
        attendee_emails = {}
        total_minutes = 0

        for m in meetings:
            dur = m.get("duration_minutes", 0)

            if m.get("is_all_day"):
                stats["all_day_events"] += 1
                continue  # Don't count all-day events in duration stats

            total_minutes += dur

            if m.get("is_online_meeting"):
                stats["online_meetings"] += 1
            else:
                stats["in_person_meetings"] += 1

            # Day of week
            date_str, _ = self._parse_dt_clean(m.get("start_datetime", ""))
            if date_str != "?":
                try:
                    dt = datetime.fromisoformat(date_str)
                    day_name = dt.strftime("%A")
                    stats["by_day_of_week"][day_name] = (
                        stats["by_day_of_week"].get(day_name, 0) + 1
                    )
                except (ValueError, TypeError):
                    pass

            # Attendees (excluding self)
            for a in m.get("attendees", []):
                name = a.get("name", "")
                email = a.get("email", "").lower()
                if email and email != "cmoore@bayone.com":
                    attendee_counter[name or email] += 1
                    attendee_emails[name or email] = email

        non_allday = stats["total_meetings"] - stats["all_day_events"]
        stats["total_hours"] = round(total_minutes / 60, 1)
        stats["avg_duration_minutes"] = (
            round(total_minutes / non_allday) if non_allday > 0 else 0
        )

        # Top attendees
        stats["top_attendees"] = [
            {"name": name, "email": attendee_emails.get(name, ""), "count": count}
            for name, count in attendee_counter.most_common(15)
        ]

        return stats

    def format_stats(self, stats: dict, start_date: str, end_date: str) -> str:
        """Format stats as a readable summary string."""
        lines = [
            f"Meeting Statistics: {start_date} to {end_date}",
            "=" * 50,
            f"  Total meetings: {stats['total_meetings']}",
            f"  Total hours in meetings: {stats['total_hours']}h",
            f"  Average duration: {stats['avg_duration_minutes']}m",
            f"  Online meetings: {stats['online_meetings']}",
            f"  In-person meetings: {stats['in_person_meetings']}",
        ]

        if stats["all_day_events"]:
            lines.append(f"  All-day events: {stats['all_day_events']}")

        lines.append("")
        lines.append("By day of week:")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            count = stats["by_day_of_week"].get(day, 0)
            if count:
                bar = "#" * count
                lines.append(f"  {day:<12} {count:>3}  {bar}")

        if stats["top_attendees"]:
            lines.append("")
            lines.append("Top attendees:")
            for a in stats["top_attendees"][:10]:
                lines.append(f"  {a['name']:<35} {a['count']:>3} meetings")

        return "\n".join(lines)
