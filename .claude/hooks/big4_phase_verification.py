#!/usr/bin/env python3
"""
Big4 Skill - Phase Verification Stop Hook

Verifies ALL PREVIOUS phases are complete before allowing current phase work.
Uses the "Check Previous Phases" pattern for cumulative verification.

Exit codes:
- 0: Allow (all previous phases verified)
- 2: Block (previous phase artifacts missing)
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def find_big4_session(project_dir: Path) -> Path | None:
    """Find the active big4 session folder."""
    claude_dir = project_dir / "claude"
    if not claude_dir.exists():
        return None

    # Look for big4 session folders
    sessions = []
    for folder in claude_dir.iterdir():
        if folder.is_dir() and "_big4_" in folder.name:
            state_file = folder / "state.json"
            if state_file.exists():
                sessions.append(folder)

    if not sessions:
        return None

    # Return most recent by folder name (date prefix)
    sessions.sort(key=lambda x: x.name, reverse=True)
    return sessions[0]


def get_phase_order() -> list[str]:
    """Return phases in required order."""
    return [
        "setup",
        "source_analysis",
        "critique",
        "rewrite",
        "comparison",
        "compliance",
        "quality_audit",
        "complete"
    ]


def get_required_artifacts(phase: str, session_dir: Path) -> list[tuple[Path, int]]:
    """
    Return list of (artifact_path, min_size) required for a phase.
    min_size is minimum character count to consider artifact valid.
    """
    artifacts = {
        "setup": [
            (session_dir / "source", 0),  # Directory exists
        ],
        "source_analysis": [
            (session_dir / "research" / "source_analysis.md", 500),
        ],
        "critique": [
            (session_dir / "planning" / "critique.md", 1000),
        ],
        "rewrite": [
            # Any file matching *_v*.md in planning/
            (session_dir / "planning", -1),  # Special handling
        ],
        "comparison": [
            (session_dir / "planning" / "version_comparison.md", 500),
        ],
        "compliance": [
            (session_dir / "planning" / "style_compliance.md", 100),
        ],
        "quality_audit": [
            (session_dir / "planning" / "quality_audit.md", -2),  # Special: must contain PASS
        ],
        "complete": [],  # No additional artifacts
    }
    return artifacts.get(phase, [])


def check_rewrite_exists(planning_dir: Path) -> bool:
    """Check if any versioned rewrite exists (_v2.md, _v3.md, etc.)."""
    if not planning_dir.exists():
        return False

    import re
    version_pattern = re.compile(r"_v\d+\.md$")

    for file in planning_dir.iterdir():
        if file.is_file() and version_pattern.search(file.name):
            if file.stat().st_size > 100:
                return True
    return False


def check_quality_audit_passed(audit_path: Path) -> tuple[bool, str]:
    """Check if quality audit contains a PASS verdict."""
    if not audit_path.exists():
        return False, f"Quality audit file missing: {audit_path}"

    content = audit_path.read_text()

    # Look for explicit PASS verdict
    import re
    pass_pattern = re.compile(r"(?:Verdict|Overall).*?:.*?\bPASS\b", re.IGNORECASE)
    if pass_pattern.search(content):
        return True, ""

    # Check if it explicitly says FAIL or NEEDS REVISION
    if re.search(r"Verdict.*?:.*?\b(FAIL|NEEDS\s+REVISION)\b", content, re.IGNORECASE):
        return False, "Quality audit verdict is FAIL or NEEDS REVISION - iterate on rewrite"

    return False, "Quality audit missing explicit PASS verdict"


def verify_artifact(artifact_path: Path, min_size: int) -> tuple[bool, str]:
    """
    Verify an artifact exists and meets size requirements.
    Returns (success, error_message).
    """
    # Special case: quality audit must contain PASS verdict
    if min_size == -2:
        return check_quality_audit_passed(artifact_path)

    # Special case: rewrite phase looks for any _v*.md file
    if min_size == -1:
        if check_rewrite_exists(artifact_path):
            return True, ""
        return False, f"No versioned rewrite found in {artifact_path}"

    # Directory check
    if min_size == 0:
        if artifact_path.exists() and artifact_path.is_dir():
            # Check directory has content
            if any(artifact_path.iterdir()):
                return True, ""
            return False, f"Directory {artifact_path} is empty"
        return False, f"Directory {artifact_path} does not exist"

    # File check
    if not artifact_path.exists():
        return False, f"Required file missing: {artifact_path}"

    if not artifact_path.is_file():
        return False, f"Expected file but found directory: {artifact_path}"

    content = artifact_path.read_text()
    if len(content) < min_size:
        return False, f"File {artifact_path.name} too small ({len(content)} chars, need {min_size})"

    return True, ""


def verify_previous_phases(current_phase: str, session_dir: Path) -> list[str]:
    """
    Verify all phases BEFORE current_phase have complete artifacts.
    Returns list of issues found.
    """
    phases = get_phase_order()
    issues = []

    try:
        current_index = phases.index(current_phase)
    except ValueError:
        return [f"Unknown phase: {current_phase}"]

    # Check all phases before current
    for i in range(current_index):
        phase = phases[i]
        artifacts = get_required_artifacts(phase, session_dir)

        for artifact_path, min_size in artifacts:
            success, error = verify_artifact(artifact_path, min_size)
            if not success:
                issues.append(f"Phase '{phase}' incomplete: {error}")

    return issues


def main():
    # Read hook input from stdin
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)  # Can't parse, allow

    # Check if we're in a stop hook recursion
    if data.get("stop_hook_active"):
        sys.exit(0)  # Already in stop hook, allow

    # Get project directory
    cwd = Path(data.get("cwd", "."))

    # Find active big4 session
    session_dir = find_big4_session(cwd)

    if session_dir is None:
        # No active consultant session, allow completion
        sys.exit(0)

    # Read state.json
    state_file = session_dir / "state.json"
    try:
        state = json.loads(state_file.read_text())
    except (json.JSONDecodeError, FileNotFoundError):
        # No valid state, allow (might be initial setup)
        sys.exit(0)

    current_phase = state.get("current_phase", "setup")

    # If complete, allow
    if current_phase == "complete":
        sys.exit(0)

    # Verify all previous phases
    issues = verify_previous_phases(current_phase, session_dir)

    if issues:
        # Block with feedback
        error_msg = f"Cannot proceed in phase '{current_phase}'. Previous phases incomplete:\n"
        error_msg += "\n".join(f"  - {issue}" for issue in issues)
        print(error_msg, file=sys.stderr)
        sys.exit(2)

    # All previous phases verified
    sys.exit(0)


if __name__ == "__main__":
    main()
