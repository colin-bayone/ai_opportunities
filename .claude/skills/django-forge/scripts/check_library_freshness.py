#!/usr/bin/env python3
"""
Check if a Python library meets freshness requirements.

Requirements:
1. Must have been updated within the last 1 year from current date
2. Must have at least version 1.0.0 (production-ready)
3. Must have active maintenance (recent commits/releases)

Usage:
    python check_library_freshness.py django-htmx
    python check_library_freshness.py --check-pypi django-filter
    python check_library_freshness.py --check-github django/channels
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta
from typing import Optional


def get_current_context() -> dict:
    """Get current date context."""
    now = datetime.now()
    return {
        "current_date": now,
        "one_year_ago": now - timedelta(days=365),
        "current_year": now.year,
    }


def check_pypi(package_name: str) -> dict:
    """Check package info from PyPI."""
    try:
        result = subprocess.run(
            ["pip", "index", "versions", package_name],
            capture_output=True,
            text=True,
            timeout=30
        )
        # Parse output for available versions
        return {
            "source": "pypi",
            "package": package_name,
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None
        }
    except Exception as e:
        return {"error": str(e)}


def check_github_releases(repo: str) -> Optional[dict]:
    """Check GitHub releases for a repository."""
    try:
        result = subprocess.run(
            ["gh", "api", f"/repos/{repo}/releases/latest"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                "tag_name": data.get("tag_name"),
                "published_at": data.get("published_at"),
                "name": data.get("name"),
            }
        return None
    except Exception:
        return None


def check_github_commits(repo: str) -> Optional[dict]:
    """Check most recent commit date."""
    try:
        result = subprocess.run(
            ["gh", "api", f"/repos/{repo}/commits?per_page=1"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data:
                commit = data[0]
                return {
                    "sha": commit.get("sha", "")[:7],
                    "date": commit.get("commit", {}).get("committer", {}).get("date"),
                    "message": commit.get("commit", {}).get("message", "").split("\n")[0][:50],
                }
        return None
    except Exception:
        return None


def parse_version(version_str: str) -> tuple:
    """Parse version string into tuple for comparison."""
    # Remove common prefixes
    version_str = version_str.lstrip("v").lstrip("V")
    # Extract numeric parts
    parts = []
    for part in version_str.split("."):
        try:
            # Handle versions like "1.0.0rc1"
            numeric = ""
            for char in part:
                if char.isdigit():
                    numeric += char
                else:
                    break
            parts.append(int(numeric) if numeric else 0)
        except ValueError:
            parts.append(0)
    return tuple(parts[:3])  # Major, minor, patch


def is_version_production_ready(version: str) -> bool:
    """Check if version is >= 1.0.0."""
    major, minor, patch = parse_version(version)
    return major >= 1


def is_date_within_year(date_str: str, context: dict) -> bool:
    """Check if date is within the last year."""
    try:
        # Handle ISO format dates
        if "T" in date_str:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            date = date.replace(tzinfo=None)
        else:
            date = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return date >= context["one_year_ago"]
    except Exception:
        return False


def evaluate_library(package_name: str, github_repo: Optional[str] = None) -> dict:
    """
    Evaluate if a library meets freshness requirements.

    Returns evaluation result with:
    - meets_requirements: bool
    - version_ok: bool (>= 1.0.0)
    - freshness_ok: bool (updated within 1 year)
    - details: dict with findings
    """
    context = get_current_context()
    result = {
        "package": package_name,
        "evaluated_on": context["current_date"].strftime("%Y-%m-%d"),
        "requirements": {
            "min_version": "1.0.0",
            "max_staleness_days": 365,
            "freshness_cutoff": context["one_year_ago"].strftime("%Y-%m-%d"),
        },
        "version_ok": False,
        "freshness_ok": False,
        "meets_requirements": False,
        "details": {},
        "recommendation": "",
    }

    # Check GitHub if repo provided
    if github_repo:
        release = check_github_releases(github_repo)
        if release:
            result["details"]["latest_release"] = release
            if release.get("tag_name"):
                result["version_ok"] = is_version_production_ready(release["tag_name"])
            if release.get("published_at"):
                result["freshness_ok"] = is_date_within_year(release["published_at"], context)

        commits = check_github_commits(github_repo)
        if commits:
            result["details"]["latest_commit"] = commits
            # If no release but has recent commits, check commit date
            if commits.get("date"):
                commit_fresh = is_date_within_year(commits["date"], context)
                result["details"]["commits_fresh"] = commit_fresh
                # Only update freshness if we haven't already determined it from release
                if not result.get("freshness_ok"):
                    result["freshness_ok"] = commit_fresh

    # Final evaluation
    result["meets_requirements"] = result["version_ok"] and result["freshness_ok"]

    # Generate recommendation
    if result["meets_requirements"]:
        result["recommendation"] = f"APPROVED: {package_name} meets all requirements"
    else:
        issues = []
        if not result["version_ok"]:
            issues.append("version < 1.0.0 (not production-ready)")
        if not result["freshness_ok"]:
            issues.append(f"not updated since {context['one_year_ago'].strftime('%Y-%m-%d')}")
        result["recommendation"] = f"REJECTED: {package_name} - {', '.join(issues)}"

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Check if a library meets freshness requirements"
    )
    parser.add_argument("package", help="Package name to check")
    parser.add_argument("--github", "-g", help="GitHub repo (owner/repo)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    result = evaluate_library(args.package, args.github)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"\nLibrary Evaluation: {args.package}")
        print("=" * 50)
        print(f"Evaluated on: {result['evaluated_on']}")
        print(f"Freshness cutoff: {result['requirements']['freshness_cutoff']}")
        print()
        print(f"Version >= 1.0.0: {'Yes' if result['version_ok'] else 'No'}")
        print(f"Updated within 1 year: {'Yes' if result['freshness_ok'] else 'No'}")
        print()
        print(f"RESULT: {result['recommendation']}")

        if result["details"]:
            print("\nDetails:")
            if "latest_release" in result["details"]:
                r = result["details"]["latest_release"]
                print(f"  Latest release: {r.get('tag_name')} ({r.get('published_at', 'unknown')[:10]})")
            if "latest_commit" in result["details"]:
                c = result["details"]["latest_commit"]
                print(f"  Latest commit: {c.get('sha')} ({c.get('date', 'unknown')[:10]})")


if __name__ == "__main__":
    main()
