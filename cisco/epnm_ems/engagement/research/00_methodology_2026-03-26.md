# 00 - Methodology

**Created:** 2026-03-26
**Engagement:** Cisco EPNM-to-EMS UI Conversion (Guhan/ Selva)
**Session Folder:** `claude/2026-02-20_ui-conversion-discovery/`

---

## Approach: Blockchain-Style Documentation

All research documents in this folder are numbered chronologically and are append-only. Once a document is written, it is never edited. New understanding, corrections, or evolving thinking goes in new documents that reference back to earlier ones.

This preserves the full arc of discovery across sessions. A new Claude session reads forward through the numbered documents and reconstructs the engagement state without re-explanation.

## Numbering Convention

- **Set number prefix** (01, 02, 03...): Represents a chronological source event. All files from the same event share a prefix.
- **Descriptive name**: What the file covers within that set.
- **Date suffix**: Date of the source material (ISO format), not the date of analysis.
- **Letter suffixes** (02a, 02b): Supplementary material tied to the same event (e.g., internal debrief after a meeting).

Example: `01_meeting_people_2026-03-25.md` = Set 01, people file, source material from March 25, 2026.

## Standard Files Per Set

| File Type | When Created |
|-----------|-------------|
| People document | First file for any transcript-based set |
| Topic map | After first pass of transcript |
| Per-topic deep dives | After topic map is approved by user |
| Summary | Always the LAST file for each set |
| Bridge document | After both sets exist (captures what changed between sets) |

## Rules

1. Never edit a numbered document after it is written.
2. New insights go in new documents with higher numbers.
3. Reference earlier documents by number when building on them.
4. Each document set covers one source event.
5. This methodology document (00) is the only file that can be updated.
6. The org chart (`org_chart.md`) is the only other file that can be updated.

## Processing Order for Transcripts

1. Read prior context (previous summary, org chart).
2. Pass 1: People file (first file written).
3. Pass 1 continued: Topic map with proposed detail files.
4. Ask user to approve the file list.
5. Per-topic deep dives (parallel agents, one topic each).
6. Update org chart.
7. Bridge document (if prior set exists).
8. Summary document (always last).

## Prior Context

This engagement has existing materials in the parent session folder that predate this methodology:

- `planning/` - Session working scratch, proposal iterations (v1-v5)
- `research/` - Technical references (Dojo framework, Angular/Java integration, timeline, themes)
- `source/` - Meeting transcripts (Feb 9, Feb 20, March 25)
- Root-level HTML files - POC proposal versions, the current being `poc_proposal_v5_detailed.html`

These files are context. The blockchain-style documentation starts with Set 01 in this `engagement/research/` folder.

## Source Material Quality

Transcripts are speech-to-text and contain transcription errors. Apply common sense:
- "EPR1" = "EPNM"
- "Tojo" = "Dojo"
- "element management institute" = "Element Management System (EMS)"
- "EMRs" = "EMS"
- "Cloud Code" = "Claude Code"
- "land graph" = "LangGraph"

## Reading Order for a New Session

1. This methodology document (00)
2. Summary documents in order (01 summary, 02 summary, etc.)
3. The org chart (`../org_chart.md`)
4. Dive into detail files as needed
