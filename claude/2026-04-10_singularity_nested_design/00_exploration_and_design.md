# Singularity Nested Design: Team Meeting Processing and Sub-Singularities

**Session Date:** 2026-04-10
**Context:** Designing the team meeting processing capability for the singularity skill, which surfaced a broader architectural concept: nested singularities (sub-singularities within a parent singularity).

---

## Part 1: Exploration Findings

### What Exists Today

The Cisco CI/CD engagement (`cisco/cicd/`) has a fully operational singularity structure with 10 document sets. Three of those sets (08, 09, 10) are internal team meetings that were processed through the main research chain alongside client discovery materials.

**Source files currently in `cisco/cicd/source/` that are team meetings:**

| File | Date | Type |
|------|------|------|
| `internal_team_meeting_2026-03-18.txt` | 2026-03-18 | Internal standup (Colin, Saurav, Askari) |
| `internal_team_meeting_2026-03-30.txt` | 2026-03-30 | Internal standup (Colin, Saurav, Askari, Srikar) |
| `internal_discovery_brainstorming_2026-03-31.txt` | 2026-03-31 | Internal working session |
| `srini_team_meet_04-02-2026.txt` | 2026-04-02 | Team meeting with Cisco (Srinivas, Anupma, Justin, Colin) |

**Additional source files that are team-to-Cisco meetings (without Colin):**

| File | Date | Type |
|------|------|------|
| `meeting_guhan_selva_2026-02-09.txt` | 2026-02-09 | BayOne team met with Guhan/Selva |
| `meeting_discovery_rama_2026-02-17.txt` | 2026-02-17 | Discovery meeting |
| `meeting_discovery_anand_srini_divakar_2026-02-17.txt` | 2026-02-17 | Discovery meeting |

### Problems with the Current Approach

1. **Mixed concerns in the main chain.** Sets 01-07 build the engagement narrative (client problem, discovery, positioning). Sets 08-09 are internal standups about team readiness. Set 10 is a hybrid (team meeting with Cisco where real work was assigned). The main chain now has two different kinds of content interleaved.

2. **Wrong processing focus.** The main singularity pipeline optimizes for: technical deep dives, business opportunity, people assessment, speaker dynamics. Team meetings need: action items and assignments, blocker tracking, progress against prior items, decisions made, team readiness.

3. **Scale problem.** As the engagement progresses, team meetings will outnumber client meetings 3:1 or more (2-3 standups/week vs. 1 client meeting/week). If all go into the main chain, the research library becomes cluttered. Someone looking for the Anupma database access discussion has to wade through standup notes.

4. **No operational tracking.** The blockchain methodology is great for the record of understanding, but team operations need living documents: "where do all action items stand right now?" The main chain has no mechanism for that.

---

## Part 2: The Sub-Singularity Pattern

### Core Concept

A **sub-singularity** is a self-contained singularity instance nested within a parent singularity. It has its own source, research, and numbering chain. It follows the same blockchain methodology as the parent, but with a processing focus tailored to its purpose.

Sub-singularities are connected to the parent through a **cross-reference file** that maps sub-singularity sets to parent sets when content overlaps or converges.

### Why This Matters Beyond Team Meetings

The sub-singularity pattern is general-purpose. Any time an engagement has a distinct track of activity that:

- Has its own source materials (transcripts, emails, documents)
- Follows its own timeline
- Is supplementary to the main engagement narrative rather than part of it
- Could overwhelm the main chain if mixed in

...it is a candidate for a sub-singularity.

**Examples beyond team meetings:**

- A parallel workstream within the same engagement (e.g., infrastructure track vs. application track)
- Vendor evaluation research (separate meetings with multiple vendors)
- Training or onboarding materials processing
- A sub-team's independent discovery meetings with client counterparts
- Compliance or legal review track

### The Pattern

Every sub-singularity follows this template:

```
<sub_singularity_name>/
├── source/                         (raw input files, never modified)
├── research/                       (blockchain chain, own numbering, append-only)
│   ├── 00_methodology_<date>.md
│   ├── 01_*
│   └── ...
├── tracking/                       (living operational documents, always created)
├── documents/                      (formatted outputs: HTML, reports, etc.)
├── planning/                       (session handoffs, notes)
└── cross_reference.md              (maps to parent and sibling sub-singularities)
```

