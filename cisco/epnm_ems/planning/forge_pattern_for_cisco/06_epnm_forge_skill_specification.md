# EPNM Forge Skill — Specification for the Cisco-Machine Claude Session

**Audience:** Claude orchestrator session on the Cisco-issued machine.
**Date:** 2026-04-26
**Status:** This is the active plan. Issue-shaped work via a forge skill is the chosen workflow.

---

## What you are building

You are building a Claude Code skill that processes GitHub issues for the EPNM-to-EMS UI conversion engagement. Each issue describes a bite-sized piece of conversion work scoped to a specific repository. The skill picks up an issue, sets up a worktree, performs the implementation in phases with enforced compliance, and produces a draft pull request linked back to the issue. Colin reviews each PR and either merges or requests changes.

You have SkillForge available to construct the skill itself. You have access to the actual EPNM and EMS repositories on this machine. The other Claude session (running on Colin's BayOne laptop) does not have repository access — its job was to give you this spec, not to design the skill in detail. The substantive technical decisions about how the conversion happens are yours to make based on what you see in the code.

The companion files in this folder (`01_anatomy_and_self_containment_audit.md` through `05_singularity_pattern_reference.md`) are the analytical reference set. You do not need to read them sequentially before starting. Use them as needed during construction:

- File 01 — DjangoForge anatomy. Reference if you want to see how an existing similar skill handled structure.
- File 02 — DjangoForge 8-phase workflow. The workflow logic in this spec adapts from there.
- File 03 — DjangoForge scripts and hooks. Reference for how the enforcement layer is implemented.
- File 04 — DjangoForge references audit. Reference for what reference material a forge skill needs.
- File 05 — Singularity skill pattern. **This is the structural template.** Self-containment, frontmatter hooks, folder layout, agent dispatch. Use this as the model for the skill's shape.

---

## Skill identity

Pick a name that reflects the engagement scope. `epnm-forge` or `cisco-forge` or similar. The exact name is your call. Use lowercase with hyphens or underscores per the skills convention.

Skill description (suggested starting point — refine):

```
End-to-end EPNM-to-EMS classic-view conversion via GitHub issues with enforced compliance.
Issue-driven, multi-repo aware, audit-ready.

WHEN to use: Processing a GitHub issue labeled `agentic` on any of the 14 EPNM/EMS repositories.
WHEN NOT to use: General code questions, exploratory work, anything not tied to a specific issue.

Features: 8-phase workflow with hook enforcement, multi-repo state, memory/load self-review,
audit-ready commit pattern verification, draft PR handoff to Colin.
```

Argument hint: `[issue-number]` or `[repo-name]/[issue-number]` if you want to disambiguate across repos.

---

## Self-containment posture (non-negotiable)

The skill must be 100% self-contained. The convention in this repository is strict: a skill carries every file it depends on within its own folder. The Singularity skill (`/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/`) is the canonical example — study its layout (file 05).

Specifically for this skill:

- **All hooks declared in SKILL.md frontmatter.** Use the YAML structure shown in file 05. Do not register hooks in `settings.local.json`. The frontmatter is the only registration point.
- **All scripts live in `scripts/` inside the skill folder.** No external script paths.
- **All references live in `references/` inside the skill folder.** No external reference paths.
- **Worktree creation and cleanup logic lives in `scripts/` as a bundled script.** Do not depend on a sibling worktree skill. If you find a worktree skill in this repository or elsewhere, copy the relevant logic into a script inside this skill, then condense it down to what this workflow actually needs. One skill, one purpose, one folder.
- **No cross-skill dependencies.** SkillForge is the construction tool, not a runtime dependency. Once your skill is built, it must run without invoking other skills.

The Singularity Hard Rule 10 phrasing fits here too: "All reference files, templates, and company context live within the skill folder. Never cross-reference session folders, engagement folders, or external paths as authoritative sources from within the skill definition."

---

## Suggested workflow shape

The DjangoForge 8-phase workflow is a good starting point. The adaptations for EPNM are listed below. Treat these as proposals — adjust based on what you find in the actual EPNM and EMS code.

### Proposed phase structure

| # | Phase | Purpose | Notable for EPNM |
|---|-------|---------|------------------|
| 0 | REPO MAP | Identify which of the 14 repos this issue touches | New phase. EPNM is multi-repo; DjangoForge was single-repo. |
| 1 | SETUP | Create worktree on the appropriate repo's `agentic UI conversion` branch | Bundled worktree script. May span multiple repos for cross-repo issues. |
| 2 | TRACE | Recursive dependency walk of the issue (per DjangoForge) | Same logic; adapt the dependency-prose patterns to whatever conventions Cisco issues use. |
| 3 | ANALYZE | Read the issue, do the Issue-vs-Reality check | Same as DjangoForge. |
| 4 | PLAN | Generate the implementation plan | Adapt to EPNM/EMS context — Java Swing → Angular conversion patterns. |
| 5 | APPROVE | Plan-mode handoff to user | Same as DjangoForge. |
| 5.5 | MEMORY GATE | Self-review the converted output for resource consumption | New phase. Guhan's gating ask from Set 09. See memory/load reference (proposed below). |
| 6 | IMPLEMENT | Execute the plan in the worktree | Per-stack patterns: Java Swing source side, Angular target side. |
| 7 | VERIFY | Tests, type checks, lint, comparative validation | Adapt to EPNM/EMS toolchain. |
| 7.5 | COMPLIANCE | Verify audit-ready commit pattern (attribution, in-line rationale, agent-tagging) | New phase. India team will be reviewing. |
| 8 | PR | Draft PR linked to issue, all artifacts in place | Same as DjangoForge with EPNM-specific PR template. |

You may decide that some of these collapse, expand, or reorder. Verify your sequence against the actual issue lifecycle by running through it once before locking it.

### State.json schema additions for multi-repo

DjangoForge's `state.json` is single-repo. For multi-repo, add at minimum:

- `repos_in_scope` — list of repository names this issue touches
- `branch_per_repo` — map of repo → branch (almost always `agentic UI conversion` off `develop`)
- `worktree_paths` — map of repo → worktree filesystem path
- `out_of_scope_explicit` — list of things NOT to touch (bookmarks behavior change, architectural debt, DPM, additional screens, EMS Angular code modification, backend changes — see file 04 section 6 for the catalog)
- `audit_ready_commits` — boolean tracking whether the current run has applied the commit pattern
- `toggle_scope` — list of screens this issue's toggle work covers (subset of inventory and fault-management screens)
- `agentic_label_confirmed` — boolean confirming the issue carries the `agentic` label (per the convention Saurav established)

Other fields from DjangoForge's schema (issue number, current phase, what we are NOT building, etc.) carry over. See file 02 section on the schema.

---

## Hooks (declared in frontmatter)

Use the Singularity hook YAML structure (file 05). The receiving skill needs at minimum:

### Stop hook
Verifies the current phase's artifacts exist before allowing the run to proceed. The "Check Previous Phases" pattern. Exit code 2 to block. Singularity's `singularity_stop.py` is the implementation model.

### SessionStart hook
Re-injects engagement context after compaction. The Cisco engagement context (current issue number, repos in scope, branch state, what we're NOT touching) is what should be re-injected. Without this, a long-running session loses the issue context after Anthropic's context-compaction kicks in.

### PreToolUse hook (optional but recommended)
Blocks tool calls that would violate the out-of-POC-scope catalog. For example: an Edit tool call that touches a file in a DPM screen, or a Bash command that runs `npm install` for a dependency that isn't on the approved list. The hook reads `state.json.out_of_scope_explicit` and matches against the tool call's target.

The DjangoForge hooks live OUTSIDE the skill in this repo. That arrangement is a deviation from the modern convention. **Do not replicate that arrangement.** Declare in frontmatter, place scripts in `scripts/` inside the skill folder, and exit-early-if-not-active is no longer needed because frontmatter-declared hooks fire only when the skill is active.

---

## Scripts to bundle

At minimum, in `scripts/`:

- `worktree_create.sh` — creates a worktree for a given repo at the `agentic UI conversion` branch. Bundled, not a cross-skill dep.
- `worktree_cleanup.sh` — removes the worktree after PR merge or run abort.
- `trace_dependencies.py` — recursive issue-dependency walker, adapted from DjangoForge (file 03 has the line-by-line). Adjust the dependency-prose patterns to whatever conventions Cisco issues use; this is something you will only know after looking at actual issues.
- `verify_branch_sync.sh` — verifies the `agentic UI conversion` branch is synced with `develop` on the target repo. Adapted from DjangoForge.
- `forge_stop_check.py` — the Stop hook implementation (Proof via Artifact pattern from Singularity).
- `forge_session_start.py` — the SessionStart hook implementation (re-injects state.json contents).
- `memory_load_aggregate.py` — collects results from the Phase 5.5 memory/load self-review and produces the artifact the Stop hook expects.
- `compliance_verify.py` — Phase 7.5 audit-ready commit pattern check (verifies attribution, rationale tags, agent-content separation in the worktree's commits).

Some of these you may collapse or rename. Keep them inside `scripts/`.

---

## References to bundle

In `references/`. The Singularity references folder is the model for how to organize this. File 04 section 6 proposed eight reference files. Refining that list:

1. **`workflow_phases.md`** — the per-phase requirements (the artifact contract the Stop hook checks). Equivalent of DjangoForge's `phase_requirements.md`. Heavily adapted for EPNM phases including REPO MAP, MEMORY GATE, COMPLIANCE.

2. **`agent_dispatch_pattern.md`** — how the skill spawns agents in parallel for sub-tasks. Equivalent of DjangoForge's `agent_teams_usage.md`. The Agent Teams pattern from DjangoForge transfers; the Singularity agent prompt template is also a useful model.

3. **`multi_repo_coordination.md`** — how to handle issues that span multiple repos. New for EPNM. Cover: when to use one worktree vs. many, how to keep cross-repo PRs in sync, how to handle a partial-success state where some repos' work landed and others did not.

4. **`audit_ready_commit_pattern.md`** — the commit conventions the India team will be reviewing. Cover: author/committer field conventions, in-line decision rationale (Colin's human-in-the-loop authorship), agent-generated content tagging, branch and naming conventions. Pull from the orchestrator briefing's "Audit-ready commit pattern" section.

5. **`toggle_architecture.md`** — the classic-view toggle architecture. UI control placement, parallel-package shipping, same-backend rule, bookmarks-as-EMS rule. Pull from Set 07 architecture research.

6. **`out_of_scope_catalog.md`** — explicit list of what NOT to touch. Bookmarks behavior change, architectural debt, DPM, additional screens, EMS Angular modification, backend changes. The PreToolUse hook reads this to block violations.

7. **`label_and_branch_conventions.md`** — `agentic` label requirement on every in-scope issue, `agentic UI conversion` branch on each repo, base of `develop`. PR linking via `Closes #N` syntax (no auto-close from forge — rely on GitHub's standard linkage).

8. **`pr_description_template.md`** — the PR body format. Sections for: what the issue asked for, what was built, what was deliberately not changed (out-of-scope), test results, comparative validation results (if applicable), reviewer guidance.

9. **`memory_load_self_review.md`** — the Phase 5.5 self-review checklist. Pull from the orchestrator briefing's "Memory and load self-review" section. Bundle size, initial-load impact, toggle-state memory, render thrashing, backend load, memory leaks in long sessions, dependency footprint.

10. **`hard_rules.md`** — the behavioral rules for this skill. Singularity's `references/hard_rules.md` is the model: numbered rules, each with a "why" tracing to a real-world incident or concern. Start with rules drawn from the Set 09 research:
   - Never expand scope into out-of-scope items (bookmarks change, debt fixes, DPM, etc.)
   - Always apply the audit-ready commit pattern
   - Never modify EMS Angular code (bolt-on, not invasive)
   - Same backend always (toggle hits same backend)
   - Honest state in commit messages and PR descriptions (no forward-leaning claims in artifacts that will be reviewed by the India team)

The hard-rules pattern from Singularity is high-value. Lift it.

---

## Design references — separate file

The technical references about the EPNM and EMS stacks (Java Swing fat client patterns, Spring Boot conventions, Angular 21 patterns, conversion best practices, anti-patterns observed in the codebase) deserve their own treatment. See file 07 — `07_design_references_to_author.md` — for the structure and authoring guidance. These references must be substantive. They are not boilerplate. They are what makes the skill's outputs match what good code looks like for this engagement.

You will author them by reading the actual code in the repositories. The other Claude session does not have access to that code, so this part is yours alone.

---

## Issue creation discipline

Per Saurav's direction, every issue this skill processes must carry the `agentic` label. This is the filter the Cisco team will use to identify BayOne-driven work. The `agentic UI conversion` branch on each repo is where commits land.

Issues are bite-sized. The DjangoForge model (per file 02) is one issue per discrete unit of conversion work, with explicit dependency declarations using the prose-pattern conventions (`Depends on`, `Blocked by`, `After`, `Requires`, `Prerequisite:`). When breaking the remaining build work into issues, favor smaller and more numerous over larger and fewer — small issues are easier for the India team to review.

Issue creation is upstream of this skill. You are not the issue creator. Colin (and Saurav) decide what gets issued and in what shape. Your skill consumes the issue, performs the work, and produces the PR.

---

## Adaptation instructions

This spec is a starting point. The codebases will tell you things this spec does not. When you find a contradiction between this spec and what is true in the EPNM/EMS code, the code wins. Document the deviation in your skill's `references/hard_rules.md` so future runs know.

Specific things you should investigate in the actual codebase before locking the workflow:

- **The actual Java Swing patterns in EPNM.** The Set 08 research file `cisco/epnm_ems/research/08_research_epnm_legacy_stack_2026-04-07.md` has Dojo-focused content from the prior research pass, but EPNM also includes Java Swing fat-client elements per the broader engagement context. Walk the actual code, identify which screens/components are Swing vs. Dojo, and let that determine the conversion pattern your skill applies.
- **The actual Angular 21 patterns and Harbor/Magnetic design system usage in EMS.** Set 08 has reference material; the actual code will have specifics that need to be encoded in your design references.
- **The actual repository layout across the 14 repos.** The Confluence page from Set 07 plus the existing 14-repo mapping in `cisco/epnm_ems/research/09_meeting_full_system_mapping_2026-04-24.md` (and the ~250 files Colin's prior pass produced) are the inventory. Verify against current repository state.
- **The actual `agentic UI conversion` branch state on each repo.** Confirm the branches exist and what they currently contain. Your skill needs to know.
- **The actual issue conventions Cisco/Saurav has set up.** Label conventions, milestone conventions, dependency-declaration patterns. The dependency-prose patterns from DjangoForge may not match what Cisco issues actually use.
- **The actual test infrastructure.** Per Set 07, Cisco has thousands of test cases across seven categories with data-driven testing. The Phase 7 verification step needs to integrate with whatever test runner the EMS repos use, not assume Django's `manage.py test` analog.

If anything in this spec contradicts what the codebase tells you, treat the codebase as authoritative and update the skill accordingly.

---

## Order of construction

Suggested order. Adapt if you see a better path.

1. **Build the skeleton skill via SkillForge.** Frontmatter shape per Singularity. Empty `scripts/`, `references/`, `gold_standards/` if you want. SKILL.md with section headers and TODOs.
2. **Implement the Stop hook script first.** `scripts/forge_stop_check.py`. Use Singularity's `singularity_stop.py` as the implementation model. The Stop hook is the central enforcement mechanism — get it right early.
3. **Implement the SessionStart hook script next.** `scripts/forge_session_start.py`. Re-injects engagement context.
4. **Build out the workflow phases in SKILL.md.** One phase at a time. For each, write the phase body, the artifact contract, and the Stop hook check that verifies it.
5. **Bundle the worktree scripts.** `worktree_create.sh`, `worktree_cleanup.sh`. Keep them small and skill-specific; do not generalize.
6. **Implement `trace_dependencies.py`.** Adapt from DjangoForge with the prose-pattern set adjusted for Cisco issue conventions.
7. **Implement `verify_branch_sync.sh`.** Multi-repo aware version of DjangoForge's.
8. **Author the references.** The 10 reference files listed above. Workflow first, then operational, then hard rules last.
9. **Author the design references** (per file 07).
10. **Run the skill end-to-end on a real Cisco issue** before declaring it ready. The first run will surface deviations from this spec.
11. **Iterate.** This skill will get better with use. Treat the first month as the calibration period.

---

## What this spec does not cover

- The exact Cisco issue conventions (labels beyond `agentic`, milestones, project boards, assignee patterns). Investigate and document in your label/branch conventions reference.
- The specific test commands and tooling for EMS verification. Investigate and document in your phase requirements reference.
- The CI/CD pipeline integration points. Investigate; if there is CI on the `agentic UI conversion` branches, your Phase 7 needs to wait for it.
- The specific commit message format. Investigate the existing commits on the branches; match the established pattern.
- Any Cisco-internal compliance requirements beyond the AI-tooling stance from Set 07. If anything is added during the engagement, fold it into hard rules.

---

## Final note

The spec is yours to refine. The other Claude session and Colin will iterate with you on outputs once the skill is running. The audit-ready commit pattern, the bolt-on rule, the same-backend rule, and the agentic-label requirement are the four hard constraints — those do not flex. Everything else is open to adaptation based on what you find in the code.

When you start, the first thing to do is read file 05 (Singularity pattern) cover to cover. That is the structural template. Files 01-04 are reference; you can mine them as needed but they are not blocking.
