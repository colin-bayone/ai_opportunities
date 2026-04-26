#!/usr/bin/env python3
"""
Meeting Transcript Skill — CLI Orchestrator.

Subcommands:
  auth        Run authentication bootstrap
  check-auth  Check current auth status
  fetch       Fetch transcripts for meetings
  list        List meetings (no transcript fetch)
  contacts    Manage contact glossary

Usage:
  python3 main.py check-auth --env-file /path/to/.env
  python3 main.py fetch --env-file /path/to/.env --person "ambar@bay.com" --last
  python3 main.py fetch --env-file /path/to/.env --start-date 2026-04-01 --end-date 2026-04-16
  python3 main.py list --env-file /path/to/.env --start-date 2026-04-10 --end-date 2026-04-16
  python3 main.py contacts --list
  python3 main.py contacts --add "Ambar Singh" "ambar@bayone.com"
  python3 main.py contacts --lookup "Ambar"
"""

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Ensure sibling modules are importable
sys.path.insert(0, str(Path(__file__).parent))

from graph_client import GraphClient, check_auth_status, get_output_dir, get_token_metadata_path, _load_token_metadata
from calendar_search import CalendarSearch
from transcript_fetcher import TranscriptFetcher, TranscriptNotAvailable
from contacts import ContactsManager


def cmd_check_auth(args):
    """Check authentication status."""
    status = check_auth_status(args.env_file)

    if status.get("authenticated"):
        print("Authentication: OK")
        print(f"  Method: {status.get('auth_method', 'unknown')}")
        print(f"  Last authenticated: {status.get('last_authenticated', 'unknown')}")
        if status.get("days_until_expiry") is not None:
            print(f"  Refresh token expires in: ~{status['days_until_expiry']} days")
        if status.get("token_valid"):
            print("  Token acquisition: SUCCESS")
        if status.get("warning"):
            print(f"  WARNING: {status['warning']}")
    else:
        print(f"Authentication: FAILED")
        print(f"  Error: {status.get('error', 'Unknown')}")
        sys.exit(1)


