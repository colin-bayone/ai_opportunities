# Decomposition Methodology

**Established:** 2026-04-06
**Engagement:** Lam Research - IP Protection / Confidential Information Detection and Redaction

---

## Blockchain Style Documentation

This research folder follows a **blockchain style** approach: documents are numbered chronologically and are **append-only**. Once written, they are never edited or revised. New understanding, corrections, or evolving thinking gets captured in subsequent documents that reference back to earlier ones.

### Why Blockchain Style

1. **Chronological progression of thought.** This engagement will span multiple meetings, multiple Claude sessions, and an evolving understanding of the problem. By preserving each document as it was written, we maintain a clear record of what we knew at each point in time, not a retroactively cleaned-up version.

2. **No re-explanation tax.** A new Claude session or team member can read forward through the numbered documents and reconstruct the full arc of discovery, including where assumptions were wrong and when corrections happened.

3. **Order of operations clarity.** When information arrives from different meetings, emails, and conversations, the numbering system makes it unambiguous which information was available at which point and what informed what.

4. **Honest record.** Early hypotheses that turn out to be wrong are just as valuable as correct ones. They show what was validated, what was invalidated, and why thinking evolved.

### Numbering Convention

- **Prefix number** = chronological document set (01, 02, 03...). All files from the same source event share a prefix.
- **Letter suffix** = supplementary material tied to the same event (02a, 02b). Used for debriefs, follow-up emails, etc.
- **Descriptive name** = what the file covers within that set.
- **Date suffix** = the date of the source material (not the date of analysis). Format: YYYY-MM-DD.

Example: `01_call_prep_situational_context_2026-03-12.md` means this is from document set 01 (the call prep), covers situational context, and the source material is from March 12, 2026.

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

**Source:** /lam_research/ip_protection/source/<filename>
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

Between numbered document sets, a **bridge document** captures what changed (e.g., `01-02_changes_2026-03-12.md`). These are written after both sets exist and describe:
- Hypotheses validated, invalidated, or still open
- What we got wrong or did not anticipate
- What we got right
- New information not in the prior set
- Questions answered from earlier open items

### People Tracking (Dual System)

1. **Per-set people document** (in research/, blockchain style): Captures what we learned about people from that specific source event. Append-only.
2. **Living org chart** (`/lam_research/ip_protection/org_chart.md`): Always reflects the most current understanding. This file IS updated over time, the one exception to append-only.

### Document Sets in This Engagement

| Set | Source | Date | Description |
|-----|--------|------|-------------|
| 01 | Call prep document | 2026-03-12 | Pre-discovery call preparation |
| 02 | Discovery call transcript | 2026-03-12 | First meeting with Lam Research team |
| 02a | Internal debrief | 2026-03-12 | Colin and Anuj post-call debrief |
| 03 | Prior working discussion | 2026-03-20 | Technical approach and strategy discussion (from prior Claude session) |

### Processing Order for New Sets

1. Read the prior set's summary document (for context on where we left off).
2. Read the current org chart (for full people context).
3. Process the new source material (multi-pass for transcripts).
4. Write detail files (agents write deep dives in parallel).
5. Update the org chart with new information.
6. Write bridge document (what changed vs. prior set).
7. Write summary document (always last).

### Reading Order for a New Session

1. This methodology document.
2. Summary documents in order (01 summary, 02 summary, 02a summary, etc.).
3. The org chart.
4. Skill notes (if exists, in planning/).
5. Session handoff (if exists, in planning/).
6. Then dive into specific detail files as needed.

### Note on This Engagement

This engagement was originally processed in a pre-Singularity session (March 2026). That work is archived at `/lam_research/ip_protection/archive/`. This research library is a fresh reprocessing of all source material using the Singularity methodology.
