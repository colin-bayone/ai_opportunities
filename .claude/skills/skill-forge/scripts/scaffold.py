#!/usr/bin/env python3
"""
Scaffold a new skill with proper structure.

Usage:
    python scaffold.py <skill_name> <output_path>
    python scaffold.py my-skill .claude/skills/my-skill --with-scripts --with-references
"""

import argparse
import json
from pathlib import Path


def find_claude_dir(start_path: Path, max_levels: int = 5) -> Path | None:
    """Walk up from start_path to find a .claude directory.

    Args:
        start_path: Starting directory to search from
        max_levels: Maximum parent levels to search (default 5)

    Returns:
        Path to .claude directory if found, None otherwise
    """
    current = start_path.resolve()

    for _ in range(max_levels):
        # Check if current directory IS .claude
        if current.name == ".claude":
            return current

        # Check if .claude exists as a child
        claude_candidate = current / ".claude"
        if claude_candidate.is_dir():
            return claude_candidate

        # Check if parent contains .claude
        parent = current.parent
        if parent == current:
            # Reached filesystem root
            break

        claude_in_parent = parent / ".claude"
        if claude_in_parent.is_dir():
            return claude_in_parent

        current = parent

    return None


def show_plan(name: str, output_path: Path, claude_dir: Path | None,
              with_scripts: bool, with_references: bool, with_hooks: bool) -> dict:
    """Generate a plan showing where all files will be created.

    Returns a dict with the planned locations for user confirmation.
    """
    plan = {
        "skill_dir": str(output_path),
        "files": {
            "SKILL.md": str(output_path / "SKILL.md"),
        }
    }

    if with_scripts:
        plan["files"]["scripts/placeholder.py"] = str(output_path / "scripts" / "placeholder.py")

    if with_references:
        plan["files"]["references/placeholder.md"] = str(output_path / "references" / "placeholder.md")

    if with_hooks and claude_dir:
        hook_path = claude_dir / "hooks" / f"{name}-hook.py"
        plan["files"][f"hooks/{name}-hook.py"] = str(hook_path)
        plan["hooks_dir"] = str(claude_dir / "hooks")

    if claude_dir:
        plan["claude_dir"] = str(claude_dir)
        plan["settings_file"] = str(claude_dir / "settings.local.json")

    return plan


SKILL_MD_TEMPLATE = '''---
name: {name}
description: |
  {description}

  WHEN to use: {when_to_use}
  WHEN NOT to use: {when_not_to_use}
---

# {title}

## Purpose

{purpose}

## Hard Rules

1. [Add your hard rules here]
2. Always use absolute paths for references (e.g., `.claude/skills/{name}/references/...`)

## Workflow

1. [Add your workflow steps here]

{references_section}

{settings_section}
'''

# Template for references section with ABSOLUTE paths
REFERENCES_TEMPLATE = '''## References

All references are at `.claude/skills/{name}/references/`. Use absolute paths:

- `.claude/skills/{name}/references/placeholder.md` - [Description]
'''

# Template for settings.local.json guidance
SETTINGS_SECTION_TEMPLATE = '''## Settings Configuration

To enable this skill's features, add to `.claude/settings.local.json`:

```json
{{
  "permissions": {{
    "allow": [
      "Skill({name})"
    ]
  }}
}}
```

{hooks_settings}
'''

HOOKS_SETTINGS_TEMPLATE = '''To enable the hook, add:

```json
{{
  "hooks": {{
    "{hook_event}": [
      {{
        "hooks": [
          {{
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/.claude/hooks/{name}-hook.py",
            "timeout": 10000,
            "statusMessage": "Running {name} hook..."
          }}
        ]
      }}
    ]
  }}
}}
```
'''

AGENT_MD_TEMPLATE = '''---
name: {name}
description: |
  {description}
model: sonnet
---

# {title}

## Purpose

{purpose}

## Responsibilities

1. [Add responsibilities here]

## Output

[Describe expected output]
'''

HOOK_TEMPLATE = '''#!/bin/bash
# Hook: {hook_name}
# Event: {event}
# Purpose: {purpose}

set -e

# Read input from stdin
input=$(cat)

# Parse relevant fields
# tool_name=$(echo "$input" | jq -r '.tool_name // empty')

# Your logic here

# Exit codes:
# 0 = success (continue)
# 2 = block action (with stderr as message)
# other = non-blocking error

exit 0
'''


