# Complete Structure: Singularity Skill

## Skill Location

```
.claude/skills/singularity/
```

Everything the skill needs to operate is self-contained here. No external dependencies.

---

## Skill File Structure

```
.claude/skills/singularity/
├── SKILL.md                                           # Skill definition, invocation, full workflow
│
├── references/
│   ├── blockchain_methodology.md                      # Core append-only methodology
│   ├── document_processing_workflow.md                 # How to process each source type
│   ├── folder_structure.md                             # THIS document (engagement folder spec)
│   ├── people_tracking.md                              # Dual system: per-set docs + org chart
│   ├── agent_architecture.md                           # Agent prompts, parallelization, permissions
│   ├── deliverables_pipeline.md                        # Client-facing output rules and workflow
│   ├── pricing_workflow.md                             # Pricing questionnaire and Excel handoff
│   ├── session_continuity.md                           # Handoffs between sessions
│   ├── anti_patterns.md                                # AI writing anti-patterns (own copy)
│   └── professional_standards.md                       # Big Four quality standards (own copy)
│
├── assets/
│   ├── templates/
│   │   ├── deliverable_template.html                   # BayOne design system HTML shell
│   │   └── ProjectCostingTemplate.xlsx                 # Ready-to-use costing workbook
│   ├── prompts/
│   │   └── excel_template_prompt.md                    # Recreate the xlsx from scratch
│   └── design/
│       ├── bayone_design_spec.md                       # BayOne design system spec (own copy)
│       └── gold_standards/                             # Gold standard HTML deliverables
│           ├── problem_restatement.html                # Lam Research problem restatement
│           ├── information_request.html                # Lam Research information request
│           └── preliminary_approach.html               # Lam Research preliminary approach
│
└── scripts/
    └── flag_ai_patterns.py                             # AI pattern detection (own copy)
```

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
└── progress/                                           # Running status tracking
    └── ...
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
3. Ask: Which folders do you need? (Default: all. Minimum: source, research)
4. Create selected folders
5. Write `research/00_methodology_<date>.md`
6. Write initial `org_chart.md` if any people are already known

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
| Store a raw transcript | `source/` |
| Decompose a transcript into structured docs | `research/` |
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
