# Lam Research Reorganization Map

**Date:** 2026-04-08
**State:** D (Single project with legacy content outside it)
**Methodology:** Singularity Reorganization Guide, Phase 0

---

## Current Structure

```
lam_research/
├── 00_index.md              (outdated)
├── org_chart.md             (older version — ip_protection/ has newer one)
├── context/                 (3 transcripts — likely duplicates of ip_protection/source/)
├── project/                 (29 files — pre-Singularity research, likely in ip_protection/archive/)
├── planning/                (session handoff from March 20)
├── deliverables/            (March 12 deliverables — 8 files)
└── ip_protection/           (Active Singularity project)
    ├── org_chart.md         (current, April 6)
    ├── archive/             (44 files — full backup of pre-Singularity state)
    ├── source/              (13 files)
    ├── research/            (47 files — 5 sets + supplements + bridges)
    ├── planning/            (5 files — no session handoff)
    ├── deliverables/        (2 files)
    ├── presentations/       (11 slides in discovery_2026-04-06/)
    ├── decisions/           (empty)
    ├── progress/            (empty)
    └── pricing/             (empty)
```

---

## ip_protection/ Validation

**Passes (10):** methodology, set mapping, summaries, bridge docs, org chart, headers, chronological order, no orphans, deliverables, presentations

**Issues (2):**
- **No session handoff** in ip_protection/planning/. The only session handoff is at the top level (`lam_research/planning/2026-03-20_session/session_handoff_2026-03-20.md`) and is from March 20 — stale by 2+ weeks.
- **Pricing empty** — may not be applicable yet.

---

## Deliverables vs Presentations Assessment

This is where I want your input. Here's what's where and what I think:

### Currently in ip_protection/deliverables/ (2 files):
| File | Type | Client-facing? | My assessment |
|------|------|----------------|---------------|
| `discovery_followup_2026-04-06.html` | Document — follow-up from discovery session | Yes | Belongs in deliverables ✓ |
| `meeting_summary_internal_2026-04-06.html` | Document — internal meeting summary | No (internal) | **Flag:** Is an internal summary a "deliverable"? Or should it be in planning/? |

### Currently in ip_protection/presentations/ (11 files):
| File | Type | Client-facing? | My assessment |
|------|------|----------------|---------------|
| `s01_title.html` through `s11_next_steps.html` | Individual HTML slides forming a presentation deck | Yes | Belongs in presentations ✓ |

### Currently at top-level lam_research/deliverables/ (8 files):
| File | Type | Client-facing? | My assessment |
|------|------|----------------|---------------|
| `problem_restatement.html` + `.md` | Document — problem restatement | Yes | Should move to ip_protection/deliverables/ |
| `preliminary_approach.html` + `.md` | Document — preliminary approach | Yes | Should move to ip_protection/deliverables/ |
| `information_request.html` + `.md` | Document — information request | Yes | Should move to ip_protection/deliverables/ |
| `followup_email_draft.md` | Email draft | Yes | Should move to ip_protection/deliverables/ |
| `README.md` | Description file | No | Can be archived or dropped |

**My proposed rule for this engagement:**
- **deliverables/** = Documents (multi-page, narrative, sent to client or shared internally as polished artifacts)
- **presentations/** = Slide decks (individual slides meant to be presented/walked through)

---

## Top-Level Content — Proposed Disposition

| Item | What it is | Proposed action | Why |
|------|-----------|----------------|-----|
| `00_index.md` | Outdated index | Rewrite after cleanup | Points to old paths |
| `org_chart.md` | Older people map | Remove (ip_protection/ has the current one) | Duplicate, stale |
| `context/` | 3 transcripts | Verify they exist in ip_protection/source/ or archive/, then archive | Likely duplicates |
| `project/` | 29 pre-Singularity research files | Verify they exist in ip_protection/archive/, then archive | Already backed up |
| `planning/` | Session handoff from March 20 | Move session_handoff to ip_protection/planning/, then archive the rest | Handoff should live in the project |
| `deliverables/` | March 12 deliverables (6 client docs + email + README) | Move the 7 substantive files to ip_protection/deliverables/ with dates, then archive | These are real deliverables that belong in the project |

---

## Proposed End State

```
lam_research/
├── 00_index.md              (rewritten — points to ip_protection/)
├── ip_protection/           (validated, consolidated Singularity project)
│   ├── org_chart.md
│   ├── source/              (13 files, unchanged)
│   ├── research/            (47 files, unchanged)
│   ├── planning/            (6+ files — session handoff moved in)
│   ├── deliverables/        (9+ files — March 12 docs moved in with dates)
│   ├── presentations/       (11 slides, unchanged)
│   ├── decisions/           (empty)
│   ├── progress/            (empty)
│   ├── pricing/             (empty)
│   └── archive/             (existing 44 files, unchanged)
└── archive/                 (top-level legacy content moved here)
    ├── context/
    ├── project/
    └── org_chart.md
```

---

## Decisions Needed

1. **`meeting_summary_internal_2026-04-06.html`** — Should an internal meeting summary stay in deliverables/ or move to planning/?

2. **March 12 deliverables** — These don't have dates in their filenames. Should I add dates when moving them (e.g., `problem_restatement_2026-03-12.html`)?

3. **Session handoff** — The March 20 handoff is stale. Should I write a new one reflecting the April 6 state, or just move the old one and note that it's outdated?