def cmd_fetch(args):
    """Fetch transcripts for meetings."""
    client = GraphClient(env_file=args.env_file)
    search = CalendarSearch(client)
    fetcher = TranscriptFetcher(client)
    contacts = ContactsManager()

    # Resolve person email if provided
    person_email = args.person
    person_name = None
    if person_email and "@" not in person_email:
        # It's a name, look up in contacts
        resolved = contacts.lookup(person_email)
        if resolved:
            person_name = person_email
            person_email = resolved
            print(f"Resolved '{person_name}' -> {person_email}")
        else:
            print(f"ERROR: No contact found for '{person_email}'.")
            print("Please provide an email address or add the contact first:")
            print(f"  python3 main.py contacts --add \"{person_email}\" \"email@example.com\"")
            sys.exit(1)
    elif person_email:
        # Extract name from contacts if available
        for name, email in contacts.list_all().items():
            if email == person_email.lower():
                person_name = name
                break

    # Determine date range
    if args.last:
        days_back = int(
            client.config.get("default_search_days", 30)
        )
        end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        start_date = (
            datetime.now(timezone.utc) - timedelta(days=days_back)
        ).strftime("%Y-%m-%d")
        print(f"Searching last {days_back} days for most recent meeting...")
    elif args.start_date and args.end_date:
        start_date = args.start_date
        end_date = args.end_date
        print(f"Searching {start_date} to {end_date}...")
    elif args.start_date:
        start_date = args.start_date
        end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        print(f"Searching {start_date} to today...")
    else:
        # Default: last 7 days
        end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        start_date = (
            datetime.now(timezone.utc) - timedelta(days=7)
        ).strftime("%Y-%m-%d")
        print(f"No date range specified. Searching last 7 days...")

    # Determine exclusive/inclusive mode
    exclusive = args.exclusive or args.only
    if exclusive and not person_email:
        print("ERROR: --exclusive/--only requires --person to be specified.")
        sys.exit(1)

    mode_label = "exclusive (1:1 only)" if exclusive else "inclusive (any meeting with them)"
    if person_email:
        print(f"Mode: {mode_label}")

    # Find meetings
    if person_email:
        print(f"Looking for meetings with: {person_email}")
        # For exclusive mode, get user's email from token metadata
        my_email = None
        if exclusive:
            meta_path = get_token_metadata_path(args.env_file)
            metadata = _load_token_metadata(meta_path)
            my_email = metadata.get("user_email")
            if not my_email:
                print("ERROR: User email not found in token metadata.")
                print("Re-run auth_bootstrap.py to store your email.")
                sys.exit(1)

        meetings = search.find_meetings_with_person(
            email=person_email, start_date=start_date, end_date=end_date,
            exclusive=exclusive, my_email=my_email,
        )
    else:
        print("Looking for all online meetings with potential transcripts...")
        meetings = search.find_meetings_in_range(
            start_date=start_date, end_date=end_date, online_only=True
        )

    if not meetings:
        print("\nNo meetings found in this date range.")
        sys.exit(0)

    # If --last, only take the most recent
    if args.last and meetings:
        meetings = [meetings[-1]]
        print(f"Found most recent: {meetings[0]['subject']}")

    print(f"\nFound {len(meetings)} meeting(s). Fetching transcripts...\n")

    # Track same-day meetings for numbering
    day_person_counts = {}
    results = {"fetched": 0, "no_transcript": 0, "errors": 0, "skipped": 0, "files": []}

    for meeting in meetings:
        subject = meeting.get("subject", "(No subject)")
        start = meeting.get("start_datetime", "?")

        # Determine sequence number for same-day meetings
        # Handle Graph API datetime format (trailing Z, 7-digit microseconds)
        # which Python 3.10 fromisoformat doesn't support
        try:
            cleaned = start.rstrip("Z")
            if "." in cleaned:
                base, frac = cleaned.split(".", 1)
                cleaned = f"{base}.{frac[:6]}"
            dt = datetime.fromisoformat(cleaned)
            date_key = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_key = "unknown"

        slug_key = f"{date_key}_{person_name or subject}"
        day_person_counts[slug_key] = day_person_counts.get(slug_key, 0) + 1
        seq_num = day_person_counts[slug_key]

        join_url = meeting.get("join_url", "")
        if not join_url:
            print(f"  SKIP: '{subject}' — not an online meeting (no join URL)")
            continue

        # Check if already downloaded
        existing = fetcher.is_already_downloaded(meeting, person_name, seq_num)
        if existing:
            results["skipped"] += 1
            print(f"  SKIP: '{subject}' ({start[:16]}) — already downloaded at {existing}")
            continue

        print(f"  Fetching: '{subject}' ({start[:16]})...", end=" ")

        try:
            transcript_data = fetcher.fetch(join_url=join_url, event_date=date_key)
            saved = fetcher.save_transcript(
                transcript_data=transcript_data,
                meeting_info=meeting,
                person_name=person_name,
                sequence_num=seq_num,
            )
            results["fetched"] += 1
            results["files"].append(saved)
            print(
                f"OK ({transcript_data['utterance_count']} utterances, "
                f"{transcript_data['word_count']} words)"
            )

        except TranscriptNotAvailable:
            results["no_transcript"] += 1
            timing_msg = fetcher.check_transcript_timing(meeting)
            if timing_msg:
                print(f"NO TRANSCRIPT — {timing_msg}")
            else:
                print("NO TRANSCRIPT — transcription was not enabled")

        except Exception as e:
            results["errors"] += 1
            print(f"ERROR — {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"Results:")
    print(f"  Transcripts fetched: {results['fetched']}")
    if results["skipped"]:
        print(f"  Already downloaded (skipped): {results['skipped']}")
    print(f"  No transcript available: {results['no_transcript']}")
    if results["errors"]:
        print(f"  Errors: {results['errors']}")

    if results["files"]:
        print(f"\nFiles saved to:")
        folders = set(f["folder"] for f in results["files"])
        for folder in sorted(folders):
            print(f"  {folder}/")

    # Output JSON summary for Claude to parse
    print(f"\n---JSON_SUMMARY---")
    print(json.dumps(results, indent=2))


def cmd_list(args):
    """List meetings in a date range (no transcript fetch)."""
    client = GraphClient(env_file=args.env_file)
    search = CalendarSearch(client)

    if not args.start_date:
        args.start_date = (
            datetime.now(timezone.utc) - timedelta(days=7)
        ).strftime("%Y-%m-%d")
    if not args.end_date:
        args.end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"Listing meetings from {args.start_date} to {args.end_date}...\n")

    meetings = search.list_meetings(args.start_date, args.end_date)
    table = search.format_meetings_table(meetings)
    print(table)

    # Save to file if requested
    if args.save:
        output_dir = get_output_dir(args.env_file)
        exports_dir = output_dir / "exports"
        exports_dir.mkdir(parents=True, exist_ok=True)

        save_format = args.format or "csv"
        filename = f"{args.start_date}_to_{args.end_date}_meetings.{save_format}"
        if save_format == "md":
            filename = f"{args.start_date}_to_{args.end_date}_meetings.md"

        save_path = exports_dir / filename

        if save_format == "csv":
            content = search.format_meetings_csv(meetings)
        elif save_format == "md":
            content = search.format_meetings_markdown(meetings)
        else:
            content = search.format_meetings_csv(meetings)

        save_path.write_text(content, encoding="utf-8")
        print(f"\nSaved to: {save_path}")

    # Also output JSON for Claude
    print(f"\n---JSON_SUMMARY---")
    print(json.dumps({"meetings": meetings, "count": len(meetings)}, indent=2, default=str))


