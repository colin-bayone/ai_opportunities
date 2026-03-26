#!/usr/bin/env python3
"""
RFP Questions Compliance Hook (Stop Hook)

This hook enforces the "Check Previous Phases" pattern for the rfp-questions skill.
It fires on every Stop event and verifies that all artifacts for previous phases
exist before allowing progression.

Exit codes:
  0 - Allow (not an rfp-questions session, or all checks pass)
  2 - Block (missing artifacts, message sent to Claude via stderr)

Usage: Configured as a Stop hook in settings.local.json
"""

import json
import sys
from pathlib import Path


def find_active_session() -> Path | None:
    """Find the active rfp-questions session by locating .active marker."""
    # Look for .rfp-questions/*/.active
    rfp_base = Path(".rfp-questions")

    if not rfp_base.exists():
        return None

    for client_dir in rfp_base.iterdir():
        if client_dir.is_dir():
            marker = client_dir / ".active"
            if marker.exists():
                return client_dir

    return None


# Phase order for verification
PHASE_ORDER = ["ingestion", "setup", "analysis", "review", "quality", "approval", "outputs"]

# Required artifacts per phase
PHASE_REQUIREMENTS = {
    "ingestion": [
        "ingested/index.md"
    ],
    "setup": [
        "phase_01_setup/source_verification.md"
    ],
    "analysis": [
        "phase_02_analysis/source_verification_report.md",
        "phase_02_analysis/question_catalog_v01.md",
        "phase_02_analysis/gap_analysis.md",
        "phase_02_analysis/refinement_recommendations.md",
        "phase_02_analysis/competitor_risk_assessment.md"
    ],
    "review": [
        "phase_03_review/review_decisions.md"
    ],
    "quality": [
        "phase_04_quality/final_risk_review.md",
        "phase_04_quality/duplication_check.md",
        "phase_04_quality/depth_check.md"
    ],
    "approval": [],  # Checked via state.json
    "outputs": [
        "phase_06_outputs/final_questions.md"
    ]
}

# Minimum file sizes (to catch empty placeholder files)
MIN_SIZES = {
    "index.md": 50,  # ingested/index.md
    "source_verification.md": 50,
    "source_verification_report.md": 100,
    "question_catalog_v01.md": 200,
    "gap_analysis.md": 200,
    "refinement_recommendations.md": 100,
    "competitor_risk_assessment.md": 200,
    "review_decisions.md": 50,
    "final_risk_review.md": 100,
    "duplication_check.md": 50,
    "depth_check.md": 50,
    "final_questions.md": 200
}


def get_phases_before(current_phase: str) -> list[str]:
    """Get all phases that must be complete before current phase."""
    if current_phase not in PHASE_ORDER:
        return []

    current_index = PHASE_ORDER.index(current_phase)
    return PHASE_ORDER[:current_index]


def check_artifact(session_folder: Path, artifact: str) -> tuple[bool, str]:
    """Check if an artifact exists and has minimum content."""
    artifact_path = session_folder / artifact

    if not artifact_path.exists():
        return False, f"Missing: {artifact}"

    # Check minimum size
    filename = Path(artifact).name
    min_size = MIN_SIZES.get(filename, 0)

    if min_size > 0:
        actual_size = artifact_path.stat().st_size
        if actual_size < min_size:
            return False, f"Too small ({actual_size} chars, need {min_size}): {artifact}"

    return True, ""


def check_approval(state: dict) -> tuple[bool, str]:
    """Check if user approval is recorded in state.json."""
    if state.get("approved", False):
        return True, ""

    return False, "User approval required (state.json 'approved' must be true)"


def main():
    # Find active session
    session_folder = find_active_session()

    if session_folder is None:
        # Not an rfp-questions session, allow everything
        sys.exit(0)

    # Read state.json
    state_path = session_folder / "orchestration" / "state.json"
    if not state_path.exists():
        # No state file yet, allow (setup phase)
        sys.exit(0)

    try:
        with open(state_path) as f:
            state = json.load(f)
    except json.JSONDecodeError:
        # Invalid state file, allow but this is unusual
        sys.exit(0)

    current_phase = state.get("current_phase", "setup")

    # Get phases to check
    phases_to_check = get_phases_before(current_phase)

    if not phases_to_check:
        # In setup phase or no phases to check, allow
        sys.exit(0)

    # Collect all errors
    errors = []

    for phase in phases_to_check:
        # Check artifacts
        for artifact in PHASE_REQUIREMENTS.get(phase, []):
            ok, error = check_artifact(session_folder, artifact)
            if not ok:
                errors.append(f"Phase '{phase}': {error}")

        # Special check for approval phase
        if phase == "approval":
            ok, error = check_approval(state)
            if not ok:
                errors.append(f"Phase 'approval': {error}")

    # Report results
    if errors:
        print("=" * 60, file=sys.stderr)
        print("BLOCKED: Previous phase artifacts missing", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        print(f"\nSession: {session_folder}", file=sys.stderr)
        print(f"Current phase: {current_phase}", file=sys.stderr)
        print(f"Phases checked: {', '.join(phases_to_check)}", file=sys.stderr)
        print(f"\nErrors ({len(errors)}):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        print("\nComplete previous phases before proceeding.", file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        sys.exit(2)  # Exit code 2 blocks in hooks

    # All clear
    sys.exit(0)


if __name__ == "__main__":
    main()
