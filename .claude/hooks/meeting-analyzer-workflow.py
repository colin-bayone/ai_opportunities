#!/usr/bin/env python3
"""
Stop hook for meeting-analyzer skill.

Enforces the complete workflow was followed:
1. Context discovery (00_context_discovery.md exists)
2. Transcription handling (## Transcription section in breakdown)
3. Required documents created (pattern-matched, not hardcoded names)
4. HTML versions generated for all markdown docs

ONLY fires when the skill is active (marker file exists).
"""

import json
import sys
from pathlib import Path
import re


# Base folder for all meeting-analyzer output
MEETING_ANALYZER_DIR = "claude/meeting-analyzer"

# Marker file indicating skill is actively being used
ACTIVE_MARKER = ".meeting-analysis-active"

# Required document patterns (match on suffix, any number prefix)
REQUIRED_DOC_PATTERNS = [
    r"\d+_meeting_breakdown\.md$",
    r"\d+_speaker_notes\.md$",
    r"\d+_sentiment.*\.md$",
]

# Context discovery file (proof Explore agent was used)
CONTEXT_DISCOVERY_FILE = "00_context_discovery.md"


def is_skill_active(project_dir: Path) -> bool:
    """Check if meeting-analyzer skill is currently active."""
    marker = project_dir / MEETING_ANALYZER_DIR / ACTIVE_MARKER
    return marker.exists()


def find_meeting_folders(project_dir: Path) -> list[Path]:
    """Find all meeting folders in the dedicated meeting-analyzer directory."""
    analyzer_dir = project_dir / MEETING_ANALYZER_DIR
    if not analyzer_dir.exists():
        return []

    meeting_folders = []
    for item in analyzer_dir.iterdir():
        if item.is_dir() and item.name.startswith("meeting_"):
            meeting_folders.append(item)
    return meeting_folders


def check_context_discovery(meeting_folder: Path) -> bool:
    """Check if context discovery file exists (proof Explore agent was used)."""
    context_file = meeting_folder / CONTEXT_DISCOVERY_FILE
    if not context_file.exists():
        return False
    # Must have actual content, not just empty file
    return len(context_file.read_text().strip()) > 50


def check_required_docs(meeting_folder: Path) -> list[str]:
    """Check if all required document types exist (pattern-matched). Returns missing types."""
    files = [f.name for f in meeting_folder.iterdir() if f.is_file()]
    missing = []

    for pattern in REQUIRED_DOC_PATTERNS:
        if not any(re.search(pattern, f) for f in files):
            # Extract human-readable name from pattern
            doc_type = pattern.replace(r"\d+_", "").replace(r"\.md$", ".md").replace("\\", "").replace(".*", "")
            missing.append(doc_type)

    return missing


def check_transcription_section(meeting_folder: Path) -> bool:
    """Check if meeting breakdown contains a Transcription section header."""
    # Find the meeting breakdown file (any number prefix)
    breakdown = None
    for f in meeting_folder.iterdir():
        if re.search(r"\d+_meeting_breakdown\.md$", f.name):
            breakdown = f
            break

    if not breakdown or not breakdown.exists():
        return False

    content = breakdown.read_text()
    # Look for ## Transcription or similar section header
    return bool(re.search(r"^#{1,3}\s+[Tt]ranscription", content, re.MULTILINE))


def check_html_exists(meeting_folder: Path) -> list[str]:
    """Check if all markdown docs have corresponding HTML. Returns missing files."""
    missing = []

    for md_file in meeting_folder.glob("*.md"):
        html_file = md_file.with_suffix(".html")
        if not html_file.exists():
            missing.append(f"{md_file.stem}.html")

    return missing


def main():
    data = json.load(sys.stdin)

    # Prevent infinite loops
    if data.get("stop_hook_active", False):
        sys.exit(0)

    project_dir = Path(data.get("cwd", "."))

    # CRITICAL: Only fire when skill is active (marker file exists)
    if not is_skill_active(project_dir):
        sys.exit(0)

    # Find meeting folders in dedicated directory
    meeting_folders = find_meeting_folders(project_dir)

    if not meeting_folders:
        # Skill is active but no meeting folders yet - probably just starting
        sys.exit(0)

    issues = []

    for folder in meeting_folders:
        folder_name = folder.name

        # Check 1: Context discovery file exists
        if not check_context_discovery(folder):
            issues.append(f"{folder_name}: Missing {CONTEXT_DISCOVERY_FILE}. Spawn Explore agent to gather project context and write findings to this file.")

        # Check 2: All required document types exist
        missing_docs = check_required_docs(folder)
        if missing_docs:
            issues.append(f"{folder_name}: Missing required documents: {', '.join(missing_docs)}")

        # Check 3: Transcription section present
        if not check_transcription_section(folder):
            issues.append(f"{folder_name}: Missing '## Transcription' section in meeting breakdown. Document transcription errors or note that none were found.")

        # Check 4: HTML versions exist for all markdown
        missing_html = check_html_exists(folder)
        if missing_html:
            issues.append(f"{folder_name}: Missing HTML versions: {', '.join(missing_html)}")

    if issues:
        issue_list = "\n- ".join(issues)
        print(f"Meeting analysis workflow incomplete:\n- {issue_list}\n\nComplete all steps before finishing.", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
