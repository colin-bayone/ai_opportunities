# Blockchain Methodology

## Core Concept

All research documents are numbered chronologically and are append-only. Once a document is written, it is never edited or revised. New understanding, corrections, or evolving thinking gets captured in subsequent documents that reference back to earlier ones.

This is called "blockchain style" because, like a blockchain, each entry is immutable and the chain is read forward to reconstruct the full state.

## Why This Approach

### 1. Chronological Progression of Thought

Consulting engagements span multiple meetings, multiple Claude sessions, and an evolving understanding of the problem. By preserving each document as it was written, you maintain a clear record of what was known at each point in time, not a retroactively cleaned-up version.

### 2. No Re-Explanation Tax

A new Claude session or team member can read forward through the numbered documents and reconstruct the full arc of discovery, including where assumptions were wrong and when corrections happened. No one has to re-explain what happened or how thinking evolved.

### 3. Order of Operations Clarity

When information arrives from different meetings, emails, and conversations, the numbering system makes it unambiguous which information was available at which point and what informed what.

### 4. Honest Record

Early hypotheses that turn out to be wrong are just as valuable as correct ones. They show what was validated, what was invalidated, and why thinking evolved. This prevents revisionist history and supports better decision-making.

## Numbering Convention

### Document Set Number

The prefix number (01, 02, 03...) represents a chronological document set. All files from the same source event share a prefix.

- `01_*` = first source event processed (could be a call prep, a meeting, an email, anything)
- `02_*` = second source event
- `03_*` = third source event

**There is nothing special about what number a set gets.** 01 is not always "call prep," 02 is not always "a meeting," 03 is not always "a discussion." The number reflects when in the project timeline the material was created or processed.

### Descriptive Name

The middle part of the filename describes what the file covers within that set:

- `01_call_prep_situational_context` = situational context from the call prep
- `02_meeting_technical_use_cases` = technical use cases from the meeting
- `02a_debrief_action_items` = action items from the debrief

### Date Suffix

The date at the end reflects the date of the source material, not the date of analysis:

- `01_call_prep_situational_context_2026-03-12.md` = source material is from March 12, 2026

This makes chronological ordering unambiguous even outside the numbering system.

### Full Example

```
01_call_prep_situational_context_2026-03-12.md
^^                                ^^^^^^^^^^
|                                 Date of source material
Set number (first event processed)
```

## Supplementary Material (Letter Suffixes)

When supplementary material is tied to the same event as an existing document set (e.g., an internal debrief immediately after a meeting, a follow-up email the same day), use a letter suffix rather than a new number:

- `02_meeting_*` = the meeting itself
- `02a_debrief_*` = internal debrief after the same meeting
- `02b_followup_email_*` = a follow-up email about the same meeting

This keeps it clear that the supplementary material is event-adjacent, not a new chronological step. The same append-only rules apply.

## Standard Files Per Set

### Required for Every Set

1. **Summary document** (e.g., `01_call_prep_summary_2026-03-12.md`)
   - Always the LAST file written for each set
   - Short, high-level overview of everything covered in the set
   - References the other files by name
   - Lets a new Claude session understand the set without reading every detail file
   - Critical because the number and type of detail files varies per set

### Required for Sets Based on Meetings/Calls

2. **People document** (e.g., `02_meeting_people_2026-03-12.md`)
   - Who was on the call, roles, titles, sentiment
   - Always created for any transcript-based set

### Created at the End (After Multiple Sets Exist)

3. **Bridge documents** (e.g., `01-02_changes_2026-03-12.md`)
   - Captures what changed between two document sets
   - What was confirmed, invalidated, or newly learned
   - Written retrospectively after both sets exist
   - Never written during processing

### Variable Files

Beyond the standard files, the set of detail files is not fixed. Different source events warrant different breakdowns. Common candidates:

- Technical deep dive breakdown (by topic)
- Business opportunity and specific notes
- Meeting breakdown and speaker dynamics
- Action items and next steps
- Hypothesis validation
- Infrastructure analysis

**The skill should always ask the user what files to create beyond the standard ones.** The user knows what matters. Ask, do not assume.

## Rules

1. Never go back and edit a numbered document after it is written.
2. New insights go in new documents with higher numbers.
3. Reference back to earlier documents by number when correcting or building on them.
4. Each document set covers one source event (a meeting, an email, a document, a discussion).
5. The methodology document (`/<client_name>/<opportunity_name>/research/00_methodology_<date>.md`) is the only file that can be updated, because it describes the system itself.
6. The org chart (`/<client_name>/<opportunity_name>/org_chart.md`) is the only other file that can be updated (see People Tracking).
7. Tracking files in sub-singularity `tracking/` folders are living documents (editable). They are the exception to the append-only rule, alongside the org chart and methodology doc. See `tracking_folder_pattern.md` for details.

## Application to Sub-Singularities

The blockchain methodology applies identically within each sub-singularity. A sub-singularity has its own research chain with its own numbering (01, 02, 03...) independent of the parent. The same immutability rules apply: research documents are never edited after creation, summaries are always last, bridge documents are retrospective.

The one addition for sub-singularities is the `tracking/` folder, which contains living operational documents (action items, blockers, decisions) that ARE editable. These complement the immutable research chain with a current-state operational view. See `nested_singularity.md` for the full pattern and `tracking_folder_pattern.md` for the tracking document specifications.

## Reading Order for a New Session

A new Claude session picking up an engagement should read:

1. `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` to understand the system
2. The summary documents in `/<client_name>/<opportunity_name>/research/` in order (01 summary, 02 summary, 02a summary, 03 summary, etc.)
3. `/<client_name>/<opportunity_name>/org_chart.md` for the current people state
4. `/<client_name>/<opportunity_name>/planning/skill_notes.md` if it exists (accumulated do's/don'ts)
5. `/<client_name>/<opportunity_name>/planning/session_handoff_<date>.md` if it exists (where the last session left off)
6. Then dive into specific detail files in `/<client_name>/<opportunity_name>/research/` as needed

This gives full context in minutes without reading every file.
