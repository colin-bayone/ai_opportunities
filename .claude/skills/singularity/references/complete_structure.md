# Complete Structure: Singularity Skill

> Regenerated 2026-04-15 as part of the folder restructure.

## Skill Location

```
.claude/skills/singularity/
```

Everything the skill needs to operate is self-contained here. No external dependencies.

**Totals:** 33 directories, 260 files.

---

## Skill File Structure

```
.claude/skills/singularity/
├── SKILL.md                                          # Skill definition, invocation, full workflow
│
├── gold_standards/                                   # Gold standard examples (135 files across 10 dirs)
│   ├── charts/                                       # Standalone mermaid.js diagrams (9 HTML + README)
│   │   ├── README.md
│   │   ├── architecture_overview.html
│   │   ├── candidate_data_flow.html
│   │   ├── ecosystem_diagram.html
│   │   ├── figure_1_platform_architecture.html
│   │   ├── figure_2_discovery_cycle.html
│   │   ├── figure_3_playbook_lifecycle.html
│   │   ├── figure_4_confidence_scoring.html
│   │   ├── fishbone_apps.html
│   │   └── session_0_platform_overview.html
│   │
│   ├── deliverables/                                 # Client-facing document gold standards (24 HTML, 1 MD, README)
│   │   ├── README.md
│   │   ├── bridge_document_example.md
│   │   └── (24 HTML deliverables spanning problem restatements,
│   │        information requests, preliminary approaches, POC proposals,
│   │        pricing breakdowns, architecture docs, executive overviews,
│   │        demo packages, and engagement pricing — from Lam Research,
│   │        Sephora EDW, and Tailored Brands engagements)
│   │
│   └── presentations/                                # Slide deck gold standards (5 decks)
│       ├── ai_education/                             # Masterminds AI education deck
│       │   ├── README.md
│       │   ├── resources/                            # 24 image assets (PNG, JPG)
│       │   └── (25 HTML slides: s0-s6 sections)
│       │
│       ├── capabilities_pitch/                       # Ariat foundational slides
│       │   ├── README.md
│       │   └── (3 HTML slides)
│       │
│       ├── discovery_session/                        # Lam Research IP Protection
│       │   ├── README.md
│       │   └── (11 HTML slides)
│       │
│       ├── rfp_proposal/                             # McGrath RentCorp MSP RFP
│       │   ├── README.md
│       │   └── (29 HTML slides)
│       │
│       └── team_status_update/                       # Cisco CI/CD (Srinivas status update)
│           ├── README.md
│           ├── charts/
│           │   └── build_log_ecosystem.html
│           └── (8 HTML slides)
│
├── layout_examples/                                  # Slide layout pattern vocabulary (8 HTML + README)
│   ├── README.md
│   ├── agenda.html
│   ├── chevron_flow_detail.html
│   ├── closing.html
│   ├── grid_takeaway.html
│   ├── profile.html
│   ├── split_concept.html
│   ├── three_column.html
│   └── title.html
│
├── mermaid_shape_library/                            # Interactive mermaid.js shape/syntax reference (8 files)
│   ├── 01_classic_shapes.html
│   ├── 02_v11_shapes.html
│   ├── 03_arrows_and_edges.html
│   ├── 04_text_formatting.html
│   ├── 05_icons_reference.html
│   ├── 06_classdef_styling.html
│   ├── 07_subgraphs_and_layout.html
│   └── 08_diagram_types_gallery.html
│
├── references/                                       # Methodology and standards docs (27 files)
│   ├── agent_architecture.md                         # Agent prompts, parallelization, permissions
│   ├── anti_patterns.md                              # AI writing anti-patterns (own copy)
│   ├── bayone_design_spec.md                         # BayOne design system spec (own copy)
│   ├── bayone_team.md                                # BayOne team context and roles
│   ├── blockchain_methodology.md                     # Core append-only methodology
│   ├── complete_structure.md                         # THIS FILE — skill structure reference
│   ├── deliverables_pipeline.md                      # Client-facing output rules and workflow
│   ├── document_processing.md                        # How to process each source type
│   ├── enforcement_architecture.md                   # Artifact-check enforcement pattern
│   ├── folder_structure.md                           # Engagement folder spec + sub-singularity structure
│   ├── hard_rules.md                                 # Behavioral hard rules B1-B16 (mandatory read)
│   ├── mermaid_design_standards.md                   # Mermaid diagram visual standards and patterns
│   ├── mermaid_flowchart_learnings.md                # Flowchart-specific mermaid lessons learned
│   ├── mermaid_shape_library.md                      # Quick-reference menu of all shapes, arrows, icons, formatting
│   ├── mermaid_svg_scaling_research.md               # SVG scaling and viewport research
│   ├── nested_singularity.md                         # Sub-singularity pattern and rules
│   ├── people_tracking.md                            # Dual system: per-set docs + org chart
│   ├── playwright_screenshot_research.md             # Playwright-based screenshot research
│   ├── presentation_design_language.md               # Slide generation design system
│   ├── pricing_workflow.md                           # Pricing questionnaire and Excel handoff
│   ├── professional_standards.md                     # Big Four quality standards (own copy)
│   ├── reorganization_guide.md                       # Reorganizing existing folders into Singularity format
│   ├── sales_forge_merger.md                         # Sales Forge skill merger documentation
│   ├── session_continuity.md                         # Handoffs between sessions
│   ├── skill_ecosystem.md                            # Skill ecosystem and integration points
│   ├── team_meeting_processing.md                    # Team meeting standard passes methodology
│   └── tracking_folder_pattern.md                    # Living tracking docs (action items, blockers, decisions)
│
├── scripts/                                          # Utility scripts (3 files)
│   ├── format_transcript.py                          # Format single-line transcripts
│   ├── html_to_pdf.py                                # Convert HTML to PDF
│   └── singularity_stop.py                           # Stop hook: artifact verification
│
├── templates/                                        # Reusable templates (3 files)
│   ├── ProjectCostingTemplate.xlsx                   # Ready-to-use costing workbook
│   ├── excel_template_prompt.md                      # Recreate the xlsx from scratch
│   └── methodology_template.md                       # Research methodology doc template
│
└── worked_examples/                                  # Complete engagement examples (67 files across 2 examples)
    ├── cisco_team/                                   # Team sub-singularity example (11 files)
    │   ├── README.md
    │   ├── cross_reference.md                        # Maps to parent chain
    │   ├── documents/                                # (empty — formatted outputs)
    │   ├── planning/                                 # (empty — session handoffs)
    │   ├── source/                                   # (empty — raw transcripts)
    │   ├── research/                                 # Blockchain chain (6 files)
    │   │   ├── 00_methodology_2026-04-10.md
    │   │   ├── 01_standup_action_items_2026-04-10.md
    │   │   ├── 01_standup_blockers_2026-04-10.md
    │   │   ├── 01_standup_people_2026-04-10.md
    │   │   ├── 01_standup_summary_2026-04-10.md
    │   │   └── 01_standup_technical_discussion_2026-04-10.md
    │   └── tracking/                                 # Living tracking docs (3 files)
    │       ├── action_items.md
    │       ├── blockers.md
    │       └── decisions.md
    │
    └── lam_research/                                 # Full client engagement example (56 files)
        ├── org_chart.md
        ├── decisions/                                # (empty)
        ├── progress/                                 # (empty)
        ├── source/                                   # Raw inputs (3 files)
        │   ├── anuj_and_colin_after_call1.txt
        │   ├── lam_call_prep (1).txt
        │   └── lam_meeting_3122026.txt
        ├── research/                                 # Blockchain chain (27 files)
        │   ├── 00_methodology_2026-03-20.md
        │   ├── 01_call_prep_*.md                     # Set 01: 5 call prep docs
        │   ├── 02_meeting_*.md                       # Set 02: 8 meeting decomposition docs
        │   ├── 02a_debrief_*.md                      # Set 02a: 4 debrief docs
        │   ├── 01-02_changes_2026-03-12.md           # Cross-set changes doc
        │   └── 03_discussion_*.md                    # Set 03: 7 discussion docs
        ├── planning/                                 # Session handoffs and skill spec (18 files)
        │   ├── session_handoff_2026-03-20.md
        │   ├── skill_notes.md
        │   └── skill_spec/                           # Original skill design docs (16 files)
        │       ├── 00_skill_overview.md
        │       ├── 01_blockchain_methodology.md
        │       ├── 02_document_processing_workflow.md
        │       ├── 03_folder_structure_and_naming.md
        │       ├── 04_people_tracking.md
        │       ├── 05_agent_architecture.md
        │       ├── 06_deliverables_pipeline.md
        │       ├── 07_session_continuity.md
        │       ├── 08_worked_example.md
        │       ├── 09_pricing_workflow.md
        │       ├── 10_complete_structure.md
        │       ├── 11_skill_ecosystem.md
        │       ├── 12_sales_forge_merger.md
        │       ├── build_plan.md
        │       ├── design_spec_update_handoff.md
        │       └── design_spec_update_kickoff.md
        └── deliverables/                             # Client-facing outputs (8 files)
            └── 02_discovery_call_2026-03-12/
                ├── README.md
                ├── followup_email_draft.md
                ├── information_request.html
                ├── information_request.md
                ├── preliminary_approach.html
                ├── preliminary_approach.md
                ├── problem_restatement.html
                └── problem_restatement.md
```

