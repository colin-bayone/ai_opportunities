# Tracking Folder Pattern

## The Dual Model

Sub-singularities use two complementary persistence mechanisms:

1. **Research chain (blockchain, immutable).** Per-meeting documents capture what was said, decided, and discovered at a specific point in time. These are never edited. They are the audit trail.

2. **Tracking folder (living, editable).** Cumulative operational documents that show the current state across all meetings. Updated after every set is processed. These are the operational dashboard.

Both exist and serve different purposes. The research chain answers "what happened at meeting 3?" The tracking folder answers "where do all our action items stand right now?"

## When the Tracking Folder Is Used

The `tracking/` folder is always created in every sub-singularity (see `nested_singularity.md`, rule 3). Its files are populated and updated after each set is processed. Even if initially empty, the folder is ready for when operational content emerges.

## Standard Tracking Files

### `tracking/action_items.md`

Cumulative tracker of all action items across all meetings.

**Three sections:**

| Section | Purpose | Mutability |
|---------|---------|------------|
| Open | Items that are assigned and in progress | Living: items move to Completed or Blocked as status changes |
| Completed | Items that have been finished | Append-only: items arrive here from Open when completed |
| Blocked | Items that cannot proceed due to a dependency | Living: items move back to Open when unblocked, or to Completed if resolved differently |

**Required columns:**

| Column | Description |
|--------|-------------|
| # | Sequential number, never reused |
| Action | What needs to be done |
| Owner | Who is responsible |
| Assigned | When and where it was assigned (set reference) |
| Due/Urgency | Deadline or urgency level |
| Source | Which team set created this item (e.g., "Team 01") |
| Status | Current status text |

**Template:**

```markdown
# Action Items Tracker

Last updated after: Team Set <NN> (<date>)

## Open

| # | Action | Owner | Assigned | Due/Urgency | Source | Status |
|---|--------|-------|----------|-------------|--------|--------|

## Completed

| # | Action | Owner | Completed | Source |
|---|--------|-------|-----------|--------|

## Blocked

| # | Action | Owner | Blocker | Source |
|---|--------|-------|---------|--------|
```

### `tracking/blockers.md`

Cumulative tracker of all blockers across all meetings.

**Two sections:**

| Section | Purpose | Mutability |
|---------|---------|------------|
| Active | Blockers currently preventing progress | Living: items move to Resolved when fixed |
| Resolved | Blockers that have been cleared | Append-only: items arrive here from Active when resolved |

**Required columns for Active:**

| Column | Description |
|--------|-------------|
| Blocker | Description of what is blocking |
| Impact | What work is affected |
| Owner | Who is responsible for resolving |
| Escalation | Who to escalate to if needed |
| First Seen | Which team set first identified this (e.g., "Team 01") |
| Current Status | Latest status text |

**Required columns for Resolved:**

| Column | Description |
|--------|-------------|
| Blocker | Description |
| Resolution | How it was resolved |
| Resolved Date | When |

**Template:**

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

Cumulative numbered log of all decisions made across all meetings.

**Single table, append-only.** Decisions are never removed or edited. If a decision is reversed, a new row is added referencing the original decision number.

**Required columns:**

| Column | Description |
|--------|-------------|
| # | Sequential number, never reused |
| Decision | What was decided |
| Rationale | Why (the reasoning, not just the conclusion) |
| Decided By | Who made the decision (individual or "team consensus") |
| Date | When |
| Source | Which team set (e.g., "Team 01") |

**Template:**

```markdown
# Decisions Log

Last updated after: Team Set <NN> (<date>)

| # | Decision | Rationale | Decided By | Date | Source |
|---|----------|-----------|------------|------|--------|
```

## Update Rules

1. **Update after every set.** After processing a team meeting set (all research files written + summary complete), update all three tracking files.

2. **Always update the "Last updated after" header** with the set number and date.

3. **Move items between sections, do not delete.** When an action item is completed, move it from Open to Completed. When a blocker is resolved, move it from Active to Resolved. Never delete rows.

4. **Source references are critical.** Every entry must reference the team set where it originated or was last updated. This enables tracing back to the immutable research chain for the full context.

5. **Decisions are append-only.** Even if a decision is reversed, add a new row: "Reversed Decision #3 because..." Do not edit the original row.

6. **The research chain is the audit trail.** If someone questions "when was this action item assigned?" or "what was the exact discussion that led to this decision?", the answer is in the research chain at the referenced set number. The tracking files are the dashboard; the research files are the evidence.

## Worked Example

See `worked_examples/cisco_team/tracking/` for populated examples of all three files from the Cisco CI/CD team sub-singularity.
