# Singularity Skill Restructure — Session TODO

**Date:** 2026-04-14
**Goal:** Redesign the Singularity skill's folder structure

---

## Phase 1: Planning and Discussion — COMPLETE

- [x] Read handoff documents and hard rules
- [x] Explore actual skill folder structure
- [x] Write structure analysis
- [x] Write formal restructure plan
- [x] Discuss all 5 feedback points from previous session
- [x] Resolve all 4 decision points
- [x] Get Colin's approval on plan

## Phase 2: File Moves — COMPLETE

- [x] Create new directory structure
- [x] Move gold_standards (deliverables, presentations/team_status_update, charts, knowledge_transfer)
- [x] Copy new gold standards (Masterminds → ai_education, Ariat → capabilities_pitch)
- [x] Move layout_examples (7 files renamed, + chevron_flow_detail from Ariat)
- [x] Move worked_examples (lam_research, cisco_team)
- [x] Move templates (methodology_template, ProjectCostingTemplate, excel_template_prompt)
- [x] Move mermaid_shape_library (8 HTML files)
- [x] Move bayone_design_spec.md to references
- [x] Copy bayone_team.md into references, delete original from .claude/context/
- [x] Copy mermaid reference docs from sephora (3 files)
- [x] Delete proposal_template.html
- [x] Delete .claude/context/bayone_team.md
- [x] Remove empty assets/ directory
- [x] Remove old references/worked_example and references/worked_example_team
- [x] Colin verified file structure looks good

## Phase 3: READMEs — COMPLETE

- [x] Write gold_standards/deliverables/README.md
- [x] Update gold_standards/presentations/team_status_update/README.md
- [x] Write gold_standards/presentations/ai_education/README.md
- [x] Write gold_standards/presentations/capabilities_pitch/README.md
- [x] Write gold_standards/charts/README.md
- [x] Write gold_standards/knowledge_transfer/README.md
- [x] Write layout_examples/README.md (index with layout descriptions)
- [ ] **PAUSED** — Colin wants to add more gold standard files and test the setup

## Phase 4: Path Updates — COMPLETE

- [x] Update SKILL.md — all internal paths
- [x] Update scripts/singularity_stop.py — path construction AND error message strings
- [x] Update references/presentation_design_language.md — 11 path edits + 5 filename renames + removed 3 never-created file references
- [x] Update references/mermaid_design_standards.md
- [x] Update references/deliverables_pipeline.md
- [x] Update references/skill_ecosystem.md
- [x] Update references/sales_forge_merger.md
- [x] Update references/nested_singularity.md
- [x] Update references/bayone_team.md
- [x] Update references/tracking_folder_pattern.md
- [x] Update references/team_meeting_processing.md
- [x] Update references/pricing_workflow.md
- [x] Update references/enforcement_architecture.md

## Phase 5: Pending Path Issues (from handoff)

- [ ] Issue 3: `flag_ai_patterns.py` — in big4 skill, not singularity. Decide: copy, reference, or remove
- [ ] Issue 5: `example_definition_bar.html` — referenced in presentation_design_language.md but never created. Remove reference or create
- [ ] Issue 6: `example_two_column.html` — same as issue 5
- [ ] Issue 7: `example_evolution_row.html` — same as issue 5
- [ ] Issue 9: `resource_plan_for_cisco.html` — referenced in deliverables_pipeline.md but not in gold standards
- [ ] Issue 10: `bayone_positioning.md` — referenced in deliverables_pipeline.md but doesn't exist

## Phase 6: Final Verification — COMPLETE

- [x] Regenerate complete_structure.md from actual file system (260 files, 33 directories)
- [x] Full path audit: grepped all .md and .py files for old paths. Only remaining hits are frozen worked_example snapshots (expected) and sales-forge migration mapping tables (historical documentation, not active paths).
- [ ] Verify stop hook still works (run singularity_stop.py against a test engagement) — deferred until next skill invocation
- [ ] Verify all 11 B2 audit items are actually resolved in the files — deferred to next session

## Phase 7: New Feature — Source Folder Date Organization

Colin wants source folders organized by week and day to prevent file jumbles:
```
source/week_2026-04-14/day_2026-04-16/
```
- Week folders use the Monday date of that week
- Day folders are the date files were uploaded to Claude/repo, NOT the date of the source material itself
- README must clarify this distinction
- Applies to all singularities and sub-singularities
- Skill should create this structure automatically when processing new source material
- **Person subfolders** within day folders for team sub-singularities only (e.g., `day_2026-04-16/srinivas/`). Prevents "whose file is this?" confusion when multiple people upload. NOT created for main engagement singularities (typically one person uploading).
- Need to update folder_structure.md, SKILL.md, and nested_singularity.md

## Phase 7b: New Feature — Singularity Health Check and Remediation — COMPLETE

