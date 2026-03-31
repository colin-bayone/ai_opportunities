#!/usr/bin/env python3
"""
Agent File-Write Capability Checker

Verifies that settings.local.json contains the necessary Write permissions
for skill-forge agents to write research files to the references/ directory.

This is a MANDATORY check that runs at skill invocation time.

Usage:
    python3 .claude/skills/skill-forge/scripts/check_agent_write_permissions.py

Exit codes:
    0 - Write permissions are configured correctly
    1 - Write permissions are missing or insufficient
    2 - settings.local.json not found or unreadable
"""

import json
import re
import sys
from pathlib import Path


def find_settings_file() -> Path:
    """Find settings.local.json."""
    # Try from CLAUDE_PROJECT_DIR env var first
    import os
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    if project_dir:
        path = Path(project_dir) / ".claude" / "settings.local.json"
        if path.exists():
            return path

    # Try from cwd
    cwd = Path.cwd()
    path = cwd / ".claude" / "settings.local.json"
    if path.exists():
        return path

    # Walk up to find it
    for parent in cwd.parents:
        path = parent / ".claude" / "settings.local.json"
        if path.exists():
            return path

    return cwd / ".claude" / "settings.local.json"


def check_write_permission(settings: dict, target_pattern: str) -> dict:
    """Check if a Write permission pattern exists in settings."""
    permissions = settings.get("permissions", {})
    allow_rules = permissions.get("allow", [])
    deny_rules = permissions.get("deny", [])

    # Check deny rules first
    for rule in deny_rules:
        if rule.startswith("Write") and target_pattern in rule:
            return {
                "has_permission": False,
                "reason": f"Write to target is explicitly DENIED: {rule}",
                "rule": rule,
            }

    # Check allow rules
    for rule in allow_rules:
        if rule.startswith("Write"):
            # Check for exact match or wildcard coverage
            if target_pattern in rule:
                return {
                    "has_permission": True,
                    "reason": f"Exact or pattern match found: {rule}",
                    "rule": rule,
                }
            # Check for broad patterns that would cover our target
            if "$CLAUDE_PROJECT_DIR/.claude/**" in rule or "$CLAUDE_PROJECT_DIR/.claude/skills/**" in rule:
                return {
                    "has_permission": True,
                    "reason": f"Broad pattern covers target: {rule}",
                    "rule": rule,
                }

    return {
        "has_permission": False,
        "reason": "No matching Write permission found in allow rules",
        "rule": None,
    }


def main():
    settings_path = find_settings_file()

    if not settings_path.exists():
        print(json.dumps({
            "status": "error",
            "error": f"settings.local.json not found at {settings_path}",
            "fix": "Create .claude/settings.local.json with Write permissions for skill-forge",
            "required_permission": 'Write($CLAUDE_PROJECT_DIR/.claude/skills/skill-forge/**)',
        }))
        sys.exit(2)

    try:
        settings = json.loads(settings_path.read_text())
    except json.JSONDecodeError as e:
        print(json.dumps({
            "status": "error",
            "error": f"Invalid JSON in {settings_path}: {e}",
        }))
        sys.exit(2)

    # Check for write permission to skill-forge references
    target = ".claude/skills/skill-forge/"
    result = check_write_permission(settings, target)

    required_permission = 'Write($CLAUDE_PROJECT_DIR/.claude/skills/skill-forge/**)'

    if result["has_permission"]:
        report = {
            "status": "ok",
            "message": "Agents CAN write to skill-forge references directory",
            "matched_rule": result["rule"],
            "settings_file": str(settings_path),
        }
        print(json.dumps(report, indent=2))
        sys.exit(0)
    else:
        report = {
            "status": "missing",
            "message": "Agents CANNOT write to skill-forge references directory",
            "reason": result["reason"],
            "settings_file": str(settings_path),
            "fix": f'Add this to permissions.allow in {settings_path.name}:',
            "required_permission": required_permission,
            "example": {
                "permissions": {
                    "allow": [
                        required_permission,
                    ]
                }
            },
        }
        print(json.dumps(report, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
