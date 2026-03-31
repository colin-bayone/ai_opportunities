#!/usr/bin/env python3
"""
Singularity Stop Hook (Skill-Scoped)

This hook is defined in the SKILL.md frontmatter, so it ONLY fires
when singularity is active. No marker file needed, no guard logic.

Verifies engagement artifacts exist using the Proof via Artifact pattern:
1. Methodology doc exists in research/
2. Org chart exists (if research has started)
3. Summary docs exist (if research files beyond methodology exist)
"""

import json
import sys
from pathlib import Path


def main():
    data = json.load(sys.stdin)

    # Loop prevention
    if data.get("stop_hook_active", False):
        sys.exit(0)

    cwd = Path(data.get("cwd", "."))

    # Find engagement folders: look for research/00_methodology_*.md
    # Search two levels deep from cwd
    methodology_files = (
        list(cwd.glob("*/research/00_methodology_*.md")) +
        list(cwd.glob("*/*/research/00_methodology_*.md"))
    )

    if not methodology_files:
        # No active engagement found. This is fine during setup.
        sys.exit(0)

    # Check the most recently modified engagement
    methodology_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    engagement_root = methodology_files[0].parent.parent

    issues = []

    # Check 1: Org chart exists (only if research has progressed beyond methodology)
    research_files = list(engagement_root.glob("research/*.md"))
    org_chart = engagement_root / "org_chart.md"

    if len(research_files) > 1 and not org_chart.exists():
        issues.append(
            f"Missing org_chart.md at {engagement_root}/. "
            "Create it after processing the first source material."
        )

    # Check 2: Summary docs exist (if detail files exist)
    summary_files = list(engagement_root.glob("research/*_summary_*.md"))
    if len(research_files) > 1 and not summary_files:
        issues.append(
            "Research files exist but no summary document found. "
            "Each document set must end with a summary file."
        )

    if issues:
        print(
            "Singularity workflow check:\n- " + "\n- ".join(issues),
            file=sys.stderr
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
