#!/usr/bin/env python3
"""
Hook: skill-forge-references
Event: Stop
Purpose: Ensure relevant skill-forge references were read before generating skills/agents/hooks.

Skill-forge eats its own cooking - this hook enforces that best practice references
are consulted before generating output.

Exit codes:
  0 = Allow (references were read or not applicable)
  2 = Block (missing required reference read)
"""

import json
import sys
import os
import glob
from pathlib import Path


# Map of generation types to required references
# At least ONE reference from each list must be read (OR logic within a type,
# so reading the 2026-03-28 update satisfies the requirement alongside the originals)
REFERENCE_REQUIREMENTS = {
    "skill": [
        "2026-02-11_skill_structure.md",
        "2026-02-11_scripts_context.md",
    ],
    "agent": [
        "2026-02-11_agents_subagents.md",
    ],
    "hook": [
        "2026-02-11_hooks_system.md",
    ],
}

# The 2026-03-28 update covers ALL categories — reading it satisfies any requirement
UNIVERSAL_REFERENCES = [
    "2026-03-28_new_features_update.md",
]

# NOTE: Detection is now based on Write/Edit tool calls to specific paths,
# not text mentions. See detect_generation_type() for implementation.


def find_transcript(session_id: str) -> str | None:
    """Find the transcript file for this session."""
    # Check common locations
    patterns = [
        f"{os.environ.get('HOME', '')}/.claude/projects/*/sessions/{session_id}/transcript.jsonl",
        f"{os.environ.get('HOME', '')}/.claude/projects/*/{session_id}/transcript.jsonl",
    ]

    for pattern in patterns:
        matches = glob.glob(pattern)
        if matches:
            return matches[0]

    return None


def check_transcript_for_reads(transcript_path: str) -> set[str]:
    """Check transcript for Read tool calls to skill-forge references.

    A read only counts if:
    1. No limit was specified (full file read), OR
    2. Limit was >= 50 lines (meaningful read)

    This prevents "gaming" the hook by reading only 10 lines.
    """
    read_files = set()
    MIN_MEANINGFUL_LINES = 50

    try:
        with open(transcript_path, 'r') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    # Look for Read tool calls
                    if entry.get('type') == 'tool_use' and entry.get('name') == 'Read':
                        tool_input = entry.get('input', {})
                        file_path = tool_input.get('file_path', '')
                        limit = tool_input.get('limit')  # None if not specified

                        # Extract just the filename
                        if 'skill-forge/references/' in file_path:
                            # Only count if full read or meaningful read (>= 50 lines)
                            if limit is None or limit >= MIN_MEANINGFUL_LINES:
                                filename = Path(file_path).name
                                read_files.add(filename)
                except json.JSONDecodeError:
                    # Malformed JSON line in transcript, skip it
                    continue
    except FileNotFoundError:
        # Transcript doesn't exist yet, nothing to check
        pass

    return read_files


def detect_generation_type(transcript_path: str) -> set[str]:
    """Detect what types of things are being generated based on WRITE/EDIT tool calls.

    Only returns generation types if:
    1. skill-forge was actually invoked in this session (Skill tool call)
    2. There are Write/Edit tool calls to skill/agent/hook paths

    This avoids false positives from just MENTIONING these paths in conversation.
    """
    generation_types: set[str] = set()
    skill_forge_active = False

    try:
        with open(transcript_path, 'r') as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())

                    # Check if skill-forge was invoked via Skill tool
                    if not skill_forge_active:
                        if entry.get('type') == 'tool_use' and entry.get('name') == 'Skill':
                            skill_input = entry.get('input', {})
                            skill_name = skill_input.get('skill', '').lower()
                            if 'skill-forge' in skill_name or 'skill_forge' in skill_name:
                                skill_forge_active = True

                    # Check for Write/Edit tool calls to skill/agent/hook paths
                    if entry.get('type') == 'tool_use':
                        tool_name = entry.get('name', '')
                        if tool_name in ('Write', 'Edit'):
                            file_path = entry.get('input', {}).get('file_path', '')
                            file_path_lower = file_path.lower()
                            filename = Path(file_path).name.lower()

                            # Use AND logic with exact filename to avoid false positives
                            if "skill" not in generation_types:
                                if ".claude/skills/" in file_path_lower and filename == "skill.md":
                                    generation_types.add("skill")

                            if "agent" not in generation_types:
                                if ".claude/agents/" in file_path_lower and filename == "agent.md":
                                    generation_types.add("agent")

                            if "hook" not in generation_types:
                                if ".claude/hooks/" in file_path_lower:
                                    generation_types.add("hook")

                except json.JSONDecodeError:
                    # Malformed JSON line, skip
                    continue

    except FileNotFoundError:
        # Transcript doesn't exist yet
        pass

    # Only return generation types if skill-forge was actually invoked
    if not skill_forge_active:
        return set()

    return generation_types


def main():
    # Read hook input from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Can't parse input, allow to continue
        sys.exit(0)

    # Check if stop hook is already active (prevent recursion)
    if input_data.get('stop_hook_active', False):
        sys.exit(0)

    session_id = input_data.get('session_id', '')
    if not session_id:
        sys.exit(0)

    # Find transcript
    transcript_path = input_data.get('transcript_path')
    if not transcript_path:
        transcript_path = find_transcript(session_id)

    if not transcript_path or not os.path.exists(transcript_path):
        # Can't find transcript, allow to continue
        sys.exit(0)

    # Detect what's being generated (only if skill-forge is active)
    generation_types = detect_generation_type(transcript_path)

    if not generation_types:
        # Not generating anything skill-forge related, or skill-forge wasn't invoked
        sys.exit(0)

    # Check what references were read
    read_files = check_transcript_for_reads(transcript_path)

    # If a universal reference was read, all requirements are satisfied
    if any(ref in read_files for ref in UNIVERSAL_REFERENCES):
        sys.exit(0)

    # Check for missing required references
    missing = []
    for gen_type in generation_types:
        required = REFERENCE_REQUIREMENTS.get(gen_type, [])
        for ref in required:
            if ref not in read_files:
                missing.append((gen_type, ref))

    if missing:
        # Build error message
        msg_parts = ["skill-forge: Missing required reference reads:"]
        for gen_type, ref in missing:
            msg_parts.append(f"  - For {gen_type}: references/{ref}")
        msg_parts.append("")
        msg_parts.append("Read these references before generating output to ensure best practices.")

        print("\n".join(msg_parts), file=sys.stderr)
        sys.exit(2)

    # All required references were read
    sys.exit(0)


if __name__ == "__main__":
    main()
