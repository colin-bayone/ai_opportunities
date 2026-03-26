#!/usr/bin/env python3
"""
State management for django-forge sessions.

Handles:
- Session initialization
- State loading and saving
- Phase advancement
- Resumption support

Usage:
    python state_manager.py init 123 "Issue title"
    python state_manager.py load 123
    python state_manager.py advance 123 exploration
    python state_manager.py status 123
"""

import argparse
import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional


WORKFLOW_BASE = ".django-workflow"
PHASES = [
    "setup",
    "documentation",
    "exploration",
    "planning",
    "approval",
    "implementation",
    "testing",
    "git",
    "complete"
]

COMPLEXITY_LEVELS = ["HIGH", "MEDIUM", "LOW"]


def get_session_path(issue_number: int) -> Path:
    """Get the session folder path for an issue."""
    return Path(WORKFLOW_BASE) / f"issue-{issue_number}"


def get_state_path(issue_number: int) -> Path:
    """Get the state.json path for an issue."""
    return get_session_path(issue_number) / "orchestration" / "state.json"


def init_session(issue_number: int, issue_title: str, complexity: str = "MEDIUM") -> dict:
    """Initialize a new session for an issue."""
    if complexity not in COMPLEXITY_LEVELS:
        raise ValueError(f"Complexity must be one of: {COMPLEXITY_LEVELS}")

    session_path = get_session_path(issue_number)

    # Create directory structure
    directories = [
        "orchestration",
        "exploration",
        "implementation/completed-work",
        "testing",
        "git"
    ]

    for dir_name in directories:
        (session_path / dir_name).mkdir(parents=True, exist_ok=True)

    # Create initial state
    state = {
        "session_id": str(uuid.uuid4()),
        "issue_number": issue_number,
        "issue_title": issue_title,
        "complexity": complexity,
        "created_at": datetime.now().isoformat(),
        "current_phase": "setup",
        "completed_phases": [],
        "phase_data": {},
        "user_decisions": [],
        "conflicts_resolved": [],
        "tasks": [],
        "implementation_stats": {
            "total_tasks": 0,
            "tasks_approved": 0,
            "tasks_reworked": 0,
            "total_rework_count": 0
        },
        "last_activity": datetime.now().isoformat()
    }

    # Save state
    save_state(issue_number, state)

    return state


def load_state(issue_number: int) -> Optional[dict]:
    """Load state for an issue."""
    state_path = get_state_path(issue_number)

    if not state_path.exists():
        return None

    with open(state_path, "r") as f:
        return json.load(f)


def save_state(issue_number: int, state: dict) -> None:
    """Save state for an issue."""
    state_path = get_state_path(issue_number)
    state_path.parent.mkdir(parents=True, exist_ok=True)

    state["last_activity"] = datetime.now().isoformat()

    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


def advance_phase(issue_number: int, new_phase: str) -> dict:
    """Advance to a new phase."""
    if new_phase not in PHASES:
        raise ValueError(f"Phase must be one of: {PHASES}")

    state = load_state(issue_number)
    if not state:
        raise ValueError(f"No session found for issue #{issue_number}")

    current_phase = state["current_phase"]

    # Mark current phase as completed
    if current_phase not in state["completed_phases"]:
        state["completed_phases"].append(current_phase)

    # Record phase completion data
    if current_phase not in state["phase_data"]:
        state["phase_data"][current_phase] = {}
    state["phase_data"][current_phase]["completed_at"] = datetime.now().isoformat()

    # Advance to new phase
    state["current_phase"] = new_phase
    state["phase_data"][new_phase] = {
        "started_at": datetime.now().isoformat()
    }

    save_state(issue_number, state)
    return state


def record_decision(issue_number: int, question: str, answer: str, rationale: str = "") -> dict:
    """Record a user decision."""
    state = load_state(issue_number)
    if not state:
        raise ValueError(f"No session found for issue #{issue_number}")

    state["user_decisions"].append({
        "question": question,
        "answer": answer,
        "rationale": rationale,
        "timestamp": datetime.now().isoformat(),
        "phase": state["current_phase"]
    })

    save_state(issue_number, state)
    return state


def record_conflict(issue_number: int, conflict: str, resolution: str) -> dict:
    """Record a resolved conflict."""
    state = load_state(issue_number)
    if not state:
        raise ValueError(f"No session found for issue #{issue_number}")

    state["conflicts_resolved"].append({
        "conflict": conflict,
        "resolution": resolution,
        "timestamp": datetime.now().isoformat(),
        "phase": state["current_phase"]
    })

    save_state(issue_number, state)
    return state


