# Team Meeting Processing Methodology

## Overview

Team meetings (internal standups, team-to-client syncs, operational check-ins) are processed differently from client discovery meetings. They are operational in nature: focused on action items, blockers, decisions, and progress, not on understanding a client's problem or building toward proposals.

Team meetings are processed within a sub-singularity (see `nested_singularity.md`), not in the main engagement research chain.

## When This Methodology Applies

- Internal team standups or sync meetings
- Meetings between team members and client counterparts that the engagement lead was not on
- Operational check-ins with recurring cadence
- Any meeting where the primary content is "what did we do, what are we blocked on, what comes next"

## When This Methodology Does NOT Apply

- Client discovery calls (use the standard topic-map methodology in `document_processing.md`)
- Strategy discussions between the user and Claude (use Flow 6 Discussion in SKILL.md)
- Working sessions to develop deliverables (those are deliverable creation, Flow 4)

## Standard Processing Passes

Team meeting transcripts default to the following standard passes. A topic-map approach may still be appropriate for some team meetings — use judgment and ask the user if unsure.

### Pass Order

1. **People and dynamics** (first file, always)
   - Who was present, roles, engagement level
   - Team dynamics: who is the strongest contributor, who is quiet, any tension
   - Any new people introduced
   - Filename: `<set>_standup_people_<date>.md`

2. **Action items and assignments**
   - Every action item mentioned (new and carried forward from prior sets)
   - Who is assigned to each
   - Due date or urgency level
   - Status of prior action items from earlier sets (completed, still open, blocked, dropped)
   - What was completed since the last meeting
   - Items to raise with the client or leadership
   - Filename: `<set>_standup_action_items_<date>.md`

3. **Blockers, dependencies, and escalations**
   - What is preventing progress (technical, access, political, organizational)
   - What depends on external parties
   - What needs to be escalated and to whom
   - What changed since the last meeting
   - Access request status (granted, pending, blocked)
   - Political dynamics and coaching on how to present issues diplomatically
   - Filename: `<set>_standup_blockers_<date>.md`

4. **Decisions made and rationale**
   - What was decided during this meeting
   - By whom (or by consensus)
   - What was the reasoning
   - What alternatives were considered and rejected
   - Filename: `<set>_standup_decisions_<date>.md`
   - Note: this file may be omitted if the meeting produced no explicit decisions. In that case, note the absence in the summary.

5. **Technical discussion** (only when substantive technical content exists)
   - Architecture discussions, tool evaluations, design decisions
   - Findings from discovery or investigation work
   - This pass is OPTIONAL. Many standups have no substantive technical content. Do not force a technical discussion file for a meeting that was purely operational.
   - Filename: `<set>_standup_technical_discussion_<date>.md`

6. **Summary** (last file, always)
   - Short overview referencing all files in the set
   - Status of the main workstreams
   - What is genuinely new vs. what was previously known
   - Filename: `<set>_standup_summary_<date>.md`

### Differences From Client Meeting Processing

| Aspect | Client Meetings | Team Meetings |
|--------|----------------|---------------|
| Topic identification | Topic map proposed by Claude, approved by user | Standard passes (above), no topic map needed |
| Per-topic deep dives | User-approved, variable count | Fixed categories, optional technical discussion |
| Agent parallelization | One agent per approved topic | One agent per standard pass (action items, blockers, technical can run in parallel) |
| Bridge documents | Focus on what we learned about the client/problem | Focus on action item progress, blocker changes, decision evolution |
| Post-processing | Update org chart | Update org chart AND tracking/ files |
| Living documents | Only org_chart.md | tracking/action_items.md, tracking/blockers.md, tracking/decisions.md |

## Post-Processing: Tracking Document Updates

After every team meeting set is processed, update the tracking documents in the sub-singularity's `tracking/` folder. These are living documents (editable, not append-only).

### `tracking/action_items.md`

Three sections: Open, Completed, Blocked.

```markdown
# Action Items Tracker

Last updated after: Team Set <NN> (<date>)

## Open

| # | Action | Owner | Assigned | Due/Urgency | Source | Status |
|---|--------|-------|----------|-------------|--------|--------|
| 1 | Description | Person | Set NN | Timeline | Team NN | Current status |

## Completed

| # | Action | Owner | Completed | Source |
|---|--------|-------|-----------|--------|
| 5 | Description | Person | Date | Team NN |

## Blocked

| # | Action | Owner | Blocker | Source |
|---|--------|-------|---------|--------|
| 3 | Description | Person | What is blocking | Team NN |
```

### `tracking/blockers.md`

Two sections: Active, Resolved.

```markdown
# Blockers

Last updated after: Team Set <NN> (<date>)

## Active

| Blocker | Impact | Owner | Escalation | First Seen | Current Status |
|---------|--------|-------|------------|------------|---------------|

## Resolved

| Blocker | Resolution | Resolved Date |
|---------|-----------|---------------|
```

### `tracking/decisions.md`

Single numbered log.

```markdown
# Decisions Log

Last updated after: Team Set <NN> (<date>)

| # | Decision | Rationale | Decided By | Date | Source |
|---|----------|-----------|------------|------|--------|
```

## Cross-Reference Update

After processing each team meeting set, check whether any content overlaps with the parent engagement chain. If it does, update `cross_reference.md` at the sub-singularity root.

Common overlap triggers:
- Team meeting discussed items that were originally assigned in a client meeting (tracked in main chain)
- Team meeting revealed information that changes the engagement narrative
- A blocker in the team meeting is the same blocker tracked in the main chain

## Agent Architecture for Team Meeting Processing

Passes 2-5 (action items, blockers, decisions, technical discussion) can be spawned as parallel agents after the people file is written in the main session:

1. **Main session writes:** Pass 1 (people file) — needs org chart context
2. **Spawn parallel agents:** Passes 2, 3, 4, 5 — each reads the full transcript with one focus
3. **Main session writes:** Pass 6 (summary) — needs all other files to exist first
4. **Main session updates:** tracking/ files and cross_reference.md

Each agent prompt follows the same template as client meeting agents (see `agent_architecture.md`) but with the team-meeting-specific focus described above.

## Worked Example

See `worked_examples/cisco_team/` for the complete first instance: the Cisco CI/CD team sub-singularity Set 01. It includes all six standard files plus the three tracking documents and a cross-reference file.
