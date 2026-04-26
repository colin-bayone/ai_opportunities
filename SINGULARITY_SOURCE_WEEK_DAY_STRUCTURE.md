# Singularity Skill Update Proposal: Week/Day Source Folder Structure

**Drafted:** 2026-04-24
**Status:** Proposal, awaiting review
**Scope:** Applies to BOTH main engagement source folder AND team sub-singularity source folder

---

## 1. Summary of Change

Adopt a `week_YYYY-MM-DD/day_YYYY-MM-DD/` hierarchy for all source files going forward, replacing the flat-file pattern currently documented in the skill for the main engagement `source/` folder.

This matches the structure already organically established in the team sub-singularity and formalizes it as the standard across all Singularity engagements.

---

## 2. Current vs. Proposed

### Current (as documented in `.claude/skills/singularity/references/folder_structure.md`)

```
/<client>/<opportunity>/source/
├── call_prep_2026-03-12.txt
├── discovery_call_transcript_2026-03-12.txt
├── internal_debrief_2026-03-12.txt
└── ...
```

Flat files, dated in the filename.

### Proposed

```
/<client>/<opportunity>/source/
├── week_2026-03-09/
│   └── day_2026-03-12/
│       ├── call_prep_2026-03-12.txt
│       ├── discovery_call_transcript_2026-03-12.txt
│       └── internal_debrief_2026-03-12.txt
└── week_2026-04-13/
    └── day_2026-04-17/
        └── srinivas-and-team_4-17-2026.txt
```

Date-based nesting: `week_<Monday_of_week>/day_<source_date>/<filename>`.

---

## 3. Convention Rules

1. **`week_` folder naming:** ISO-week anchored. The folder is named `week_<YYYY-MM-DD>` where the date is the **Monday** of the calendar week. All source dates Monday–Sunday for that week live inside.

2. **`day_` folder naming:** `day_<YYYY-MM-DD>` where the date is the actual source date of the material (meeting date, email send date, etc.).

3. **Person subfolders (optional):** Within a `day_` folder, per-contributor materials (their emails, files they produced, their chat excerpts) can nest further under `day_.../person_name/`. This matches the existing team sub-singularity pattern at `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/`.

4. **1:1 meetings and group meetings at day root:** Full meeting transcripts (whether 1:1 or group) go directly in the `day_` folder, not in person subfolders. Only individual-contributor artifacts get person subfolders.

5. **Filename convention unchanged:** Source files still carry the source date in the filename (e.g., `colin-srikar-1on1_2026-04-21_01.txt`). Redundant with the folder path, but preserved for search/grep-ability and for files that may be referenced outside the folder structure.

6. **Main vs. team placement rule unchanged:**
   - **Main** (`/<client>/<opportunity>/source/`) = client-facing meetings and high-level internal meetings (shareable)
   - **Team sub-singularity** (`/<client>/<opportunity>/team/source/`) = 1:1s, internal debriefs, private team operations

---

## 4. Why

1. **Consistency across main and team folders.** The team sub-singularity already uses this structure. Divergence in the main folder forces readers to learn two conventions.
2. **Scale.** Engagements spanning many months produce dozens of source files. Flat lists become unreadable; date-nested folders make chronology immediately visible.
3. **Chronological navigation.** A file browser sorted alphabetically lines up correctly by date (week, then day) without any manual sort order.
4. **Batch operations.** Week-scoped or day-scoped operations (bulk moves, per-week cleanup, per-week research snapshots) become one-liner shell globs.

---

## 5. Files to Update in the Skill

### 5.1 `.claude/skills/singularity/references/folder_structure.md`
Replace the current `source/` example tree with the proposed `week_/day_/` version. Add the convention rules from Section 3 above.

### 5.2 `.claude/skills/singularity/references/document_processing.md`
Update any example paths that point to `source/<filename>` to use `source/week_<date>/day_<date>/<filename>`.

### 5.3 `.claude/skills/singularity/SKILL.md`
In "FLOW 1: NEW ENGAGEMENT" and "FLOW 3: PROCESS SOURCE MATERIAL", update source-file path examples to the new structure.

### 5.4 `.claude/skills/singularity/references/complete_structure.md`
Refresh the canonical engagement-folder tree diagram.

### 5.5 Agent prompt templates (in SKILL.md / `agent_architecture.md`)
The deep-dive agent prompt references `/<client>/<opportunity>/source/<transcript_filename>` as the read path. Update to reflect that source files now sit inside `week_/day_/` subfolders; the full path must be provided to each agent.

### 5.6 `.claude/skills/singularity/scripts/singularity_stop.py`
The script looks for `research/00_methodology_*.md` and `source/*` files to validate engagement artifacts. Confirm its globbing is recursive or update it to traverse `source/**` instead of `source/*`.

---

## 6. Migration Strategy

- **New source files from this point forward** follow the new convention immediately.
- **Existing source files in the main folder** stay where they are. Do not retrospectively reorganize existing engagements.
- A future pass may reorganize historical files, but that work is out of scope for this proposal (separate session).
- The team sub-singularity for `cisco/cicd/` is already effectively compliant and requires no migration.

---

## 7. Example Path Transitions

| Old path | New path |
|----------|----------|
| `cisco/cicd/source/srinivas-and-team_4-17-2026.txt` | `cisco/cicd/source/week_2026-04-13/day_2026-04-17/srinivas-and-team_4-17-2026.txt` |
| `lam_research/ip_protection/source/lam_meeting_3122026.txt` | `lam_research/ip_protection/source/week_2026-03-09/day_2026-03-12/lam_meeting_3122026.txt` |
| `sephora/edw/source/discovery_call_prep_2026-02-10.txt` | `sephora/edw/source/week_2026-02-09/day_2026-02-10/discovery_call_prep_2026-02-10.txt` |

---

## 8. Open Questions for Colin

1. **Week anchor day:** Monday (ISO-week) proposed. Confirm, or prefer a different anchor (e.g., Sunday-start)?
2. **Retroactive fix scope:** Leave existing engagements untouched per migration section, or should a future session standardize all of them?
3. **Nested `week_` for long ranges:** A source that spans multiple weeks (e.g., a long email thread) — which `week_` folder does it live in? Proposal: the week of the first message in the thread, unchanged once assigned.
4. **The existing team sub-singularity uses `week_2026-04-14` (Tuesday-anchored) alongside `week_2026-04-20` (Monday-anchored).** After this update lands, should the earlier folder be renamed to `week_2026-04-13` for consistency? If yes, that is a one-line `mv` that also requires updating any research docs that reference the old path.

---

## 9. Sign-off Checklist (before applying to the skill)

- [ ] Colin confirms the proposal
- [ ] Week anchor day confirmed (Monday default)
- [ ] Q4 answered re: existing `week_2026-04-14` inconsistency
- [ ] Skill files updated (list in Section 5)
- [ ] `singularity_stop.py` verified to still work with nested source paths
- [ ] Example engagement (next new client opportunity) uses the new structure end-to-end as a real-world validation
