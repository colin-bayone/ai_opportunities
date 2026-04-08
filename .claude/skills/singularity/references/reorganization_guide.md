# Singularity Reorganization Guide

**Purpose:** Step-by-step instructions for reorganizing existing engagement folders into Singularity format. Designed for any Claude session to follow, whether or not the operator has deep context on the engagement.

**When to use:** When an engagement folder predates Singularity, has been partially organized, or needs validation that its Singularity structure is complete and current.

---

## Overview

Engagement folders fall into one of four states:

| State | Description | Action |
|-------|-------------|--------|
| **A: Never touched** | Raw folder with transcripts, notes, deliverables, no Singularity structure | Full reorganization from scratch |
| **B: Partially done** | Some Singularity structure exists, but content is incomplete or mixed with unorganized material | Validate existing structure, process remaining content |
| **C: Fully done, needs validation** | Complete Singularity structure, but may have gaps or new content not yet processed | Audit and fill gaps |
| **D: Multi-project folder** | A client folder containing multiple engagement subfolders, some organized, some not | Per-subfolder assessment, then top-level cleanup |

Most real cases are State D (like Sephora, which has two Singularity-formatted projects plus loose content). The process below handles all four states.

---

## Phase 0: Explore and Map (ALWAYS DO THIS FIRST)

**Rule: Never move, create, or modify anything without explicit user approval.**

### Step 0.1: Inventory the Folder

List everything recursively. Understand what exists before proposing anything.

For each item, classify it as:
- **Source material:** Transcripts, emails, call preps, meeting notes, PDFs, images, documents provided by the client
- **Research/analysis:** Decomposition docs, meeting breakdowns, synthesized findings, technical references
- **Planning:** Session handoffs, game plans, goals, status tracking, glossaries
- **Deliverables:** Client-facing documents (HTML, PDF, slide decks)
- **Pricing:** Pricing models, Excel specs, correction prompts
- **Infrastructure:** Index files, READMEs, scripts, utilities
- **Unknown:** Anything that does not fit the above categories

### Step 0.2: Identify Projects

A "project" is a distinct engagement or workstream with its own source materials, timeline, and deliverables. Within a client folder, there may be multiple projects.

Examples from Sephora:
- `edw_modernization/` — One project (EDW data warehouse modernization)
- `qa_qe_playwright/` — Another project (QA/QE Playwright testing opportunity)
- Job description creation for Ravi — Could be its own project or an archive item

Ask: **Does each folder represent a distinct engagement with its own meetings, transcripts, and deliverables?** If yes, it is a project. If it is supporting material for an existing project, it belongs inside that project.

### Step 0.3: Determine State for Each Project

For each identified project, determine its state (A, B, C, or D) based on:

| Check | State A (Never touched) | State B (Partial) | State C (Complete) |
|-------|------------------------|-------------------|-------------------|
| Has `source/` folder? | No | Maybe | Yes |
| Has `research/` with numbered sets? | No | Some | Yes, chronological |
| Has `00_methodology` doc? | No | Maybe | Yes |
| Has `org_chart.md`? | No | Maybe | Yes |
| Has bridge documents? | No | No | Yes |
| Has summaries for each set? | No | Some | Yes |
| Has unprocessed source materials? | Yes (everything) | Yes (some) | No (or newly added) |

### Step 0.4: Produce the Map

Write a markdown document summarizing:
1. Every project identified and its state
2. Every file/folder that does NOT belong to a project (candidates for archive or relocation)
3. Source materials that exist but have not been processed
4. Any chronological gaps (meetings referenced but transcripts missing)
5. Specific recommendations for each item

**Present this map to the user and get approval before doing anything.**

---

## Phase 1: Archive and Structure (State A and State D cleanup)

### For State A (Never touched):

1. Create the full Singularity folder structure:
   ```
   /<project>/
   ├── org_chart.md
   ├── source/
   ├── research/
   ├── planning/
   ├── pricing/
   ├── deliverables/
   ├── presentations/
   ├── decisions/
   └── progress/
   ```

2. Move source materials (transcripts, emails, images, PDFs) into `source/`. Rename with dates if not already dated.

3. Move existing deliverables into `deliverables/` with dates in filenames.

4. Move existing analysis/research into `archive/` within the project (NOT into `research/` — Singularity research docs are written fresh from source materials).

5. Move planning docs into `planning/` or `archive/` depending on whether they are still relevant.

6. **Format transcripts** using `format_transcript.py` from the Singularity skill scripts folder. Every single-line transcript must be formatted before processing.

### For State D (Multi-project folder cleanup):

