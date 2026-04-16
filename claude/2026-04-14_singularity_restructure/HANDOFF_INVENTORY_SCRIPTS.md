# Handoff: Singularity Engagement Inventory Scripts

**From:** Session that completed the Singularity skill folder restructure (2026-04-16)
**To:** New Claude session to build the inventory scripts
**Skill location:** `.claude/skills/singularity/`

---

## What You're Building

A set of Python scripts that generate an inventory of any Singularity engagement folder. The scripts produce markdown files in tree-view format that document what exists in the engagement. These are current-state snapshots that get overwritten each time the scripts run.

## Output Files

The scripts produce files in `<engagement>/inventory/`:

| File | What It Contains |
|------|-----------------|
| `master_map.md` | Complete tree of every file in the engagement — source, research, deliverables, presentations, planning, tracking, sub-singularities, everything |
| `markdown_inventory.md` | Tree of all `.md` files only |
| `non_markdown_inventory.md` | Tree of all non-`.md` files (HTML, py, xlsx, txt, images, etc.) |
| `folder_descriptions.md` | Tree of folders only, each with a brief description of what it contains and when it was last updated (based on most recent file modification in that folder) |
| `sub_<name>.md` | One file per sub-singularity (e.g., `sub_team.md`) with a focused tree view of just that sub-singularity's contents. Only created if sub-singularities exist. |

All files use tree-view format (the `├──` / `└──` style).

## Script Design

Scripts live at `.claude/skills/singularity/scripts/` and take an engagement path as input:

```bash
python3 .claude/skills/singularity/scripts/generate_inventory.py <engagement_path>
```

This can be a single script that produces all output files, or a module with separate functions — use your judgment on what's cleanest. The script should:

- Accept an absolute or relative path to an engagement root folder
- Create the `inventory/` folder if it doesn't exist
- Overwrite existing inventory files (these are snapshots, not append-only)
- Detect sub-singularities automatically (folders that contain their own `research/00_methodology_*.md`)
- Generate the sub-singularity files only when sub-singularities exist
- Handle edge cases: empty folders, missing expected folders, engagements with no deliverables yet

## What a Singularity Engagement Looks Like

Read `.claude/skills/singularity/references/folder_structure.md` for the canonical structure. The key folders:

```
<client>/<opportunity>/
├── org_chart.md
├── source/                    # Raw input files
├── research/                  # Blockchain-style decomposition (numbered, append-only)
├── planning/                  # Skill notes, session handoffs, glossary
├── pricing/                   # Pricing specs, workbooks
├── deliverables/              # Client-facing documents (md + html)
├── presentations/             # Slide decks
├── decisions/                 # Open questions, agreed decisions
├── progress/                  # Status tracking
├── inventory/                 # <-- YOU ARE BUILDING THIS
└── team/                      # Sub-singularity (if exists)
    ├── source/
    ├── research/
    ├── tracking/
    ├── documents/
    ├── planning/
    └── cross_reference.md
```

## Folder Descriptions Logic

For `folder_descriptions.md`, each folder needs:
- The folder name
- A brief description of its purpose (derive from the folder name and contents — `research/` is "Blockchain-style research decomposition", `source/` is "Raw input files", etc.)
- Last updated date (the most recent file modification timestamp in that folder, not recursive into subfolders)

Use the canonical descriptions from `references/folder_structure.md` where possible.

## Test Engagements

Use these real engagements to test against:

1. **Lam Research IP Protection** — `lam_research/ip_protection/` — Full engagement with source, research (3 sets + bridge docs), deliverables (HTML + md), presentations (discovery deck), planning, pricing. No sub-singularity.

2. **Cisco CI/CD** — `cisco/cicd/` — Engagement with a `team/` sub-singularity. Has source, research, deliverables, presentations (srinivas status deck), and the team sub-singularity with its own research chain and tracking docs.

3. **Sephora QA/QE** — `sephora/qa_qe_playwright/` — Engagement with deliverables, planning, research, and charts. No sub-singularity.

Run the script against all three and verify the output makes sense.

## Behavioral Rules

- Read `.claude/skills/singularity/references/hard_rules.md` before starting work
- Read files before describing them (B4)
- Propose script structure before writing code (B7)
- Do not invent requirements that aren't in this handoff (B2)
- Ask Colin if anything is unclear rather than guessing

## What Success Looks Like

1. A script (or module) at `.claude/skills/singularity/scripts/` that generates inventory files
2. The script works against all 3 test engagements and produces correct, readable output
3. Tree views are properly formatted and complete
4. Sub-singularity detection works automatically
5. Folder descriptions are accurate and include last-updated dates
6. The inventory folder is documented in `references/folder_structure.md` as part of the canonical engagement structure
