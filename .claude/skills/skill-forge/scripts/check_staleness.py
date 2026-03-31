#!/usr/bin/env python3
"""
Skill-Forge Staleness Checker

Reads VERSION.md to determine when skill-forge was last updated.
Outputs a JSON report with staleness status and recommended action.

Usage:
    python3 .claude/skills/skill-forge/scripts/check_staleness.py

Exit codes:
    0 - Up to date (within threshold)
    1 - Stale (exceeds threshold, update recommended)
    2 - Error reading VERSION.md
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


def find_version_file() -> Path:
    """Find VERSION.md relative to this script's location."""
    script_dir = Path(__file__).resolve().parent
    version_file = script_dir.parent / "VERSION.md"
    if version_file.exists():
        return version_file

    # Fallback: try from cwd
    cwd_path = Path.cwd() / ".claude" / "skills" / "skill-forge" / "VERSION.md"
    if cwd_path.exists():
        return cwd_path

    return version_file  # Return expected path even if missing


def parse_version_md(content: str) -> dict:
    """Extract key fields from VERSION.md."""
    result = {
        "last_updated": None,
        "staleness_threshold_days": 30,
        "features_covered_through": None,
        "known_gaps": [],
    }

    # Extract Last Updated date
    match = re.search(r"\*\*Last Updated\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})", content)
    if match:
        result["last_updated"] = match.group(1)

    # Extract staleness threshold
    match = re.search(r"\*\*Staleness Threshold \(days\)\*\*\s*\|\s*(\d+)", content)
    if match:
        result["staleness_threshold_days"] = int(match.group(1))

    # Extract features covered through
    match = re.search(r"\*\*Features Covered Through\*\*\s*\|\s*(.+?)(?:\s*\|)?\s*$", content, re.MULTILINE)
    if match:
        result["features_covered_through"] = match.group(1).strip()

    # Extract known gaps
    gap_section = re.search(r"## Known Gaps.*?\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if gap_section:
        gaps = re.findall(r"- \*\*(\d{4}-\d{2}-\d{2})\*\*:\s*(.+)", gap_section.group(1))
        result["known_gaps"] = [{"date": g[0], "description": g[1]} for g in gaps]

    return result


def main():
    version_file = find_version_file()

    if not version_file.exists():
        print(json.dumps({
            "error": f"VERSION.md not found at {version_file}",
            "action": "Create VERSION.md by running the skill-forge-updater agent",
        }))
        sys.exit(2)

    content = version_file.read_text()
    info = parse_version_md(content)

    if not info["last_updated"]:
        print(json.dumps({
            "error": "Could not parse 'Last Updated' date from VERSION.md",
            "action": "Check VERSION.md format",
        }))
        sys.exit(2)

    last_updated = datetime.strptime(info["last_updated"], "%Y-%m-%d")
    today = datetime.now()
    days_since_update = (today - last_updated).days
    threshold = info["staleness_threshold_days"]
    is_stale = days_since_update > threshold

    report = {
        "last_updated": info["last_updated"],
        "days_since_update": days_since_update,
        "threshold_days": threshold,
        "is_stale": is_stale,
        "features_covered_through": info["features_covered_through"],
        "known_gaps_count": len(info["known_gaps"]),
        "known_gaps": info["known_gaps"][:5],  # Show first 5
        "recommendation": (
            f"STALE: Last updated {days_since_update} days ago (threshold: {threshold}). "
            "Run the skill-forge-updater agent to refresh references."
            if is_stale
            else f"OK: Updated {days_since_update} days ago (threshold: {threshold})."
        ),
    }

    print(json.dumps(report, indent=2))
    sys.exit(1 if is_stale else 0)


if __name__ == "__main__":
    main()
