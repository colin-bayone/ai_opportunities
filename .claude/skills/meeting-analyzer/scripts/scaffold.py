#!/usr/bin/env python3
"""
Scaffold script for meeting-analyzer skill.
Creates session folder structure for meeting analysis.

Usage:
    python3 scaffold.py <session-name> <target-path>
    python3 scaffold.py cisco-meetings claude/2026-02-17_cisco-meeting-summaries

Arguments:
    session-name: Descriptive name for the session (used in confirmation)
    target-path: Where to create the folder structure (relative to project root)
"""

import sys
import os
from pathlib import Path


def create_session_structure(target_path: str) -> dict:
    """Create the session folder structure and return status."""

    base = Path(target_path)

    # Folders to create
    folders = [
        base / "source",      # Raw transcripts
        base / "summaries",   # Optional roll-ups
    ]

    created = []
    existed = []

    for folder in folders:
        if folder.exists():
            existed.append(str(folder))
        else:
            folder.mkdir(parents=True, exist_ok=True)
            created.append(str(folder))

    return {
        "base": str(base),
        "created": created,
        "existed": existed,
        "success": True
    }


def print_structure(base_path: str):
    """Print the expected structure."""
    print(f"""
Session folder created: {base_path}/

Structure:
├── source/              # Place raw transcripts here
├── meeting1_<participants>/
│   ├── 00_meeting_breakdown.md
│   ├── 01_speaker_notes.md
│   ├── 02_crossover_analysis.md  (if applicable)
│   └── 03_sentiment_and_relationship.md
├── meeting2_<participants>/
│   └── ...
└── summaries/           # Optional roll-ups

Next steps:
1. Copy transcript files to {base_path}/source/
2. Invoke /meeting-analyzer or continue with analysis
""")


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 scaffold.py <session-name> <target-path>")
        print("Example: python3 scaffold.py cisco-meetings claude/2026-02-17_cisco-meetings")
        sys.exit(1)

    session_name = sys.argv[1]
    target_path = sys.argv[2]

    print(f"Creating session folder for: {session_name}")
    print(f"Location: {target_path}")
    print()

    result = create_session_structure(target_path)

    if result["created"]:
        print(f"Created {len(result['created'])} folders:")
        for folder in result["created"]:
            print(f"  + {folder}")

    if result["existed"]:
        print(f"\nAlready existed ({len(result['existed'])} folders):")
        for folder in result["existed"]:
            print(f"  = {folder}")

    print_structure(result["base"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
