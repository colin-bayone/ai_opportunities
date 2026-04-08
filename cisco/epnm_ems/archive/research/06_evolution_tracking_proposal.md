# Document Evolution Tracking System Proposal

**Generated:** 2026-03-13

---

## The Problem

Documents in this repository follow a "blockchain" pattern - each point in time adds information, and earlier documents may be superseded by later ones. However, there's currently no systematic way to:

1. Know which session documents have been migrated to project docs
2. Track when "current state" was last verified
3. Identify which historical documents are still accurate vs. superseded
4. Understand the evolution of a topic across multiple sessions

---

## Proposed Solution: Three-Tier with Migration Tracking

### Tier Structure (Already Exists)

```
session folders    →    project/    →    history/
(working scratch)       (current)        (immutable log)
```

### What's Missing: Migration Tracking

Add a `_meta.md` file to each session folder that tracks:
- What was migrated to project docs
- What remains session-only (and why)
- Links to related history entries

---

## Proposed Session Folder Structure

```
claude/<date>_<topic>/
├── _meta.md                  # NEW: Migration and status tracking
├── planning/
├── research/
├── source/
└── ...
```

### _meta.md Template

```markdown
# Session: <topic>
**Date:** <session date>
**Status:** ACTIVE | ARCHIVED | MIGRATED

## Migration Status

### Migrated to Project
- [ ] Problem statement → project/<doc>.md
- [ ] Timeline/approach → project/<doc>.md
- [ ] ...

### Migrated to History
- [ ] Discovery findings → history/NNNN_<date>_<summary>.md

### Remains Session-Only (Intentionally)
- Working drafts (superseded by final versions)
- Intermediate feedback (captured in final deliverable)
- Failure analysis (internal learning only)

### Not Yet Migrated (TODO)
- Current deliverable: planning/05_poc_proposal_v5.md
- Technical context: research/*.md references

## Related Documents
- History: history/0002_2026-02-20_ui-conversion-discovery.md
- Project: project/ui-conversion-status.md
- Prior sessions: claude/2026-02-17_cisco-meeting-summaries/
```

---

## Point-in-Time Awareness

### For Session Documents

Add header to significant session documents:

```markdown
**Created:** 2026-02-21
**Last Verified:** 2026-02-23
**Superseded By:** None (or link to newer version)
```

### For Project Documents

Add "currency" section:

```markdown
## Document Currency
**Last Updated:** 2026-03-13
**Based On:** claude/2026-02-20_ui-conversion-discovery/
**Next Review:** When laptop arrives or timeline changes
```

### For History Documents

No changes needed - already immutable by convention.

---

## Supersession Tracking

When new information invalidates old:

1. **Don't edit old documents** (already in CLAUDE.md)
2. **Create new document** with reference to what it supersedes
3. **Update _meta.md** in session folder to note supersession
4. **Update project doc** to point to latest

Example supersession note:
```markdown
**Note:** This document supersedes planning/05_poc_proposal_v3.md based on
Colin's Feb 22 feedback. See planning/11_v3_revision_feedback.md for changes.
```

---

## Session Archive Checklist

When a session is complete, update _meta.md with:

```markdown
## Archive Checklist
- [ ] Final deliverable identified and versioned
- [ ] Key decisions migrated to history
- [ ] Current state updated in project docs
- [ ] Open items captured for next session
- [ ] Session marked as ARCHIVED
```

---

## For This Session (2026-02-20_ui-conversion-discovery)

### Immediate Migration Needed

| Source | Target | Content |
|--------|--------|---------|
| `planning/05_poc_proposal_v5.md` | `project/ui-conversion-status.md` | Current POC status |
| `planning/01_meeting_breakdown.md` | `history/0002_...` | Feb 20 discovery findings |
| `research/04_themes_and_decisions.md` | Project doc | Key decisions |

### Already Captured in This Research

| File | Purpose |
|------|---------|
| `research/00_folder_inventory.md` | What exists in this session |
| `research/03_chronological_timeline.md` | How documents evolved |
| `research/04_themes_and_decisions.md` | What was decided |
| `research/05_documentation_gaps.md` | What's missing from project/ |
| `research/06_evolution_tracking_proposal.md` | This proposal |

---

## Implementation Approach

### Phase 1: Immediate (This Session)
1. Create `_meta.md` for this session folder
2. Create missing project doc for UI conversion
3. Create missing history entry

### Phase 2: Retroactive
4. Add `_meta.md` to other active session folders
5. Review project docs for currency

### Phase 3: Process
6. Add migration checklist to session handoffs
7. Consider automated "stale document" warnings