**Rules:**

1. Each sub-singularity has its own independent numbering chain (01, 02, 03...).
2. The blockchain methodology applies within each sub-singularity: research docs are append-only, numbered chronologically, never edited after creation.
3. The `cross_reference.md` file is a living document that maps sub-singularity sets to parent sets and other sub-singularity sets when there is convergence.
4. The parent singularity's `org_chart.md` remains the single source of truth for people. Sub-singularities reference it but do not maintain their own.
5. Sub-singularities can have a `tracking/` folder for living operational documents when the track is operational in nature (like team meetings). Research-oriented sub-singularities may not need it.
6. The `documents/` folder holds formatted outputs (HTML reports, status documents, etc.) produced from the sub-singularity's research.

### Cross-Reference File Format

The cross-reference file is the connective tissue. It serves as a lookup: "this team meeting relates to these items in the main chain."

```markdown
# Cross Reference: Team Meetings <> Main Chain

## By Team Meeting Set

| Team Set | Date | Main Chain Sets | Notes |
|----------|------|-----------------|-------|
| 01 | 2026-03-18 | 08 (same meeting processed in main chain) | First internal standup |
| 02 | 2026-03-30 | 09 (same meeting processed in main chain) | Full team briefing |
| 03 | 2026-04-02 | 10 (same meeting processed in main chain) | First Srinivas team sync |

## By Topic Thread

| Thread | Team Sets | Main Sets | Status |
|--------|-----------|-----------|--------|
| GitHub MFA blocker | 02, 03 | 09, 10 | Unresolved as of 04-02 |
| WebEx scraper task | 03 | 10 | Assigned, not started |
| Build log analysis | 03 | 10 | Assigned, pending Justin meeting |
```

---

## Part 3: Team Sub-Singularity Design (The First Instance)

### Folder Structure

```
cisco/cicd/
├── [existing master singularity structure unchanged]
│
└── team/                                    (sub-singularity: team operations)
    ├── source/                              (raw team meeting transcripts)
    │   ├── internal_standup_2026-03-18.txt
    │   ├── internal_standup_2026-03-30.txt
    │   ├── cisco_sync_srinivas_2026-04-02.txt
    │   └── ...
    │
    ├── research/                            (blockchain chain, own numbering)
    │   ├── 00_methodology_2026-04-10.md
    │   ├── 01_standup_people_2026-03-18.md
    │   ├── 01_standup_action_items_2026-03-18.md
    │   ├── 01_standup_blockers_2026-03-18.md
    │   ├── 01_standup_summary_2026-03-18.md
    │   ├── 01-02_changes_2026-03-30.md
    │   ├── 02_standup_people_2026-03-30.md
    │   ├── 02_standup_action_items_2026-03-30.md
    │   ├── ...
    │   └── ...
    │
    ├── tracking/                            (living operational documents)
    │   ├── action_items.md                  (cumulative, updated after each meeting)
    │   ├── blockers.md                      (cumulative, items removed when resolved)
    │   └── decisions.md                     (cumulative log of decisions and rationale)
    │
    ├── documents/                           (formatted outputs)
    │   ├── team_status_2026-04-10.html
    │   └── ...
    │
    ├── planning/                            (session handoffs, notes)
    │   └── session_handoff_<date>.md
    │
    └── cross_reference.md                   (maps to parent chain)
```

### Processing Methodology for Team Meetings

Team meeting processing follows the same blockchain principles as the parent singularity but with a different set of standard passes optimized for operational content.

#### Standard Passes for Team Meetings

1. **People and dynamics** (same as parent). Who was present, engagement level, team dynamics, any new people. First file for every set.

2. **Action items and assignments.** The core operational pass. For each action item:
   - What is the action?
   - Who is assigned?
   - When is it due (or what is the urgency)?
   - What is the status of prior action items from earlier sets?
   - What was completed since the last meeting?
   - What is carried forward?

3. **Blockers, dependencies, and escalations.** What is preventing progress? What depends on external parties? What needs to be escalated? What changed since the last meeting?

4. **Decisions made and rationale.** What was decided? By whom? What was the reasoning? What alternatives were considered? This is the "why" behind operational choices.

