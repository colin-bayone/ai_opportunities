#!/usr/bin/env python3
"""
Get current date and time for use in skill context.

This script provides the current date/time to ensure:
1. Web searches are relative to current date
2. Library freshness checks use accurate dates
3. Research is always time-aware

Usage:
    python get_current_date.py
    python get_current_date.py --format iso
    python get_current_date.py --format search  # For web search context
"""

import argparse
from datetime import datetime, timedelta


def get_date_context(format_type: str = "full") -> dict:
    """Return date context for skill operations."""
    now = datetime.now()
    one_year_ago = now - timedelta(days=365)

    context = {
        "current_date": now.strftime("%Y-%m-%d"),
        "current_time": now.strftime("%H:%M:%S"),
        "current_year": now.year,
        "current_month": now.strftime("%B %Y"),
        "one_year_ago": one_year_ago.strftime("%Y-%m-%d"),
        "iso_timestamp": now.isoformat(),
        "search_context": f"in {now.year}",
        "freshness_cutoff": one_year_ago.strftime("%Y-%m-%d"),
    }
    return context


def main():
    parser = argparse.ArgumentParser(description="Get current date context for skill operations")
    parser.add_argument(
        "--format",
        choices=["full", "iso", "search", "freshness", "json"],
        default="full",
        help="Output format type"
    )
    args = parser.parse_args()

    context = get_date_context()

    if args.format == "full":
        print(f"Current Date: {context['current_date']}")
        print(f"Current Time: {context['current_time']}")
        print(f"Current Year: {context['current_year']}")
        print(f"One Year Ago: {context['one_year_ago']}")
        print(f"Search Context: {context['search_context']}")
        print(f"Library Freshness Cutoff: {context['freshness_cutoff']}")
        print()
        print("For web searches, use phrases like:")
        print(f'  "Django best practices {context["current_year"]}"')
        print(f'  "HTMX Django {context["current_year"]}"')
        print(f'  "after:{context["one_year_ago"]}"')
    elif args.format == "iso":
        print(context["iso_timestamp"])
    elif args.format == "search":
        print(f"Current date: {context['current_date']}")
        print(f"Use search terms like: '{context['current_year']}' or 'after:{context['one_year_ago']}'")
    elif args.format == "freshness":
        print(f"Library must have commits after: {context['one_year_ago']}")
        print(f"Library must have version >= 1.0.0")
    elif args.format == "json":
        import json
        print(json.dumps(context, indent=2))


if __name__ == "__main__":
    main()