---

## File Counts by Area

| Area | Dirs | Files | Notes |
|------|------|-------|-------|
| `gold_standards/charts/` | 1 | 10 | 9 HTML diagrams + README |
| `gold_standards/deliverables/` | 1 | 26 | 24 HTML + 1 MD + README |
| `gold_standards/presentations/ai_education/` | 2 | 50 | 25 slides + 24 resources + README |
| `gold_standards/presentations/capabilities_pitch/` | 1 | 4 | 3 slides + README |
| `gold_standards/presentations/discovery_session/` | 1 | 12 | 11 slides + README |
| `gold_standards/presentations/rfp_proposal/` | 1 | 30 | 29 slides + README |
| `gold_standards/presentations/team_status_update/` | 2 | 10 | 8 slides + 1 chart + README |
| `layout_examples/` | 1 | 9 | 8 layout patterns + README |
| `mermaid_shape_library/` | 1 | 8 | 8 interactive reference pages |
| `references/` | 1 | 27 | Methodology and standards docs |
| `scripts/` | 1 | 3 | Utility scripts |
| `templates/` | 1 | 3 | Reusable templates |
| `worked_examples/cisco_team/` | 6 | 11 | Team sub-singularity example |
| `worked_examples/lam_research/` | 8 | 56 | Full client engagement example |
| **TOTAL** | **33** | **260** | |

