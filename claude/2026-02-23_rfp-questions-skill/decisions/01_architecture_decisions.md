# RFP Questions Skill - Architecture Decisions

**Date:** February 23, 2026
**Session:** Building rfp-questions skill with skill-forge
**Status:** APPROVED by user

---

## Decision 1: Model Selection

**Decision:** Sonnet as minimum model, Opus for analysis tasks.

**Rationale:** User has no issue using Opus freely. Cost is not a primary concern for this workflow.

| Agent Role | Model |
|------------|-------|
| source-verifier | Sonnet |
| question-cataloger | Sonnet |
| gap-analyzer | Opus |
| refinement-analyzer | Opus |
| competitor-assessor | Opus |
| final-risk-reviewer | Opus |
| duplicate-checker | Sonnet |
| depth-checker | Sonnet |
| document-generator | Opus |

---

## Decision 2: Agent Teams as Default

**Decision:** Use Agent Teams (peer-to-peer) instead of hierarchical subagents.

**Rationale:** Following django-forge-v2 pattern. Agent Teams is stable enough for production use in 2026. Enables direct communication between workers without coordinator bottleneck.

**Fallback:** Hierarchical mode available if CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS not set.

---

## Decision 3: Hook-Enforced Compliance

**Decision:** Single Stop hook using "Check Previous Phases" pattern.

**Rationale:** Text saying "MUST" doesn't work. Hooks enforce with exit code 2. The hook:
1. Checks for `.rfp-questions/.active` marker (scopes to this skill only)
2. Reads state.json for current_phase
3. Verifies ALL previous phase artifacts exist
4. Blocks progression if any missing

This solves the "LLM skips steps" problem with deterministic enforcement.

---

## Decision 4: Phased Folder Structure

**Decision:** 6-phase folder structure where artifacts MUST be populated.

**Rationale:** User noted that in manual session, "half of the folders were empty or documents were scattered." The hook enforcement ensures every folder gets populated before progression.

```
.rfp-questions/<client-name>/
├── .active
├── orchestration/state.json
├── phase_01_setup/
├── phase_02_analysis/
├── phase_03_review/
├── phase_04_quality/
├── phase_05_approval/
└── phase_06_outputs/
```

---

## Decision 5: HTML Template Embedded in Reference

**Decision:** Embed BayOne HTML/CSS template in a reference file within the skill.

**Rationale:** User preference. Makes skill self-contained rather than depending on external spec file.

---

## Decision 6: User Choice in Output Generation

**Decision:** Phase 6 must confirm with user what outputs they want before generating.

**Rationale:** User feedback: "the user should be involved, and the skill should confirm with the user what they actually want to generate instead of just blindly creating documents."

Options to present:
- Final markdown (always)
- HTML review document (optional)
- CSV export (optional)
- Big4 skill review/refinement (optional)

---

## Decision 7: Big4 Skill Integration

**Decision:** Reference the big4 skill as optional last step for content review.

**Rationale:** User noted: "The Big Four skill effectively acts like a Big Four consultant to review and refine content to prevent misfires and improve phrasing."

Implementation: In Phase 6, after user selects outputs, offer to invoke big4 skill for final polish before generation.

---

## Decision 8: Interactive Review Pattern

**Decision:** Present findings 3-5 items at a time during Phase 3.

**Rationale:** From McGrath session learnings - "Dumping 12 gaps at once" overwhelmed the human. Incremental presentation with "ready to continue?" checkpoints.

---

## Decision 9: Explicit Decision Recording

**Decision:** Every human decision must be confirmed back and logged to review_decisions.md AND state.json.

**Rationale:** "Sounds good" is ambiguous. Need clear audit trail. Pattern:
1. Present item
2. Human responds
3. Coordinator confirms: "Confirmed: [decision]. Recording."
4. Write to both files

---

## Decision 10: All Workers Read-Only

**Decision:** All 9 worker agents use `permissionMode: plan`.

**Rationale:** Workers analyze and report. Only coordinator makes decisions and edits files. This prevents workers from making changes without human oversight.

---

## Cross-References

- Requirements doc: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_mcgrath_rfp/issues_and_improvements/01_skill_requirements_v2.md`
- Handoff doc: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_mcgrath_rfp/issues_and_improvements/02_skill_builder_handoff.md`
- Django-forge-v2 pattern: `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/SKILL.md`
- Reference HTML output: `/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/rfp_questions_review.html`
- Reference CSV output: `/home/cmoore/programming/cisco_projects/cicd/mcgrath/questions/rfp_questions.csv`
