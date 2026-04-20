# Path Verification: complete_structure.md vs Disk

**Source:** `.claude/skills/singularity/references/complete_structure.md`
**Skill root:** `.claude/skills/singularity/`
**Date:** 2026-04-13

---

## Section 1: Skill File Structure (lines 16-66)

The tree documents paths relative to `.claude/skills/singularity/`.

| Documented Path | EXISTS | Notes |
|---|---|---|
| `SKILL.md` | YES | |
| `references/` | YES | directory |
| `references/blockchain_methodology.md` | YES | |
| `references/document_processing_workflow.md` | **NO** | Actual file is `document_processing.md` (name mismatch) |
| `references/folder_structure.md` | YES | |
| `references/people_tracking.md` | YES | |
| `references/agent_architecture.md` | YES | |
| `references/deliverables_pipeline.md` | YES | |
| `references/pricing_workflow.md` | YES | |
| `references/session_continuity.md` | YES | |
| `references/anti_patterns.md` | YES | |
| `references/professional_standards.md` | YES | |
| `references/hard_rules.md` | YES | |
| `references/enforcement_architecture.md` | YES | |
| `references/nested_singularity.md` | YES | |
| `references/team_meeting_processing.md` | YES | |
| `references/tracking_folder_pattern.md` | YES | |
| `references/presentation_design_language.md` | YES | |
| `references/mermaid_design_standards.md` | YES | |
| `references/mermaid_shape_library.md` | YES | |
| `references/reorganization_guide.md` | YES | |
| `references/worked_example/` | YES | directory |
| `references/worked_example_team/` | YES | directory |
| `assets/` | YES | directory |
| `assets/templates/` | YES | directory |
| `assets/templates/deliverable_template.html` | **NO** | File does not exist; actual templates are `proposal_template.html` and `methodology_template.md` |
| `assets/templates/ProjectCostingTemplate.xlsx` | YES | |
| `assets/prompts/` | YES | directory |
| `assets/prompts/excel_template_prompt.md` | YES | |
| `assets/slide_examples/` | YES | directory; contains 7 example HTML files |
| `assets/design/` | YES | directory |
| `assets/design/bayone_design_spec.md` | YES | |
| `assets/design/gold_standards/` | YES | directory |
| `assets/design/gold_standards/problem_restatement.html` | YES | |
| `assets/design/gold_standards/information_request.html` | YES | |
| `assets/design/gold_standards/preliminary_approach.html` | YES | |
| `assets/design/gold_standards/presentations/srinivas_status/` | YES | directory; contains 8 slides + README + charts/ |
| `assets/design/gold_standards/knowledge_transfer/` | YES | directory |
| `assets/design/gold_standards/knowledge_transfer/session_0_platform_overview.html` | YES | |
| `assets/design/gold_standards/knowledge_transfer/charts/` | YES | directory; contains 3 files (architecture_overview.html, candidate_data_flow.html, fishbone_apps.html) |
| `assets/design/gold_standards/charts/example_ecosystem_diagram.html` | YES | |
| `scripts/` | YES | directory |
| `scripts/singularity_stop.py` | YES | |
| `scripts/format_transcript.py` | YES | |
| `scripts/html_to_pdf.py` | YES | |
| `scripts/flag_ai_patterns.py` | **NO** | File does not exist on disk |

---

## Section 2: Files on Disk NOT in the Documented Tree

These files exist under `.claude/skills/singularity/` but are absent from the tree in `complete_structure.md`.

