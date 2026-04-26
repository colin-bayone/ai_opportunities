#!/usr/bin/env python3
"""
Hook: fido-workflow
Event: Stop
Purpose: Enforce fido workflow compliance.

Checks performed (only when fido is active):
1. SKILL.md was read before operating
2. check_deps.py was run (dependency verification)
3. Auth was checked before API calls
4. Output files have matching metadata JSON
5. Token cache files are gitignored

Skill-scoped: Only fires when fido was invoked
via the Skill tool. Exits 0 immediately otherwise.

Exit codes:
  0 = Allow (checks pass or skill not active)
  2 = Block (workflow violation detected)
"""

import json
import sys
import os
import glob as glob_mod
from pathlib import Path


SKILL_MD_PATH = ".claude/skills/fido/SKILL.md"
SCRIPTS_DIR = ".claude/skills/fido/scripts"
OUTPUT_DIR = "claude/meeting_transcripts"


def find_transcript(input_data: dict) -> str | None:
    """Find the transcript file for this session."""
    transcript_path = input_data.get("transcript_path")
    if transcript_path and os.path.exists(transcript_path):
        return transcript_path

    session_id = input_data.get("session_id", "")
    if not session_id:
        return None

    patterns = [
        f"{os.environ.get('HOME', '')}/.claude/projects/*/sessions/{session_id}/transcript.jsonl",
        f"{os.environ.get('HOME', '')}/.claude/projects/*/{session_id}/transcript.jsonl",
    ]
    for pattern in patterns:
        matches = glob_mod.glob(pattern)
        if matches:
            return matches[0]
    return None


def check_skill_invoked(transcript_path: str) -> bool:
    """Check if fido was invoked via Skill tool."""
    try:
        with open(transcript_path, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get("type") == "tool_use" and entry.get("name") == "Skill":
                        skill_input = entry.get("input", {})
                        skill_name = skill_input.get("skill", "").lower()
                        if "fido" in skill_name:
                            return True
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return False


def check_skill_md_read(transcript_path: str) -> bool:
    """Verify SKILL.md was read in this session."""
    try:
        with open(transcript_path, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get("type") == "tool_use" and entry.get("name") == "Read":
                        file_path = entry.get("input", {}).get("file_path", "")
                        if "fido/SKILL.md" in file_path:
                            return True
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return False


def check_deps_verified(transcript_path: str) -> bool:
    """Verify check_deps.py was run before any other script."""
    deps_checked = False
    other_script_run = False

    try:
        with open(transcript_path, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get("type") == "tool_use" and entry.get("name") == "Bash":
                        command = entry.get("input", {}).get("command", "")
                        if "check_deps.py" in command:
                            deps_checked = True
                        elif "fido/scripts/" in command and "check_deps" not in command:
                            if not deps_checked:
                                other_script_run = True
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass

    # Fail only if other scripts ran without deps being checked first
    if other_script_run and not deps_checked:
        return False
    return True


def check_auth_verified(transcript_path: str) -> bool:
    """Verify auth was checked before fetch/list operations."""
    auth_checked = False
    api_call_made = False

    try:
        with open(transcript_path, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    if entry.get("type") == "tool_use" and entry.get("name") == "Bash":
                        command = entry.get("input", {}).get("command", "")
                        if "check-auth" in command or "auth_bootstrap" in command:
                            auth_checked = True
                        elif ("main.py fetch" in command or "main.py list" in command):
                            if not auth_checked:
                                api_call_made = True
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass

    if api_call_made and not auth_checked:
        return False
    return True


def check_output_has_metadata(project_dir: Path) -> list[str]:
    """Verify every transcript file has a matching metadata JSON."""
    issues = []
    output_dir = project_dir / OUTPUT_DIR

    if not output_dir.exists():
        return []

    for subdir in output_dir.iterdir():
        if not subdir.is_dir() or subdir.name in (".", ".."):
            continue
        # Skip non-date folders (contacts.json, token files, etc.)
        if not subdir.name[0:4].isdigit():
            continue

        txt_files = list(subdir.glob("*.txt"))
        vtt_files = list(subdir.glob("*.vtt"))
        transcript_files = txt_files + vtt_files

        for tf in transcript_files:
            # Derive expected meta path: file_01.txt -> file_01_meta.json
            stem = tf.stem  # e.g., 2026-04-16_ambar-singh_01
            meta_path = tf.parent / f"{stem}_meta.json"
            if not meta_path.exists():
                # Only flag .txt files, not .vtt (vtt is backup)
                if tf.suffix == ".txt":
                    issues.append(
                        f"Missing metadata: {meta_path.relative_to(project_dir)}"
                    )

    return issues


def check_gitignore(project_dir: Path) -> list[str]:
    """Warn if token files might be tracked by git."""
    issues = []
    token_cache = project_dir / OUTPUT_DIR / "token_cache.json"
    token_meta = project_dir / OUTPUT_DIR / "token_metadata.json"

    if not token_cache.exists() and not token_meta.exists():
        return []

    # Check if .gitignore covers these
    gitignore_path = project_dir / ".gitignore"
    if gitignore_path.exists():
        gitignore_content = gitignore_path.read_text()
        # Check for common patterns that would cover these files
        covered = False
        for pattern in ["token_cache.json", "token_metadata.json",
                        "claude/meeting_transcripts/", "claude/"]:
            if pattern in gitignore_content:
                covered = True
                break
        if not covered:
            issues.append(
                "token_cache.json and token_metadata.json may not be gitignored. "
                "Add 'claude/meeting_transcripts/token_cache.json' and "
                "'claude/meeting_transcripts/token_metadata.json' to .gitignore."
            )

    return issues


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    # Prevent recursion
    if input_data.get("stop_hook_active", False):
        sys.exit(0)

    # Find transcript
    transcript_path = find_transcript(input_data)
    if not transcript_path:
        sys.exit(0)

    # Skill-scoped: only fire if fido was invoked
    if not check_skill_invoked(transcript_path):
        sys.exit(0)

    project_dir = Path(input_data.get("cwd", "."))
    issues = []

    # Check 1: SKILL.md was read
    if not check_skill_md_read(transcript_path):
        issues.append(
            "fido SKILL.md was not read before operating. "
            "Read .claude/skills/fido/SKILL.md first."
        )

    # Check 2: Dependencies were verified
    if not check_deps_verified(transcript_path):
        issues.append(
            "Scripts were run without verifying dependencies first. "
            "Run: python3 .claude/skills/fido/scripts/check_deps.py"
        )

    # Check 3: Auth was checked before API calls
    if not check_auth_verified(transcript_path):
        issues.append(
            "API operations were attempted without checking auth first. "
            "Run: python3 .claude/skills/fido/scripts/main.py check-auth --env-file <path>"
        )

    # Check 4: Output files have metadata
    meta_issues = check_output_has_metadata(project_dir)
    issues.extend(meta_issues)

    # Check 5: Token files are gitignored
    gitignore_issues = check_gitignore(project_dir)
    issues.extend(gitignore_issues)

    if issues:
        msg = "fido workflow violations:\n"
        for i, issue in enumerate(issues, 1):
            msg += f"  {i}. {issue}\n"
        msg += "\nResolve these before proceeding."
        print(msg, file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
