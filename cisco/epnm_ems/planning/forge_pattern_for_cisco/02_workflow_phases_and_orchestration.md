# DjangoForge v2 — Workflow Phases and Orchestration

**Audience:** Claude orchestrator session on the Cisco machine.
**Source skill:** /home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/
**Purpose:** Operational reference for the forge pattern. Pair with the anatomy audit (file 01) and the scripts/hooks deep-dive (file 03).

---

## 0. Orientation

DjangoForge v2 is an 8-phase, hook-enforced workflow that takes a single GitHub issue from "open" to "PR ready for review" without ever working directly on `main`. The workflow is opinionated about three things, and every other rule descends from them:

1. **Phases produce artifacts on disk.** Hooks read the artifacts; the phases cannot lie about being done.
2. **Compaction is a first-class threat.** A `state.json` carries everything the next session needs, and a SessionStart hook re-injects it.
3. **Issue text lies.** Issues are written before merged PRs land. Phase 3 forces a textual reconciliation (`issue_vs_reality.md`) before any planning.

Frontmatter from `SKILL.md`:

> ```yaml
> name: django-forge-v2
> description: |
>   End-to-end Django issue implementation with Agent Teams and enforced compliance via hooks.
>   WHEN to use: User explicitly invokes /django-forge-v2 or says "use django-forge-v2"
>   WHEN NOT to use: Simple questions, research-only tasks, when user invokes /django-forge (v1)
>   Features: 8-phase workflow with hook enforcement, Agent Teams coordination,
>   "Check Previous Phases" pattern that guarantees workflow compliance.
> argument-hint: [issue-number]
> ```

The v1-vs-v2 differentiator table from the source:

> | Aspect | v1 | v2 |
> |--------|----|----|
> | Compliance | Text says "MUST" | Hooks enforce with exit code 2 |
> | Agents | Hierarchical (foreman → workers) | Agent Teams (peer-to-peer) |
> | Context | Lost on compaction | SessionStart hook re-injects |
> | Issue Text | Followed blindly | Issue vs Reality check |
> | Retrieval | Arbitrary "top N" | Recursive chain OR date-based only |

---

## 1. The 8-Phase Workflow in Detail

ASCII map of the pipeline:

```
[gh issue]
    │
    ▼
Phase 1 SETUP ────► worktree, state.json, branch_sync_verified.md
    │
    ▼
Phase 2 DOCS ─────► docs_findings.md (CLAUDE.md + project standards)
    │
    ▼
Phase 3 EXPLORE ──► codebase_state.md, pr_analysis/*.md, issue_vs_reality.md
    │              (this is the v2 "Issue vs Reality" gate)
    ▼
Phase 4 PLAN ─────► task-manifest.md, technical-design.md
    │              (Architect+Engineer for HIGH; Planner for MED/LOW)
    ▼
Phase 5 APPROVAL ─► state.json: user_decisions[plan_approved=true]
    │              (USER INTERACTION POINT — explicit consent)
    ▼
Phase 6 IMPLEMENT ► completed-work/*.md + judge-evaluations/*.md
    │              (Foreman + Workers + Judge in waves)
    ▼
Phase 7 TEST ─────► test_results.md (+ playwright_results/ if UI)
    │
    ▼
Phase 8 GIT ──────► final_commit.md, pr_description.md, PR Ready
                    .active marker removed
```

Each phase below specifies inputs, outputs, agents, scripts, the gate, hooks, and the user-touch surface.

---

### Phase 1 — SETUP

**Produces:**
- `phase_01_setup/issue_fetched.json` — raw `gh issue view` JSON (≥50 chars).
- `phase_01_setup/worktree_created.md` — confirmation note (≥50 chars).
- `phase_01_setup/branch_sync_verified.md` — output of `verify_branch_sync.sh` (≥50 chars).
- `orchestration/state.json` — initialized with issue number, title, worktree path, complexity (LOW/MEDIUM/HIGH), `current_phase: "setup"`.
- A new git worktree at `<repo>-issue-{N}/` (path stored in `state.json.worktree_path`).
- The marker file `.django-forge-v2/.active` (this is what tells skill-scoped hooks to fire).

**Consumes:**
- The CLI argument `[issue-number]`.
- GitHub credentials for `gh issue view`.
- Current state of `origin/<branch>` (must be in sync — `git fetch` + `git rev-list` check).

**Agents:** None. Main session does Phase 1 directly.

**Scripts:**
- `scripts/verify_branch_sync.sh` — runs `git fetch`, then uses `git rev-parse`, `git merge-base`, `git rev-list` to compare local vs remote. Exit code 2 if behind/diverged.
- The skill invokes the separate `git-worktrees-skill` for worktree creation:
  > ```
  > Use the git-worktrees-skill to create worktree for issue {issue_number}
  > ```

