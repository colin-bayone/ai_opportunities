# Folder Structure and Naming Conventions

## Engagement Folder Structure

When the skill is invoked for a new engagement, create the following folder structure at `/<client_name>/<opportunity_name>/`:

```
/<client_name>/<opportunity_name>/
├── org_chart.md                                        (living document, always current)
│
├── source/                                             (raw input files. NEVER modified.)
│   ├── call_prep_2026-03-12.txt
│   ├── discovery_call_transcript_2026-03-12.txt
│   └── ...
│
├── research/                                           (blockchain-style decomposition. Append-only.)
│   ├── 00_methodology_<date>.md                        (explains the approach, first file created)
│   ├── 01_*                                            (first document set)
│   ├── 02_*                                            (second document set)
│   ├── 02a_*                                           (supplementary to second set)
│   ├── 01-02_changes_<date>.md                         (bridge document)
│   └── ...
│
├── planning/                                           (approach planning, notes, handoffs)
│   ├── skill_notes.md                                  (accumulated do's/don'ts for this engagement)
│   ├── glossary_<date>.md                              (optional: key terms and definitions)
│   ├── session_handoff_<date>.md                       (where a session left off)
│   └── ...
│
├── pricing/                                            (pricing specs, corrections, workbooks)
│   ├── pricing_spec_<date>.md
│   ├── pricing_corrections_v<N>_<date>.md
│   └── ...
│
├── deliverables/                                       (client-facing documents. Dated, flat.)
│   ├── problem_restatement_<date>.md
│   ├── problem_restatement_<date>.html
│   ├── information_request_<date>.md
│   ├── information_request_<date>.html
│   └── ...
│
├── presentations/                                      (slide decks, presentation materials. Dated.)
│   ├── discovery_findings_<date>.html
│   └── ...
│
├── decisions/                                          (open questions and agreed decisions)
│
└── progress/                                           (running status tracking)
```

### Folder Purposes

| Folder | Purpose | Mutability | Dated? |
|--------|---------|------------|--------|
| `/<client_name>/<opportunity_name>/source/` | Raw input files (transcripts, emails, docs) | Never modified | Yes (source date) |
| `/<client_name>/<opportunity_name>/research/` | Blockchain decomposition documents | Append-only (new files, never edit old) | Yes (source date) |
| `/<client_name>/<opportunity_name>/planning/` | Approach planning, skill notes, glossary, session handoffs | Editable | Yes |
| `/<client_name>/<opportunity_name>/pricing/` | Pricing specs, correction prompts, cost models, workbooks | Editable, versioned | Yes |
| `/<client_name>/<opportunity_name>/deliverables/` | Client-facing documents (markdown + HTML) | Editable, versioned | Yes |
| `/<client_name>/<opportunity_name>/presentations/` | Slide decks, pitch materials, executive briefings | Editable, versioned | Yes |
| `/<client_name>/<opportunity_name>/decisions/` | Open questions and agreed decisions | Editable | Yes |
| `/<client_name>/<opportunity_name>/progress/` | Running status tracking | Editable | Yes |

### Ask Before Creating

The skill should ask the user if they want the full folder structure when starting a new engagement. Not every engagement needs every folder. The minimum is `/<client_name>/<opportunity_name>/source/` and `/<client_name>/<opportunity_name>/research/`.

## File Naming Convention

### Research Files

Pattern: `<set_number>_<descriptive_name>_<source_date>.md`

Examples (all files live in `/<client_name>/<opportunity_name>/research/`):
```
/<client_name>/<opportunity_name>/research/00_methodology_2026-03-20.md
/<client_name>/<opportunity_name>/research/01_call_prep_situational_context_2026-03-12.md
/<client_name>/<opportunity_name>/research/01_call_prep_discovery_strategy_2026-03-12.md
/<client_name>/<opportunity_name>/research/01_call_prep_people_2026-03-12.md
/<client_name>/<opportunity_name>/research/01_call_prep_summary_2026-03-12.md
/<client_name>/<opportunity_name>/research/01-02_changes_2026-03-12.md
/<client_name>/<opportunity_name>/research/02_meeting_people_2026-03-12.md
/<client_name>/<opportunity_name>/research/02_meeting_topic_map_2026-03-12.md
/<client_name>/<opportunity_name>/research/02_meeting_technical_use_cases_2026-03-12.md
/<client_name>/<opportunity_name>/research/02_meeting_speaker_dynamics_2026-03-12.md
/<client_name>/<opportunity_name>/research/02_meeting_summary_2026-03-12.md
/<client_name>/<opportunity_name>/research/02a_debrief_people_2026-03-12.md
/<client_name>/<opportunity_name>/research/02a_debrief_internal_assessment_2026-03-12.md
/<client_name>/<opportunity_name>/research/02a_debrief_summary_2026-03-12.md
/<client_name>/<opportunity_name>/research/03_discussion_technical_approach_2026-03-20.md
/<client_name>/<opportunity_name>/research/03_discussion_summary_2026-03-20.md
```