1. Identify which top-level items belong to which project.

2. Move orphaned content that belongs to a specific project into that project's `source/` or `archive/`.

3. Move content that does not belong to any project into a top-level `archive/` folder.

4. The top-level client directory should contain ONLY:
   - Project subfolders (each with Singularity structure)
   - `archive/` (for content that predates or does not fit any project)
   - `00_index.md` (optional, navigation file)

**Present the proposed moves to the user. Get approval. Then execute.**

---

## Phase 2: Process Source Materials (State A and State B)

Follow the standard Singularity processing order:

### Step 2.1: Establish the Timeline

List all source materials in chronological order. Assign set numbers:
- Each distinct event (meeting, email, discussion) gets a set number (01, 02, 03...)
- Supplementary material for the same event gets a letter suffix (01a, 01b)
- Date reflects the source material date, not the processing date

**Present the chronological timeline and set numbering to the user. Get approval.**

### Step 2.2: Write the Methodology Doc

Write `research/00_methodology_<date>.md` using the Singularity template. Date is the earliest source material date.

### Step 2.3: Process Each Set Chronologically

For each set, follow the standard Singularity processing flow:

**For transcripts (most common):**
1. Read prior context (latest summary + org chart)
2. Format the transcript if not already done
3. Pass 1: People file (always first for transcript sets)
4. Pass 1 continued: Topic map with proposed deep-dive files and rationale
5. **Present topic map to user. Get approval.**
6. Spawn parallel agents for deep-dive files (one agent per topic)
7. Update org chart
8. Bridge document (if not the first set)
9. Summary (always last)
10. Offer web research if unfamiliar technologies encountered

**For call preps, emails, notes:**
- Lighter treatment. Usually 1-2 files plus a summary.
- Still follows the header format and numbering convention.

**For discussions (Colin + Claude working sessions):**
- If detailed notes already exist in archive, adopt them with reformatted headers and corrected set numbers.
- Add a "Note: Originally numbered Set X. Renumbered to Set Y during Singularity reorganization" line.

**For existing Singularity research docs being adopted:**
- Copy to the correct location with renumbered filenames
- Read each file's header and update the set number, document set description, and any cross-references
- Add a renumbering note in the header

### Step 2.4: After All Sets Are Processed

1. Write a session handoff document to `planning/session_handoff_<date>.md`
2. Update the session plan or progress tracking as appropriate
3. Do a final inventory count and present the summary to the user

---

## Phase 3: Validate (State B and State C)

For projects that already have Singularity structure, validate completeness.

### Checklist

| Item | Check |
|------|-------|
| `source/` contains all raw materials | Compare against any external sources, archive folders, or other repos |
| `research/00_methodology` exists | Must be present |
| Every source material has a corresponding set | No unprocessed transcripts or emails |
| Every set has a summary | Summary is always the last file per set |
| Every set (after the first) has a bridge document | Bridges track what changed between sets |
| `org_chart.md` is current | Should reflect the latest set's people information |
| All files have proper headers | Set number, source, date, document set, pass |
| Chronological order is correct | Set numbers increase with date |
| No orphaned files outside the structure | Everything is in the right folder |
| `planning/session_handoff_<date>.md` exists | For session continuity |

### Common Issues

1. **Missing bridge documents** — Write them retroactively. They capture what changed between sets.
2. **Outdated org chart** — Read the latest set's people file and update.
3. **Unprocessed source materials** — New transcripts or emails added after the last session. Process as the next set.
4. **Inconsistent numbering** — If sets were numbered in a prior system, renumber with notes.
5. **Research docs without proper headers** — Add headers. Do not change the content.

---

## Phase 4: Top-Level Cleanup (State D only)

After all projects within a client folder are validated, clean up the top level.

### Rules

1. **Only projects and archive at the top level.** No loose files, no orphaned folders.
2. **`archive/` is flat or minimally nested.** It preserves old content, not reorganizes it.
3. **`00_index.md` is optional** but helpful for navigation. Update it if it exists.
4. **Do not delete anything.** Move to archive. The user decides what to delete later.

### Decision Framework for Orphaned Content

| Content Type | Where It Goes |
|-------------|--------------|
| Old analysis that duplicates Singularity research | `archive/` |
| Source material that belongs to a project | That project's `source/` |
| Deliverables that belong to a project | That project's `deliverables/` |
| Content for a project that doesn't exist yet | Create the project or `archive/` (ask user) |
| Scripts, utilities, tools | `planning/` of the relevant project, or skill scripts folder |
| Index files, READMEs | Update or `archive/` |