**Gate (Stop hook):** all three artifacts above must exist; complexity recorded; `state.json` initialized.

**Hooks active:**
- SessionStart: triggered by `.active` marker → re-injects state if resuming.
- PreToolUse: blocks `sed`, blocks unauthorized Python replace scripts.
- Stop: enforces gate.

**User interaction:** the "Session Start Checklist" requires the orchestrator to *first* ask:
> "Do you have anything to share before we begin? Constraints, preferences, related work?"
> ...then **wait for user** before Phase 2.

---

### Phase 2 — DOCUMENTATION

**Produces:**
- `phase_02_docs/docs_findings.md` (≥100 chars) — must capture:
  - CLAUDE.md patterns extracted
  - Relevant skill documentation identified
  - Project conventions noted
  - Testing requirements identified

**Consumes:** repo root `CLAUDE.md`, any per-app `CLAUDE.md`, design docs, dev_docs (e.g. `dev_docs/git-workflow-requirements.md` is referenced for Draft-PR-early policy).

**Agents:** None for LOW/MEDIUM. Optional documentation explorer subagent for HIGH.

**Scripts:** none.

**Gate:** `docs_findings.md` exists with content >100 chars.

**Hooks:** Stop hook still enforces Phase 1 + Phase 2 artifacts (cumulative — see "Check Previous Phases" §3).

**User interaction:** none required.

---

### Phase 3 — CODEBASE EXPLORATION (the v2 differentiator phase)

**Produces:**
- `phase_03_codebase/codebase_state.md` (≥200 chars) — current state of relevant code.
- `phase_03_codebase/pr_analysis/pr_{N}_review.md` (≥100 chars) — one per related PR.
- `phase_03_codebase/issue_vs_reality.md` (≥200 chars) — the reconciliation document.
- `phase_03_codebase/dependency_chain.md` — records which retrieval method (recursive vs date-based) was used.
- Optional: `gh issue edit {N} --body "..."` if issue text contradicts merged PRs.

**Consumes:**
- The issue body and its referenced PRs.
- The transitive "Depends on #..." graph (recursive) OR all issues since a project epoch (date-based).
- The actual code on the worktree branch.

**Agents:**
- HIGH: spawn explorers as Agent Teams or parallel subagents to read PRs deeply and survey related modules.
- MEDIUM: a single explorer agent.
- LOW: inline exploration in the main session.

**Scripts:** `scripts/trace_dependencies.py` (referenced for the recursive chain method).

**Gate:** all three Phase-3 artifacts must exist with the size minimums above. The Stop hook treats `issue_vs_reality.md` as the most important gate of the workflow.

