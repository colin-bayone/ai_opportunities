# DjangoForge v2 — References and Standards

**Audience:** Claude orchestrator session on the Cisco machine.
**Source skill:** /home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/
**Purpose:** Reference content audit and EPNM adaptation map. Pair with files 01-03.

---

## 0. Reference inventory at a glance

DjangoForge v2 ships exactly two reference files, both inside the skill folder:

```
.claude/skills/django-forge-v2/
├── SKILL.md
├── references/
│   ├── agent_teams_usage.md       (296 lines)
│   └── phase_requirements.md      (247 lines)
└── scripts/
    ├── trace_dependencies.py
    └── verify_branch_sync.sh
```

That is the entire reference surface. The skill does not carry a code-style guide, a commit-message template, an ADR template, a test-coverage policy, or a PR-description template as separate files — those concerns are either inlined in `SKILL.md`, embedded in agent prompts, or absent. Section 4 below catalogs the gaps.

---

## 1. `agent_teams_usage.md` — full content walkthrough

### 1.1 What is in this file

A nine-section reference describing how to operate Claude Code's experimental peer-to-peer agent feature inside the forge workflow. Sections (in order):

1. **What is Agent Teams?** — definition: peer-to-peer collaboration vs. strict hierarchy; agents can message directly, share a task list, give feedback without a coordinator, react in real time.
2. **Enabling Agent Teams** — environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, `.bashrc`/`.zshrc` persistence, and a startup verification snippet that warns if unset.
3. **Agent Teams vs Hierarchical Mode** — comparison table across Communication, Task Assignment, Feedback Loop, Coordination, Token Usage, Parallelism.
4. **Agent Team Composition** — three tables (HIGH / MEDIUM / LOW complexity), each enumerating Agent / Role / Model / Responsibility.
5. **Shared Task List** — the JSON schema agents read and update, with task states (`pending`, `in_progress`, `completed`, `approved`, `rework`).
6. **Communication Patterns** — three quoted dialog examples: Worker→Worker, Worker→Judge, Judge→Worker (rework).
7. **Wave Execution** — the rule that even with peer-to-peer messaging, waves are still enforced; example flow across three waves.
8. **Legacy Mode (Hierarchical)** — how to opt out via `--legacy` flag or `state.json: agent_mode: hierarchical`.
9. **Token Considerations**, **Troubleshooting**, **Best Practices** — operational guidance.

### 1.2 When the skill instructs the agent to read it

`SKILL.md` references this file once, at the bottom under "References":

> For Agent Teams patterns:
> `.claude/skills/django-forge-v2/references/agent_teams_usage.md`

