#!/usr/bin/env python3
"""
Scaffold RFP Questions project folder structure.

Usage: python scaffold_project.py <client-name> [--rfp-name "RFP Name"]

Creates the complete folder structure for an RFP question development session.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


def slugify(name: str) -> str:
    """Convert name to folder-safe slug."""
    return name.lower().replace(" ", "-").replace("_", "-")


def create_structure(base_path: Path) -> None:
    """Create the complete folder structure."""
    folders = [
        "source",           # User puts original documents here
        "ingested",         # Processed documents go here
        "orchestration",
        "phase_01_setup",
        "phase_02_analysis",
        "phase_03_review",
        "phase_04_quality",
        "phase_05_approval",
        "phase_06_outputs",
    ]

    for folder in folders:
        (base_path / folder).mkdir(parents=True, exist_ok=True)

    print(f"Created folder structure at: {base_path}")


def create_state_json(base_path: Path, client_name: str, rfp_name: str) -> None:
    """Initialize state.json with default values."""
    state = {
        "client_name": client_name,
        "rfp_name": rfp_name,
        "session_folder": str(base_path),
        "created_at": datetime.now().isoformat(),
        "current_phase": "ingestion",
        "completed_phases": [],
        "ingestion_complete": False,
        "ingested_documents": [],
        "what_we_are_building": "",
        "competitive_context": "",
        "source_documents": [],
        "existing_questions_count": 0,
        "question_counts": {
            "original": 0,
            "revised": 0,
            "new": 0,
            "removed": 0,
            "total": 0
        },
        "review_decisions": [],
        "gaps_reviewed": 0,
        "gaps_accepted": 0,
        "gaps_modified": 0,
        "gaps_rejected": 0,
        "critical_learnings": [],
        "approved": False,
        "requested_outputs": [],
        "big4_review_requested": False,
        "workflow_complete": False,
        "agent_mode": "teams"
    }

    state_path = base_path / "orchestration" / "state.json"
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)

    print(f"Initialized state.json at: {state_path}")


def create_marker_file(base_path: Path) -> None:
    """Create the .active marker file for hook scoping."""
    marker_path = base_path / ".active"
    marker_path.touch()
    print(f"Created marker file: {marker_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold RFP Questions project folder structure"
    )
    parser.add_argument(
        "client_name",
        help="Client name (will be slugified for folder name)"
    )
    parser.add_argument(
        "--rfp-name",
        default="",
        help="RFP name/description"
    )
    parser.add_argument(
        "--base-dir",
        default=".rfp-questions",
        help="Base directory for RFP question projects"
    )

    args = parser.parse_args()

    # Create folder path
    slug = slugify(args.client_name)
    base_path = Path(args.base_dir) / slug

    # Check if already exists
    if base_path.exists():
        print(f"Warning: Folder already exists at {base_path}")

        # Check for active marker
        if (base_path / ".active").exists():
            print("Error: An active session already exists. Remove .active marker to start fresh.")
            sys.exit(1)

        response = input("Continue and reinitialize? (y/N): ")
        if response.lower() != "y":
            print("Aborted.")
            sys.exit(0)

    # Create structure
    create_structure(base_path)

    # Initialize state
    rfp_name = args.rfp_name or f"{args.client_name} RFP"
    create_state_json(base_path, args.client_name, rfp_name)

    # Create marker
    create_marker_file(base_path)

    print(f"\nProject scaffolded successfully!")
    print(f"  Session folder: {base_path}")
    print(f"  Source folder: {base_path / 'source'}")
    print(f"  State file: {base_path / 'orchestration' / 'state.json'}")
    print(f"  Marker file: {base_path / '.active'}")
    print(f"\nNext steps:")
    print(f"  1. Add source documents to: {base_path / 'source'}")
    print(f"  2. Run document scan: python3 .claude/skills/rfp-questions/scripts/scan_documents.py {base_path}")
    print(f"  3. Process documents with Gemini (Phase 0)")
    print(f"  4. Proceed to Phase 1 setup")


if __name__ == "__main__":
    main()
