# Nested Singularity (Sub-Singularity) Pattern

## What Is a Sub-Singularity

A sub-singularity is a self-contained singularity instance nested within a parent engagement. It has its own source materials, its own numbered research chain, its own tracking documents, and its own methodology. It follows the same blockchain rules as the parent but with a processing focus tailored to its purpose.

Sub-singularities are connected to the parent through a **cross-reference file** that maps sub-singularity sets to parent sets when content overlaps or converges.

## When to Create One

Create a sub-singularity when an engagement has a distinct track of activity that:

- Has its own source materials (transcripts, emails, documents)
- Follows its own timeline separate from the main engagement arc
- Is supplementary to the main engagement narrative rather than part of it
- Could overwhelm the main research chain if mixed in (e.g., 2-3 team standups per week vs. 1 client meeting per month)

**Common use cases:**

| Use Case | Name Convention | Example |
|----------|----------------|---------|
| Internal team standups and syncs | `team/` | `cisco/cicd/team/` |
| Team meetings with client counterparts (without the lead) | `team_cisco_syncs/` | Meetings Srikar/Namita had with Justin/Divakar |
| Parallel workstream within the same engagement | `<workstream_name>/` | Infrastructure track vs. application track |
| Vendor evaluation research | `vendor_eval/` | Evaluating 3 competing platforms |
| Training or onboarding materials processing | `training/` | Processing onboarding docs for new team members |
| Compliance or legal review track | `compliance/` | Separate regulatory review alongside technical work |

## Folder Structure Template

Every sub-singularity follows this structure:

```
/<client_name>/<opportunity_name>/<sub_singularity_name>/
├── source/                         (raw input files, never modified)
│   ├── README.md                   (explains week/day/person structure)
│   └── week_YYYY-MM-DD/           (Monday date)
│       └── day_YYYY-MM-DD/        (upload date, not source date)
│           └── <person>/          (who uploaded — person subfolders for team sub-singularities)
├── research/                       (blockchain chain, own numbering, append-only)
│   ├── 00_methodology_<date>.md    (explains this sub-singularity's purpose and processing approach)
│   ├── 01_*                        (first document set)
│   ├── 01-02_changes_<date>.md     (bridge document, same rules as parent)
│   └── ...
├── tracking/                       (living operational documents, ALWAYS created)
│   ├── action_items.md             (cumulative: open, completed, blocked)
│   ├── blockers.md                 (cumulative: active, resolved)
│   └── decisions.md                (numbered log with rationale)
├── documents/                      (formatted outputs: HTML reports, status docs, etc.)
├── planning/                       (session handoffs, notes)
│   └── session_handoff_<date>.md
└── cross_reference.md              (maps to parent and sibling sub-singularities)
```

## Rules

### Structural Rules

1. **Each sub-singularity has its own independent numbering chain.** Set 01 in the team sub-singularity is unrelated to Set 01 in the parent. No confusion, no collision.

2. **Blockchain methodology applies within each sub-singularity.** Research docs are append-only, numbered chronologically, never edited after creation. The same rules from `blockchain_methodology.md` apply.

3. **The `tracking/` folder is always created.** Even if a sub-singularity does not immediately need living operational documents, the folder exists from the start. Tracks that seem purely research-oriented at creation time often develop operational needs as they mature. Keeping the structure consistent eliminates "do I need this yet?" decisions.

4. **The `documents/` folder is standard.** Every sub-singularity can produce formatted outputs (HTML reports, status summaries, etc.).

5. **The `cross_reference.md` file is living.** It gets updated after every set that has overlap with the parent or a sibling sub-singularity.

### Relationship Rules

6. **Sub-singularities are peers, not nested further.** One level of nesting only. A sub-singularity does not contain sub-sub-singularities. If a track needs that level of complexity, it probably deserves to be its own engagement.

7. **The parent singularity is the master.** It holds the org chart, the primary engagement narrative, client-facing deliverables, pricing, and presentations. Sub-singularities are supplementary tracks.

8. **The parent's `org_chart.md` is the single people reference.** Sub-singularities may have people docs per-set (capturing who was on a specific call), but the parent org chart is always updated when new people appear in any sub-singularity.

9. **Each sub-singularity is self-contained for processing.** A new session can pick up a sub-singularity by reading its own `00_methodology` and summaries without reading the parent. The cross-reference file tells you where to look if parent context is needed.

10. **Convergence flows upward.** When a sub-singularity produces findings that matter to the parent chain (e.g., a team sync reveals a new technical constraint that affects the engagement narrative), that information enters the parent chain as a new set or supplementary set. The sub-singularity does not edit parent research. The cross-reference file documents the connection.

### Naming Rules

11. **Sub-singularity naming is descriptive and flat.** Names like `team/`, `team_cisco_syncs/`, `vendor_eval/`. No nested folder hierarchies beyond the sub-singularity template.

12. **Sub-singularities live at the engagement root level.** They are siblings of `source/`, `research/`, `deliverables/`, etc.

## Cross-Reference File Format

The cross-reference file maps sub-singularity sets to parent sets and sibling sub-singularity sets when content overlaps. Two views: by set number and by topic thread.

```markdown
# Cross Reference: <Sub-Singularity Name> <> Main Chain

## By Set

| Sub Set | Date | Main Chain Sets | Notes |
|---------|------|-----------------|-------|
| 01 | 2026-04-10 | 10 (Srinivas task assignments) | First standup, covers progress on 3 assigned items |
| 02 | 2026-04-17 | (none) | Internal standup, no parent overlap |

## By Topic Thread

| Thread | Sub Sets | Main Sets | Status |
|--------|----------|-----------|--------|
| GitHub MFA blocker | 01, 02 | 09, 10 | Resolved in Sub 02 |
| WebEx scraper scope | 01 | 10 | Open, pending Srinivas decision |

## Historical Notes

(Document any sets that were processed in the parent chain before this sub-singularity existed, for provenance.)
```

## How to Add a New Sub-Singularity

When a new parallel track is identified during an engagement:

1. **Propose the sub-singularity** name, purpose, and expected content to the user.
2. **Get approval.** The user decides whether it warrants its own sub-singularity or should stay in the main chain.
3. **Create the folder structure** using the template above.
4. **Write `research/00_methodology_<date>.md`** describing this track's purpose, what goes here vs. the parent, and the processing approach (standard team passes for team meetings, topic-map approach for discovery tracks, etc.).
5. **Create `cross_reference.md`** with an initial mapping to any existing parent or sibling sets that relate.
6. **Begin processing** source materials using the track-appropriate methodology.

## Worked Example

See `references/worked_examples/cisco_team/` for the complete first instance: the Cisco CI/CD team sub-singularity. It includes a methodology doc, a full Set 01 (people, action items, blockers, technical discussion, summary), three tracking files, and a cross-reference file.

## What About the Parent Org Chart?

When processing a sub-singularity transcript that introduces new people:

1. Write the per-set people file in the sub-singularity's `research/` folder (as always for transcript sets).
2. After the set is complete, update the **parent's** `org_chart.md` with any new people. The parent org chart is the single source of truth.
3. Do NOT create a separate org chart in the sub-singularity. There is only one org chart per engagement.
