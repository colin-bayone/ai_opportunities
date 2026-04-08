# Decomposition Methodology

**Established:** 2026-04-02
**Engagement:** Sephora - EDW Modernization (ETL/DataStage Migration Demo and Engagement)

---

## Blockchain Style Documentation

This research folder follows a **blockchain style** approach: documents are numbered chronologically and are **append-only**. Once written, they are never edited or revised. New understanding, corrections, or evolving thinking gets captured in subsequent documents that reference back to earlier ones.

### Why Blockchain Style

1. **Chronological progression of thought.** This engagement spans multiple meetings (Mani discovery calls, Andrew/Grishi meeting, technical deep dive with Malika/Sergey, internal debriefs with Saurav), multiple Claude sessions, and an evolving understanding of the problem. By preserving each document as it was written, we maintain a clear record of what we knew at each point in time.

2. **No re-explanation tax.** A new Claude session or team member can read forward through the numbered documents and reconstruct the full arc of discovery, including where assumptions were wrong and when corrections happened.

3. **Order of operations clarity.** Information arrived from different meetings, emails, and conversations. The numbering system makes it unambiguous which information was available at which point and what informed what.

4. **Honest record.** Early hypotheses that turn out to be wrong are just as valuable as correct ones. They show what was validated, what was invalidated, and why thinking evolved.

### Numbering Convention

- **Prefix number** = chronological document set (01, 02, 03...). All files from the same source event share a prefix.
- **Letter suffix** = supplementary material tied to the same event (02a, 02b). Used for debriefs, follow-up emails, etc.
- **Descriptive name** = what the file covers within that set.
- **Date suffix** = the date of the source material (not the date of analysis). Format: YYYY-MM-DD.

### Document Sets for This Engagement

| Set | Source Date | Type | Description |
|-----|-----------|------|-------------|
| 01 | 2026-02 | Meeting | Mani meeting 1 (initial discovery) |
| 02 | 2026-02 | Meeting | Mani meeting 2 (follow-up) |
| 03 | 2026-03-05 | Meeting | Andrew/Grishi meeting |
| 04 | 2026-03 | Meeting | Technical deep dive (Malika, Sergey, Neha, Zahra) |
| 04a | 2026-03 | Email | Malika email thread (Track A/B, materials provided) |
| 05 | 2026-03-30 | Debrief | Saurav/Colin call (demo status, vendor intel, strategy) |
| 06 | 2026-04-02 | Debrief | Saurav/Colin call (demo walkthrough, pipeline architecture, demo prep) |
| 07 | 2026-04-02 | Meeting | The actual demo to Sephora (Andrew, Grishi, Maher, Malika, Vishal) |

### Rules

1. Never go back and edit a numbered document after it is written.
2. New insights go in new documents with higher numbers.
3. Reference back to earlier documents by number when correcting or building on them.
4. Each document set covers one source event (a meeting, an email, a document, a discussion).
5. This methodology document is the only file in research/ that can be updated, because it describes the system itself.

### Document Header Format

Every research document starts with this header for traceability:

```
# <Set Number> - <Source Type>: <Topic>

**Source:** /sephora/edw_modernization/source/<filename>
**Source Date:** <date> (<context>)
**Document Set:** <set number> (<description>)
**Pass:** <if applicable, which pass this represents>

---
```

### Standard Files Per Set

- **People file** (first file for transcript-based sets): Who was present, roles, titles, sentiment, dynamics.
- **Topic map** (after first pass): Topics identified, proposed deep-dive files with rationale.
- **Deep-dive files** (one per topic, agent-written in parallel): Exhaustive detail on one specific topic.
- **Summary file** (always last): Short, high-level overview referencing all other files in the set.

### Bridge Documents

Between numbered document sets, a **bridge document** captures what changed. These are written after both sets exist.

### People Tracking (Dual System)

1. **Per-set people document** (in research/, blockchain style): Append-only.
2. **Living org chart** (`/sephora/edw_modernization/org_chart.md`): Always reflects most current understanding.

### Source Material Locations

Source transcripts and emails are stored in two locations:
- **Original location:** `/sephora/context/` (where they were first added to the repo)
- **Singularity source:** `/sephora/edw_modernization/source/` (symlinks or copies for singularity workflow)

Both are valid references. Research documents should reference the singularity source path.
