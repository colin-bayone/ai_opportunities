#!/usr/bin/env python3
"""
Singularity Stop Hook (Skill-Scoped)

This hook is defined in the SKILL.md frontmatter, so it ONLY fires
when singularity is active. No marker file needed, no guard logic.

Verifies engagement artifacts exist using the Proof via Artifact pattern:
1. Methodology doc exists in research/
2. Org chart exists (if research has started)
3. Summary docs exist (if research files beyond methodology exist)
4. Presentation design references were read (if presentation files were generated)
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

    # Check 3: Hard rules file exists
    skill_dir = cwd / ".claude" / "skills" / "singularity"
    hard_rules = skill_dir / "references" / "hard_rules.md"
    if not hard_rules.exists():
        issues.append(
            "Behavioral hard rules file is missing at "
            ".claude/skills/singularity/references/hard_rules.md. "
            "This file must exist and be read at the start of every invocation."
        )

    # Check 4: Presentation design references gate
    # If presentation HTML files exist in this engagement, verify the
    # design language spec and example slides exist in the skill assets.
    # The actual "did the session read them" enforcement is in the SKILL.md
    # instructions (hard gate). This hook verifies the assets themselves
    # are present so generation cannot proceed without them.
    presentation_dirs = list(engagement_root.glob("presentations/*"))
    presentation_html = list(engagement_root.glob("presentations/**/*.html"))
    if presentation_html:
        skill_dir = cwd / ".claude" / "skills" / "singularity"
        spec_file = skill_dir / "references" / "presentation_design_language.md"
        examples_dir = skill_dir / "layout_examples"

        if not spec_file.exists():
            issues.append(
                "Presentation HTML files exist but the design language spec is missing at "
                ".claude/skills/singularity/references/presentation_design_language.md. "
                "The spec must be read before generating presentations."
            )

        if not examples_dir.exists() or not list(examples_dir.glob("*.html")):
            issues.append(
                "Presentation HTML files exist but no example slides found at "
                ".claude/skills/singularity/layout_examples/. "
                "Example slides must be read before generating presentations."
            )

        gold_standard_dir = skill_dir / "gold_standards" / "presentations" / "team_status_update"
        if not gold_standard_dir.exists():
            issues.append(
                "Presentation HTML files exist but the gold standard deck is missing at "
                ".claude/skills/singularity/gold_standards/presentations/team_status_update/. "
                "The gold standard must be read before generating presentations."
            )

    # Check 5: Sub-singularity references gate
    # If sub-singularity folders exist, verify the nested_singularity reference exists
    team_methodology = list(engagement_root.glob("*/research/00_methodology_*.md"))
    if team_methodology:
        nested_ref = skill_dir / "references" / "nested_singularity.md"
        if not nested_ref.exists():
            issues.append(
                "Sub-singularity folders exist but nested_singularity.md reference is missing at "
                ".claude/skills/singularity/references/nested_singularity.md."
            )

    # Check 6: Chart back button verification
    chart_dirs = list(engagement_root.glob("presentations/*/charts"))
    for chart_dir in chart_dirs:
        for chart_file in chart_dir.glob("*.html"):
            content = chart_file.read_text()
            if 'class="back-btn"' not in content:
                issues.append(
                    f"Chart file {chart_file.name} in {chart_dir} is missing a back button "
                    "(class='back-btn'). All chart pages must have a back button."
                )

    if issues:
        print(
            "Singularity workflow check:\n- " + "\n- ".join(issues),
            file=sys.stderr
        )
        sys.exit(2)

    # Auto-regenerate engagement inventory after all checks pass
    inventory_script = skill_dir / "scripts" / "generate_inventory.py"
    if inventory_script.exists():
        import subprocess
        try:
            subprocess.run(
                [sys.executable, str(inventory_script), str(engagement_root)],
                timeout=30,
                capture_output=True
            )
        except (subprocess.TimeoutExpired, Exception):
            pass  # Inventory generation is best-effort, never blocks the workflow

    sys.exit(0)


if __name__ == "__main__":
    main()
