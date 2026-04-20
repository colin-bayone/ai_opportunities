# Team Sub-Singularity: Methodology

**Engagement:** Cisco CI/CD
**Created:** 2026-04-10
**Purpose:** Process internal team meetings, standups, and team-to-Cisco sync meetings into structured operational intelligence. Separate from the main engagement research chain, which tracks the client relationship and discovery arc.

---

## What This Is

This is a sub-singularity within the Cisco CI/CD engagement. It has its own source materials, its own numbered research chain, and its own tracking documents. It follows the same blockchain methodology as the parent (append-only, numbered chronologically, never edit after creation) but with a processing focus optimized for operational content rather than client discovery.

## What Goes Here vs. the Main Chain

| Content Type | Where It Goes |
|-------------|--------------|
| Client discovery meetings | Main chain (`cisco/cicd/research/`) |
| Internal team standups and syncs | Here (`cisco/cicd/team/research/`) |
| Team meetings with Cisco counterparts (without Colin) | Here, or a sibling sub-singularity if volume warrants |
| Strategy discussions (Colin + Claude) | Main chain |
| Deliverables and proposals | Main chain (`cisco/cicd/deliverables/`) |
| Presentations | Main chain (`cisco/cicd/presentations/`) |

## Processing Focus

Team meetings are processed for operational content. The standard passes are:

1. **People and dynamics.** Who was present, engagement level, team dynamics.
2. **Action items and assignments.** New items, status of prior items, who owes what by when.
3. **Blockers, dependencies, and escalations.** What is preventing progress, what needs external resolution.
4. **Decisions made and rationale.** What was decided, by whom, why.
5. **Technical discussion.** Only when substantive technical content exists (architecture, approach, tools).
6. **Summary.** Always last. References all files in the set.

## Tracking Documents

The `tracking/` folder contains living operational documents updated after every meeting:

- `action_items.md` — Cumulative tracker with open, completed, and blocked items
- `blockers.md` — Current blockers with status and escalation path
- `decisions.md` — Decisions log with rationale

These are the operational dashboard. The research chain is the audit trail.

## Cross-Reference

`cross_reference.md` at the team root maps team sets to main chain sets when content overlaps.

## Numbering

Independent chain: 01, 02, 03... No relation to main chain numbering.