---

## Engagement Output Structure

When the skill runs for an engagement, it creates this structure. The root is NOT in `claude/`. It is at the project root:

```
/<client_name>/<opportunity_name>/
```

For example:
```
/lam_research/ip_protection/
/cisco/epnm_ems_conversion/
/acme_corp/platform_migration/
```

### Full Engagement Folder

```
/<client_name>/<opportunity_name>/
├── org_chart.md                                        # Living document, always current
│
├── source/                                             # Raw input files. NEVER modified.
│   ├── call_prep_2026-03-12.txt
│   ├── discovery_call_transcript_2026-03-12.txt
│   ├── internal_debrief_2026-03-12.txt
│   ├── followup_email_2026-03-15.txt
│   └── ...
│
├── research/                                           # Blockchain-style decomposition. Append-only.
│   ├── 00_methodology_2026-03-12.md
│   ├── 01_call_prep_situational_context_2026-03-12.md
│   ├── 01_call_prep_discovery_strategy_2026-03-12.md
│   ├── 01_call_prep_people_2026-03-12.md
│   ├── 01_call_prep_summary_2026-03-12.md
│   ├── 02_meeting_people_2026-03-12.md
│   ├── 02_meeting_topic_map_2026-03-12.md
│   ├── 02_meeting_technical_use_cases_2026-03-12.md
│   ├── 02_meeting_what_was_tried_2026-03-12.md
│   ├── 02_meeting_summary_2026-03-12.md
│   ├── 02a_debrief_people_2026-03-12.md
│   ├── 02a_debrief_internal_assessment_2026-03-12.md
│   ├── 02a_debrief_summary_2026-03-12.md
│   ├── 01-02_changes_2026-03-12.md
│   ├── 03_discussion_technical_approach_2026-03-20.md
│   ├── 03_discussion_summary_2026-03-20.md
│   └── ...
│
├── planning/                                           # Approach planning, notes, handoffs
│   ├── skill_notes.md                                  # Accumulated do's/don'ts for this engagement
│   ├── session_handoff_2026-03-20.md                   # Where a session left off
│   └── ...
│
├── pricing/                                            # All pricing artifacts. Dated.
│   ├── pricing_spec_2026-03-26.md                      # Output of pricing questionnaire (also prompt for Excel)
│   ├── pricing_corrections_v1_2026-03-28.md            # Iterative corrections for Excel session
│   ├── pricing_corrections_v2_2026-03-28.md
│   ├── pricing_model_prototype_2026-03-26.md           # Raw discussion output with numbers
│   └── ProjectCosting_<client>_2026-03-28.xlsx         # The customized workbook (if saved back)
│
├── deliverables/                                       # Client-facing documents. Dated.
│   ├── problem_restatement_2026-03-20.md
│   ├── problem_restatement_2026-03-20.html
│   ├── information_request_2026-03-20.md
│   ├── information_request_2026-03-20.html
│   ├── preliminary_approach_2026-03-20.md
│   ├── preliminary_approach_2026-03-20.html
│   ├── formal_proposal_2026-04-15.md
│   ├── formal_proposal_2026-04-15.html
│   ├── followup_email_2026-03-20.md
│   └── ...
│
├── presentations/                                      # Slide decks, presentation materials. Dated.
│   ├── discovery_findings_2026-03-20.html
│   ├── technical_approach_2026-04-01.html
│   ├── executive_briefing_2026-04-15.html
│   └── ...
│
├── decisions/                                          # Open questions and agreed decisions
│   └── ...
│
├── progress/                                           # Running status tracking
│   └── ...
│
├── team/                                                # Sub-singularity: team operations (optional)
│   ├── source/                                          # Raw team meeting transcripts
│   ├── research/                                        # Blockchain chain, own numbering
│   │   ├── 00_methodology_<date>.md
│   │   └── ...
│   ├── tracking/                                        # Living: action items, blockers, decisions
│   ├── documents/                                       # Formatted outputs
│   ├── planning/                                        # Session handoffs
│   └── cross_reference.md                               # Maps to parent chain
│
└── <other_sub_singularity>/                             # Additional parallel tracks (optional)
    ├── source/
    ├── research/
    ├── tracking/
    ├── documents/
    ├── planning/
    └── cross_reference.md
```