| Undocumented Path | Type | Notes |
|---|---|---|
| `references/complete_structure.md` | file | This document itself (meta, reasonable omission) |
| `references/document_processing.md` | file | Likely the actual file for the documented `document_processing_workflow.md` |
| `references/asshole.txt` | file | Not documented |
| `references/image.png` | file | Not documented |
| `references/sales_forge_merger.md` | file | Not documented |
| `references/skill_ecosystem.md` | file | Not documented |
| `assets/templates/methodology_template.md` | file | Not documented |
| `assets/templates/proposal_template.html` | file | Not documented (may be the replacement for `deliverable_template.html`) |
| `assets/mermaid_shape_library/` | directory | Not documented (8 HTML files: 01-08 shape library reference pages) |
| `assets/mermaid_shape_library/01_classic_shapes.html` | file | |
| `assets/mermaid_shape_library/02_v11_shapes.html` | file | |
| `assets/mermaid_shape_library/03_arrows_and_edges.html` | file | |
| `assets/mermaid_shape_library/04_text_formatting.html` | file | |
| `assets/mermaid_shape_library/05_icons_reference.html` | file | |
| `assets/mermaid_shape_library/06_classdef_styling.html` | file | |
| `assets/mermaid_shape_library/07_subgraphs_and_layout.html` | file | |
| `assets/mermaid_shape_library/08_diagram_types_gallery.html` | file | |
| `assets/design/gold_standards/bridge_document_example.md` | file | Not documented |
| `assets/design/gold_standards/poc_proposal_v5.html` | file | Not documented |
| `assets/design/gold_standards/poc_proposal_v5_detailed.html` | file | Not documented |
| `assets/design/gold_standards/presentations/srinivas_status/README.md` | file | Not in tree (internal doc) |
| `assets/design/gold_standards/presentations/srinivas_status/charts/` | directory | Not documented |
| `assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html` | file | Not documented |
| `references/worked_example/decisions/` | directory | Empty directory, not shown in tree |
| `references/worked_example/progress/` | directory | Empty directory, not shown in tree |
| `references/worked_example/planning/skill_spec/` | directory + 14 files | Entire subdirectory not documented |
| `references/worked_example/deliverables/02_discovery_call_2026-03-12/README.md` | file | Not documented |
| `references/worked_example_team/documents/` | directory | Empty; not in tree |
| `references/worked_example_team/planning/` | directory | Empty; not in tree |
| `references/worked_example_team/source/` | directory | Empty; not in tree |

---

## Section 3: Summary

### Missing from disk (documented but not found): 3

1. **`references/document_processing_workflow.md`** -- Actual file is `document_processing.md` (name mismatch)
2. **`assets/templates/deliverable_template.html`** -- Does not exist; `proposal_template.html` and `methodology_template.md` are present instead
3. **`scripts/flag_ai_patterns.py`** -- Does not exist on disk at all

### Undocumented on disk (found but not in tree): 28 items

Broken into categories:

- **Reference docs (4):** `complete_structure.md` (self), `asshole.txt`, `image.png`, `sales_forge_merger.md`, `skill_ecosystem.md`
- **Filename mismatch (1):** `document_processing.md` (documented as `document_processing_workflow.md`)
- **Template additions (2):** `methodology_template.md`, `proposal_template.html`
- **Entire new directory (8 files):** `assets/mermaid_shape_library/` with 8 HTML reference pages
- **Gold standard additions (3):** `bridge_document_example.md`, `poc_proposal_v5.html`, `poc_proposal_v5_detailed.html`
- **Presentation sub-items (2):** `srinivas_status/README.md`, `srinivas_status/charts/build_log_ecosystem.html`
- **Worked example extras (3):** `decisions/` (empty), `progress/` (empty), `planning/skill_spec/` (14 files)
- **Worked example team extras (3):** `documents/`, `planning/`, `source/` (all empty directories)
- **Worked example deliverables (1):** `02_discovery_call_2026-03-12/README.md`

### Recommended Fixes

1. Rename `document_processing_workflow.md` to `document_processing.md` in tree, or rename the file on disk
2. Update `deliverable_template.html` to `proposal_template.html` in tree, or rename the file; also add `methodology_template.md`
3. Either create `scripts/flag_ai_patterns.py` or remove it from the tree
4. Add `assets/mermaid_shape_library/` directory (8 HTML files) to tree
5. Add `references/sales_forge_merger.md` and `references/skill_ecosystem.md` to tree
6. Add gold standard files: `bridge_document_example.md`, `poc_proposal_v5.html`, `poc_proposal_v5_detailed.html`
7. Add `presentations/srinivas_status/charts/` and its `build_log_ecosystem.html` to tree
8. Add `assets/templates/methodology_template.md` and `assets/templates/proposal_template.html` to tree
9. Consider documenting worked_example `planning/skill_spec/` subdirectory (14 files)
10. Consider noting `references/asshole.txt` and `references/image.png` or removing them