It is **not** marked "MUST read" and there is **no hook** that enforces reading it. It is loaded **lazily** — implicitly when the orchestrator decides to use Agent Teams mode (which is the default per Hard Rule #9, "Agent Teams default — Use `--legacy` flag for hierarchical mode") or when something goes wrong and the orchestrator needs to troubleshoot.

In practice, the main orchestrator session reads it at session start to verify the env var and to recall composition tables. Spawned Foreman/Judge/Worker agents do not read it directly — they receive composition context via their spawn prompts.

### 1.3 What problems it solves

The file exists to prevent these failure modes:

- **Silent fallback to hierarchical mode** when the env var isn't set — solved by the verification snippet.
- **Agents talking through the Foreman unnecessarily**, wasting tokens and serializing parallel work — solved by the explicit communication-pattern examples.
- **Wave skipping** (Workers starting Wave 2 tasks before Wave 1 is fully approved) — solved by the "Wave Execution" section asserting waves are enforced even with peer messaging.
- **Circular dependencies** in the shared task list — called out under Troubleshooting with a concrete example.
- **Choosing the wrong mode for the wrong issue size** — addressed by Token Considerations: prefer `--legacy` for simple issues, Teams for complex.

### 1.4 What patterns it prescribes

- **Peer-to-peer with shared state** — workers read and update one shared task list rather than relaying through Foreman.
- **Direct Worker↔Judge feedback loops** — Judge talks to Workers without a Foreman intermediary.
- **Wave gating preserved** — peer-to-peer is for *intra-wave* parallelism, not for skipping wave boundaries.
- **Per-task-ID communication** — every message references `TASK-NNN`, every status update flows through the JSON schema.
- **Best practices list** — clear task boundaries (independently testable), explicit dependencies, incremental commits per task, judge early (don't batch), summarize what you created when handing off.

### 1.5 Quoted examples

**Worker-to-Worker handoff:**
> Worker-1: "TASK-001 complete. Created GroupConverter class at integrations/jobdiva/search/group_converter.py. Key methods: convert_to_groups(), handle_nested()."
>
> Worker-2: "Acknowledged. Starting TASK-002 which depends on TASK-001. Will use GroupConverter.handle_nested() for my implementation."

**Worker-to-Judge approval:**
> Judge: "Reviewing TASK-001... VERDICT: APPROVED — Clean implementation, Good error handling, Tests pass. Proceed to dependent tasks."

**Judge-to-Worker rework:**
> Judge: "Reviewing TASK-002... VERDICT: NEEDS_REWORK. Issues: Missing null check on line 45; Method name doesn't follow convention. Required changes: 1. Add null check before accessing group.children. 2. Rename process_group() to _process_group() (private method)"

**Wave execution flow:**
> Wave 1: TASK-001 (no deps) → Worker-1 → Judge → APPROVED; TASK-002 (no deps) → Worker-2 → Judge → REWORK → Worker-2 → Judge → APPROVED.
> Wave 2 (starts after Wave 1 all APPROVED): TASK-003 (deps: 001) → Worker-1 → Judge → APPROVED…

**Shared task list JSON** (the structural contract — every agent reads/writes this shape):
```json
{
  "id": "TASK-001",
  "description": "Create group converter class",
  "status": "completed",
  "assigned_to": "Code-Worker-1",
  "depends_on": [],
  "completed_by": "Code-Worker-1",
  "judge_verdict": "APPROVED"
}
```

### 1.6 Adaptation: framework-agnostic vs. Django-specific

| Section | Django-specific? | Notes |
|---------|-----------------|-------|
| What is Agent Teams? | No | Pure Claude Code feature description. |
| Enabling Agent Teams | No | Environment variable is framework-agnostic. |
| Agent Teams vs Hierarchical | No | Generic comparison. |
| Agent Team Composition (HIGH/MEDIUM/LOW) | Mostly no | Roles (Foreman/Worker/Judge/Test-Worker) are generic. The model assignments (Opus for everything except Test-Worker on Sonnet) are skill-specific opinions and may need to be revisited for EPNM. |
| Shared Task List schema | No | Generic JSON contract. |
| Communication Patterns | **Yes — examples only** | The example file paths (`integrations/jobdiva/search/group_converter.py`) and class names (`GroupConverter`, `handle_nested()`) are Django/JobDiva-specific. The *structure* of the dialog is fully generic. |
| Wave Execution | No | Generic dependency-graph semantics. |
| Legacy Mode | No | Generic. |
| Token Considerations | No | Generic. |
| Troubleshooting | No | Generic. |
| Best Practices | No | Generic. |

**Net for EPNM adaptation:** roughly 95% transfers verbatim. The only substantive edits are swapping the example file paths and class names in the Communication Patterns section to EPNM-flavored examples (e.g., a Worker handing off the `BookmarksController` Java port between the EPNM legacy repo and the EMS Spring Boot repo, or a Worker handing off an Angular 21 component shell to a peer who fills in the data binding).

---

## 2. `phase_requirements.md` — full content walkthrough

### 2.1 What is in this file

A per-phase artifact specification that doubles as a Stop-hook contract. The file opens with the explicit promise:

> This document defines the **required artifacts** for each phase. The Stop hook verifies these artifacts exist before allowing progression to the next phase.

It then walks the eight phases in order. For each phase: a one-line **Gate** statement, a table of required artifacts (Path / Min Size / Description), and inline content requirements. The phases are:

1. **Setup** — `issue_fetched.json` (50 chars), `worktree_created.md` (50 chars), `branch_sync_verified.md` (50 chars). Plus: worktree path on filesystem, complexity in state.json, state.json initialized with issue number/title.
2. **Documentation** — `docs_findings.md` (100 chars). Must contain CLAUDE.md patterns, relevant skill docs, project conventions, testing requirements.
3. **Codebase Exploration** — `codebase_state.md` (200 chars), `issue_vs_reality.md` (200 chars), one `pr_analysis/pr_{N}_review.md` per related PR (100 chars each). Includes a templated structure for `issue_vs_reality.md` and a checklist for PR analyses.
4. **Planning** — `task-manifest.md` (100 chars) and `technical-design.md` (100 chars). For HIGH complexity, Architect and Engineer agents produce them separately; for MEDIUM/LOW, a single Planner combines them.
5. **User Approval** — no file artifact; `user_decisions` array in state.json must contain `plan_approved: true`. Includes a Python verification snippet and the explicit rule "**NEVER assume approval. ALWAYS wait for explicit 'approved', 'yes', 'proceed'.**"
6. **Implementation** — one `completed-work/*.md` per task, one `judge-evaluations/judge_evaluation_{TASK-ID}.md` per task. Includes a Python verification snippet that walks `state.completed_tasks` and verifies the eval file exists. Wave progression rule restated.
7. **Testing** — `test_results.md` (50 chars), optional `playwright_results/` directory if UI changed. Lists trigger conditions for Playwright (templates, JS, CSS, HTMX changes).
8. **Git Operations** — `pr_description.md` (50 chars), `final_commit.md` (50 chars). PR linkage and commit-message rules.

The file closes with two anchors:
- A **State.json Critical Fields** JSON template (the canonical schema — issue number, worktree path, complexity, current/completed phases, what_we_are_building, what_we_are_NOT_building, files_being_modified, files_NOT_to_touch, critical_learnings, user_decisions, related_prs, current_wave, pending/completed_tasks, agent_mode).
- A **Verification Commands** block of bash one-liners for manual phase checks.

### 2.2 When the skill instructs reading it

Same place as `agent_teams_usage.md` — listed in the "References" section at the bottom of `SKILL.md`:

> For detailed artifact requirements per phase, see:
> `.claude/skills/django-forge-v2/references/phase_requirements.md`

There is no "MUST read" annotation in the skill body. However, the file is **operationally enforced** because the Stop hook is documented to read it (see 2.3 below). So even if the orchestrator never opens the file, the hooks do — failing to produce the listed artifacts trips an exit-code-2 block.

### 2.3 What enforcement role it plays

This file is the **machine-readable contract for the Stop hook**. From `SKILL.md` Hard Rule #1:

> Hooks enforce compliance — Every phase produces artifacts. Stop hook verifies ALL previous phases complete.

And from the `phase_requirements.md` preamble:

> The Stop hook verifies these artifacts exist before allowing progression to the next phase.

The "Check Previous Phases" pattern (named in Hard Rule #1 and the v2-vs-v1 comparison table) is exactly this contract: at every Stop, walk the prior phases listed in this file and confirm each artifact exists at the documented path with at least the documented minimum size. Phase 5 is special — it checks the `user_decisions` array in state.json instead of a file. Phase 6 is special — it walks `state.completed_tasks` and demands a matching `judge_evaluation_{TASK-ID}.md` for each.

The file itself doesn't run anything; it is the spec the hook implements against. (The hook code lives elsewhere — likely under `.claude/hooks/` in the parent project — but the contract is here in the skill.)

### 2.4 Adaptation: Django-specific vs. generally applicable

| Phase | Django-specific items | Generally applicable items |
|-------|----------------------|---------------------------|
| 1 Setup | None — just `gh issue view`, worktree, branch sync. | All. |
| 2 Documentation | "CLAUDE.md patterns extracted" is project-convention, not framework. | All. The "testing requirements" line presumes the project has documented test requirements somewhere — true for any forge skill. |
| 3 Codebase | None framework-bound. The `issue_vs_reality.md` template is a hard-won pattern from issue #1190 that transfers verbatim. | All. Especially the PR-analysis-per-related-PR pattern. |
| 4 Planning | None. | All. Architect/Engineer split is a complexity-routing pattern, not a framework one. |
| 5 Approval | None. | All. The "never assume approval" rule is universal. |
| 6 Implementation | The wave/judge structure is generic; the `judge_evaluation_{TASK-ID}.md` filename pattern is generic. | All. |
| 7 Testing | "**Django test output**" wording, `poetry run python manage.py test app.tests` command, "HTMX behavior changes" as a Playwright trigger. | The *structure* (test_results.md with command/status/failures/manual checklist) and the Playwright triggers (templates / JS / CSS / behavior) are generic. |
| 8 Git Operations | None. The "no AI/Claude attribution" commit rule is project-convention. | All. |

**Net for EPNM adaptation:** about 90% transfers structurally. The Django-specific surface to replace:

- Phase 2 Documentation must point at the EPNM-equivalent source-of-truth files (e.g., the engagement's CLAUDE.md, the audit-ready commit policy doc, the toggle architecture doc).
- Phase 7 Testing must replace `poetry run python manage.py test` with the actual EPNM build/test command surface — likely some combination of `mvn test` for Spring Boot, `go test ./...` for the Go services, `ng test` and/or Playwright for Angular 21, and a multi-repo orchestration step.
- Phase 7 Playwright triggers translate cleanly: template change → Angular component change; HTMX behavior → Angular signals/RxJS state change.
- The state.json schema needs new fields for multi-repo (see Section 6).

---

## 3. References loading strategy

### 3.1 Where in the workflow are reference files read?

| File | Read when | By whom | How |
|------|-----------|---------|-----|
| `agent_teams_usage.md` | At skill activation, when deciding mode; on troubleshooting agent communication | Main orchestrator | Lazy — referenced from "References" footer of SKILL.md, not loaded eagerly |
| `phase_requirements.md` | At every phase boundary — when producing artifacts (orchestrator) and when verifying them (Stop hook) | Main orchestrator + Stop hook (machine-read) | Lazy by orchestrator; eager/automated by hook |

### 3.2 Eager or lazy

Both files are **lazy** from the orchestrator's perspective. SKILL.md does not say "read these now"; it says "for X, see Y". The skill banks on the orchestrator either remembering the patterns from prior context or pulling the file when stuck.

The Stop hook makes `phase_requirements.md` **effectively eager-from-the-system-side**: even if the orchestrator never reads it, the artifacts must exist or the Stop trips. The orchestrator cannot avoid the contract by ignoring the file; it can only fail.

### 3.3 Who reads them — orchestrator, agents, or both?

- **Main orchestrator session** — reads both, on demand.
- **Spawned agents (Foreman, Workers, Judge, Architect, Engineer, Planner, Test-Worker)** — receive the relevant excerpts via their spawn prompts. They do not generally crack open the reference files themselves. Their accountability is "produce the artifact at the path the orchestrator told you" — the contract is one level removed for them.
- **Stop hook** — reads `phase_requirements.md` (or has the contract baked into its code).
- **SessionStart hook** — does *not* read these references; it re-injects state.json (which is described in `phase_requirements.md` but is a separate live artifact).

### 3.4 Does the skill enforce that they be read?

Not directly. There is no "you must `cat` this file before proceeding" guard. Enforcement happens **indirectly through artifact validation**:

- If you don't read `phase_requirements.md`, you'll likely fail to produce a required artifact and the Stop hook will exit 2.
- If you don't read `agent_teams_usage.md`, you may use the wrong env var or the wrong communication pattern and watch agents silently fall back to hierarchical mode (the verification snippet in Section 1 fires a warning but does not block).

This is a deliberately soft posture — the references inform; the hooks enforce.

---

## 4. What's missing from the reference set

DjangoForge v2 omits several reference categories a mature forge skill might carry. Cataloged here so the EPNM equivalent can decide what to add:

| Missing reference | Status in DjangoForge v2 | Comment |
|-------------------|--------------------------|---------|
| **Code style / lint policy** | Implicit. Not in SKILL.md, not in references, not in scripts. Presumably baked into agent prompts ("follow project conventions") and handled by project-level pre-commit hooks. | EPNM should NOT replicate this gap — see Section 6 for `code_style_per_stack.md` proposal. |
| **Test coverage requirements** | Partly implicit. Phase 7 demands `test_results.md` shows "pass" but doesn't specify a coverage threshold. | EPNM may want a per-stack coverage minimum if Cisco India review will look for it. |
| **PR description template** | Inlined in SKILL.md as prose ("Linked to original issue, Description includes what changed and why, Test plan included"), not as a templated artifact. | A formal template would help — see Section 6 `pr_description_template.md`. |
| **Commit message convention** | Inlined: "References issue number, No AI/Claude attribution, Clear description of changes." Three lines, no examples. | EPNM should formalize this — Cisco audit-ready commits are a hard requirement, not a soft convention. |
| **Architecture Decision Record (ADR) template** | Genuinely absent. There is no ADR pattern in the skill. The closest is `technical-design.md`, but that's a per-task design, not a durable architectural decision. | EPNM may want this for cross-repo architectural choices (toggle scope, classic-view fallback semantics, bookmark mapping). |
| **Branch / label naming** | Implicit. SKILL.md mentions worktrees but not branch naming or labels. | EPNM has an explicit `agentic` label requirement (Saurav) — this needs a reference file. |
| **Out-of-scope catalog** | Implicit. `state.what_we_are_NOT_building` is a single string per session. There is no durable "things this skill never does" list. | For EPNM, "out of POC scope" is a recurring discipline issue (bookmarks-as-EMS, no architectural debt fixes, no DPM, no extra screens) — needs its own reference. |
| **Multi-repo coordination** | Genuinely absent — DjangoForge is single-repo by assumption. | EPNM is 14 repos. Required. |
| **Memory/load self-review gate** | Genuinely absent. | A specific Set-09 requirement for EPNM. Required. |
| **Audit-ready commit pattern** | Partly covered by Phase 8 commit rules; not a standalone pattern. | Cisco India team review demands this; needs to be elevated to a first-class reference. |
| **Toggle architecture / classic-view scope discipline** | Genuinely absent — Django app has no toggle concept. | Required for EPNM-to-EMS classic-view conversion. |

---

## 5. Adaptation map for EPNM context

For each existing DjangoForge reference, here is what the EPNM equivalent should look like:

### 5.1 `agent_teams_usage.md` → `agent_teams_usage.md` (lift-and-shift)

| Section | Action |
|---------|--------|
| What is Agent Teams? | Keep verbatim. |
| Enabling Agent Teams | Keep verbatim. Confirm Cisco-issued machine has the env var permission. |
| Agent Teams vs Hierarchical | Keep verbatim. |
| Agent Team Composition | Keep tables. Reconsider model assignments — for EPNM-to-EMS conversion, Architect (toggle/scope discipline) and Judge (audit-readiness reviewer) probably want Opus; Workers doing per-component conversion can be Sonnet to control cost across a 14-repo workload. |
| Shared Task List schema | Keep verbatim. Add fields for `repo` and `branch` per task (multi-repo). |
| Communication Patterns | **Replace examples.** Substitute Django/JobDiva file paths with EPNM-flavored ones. Example: Worker-1 hands off the converted `BookmarksService` Spring Boot port; Worker-2 picks up the Angular 21 component that consumes it. |
| Wave Execution | Keep verbatim — wave semantics are framework-agnostic. |
| Legacy Mode | Keep verbatim. |
| Token Considerations | Keep, with note: 14-repo coordination amplifies Teams token cost; default to `--legacy` for single-screen conversions, Teams for multi-repo features. |
| Troubleshooting | Keep verbatim. |
| Best Practices | Keep, add: "Each task lives in exactly one repo. Cross-repo work splits into one task per repo with explicit dependencies." |

### 5.2 `phase_requirements.md` → `phase_requirements.md` (substantial rework)

The eight-phase structure transfers cleanly. The artifact contracts need EPNM-specific content. Below is a proposed phase-by-phase mapping drawing from the Set-09 disciplines:

| Phase | DjangoForge artifact | EPNM equivalent |
|-------|---------------------|-----------------|
| 1 Setup | `issue_fetched.json`, `worktree_created.md`, `branch_sync_verified.md` | Same three artifacts. Plus: `repos_touched.md` listing which of the 14 EPNM/EMS repos are in scope, and `agentic_label_applied.md` confirming the `agentic` label is on the source ticket per Saurav's convention. Plus per-repo worktree confirmations for multi-repo tasks. |
| 2 Documentation | `docs_findings.md` | Same, with required content checklist expanded: classic-view toggle policy read, bookmarks-as-EMS rule read, no-debt-fixes rule read, audit-ready commit pattern read. |
| 3 Codebase | `codebase_state.md`, `issue_vs_reality.md`, `pr_analysis/*` | Same three. Add: `cross_repo_state.md` describing where logic lives across the 14 repos for the feature in question (which repo owns the data, which owns the API, which owns the classic UI, which owns the new EMS UI). Add: `scope_discipline_check.md` confirming the change does not include bookmarks fixes, debt cleanup, DPM features, or additional screens beyond the converted one. |
| 4 Planning | `task-manifest.md`, `technical-design.md` | Same. Tasks must be tagged with `repo` and `branch_pattern` (the `agentic UI conversion` branch convention). For HIGH complexity, add a `toggle_design.md` artifact specifying classic-view fallback semantics. |
| 5 Approval | `user_decisions: plan_approved` | Same. Plus: explicit acknowledgment that out-of-scope items have been re-stated and rejected from the plan. |
| 6 Implementation | `completed-work/*`, `judge-evaluations/judge_evaluation_{TASK-ID}.md` | Same. Add: each `judge_evaluation_*.md` must include an **audit-readiness verdict** in addition to the APPROVED/NEEDS_REWORK verdict — does this commit, in isolation, tell a complete and reviewable story to the Cisco India team. |
| 7 Testing | `test_results.md`, optional `playwright_results/` | Same. Replace the Django command with stack-appropriate commands (Angular `ng test`, Spring Boot `mvn test`, Go `go test ./...`). Playwright triggers update to: any Angular component change, any classic-view toggle path, any bookmarks read path. Add: `memory_load_self_review.md` artifact — the Set-09 self-review gate, where the agent reflects on whether it has held the full scope discipline in working memory throughout the implementation. |
| 8 Git Operations | `pr_description.md`, `final_commit.md` | Same. Plus: `audit_ready_commit_chain.md` showing the commit graph and confirming each commit is independently meaningful. PR description template must include a "what was NOT changed" section per the scope discipline rule. |

State.json schema additions for EPNM:

```json
{
  "repos_in_scope": ["epnm-classic-ui", "ems-angular-app", "ems-bff", "..."],
  "branch_per_repo": {"epnm-classic-ui": "agentic-ui-conversion-bookmarks", "...": "..."},
  "out_of_scope_explicit": ["bookmarks_data_layer_fixes", "DPM_features", "architectural_debt", "additional_screens"],
  "audit_ready_commits": ["sha1...", "sha2..."],
  "toggle_scope": "classic-view-fallback-only",
  "agentic_label_confirmed": true
}
```

---

## 6. New reference files the EPNM forge skill should carry

These are EPNM-specific concerns DjangoForge does not address. Each gets a short outline below.

### 6.1 `multi_repo_coordination.md` (new)

**Purpose:** rules for working across the 14 EPNM/EMS repos in a single forge session.

**Outline:**
- Repo inventory table (name, role — classic UI / EMS UI / BFF / data / shared lib, primary stack — Angular 21 / Spring Boot / Go / static).
- Dependency graph between repos (which repo's API contracts feed which UI).
- Worktree-per-repo pattern: one worktree per repo touched, all tracked in `state.json:repos_in_scope`.
- Branch convention per repo: `agentic-ui-conversion-{feature}` per Saurav's directive.
- Cross-repo task dependencies: how a task in repo A blocking a task in repo B is recorded in the shared task list.
- PR pattern: one PR per repo, all linked back to the source issue, all carrying the `agentic` label, all referenced from a coordination doc in the session folder.
- Order of merge: the dependency graph dictates order; the orchestrator records the planned merge order in `phase_08_git/merge_order.md`.

### 6.2 `audit_ready_commit_pattern.md` (new)

**Purpose:** the commit discipline expected by the Cisco India review team.

**Outline:**
- Definition: an audit-ready commit is one a reviewer can read in isolation and understand fully without needing surrounding commits.
- Anti-patterns: "WIP", squashed-everything, mixed-concern commits (UI + API + tests in one).
- Required structure: subject line referencing issue, body explaining *why* (not *what*), file list grouped by concern.
- Per-task commit rule: one commit per `TASK-NNN`, never multiple tasks in one commit.
- Examples: a good commit, a bad commit, side by side.
- Verification: the Phase 8 `audit_ready_commit_chain.md` artifact walks `git log --oneline` and confirms each commit passes the criteria.
- Cross-reference to `pr_description_template.md` (6.6).

### 6.3 `toggle_architecture.md` (new)

**Purpose:** the rules for the EPNM-to-EMS classic-view toggle.

**Outline:**
- Background: the classic-view toggle exists so EPNM users can fall back if the new EMS UI breaks.
- Scope discipline: a forge session converts ONE screen behind the toggle. Never extends the toggle's role beyond fallback.
- What "behind the toggle" means at the routing/feature-flag level (Angular guard, Spring Boot config, Go service flag).
- Forbidden patterns: using the toggle as a long-lived switch for two parallel features; using the toggle to gate partially-converted screens; gating bookmarks behind the toggle (bookmarks are EMS-only — see 6.4).
- Required artifact at Phase 4: `toggle_design.md` showing where the toggle gates the feature, what the fallback path looks like, when the toggle will be removed.

### 6.4 `out_of_poc_scope.md` (new)

**Purpose:** durable list of things every EPNM forge session refuses to do.

**Outline:**
- **Bookmarks data layer fixes** — bookmarks are an EMS-only feature; do not patch the classic-view bookmarks path.
- **Architectural debt fixes** — the POC is a UI conversion; debt cleanup is a separate program of work.
- **DPM (Device Performance Monitoring) features** — out of POC scope entirely.
- **Additional screens beyond the assigned one** — one screen per session, period.
- **Test framework migrations** — use what each repo currently uses; do not introduce new test frameworks.
- **Build tooling changes** — use what each repo currently has; do not modernize tooling.
- For each entry: the rationale, the boundary case ("what if the bookmarks path is literally broken in the screen I'm converting?" — answer: file a separate issue, do not fix in this session), and the artifact in Phase 3 / Phase 5 that re-affirms the boundary.

### 6.5 `label_and_branch_conventions.md` (new)

**Purpose:** codify the Saurav `agentic` label rule and the `agentic UI conversion` branch convention.

**Outline:**
- Issue must carry the `agentic` label before any work begins. Phase 1 verifies and records.
- Branch name: `agentic-ui-conversion-{feature-slug}` per repo touched.
- PR title prefix: `[agentic]` for traceability.
- Why: the Cisco team filters their dashboards by these markers to track AI-generated work separately from human-authored work.
- Verification commands for each.

### 6.6 `pr_description_template.md` (new)

**Purpose:** standard PR description that satisfies both Cisco audit and Phase 8 requirements.

**Outline (the template itself):**
```
## Summary
[1-3 sentences: what changed and why]

## Issue
Closes #NNN. Label: agentic.

## Repos / PRs in this conversion
[Multi-repo: list sibling PRs in other repos]

## What was NOT changed
[Required section. Restate the out-of-scope boundaries respected.]

## Toggle behavior
[How the classic-view toggle is involved, if at all.]

## Test plan
- [ ] Stack-specific test command run
- [ ] Playwright for UI changes
- [ ] Manual verification in classic-view fallback

## Audit-ready commit chain
[Output of `git log --oneline` since base]
```

### 6.7 `memory_load_self_review.md` (new)

**Purpose:** the Set-09 self-review gate. Forces the agent to reflect, before testing, on whether the scope discipline survived the implementation.

**Outline:**
- When invoked: at the start of Phase 7, before any tests run.
- Required prompts the agent must answer in the artifact:
  - Did I touch any file outside the planned `files_being_modified` list?
  - Did I implement any of the `out_of_scope_explicit` items, even partially?
  - Is every commit independently meaningful?
  - Did the toggle scope stay within fallback semantics?
- Output: `phase_07_testing/memory_load_self_review.md`. Required by Stop hook.
- If self-review fails on any line, the agent must surface it to the user and either revert the offending changes or escalate for a scope-amendment decision.

### 6.8 (Optional) `code_style_per_stack.md` (new)

**Purpose:** point at the right linter/formatter per stack rather than restating rules.

**Outline:** Angular 21 → ESLint config in repo, Prettier; Spring Boot → Checkstyle / Spotless; Go → `gofmt`/`golangci-lint`; Postgres SQL → project's existing conventions. One paragraph per stack pointing at the existing config file in the repo. The skill enforces "use what's there", not a new policy.

---

## 7. Self-containment posture

DjangoForge v2 is **fully self-contained** today:

- Both reference files live inside `.claude/skills/django-forge-v2/references/`.
- Both scripts live inside `.claude/skills/django-forge-v2/scripts/`.
- `SKILL.md` references its own files via skill-relative paths.
- Nothing outside the skill folder is required for the skill to function (the Stop hook lives outside, but it implements the contract documented inside the skill — the contract is portable with the skill).

**Conclusion: confirmed self-contained.**

The EPNM forge skill must follow the same convention strictly per the user-memory entry "feedback_skills_self_contained". That means:

- All seven (or eight, including the optional code-style file) new reference files in Section 6 live inside the EPNM skill folder.
- The lifted-and-shifted `agent_teams_usage.md` and `phase_requirements.md` live inside the EPNM skill folder, even if they are nearly identical to DjangoForge's versions. **Do not symlink, do not source-from-elsewhere.** Each skill carries its own copy of every resource.
- Any scripts (e.g., `verify_branch_sync.sh` adapted for multi-repo, a `verify_agentic_label.sh`, an `audit_commit_chain.sh`) live in the EPNM skill's `scripts/` folder, not in a shared skills lib.
- Hooks that enforce the contract live outside the skill (in `.claude/hooks/`) but read from the skill's own reference files — they do not reach into a sibling skill's references.

---

## 8. Summary of what to carry forward

| Take from DjangoForge | Adapt | Add fresh for EPNM |
|----------------------|-------|--------------------|
| `agent_teams_usage.md` (95% verbatim) | Communication-pattern examples; model assignments per role | — |
| `phase_requirements.md` (90% structural) | Stack commands, content checklists, Playwright triggers, state.json schema | — |
| 8-phase workflow | Multi-repo extensions to phases 1, 4, 6, 8 | Memory/load self-review gate in Phase 7 |
| Stop-hook contract pattern | Re-implement against EPNM artifact paths | Audit-ready commit verification |
| State.json critical fields | Add multi-repo, label, toggle, scope fields | — |
| Self-containment convention | — | Strict — own copies of everything |
| — | — | `multi_repo_coordination.md` |
| — | — | `audit_ready_commit_pattern.md` |
| — | — | `toggle_architecture.md` |
| — | — | `out_of_poc_scope.md` |
| — | — | `label_and_branch_conventions.md` |
| — | — | `pr_description_template.md` |
| — | — | `memory_load_self_review.md` |
| — | — | `code_style_per_stack.md` (optional) |

The receiving session should now have enough to scaffold the EPNM forge skill's `references/` folder. Pair this document with files 01-03 in the same directory for the full forge-pattern picture.
