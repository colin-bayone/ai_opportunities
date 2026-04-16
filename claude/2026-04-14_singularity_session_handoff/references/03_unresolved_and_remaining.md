# Unresolved Items, Remaining Work, and Open Decisions

**Date:** 2026-04-14
**Purpose:** Complete reference for any future session picking up the Singularity skill work. Covers every known unresolved item, pending decision, and remaining task as of the end of the 2026-04-10 through 2026-04-14 multi-day session.

---

## Table of Contents

1. [Folder Structure Redesign (Critical Priority)](#1-folder-structure-redesign-critical-priority)
2. [Path Issues Master List (10 Items)](#2-path-issues-master-list-10-items)
3. [Open Questions Awaiting Decisions (8 Items)](#3-open-questions-awaiting-decisions-8-items)
4. [Other Remaining Work Items](#4-other-remaining-work-items)
5. [Current Skill File Inventory (134 Files)](#5-current-skill-file-inventory-134-files)

---

## 1. Folder Structure Redesign (Critical Priority)

### Why This Needs to Happen

The Singularity skill's internal folder structure has become disorganized through incremental growth over multiple sessions. It was identified as the immediate next priority at the end of the 2026-04-10 to 2026-04-14 session. The problems are severe enough that the `complete_structure.md` documentation file no longer reflects reality.

### Specific Problems

**Excessive nesting depth.** The deepest paths in the skill reach 7+ directory levels. For example:

```
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html
```

That is `.claude/skills/singularity/` (3 levels of prefix) followed by `assets/design/gold_standards/presentations/srinivas_status/charts/` (6 more levels) for a total of 9 directory levels to reach a single HTML file. The `assets/design/gold_standards/` subtree alone contains three separate `charts/` folders at different nesting depths.

**Gold standards are split across two locations.** Some gold standard examples live under `references/worked_example/` and `references/worked_example_team/`, while others live under `assets/design/gold_standards/`. This split means a session looking for "how should this deliverable look" has to search two unrelated directory trees. There is no single location where all exemplar content is gathered.

**The `assets/` directory was introduced during this session and created the deep nesting.** Before this session, design-related files were more directly accessible. The introduction of `assets/design/` as an intermediate layer pushed everything one level deeper without a corresponding benefit.

**`complete_structure.md` is stale.** The documented tree has 28 files that exist on disk but are not listed, 3 files with wrong names, and 1 file documented that does not exist at all. The tree cannot be trusted for navigation or verification purposes.

**Inconsistent organizational logic.** The `references/` folder mixes three very different kinds of content:
- Instructional reference docs (e.g., `blockchain_methodology.md`, `hard_rules.md`)
- Full worked examples with deep subtrees of research files, deliverables, and source materials (`worked_example/`, `worked_example_team/`)
- Miscellaneous items (`asshole.txt`, `image.png`)

Similarly, `assets/` mixes templates, prompts, slide examples, a mermaid shape library, and deeply nested gold standards with no clear hierarchy.

### What the Redesign Must Accomplish

1. Flatten the deepest paths. No file should require more than 4 directory levels below the skill root.
2. Consolidate gold standards into one location, not split between `references/` and `assets/`.
3. Update `complete_structure.md` to match reality (or replace it with a new tree file).
4. Remove or relocate files that do not belong (`asshole.txt`, `image.png`).
5. Ensure every path referenced in SKILL.md, the stop hook, and other reference docs is updated to match the new structure.

### Constraints

- The redesign must not break any existing references in SKILL.md, the stop hook (`singularity_stop.py`), or the presentation design language.
- Gold standard files should not be modified, only relocated.
- The worked examples (Lam Research engagement, Cisco team sub-singularity) must remain intact as coherent examples.

---

## 2. Path Issues Master List (10 Items)

These were identified by 5 parallel verification agents plus manual repository search during the session. The full details are in `claude/2026-04-13_mermaid_research/path_issues_master.md`.

### Issue 1: `document_processing_workflow.md` Name Mismatch — RESOLVED

- **Problem:** `complete_structure.md` referenced `references/document_processing_workflow.md` but the actual file is named `references/document_processing.md`.
- **Status:** The tree in `complete_structure.md` was updated to show the correct shorter filename.

### Issue 2: `deliverable_template.html` Missing — RESOLVED

- **Problem:** `complete_structure.md` listed `assets/templates/deliverable_template.html` but this file does not exist. The files that do exist are `proposal_template.html`, `methodology_template.md`, and `ProjectCostingTemplate.xlsx`.
- **Status:** The obsolete `proposal_template.html` was deleted. The tree entry for `deliverable_template.html` was removed or corrected. This cleanup was completed during the session.

### Issue 3: `flag_ai_patterns.py` in Wrong Skill — PENDING

- **Problem:** `complete_structure.md` lists `scripts/flag_ai_patterns.py` as part of the Singularity skill, but this file only exists in `.claude/skills/big4/scripts/flag_ai_patterns.py`. It is not present in the Singularity scripts folder.
- **Status:** Pending the folder restructure. Needs a decision: copy it into Singularity, reference the big4 location, or remove it from the tree.

### Issue 4: 28 Files on Disk Not in the Documented Tree — PENDING

- **Problem:** 28 files exist in the skill directory but are not documented in `complete_structure.md`. Notable undocumented items include:
  - `assets/mermaid_shape_library/` (8 HTML files)
  - `references/sales_forge_merger.md`
  - `references/skill_ecosystem.md`
  - `assets/design/gold_standards/bridge_document_example.md`
  - `assets/design/gold_standards/poc_proposal_v5.html` and `poc_proposal_v5_detailed.html`
  - `assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html`
  - `references/worked_example/planning/skill_spec/` (14 files)
  - `assets/templates/methodology_template.md`
  - `assets/templates/proposal_template.html`
  - `references/asshole.txt`
  - `references/image.png`
- **Status:** Pending the folder restructure. The tree needs a full refresh. Some of these files (like `asshole.txt`) may need to be removed entirely rather than documented.

### Issue 5: `example_definition_bar.html` Referenced but Never Created — PENDING

- **Problem:** `presentation_design_language.md` references `example_definition_bar.html` in the Example Layout Patterns section, but this file was never created as one of the 7 example slide HTML files.
- **Status:** Pending. Either create the missing example or remove the reference.

### Issue 6: `example_two_column.html` Referenced but Never Created — PENDING

- **Problem:** Same as Issue 5. Referenced in `presentation_design_language.md` but never created.
- **Status:** Pending. Either create the missing example or remove the reference.

### Issue 7: `example_evolution_row.html` Referenced but Never Created — PENDING

- **Problem:** Same as Issues 5-6. Referenced in `presentation_design_language.md` but never created.
- **Status:** Pending. Either create the missing examples or remove the references.

### Issue 8: Inconsistent Path Prefixes in `presentation_design_language.md` — PENDING

- **Problem:** Some references use the short prefix `gold_standards/presentations/srinivas_status/` while others use the full path `assets/design/gold_standards/presentations/srinivas_status/`. The actual full path from the skill root is the longer version.
- **Status:** Pending. All paths should be made consistent. This will be affected by the folder restructure since the paths may change entirely.

### Issue 9: `resource_plan_for_cisco.html` Gold Standard Missing from Skill — PENDING

- **Problem:** `deliverables_pipeline.md` references a Cisco resource plan as a gold standard at `assets/design/gold_standards/resource_plan_for_cisco.html`. The file exists in two other locations in the repository (`claude/2026-02-02_resource-planning/deliverables/` and `cisco/cicd/archive/planning/`) but was never copied into the skill's gold standards folder.
- **Status:** Pending. The reference labels it as "(silver)" status, suggesting it was acknowledged as not yet promoted. Decision needed: copy it in as a gold standard, keep it as a silver reference, or remove the reference.

### Issue 10: `bayone_positioning.md` Missing — PENDING

- **Problem:** `deliverables_pipeline.md` references `.claude/context/bayone_positioning.md` but this file does not exist anywhere in the repository. `.claude/context/bayone_team.md` does exist and may be the intended reference.
- **Status:** Pending. This reference predates the current session. May have been renamed, may never have been created, or may have been consolidated into another file.

### Summary

| Issue | Description | Status |
|-------|-------------|--------|
| 1 | `document_processing_workflow.md` wrong filename | RESOLVED |
| 2 | `deliverable_template.html` does not exist | RESOLVED |
| 3 | `flag_ai_patterns.py` in wrong skill | PENDING |
| 4 | 28 undocumented files | PENDING |
| 5 | `example_definition_bar.html` never created | PENDING |
| 6 | `example_two_column.html` never created | PENDING |
| 7 | `example_evolution_row.html` never created | PENDING |
| 8 | Inconsistent path prefixes | PENDING |
| 9 | `resource_plan_for_cisco.html` not in gold standards | PENDING |
| 10 | `bayone_positioning.md` missing | PENDING |

---

## 3. Open Questions Awaiting Decisions (8 Items)

These are architectural and design decisions that require user input before the next session can proceed. They are documented in `claude/2026-04-10_singularity_nested_design/04_open_questions.md`.

### Q1: What Does `client/` Mean as a Folder Concept?

During engagement setup, the concept of a `client/` subfolder came up (e.g., `cisco/cicd/client/`). The intended purpose is ambiguous:

- **Interpretation A:** `client/` is a sub-singularity for all client-facing outputs (presentations, proposals, status decks delivered to the client). Under this model, `presentations/` at the engagement root would be for internal/BayOne-facing presentations only.
- **Interpretation B:** `client/` is just the presentations folder with a different name because "presentations" is too generic.
- **Interpretation C:** `client/` is broader than presentations, encompassing client communication transcripts, delivered artifacts, and meeting notes from client-facing delivery.

This directly affects `folder_structure.md` and how the skill creates new engagements. A decision here changes the canonical folder structure for all future engagements.

### Q2: Gold Standard Treatment for Deliverables

The Srinivas status deck became a gold standard because it was a real engagement output that performed well in an actual client meeting. The question is whether to expand the gold standard library with:

- A full deliverable chain (problem restatement + information request + preliminary approach) treated as an end-to-end gold standard rather than standalone files
- A formal proposal with pricing as a gold standard
- A team status presentation chain (week 1 through week 3) showing how tracking documents evolve over time

This affects the gold standards folder structure and what reference material the skill reads when producing deliverables.

### Q3: Depth of Methodology Enforcement

The skill currently uses two enforcement mechanisms:
- Behavioral instructions in SKILL.md (tells the skill what to do)
- Deterministic hook checks in `singularity_stop.py` (verifies the skill did it)

The question is whether the current balance is right. Should more checks be added to the stop hook? Should some be removed if they cause friction? Are there behaviors that are instructed but never verified, or verified but the verification is too strict?

### Q4: When to Offer Sub-Singularity vs. When to Enforce

Sub-singularities (nested singularity patterns for team operations within an engagement) are valuable for some engagements but may be overhead for others. The design question:

- Always offer the option at engagement creation?
- Only create one when explicitly asked?
- Detect automatically (e.g., if 2+ internal team meetings are processed, suggest one)?

This affects Flow 3 (team routing) in SKILL.md and the nested singularity reference docs.

### Q5: Cross-Engagement Learning

Each engagement has its own isolated research library. Patterns emerge across engagements (e.g., recurring meeting structures, similar client archetypes, pricing patterns). The question is whether a cross-engagement knowledge layer should exist that the skill consults, or whether that represents scope creep beyond the skill's purpose.

### Q6: Backup and Recovery for Blockchain Chains

The skill creates append-only blockchain-style research chains where each set references its predecessor. If a file gets accidentally modified or deleted, there is no recovery mechanism. The question is whether a recovery pattern should exist (e.g., checksums, snapshots, or instructions for reconstruction from source material).

### Q7-Q8: Behavioral Rule Additions (From Feedback)

Three specific behavioral failures documented during this session led to proposed new rules or rule modifications:

- **Batched questions in discussion mode:** Rule B1 exists but was violated multiple times. The proposal is to codify enforcement more aggressively in SKILL.md, not just as a rule but as a hard gate in Flow 6 (Discussion).
- **Unilateral filtering during exploration:** When instructed to explore or inventory, the skill narrowed scope without permission by claiming to focus on "the most important" items. The proposal is a hard rule banning filtering language during inventory presentation.
- **Executing after multiple corrections without confirmation:** After being corrected several times on an approach, the skill immediately started executing the corrected version instead of confirming alignment. The proposal is B16: the more corrections in a thread, the more important explicit confirmation becomes before acting.

These were partially addressed during the session (B1-B16 are now in `references/hard_rules.md`) but the enforcement depth and specific gating mechanisms are unresolved.

---

## 4. Other Remaining Work Items

### 4.1 Stop Hook: Mermaid Shape Library Not Verified

The mermaid shape library (8 HTML files in `assets/mermaid_shape_library/`) exists but the stop hook (`singularity_stop.py`) does not verify its presence or integrity. This was identified as a gap during the session but not fixed.

### 4.2 Three Missing Slide Example Files

Issues 5, 6, and 7 from the path issues list identify three slide examples that are referenced in `presentation_design_language.md` but were never created:
- `example_definition_bar.html`
- `example_two_column.html`
- `example_evolution_row.html`

Seven slide examples were created during the session in `assets/slide_examples/` (title, agenda, profile, split concept, three column, grid takeaway, closing). These three additional patterns were referenced in the design language spec but not implemented.

### 4.3 `complete_structure.md` Full Refresh

Regardless of the folder restructure, this file is currently unreliable. It has:
- 3 filename mismatches (1 resolved, 2 pending)
- 1 non-existent file listed (resolved)
- 28 files on disk that it does not document
- Path references that use inconsistent prefixes

After the folder restructure, this file must be regenerated from scratch using the actual file system as ground truth.

### 4.4 B2 Violation Audit Pattern

During this session, a full audit of all skill files was performed for B2 violations (Claude inventing absolute rules from specific situational feedback). 11 items were flagged, all 11 were reviewed and resolved. However, this audit pattern should be repeated after the folder restructure, since the restructure will touch many files and may introduce new violations.

### 4.5 Feedback Synthesis Integration

The feedback synthesis at `claude/singularity_feedback/2026-04-13_round_01/00_synthesis.md` contains 19 sections of consolidated rules and patterns from 8 source files. Not all of these have been fully integrated into the skill's reference documents. The synthesis serves as a comprehensive checklist of everything the skill should enforce, but the degree to which each item is reflected in SKILL.md, the stop hook, or the reference docs varies.

### 4.6 Session Continuity Pattern Validation

The handoff documents being created (including this one) represent the first real test of the session continuity pattern documented in `references/session_continuity.md`. Validating that the next session can actually pick up work smoothly will confirm or reveal gaps in that methodology.

---

## 5. Current Skill File Inventory (134 Files)

This is the complete file listing of the Singularity skill as it exists on disk at the time of handoff. Generated by `find .claude/skills/singularity/ -type f | sort` on 2026-04-14.

### Root

```
.claude/skills/singularity/SKILL.md
```

### Scripts (3 files)

```
.claude/skills/singularity/scripts/format_transcript.py
.claude/skills/singularity/scripts/html_to_pdf.py
.claude/skills/singularity/scripts/singularity_stop.py
```

### References — Top-Level Docs (20 files)

```
.claude/skills/singularity/references/agent_architecture.md
.claude/skills/singularity/references/anti_patterns.md
.claude/skills/singularity/references/blockchain_methodology.md
.claude/skills/singularity/references/complete_structure.md
.claude/skills/singularity/references/deliverables_pipeline.md
.claude/skills/singularity/references/document_processing.md
.claude/skills/singularity/references/enforcement_architecture.md
.claude/skills/singularity/references/folder_structure.md
.claude/skills/singularity/references/hard_rules.md
.claude/skills/singularity/references/mermaid_design_standards.md
.claude/skills/singularity/references/mermaid_shape_library.md
.claude/skills/singularity/references/nested_singularity.md
.claude/skills/singularity/references/people_tracking.md
.claude/skills/singularity/references/presentation_design_language.md
.claude/skills/singularity/references/pricing_workflow.md
.claude/skills/singularity/references/professional_standards.md
.claude/skills/singularity/references/reorganization_guide.md
.claude/skills/singularity/references/sales_forge_merger.md
.claude/skills/singularity/references/session_continuity.md
.claude/skills/singularity/references/skill_ecosystem.md
.claude/skills/singularity/references/team_meeting_processing.md
.claude/skills/singularity/references/tracking_folder_pattern.md
```

### References — Worked Example: Lam Research Engagement (38 files)

```
.claude/skills/singularity/references/worked_example/org_chart.md
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/README.md
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/followup_email_draft.md
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/information_request.html
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/information_request.md
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/preliminary_approach.html
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/preliminary_approach.md
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/problem_restatement.html
.claude/skills/singularity/references/worked_example/deliverables/02_discovery_call_2026-03-12/problem_restatement.md
.claude/skills/singularity/references/worked_example/planning/session_handoff_2026-03-20.md
.claude/skills/singularity/references/worked_example/planning/skill_notes.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/00_skill_overview.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/01_blockchain_methodology.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/02_document_processing_workflow.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/03_folder_structure_and_naming.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/04_people_tracking.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/05_agent_architecture.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/06_deliverables_pipeline.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/07_session_continuity.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/08_worked_example.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/09_pricing_workflow.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/10_complete_structure.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/11_skill_ecosystem.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/12_sales_forge_merger.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/build_plan.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/design_spec_update_handoff.md
.claude/skills/singularity/references/worked_example/planning/skill_spec/design_spec_update_kickoff.md
.claude/skills/singularity/references/worked_example/research/00_methodology_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/01-02_changes_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/01_call_prep_discovery_strategy_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/01_call_prep_people_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/01_call_prep_situational_context_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/01_call_prep_summary_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/01_call_prep_technical_reference_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_business_opportunity_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_infrastructure_and_access_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_people_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_speaker_dynamics_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_summary_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_technical_use_cases_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_topic_map_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02_meeting_what_was_tried_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02a_debrief_action_items_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02a_debrief_internal_assessment_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02a_debrief_people_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/02a_debrief_summary_2026-03-12.md
.claude/skills/singularity/references/worked_example/research/03_discussion_final_clarifications_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_open_information_needs_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_strategy_and_deliverables_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_summary_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_technical_approach_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_technical_approach_continued_2026-03-20.md
.claude/skills/singularity/references/worked_example/research/03_discussion_technical_approach_round3_2026-03-20.md
.claude/skills/singularity/references/worked_example/source/anuj_and_colin_after_call1.txt
.claude/skills/singularity/references/worked_example/source/lam_call_prep (1).txt
.claude/skills/singularity/references/worked_example/source/lam_meeting_3122026.txt
```

### References — Worked Example: Team Sub-Singularity (11 files)

```
.claude/skills/singularity/references/worked_example_team/README.md
.claude/skills/singularity/references/worked_example_team/cross_reference.md
.claude/skills/singularity/references/worked_example_team/research/00_methodology_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/research/01_standup_action_items_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/research/01_standup_blockers_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/research/01_standup_people_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/research/01_standup_summary_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/research/01_standup_technical_discussion_2026-04-10.md
.claude/skills/singularity/references/worked_example_team/tracking/action_items.md
.claude/skills/singularity/references/worked_example_team/tracking/blockers.md
.claude/skills/singularity/references/worked_example_team/tracking/decisions.md
```

### Assets — Templates (3 files)

```
.claude/skills/singularity/assets/templates/ProjectCostingTemplate.xlsx
.claude/skills/singularity/assets/templates/methodology_template.md
.claude/skills/singularity/assets/templates/proposal_template.html
```

### Assets — Prompts (1 file)

```
.claude/skills/singularity/assets/prompts/excel_template_prompt.md
```

### Assets — Slide Examples (7 files)

```
.claude/skills/singularity/assets/slide_examples/example_agenda.html
.claude/skills/singularity/assets/slide_examples/example_closing.html
.claude/skills/singularity/assets/slide_examples/example_grid_takeaway.html
.claude/skills/singularity/assets/slide_examples/example_profile.html
.claude/skills/singularity/assets/slide_examples/example_split_concept.html
.claude/skills/singularity/assets/slide_examples/example_three_column.html
.claude/skills/singularity/assets/slide_examples/example_title.html
```

### Assets — Mermaid Shape Library (8 files)

```
.claude/skills/singularity/assets/mermaid_shape_library/01_classic_shapes.html
.claude/skills/singularity/assets/mermaid_shape_library/02_v11_shapes.html
.claude/skills/singularity/assets/mermaid_shape_library/03_arrows_and_edges.html
.claude/skills/singularity/assets/mermaid_shape_library/04_text_formatting.html
.claude/skills/singularity/assets/mermaid_shape_library/05_icons_reference.html
.claude/skills/singularity/assets/mermaid_shape_library/06_classdef_styling.html
.claude/skills/singularity/assets/mermaid_shape_library/07_subgraphs_and_layout.html
.claude/skills/singularity/assets/mermaid_shape_library/08_diagram_types_gallery.html
```

### Assets — Design Spec (1 file)

```
.claude/skills/singularity/assets/design/bayone_design_spec.md
```

### Assets — Gold Standards (21 files)

```
.claude/skills/singularity/assets/design/gold_standards/bridge_document_example.md
.claude/skills/singularity/assets/design/gold_standards/charts/example_ecosystem_diagram.html
.claude/skills/singularity/assets/design/gold_standards/information_request.html
.claude/skills/singularity/assets/design/gold_standards/knowledge_transfer/charts/architecture_overview.html
.claude/skills/singularity/assets/design/gold_standards/knowledge_transfer/charts/candidate_data_flow.html
.claude/skills/singularity/assets/design/gold_standards/knowledge_transfer/charts/fishbone_apps.html
.claude/skills/singularity/assets/design/gold_standards/knowledge_transfer/session_0_platform_overview.html
.claude/skills/singularity/assets/design/gold_standards/poc_proposal_v5.html
.claude/skills/singularity/assets/design/gold_standards/poc_proposal_v5_detailed.html
.claude/skills/singularity/assets/design/gold_standards/preliminary_approach.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/00_title.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/01_assigned_items_status.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/02_discovery_findings_build.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/02a_build_ecosystem_diagram.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/03_discovery_findings_webex.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/04_items_for_discussion.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/05_access_status.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/06_next_steps.html
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/README.md
.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html
.claude/skills/singularity/assets/design/gold_standards/problem_restatement.html
```

### Total File Count by Area

| Area | Count |
|------|-------|
| Root (SKILL.md) | 1 |
| Scripts | 3 |
| References (top-level docs) | 22 |
| References (worked_example — Lam) | 56 |
| References (worked_example_team) | 11 |
| Assets (templates) | 3 |
| Assets (prompts) | 1 |
| Assets (slide examples) | 7 |
| Assets (mermaid shape library) | 8 |
| Assets (design spec) | 1 |
| Assets (gold standards) | 21 |
| **Total** | **134** |

---

## Appendix: Priority Ordering for the Next Session

1. **Folder structure redesign** — This is the stated immediate priority. It affects nearly every other item on this list because paths will change.
2. **Path issues 3-10** — Most of these will be resolved naturally as part of the folder restructure.
3. **Open questions Q1 and Q2** — These directly affect the folder structure design (where `client/` goes, where gold standards live).
4. **`complete_structure.md` regeneration** — Must happen after the restructure, not before.
5. **Missing slide examples (Issues 5-7)** — Lower priority, can be addressed any time.
6. **Stop hook updates** — Should happen after the folder restructure so paths are stable.
7. **Open questions Q3-Q6** — These are strategic decisions that do not block the restructure work.
