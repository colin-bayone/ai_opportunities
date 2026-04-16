# Health Check Methodology

**Purpose:** Defines what the audit flow checks when evaluating an existing Singularity engagement for conformance. The skill spec is the sole source of truth — every check in this document traces to a specific rule or convention documented in the skill's reference files.

---

## Mandatory Pre-Audit Reading

Before performing ANY health check, the auditor MUST read these files in order. No exceptions. Do not assess an engagement based on assumptions about what it should look like.

1. `.claude/skills/singularity/SKILL.md` — structural rules, flows, hard rules
2. `.claude/skills/singularity/references/folder_structure.md` — canonical folder structure, naming conventions, week/day source organization
3. `.claude/skills/singularity/references/blockchain_methodology.md` — append-only rules, numbering, bridge documents
4. `.claude/skills/singularity/references/nested_singularity.md` — sub-singularity pattern (if sub-singularities exist)
5. `.claude/skills/singularity/references/people_tracking.md` — dual system (per-set people docs + living org chart)
6. `.claude/skills/singularity/references/document_processing.md` — processing order, standard files per set

Only after reading these can the audit proceed. If any of these files have been updated since the last audit, the auditor must re-read them — do not rely on prior knowledge.

---

## Audit Checklist

### 1. Folder Structure

**Source of truth:** `references/folder_structure.md`

- [ ] Engagement root exists at `/<client_name>/<opportunity_name>/`
- [ ] All canonical folders exist: `source/`, `research/`, `planning/`, `pricing/`, `deliverables/`, `presentations/`, `decisions/`, `progress/`
- [ ] No unexpected top-level folders (folders not in the canonical structure should be flagged, not automatically treated as errors — they may be sub-singularities or legitimate additions)
- [ ] `org_chart.md` exists at the engagement root (if research has progressed beyond methodology)

### 2. Source Organization

**Source of truth:** `references/folder_structure.md` (source section)

- [ ] Source files are organized in `week_YYYY-MM-DD/day_YYYY-MM-DD/` structure
- [ ] Week folders use Monday dates
- [ ] `source/README.md` exists explaining the week/day structure
- [ ] For sub-singularities: person subfolders exist within day folders
- [ ] No loose files directly in `source/` (outside of README.md and week folders)

### 3. Research Chain Integrity

**Source of truth:** `references/blockchain_methodology.md`, `references/folder_structure.md` (naming conventions)

- [ ] `research/00_methodology_<date>.md` exists
- [ ] Files are numbered sequentially (01, 02, 02a, 03, etc.) with no gaps in the main sequence
- [ ] Each set has a summary file (`<set>_*_summary_<date>.md`)
- [ ] Bridge documents exist between sequential sets (`01-02_changes_<date>.md`)
- [ ] File naming follows convention: `<set>_<descriptive_name>_<date>.md`
- [ ] Dates in filenames use ISO format (YYYY-MM-DD)
- [ ] No evidence of edited research files (this is harder to check — look for modification dates significantly after creation dates)

### 4. Document Headers

**Source of truth:** `SKILL.md` (Document Header Format section)

- [ ] Research documents start with the standard header (Set Number, Source, Source Date, Document Set, Pass)
- [ ] Headers reference the correct source file path
- [ ] Set numbers in headers match filename prefixes

### 5. People Tracking

**Source of truth:** `references/people_tracking.md`

- [ ] `org_chart.md` exists at engagement root
- [ ] Each transcript-based set has a people file (`<set>_*_people_<date>.md`)
- [ ] Org chart appears to be current (contains people from the latest set, not just early sets)

### 6. Sub-Singularities (if present)

**Source of truth:** `references/nested_singularity.md`

- [ ] Sub-singularity folders live at engagement root level (siblings of `source/`, `research/`, etc.)
- [ ] Each sub-singularity has: `source/`, `research/`, `tracking/`, `documents/`, `planning/`
- [ ] `tracking/` contains `action_items.md`, `blockers.md`, `decisions.md`
- [ ] `cross_reference.md` exists at sub-singularity root
- [ ] Independent numbering chain in `research/` (starts at 01, not continuing parent's numbers)
- [ ] Own `research/00_methodology_<date>.md`
- [ ] Source files use week/day/person structure

### 7. Deliverables and Presentations

**Source of truth:** `references/deliverables_pipeline.md`, `references/folder_structure.md`

- [ ] Deliverables are in `deliverables/` as flat, dated files
- [ ] HTML deliverables have corresponding markdown versions where applicable
- [ ] Presentations are in `presentations/` organized by deck
- [ ] Presentation slides have navigation (prev/next/home) — spot check, not exhaustive
- [ ] Chart files in `charts/` subfolders have back buttons

### 8. Planning and Session Continuity

**Source of truth:** `references/session_continuity.md`

- [ ] `planning/skill_notes.md` exists (if the engagement has accumulated feedback)
- [ ] Session handoff files exist for multi-session engagements
- [ ] Handoff files reference the correct engagement state

---

## Output Format

### Health Check Report (`planning/health_check_<date>.md`)

```markdown
# Health Check: <Client> / <Opportunity>

**Date:** YYYY-MM-DD
**Auditor:** Claude (Singularity skill audit flow)
**Skill version:** Read from SKILL.md on <date>

## Summary

<1-3 sentence overall assessment: conformant, mostly conformant with gaps, or significant issues>

## Conformant

<List everything that IS correct, organized by checklist section>

## Issues Found

<Each issue as its own item with:>
- **What:** Description of the issue
- **Where:** Full file path or folder path
- **Expected:** What the skill spec says should be there
- **Actual:** What was found instead
- **Severity:** Missing (something should exist but doesn't), Non-conformant (exists but wrong), Unexpected (exists but shouldn't per spec — flag for user review, may be intentional)

## Recommendations

<Prioritized list of what to fix, from most impactful to least>
```

### Remediation Plan (`planning/remediation_plan_<date>.md`)

Only produced if the health check found issues. Lists every proposed action:

```markdown
# Remediation Plan: <Client> / <Opportunity>

**Date:** YYYY-MM-DD
**Based on:** health_check_<date>.md

## Proposed Actions

### Action 1: <description>
- **Type:** Create / Move / Rename / Update reference
- **Details:** <exactly what would change>
- **Impact:** <what this fixes>
- **Requires:** User approval

### Action 2: ...

## Actions Requiring Special Approval

<Any file moves or deletions listed separately with extra context>

## Notes

- No actions will be taken without explicit user approval
- File deletions require explicit permission per action
- File moves require explicit permission per action
```

---

## What This Audit Does NOT Do

- It does not execute any remediation actions
- It does not move, rename, or delete any files
- It does not modify any existing documents
- It does not create folders or files (except the health check and remediation plan themselves in `planning/`)
- It does not make assumptions about what should exist — it checks the skill spec and compares
