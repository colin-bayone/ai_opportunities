#!/usr/bin/env python3
"""
Docker Compose File Validator
Validates compose files against modern (2025) best practices.
Run: python compose_validator.py [compose_file]
"""

import sys
import re
import json
from pathlib import Path
from typing import Optional


class Issue:
    """Represents a validation issue."""
    
    def __init__(self, level: str, message: str, line: Optional[int] = None, fix: Optional[str] = None):
        self.level = level  # error, warning, info
        self.message = message
        self.line = line
        self.fix = fix
    
    def __repr__(self):
        icon = {"error": "🔴", "warning": "🟡", "info": "🔵"}.get(self.level, "⚪")
        line_info = f" (line {self.line})" if self.line else ""
        return f"{icon} [{self.level.upper()}]{line_info} {self.message}"


def find_compose_file(path: Path = Path(".")) -> Optional[Path]:
    """Find compose file in order of preference."""
    candidates = [
        "compose.yaml",
        "compose.yml",
        "docker-compose.yaml",
        "docker-compose.yml"
    ]
    
    for name in candidates:
        filepath = path / name
        if filepath.exists():
            return filepath
    
    return None


def validate_compose_file(filepath: Path) -> list[Issue]:
    """Validate a compose file and return issues."""
    issues = []
    
    content = filepath.read_text()
    lines = content.split('\n')
    
    # Check for version key (obsolete)
    for i, line in enumerate(lines, 1):
        if re.match(r'^version:\s*["\']?\d', line):
            issues.append(Issue(
                "warning",
                "The 'version' key is obsolete in Compose v2 - remove it",
                line=i,
                fix="Delete this line"
            ))
            break
    
    # Check for docker-compose in filename
    if "docker-compose" in filepath.name:
        issues.append(Issue(
            "info",
            f"Consider renaming '{filepath.name}' to 'compose.yaml' (preferred naming)",
            fix=f"mv {filepath.name} compose.yaml"
        ))
    
    # Check for latest tag
    latest_pattern = re.compile(r'image:\s*["\']?[\w\-/]+:latest["\']?')
    for i, line in enumerate(lines, 1):
        if latest_pattern.search(line):
            issues.append(Issue(
                "warning",
                f"Using ':latest' tag is not recommended - pin to specific version",
                line=i,
                fix="Change to specific version like ':16-alpine' or ':3.11-slim'"
            ))
    
    # Check for hardcoded passwords/secrets
    secret_patterns = [
        (r'password:\s*["\'][^$][^"\']+["\']', "Hardcoded password found"),
        (r'POSTGRES_PASSWORD:\s*["\'][^$][^"\']+["\']', "Hardcoded database password"),
        (r'SECRET_KEY:\s*["\'][^$][^"\']+["\']', "Hardcoded secret key"),
        (r'API_KEY:\s*["\'][^$][^"\']+["\']', "Hardcoded API key"),
    ]
    
    for i, line in enumerate(lines, 1):
        for pattern, message in secret_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(Issue(
                    "error",
                    f"{message} - use environment variable substitution",
                    line=i,
                    fix="Use ${VARIABLE_NAME} syntax and .env file"
                ))
    
    # Check for deprecated 'links'
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*links:', line):
            issues.append(Issue(
                "warning",
                "'links' is deprecated - use 'depends_on' and networks instead",
                line=i,
                fix="Replace with 'depends_on:' section"
            ))
    
    # Check for build without context
    in_build = False
    build_line = 0
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*build:\s*$', line):
            in_build = True
            build_line = i
        elif in_build and not re.match(r'\s+', line):
            in_build = False
            # Check if build was just 'build:' with no content
        elif re.match(r'\s*build:\s+["\']?\.$', line):
            # Simple build: . is fine but could be more explicit
            pass
    
    # Check for ports exposed as strings vs integers
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*-\s*\d+:\d+\s*$', line):
            issues.append(Issue(
                "info",
                "Consider quoting port mappings to avoid YAML parsing issues",
                line=i,
                fix='Use quotes: "8000:8000" instead of 8000:8000'
            ))
    
    # Check for depends_on without conditions
    simple_depends = False
    for i, line in enumerate(lines, 1):
        if re.match(r'\s*depends_on:', line):
            # Check next few lines for simple list vs condition
            for j in range(i, min(i + 5, len(lines))):
                next_line = lines[j]
                if re.match(r'\s+-\s+\w+\s*$', next_line):
                    simple_depends = True
                    issues.append(Issue(
                        "info",
                        "Consider using depends_on with conditions for better startup ordering",
                        line=j + 1,
                        fix="Use: service_name:\\n  condition: service_healthy"
                    ))
                    break
                elif "condition:" in next_line:
                    break
    
    # Check for missing healthchecks on key services
    services_without_healthcheck = []
    current_service = None
    has_healthcheck = False
    
    for line in lines:
        service_match = re.match(r'^  (\w+):', line)
        if service_match:
            if current_service and not has_healthcheck:
                if current_service in ['db', 'postgres', 'mysql', 'redis', 'web', 'api']:
                    services_without_healthcheck.append(current_service)
            current_service = service_match.group(1)
            has_healthcheck = False
        elif 'healthcheck:' in line:
            has_healthcheck = True
    
    # Check last service
    if current_service and not has_healthcheck:
        if current_service in ['db', 'postgres', 'mysql', 'redis', 'web', 'api']:
            services_without_healthcheck.append(current_service)
    
    for service in services_without_healthcheck:
        issues.append(Issue(
            "info",
            f"Service '{service}' has no healthcheck defined",
            fix="Add healthcheck section for better dependency management"
        ))
    
    # Check for container_name with deploy.replicas
    has_container_name = False
    has_replicas = False
    
    for line in lines:
        if 'container_name:' in line:
            has_container_name = True
        if 'replicas:' in line:
            has_replicas = True
    
    if has_container_name and has_replicas:
        issues.append(Issue(
            "error",
            "container_name conflicts with replicas - containers must have unique names",
            fix="Remove container_name when using replicas"
        ))
    
    return issues


