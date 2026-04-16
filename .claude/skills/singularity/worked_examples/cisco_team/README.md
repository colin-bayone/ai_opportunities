# Worked Example: Team Sub-Singularity

**Source engagement:** Cisco CI/CD
**Created:** 2026-04-10
**Purpose:** Reference implementation of the nested singularity (sub-singularity) pattern applied to team meeting processing. Read this to see what a functioning team sub-singularity looks like end-to-end.

---

## What This Example Demonstrates

1. **Independent numbering chain.** Set 01 here is unrelated to Set 01 in the parent engagement. The team sub-singularity has its own chronological sequence.

2. **Team meeting processing passes.** Instead of the client-meeting topic-map approach, team meetings use standard passes: people, action items, blockers, technical discussion, summary.

3. **Tracking folder (dual model).** The `research/` chain is immutable (blockchain). The `tracking/` folder has living documents (action_items.md, blockers.md, decisions.md) that get updated after every meeting set.

4. **Cross-reference file.** `cross_reference.md` at the root maps team sets to parent engagement sets where content overlaps.

5. **Standard folder structure.** `source/`, `research/`, `tracking/`, `documents/`, `planning/` all present. `tracking/` is always created even if initially empty.

## Contents

```
worked_example_team/
├── README.md                              (this file)
├── cross_reference.md                     (maps Team Set 01 to Main Set 10)
├── source/                                (empty in the example — real transcript not included)
├── research/
│   ├── 00_methodology_2026-04-10.md       (team sub-singularity methodology)
│   ├── 01_standup_people_2026-04-10.md    (who was present, dynamics)
│   ├── 01_standup_action_items_2026-04-10.md  (all action items with status)
│   ├── 01_standup_blockers_2026-04-10.md  (blockers, access status, escalation strategy)
│   ├── 01_standup_technical_discussion_2026-04-10.md  (build systems, log architecture, WebEx tools)
│   └── 01_standup_summary_2026-04-10.md   (summary referencing all files in the set)
├── tracking/
│   ├── action_items.md                    (cumulative tracker: open, completed, blocked)
│   ├── blockers.md                        (active and resolved blockers)
│   └── decisions.md                       (numbered decision log with rationale)
├── documents/                             (empty — no formatted outputs produced for this set)
└── planning/                              (empty — no session handoffs yet)
```

## Key Differences From the Parent Worked Example

| Aspect | Parent (`worked_example/`) | Team (`worked_example_team/`) |
|--------|---------------------------|-------------------------------|
| Meeting type | Client discovery calls, internal debriefs | Internal team standups, team-to-counterpart syncs |
| Processing passes | Topic map with user-approved deep dives | Standard passes: people, action items, blockers, decisions, technical, summary |
| Living documents | Only org_chart.md | tracking/action_items.md, tracking/blockers.md, tracking/decisions.md |
| Cross-reference | N/A (it IS the parent) | cross_reference.md maps to parent sets |
| Numbering | Main chain (01, 02, 03...) | Independent chain (01, 02, 03...) |

## Source File Note

The `source/` folder is empty in this worked example. The original transcript contained internal BayOne team discussions with candid assessments that should not be preserved in a skill reference. The research files capture the processed output, which is what matters for understanding the pattern.
