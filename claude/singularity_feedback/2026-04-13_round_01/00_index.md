# Singularity Feedback Round 01

**Round date:** 2026-04-13
**Scope:** Consolidation of all Singularity-specific feedback, observations, and improvement notes discovered in the repository as of this date.
**Purpose:** Single location for future sessions to reference accumulated feedback when extending or refining the Singularity skill.

---

## Structure

- `00_index.md` — This file. Inventory and reading order.
- `sources/` — Copies of every Singularity feedback file found in the repository, preserved as snapshots. Originals remain in their original locations.
- (future) `00_synthesis.md` — Thematic synthesis across all sources. Not yet written.

---

## Source File Inventory

### Primary Sources (Current, Authoritative)

| File | Copied From | Original Date | Description |
|------|-------------|---------------|-------------|
| `sources/01_lam_skill_notes_authoritative_2026-04-09.md` | `lam_research/ip_protection/planning/skill_notes.md` | Through 2026-04-09 | The authoritative and current skill notes file. 271 lines. Includes all patterns from 2026-03-20 plus critical failure corrections added on 2026-04-06 and 2026-04-09. This is the most complete record. |
| `sources/02_reorganization_session_skill_issues_2026-04-13.md` | `claude/2026-04-13_singularity_reorganization_session/skill_issues.md` | 2026-04-13 | Issues encountered during a session reorganizing four engagement folders (cisco/epnm_ems, sephora, lam_research, tailored_brands) into Singularity format. Covers source material handling, decision presentation, reorganization gaps in the skill, and process patterns. |

### Stale Snapshots (Historical, Superseded by Source 01)

| File | Copied From | Original Date | Description |
|------|-------------|---------------|-------------|
| `sources/03_stale_snapshot_skill_notes_2026-03-20.md` | `claude/2026-03-20_lam-research/planning/skill_notes.md` | 2026-03-20 | Earlier snapshot of the skill notes file, 154 lines. Ends at "Discussion Capture" section. Missing all 2026-04-06 and 2026-04-09 additions. **Fully superseded by source 01.** |

**Note on stale snapshots:** Three byte-identical copies of this stale snapshot existed in the repository (md5 hash `3687d905a845f73a673806124a841fb1`) at these locations:

1. `claude/2026-03-20_lam-research/planning/skill_notes.md` — the one copied above
2. `lam_research/ip_protection/archive/planning/2026-03-20_session/skill_notes.md` — archived copy
3. `.claude/skills/singularity/references/worked_example/planning/skill_notes.md` — inside the skill's worked_example folder

Only one copy is preserved here because they are byte-identical. The copy inside the skill's worked_example folder exists because the entire `worked_example/` directory was copied from the Lam engagement as a reference example, and the skill_notes came along for the ride. That copy needs a frozen-in-time header added to it so future sessions do not treat it as authoritative (tracked in source 07, item to be addressed separately).

### This Session's Work Products (Round 01 Contributions)

These are the analysis and synthesis documents produced during the 2026-04-10 through 2026-04-13 work. They are Singularity feedback in the sense that they capture patterns, design decisions, and improvement items discovered during active use.

| File | Copied From | Description |
|------|-------------|-------------|
| `sources/04_nested_design_exploration_2026-04-10.md` | `claude/2026-04-10_singularity_nested_design/00_exploration_and_design.md` | Design document for nested singularity (sub-singularity) pattern. Covers team sub-singularities, cross-reference files, tracking folder dual model, documents folder. |
| `sources/05_slide_format_spec_2026-04-10.md` | `claude/2026-04-10_singularity_nested_design/01_slide_format_spec.md` | Presentation design language spec (the version that was copied into the skill as `references/presentation_design_language.md`). |
| `sources/06_improvements_tracker_2026-04-13.md` | `claude/2026-04-10_singularity_nested_design/02_skill_improvements_tracker.md` | Running tracker of improvements: completed, working implementations not yet codified, pending integrations, lessons learned from Srinivas deck. |
| `sources/07_master_todo_list_2026-04-13.md` | `claude/2026-04-10_singularity_nested_design/03_master_todo_list.md` | Full five-phase to-do list covering gold standards, nested singularity codification, presentation design hardening, SKILL.md integration, and mermaid polish. |
| `sources/08_open_questions_2026-04-13.md` | `claude/2026-04-10_singularity_nested_design/04_open_questions.md` | Open questions for Colin, what is not working well, and pending clarifications. Includes two recorded recurring failure patterns from this session (batched questions, unilateral filtering during exploration). |

---

## Files Explicitly Not Included (Ruled Out of Scope)

These files were discovered during exploration but are not about Singularity. They remain in their original locations for their respective skills:

| File | Skill | Why Excluded |
|------|-------|--------------|
| `claude/2026-02-20_meeting-analyzer-hook-redesign/00_skill_forge_feedback.md` | skill-forge | About hook design issues in the meeting-analyzer skill, not Singularity. Belongs to skill-forge's feedback history. |
| `.claude/projects/-home-cmoore-programming-cisco-projects-cicd/memory/feedback_follow_skill_workflows.md` | skill-forge | About workflow compliance during skill-forge builds. Not Singularity-specific. |
| `mcgrath/planning/2026-02-20_rfp_question_workflow/skill_development/00_feedback_log.md` | rfp-questions | About RFP question skill development. Not Singularity. |

If future rounds of consolidation cover other skills, those files should go into their respective `claude/<skill>_feedback/` folders.

---

## Reading Order

For a future session picking this up cold:

1. Read this index file (`00_index.md`) to understand what is here
2. Read `sources/01_lam_skill_notes_authoritative_2026-04-09.md` first — it is the most comprehensive record of accumulated skill wisdom
3. Read `sources/02_reorganization_session_skill_issues_2026-04-13.md` for the reorganization-specific gaps
4. Read `sources/06_improvements_tracker_2026-04-13.md` to see what has been completed vs. pending
5. Read `sources/07_master_todo_list_2026-04-13.md` to see the five-phase plan
6. Read `sources/08_open_questions_2026-04-13.md` for unresolved items and recurring failure patterns
7. Skip `sources/03_stale_snapshot_skill_notes_2026-03-20.md` unless historical context is needed — its content is fully inside source 01
8. Read `sources/04_nested_design_exploration_2026-04-10.md` and `sources/05_slide_format_spec_2026-04-10.md` for the specific new patterns established this session

---

## Future Rounds

When a new round of feedback is consolidated:

1. Create a new sibling folder: `claude/singularity_feedback/YYYY-MM-DD_round_NN/`
2. Follow the same structure (`00_index.md` + `sources/` subfolder)
3. Cross-reference prior rounds when topics overlap
4. Do not modify prior rounds — they are historical snapshots

---

## Open Synthesis Work

The synthesis document (`00_synthesis.md`) has not yet been written. It would extract themes across all sources and produce a clean, deduplicated view of the feedback. Candidate themes observed during inventory:

- Discussion mode behavior (one question at a time, bring perspective, etc.)
- Transcript processing (multi-pass, format before reading, speech-to-text interpretation)
- Critical failure patterns (using research library, reading references before discussing, declaring work done prematurely)
- Folder organization (deliverables vs presentations vs planning, sub-singularity structure)
- Source material handling (format transcripts first, no duplicate files, verify before assuming)
- Agent file writing (permissions, write directly, do not fall back)
- Document quality (anti-patterns, paraphrase not verbatim, context and framing)
- Exploration behavior (no unilateral filtering, surface inventory first)

Writing the synthesis is a next step when Colin is ready.