---

## Worked Examples

### Example 1: Sephora (State D — Multi-project with mixed content)

**Current state:**
- `edw_modernization/` — State C (Singularity complete, needs validation)
- `qa_qe_playwright/` — State C (Singularity complete, needs validation)
- `2025-02-25_andrew-meeting-prep/` — 124 files, pre-Singularity meeting analysis. Overlaps with edw_modernization research.
- `context/` — 37 raw source files including ETL use case materials
- `ravi/` — 26 files, job description creation track
- `project/`, `planning/`, `stakeholders/`, `deliverables/`, `research/`, `docs/` — Legacy top-level folders with 0-5 files each
- `00_index.md` — Outdated navigation file

**Proposed approach:**
1. Validate `edw_modernization/` (State C checklist)
2. Validate `qa_qe_playwright/` (State C checklist)
3. Compare `2025-02-25_andrew-meeting-prep/` against `edw_modernization/research/` to check if its content is already captured. If yes, archive it. If not, identify what is missing and either adopt it or process it as a new set.
4. Review `context/` files. Source materials that belong to edw_modernization go into `edw_modernization/source/`. ETL use case materials may warrant their own project or go to archive. Ask user.
5. Determine if `ravi/` is a standalone project (create Singularity structure) or a completed task (archive). Ask user.
6. Move legacy top-level folders (`project/`, `planning/`, `stakeholders/`, `deliverables/`, `research/`, `docs/`) to `archive/`. Their content was the pre-Singularity version of what now lives in `edw_modernization/`.
7. Update or recreate `00_index.md` as a navigation file pointing to the projects.

**End state:**
```
sephora/
├── 00_index.md
├── edw_modernization/    (validated Singularity project)
├── qa_qe_playwright/     (validated Singularity project)
├── ravi/                 (Singularity project OR archive — user decides)
└── archive/              (everything else)
```

### Example 2: Tailored Brands (State A — Never touched)

**Current state:**
- 11 files across 5 folders
- One source transcript (`meetings/1.txt`, 32KB internal planning call)
- One image (`IMG_0012.jpeg`, handwritten org chart)
- Existing analysis docs (transcript decomposition, synthesized research, game plan)
- Two HTML deliverables (discovery prep v1 and v2)
- All content from a single engagement: discovery meeting prep for Tailored Brands

**Proposed approach:**
1. This is a single project. Create Singularity structure at `tailored_brands/discovery/` or keep at `tailored_brands/` if there is only one engagement.
2. Move `meetings/1.txt` to `source/`. Format it.
3. Move `IMG_0012.jpeg` to `source/`.
4. Move HTML deliverables to `deliverables/`.
5. Move existing analysis to `archive/` (Singularity processes from source, not from prior analysis).
6. Process the transcript as Set 01 with full Singularity treatment.
7. The existing analysis in `archive/` can be compared afterward for gap coverage.

**End state:**
```
tailored_brands/
├── org_chart.md
├── source/
│   ├── internal_planning_call_2026-02-18.txt
│   ├── internal_planning_call_2026-02-18_formatted.txt
│   └── IMG_0012.jpeg
├── research/
│   ├── 00_methodology_2026-02-18.md
│   ├── 01_meeting_people_2026-02-18.md
│   ├── 01_meeting_topic_map_2026-02-18.md
│   ├── 01_meeting_<topics>_2026-02-18.md
│   └── 01_meeting_summary_2026-02-18.md
├── planning/
├── pricing/
├── deliverables/
│   ├── discovery_prep_tailored_brands_2026-03-04.html
│   └── discovery_prep_tailored_brands_v2_2026-03-04.html
├── presentations/
├── decisions/
├── progress/
└── archive/
    ├── project/
    ├── planning/
    └── context/
```

---

## Key Principles

1. **Never modify existing Singularity research files.** Blockchain rule. New understanding goes in new documents.
2. **Always present plans to the user before executing.** The user controls what gets created.
3. **Format transcripts before reading them.** Use `format_transcript.py` from `.claude/skills/singularity/scripts/`.
4. **Process chronologically.** Never skip ahead or process out of order.
5. **Archive, never delete.** Old content goes to `archive/`, not the trash.
6. **One project per engagement.** If a client has multiple engagements, each gets its own Singularity-structured folder.
7. **Top-level client folder is clean.** Only projects, archive, and an optional index file.
8. **Bridge documents capture evolution.** Every set after the first gets a bridge document.
9. **Summaries are always last.** Every set ends with a summary that references all other files in the set.
10. **The org chart is the only living document** in research. Everything else is append-only.
