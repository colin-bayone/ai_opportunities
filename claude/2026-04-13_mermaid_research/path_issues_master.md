# Path Issues — Master List

**Date:** 2026-04-14
**Source:** 5 parallel verification agents + manual repository search
**Status:** Information gathered. No changes made.

---

## Issue 1: `complete_structure.md` — `document_processing_workflow.md` name mismatch

- **Documented as:** `references/document_processing_workflow.md`
- **Actual file on disk:** `references/document_processing.md`
- **Repository search:** Found at `.claude/skills/singularity/references/document_processing.md`
- **Verdict:** File exists but with a shorter name. The tree documents the wrong filename.

## Issue 2: `complete_structure.md` — `deliverable_template.html` missing

- **Documented as:** `assets/templates/deliverable_template.html`
- **Repository search:** No file named `deliverable_template.html` found anywhere in the repository.
- **Files that DO exist in `assets/templates/`:** `proposal_template.html`, `methodology_template.md`, `ProjectCostingTemplate.xlsx`
- **Verdict:** The documented filename does not exist. It may have been renamed to `proposal_template.html` at some point, or it may be a different file entirely. Needs clarification.

## Issue 3: `complete_structure.md` — `flag_ai_patterns.py` missing from singularity scripts

- **Documented as:** `scripts/flag_ai_patterns.py`
- **Actual location on disk:** `.claude/skills/big4/scripts/flag_ai_patterns.py` (in the big4 skill, not singularity)
- **In singularity scripts folder:** NOT present. Only `singularity_stop.py`, `format_transcript.py`, and `html_to_pdf.py` exist there.
- **Verdict:** The file exists in the repository but in a different skill (big4). The complete_structure.md documents it as being in singularity's scripts folder, but it is not there. Either it needs to be copied over, or the tree should reference the big4 location, or it should be removed from the tree.

## Issue 4: `complete_structure.md` — 28 files on disk not in the documented tree

- **Notable undocumented items:**
  - `assets/mermaid_shape_library/` (8 HTML files)
  - `references/sales_forge_merger.md`
  - `references/skill_ecosystem.md`
  - `assets/design/gold_standards/bridge_document_example.md`
  - `assets/design/gold_standards/poc_proposal_v5.html`
  - `assets/design/gold_standards/poc_proposal_v5_detailed.html`
  - `assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html`
  - `references/worked_example/planning/skill_spec/` (14 files)
  - `assets/templates/methodology_template.md`
  - `assets/templates/proposal_template.html`
  - `references/asshole.txt`
  - `references/image.png`
- **Verdict:** The tree is out of date. These files exist and should be documented, or the tree needs a full refresh to match reality.

## Issue 5: `presentation_design_language.md` — `example_definition_bar.html` referenced but not created

- **Referenced in:** Example Layout Patterns section, line 309
- **Repository search:** No file named `example_definition_bar.html` found anywhere.
- **Verdict:** This slide example was referenced in the spec when the layout patterns were documented but was never created as one of the 7 example HTML files. Either create it or remove the reference.

## Issue 6: `presentation_design_language.md` — `example_two_column.html` referenced but not created

- **Referenced in:** Example Layout Patterns section, line 309
- **Repository search:** No file named `example_two_column.html` found anywhere.
- **Verdict:** Same as issue 5. Referenced but never created.

## Issue 7: `presentation_design_language.md` — `example_evolution_row.html` referenced but not created

- **Referenced in:** Example Layout Patterns section, line 309
- **Repository search:** No file named `example_evolution_row.html` found anywhere.
- **Verdict:** Same as issues 5-6. Referenced but never created.

## Issue 8: `presentation_design_language.md` — inconsistent path prefixes

- **Some references use:** `gold_standards/presentations/srinivas_status/`
- **Other references use:** `assets/design/gold_standards/presentations/srinivas_status/`
- **The actual full path from skill root is:** `assets/design/gold_standards/presentations/srinivas_status/`
- **Verdict:** The shorter prefix works for human reading but would break automated path resolution. Should be made consistent.

## Issue 9: `deliverables_pipeline.md` — `resource_plan_for_cisco.html` gold standard missing from skill

- **Referenced as:** `.claude/skills/singularity/assets/design/gold_standards/resource_plan_for_cisco.html`
- **Repository search:** Found at two locations:
  - `claude/2026-02-02_resource-planning/deliverables/resource_plan_for_cisco.html`
  - `cisco/cicd/archive/planning/2026-02-02_resource_planning/deliverables/resource_plan_for_cisco.html`
- **In the skill's gold_standards folder:** NOT present.
- **Verdict:** The file exists in the repository but was never copied into the skill's gold standards. The reference in deliverables_pipeline.md labels it "(silver)" suggesting it was acknowledged as not yet promoted to gold standard status.

## Issue 10: `deliverables_pipeline.md` — `bayone_positioning.md` missing

- **Referenced as:** `.claude/context/bayone_positioning.md`
- **Repository search:** No file named `bayone_positioning.md` found anywhere.
- **Note:** `.claude/context/bayone_team.md` DOES exist.
- **Verdict:** This file was referenced but may never have been created, or it may have been named something different. The reference predates this session's work.