### Folder Purposes

| Folder | Purpose | Mutability | Dated? |
|--------|---------|------------|--------|
| `source/` | Raw input files (transcripts, emails, docs) | Never modified | Yes (source date) |
| `research/` | Blockchain decomposition documents | Append-only (new files, never edit old) | Yes (source date) |
| `planning/` | Approach planning, skill notes, session handoffs | Editable | Yes |
| `pricing/` | Pricing specs, correction prompts, cost models, workbooks | Editable, versioned | Yes |
| `deliverables/` | Client-facing documents (markdown + HTML) | Editable, versioned | Yes |
| `presentations/` | Slide decks, pitch materials, executive briefings | Editable, versioned | Yes |
| `decisions/` | Open questions and agreed decisions | Editable | Yes |
| `progress/` | Running status tracking | Editable | Yes |

### Dating Rules

Every file in the engagement gets a date. No exceptions.

- **Source files:** Date of the source event (e.g., `discovery_call_transcript_2026-03-12.txt`)
- **Research files:** Date of the source material they decompose (e.g., `02_meeting_people_2026-03-12.md`)
- **Planning files:** Date created or last updated (e.g., `session_handoff_2026-03-20.md`)
- **Pricing files:** Date created or version date (e.g., `pricing_spec_2026-03-26.md`)
- **Deliverables:** Date produced (e.g., `problem_restatement_2026-03-20.html`)
- **Presentations:** Date produced (e.g., `executive_briefing_2026-04-15.html`)
- **Decisions/Progress:** Date created

Date format is always `YYYY-MM-DD`, appended before the extension or at the end of the filename stem.

### Naming Convention

All filenames: lowercase, underscores, dated, descriptive.

```
<descriptive_name>_<date>.ext
```

For research files (which also have set numbers):
```
<set_number>_<source_type>_<topic>_<date>.ext
```

---

## Session Setup Flow

When the skill is invoked for a new engagement:

1. Ask: Client name and opportunity name
2. Create `/<client_name>/<opportunity_name>/`
3. Create all folders (source, research, planning, pricing, deliverables, presentations, decisions, progress)
4. Write `research/00_methodology_<date>.md`
5. Write initial `org_chart.md` if any people are already known

When the skill is invoked for an existing engagement:

1. Read `org_chart.md`
2. Read the most recent summary in `research/`
3. Read `planning/skill_notes.md` if it exists
4. Read `planning/session_handoff_*.md` if it exists
5. Ask: What are we working on today?

---

## What Lives Where: Decision Guide

| I need to... | It goes in... |
|---|---|
| Store a raw transcript (client meeting) | `source/` |
| Store a raw transcript (team meeting) | `team/source/` (or relevant sub-singularity) |
| Decompose a client transcript into structured docs | `research/` |
| Decompose a team transcript into structured docs | `team/research/` (using team meeting passes) |
| Track action items, blockers, decisions operationally | `team/tracking/` (living docs) |
| Capture a working discussion with Claude | `research/` (as a discussion set) |
| Write notes about how the engagement works | `planning/skill_notes.md` |
| Hand off to a future session | `planning/session_handoff_<date>.md` |
| Build a pricing model | `pricing/pricing_spec_<date>.md` |
| Write corrections for Claude in Excel | `pricing/pricing_corrections_v<N>_<date>.md` |
| Draft a client-facing document | `deliverables/<name>_<date>.md` + `.html` |
| Create a presentation or slide deck | `presentations/<name>_<date>.html` |
| Record an open question | `decisions/` |
| Track what is done and what is not | `progress/` |
| Create a prompt for another Claude session | Whichever folder the output belongs to (pricing prompts in `pricing/`, deliverable prompts in `deliverables/`, etc.) |
