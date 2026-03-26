#!/usr/bin/env python3
"""
Check Previous Phases - Verification logic for Stop hook.

This script verifies that all artifacts for previous phases exist before
allowing work on the current phase. Used by the Stop hook.

Usage: python check_previous_phases.py <session-folder>

Exit codes:
  0 - All previous phases complete, OK to proceed
  2 - Missing artifacts, blocks progression (stderr contains message)
  1 - Script error
"""

import json
import sys
from pathlib import Path


# Phase order for verification
PHASE_ORDER = ["setup", "analysis", "review", "quality", "approval", "outputs"]

# Required artifacts per phase
PHASE_REQUIREMENTS = {
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

    # Also check user_decisions array for backwards compatibility
    for decision in state.get("user_decisions", []):
        if decision.get("decision") == "plan_approved" and decision.get("value"):
            return True, ""

    return False, "User approval required (state.json 'approved' must be true)"


def main():
    if len(sys.argv) < 2:
        print("Usage: check_previous_phases.py <session-folder>", file=sys.stderr)
        sys.exit(1)

    session_folder = Path(sys.argv[1])

    # Check session folder exists
    if not session_folder.exists():
        print(f"Session folder not found: {session_folder}", file=sys.stderr)
        sys.exit(1)

    # Read state.json
    state_path = session_folder / "orchestration" / "state.json"
    if not state_path.exists():
        print(f"state.json not found: {state_path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(state_path) as f:
            state = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Invalid state.json: {e}", file=sys.stderr)
        sys.exit(1)

    current_phase = state.get("current_phase", "setup")

    # Get phases to check
    phases_to_check = get_phases_before(current_phase)

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
        print(f"\nCurrent phase: {current_phase}", file=sys.stderr)
        print(f"Phases checked: {', '.join(phases_to_check)}", file=sys.stderr)
        print(f"\nErrors ({len(errors)}):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        print("\nComplete previous phases before proceeding.", file=sys.stderr)
        sys.exit(2)  # Exit code 2 blocks in hooks

    # All clear
    print(f"OK: All previous phases complete for '{current_phase}'")
    sys.exit(0)


if __name__ == "__main__":
    main()