def cmd_stats(args):
    """Show meeting summary statistics."""
    client = GraphClient(env_file=args.env_file)
    search = CalendarSearch(client)

    if not args.start_date:
        args.start_date = (
            datetime.now(timezone.utc) - timedelta(days=30)
        ).strftime("%Y-%m-%d")
    if not args.end_date:
        args.end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"Gathering stats from {args.start_date} to {args.end_date}...\n")

    meetings = search.list_meetings(args.start_date, args.end_date)
    stats = search.compute_stats(meetings)
    formatted = search.format_stats(stats, args.start_date, args.end_date)
    print(formatted)

    print(f"\n---JSON_SUMMARY---")
    print(json.dumps(stats, indent=2, default=str))


def cmd_upcoming(args):
    """Show upcoming meetings."""
    client = GraphClient(env_file=args.env_file)
    search = CalendarSearch(client)

    days = args.days or 7
    start_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    end_date = (datetime.now(timezone.utc) + timedelta(days=days)).strftime("%Y-%m-%d")

    print(f"Upcoming meetings: next {days} days ({start_date} to {end_date})\n")

    meetings = search.list_meetings(start_date, end_date)

    if not meetings:
        print("No upcoming meetings.")
        return

    # Group by day
    from collections import defaultdict
    by_day = defaultdict(list)
    for m in meetings:
        date_str, _ = search._parse_dt_clean(m.get("start_datetime", ""))
        by_day[date_str].append(m)

    for day in sorted(by_day.keys()):
        try:
            dt = datetime.fromisoformat(day)
            day_label = dt.strftime("%A, %B %d")
        except (ValueError, TypeError):
            day_label = day

        day_meetings = by_day[day]
        print(f"--- {day_label} ({len(day_meetings)} meetings) ---")

        for m in day_meetings:
            _, time_str = search._parse_dt_clean(m["start_datetime"])
            dur = m.get("duration_minutes", 0)
            subject = m["subject"]
            online = " [Online]" if m.get("is_online_meeting") else ""

            if m.get("is_all_day"):
                print(f"  All day   {subject}")
            else:
                attendee_names = [a["name"] for a in m.get("attendees", [])[:4] if a.get("name")]
                att_str = f" — {', '.join(attendee_names)}" if attendee_names else ""
                print(f"  {time_str}  {dur}m  {subject}{online}{att_str}")

        print()

    # Quick stats
    non_allday = [m for m in meetings if not m.get("is_all_day")]
    total_hours = sum(m.get("duration_minutes", 0) for m in non_allday) / 60
    online_count = sum(1 for m in non_allday if m.get("is_online_meeting"))
    print(f"Summary: {len(non_allday)} meetings, {total_hours:.1f}h total, {online_count} online")

    print(f"\n---JSON_SUMMARY---")
    print(json.dumps({"days": days, "meetings": meetings, "count": len(meetings)}, indent=2, default=str))