### Naming Rules

- All lowercase with underscores (snake_case)
- Set number prefix is always two digits (01, 02, 03... not 1, 2, 3)
- Supplementary sets use letter suffix (02a, 02b, 02c)
- Date suffix uses ISO format (YYYY-MM-DD)
- Date reflects the source material date, not the analysis date
- Descriptive name should be clear enough that someone can understand the file's purpose without opening it

### Bridge Documents

Pattern: `<set_from>-<set_to>_changes_<date>.md`

Examples:
```
/<client_name>/<opportunity_name>/research/01-02_changes_2026-03-12.md
/<client_name>/<opportunity_name>/research/02-03_changes_2026-03-20.md
```

Bridge documents capture what changed between two sets. They are written after both sets exist.

### Standard File Names

Some file names are standard across all sets:

| File Type | Full Path | When Created |
|-----------|-----------|--------------|
| Methodology | `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` | Once, at engagement start |
| People | `/<client_name>/<opportunity_name>/research/<set>_<source_type>_people_<date>.md` | First file for transcript sets |
| Topic map | `/<client_name>/<opportunity_name>/research/<set>_<source_type>_topic_map_<date>.md` | After first pass of transcript |
| Summary | `/<client_name>/<opportunity_name>/research/<set>_<source_type>_summary_<date>.md` | Last file for every set |
| Bridge | `/<client_name>/<opportunity_name>/research/<from>-<to>_changes_<date>.md` | After both sets exist |

### Deliverable Files

Deliverables go in `/<client_name>/<opportunity_name>/deliverables/` as flat, dated files:

```
/<client_name>/<opportunity_name>/deliverables/problem_restatement_2026-03-20.md
/<client_name>/<opportunity_name>/deliverables/problem_restatement_2026-03-20.html
/<client_name>/<opportunity_name>/deliverables/information_request_2026-03-20.md
/<client_name>/<opportunity_name>/deliverables/information_request_2026-03-20.html
/<client_name>/<opportunity_name>/deliverables/preliminary_approach_2026-03-20.md
/<client_name>/<opportunity_name>/deliverables/preliminary_approach_2026-03-20.html
/<client_name>/<opportunity_name>/deliverables/followup_email_2026-03-20.md
/<client_name>/<opportunity_name>/deliverables/formal_proposal_2026-04-15.md
/<client_name>/<opportunity_name>/deliverables/formal_proposal_2026-04-15.html
```

Presentations go in `/<client_name>/<opportunity_name>/presentations/` as flat, dated files:

```
/<client_name>/<opportunity_name>/presentations/discovery_findings_2026-03-20.html
/<client_name>/<opportunity_name>/presentations/technical_approach_2026-04-01.html
/<client_name>/<opportunity_name>/presentations/executive_briefing_2026-04-15.html
```

## Document Header Format

Every research document should start with a consistent header:

```markdown
# <Set Number> - <Source Type>: <Topic>

**Source:** `/<client_name>/<opportunity_name>/source/<filename>`
**Source Date:** <date> (<context>)
**Document Set:** <set number> (<description>)
**Pass:** <if applicable, which pass this represents>

---
```

Example:
```markdown
# 02 - Meeting: Technical Use Cases (Deep Dive)

**Source:** `/<client_name>/<opportunity_name>/source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on use cases

---
```

For discussion documents:
```markdown
# 03 - Discussion: Technical Approach

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Post-meeting analysis, informed by Sets 01, 02, and 02a

---
```
