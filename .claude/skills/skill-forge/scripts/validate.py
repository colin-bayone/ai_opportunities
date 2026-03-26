#!/usr/bin/env python3
"""
Validate a skill's structure and frontmatter.

Usage:
    python validate.py <skill_path>
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_str = parts[1].strip()
    body = parts[2].strip()

    # Simple YAML parsing (key: value)
    frontmatter = {}
    current_key = None
    current_value = []

    for line in frontmatter_str.split("\n"):
        # Support hyphenated keys like disable-model-invocation, user-invocable
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            if current_key:
                frontmatter[current_key] = "\n".join(current_value).strip()
            match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)", line)
            if match:
                current_key = match.group(1)
                value = match.group(2).strip()
                current_value = [value] if value else []
        elif current_key and line.startswith("  "):
            current_value.append(line.strip())

    if current_key:
        frontmatter[current_key] = "\n".join(current_value).strip()

    return frontmatter, body


def validate_name(name: str) -> list[str]:
    """Validate skill name format."""
    issues = []
    if not name:
        issues.append("Missing required field: name")
        return issues

    if len(name) > 64:
        issues.append(f"Name exceeds 64 characters: {len(name)}")

    if not re.match(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$", name):
        issues.append("Name must be lowercase alphanumeric with hyphens, cannot start/end with hyphen")

    if "--" in name:
        issues.append("Name cannot contain consecutive hyphens")

    return issues


def validate_description(description: str) -> list[str]:
    """Validate description field."""
    issues = []
    if not description:
        issues.append("Missing required field: description")
        return issues

    if len(description) > 1024:
        issues.append(f"Description exceeds 1024 characters: {len(description)}")

    # Check for WHEN pattern
    if "WHEN" not in description.upper():
        issues.append("Recommendation: Include 'WHEN to use' in description for better triggering")

    return issues


def validate_skill(skill_path: Path) -> dict:
    """Validate a skill directory."""
    issues = []
    warnings = []

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        issues.append("Missing required file: SKILL.md")
        return {"valid": False, "issues": issues, "warnings": warnings}

    content = skill_md.read_text()
    frontmatter, body = parse_frontmatter(content)

    # Validate required fields
    issues.extend(validate_name(frontmatter.get("name", "")))
    issues.extend(validate_description(frontmatter.get("description", "")))

    # Check token count
    char_count = len(content)
    token_estimate = char_count // 4
    if token_estimate > 5000:
        warnings.append(f"SKILL.md exceeds ~5K tokens ({token_estimate} estimated). Consider using references/")

    # Check directory structure
    if (skill_path / "agents").exists():
        warnings.append("Agents should be at .claude/agents/, not inside skill folder")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "warnings": warnings,
        "frontmatter": frontmatter,
        "estimated_tokens": token_estimate,
    }


def main():
    parser = argparse.ArgumentParser(description="Validate a skill")
    parser.add_argument("skill_path", help="Path to skill directory")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)

    if not skill_path.exists():
        print(json.dumps({"error": f"Path not found: {skill_path}"}))
        sys.exit(1)

    result = validate_skill(skill_path)
    print(json.dumps(result, indent=2))

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
