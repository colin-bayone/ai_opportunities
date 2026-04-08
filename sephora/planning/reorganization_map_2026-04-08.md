# Sephora Reorganization Map

**Date:** 2026-04-08
**State:** D (Multi-project folder with mixed content)
**Methodology:** Singularity Reorganization Guide, Phase 0

---

## Current Top-Level Inventory

| Item | Type | Files | State |
|------|------|-------|-------|
| `edw_modernization/` | Singularity project | 110 | C (Complete, needs validation) |
| `qa_qe_playwright/` | Singularity project | 21 | C (Complete, needs validation) |
| `2025-02-25_andrew-meeting-prep/` | Pre-Singularity analysis | 124 | Needs assessment |
| `context/` | Raw source materials | 37 | Needs sorting |
| `ravi/` | Job description track | 26 | Needs decision |
| `project/` | Legacy folder | 5 | Needs decision |
| `planning/` | Legacy folder | 2 | Needs decision |
| `stakeholders/` | Legacy folder | 1 | Needs decision |
| `deliverables/` | Legacy folder | 1 | Needs decision |
| `research/` | Legacy folder | 0 (empty) | Remove |
| `docs/` | Legacy folder | 0 (empty) | Remove |
| `00_index.md` | Navigation file | 1 | Outdated |

---

## Proposed Decisions (Need Your Input)

### 1. `edw_modernization/` — Validate only

Already Singularity-formatted with 110 files, 58 research docs, active through April 2, 2026. Proposed action: run the State C validation checklist to confirm everything is complete and no source materials were missed. No restructuring needed.

**Decision needed:** Agree to validate-only?

### 2. `qa_qe_playwright/` — Validate only

Singularity-formatted with 21 files, lighter but complete structure. One source transcript (Vaibhav, March 24). Proposed action: same State C validation.

**Decision needed:** Agree to validate-only?

### 3. `2025-02-25_andrew-meeting-prep/` — Archive candidate

124 files of pre-Singularity meeting analysis. This folder has a rich custom structure (meetings broken into metadata, timeline, speaker analysis, quotes, Q&A, commitments, sentiment) covering the same meetings that `edw_modernization/research/` now covers.

**Key question:** Is any of this content NOT already captured in the edw_modernization Singularity research? If the Singularity research was built from the same source transcripts, this entire folder is superseded.

**Proposed action:** Compare the source transcripts in this folder against `edw_modernization/source/`. If they match, move the entire folder to `archive/`. If there are unique source materials here, copy them to `edw_modernization/source/` first.

**Decision needed:** Do you know if this was the pre-Singularity version of what became edw_modernization? If yes, archive the whole thing.

### 4. `context/` — Sort and distribute

37 files of raw source materials. Two subcategories:

**4a. Meeting transcripts and emails** (14 files): `email1.txt`, `email2.txt`, `email_3.txt`, `email_3-6-2026.txt`, `mani-transcript1.txt`, `mani_transcript2.txt`, `meeting4-technical-deep-dive.txt`, `mani-meeting2-notes.txt`, `mani_transcript2_summary.txt`, `andrew-girishi-meeting1.txt`, `maher_profile.txt`, etc.

These are likely the raw source materials that edw_modernization was built from. **Proposed action:** Check if each one already exists in `edw_modernization/source/`. If yes, archive. If not, copy to `edw_modernization/source/`.

**4b. ETL_use_case/ subfolder** (23 files): XML job definitions, DDL statements, stored procedures, YAML deployment files, Excel files, a DOCX describing ETL migration use cases.

**Decision needed:** Is this a separate workstream that deserves its own Singularity project? Or is it reference material for edw_modernization? Or archive material?

**4c. andrew-ho/ and other subfolders**: Appear to be supplementary context. Will check if already captured.

### 5. `ravi/` — Needs your call

26 files across 4 job description tracks (ML Platform Engineer, ML Engineer, AI Engineer, Data Engineer) with recruiter guides and search terms.

**Options:**
- **Option A:** Make it its own Singularity project (`sephora/staffing/` or `sephora/ravi_jd_creation/`)
- **Option B:** Archive it as a completed task
- **Option C:** Leave it as-is if it's still active

**Decision needed:** Is this an active workstream or completed? Should it be a project or archived?

### 6. Legacy top-level folders — Archive

`project/` (5 files), `planning/` (2 files), `stakeholders/` (1 file), `deliverables/` (1 file) contain early engagement content that predates Singularity. This content should now live in `edw_modernization/` if it is not already captured there.

**Proposed action:** Check each file against edw_modernization. Archive everything that is already captured. Copy anything unique to the appropriate project folder first.

### 7. Empty folders — Remove

`research/` and `docs/` are empty. Remove them.

### 8. `00_index.md` — Rewrite after cleanup

Outdated as of Feb 12, 2026. Rewrite after reorganization is complete to reflect the new structure.

---

## Proposed End State

```
sephora/
├── 00_index.md                (rewritten)
├── edw_modernization/         (validated Singularity project)
├── qa_qe_playwright/          (validated Singularity project)
├── [ravi/ or staffing/]       (project or archived — your call)
└── archive/
    ├── 2025-02-25_andrew-meeting-prep/
    ├── context/               (after distributing unique files)
    ├── project/
    ├── planning/
    ├── stakeholders/
    └── deliverables/
```

---

## Execution Order (After Approval)

1. Validate `edw_modernization/` (State C checklist)
2. Validate `qa_qe_playwright/` (State C checklist)
3. Compare `context/` files against project source/ folders, distribute unique ones
4. Compare `2025-02-25_andrew-meeting-prep/` against edw_modernization, determine overlap
5. Compare legacy top-level folders against projects
6. Handle `ravi/` per your decision
7. Move everything that's been accounted for to `archive/`
8. Remove empty folders
9. Rewrite `00_index.md`