5. **Technical discussion** (only when substantive). If the meeting included genuine technical content (architecture discussion, tool evaluation, design decisions), it gets its own deep-dive pass. Many standups will not have this.

6. **Summary.** Always last. References all files in the set. Includes a "net-new" section for information not captured in prior sets.

#### Key Differences from Parent Singularity Processing

| Aspect | Parent Singularity | Team Sub-Singularity |
|--------|-------------------|---------------------|
| Topic map | Proposed per-meeting, user-approved | Standard passes above, with optional technical deep-dive |
| Agent parallelization | One agent per topic | Same, but standard passes mean fewer custom agents |
| Bridge documents | Focus on what we learned/corrected | Focus on action item progress, blocker changes |
| Post-processing | Update org chart | Update tracking/ files (action_items.md, blockers.md, decisions.md) |
| Living documents | Only org_chart.md | tracking/ folder has multiple living docs |
| Cross-referencing | Self-contained | cross_reference.md maps to parent chain |

#### Tracking Documents (Living, Editable)

These are the operational dashboards. Updated after every team meeting set is processed.

**`tracking/action_items.md`** — Cumulative tracker:

```markdown
# Action Items Tracker

Last updated after: Team Set 03 (2026-04-02)

## Open

| # | Action | Owner | Assigned | Due/Urgency | Source Set | Status |
|---|--------|-------|----------|-------------|------------|--------|
| 5 | Build WebEx chat scraper | Colin/Team | Team 03 | ASAP | Team 03, Main 10 | Not started |
| 6 | Meet with Justin on build logs | Colin | Team 03 | Next week | Team 03, Main 10 | Not started |
| 7 | Share team profiles with Srinivas | Colin | Team 03 | This week | Team 03 | Not started |

## Completed

| # | Action | Owner | Completed | Source Set | Resolved Set |
|---|--------|-------|-----------|------------|-------------|
| 1 | Ship BayOne laptop to Askari | BayOne ops | 2026-03-18 | Team 01 | Team 02 |

## Blocked

| # | Action | Owner | Blocker | Source Set |
|---|--------|-------|---------|------------|
| 3 | Access GitHub Enterprise repos | All | MFA/Duo loop (IT ticket open) | Team 02 |
```

**`tracking/blockers.md`** — Current blockers with status:

```markdown
# Blockers

Last updated after: Team Set 03 (2026-04-02)

## Active

| Blocker | Impact | Owner | Escalation | First Seen | Current Status |
|---------|--------|-------|------------|------------|---------------|
| GitHub MFA/Duo infinite loop | Cannot access repos, gating all dev work | IT ticket | Srinivas aware | Team 02 | Open, IT case filed |
| Anupma database access | Cannot build MCPs for DevEx data | Srinivas/Anupma | Offline discussion | Team 03 | Pending offline chat |

## Resolved

| Blocker | Resolution | Resolved Date |
|---------|-----------|---------------|
| Askari laptop | Shipped, received | 2026-03-18 |
```

**`tracking/decisions.md`** — Decisions with rationale:

```markdown
# Decisions Log

Last updated after: Team Set 03 (2026-04-02)

| # | Decision | Rationale | Decided By | Date | Source Set |
|---|----------|-----------|------------|------|------------|
| 1 | Use existing Airflow instance, not standalone | Avoid parallel infrastructure to monitor | Srinivas | 2026-04-02 | Team 03 |
| 2 | Start with WebEx scraper as first task | Gives user pain point baseline, low barrier | Srinivas | 2026-04-02 | Team 03 |
| 3 | Twice-weekly team syncs with Srinivas | Cadence for progress | Srinivas | 2026-04-02 | Team 03 |
```

---

## Part 4: Scalable Architecture for Nested Singularities

### How Sub-Singularities Relate to the Parent

