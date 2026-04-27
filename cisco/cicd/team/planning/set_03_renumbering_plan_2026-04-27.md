# Set 03 Collision Resolution Plan

**Date:** 2026-04-27
**Engagement:** cisco/cicd/team/ (sub-singularity)
**Trigger:** Canonical summary naming exposed a latent duplicate-set defect.

---

## Diagnosis

The current state is not a "two distinct meetings sharing a number" problem. It is a "the same meeting was processed twice under different source paths" problem.

### Evidence

| File group | Source path declared in header | Source date | Verdict |
|---|---|---|---|
| `03_briefing_*` | `/cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/internal_team_briefing_2026-04-07_formatted.txt` | 2026-04-07 | Distinct event. Pre-Srinivas team briefing. |
| `03_sync_*` | `/claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/cisco-team-sync_4-16-2026.txt.txt` (non-canonical brainstorm-folder path) | 2026-04-16 | First-pass processing of the Wednesday team sync, before the source was placed in the canonical engagement folder. |
| `04_sync_*` | `/cisco/cicd/team/source/2026-04-16/cisco-team-sync_01.txt` (canonical engagement path) | 2026-04-16 | Second-pass processing of the same Wednesday team sync from the canonical source. |

Both Apr 16 file groups document the same meeting. They share topics (architecture framework, blockers and access, Rui Guo / Nexus T, people present). They differ in detail because they are independent passes by different processing runs, not because they are different events.

### Authoritative framing

The `03-04_changes_2026-04-16.md` bridge document explicitly states `Set 03 = briefing (2026-04-07)` and `Set 04 = sync (2026-04-16)`. That framing is structurally consistent with the chronology and with the 04_sync canonical source path. The bridge is correct. The duplication is the leftover.

---

## Proposed Resolution

**Three options, with recommendation.**

### Option A (recommended): Archive the 03_sync_* files

- Move all `03_sync_*` files (10 files: summary plus 9 sub-files) to `cisco/cicd/team/research/_archive/superseded_03_sync_2026-04-27/` with a README explaining why.
- Set 03 cleanly becomes the briefing.
- Set 04 cleanly becomes the Wednesday sync via the 04_sync_* files.
- The `03-04_changes` bridge already matches this framing.

**Pros:** Cleanest outcome. Removes a duplicate processing pass that should not have existed.
**Cons:** If the 03_sync pass captured analysis the 04_sync pass missed, that content is removed from the active chain. Mitigation: keep the archive folder for retrieval; do not delete.

### Option B: Demote 03_sync_* to letter-suffix files under Set 04

- Rename each `03_sync_<topic>_<date>.md` to `04g_sync_<topic>_<date>.md` (or another unused letter, since 04 already has 04d/e/f).
- Delete `03_sync_summary_2026-04-16.md` because Set 04 already has its own canonical summary (`04_summary_2026-04-16.md`).
- Update inbound references.

**Pros:** Preserves the first-pass analysis as supplementary to Set 04.
**Cons:** Adds noise. Set 04 already has substantive sub-files; mixing in a redundant pass complicates the set.

### Option C: Promote 03_sync_* to its own set number (e.g., a new 03b or 04 if briefing moves)

- This effectively re-introduces the renumbering problem.

**Not recommended.**

---

## Reference Updates Required (under Option A)

Inbound references discovered:

1. **`cisco/cicd/team/cross_reference.md`** — the Set 03 row currently describes the sync content. Replace with briefing content. Add a new Set 04 row describing the Wednesday sync.

2. **`cisco/cicd/team/research/06g-07_changes_2026-04-13.md`** — contains a reference to `03_sync`. Update to point to the equivalent Set 04 file (the topic of the reference will determine which 04 file).

3. **`cisco/cicd/team/research/03_sync_colin_directives_2026-04-16.md`** — internal cross-link to `03_briefing`. Will be archived along with the rest of 03_sync; no separate update needed.

4. **`cisco/cicd/team/research/03-04_changes_2026-04-16.md`** — already correctly framed; no change.

---

## Summary Filename Renames Still Pending

After Option A is executed, two summary files remain to rename to canonical format:

- `03_briefing_summary_2026-04-07.md` -> `03_summary_2026-04-07.md`
- `03_sync_summary_2026-04-16.md` -> archived (no rename needed)

---

## Hook Patch (separate, follow-on)

After the collision is resolved, patch `singularity_stop.py` to:

1. Include the canonical filename pattern (`NN_summary_<date>.md`) in the missing-summary error message.
2. Detect set-number collisions by counting summary files per set prefix; flag any set with more than one summary file as a structural error.
3. Reject summary filenames that match `^\d{2}[a-z]?_[a-z]+_summary_` (the type-prefixed anti-pattern) with an explicit "rename to canonical format" instruction.

Patching the hook before resolving the collision would block any subsequent stop-hook-gated work in this engagement.

---

## Decision Required

Colin's call: Option A, Option B, or a different approach. Once decided, the executable steps will be enumerated and run only after explicit approval.