def update_implementation_stats(
    issue_number: int,
    total_tasks: Optional[int] = None,
    tasks_approved: Optional[int] = None,
    tasks_reworked: Optional[int] = None,
    total_rework_count: Optional[int] = None
) -> dict:
    """Update implementation statistics."""
    state = load_state(issue_number)
    if not state:
        raise ValueError(f"No session found for issue #{issue_number}")

    stats = state["implementation_stats"]

    if total_tasks is not None:
        stats["total_tasks"] = total_tasks
    if tasks_approved is not None:
        stats["tasks_approved"] = tasks_approved
    if tasks_reworked is not None:
        stats["tasks_reworked"] = tasks_reworked
    if total_rework_count is not None:
        stats["total_rework_count"] = total_rework_count

    save_state(issue_number, state)
    return state


def get_status(issue_number: int) -> dict:
    """Get current session status."""
    state = load_state(issue_number)
    if not state:
        return {"error": f"No session found for issue #{issue_number}"}

    return {
        "issue_number": state["issue_number"],
        "issue_title": state["issue_title"],
        "complexity": state["complexity"],
        "current_phase": state["current_phase"],
        "completed_phases": state["completed_phases"],
        "decisions_count": len(state["user_decisions"]),
        "conflicts_count": len(state["conflicts_resolved"]),
        "implementation_stats": state["implementation_stats"],
        "created_at": state["created_at"],
        "last_activity": state["last_activity"]
    }


def find_existing_sessions() -> list:
    """Find all existing session folders."""
    base = Path(WORKFLOW_BASE)
    if not base.exists():
        return []

    sessions = []
    for folder in base.iterdir():
        if folder.is_dir() and folder.name.startswith("issue-"):
            state_file = folder / "orchestration" / "state.json"
            if state_file.exists():
                try:
                    with open(state_file) as f:
                        state = json.load(f)
                    sessions.append({
                        "issue_number": state["issue_number"],
                        "issue_title": state["issue_title"],
                        "current_phase": state["current_phase"],
                        "last_activity": state["last_activity"]
                    })
                except (json.JSONDecodeError, KeyError):
                    pass
    return sessions


def main():
    parser = argparse.ArgumentParser(description="State management for django-forge")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new session")
    init_parser.add_argument("issue_number", type=int, help="GitHub issue number")
    init_parser.add_argument("issue_title", help="Issue title")
    init_parser.add_argument("--complexity", choices=COMPLEXITY_LEVELS, default="MEDIUM")

    # load command
    load_parser = subparsers.add_parser("load", help="Load session state")
    load_parser.add_argument("issue_number", type=int, help="GitHub issue number")

    # advance command
    advance_parser = subparsers.add_parser("advance", help="Advance to next phase")
    advance_parser.add_argument("issue_number", type=int, help="GitHub issue number")
    advance_parser.add_argument("phase", choices=PHASES, help="Phase to advance to")

    # status command
    status_parser = subparsers.add_parser("status", help="Get session status")
    status_parser.add_argument("issue_number", type=int, help="GitHub issue number")

    # list command
    subparsers.add_parser("list", help="List all existing sessions")

    args = parser.parse_args()

    if args.command == "init":
        state = init_session(args.issue_number, args.issue_title, args.complexity)
        print(f"Session initialized for issue #{args.issue_number}")
        print(f"Session ID: {state['session_id']}")
        print(f"Path: {get_session_path(args.issue_number)}")

    elif args.command == "load":
        state = load_state(args.issue_number)
        if state:
            print(json.dumps(state, indent=2))
        else:
            print(f"No session found for issue #{args.issue_number}")

    elif args.command == "advance":
        try:
            state = advance_phase(args.issue_number, args.phase)
            print(f"Advanced to phase: {args.phase}")
            print(f"Completed phases: {state['completed_phases']}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "status":
        status = get_status(args.issue_number)
        print(json.dumps(status, indent=2))

    elif args.command == "list":
        sessions = find_existing_sessions()
        if sessions:
            print("Existing sessions:")
            for s in sessions:
                print(f"  Issue #{s['issue_number']}: {s['issue_title']}")
                print(f"    Phase: {s['current_phase']}, Last activity: {s['last_activity']}")
        else:
            print("No existing sessions found")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