def cmd_search(args):
    """Search meetings by subject/name, optionally fetch transcript."""
    client = GraphClient(env_file=args.env_file)
    search = CalendarSearch(client)

    if not args.start_date:
        args.start_date = (
            datetime.now(timezone.utc) - timedelta(days=7)
        ).strftime("%Y-%m-%d")
    if not args.end_date:
        args.end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"Searching for '{args.query}' from {args.start_date} to {args.end_date}...\n")

    meetings = search.find_meetings_by_subject(
        query=args.query, start_date=args.start_date, end_date=args.end_date
    )

    if not meetings:
        print(f"No meetings found matching '{args.query}'.")
        sys.exit(0)

    # Show numbered list for selection
    for i, m in enumerate(meetings):
        try:
            cleaned = m["start_datetime"].rstrip("Z")
            if "." in cleaned:
                base, frac = cleaned.split(".", 1)
                cleaned = f"{base}.{frac[:6]}"
            dt = datetime.fromisoformat(cleaned)
            date_str = dt.strftime("%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            date_str = "?"
        attendee_names = [a["name"] or a["email"] for a in m.get("attendees", [])[:5]]
        online = "Online" if m.get("is_online_meeting") else "In-person"
        print(f"  [{i+1}] {m['subject']}")
        print(f"      {date_str} | {m.get('duration_minutes', 0)}m | {online}")
        print(f"      Attendees: {', '.join(attendee_names)}")
        print()

    print(f"Total: {len(meetings)} meeting(s)")

    # If --fetch, prompt for selection
    if args.fetch:
        if len(meetings) == 1:
            choice = 1
            print(f"\nOnly one match — selecting [{choice}].")
        else:
            try:
                choice = int(input(f"\nEnter number to fetch transcript [1-{len(meetings)}]: "))
            except (ValueError, EOFError):
                print("Invalid selection. Aborting.")
                sys.exit(1)

        if choice < 1 or choice > len(meetings):
            print(f"Invalid selection: {choice}. Must be 1-{len(meetings)}.")
            sys.exit(1)

        meeting = meetings[choice - 1]
        join_url = meeting.get("join_url", "")
        if not join_url:
            print("This meeting is not an online meeting — no transcript available.")
            sys.exit(1)

        # Get event date for transcript matching
        try:
            cleaned = meeting["start_datetime"].rstrip("Z")
            if "." in cleaned:
                base, frac = cleaned.split(".", 1)
                cleaned = f"{base}.{frac[:6]}"
            event_date = datetime.fromisoformat(cleaned).strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            event_date = None

        print(f"\nFetching transcript for '{meeting['subject']}'...")

        fetcher = TranscriptFetcher(client)
        try:
            transcript_data = fetcher.fetch(join_url=join_url, event_date=event_date)
            # Use subject slug for folder name
            saved = fetcher.save_transcript(
                transcript_data=transcript_data,
                meeting_info=meeting,
                person_name=None,
                sequence_num=1,
            )
            print(
                f"OK ({transcript_data['utterance_count']} utterances, "
                f"{transcript_data['word_count']} words)"
            )
            print(f"\nSaved to: {saved['folder']}/")

            print(f"\n---JSON_SUMMARY---")
            print(json.dumps({"fetched": 1, "files": [saved]}, indent=2))

        except TranscriptNotAvailable as e:
            timing_msg = fetcher.check_transcript_timing(meeting)
            if timing_msg:
                print(f"NO TRANSCRIPT — {timing_msg}")
            else:
                print(f"NO TRANSCRIPT — {e}")

        except Exception as e:
            print(f"ERROR — {e}")
    else:
        print(f"\n---JSON_SUMMARY---")
        print(json.dumps({"query": args.query, "meetings": meetings, "count": len(meetings)}, indent=2, default=str))


def cmd_contacts(args):
    """Manage contacts glossary."""
    mgr = ContactsManager()

    if args.lookup:
        email = mgr.lookup(args.lookup)
        if email:
            print(json.dumps({"name": args.lookup, "email": email}))
        else:
            print(json.dumps({"name": args.lookup, "email": None, "error": "not found"}))
            sys.exit(1)

    elif args.add:
        name, email = args.add
        mgr.add(name, email)

    elif args.remove:
        if mgr.remove(args.remove):
            print(f"Removed: {args.remove}")
        else:
            print(f"Not found: {args.remove}")
            sys.exit(1)

    elif args.list:
        print(mgr.list_formatted())


def main():
    parser = argparse.ArgumentParser(
        description="Meeting Transcript Skill CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # check-auth
    auth_parser = subparsers.add_parser("check-auth", help="Check authentication status")
    auth_parser.add_argument("--env-file", required=True, help="Path to .env file")

    # fetch
    fetch_parser = subparsers.add_parser("fetch", help="Fetch meeting transcripts")
    fetch_parser.add_argument("--env-file", required=True, help="Path to .env file")
    fetch_parser.add_argument("--person", help="Person email or name from contacts")
    fetch_parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    fetch_parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    fetch_parser.add_argument(
        "--last", action="store_true",
        help="Fetch only the most recent meeting"
    )
    fetch_parser.add_argument(
        "--exclusive", action="store_true",
        help="Only meetings with JUST you and the specified person (1:1s only)"
    )
    fetch_parser.add_argument(
        "--inclusive", action="store_true",
        help="Any meeting where the person is an attendee (default behavior)"
    )
    fetch_parser.add_argument(
        "--only", action="store_true",
        help="Shorthand for --exclusive"
    )

    # stats
    stats_parser = subparsers.add_parser("stats", help="Meeting summary statistics")
    stats_parser.add_argument("--env-file", required=True, help="Path to .env file")
    stats_parser.add_argument("--start-date", help="Start date (default: 30 days ago)")
    stats_parser.add_argument("--end-date", help="End date (default: today)")

    # upcoming
    upcoming_parser = subparsers.add_parser("upcoming", help="Show upcoming meetings")
    upcoming_parser.add_argument("--env-file", required=True, help="Path to .env file")
    upcoming_parser.add_argument("--days", type=int, default=7, help="Number of days ahead (default: 7)")

    # search
    search_parser = subparsers.add_parser("search", help="Search meetings by subject/name")
    search_parser.add_argument("--env-file", required=True, help="Path to .env file")
    search_parser.add_argument("--query", required=True, help="Search term to match in meeting subjects")
    search_parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    search_parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    search_parser.add_argument(
        "--fetch", action="store_true",
        help="After finding matches, select one and fetch its transcript"
    )

    # list
    list_parser = subparsers.add_parser("list", help="List meetings (no transcript fetch)")
    list_parser.add_argument("--env-file", required=True, help="Path to .env file")
    list_parser.add_argument("--start-date", help="Start date (YYYY-MM-DD)")
    list_parser.add_argument("--end-date", help="End date (YYYY-MM-DD)")
    list_parser.add_argument(
        "--save", action="store_true",
        help="Save meeting list to a file"
    )
    list_parser.add_argument(
        "--format", choices=["csv", "md"], default=None,
        help="Export format when using --save (default: csv)"
    )

    # contacts
    contacts_parser = subparsers.add_parser("contacts", help="Manage contact glossary")
    contacts_group = contacts_parser.add_mutually_exclusive_group(required=True)
    contacts_group.add_argument("--lookup", metavar="NAME", help="Look up by name")
    contacts_group.add_argument(
        "--add", nargs=2, metavar=("NAME", "EMAIL"), help="Add a contact"
    )
    contacts_group.add_argument("--remove", metavar="NAME", help="Remove a contact")
    contacts_group.add_argument("--list", action="store_true", help="List all contacts")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "check-auth":
        cmd_check_auth(args)
    elif args.command == "fetch":
        cmd_fetch(args)
    elif args.command == "stats":
        cmd_stats(args)
    elif args.command == "upcoming":
        cmd_upcoming(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "contacts":
        cmd_contacts(args)


if __name__ == "__main__":
    main()