**Hooks:**
- PreToolUse: blocks "top 50 issues" / arbitrary-N retrievals (rule #3, "No arbitrary retrieval").
- Stop: enforces all Phase 3 artifacts.

**User interaction:** none required, but if the issue is materially out of date the orchestrator may surface the discrepancy and propose the `gh issue edit` rewording before continuing.

The SKILL.md is explicit about why this phase exists:

> **This is the most critical step.** The #1190 session failed because it followed outdated issue text.

---

### Phase 4 — PLANNING

**Produces:**
- `phase_04_planning/task-manifest.md` (≥100 chars) — tasks with unique IDs (`TASK-001`...), dependencies, success criteria, S/M/L sizing.
- `phase_04_planning/technical-design.md` (≥100 chars) — *how* the tasks will be implemented.

**Consumes:** Phase 3 artifacts (especially `issue_vs_reality.md`) and `docs_findings.md`.

**Agents:**
- HIGH: **Architect** (initial breakdown) → **Engineer** (technical detail). Two separate agents, two passes.
- MEDIUM/LOW: a single **Planner** agent producing a combined document.

**Scripts:** none.

**Gate:** `task-manifest.md` exists with parseable tasks; `technical-design.md` exists.

**Hooks:** Stop hook enforces gate; PreToolUse continues to block sed and arbitrary retrievals.

**User interaction:** none in this phase — *but the skill explicitly waits for Phase 5 before any code is written.*

---

### Phase 5 — USER APPROVAL (hard checkpoint)

**Produces:**
- An entry in `state.json.user_decisions`:
  ```json
  {"decision": "plan_approved", "value": true, "timestamp": "..."}
  ```

**Consumes:** the Phase 4 plan + a human-readable summary the orchestrator presents.

**Agents:** none.

**Scripts:** the Stop-hook verifier walks `state["user_decisions"]`:
> ```python
> for decision in state.get("user_decisions", []):
>     if decision.get("decision") == "plan_approved" and decision.get("value"):
>         return True
> ```

**Gate:** the boolean above must be true.

**Hooks:** Stop hook fails the phase if `plan_approved` is missing or false.

**User interaction:** this is *the* approval gate. The summary must include:
- What will be built
- What will NOT be built
- Conflicts / open questions
- Estimated number of tasks + complexity

> **NEVER assume approval. ALWAYS wait for explicit "approved", "yes", "proceed".**

---

### Phase 6 — IMPLEMENTATION

**Produces:**
- `phase_06_implementation/completed-work/{TASK-ID}.md` — one per task.
- `phase_06_implementation/judge-evaluations/judge_evaluation_{TASK-ID}.md` — verdict (APPROVED / NEEDS_REWORK / BLOCKED) per task.
- Real code edits on the worktree branch.
- A **Draft PR** (created after the *first* file edit, per `dev_docs/git-workflow-requirements.md` and Hard Rule #14: "Draft PR early").
- `state.json` updates: `current_wave`, `pending_tasks`, `completed_tasks`.

**Consumes:** the task manifest from Phase 4.

**Agents (HIGH):**
| Agent | Role | Model |
|-------|------|-------|
| Foreman | Coordinator | Opus |
| Code-Worker-1..N | Implementation | Opus |
| Test-Worker | Tests | Sonnet |
| Judge | Quality | Opus |

**Agents (MEDIUM):** Planner (already done), Code-Worker, Judge.
**Agents (LOW):** main session does the work; a Judge pass at the end.

**Scripts:** none directly; agents use Edit / Write / Bash. PreToolUse hook blocks `sed` and unauthorized Python replace scripts (Hard Rules #2 and #4).

**Gate:** every task in `completed_tasks` has a corresponding `judge_evaluation_{TASK-ID}.md` ≥50 chars. Wave N+1 cannot start until **all** Wave N tasks are APPROVED.

**Hooks:**
- PreToolUse: rules #2/#4 above; also blocks `git push` (push is the user's only job).
- Stop: walks `completed_tasks` and matches them to judge files.

**User interaction:** none mid-wave under normal circumstances; orchestrator surfaces blockers.

---

### Phase 7 — TESTING

**Produces:**
- `phase_07_testing/test_results.md` (≥50 chars) — Django test command, pass/fail, root-cause notes for failures, manual verification checklist.
- `phase_07_testing/playwright_results/` — required if any UI/JS/CSS/HTMX changes occurred.

**Consumes:** the implemented code on the worktree branch.

**Agents:** Test-Worker (if Agent Teams) or main session.

**Scripts:** project test commands (e.g. `poetry run python manage.py test app.tests`); Playwright runner.

**Gate:** `test_results.md` shows pass.

**Hooks:** Stop hook enforces. PreToolUse continues to allow normal commands.

**User interaction:** if tests fail, orchestrator may need to loop back into Phase 6 (rework) before re-attempting Phase 7.

---

### Phase 8 — GIT OPERATIONS

**Produces:**
- `phase_08_git/final_commit.md` (≥50 chars) — final commit message + hash.
- `phase_08_git/pr_description.md` (≥50 chars) — full PR description text.
- The Draft PR is **converted to Ready for review** (`gh pr ready`), unless the user prefers to keep it draft.
- The `.django-forge-v2/.active` marker is removed.
- `state.json.workflow_complete = true`.

**Consumes:** the implementation on the worktree, the issue, and the existing Draft PR (created back in Phase 6).

**Agents:** none.

**Scripts:** `gh pr edit`, `gh pr ready`, `git commit`, `git add`. **Not** `git push` — that's reserved for the user (Hard Rule #15).

**Gate:** PR is in Ready state, linked to issue, with description and test plan.

**Hooks:**
- PreToolUse: still blocks `git push` from Claude.
- Stop: confirms artifacts and clears `.active`.

**User interaction:**
1. Claude completes the commit(s).
2. Claude provides the push command:
   > ```
   > Ready to push. Run this command:
   > cd /path/to/worktree && git push -u origin branch-name
   > Let me know when pushed, and I'll create the PR.
   > ```
3. Claude **waits** for user confirmation.
4. Claude runs `gh pr create` (or `gh pr ready` if Draft).

---

## 2. The Agent Teams Pattern

### What it is

Agent Teams is an experimental Claude Code feature gated by:

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

It enables **peer-to-peer collaboration** between agents. Quoting the source:

> Instead of strict hierarchical communication (Foreman → Workers → Report back), agents can:
> - Message each other directly
> - Share a task list with dependency tracking
> - Provide feedback without going through a coordinator
> - React to completed work in real-time

### How it differs from the older hierarchical foreman/worker pattern

The contrast table from `agent_teams_usage.md`:

> | Aspect | Hierarchical (Legacy) | Agent Teams (Default) |
> |--------|----------------------|----------------------|
> | Communication | Through Foreman | Direct peer-to-peer |
> | Task Assignment | Foreman assigns | Shared task list |
> | Feedback Loop | Worker → Foreman → Judge → Foreman → Worker | Worker ↔ Judge directly |
> | Coordination | Central control | Distributed |
> | Token Usage | Lower | Higher |
> | Parallelism | Limited by Foreman | True parallel |

Legacy mode (still selectable via `--legacy`) flows like this:

> ```
> Orchestrator
>     ↓
> Foreman (spawned)
>     ↓
> Workers (spawned by Foreman)
>     ↓
> Report back to Foreman
>     ↓
> Foreman presents to Judge
>     ↓
> Judge evaluates
>     ↓
> Foreman coordinates next wave
> ```

### How peer-to-peer coordination works in this skill

A shared task list lives in `state.json` (or a sibling file) with a status enum (`pending` / `in_progress` / `completed` / `approved` / `rework`) and a `depends_on` list. All agents read and write the same list. Two example interactions from the source:

**Worker→Worker handoff:**

> ```
> Worker-1: "TASK-001 complete. Created GroupConverter class at
>           integrations/jobdiva/search/group_converter.py.
>           Key methods: convert_to_groups(), handle_nested()."
> Worker-2: "Acknowledged. Starting TASK-002 which depends on TASK-001.
>           Will use GroupConverter.handle_nested() for my implementation."
> ```

**Judge→Worker rework (no Foreman in the loop):**

> ```
> Judge: "Reviewing TASK-002...
>         VERDICT: NEEDS_REWORK
>         Issues:
>         - Missing null check on line 45
>         - Method name doesn't follow convention
>         Required changes:
>         1. Add null check before accessing group.children
>         2. Rename process_group() to _process_group() (private method)"
> Worker-2: "Acknowledged. Implementing required changes..."
> ```

**Wave discipline still applies:** even with peer-to-peer, Wave N+1 cannot start until every task in Wave N has Judge verdict `APPROVED`. The skill enforces this via `state.json.current_wave` and the Phase 6 Stop-hook gate.

---

## 3. The "Check Previous Phases" Enforcement Pattern

This is the spine of v2.

### Where it lives

- **In SKILL.md** — Hard Rule #1: *"Hooks enforce compliance — Every phase produces artifacts. Stop hook verifies ALL previous phases complete."*
- **In hooks** — a Stop hook (skill-scoped via the `.django-forge-v2/.active` marker) walks the `phase_NN_*` directories on every Stop event and validates artifacts against `references/phase_requirements.md`.
- **In scripts** — `verify_branch_sync.sh` is the Phase-1-specific check; the Stop hook calls into shared verifier logic that reads `state.json` and checks files-on-disk.

### What is checked

The Stop hook is **cumulative**: at the end of Phase N it verifies Phases 1..N. Each phase declares:

- A list of required files with minimum sizes (the `references/phase_requirements.md` table).
- A list of required `state.json` fields (e.g., `complexity`, `current_phase`, `user_decisions[plan_approved]`).
- A list of derived assertions (e.g., `worktree_path` exists on the filesystem; every `completed_tasks` entry has a matching `judge_evaluation_{TASK-ID}.md`).

The verification snippet for Phase 5 from the source:

> ```python
> for decision in state.get("user_decisions", []):
>     if decision.get("decision") == "plan_approved" and decision.get("value"):
>         return True
> ```

The Phase 6 verification snippet:

> ```python
> completed_tasks = state.get("completed_tasks", [])
> judge_dir = session_dir / "phase_06_implementation" / "judge-evaluations"
> for task in completed_tasks:
>     eval_file = judge_dir / f"judge_evaluation_{task}.md"
>     if not eval_file.exists():
>         return f"Missing judge evaluation for {task}"
> ```

### Failure mode when a phase is skipped

- The Stop hook **exits with code 2**, which Claude Code surfaces as a blocking error message back into the conversation.
- The error names the missing artifact and the phase that owns it.
- Claude is forced to backtrack and produce the artifact before any further tool use is allowed.
- For Phase 1 specifically, `verify_branch_sync.sh` exits 2 if the branch is behind/diverged, refusing to let Phase 1 close until the user pulls/rebases.

The `.django-forge-v2/.active` marker is the *scoping mechanism*: hooks check for the marker before activating, so non-forge sessions are not affected.

---

## 4. The Issue vs Reality Check (v2's flagship guard)

### What it is

A required Phase 3 artifact (`phase_03_codebase/issue_vs_reality.md`) that explicitly compares the issue body — written at some past moment — against the *current* state of the codebase, including PRs that have merged in the meantime. Without this artifact, Phase 4 cannot start.

### When it runs

Inside Phase 3 (CODEBASE EXPLORATION), after the orchestrator has read every related PR's diff into `pr_analysis/pr_{N}_review.md`.

### What it produces

The required template (quoted from SKILL.md):

> ```markdown
> # Issue vs Reality Check
>
> ## Issue Text Says:
> [Quote the issue description]
>
> ## Current Reality:
> [What the codebase actually looks like now]
> [Which PRs have been merged since issue was written]
>
> ## Discrepancies:
> [List any contradictions]
>
> ## Rationalization:
> [What we will ACTUALLY build based on reality, not outdated text]
> ```

### How it changes phase behavior

- If the issue text and reality agree: planning proceeds normally.
- If they conflict: the orchestrator may run `gh issue edit {N} --body "..."` to correct the issue, with session notes explaining the rewrite. The Phase 4 plan is built from `Rationalization`, **not** from the original issue body.
- The Phase 5 user-approval summary explicitly cites the discrepancies so the user knows we deliberately diverged from the literal issue text.

### Why it exists

> **This is the most critical step.** The #1190 session failed because it followed outdated issue text.

The v1-vs-v2 table calls this out as "Issue Text — Followed blindly (v1) → Issue vs Reality check (v2)."

---

## 5. GitHub Issue Handling

### How the issue is specified

Via the slash-command argument: `/django-forge-v2 [issue-number]`.
The frontmatter declares `argument-hint: [issue-number]`.

### What metadata is read

Phase 1 calls:

```bash
gh issue view {issue_number} --json number,title,state,body,assignees,labels
```

The result is parked in `phase_01_setup/issue_fetched.json`. Fields used downstream:

- `number`, `title` — populate `state.json` and the eventual PR.
- `body` — the source for the Issue vs Reality check in Phase 3.
- `labels` — influence complexity heuristics (e.g., a `breaking-change` or `migration` label nudges toward HIGH).
- `assignees` — informational; recorded in state.
- (Implicit) `Depends on #...` lines in the body — feed the recursive dependency tracer.

### Recursive-chain vs date-based retrieval

This is rule #3 ("No arbitrary retrieval"). Quoting:

> **NEVER use arbitrary limits like "top 50 issues".**
>
> **Method 1: Recursive Chain**
> ```
> Issue #1190 says "Depends on #1185"
>   → Read #1185
>   → #1185 says "Depends on #905"
>     → Read #905
>     → #905 has no dependencies (root)
> Result: Read issues 905, 1185, 1190 in that order
> ```
>
> **Method 2: Date-Based**
> ```
> Project epoch: 2026-01-01 (when Search Architecture started)
> → Read all issues created after this date
> ```
>
> Document which method was used in `phase_03_codebase/dependency_chain.md`.

`scripts/trace_dependencies.py` automates Method 1.

### How the issue is closed / marked complete

DjangoForge v2 does **not** close the issue itself. It links the PR to the issue (e.g., `Closes #123` in the PR body). Closure happens automatically when the PR merges. Phase 8's `pr_description.md` carries the linkage.

---

## 6. Worktree Usage

### When created

Phase 1, Step 1.2 — *before* anything else touches files.

### Naming convention

`<repo>-issue-{N}` (the SKILL.md example shows `/home/user/talent_ai-issue-123`).

### Where it lives

A sibling of the main repo (not inside it). `state.json.worktree_path` records the absolute path so parallel sessions can be matched to their worktrees.

### Why mandatory

Hard Rule #7: *"Worktrees mandatory — Always create worktree. Never work on main."*
Hard Rule #8 nuances this: *"Session folder on main — `.django-forge-v2/issue-{N}/` in main repo, not worktree."* The session/orchestration artifacts stay on `main` so they survive worktree teardown and so multiple worktrees can share them.

### How it's created

The skill delegates to a separate skill:

> ```
> Use the git-worktrees-skill to create worktree for issue {issue_number}
> ```

…and writes a confirmation to `phase_01_setup/worktree_created.md`.

### Cleanup

Two scenarios:
- **Workflow completes** — Phase 8 removes `.active`, sets `workflow_complete: true`. The worktree may be cleaned up by `git-worktrees-skill` or kept for follow-up work.
- **User aborts** — `.active` is removed; `state.json` is preserved (so the workflow can be resumed); the worktree is retained for later resume or manual cleanup.

### If a worktree already exists

The session is matched to it via `state.json.worktree_path`; the orchestrator reuses the worktree rather than creating a duplicate. This is critical for parallel sessions:

> **Note:** `worktree_path` is critical for parallel sessions. Each session is matched to its worktree, allowing multiple issues to be worked on simultaneously in different worktrees.

---

## 7. PR Creation

### When the PR gets created

**Twice.**

1. **Draft PR** — created **after the first file edit in Phase 6** (Hard Rule #14: "Draft PR early"). This is per `dev_docs/git-workflow-requirements.md`. The Draft PR exists for the entire implementation phase so reviewers can watch progress.
2. **Ready for review** — Phase 8 converts Draft → Ready via `gh pr ready`.

### PR metadata

- **Title:** typically `Issue #{N}: {issue_title}` (or repo convention).
- **Body:** the contents of `phase_08_git/pr_description.md`, which includes:
  - What changed and why
  - Test plan
  - `Closes #{issue_number}` linkage
  - Notes from `issue_vs_reality.md` if the implementation deliberately diverged from the issue body
- **Labels:** carried over from the issue where appropriate.
- **Linked issue:** via `Closes #{N}` (auto-close on merge).
- **Base branch:** the project default (typically `main`); the worktree branch is the head.
- **Draft initially:** yes (per Hard Rule #14).

### Automation against the PR

CI is project-defined (Django tests, lint, etc.). The skill itself runs no extra automation against the PR after creation; reviewer assignment is left to the user / GitHub CODEOWNERS.

### How the push/PR handoff works (Hard Rule #15)

> **Claude does ALL git ops except push.** ... User says "pushed" or similar → Claude creates PR with `gh pr create`.

---

## 8. Plan-Mode Usage

DjangoForge v2 uses Claude Code's plan-mode mechanism implicitly at one place: **Phase 5 (User Approval)**.

- **Entered:** at the end of Phase 4, when the orchestrator presents the plan summary (what will be built, what will not, conflicts, complexity, task count).
- **Exited:** only when the user gives explicit approval ("approved", "yes", "proceed"). The orchestrator records `{"decision": "plan_approved", "value": true}` in `state.json.user_decisions` and proceeds to Phase 6.
- **What is in plan mode:** the summary, the conflicts list, the open questions. No code edits.
- **What is in auto mode:** Phases 1–4 are executable without plan mode (subject to the gates), Phases 6–8 are auto after approval.

The Phase 1 "Session Start Checklist" also has a plan-mode-like behavior: the orchestrator asks for context up front and *waits* before exploration.

---

## 9. End-to-End Run Example

User runs:

```
/django-forge-v2 1452
```

Step-by-step trace:

```
[T+00:00] Orchestrator session starts.
          SessionStart hook checks for .django-forge-v2/.active — absent, skip re-injection.
          Skill activated.

[T+00:01] Orchestrator: "Do you have anything to share before we begin?"
          USER INTERACTION → user provides context (or says "no").

──────── Phase 1: SETUP ────────

[T+00:02] Run: gh issue view 1452 --json number,title,state,body,assignees,labels
          Save → phase_01_setup/issue_fetched.json
[T+00:03] Invoke git-worktrees-skill → creates /home/user/talent_ai-issue-1452
          Write phase_01_setup/worktree_created.md
[T+00:04] Run scripts/verify_branch_sync.sh → exit 0 (branch in sync).
          Write phase_01_setup/branch_sync_verified.md
[T+00:05] Create .django-forge-v2/issue-1452/ tree.
          Initialize orchestration/state.json with complexity=HIGH (multi-file feature).
          Touch .django-forge-v2/.active.
[T+00:06] Stop hook fires → checks Phase 1 artifacts → PASS. Phase 1 closes.

──────── Phase 2: DOCS ────────

[T+00:07] Read CLAUDE.md, app-level CLAUDE.md, dev_docs/*, design specs.
          Write phase_02_docs/docs_findings.md (CLAUDE.md patterns, conventions, test setup).
[T+00:09] Stop hook → PASS.

──────── Phase 3: CODEBASE EXPLORATION ────────

[T+00:10] Issue body says "Depends on #1407, #1377, #1356".
          Run scripts/trace_dependencies.py → recursive chain: 1356 → 1377 → 1407 → 1452.
          Write phase_03_codebase/dependency_chain.md (method=recursive).
[T+00:12] AGENT TEAMS SPAWN (HIGH):
          - Explorer-1: read PR #1356 diff
          - Explorer-2: read PR #1377 diff
          - Explorer-3: read PR #1407 diff
          - Surveyor: map current state of integrations/jobdiva/search/
          Each writes phase_03_codebase/pr_analysis/pr_{N}_review.md.
[T+00:18] Surveyor writes phase_03_codebase/codebase_state.md.
[T+00:19] Orchestrator reconciles: issue body still references the OLD class name
          (CandidateHybridSearch), but PR #1377 renamed everything to JobDivaCandidateSearch.
          Write phase_03_codebase/issue_vs_reality.md.
[T+00:20] Run gh issue edit 1452 --body "..." (with corrected class names).
          Append note to issue_fetched.json change-log.
[T+00:21] Stop hook → PASS (codebase_state, pr_analysis/*, issue_vs_reality all present).

──────── Phase 4: PLANNING ────────

[T+00:22] AGENT SPAWN: Architect (Opus). Produces initial 6-task breakdown.
[T+00:26] AGENT SPAWN: Engineer (Opus). Adds technical detail, dependency edges,
          success criteria, S/M/L sizing.
[T+00:30] Write phase_04_planning/task-manifest.md (TASK-001..TASK-006).
          Write phase_04_planning/technical-design.md.
[T+00:31] Stop hook → PASS.

──────── Phase 5: USER APPROVAL ────────

[T+00:32] Orchestrator presents:
          - WILL BUILD: Boolean group UI on JobDivaCandidateSearch
          - WILL NOT BUILD: changes to CandidateHybridSearch (deprecated)
          - 6 tasks, complexity HIGH, ~3 waves
          - Conflicts: issue text was outdated (corrected via gh issue edit)
[T+00:33] USER INTERACTION → user replies "approved".
[T+00:33] Append {"decision": "plan_approved", "value": true} to state.json.
[T+00:33] Stop hook → PASS.

──────── Phase 6: IMPLEMENTATION ────────

[T+00:34] Foreman spawns Wave 1:
          - Code-Worker-1 → TASK-001 (no deps)
          - Code-Worker-2 → TASK-002 (no deps)
[T+00:35] Code-Worker-1 makes first Edit → orchestrator runs gh pr create --draft.
          Draft PR #1453 created, linked to issue #1452.
[T+00:42] Code-Worker-1 finishes TASK-001 → writes completed-work/TASK-001.md.
          Judge → APPROVED → judge-evaluations/judge_evaluation_TASK-001.md.
[T+00:44] Code-Worker-2 finishes TASK-002 → writes completed-work/TASK-002.md.
          Judge → NEEDS_REWORK (missing null check).
[T+00:45] Code-Worker-2 (peer-to-peer) acknowledges, fixes, resubmits.
          Judge → APPROVED.
[T+00:46] Wave 1 complete (all APPROVED). Foreman starts Wave 2.
          - Code-Worker-1 → TASK-003 (deps: 001)
          - Code-Worker-2 → TASK-004 (deps: 002)
          - Test-Worker → TASK-005 (deps: 001, 002)
[T+01:00] Wave 2 complete. Wave 3: TASK-006 (deps: 003,004,005).
[T+01:08] All tasks APPROVED. Stop hook → PASS (every completed_task has judge_evaluation_*.md).

──────── Phase 7: TESTING ────────

[T+01:09] Run: poetry run python manage.py test integrations.jobdiva
          → 47 tests, 47 passing.
          Write phase_07_testing/test_results.md.
[T+01:11] UI changed → run Playwright suite.
          Save screenshots to phase_07_testing/playwright_results/.
[T+01:14] Stop hook → PASS.

──────── Phase 8: GIT OPERATIONS ────────

[T+01:15] Final commit: orchestrator stages files, commits with proper message
          (no AI attribution, references issue #1452).
          Write phase_08_git/final_commit.md.
[T+01:16] Update Draft PR description via gh pr edit.
          Write phase_08_git/pr_description.md.
[T+01:17] Orchestrator: "Ready to push. Run: cd /home/user/talent_ai-issue-1452 && git push -u origin issue-1452"
          USER INTERACTION → user pushes, replies "pushed".
[T+01:18] Run: gh pr ready 1453 (Draft → Ready).
[T+01:18] Remove .django-forge-v2/.active.
          Set state.json.workflow_complete = true.
[T+01:18] Stop hook → final pass. Workflow complete. PR #1453 ready for review.
```

---

## 10. Adaptation Guidance for Cisco EPNM-to-EMS

The Cisco engagement is Angular + Java across **14 repositories**, with a single shared `agentic UI conversion` branch on each repo. Here is what transfers, what needs adaptation, and what may need additional phases.

### Transfers cleanly

| Element | Why it transfers |
|---------|------------------|
| Issue → branch → work → PR → close | GitHub-native; the workflow is repo-agnostic. |
| `.<skill-name>/.active` marker for hook scoping | Mechanism is independent of language. |
| `state.json` with compaction-survival fields | Same problem on any long-running engagement. |
| SessionStart re-injection hook | Same. |
| Stop hook + `references/phase_requirements.md` table | Same. |
| Recursive dependency-chain retrieval | GitHub feature, not Django. |
| Issue vs Reality check | Even more important on a 14-repo conversion where source-of-truth drifts fast. |
| Worktree usage and naming | Pure Git. Naming becomes `<repo>-issue-{N}` per repo. |
| Draft PR early + Ready at Phase 8 | Pure GitHub. |
| Phase 5 user-approval gate | Domain-agnostic. |
| Agent Teams pattern (Foreman / Workers / Judge / Test-Worker) | Useful for any large multi-file change. |
| Wave discipline | Same logic; tasks have dependencies regardless of stack. |
| Hard Rule #15 (Claude does all git ops except push) | Carry over verbatim. |

### Needs adaptation (Django-specific bits)

| Django element | Cisco replacement |
|----------------|-------------------|
| `manage.py test` in Phase 7 | `mvn test` / `gradle test` for Java; `ng test` / `karma` / `jest` for Angular. The `test_results.md` template stays; the command list changes. |
| Django ORM model-reading guidance ("Models before queries") | Replace with: "Read EPNM's existing Java service interfaces and Angular component contracts before writing client code." |
| HTMX/Phoenix theme awareness | N/A. Replace with Cisco's UI design system / EMS component library guidance. |
| `dev_docs/git-workflow-requirements.md` reference | Point to Cisco's equivalent process doc (or write one). |
| CLAUDE.md patterns scope | Each of the 14 repos likely needs its own CLAUDE.md, or a top-level multi-repo CLAUDE.md. |
| Playwright trigger ("any template/JS/CSS/HTMX change") | Trigger on any Angular `.html` / `.ts` / `.scss` change. |
| `verify_branch_sync.sh` | Keep as-is; works on any Git repo. |
| `trace_dependencies.py` | Keep; pure GitHub. |

### May need additional phases

The Cisco engagement has structural realities Django Forge does not handle:

1. **Multi-repo coordination phase (new Phase 1.5 or pre-Phase 1).**
   A single issue may span several of the 14 repos. Need a phase that:
   - Identifies which repos are touched.
   - Verifies the `agentic UI conversion` branch is current on each.
   - Creates one worktree per repo.
   - Tracks all repos in `state.json.repos[]`.
   The current `worktree_path` field becomes `worktree_paths[]`.

2. **Cross-repo PR coordination (extends Phase 8).**
   If a change touches Angular + Java + a shared library, Phase 8 must:
   - Open one Draft PR per repo.
   - Cross-link them in each PR body ("Companion PR: org/repo-x#123").
   - Coordinate "Ready" conversion (typically the dependency PR goes Ready first).
   - Decide a merge order.

3. **Cisco-specific compliance phase (between Phase 7 and Phase 8).**
   For an enterprise client, there may be:
   - Static analysis gates (Coverity, SonarQube).
   - License-scan / SBOM requirements.
   - Internal security review labels.
   - Mandatory commit-message footers (Jira links, Cisco bug IDs).
   This belongs as `Phase 7.5: COMPLIANCE` with its own artifact (`compliance_results.md`).

4. **Memory / load review gate (the "Set 09" gate Colin mentioned).**
   For a long-lived engagement, a periodic memory/load review prevents drift. Place between Phase 5 and Phase 6 for HIGH-complexity tickets:
   - Re-read `state.json.critical_learnings`.
   - Check whether new project-level learnings (from prior tickets) modify the plan.
   - Surface anything that should bounce the plan back to the user.

5. **Angular/Java agent specialization.**
   Replace generic `Code-Worker` with role-specialized workers:
   - `Angular-Worker` (Sonnet or Opus) — `.ts`, `.html`, `.scss`, RxJS.
   - `Java-Worker` (Opus) — Spring services, REST endpoints, JPA entities.
   - `Contract-Worker` (Opus) — keeps the Angular/Java interface honest (DTOs, OpenAPI).
   - `Test-Worker` (Sonnet) — split into `Karma-Worker` and `JUnit-Worker` if volume warrants.

### Recommended forge structure for Cisco

```
Phase 0: REPO MAP (new) ────► repos_touched.md, per-repo branch_sync
Phase 1: SETUP ─────────────► worktree per repo, state.json with repos[]
Phase 2: DOCS ──────────────► CLAUDE.md per repo + cross-repo design docs
Phase 3: EXPLORE ───────────► issue_vs_reality across repos
Phase 4: PLAN ──────────────► task manifest with repo column
Phase 5: APPROVAL ──────────► (unchanged, but plan summary lists repos)
Phase 5.5: MEMORY GATE (new)─► critical_learnings replay
Phase 6: IMPLEMENT ─────────► Angular/Java/Contract Workers, per-repo Draft PRs
Phase 7: TEST ──────────────► mvn + ng test per repo
Phase 7.5: COMPLIANCE (new)─► Coverity/Sonar/license scans, Jira footers
Phase 8: GIT ───────────────► coordinate Ready on N PRs in dependency order
```

That structure preserves every v2 invariant (artifact gates, Issue vs Reality, peer-to-peer agents, draft-PR-early, Hard Rule #15) while accommodating multi-repo and enterprise reality.

---

## 11. Files in the Source Skill

- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/SKILL.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/references/phase_requirements.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/references/agent_teams_usage.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/verify_branch_sync.sh`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/trace_dependencies.py`

Pair this document with file `01_anatomy_audit.md` (skill file inventory) and file `03_scripts_and_hooks_deep_dive.md` (the verifier internals) when designing the Cisco forge.