- [x] Created `references/health_check_methodology.md` — full audit checklist with 8 sections, mandatory pre-audit reading list, output format for both health check and remediation plan
- [x] Added Flow 8 (Audit) to SKILL.md — invocation menu option, hard gate on reading skill spec before auditing, process steps, load references
- [x] Key requirement enforced: Claude must read the skill definition first — SKILL.md and reference docs are the sole source of truth. No assumptions about what an engagement should look like.

## Phase 8: New Feature — Master Inventory Scripts — COMPLETE

Built by a separate Claude session. Script at `.claude/skills/singularity/scripts/generate_inventory.py`.
Design doc at `.claude/skills/singularity/references/inventory_design.md`.

Produces 4-5 files in `<engagement>/inventory/`: master_map.md, markdown_inventory.md, non_markdown_inventory.md, folder_descriptions.md, and sub_<name>.md per sub-singularity.

Tested against Lam Research, Cisco CI/CD (with sub-singularity), and Sephora QA/QE. All passing.

- [x] Discuss and agree on exact requirements
- [x] Create handoff document with full context
- [x] Create kickoff prompt for the new session
- [x] Build and test the scripts (completed by other session)
- [x] Document assumptions (references/inventory_design.md)
- [x] Update folder_structure.md with inventory/ folder

## Open Questions (from handoff, not blocking restructure)

- [x] Q1: What does `client/` mean as a folder concept? — RESOLVED: Not needed. The existing deliverables/ and presentations/ split already handles the distinction.
- [x] Q2: Gold standard treatment for deliverables — RESOLVED: Less urgent now. Pricing gold standards added. Chain concept covered by worked example. Evolution tracking deferred until multiple weeks of status decks exist.
- [x] Q3: Depth of methodology enforcement — RESOLVED: Current depth is fine. No changes needed.
- [x] Q4: When to offer vs enforce sub-singularity creation — RESOLVED: Current "offer when relevant" behavior is correct. Offer when a team meeting arrives and no sub-singularity exists. Don't front-load at engagement creation, don't auto-detect.
- [x] Q5: Cross-engagement learning layer — RESOLVED: Scope creep. Cross-engagement learning should be organic and human-driven, not prescriptive by AI. Premature.
- [x] Q6: Backup/recovery for blockchain chains — RESOLVED: Non-issue. Git handles recovery. No additional mechanism needed.

## Feedback Log

### Previous session feedback review (2026-04-14)

**Point 1 — `proposal_template.html`:** DELETE. Colin confirmed no value. The gold standard HTMLs are better starting points because they show content structure, not just an empty CSS shell. When producing a new deliverable, start from the relevant gold standard rather than a blank template.

**Point 2 — Gold standards and layout examples are separate concepts:**
- **Gold standards** are the best available representations of a given output format using real production-quality content. They can be complete decks, single HTML documents (like proposals), individual slides, or any other format the skill produces. They are NOT limited to complete decks.
- Gold standards are categorized by purpose (team status update, AI education, capabilities pitch, proposal, information request, etc.)
- Each gold standard folder gets a README explaining what files are there and how they're meant to be used. The skill MUST update these READMEs if the files change.
- **Layout examples** are a separate concept — individual slides extracted from across all decks showing unique layout patterns (chevron flow, split panel, card grid, etc.). These are visual vocabulary for building new slides.
- Layout examples get a lookup/index document describing each layout pattern with a visual representation so you can find the right one without reading every file.
- Sources identified so far: Masterminds deck (blue, AI education), Ariat foundational slides (purple, capabilities pitch), Srinivas deck (blue, team status update)
- `proposal_template.html` — deleted, no value
- `srinivas_status` is not a valid folder name — use descriptive purpose-based names

**Point 3 — Frozen-snapshot header on `skill_notes.md`:** Acknowledged. Header stays intact during move. Paths it references point outside the skill (to `claude/singularity_feedback/` and live Lam engagement) — unaffected by restructure.

**Point 4 — `bayone_team.md` moves INTO the skill:**
- `.claude/context/bayone_team.md` should move into `references/bayone_team.md` inside the Singularity skill
- Self-contained principle (Structural Rule 10) trumps the speculative "shared across skills" design
- YAGNI: no other skill actually references it. The "referenced by multiple skills" note was aspirational.
- Delete the original from `.claude/context/` after moving
- Update active references in: SKILL.md (2), deliverables_pipeline.md (1), sales_forge_merger.md (1), skill_ecosystem.md (4)
- Frozen worked_example files are not updated (historical snapshots)

**Point 5 — Duplicate deliverable HTMLs in worked example:** KEEP BOTH. It is natural and correct that worked example deliverables also appear in gold standards — that's how gold standards originate. The worked example copy shows what a complete engagement looks like. The gold standards copy makes it findable by category. Both purposes are valid. This is not a duplication problem to solve.

**Colin's warning on plan edits:** Use surgical, targeted edits only. Do not reword or change anything unrelated to the specific change being made. Do not use Write to replace the whole file. Edit tool with precise old_string/new_string only.

---
