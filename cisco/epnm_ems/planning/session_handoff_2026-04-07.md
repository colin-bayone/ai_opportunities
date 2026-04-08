# Session Handoff: 2026-04-07

**Session:** Full Singularity reorganization of cisco/epnm_ems/
**Duration:** Single session
**Status:** Complete

---

## What Was Done

Reorganized the entire `cisco/epnm_ems/` engagement folder from scratch using the Singularity skill. All prior content was moved to `archive/`. Source materials were gathered from two repositories, formatted, and processed chronologically.

### Research Library: 57 documents across 9 sets

| Set | Date | Type | Source | Documents |
|-----|------|------|--------|-----------|
| 01 | Feb 9 | Meeting | guhan_selva-2-9-2026.txt | 8 (people, topic map, 5 deep dives, summary) |
| 01a | ~Feb 18 | Call Prep | discovery_questions_call_prep_2026-02-20.md | 2 |
| 02 | Feb 20 | Meeting | guhan_selva-2-20-2026.txt | 8 + bridge (01-02) |
| 03 | Mar 25 | Meeting | guhan_selva-3-25-2026.txt | 7 + bridge (02-03) |
| 04 | Mar 26 | Discussion | Pricing strategy | 2 + bridge (03-04) |
| 05 | Mar 30 | Internal Call | ceo_rahul_call_2026-03-30.txt | 3 |
| 05a | Mar 30 | Notes | venkat_notes_2026-03-30.txt | 2 + bridge (04-05) |
| 06 | Apr 2 | Discussion | Pricing breakdown (adopted from archive) | 6 + bridge (05-06) |
| 07 | Apr 6 | Meeting | selva_and_team_4-6-2026.txt | 9 + bridge (06-07) |
| 08 | Apr 7 | Web Research | EPNM stack, EMS stack, conversion patterns | 4 |

### Other Artifacts
- Methodology document (00_methodology)
- Living org chart (updated through Set 07)
- 10 deliverables in deliverables/
- 6 pricing files in pricing/
- Session plan in planning/
- All original content preserved in archive/
- format_transcript.py copied to singularity skill scripts/

---

## Key Findings

### Scope Reframe (Set 03 — Most Important)
The project scope fundamentally changed between Set 02 (Feb 20) and Set 03 (Mar 25):
- **Before:** Full-stack vertical conversion of missing EPNM functionality into EMS
- **After:** Classic view toggle on screens that ALREADY EXIST in EMS. Backend stays. UX overlay only.
- This changes the nature, complexity, and pricing of the entire engagement.

### Pricing Inconsistency (Flagged, Unresolved)
The $500K pricing model (Sets 04, 06) uses "full vertical slice" and "full-stack" language that contradicts the Set 03 reframe. The per-screen effort estimate of 8 hours may need recalibration for the lighter toggle scope.

### People
- **Guhan:** Decision-maker, strategic direction
- **Selva Subramanian:** Operational lead, day-to-day counterpart
- **Venkat:** Executive sponsor, exploring July timeline
- **Praveen Kumar Vangala:** Engineering team lead (likely = "Varel" from early sets)
- **7 Cisco tech leads** identified in Set 07 with names, emails, roles
- **BayOne team:** Colin (technical lead), Neha (ops), Rahul (exec), Zahra (accounts)

### Technical Stack
- **EPNM:** Dojo 1.x, Java monolith, Oracle
- **EMS:** Angular 21, Spring Boot + Go, Postgres, Harbor/Magnetic design system
- ~80% of backend already reimplemented in EMS

---

## What Comes Next

1. **POC execution** — Colin begins code exploration on Cisco hardware
2. **Access provisioning** — AD groups, VMs, repo access (action items from Set 07)
3. **Pricing recalibration** — Resolve the full-stack vs toggle inconsistency
4. **Team walkthrough follow-ups** — Deeper sessions on specific screens may be needed
5. **Any new meetings or transcripts** — Process as Set 09+ following the same methodology

---

## Reading Order for a New Session

1. `research/00_methodology_2026-02-09.md`
2. Summary documents in order: 01, 01a, 02, 03, 04, 05, 05a, 06, 07
3. `org_chart.md`
4. This handoff document
5. Then dive into specific detail files as needed
