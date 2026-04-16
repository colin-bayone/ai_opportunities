# Session Handoff: Singularity Skill Extension

**From:** Claude session spanning 2026-04-10 through 2026-04-14
**To:** Next Claude session continuing the work
**Priority:** Folder structure redesign for the Singularity skill

---

## Read This First

This handoff covers a massive multi-day session (11,000+ line transcript) that extended the Singularity skill with presentations, sub-singularities, mermaid diagrams, behavioral enforcement rules, and gold standards. A lot was accomplished. A lot of mistakes were also made and corrected. The next session must understand both.

## Session Folder Structure

```
claude/2026-04-14_singularity_session_handoff/
├── HANDOFF.md                          (this file — start here)
├── KICKOFF.md                          (prompt to paste into the new session)
├── 00_session_overview.md              (high-level summary of everything)
└── references/
    ├── 01_all_changes_by_phase.md      (every file created/modified, organized by phase)
    ├── 02_feedback_violations_and_lessons.md  (all behavioral corrections, B2 audit, lessons)
    ├── 03_unresolved_and_remaining.md  (folder restructure, path issues, open questions, full file list)
    ├── 04_hooks_and_enforcement.md     (enforcement architecture, stop hook, hard rules)
    └── 05_presentations_and_mermaid.md (design language, diagram pattern, mermaid research)
```

## Reading Order

1. **This file** (HANDOFF.md) for orientation
2. **00_session_overview.md** for the full picture
3. **03_unresolved_and_remaining.md** for what needs to happen next (the folder restructure is the immediate priority)
4. **02_feedback_violations_and_lessons.md** for behavioral patterns to avoid
5. The other reference files as needed for specific context

## The Immediate Priority: Folder Structure Redesign

The Singularity skill's file organization is a mess after this session's additions. Colin explicitly flagged this as the next thing to tackle. Specific problems:

- `assets/design/gold_standards/` is 7 levels deep in places
- Three separate `charts/` folders exist at different levels
- Gold standards are split between `references/worked_example*/` and `assets/design/gold_standards/`
- The `assets/` folder was introduced this session and created unnecessary nesting
- `complete_structure.md` is out of date (28 undocumented files, misnamed entries)
- Some files referenced in docs do not exist; some existing files are not referenced

Colin's vision: gold_standards should be organized by category (proposals, approaches, presentations, etc.) with each category being self-contained. The folder depth needs to be drastically reduced.

**Do NOT start reorganizing without discussing the target structure with Colin first.** He has opinions about how it should look.

## Key Files in the Skill

The skill is at `.claude/skills/singularity/` and currently has 115+ files. The most important ones for the next session:

| File | What It Is |
|------|-----------|
| `SKILL.md` | Main skill definition with 10 structural rules, 7 flows, sub-singularities section |
| `references/hard_rules.md` | 16 behavioral rules (B1-B16) — MANDATORY read every invocation |
| `references/enforcement_architecture.md` | How the artifact-check enforcement pattern works |
| `references/presentation_design_language.md` | Slide generation system (recently corrected for prescriptive content) |
| `references/mermaid_design_standards.md` | Diagram visual standards (recently corrected for prescriptive content) |
| `references/mermaid_shape_library.md` | Quick-reference menu of all mermaid shapes, arrows, icons |
| `references/nested_singularity.md` | Sub-singularity pattern |
| `references/complete_structure.md` | **OUT OF DATE** — needs full refresh after restructure |
| `scripts/singularity_stop.py` | Stop hook with 6 artifact checks |

## Critical Behavioral Context

The dominant failure pattern this session was **B2 violations**: Claude taking specific, situational feedback and generalizing it into rigid universal rules with invented thresholds. This happened repeatedly with diagrams, slide content, file reading counts, and team meeting methodology.

The full audit is in `references/02_feedback_violations_and_lessons.md`. The 11 items found and their resolutions are in `claude/2026-04-13_mermaid_research/b2_violation_review_2026-04-14.md`.

**Key rule for the next session:** Do not invent thresholds, absolute bans, or universal rules from specific feedback. If Colin says one specific thing needs to change in one specific context, change that one thing. Do not generalize.

## Other Key Context

- **Feedback catalog:** `claude/singularity_feedback/2026-04-13_round_01/` has the exhaustive synthesis, change log, and all source files
- **Mermaid research:** `claude/2026-04-13_mermaid_research/` has 5 research docs, diagram versions, shape library prompt, path verification results
- **Path issues:** `claude/2026-04-13_mermaid_research/path_issues_master.md` has 10 path issues (1 fixed, 1 file deleted, 8 pending restructure)
- **Cisco presentation:** `cisco/cicd/presentations/srinivas_status_2026-04-10/` is the real deck that was used in a client meeting
- **Team sub-singularity:** `cisco/cicd/team/` is the first working instance of the nested singularity pattern
- **Full transcript:** `/home/cmoore/programming/ai_opportunities/2026-04-14-170841-look-at-ciscocicd-we-have-used-the-singularity_508PM_MASTER.txt` (11,000+ lines, read sections as needed for specific context)

## How to Operate

1. Use to-do lists in markdown files that persist to disk
2. Capture ALL feedback from Colin in a session folder immediately
3. Do NOT invent rules, thresholds, or restrictions that Colin did not give
4. Ask Colin when in doubt — do not prescribe
5. Read files before describing them (B4)
6. One question at a time in discussion (B1)
7. Do not execute after multiple corrections without confirming the agreed approach (B16)
8. The folder structure redesign is the immediate priority — but wait for Colin to guide the target structure
