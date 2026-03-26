#!/usr/bin/env python3
"""
State management utilities for meeting-git-issue-extractor sessions.

Usage:
    # As a module
    from state_manager import load_state, save_state, advance_phase

    # As CLI
    python state_manager.py <session_path> status
    python state_manager.py <session_path> advance <new_phase>
    python state_manager.py <session_path> add-topic <topic_name>
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


VALID_PHASES = [
    "setup",
    "analysis",
    "workflow_selection",
    "exploration",
    "clarification",
    "drafting",
    "review",
    "creation",
    "complete",
]


def load_state(session_path: str) -> dict:
    """Load state from session folder."""
    state_file = Path(session_path) / "orchestration" / "state.json"

    if not state_file.exists():
        raise FileNotFoundError(f"State file not found: {state_file}")

    with open(state_file, 'r') as f:
        return json.load(f)


def save_state(session_path: str, state: dict) -> None:
    """Save state to session folder."""
    state_file = Path(session_path) / "orchestration" / "state.json"

    # Update last activity timestamp
    state["last_activity"] = datetime.now().isoformat()

    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)


def get_current_phase(session_path: str) -> str:
    """Get current phase from state."""
    state = load_state(session_path)
    return state.get("current_phase", "unknown")


def advance_phase(session_path: str, new_phase: str) -> dict:
    """Advance to a new phase, recording the previous as completed."""

    if new_phase not in VALID_PHASES:
        raise ValueError(f"Invalid phase: {new_phase}. Valid phases: {VALID_PHASES}")

    state = load_state(session_path)

    # Record current phase as completed
    current = state.get("current_phase")
    if current and current not in state.get("completed_phases", []):
        state.setdefault("completed_phases", []).append(current)

    # Advance to new phase
    state["current_phase"] = new_phase

    save_state(session_path, state)
    return state


def add_topic(session_path: str, topic_name: str, topic_slug: str = None, priority: str = "medium") -> dict:
    """Add a topic to the session."""

    state = load_state(session_path)

    if topic_slug is None:
        topic_slug = topic_name.lower().replace(" ", "-")

    topic = {
        "name": topic_name,
        "slug": topic_slug,
        "priority": priority,
        "status": "pending",
        "added_at": datetime.now().isoformat(),
    }

    state.setdefault("topics", []).append(topic)
    save_state(session_path, state)

    return state


def update_topic_status(session_path: str, topic_slug: str, status: str) -> dict:
    """Update a topic's status."""

    state = load_state(session_path)

    for topic in state.get("topics", []):
        if topic["slug"] == topic_slug:
            topic["status"] = status
            topic["updated_at"] = datetime.now().isoformat()
            break
    else:
        raise ValueError(f"Topic not found: {topic_slug}")

    save_state(session_path, state)
    return state


def record_issue_created(session_path: str, issue_number: int, issue_url: str, title: str) -> dict:
    """Record that an issue was created in GitHub."""

    state = load_state(session_path)

    issue_record = {
        "number": issue_number,
        "url": issue_url,
        "title": title,
        "created_at": datetime.now().isoformat(),
    }

    state.setdefault("issues_created", []).append(issue_record)
    save_state(session_path, state)

    return state


def set_workflow_mode(session_path: str, mode: str) -> dict:
    """Set the workflow mode for the session."""

    valid_modes = ["parallel_explore_sequential_issues", "fully_parallel"]
    if mode not in valid_modes:
        raise ValueError(f"Invalid workflow mode: {mode}. Valid: {valid_modes}")

    state = load_state(session_path)
    state["workflow_mode"] = mode
    save_state(session_path, state)

    return state


def print_status(session_path: str) -> None:
    """Print current session status."""

    state = load_state(session_path)

    print(f"\n📊 Session Status: {session_path}\n")
    print(f"Session ID: {state.get('session_id', 'unknown')}")
    print(f"Created: {state.get('created_at', 'unknown')}")
    print(f"Last Activity: {state.get('last_activity', 'unknown')}")
    print(f"\nCurrent Phase: {state.get('current_phase', 'unknown')}")
    print(f"Completed Phases: {', '.join(state.get('completed_phases', [])) or 'None'}")
    print(f"Workflow Mode: {state.get('workflow_mode', 'Not set')}")

    topics = state.get("topics", [])
    if topics:
        print(f"\nTopics ({len(topics)}):")
        for topic in topics:
            print(f"  - {topic['name']} [{topic['status']}] (priority: {topic['priority']})")

    issues = state.get("issues_created", [])
    if issues:
        print(f"\nIssues Created ({len(issues)}):")
        for issue in issues:
            print(f"  - #{issue['number']}: {issue['title']}")


def find_incomplete_sessions(base_path: str = None) -> list:
    """Find sessions that are not complete."""

    if base_path is None:
        # Default to project claude/ folder
        script_dir = Path(__file__).parent
        base_path = script_dir.parent.parent.parent.parent / "claude"

    base = Path(base_path)
    incomplete = []

    for folder in base.iterdir():
        if folder.is_dir():
            state_file = folder / "orchestration" / "state.json"
            if state_file.exists():
                try:
                    state = load_state(str(folder))
                    if state.get("current_phase") != "complete":
                        incomplete.append({
                            "path": str(folder),
                            "topic": state.get("topic_slug"),
                            "phase": state.get("current_phase"),
                            "last_activity": state.get("last_activity"),
                        })
                except Exception:
                    pass

    return incomplete


def main():
    parser = argparse.ArgumentParser(
        description="Manage meeting-git-issue-extractor session state"
    )
    parser.add_argument(
        "session_path",
        nargs="?",
        help="Path to session folder"
    )
    parser.add_argument(
        "command",
        choices=["status", "advance", "add-topic", "find-incomplete"],
        help="Command to execute"
    )
    parser.add_argument(
        "value",
        nargs="?",
        help="Value for command (phase name or topic name)"
    )
    parser.add_argument(
        "--priority",
        default="medium",
        help="Priority for add-topic (default: medium)"
    )

    args = parser.parse_args()

    if args.command == "find-incomplete":
        sessions = find_incomplete_sessions()
        if sessions:
            print("\n🔍 Incomplete Sessions:\n")
            for session in sessions:
                print(f"  📁 {session['path']}")
                print(f"     Topic: {session['topic']}")
                print(f"     Phase: {session['phase']}")
                print(f"     Last: {session['last_activity']}\n")
        else:
            print("\n✅ No incomplete sessions found.\n")
        return

    if not args.session_path:
        print("❌ Session path required for this command")
        sys.exit(1)

    try:
        if args.command == "status":
            print_status(args.session_path)

        elif args.command == "advance":
            if not args.value:
                print(f"❌ New phase required. Valid phases: {VALID_PHASES}")
                sys.exit(1)
            state = advance_phase(args.session_path, args.value)
            print(f"✅ Advanced to phase: {args.value}")

        elif args.command == "add-topic":
            if not args.value:
                print("❌ Topic name required")
                sys.exit(1)
            state = add_topic(args.session_path, args.value, priority=args.priority)
            print(f"✅ Added topic: {args.value}")

    except FileNotFoundError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