```
cisco/cicd/                              (PARENT SINGULARITY)
├── org_chart.md                         (master people reference)
├── source/
├── research/                            (main chain: 01, 02, 03...)
├── planning/
├── pricing/
├── deliverables/
├── presentations/
├── decisions/
├── progress/
│
├── team/                                (SUB-SINGULARITY: team operations)
│   ├── source/
│   ├── research/                        (own chain: 01, 02, 03...)
│   ├── tracking/
│   ├── documents/
│   ├── planning/
│   └── cross_reference.md
│
├── team_cisco_syncs/                    (SUB-SINGULARITY: team-Cisco meetings w/o Colin)
│   ├── source/
│   ├── research/                        (own chain: 01, 02, 03...)
│   ├── documents/
│   ├── planning/
│   └── cross_reference.md
│
└── <future_track>/                      (SUB-SINGULARITY: any future parallel track)
    ├── source/
    ├── research/
    ├── documents/
    ├── planning/
    └── cross_reference.md
```

### Rules for the Nested Pattern

1. **The parent singularity is the master.** It holds the org chart, the primary engagement narrative, client-facing deliverables, pricing, and presentations. Sub-singularities are supplementary tracks.

2. **Sub-singularities are peers, not nested further.** One level of nesting only. A sub-singularity does not contain sub-sub-singularities. If a track needs that level of complexity, it probably deserves to be its own engagement.

3. **Each sub-singularity is self-contained for processing.** A new session can pick up a sub-singularity by reading its own 00_methodology and summaries without reading the parent. The cross-reference file tells you where to look if you need parent context.

4. **Convergence flows upward.** When a sub-singularity produces findings that matter to the parent chain (e.g., a team-Cisco sync reveals a new technical constraint), that information enters the parent chain as a new set or supplementary set. The sub-singularity does not edit parent research. The cross-reference file documents the connection.

5. **The parent's org chart is the single people reference.** Sub-singularities may have people docs per-set, but the parent org chart is always updated when new people appear in any sub-singularity.

6. **Sub-singularity naming is descriptive and flat.** Names like `team/`, `team_cisco_syncs/`, `vendor_eval/`. No nested folder hierarchies beyond the sub-singularity template.

7. **The `tracking/` folder is always created.** Even if a sub-singularity does not immediately need living operational documents, the folder exists from the start. Tracks that seem purely research-oriented at creation time often develop operational needs as they mature. Having the folder ready eliminates the decision of "do I need this yet?" and keeps the structure consistent across all sub-singularities.

8. **The `documents/` folder is standard.** Every sub-singularity can produce formatted outputs. HTML reports, status summaries, etc.

### How to Add a New Sub-Singularity

When a new parallel track is identified during an engagement:

1. Propose the sub-singularity name, purpose, and expected content to the user.
2. Create the folder structure using the template.
3. Write `research/00_methodology_<date>.md` describing this track's purpose and processing focus.
4. Create `cross_reference.md` with an initial mapping to any existing parent or sibling sets that relate.
5. Begin processing source materials using the track-specific methodology.

---

## Part 5: Emerging Ideas (To Track, Not Act On Yet)

### Master Aggregation

If a singularity has multiple sub-singularities, there could be a mechanism to aggregate across all of them: "show me all open action items across team standups AND cisco syncs." This would be a roll-up view that reads all tracking/ folders. Not needed now, but worth considering as the pattern matures.

### Sub-Singularity Templates

Different types of sub-singularities might warrant different methodology templates:

- **Operational** (team meetings): Action items, blockers, decisions, progress tracking
- **Discovery** (parallel discovery tracks): Technical deep dives, information needs, hypothesis tracking
- **Research** (vendor eval, technology investigation): Findings, comparisons, recommendations
- **Compliance/Legal** (review tracks): Requirements, gaps, risk assessment

### Automatic Cross-Referencing

The cross-reference file is manually maintained today. In the future, it could be automatically populated during processing by detecting topic overlap with the parent chain (e.g., "this team meeting discussed the GitHub MFA blocker, which was first identified in parent Set 10").

---

## Part 6: Immediate Next Steps

1. **Update the singularity skill** to support the sub-singularity pattern and team meeting processing methodology.
2. **Create `cisco/cicd/team/`** with the full structure.
3. **Write the team methodology doc** (`team/research/00_methodology_2026-04-10.md`).
4. **Process existing team meeting transcripts** through the team sub-singularity pipeline. Note: Sets 08, 09, 10 in the main chain stay where they are (blockchain rule). Future team meetings go into `team/`.
5. **Test with the Cisco sync transcripts** Colin mentioned having from team members.
6. **Integrate into SKILL.md** as a new flow or extension of existing flows.
