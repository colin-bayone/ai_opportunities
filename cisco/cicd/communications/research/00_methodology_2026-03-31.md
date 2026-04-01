# Decomposition Methodology

**Established:** 2026-03-31
**Engagement:** Cisco CI/CD Pipeline Modernization (communications and action planning)

---

## Blockchain Style Documentation

This research folder follows a **blockchain style** approach: documents are numbered chronologically and are **append-only**. Once written, they are never edited or revised. New understanding, corrections, or evolving thinking gets captured in subsequent documents that reference back to earlier ones.

### Why Blockchain Style

1. **Chronological progression of thought.** This engagement has already spanned months of conversations, meetings, and an evolving understanding of the problem. By preserving each document as it was written, we maintain a clear record of what was known at each point in time.

2. **No re-explanation tax.** A new Claude session or team member can read forward through the numbered documents and reconstruct the full arc, including where assumptions were wrong and when corrections happened.

3. **Order of operations clarity.** When information arrives from different meetings, emails, and conversations, the numbering system makes it unambiguous which information was available at which point.

4. **Honest record.** Early hypotheses that turn out to be wrong are just as valuable as correct ones.

### Numbering Convention

- **Prefix number** = chronological document set (01, 02, 03...). All files from the same source event share a prefix.
- **Letter suffix** = supplementary material tied to the same event (02a, 02b).
- **Descriptive name** = what the file covers within that set.
- **Date suffix** = the date of the source material (not the date of analysis). Format: YYYY-MM-DD.

### Document Sets for This Engagement

| Set | Source | Date | Description |
|-----|--------|------|-------------|
| 01 | Feb 17 discovery meeting transcript + clarification questions | 2026-02-17 | In-person discovery at Cisco with Anand, Divakar, Srinivas |
| 02 | WebEx group chat + private Anand chat | 2026-02-10 to 2026-03-31 | Full external communication record showing timeline and delays |
| 03 | Internal team meeting | 2026-03-18 | First internal team briefing (Colin, Saurav, Askari) |
| 04 | Internal team meeting | 2026-03-30 | Full team briefing (Colin, Saurav, Askari, Srikar) |
| 04a | Discovery brainstorming notes | 2026-03-31 | Colin's brainstormed topics for Anand response |

### Rules

1. Never go back and edit a numbered document after it is written.
2. New insights go in new documents with higher numbers.
3. Reference back to earlier documents by number when correcting or building on them.
4. Each document set covers one source event.
5. This methodology document is the only file in research/ that can be updated.

### Document Header Format

Every research document starts with:

```
# <Set Number> - <Source Type>: <Topic>

**Source:** cisco/cicd/communications/source/<filename>
**Source Date:** <date> (<context>)
**Document Set:** <set number> (<description>)
**Pass:** <what this specific read was focused on>

---
```

### Standard Files Per Set

- **People file** (first file for transcript sets): Who was present, roles, titles, sentiment.
- **Topic map** (after first pass): Topics identified, proposed deep-dive files.
- **Deep-dive files** (one per topic, agent-written in parallel): Exhaustive detail.
- **Summary file** (always last): Short overview referencing all files in the set.

### Bridge Documents

Between sets, a bridge document captures what changed (e.g., `01-02_changes_<date>.md`).

### People Tracking (Dual System)

1. **Per-set people documents** in research/ (blockchain style, append-only)
2. **Living org chart** at `cisco/cicd/communications/org_chart.md` (always current, the one exception to append-only)

### Cross-References

This communications folder draws on prior structured knowledge in the broader `cisco/cicd/` directory:
- `cisco/cicd/documents/` -- problem understanding, clarification questions, resourcing
- `cisco/cicd/meetings/2026-02-17_discovery_summaries/` -- detailed meeting breakdowns
- `cisco/cicd/planning/2026-02-02_resource_planning/` -- team structure, roles, costs, JDs
- `cisco/cicd/SOW/` -- the signed SOW document

### Reading Order for a New Session

1. This methodology document
2. Summary documents in order (01 summary, 02 summary, etc.)
3. The org chart
4. Planning files (skill notes, session handoff)
5. Then dive into specific detail files as needed
