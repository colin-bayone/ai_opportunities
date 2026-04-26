#!/usr/bin/env python3
"""
Singularity Stop Hook (Skill-Scoped)

This hook is defined in the SKILL.md frontmatter, so it ONLY fires
when singularity is active. No marker file needed for scope, no guard logic.

Verifies engagement artifacts exist using the Proof via Artifact pattern:
1. Methodology doc exists in research/
2. Org chart exists (if research has started)
3. Per-set summary completion (each completed set has a summary; the most
   recent set is exempt if a research/.set_<N>_in_progress marker exists)
4. Presentation design references exist (if presentation files were generated)
5. Sub-singularity references exist (if sub-singularity folders exist)
6. Chart back buttons present (if chart HTML files exist)
"""

import json
import re
import sys
from pathlib import Path


SUMMARY_MIN_CHARS = 200

SET_PREFIX = re.compile(r'^(\d{2})([a-z])?_')
BRIDGE_PREFIX = re.compile(r'^\d{2}-\d{2}_')
SUMMARY_NAME = re.compile(r'^(\d{2})_summary_')


def check_set_completion(research_dir: Path) -> list[str]:
    """Group research files by set prefix and enforce summary completeness.

    Rules:
    - Files prefixed 00_ are the methodology (skipped).
    - Files matching NN-MM_ are bridge documents between sets (skipped).
    - Files matching NN_ or NNa_, NNb_ (letter suffix) belong to set NN.
      Letter suffixes are addenda, they inherit the parent set's summary.
    - A set is complete when a NN_summary_*.md file exists in research/
      with at least SUMMARY_MIN_CHARS of content.
    - The highest-numbered set is exempt from needing a summary if a marker
      file research/.set_NN_in_progress exists (the set is mid-processing).
    - Any set other than the highest-numbered MUST have a complete summary.
    """
    issues: list[str] = []
    if not research_dir.is_dir():
        return issues

    sets: dict[str, dict] = {}
    for entry in research_dir.iterdir():
        if not entry.is_file() or entry.suffix != ".md":
            continue
        name = entry.name
        if name.startswith("00_"):
            continue
        if BRIDGE_PREFIX.match(name):
            continue
        m = SET_PREFIX.match(name)
        if not m:
            continue
        prefix = m.group(1)
        bucket = sets.setdefault(prefix, {"summary": None, "files": []})
        bucket["files"].append(entry)
        summary_match = SUMMARY_NAME.match(name)
        if summary_match and summary_match.group(1) == prefix:
            try:
                size = entry.stat().st_size
            except OSError:
                size = 0
            if size >= SUMMARY_MIN_CHARS:
                bucket["summary"] = entry

    if not sets:
        return issues

    ordered = sorted(sets.keys())
    highest = ordered[-1]
    for prefix in ordered:
        bucket = sets[prefix]
        if bucket["summary"] is not None:
            continue
        marker = research_dir / f".set_{prefix}_in_progress"
        if prefix == highest and marker.exists():
            continue  # in-flight, exempt
        if prefix == highest:
            issues.append(
                f"Set {prefix} has no summary file (research/{prefix}_summary_<date>.md). "
                f"If this set is still being processed, create a marker at "
                f"research/.set_{prefix}_in_progress and the hook will allow the "
                f"in-flight state. Otherwise, write the summary to close the set."
            )
        else:
            issues.append(
                f"Set {prefix} is missing its summary file "
                f"(research/{prefix}_summary_<date>.md). "
                f"Every set prior to the most recent must be closed with a "
                f"summary of at least {SUMMARY_MIN_CHARS} characters before "
                f"additional sets are started."
            )
    return issues


def find_skill_dir(start: Path) -> Path | None:
    """Walk up from start until .claude/skills/singularity is found."""
    current = start.resolve()
    while True:
        candidate = current / ".claude" / "skills" / "singularity"
        if candidate.is_dir():
            return candidate
        if current.parent == current:
            return None
        current = current.parent


def main():
    data = json.load(sys.stdin)

    # Loop prevention
    if data.get("stop_hook_active", False):
        sys.exit(0)

    cwd = Path(data.get("cwd", "."))

    # Find engagement folders: look for research/00_methodology_*.md
    # Search one, two, and three levels deep from cwd so the hook behaves
    # correctly whether cwd is the project root, a client folder, or an
    # engagement folder.
    methodology_files = (
        list(cwd.glob("research/00_methodology_*.md")) +
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

    # Check 2: Per-set summary completion
    # Every completed set must have a summary file with minimum content.
    # The most recent (highest-numbered) set is exempt if a marker file
    # research/.set_<N>_in_progress exists, which indicates the set is
    # still being actively processed. Letter suffixes (01a, 01b, etc.)
    # inherit their parent set's summary and do not need their own.
    issues.extend(check_set_completion(engagement_root / "research"))

    # Apply the same per-set check to any sub-singularities
    for sub_methodology in engagement_root.glob("*/research/00_methodology_*.md"):
        sub_research = sub_methodology.parent
        issues.extend(check_set_completion(sub_research))

    # Check 3: Hard rules file exists
    skill_dir = find_skill_dir(cwd) or find_skill_dir(engagement_root)
    if skill_dir is None:
        sys.exit(0)
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
