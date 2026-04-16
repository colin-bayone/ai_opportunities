# Decomposition Methodology

**Established:** 2026-03-20
**Project:** Lam Research - Custom NER/Redaction for IP Protection

---

## Blockchain Style Documentation

This research folder follows a **blockchain style** approach: documents are numbered chronologically and are **append-only**. Once written, they are never edited or revised. New understanding, corrections, or evolving thinking gets captured in subsequent documents that reference back to earlier ones.

### Why Blockchain Style

1. **Chronological progression of thought.** This engagement will span multiple meetings, multiple Claude sessions, and an evolving understanding of the problem. By preserving each document as it was written, we maintain a clear record of what we knew at each point in time - not a retroactively cleaned-up version.

2. **No re-explanation tax.** A new Claude session or team member can read forward through the numbered documents and reconstruct the full arc of discovery, including where assumptions were wrong and when corrections happened.

3. **Order of operations clarity.** When information arrives from different meetings, emails, and conversations, the numbering system makes it unambiguous which information was available at which point and what informed what.

4. **Honest record.** Early hypotheses that turn out to be wrong are just as valuable as correct ones - they show what was validated, what was invalidated, and why our thinking evolved.

### Numbering Convention

- **Prefix number** = chronological document set (01, 02, 03...). All files from the same source event share a prefix.
- **Descriptive name** = what the file covers within that set.
- **Date suffix** = the date of the source material (not the date of analysis).

Example: `01_call_prep_situational_context_2026-03-12.md` means this is from document set 01 (the call prep), covers situational context, and the source material is from March 12, 2026.

### Rules

- Never go back and edit a numbered document after it's written.
- New insights go in new documents with higher numbers.
- Reference back to earlier documents by number when correcting or building on them.
- Each document set covers one source event (a meeting, an email, a document).

### Summary Documents

Every document set ends with a **summary file** (e.g., `01_call_prep_summary_2026-03-12.md`). This is a short, high-level overview of everything covered in that set's files. Its purpose is to let a new Claude session quickly understand the document set without reading every detail file. The summary is the last file written for each set and should reference the other files by name.

The number and type of detail files will vary per document set - there is no fixed template. The summary tells you what's there and why.

### Bridge Documents

Between numbered document sets, a **bridge document** captures what changed (e.g., `01-02_changes.md`). These are written after both sets exist and describe what was confirmed, invalidated, or newly learned between the two source events. Bridge documents are created at the end, not during processing.

### People Tracking (Dual System)

People information is tracked in two places:

1. **Per-set people document** (in `research/`, blockchain style): Captures what we learned about people from that specific source event. Append-only like everything else in research.

2. **Living org chart** (`org_chart.md` at session folder root): Always reflects the most current and complete understanding of all people across all meetings. This file IS updated over time - it's the one exception to append-only, because its purpose is to be the current-state reference.

The workflow: before processing a new document set, read the current org chart to have full context on known people. After processing, update the org chart with anything new. The per-set people document preserves what we learned when.

### Processing Order

When starting a new document set:
1. Read the prior set's summary document (for context on where we left off)
2. Read the current org chart (for full people context)
3. Process the new source material
4. Write the detail files, people file, and summary file
5. Update the org chart with new information