def create_skill(
    name: str,
    output_path: Path,
    with_scripts: bool = False,
    with_references: bool = False,
    with_hooks: bool = False,
    hook_event: str = "Stop",
) -> dict:
    """Create a skill scaffold with absolute paths and settings guidance."""

    # Create directories
    output_path.mkdir(parents=True, exist_ok=True)

    if with_scripts:
        (output_path / "scripts").mkdir(exist_ok=True)

    if with_references:
        (output_path / "references").mkdir(exist_ok=True)

    # Create SKILL.md with ABSOLUTE paths
    title = name.replace("-", " ").title()

    # References section with absolute paths
    if with_references:
        references_section = REFERENCES_TEMPLATE.format(name=name)
    else:
        references_section = "## References\n\n[No references yet - add `.claude/skills/{name}/references/` if needed]".format(name=name)

    # Settings section with hook config if needed
    if with_hooks:
        hooks_settings = HOOKS_SETTINGS_TEMPLATE.format(name=name, hook_event=hook_event)
    else:
        hooks_settings = ""

    settings_section = SETTINGS_SECTION_TEMPLATE.format(
        name=name,
        hooks_settings=hooks_settings,
    )

    skill_content = SKILL_MD_TEMPLATE.format(
        name=name,
        title=title,
        description=f"[Describe what {title} does]",
        when_to_use="[Describe when Claude should invoke this skill]",
        when_not_to_use="[Describe when NOT to use this skill]",
        purpose=f"[Explain the purpose of {title}]",
        references_section=references_section,
        settings_section=settings_section,
    )

    (output_path / "SKILL.md").write_text(skill_content)

    created = ["SKILL.md"]

    if with_scripts:
        # Create placeholder script
        script_content = '''#!/usr/bin/env python3
"""
Placeholder script for {name}.
"""

def main():
    print("TODO: Implement")


if __name__ == "__main__":
    main()
'''.format(name=name)
        (output_path / "scripts" / "placeholder.py").write_text(script_content)
        created.append("scripts/placeholder.py")

    if with_references:
        # Create placeholder reference with absolute path note
        ref_content = f'''# {title} Reference

[Add detailed reference content here]

**Note:** When referencing this file from SKILL.md, use the absolute path:
`.claude/skills/{name}/references/placeholder.md`
'''
        (output_path / "references" / "placeholder.md").write_text(ref_content)
        created.append("references/placeholder.md")

    if with_hooks:
        # Find .claude directory by walking up from output_path (max 5 levels)
        # Standard structure: .claude/skills/skill-name/ -> .claude/hooks/
        claude_dir = find_claude_dir(output_path, max_levels=5)

        if claude_dir is None:
            # Could not find .claude directory - this is an error
            return {
                "success": False,
                "error": "Could not find .claude directory. Expected structure: .claude/skills/<skill-name>/",
                "skill_path": str(output_path),
                "suggestion": "Ensure output_path is within a project with .claude/ at the root",
            }

        hooks_dir = claude_dir / "hooks"
        hooks_dir.mkdir(parents=True, exist_ok=True)

        hook_filename = f"{name}-hook.py"
        hook_path = hooks_dir / hook_filename

        hook_content = f'''#!/usr/bin/env python3
"""
Hook: {name}-hook
Event: {hook_event}
Purpose: [Describe what this hook enforces]

Exit codes:
  0 = Allow (continue)
  2 = Block (stderr message fed to Claude)
"""

import json
import sys


def main():
    # Read hook input from stdin
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    session_id = input_data.get('session_id', '')

    # TODO: Implement your hook logic here
    # Example: Check if required conditions are met

    # Exit 0 to allow, exit 2 to block
    sys.exit(0)


if __name__ == "__main__":
    main()
'''
        hook_path.write_text(hook_content)
        hook_path.chmod(0o755)
        created.append(f"../../hooks/{hook_filename}")

    return {
        "success": True,
        "skill_path": str(output_path),
        "created": created,
    }


def create_agent(name: str, output_path: Path) -> dict:
    """Create an agent scaffold at .claude/agents/."""

    title = name.replace("-", " ").title()

    agent_content = AGENT_MD_TEMPLATE.format(
        name=name,
        title=title,
        description=f"[Describe what {title} does and when to invoke it]",
        purpose=f"[Explain the purpose of {title}]",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(agent_content)

    return {
        "success": True,
        "agent_path": str(output_path),
    }


def create_hook(hook_name: str, event: str, output_path: Path) -> dict:
    """Create a hook scaffold."""

    hook_content = HOOK_TEMPLATE.format(
        hook_name=hook_name,
        event=event,
        purpose=f"[Describe what this hook does]",
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(hook_content)
    output_path.chmod(0o755)

    return {
        "success": True,
        "hook_path": str(output_path),
    }


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new skill")
    parser.add_argument("name", help="Skill name (lowercase with hyphens)")
    parser.add_argument("output_path", help="Output directory path")
    parser.add_argument("--with-scripts", action="store_true", help="Include scripts/ directory")
    parser.add_argument("--with-references", action="store_true", help="Include references/ directory")
    parser.add_argument("--with-hooks", action="store_true", help="Include hook template at .claude/hooks/")
    parser.add_argument("--hook-event", default="Stop", help="Hook event type (default: Stop)")
    parser.add_argument("--plan", action="store_true", help="Show plan only, don't create files")
    parser.add_argument("--claude-dir", help="Explicit path to .claude directory (optional)")
    args = parser.parse_args()

    output_path = Path(args.output_path)

    # Find .claude directory
    if args.claude_dir:
        claude_dir = Path(args.claude_dir)
        if not claude_dir.is_dir():
            print(json.dumps({
                "success": False,
                "error": f"Specified --claude-dir does not exist: {args.claude_dir}",
            }, indent=2))
            return
    else:
        claude_dir = find_claude_dir(output_path, max_levels=5)

    # If --plan flag, show plan and exit
    if args.plan:
        plan = show_plan(
            name=args.name,
            output_path=output_path,
            claude_dir=claude_dir,
            with_scripts=args.with_scripts,
            with_references=args.with_references,
            with_hooks=args.with_hooks,
        )

        if claude_dir is None and args.with_hooks:
            plan["warning"] = "Could not find .claude directory. Use --claude-dir to specify."

        print(json.dumps({"plan": plan}, indent=2))
        return

    result = create_skill(
        name=args.name,
        output_path=output_path,
        with_scripts=args.with_scripts,
        with_references=args.with_references,
        with_hooks=args.with_hooks,
        hook_event=args.hook_event,
    )

    # Add plan to result so user can see what was created
    if result.get("success"):
        result["plan"] = show_plan(
            name=args.name,
            output_path=output_path,
            claude_dir=claude_dir,
            with_scripts=args.with_scripts,
            with_references=args.with_references,
            with_hooks=args.with_hooks,
        )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