def print_results(filepath: Path, issues: list[Issue]):
    """Print validation results."""
    print("=" * 60)
    print(f"COMPOSE FILE VALIDATION: {filepath}")
    print("=" * 60)
    print()
    
    if not issues:
        print("✅ No issues found!")
        print()
        print("=" * 60)
        return
    
    # Group by level
    errors = [i for i in issues if i.level == "error"]
    warnings = [i for i in issues if i.level == "warning"]
    infos = [i for i in issues if i.level == "info"]
    
    print(f"Found {len(issues)} issues:")
    print(f"  🔴 Errors: {len(errors)}")
    print(f"  🟡 Warnings: {len(warnings)}")
    print(f"  🔵 Info: {len(infos)}")
    print()
    
    for issue in errors + warnings + infos:
        print(str(issue))
        if issue.fix:
            print(f"   💡 Fix: {issue.fix}")
        print()
    
    print("=" * 60)


def main():
    # Find compose file
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        filepath = Path(sys.argv[1])
    else:
        filepath = find_compose_file()
    
    if not filepath or not filepath.exists():
        print("Error: No compose file found")
        print("Usage: python compose_validator.py [compose_file]")
        sys.exit(1)
    
    issues = validate_compose_file(filepath)
    
    if "--json" in sys.argv:
        output = {
            "file": str(filepath),
            "issues": [
                {
                    "level": i.level,
                    "message": i.message,
                    "line": i.line,
                    "fix": i.fix
                }
                for i in issues
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        print_results(filepath, issues)
    
    # Exit with error if there are errors
    if any(i.level == "error" for i in issues):
        sys.exit(1)


if __name__ == "__main__":
    main()
