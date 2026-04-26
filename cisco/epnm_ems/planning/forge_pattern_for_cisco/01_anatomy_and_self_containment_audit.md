# DjangoForge v2 — Anatomy and Self-Containment Audit

**Audience:** Claude orchestrator session on the Cisco machine, planning to recreate a forge-pattern skill for the EPNM engagement.
**Source skill:** /home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/
**Purpose:** Structural reference for adaptation, not tutorial.

---

## 1. Executive Summary

DjangoForge v2 is a Claude Code skill that orchestrates an **8-phase, gate-driven workflow** for taking a single GitHub issue from "fetched" to "PR ready for review" inside a Django/Python codebase. The defining characteristics are:

- **Phase gates enforced by hooks**, not by prose. Stop hook verifies artifacts; PreToolUse hook blocks forbidden operations (`sed`, arbitrary `top-N` retrieval, unapproved Python replace scripts); SessionStart hook re-injects context after compaction.
- **Worktree-mandatory** — every issue gets its own worktree; never works on main.
- **Session folder lives on main repo** (`.django-forge-v2/issue-{N}/`), not in the worktree, so artifacts survive worktree teardown.
- **Marker-file activation pattern** — `.django-forge-v2/.active` toggles whether the skill-scoped hooks fire. All three hook scripts gate on this marker.
- **State.json is the survival mechanism** — full context lives in JSON so SessionStart can re-inject after compaction.
- **Agent Teams (peer-to-peer) is the default**, with a `--legacy` flag for hierarchical Foreman→Worker→Judge orchestration.
- **Issue-vs-Reality discipline** — Phase 3 mandates a written comparison between what the issue says and what the code currently looks like, because issue text goes stale as related PRs merge.
- **Git split** — Claude does add/commit/branch/PR-create; user does ONLY push.

The critical structural finding for adaptation: **DjangoForge v2 is NOT self-contained by the modern 2026 convention.** Its hooks are scripts in `.claude/hooks/` (a sibling of `skills/`), and they are wired up via `settings.local.json` rather than via SKILL.md frontmatter. There is also one external skill dependency (`git-worktrees-skill`). See section 4.

---

## 2. SKILL.md Frontmatter (Verbatim)

The entire YAML frontmatter is short:

```yaml
---
name: django-forge-v2
description: |
  End-to-end Django issue implementation with Agent Teams and enforced compliance via hooks.

  WHEN to use: User explicitly invokes /django-forge-v2 or says "use django-forge-v2"
  WHEN NOT to use: Simple questions, research-only tasks, when user invokes /django-forge (v1)

  Features: 8-phase workflow with hook enforcement, Agent Teams coordination,
  "Check Previous Phases" pattern that guarantees workflow compliance.
argument-hint: [issue-number]
---
```

That is the entire frontmatter. **There are no `hooks:` declarations, no `allowed-tools:`, no `model:` field, no `disable-model-invocation:`, no `metadata:` block.** Just `name`, `description`, and `argument-hint`.

### Implication: hooks are defined elsewhere

The body of SKILL.md repeatedly references hooks ("Stop hook verifies", "PreToolUse hook blocks", "SessionStart hook re-injects") but does not declare them in frontmatter. They are wired up at the **project settings level**, in `/home/cmoore/programming/talent_ai/.claude/settings.local.json`, and the scripts live at the **project hooks level**, in `/home/cmoore/programming/talent_ai/.claude/hooks/`. See the self-containment audit (section 4) for full detail.

This means a session on the Cisco machine that wants to recreate the same enforcement pattern using the **modern self-contained convention** must move the hook declarations into SKILL.md frontmatter and the hook scripts into a `hooks/` subdirectory under the new skill folder.

---

## 3. Folder Structure

```
/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/
├── SKILL.md                              (~13 KB, the orchestration playbook)
├── references/
│   ├── agent_teams_usage.md              (~7 KB, Agent Teams mode reference)
│   └── phase_requirements.md             (~7.5 KB, per-phase artifact spec)
└── scripts/
    ├── trace_dependencies.py             (~6 KB, executable)
    └── verify_branch_sync.sh             (~2.5 KB, executable)
```

### File-by-file purpose

- **SKILL.md** — The full 8-phase playbook. Contains: hard rules, activation procedure, phase-by-phase steps, Agent Teams composition tables, dependency tracing rules, state.json schema, session-start checklist, and the git operations rule.

- **references/agent_teams_usage.md** — Reference for the Agent Teams (peer-to-peer) mode. Documents the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` env var requirement, agent composition tables for HIGH/MEDIUM/LOW complexity, the shared task-list JSON shape, communication patterns (worker↔worker, worker↔judge), wave execution rules, and `--legacy` mode.

- **references/phase_requirements.md** — The artifact-gate specification. For each of the 8 phases, lists: required artifact paths, minimum size in characters, content requirements, and verification logic. This is what the Stop hook reads when deciding whether to allow progress to the next phase.

- **scripts/verify_branch_sync.sh** — Bash script invoked at Phase 1 step 1.3. Runs `git fetch`, compares `HEAD` to `@{upstream}` via `git merge-base` and `git rev-list`, exits 0 if branch is current or ahead, exits 2 if behind or diverged. The exit code 2 is the standard Claude Code hook contract for "block this action."

- **scripts/trace_dependencies.py** — Python script implementing the two permitted dependency-tracing methods: recursive chain (parses `Depends on #X`, `Blocked by #X`, `After #X`, `Requires #X`, `Prerequisite: #X` from issue body via `gh issue view`) and date-based (`gh issue list --search "created:>YYYY-MM-DD"`). Used to enforce the rule that "top 50 issues" is forbidden.

### What is NOT in the skill folder

The skill folder contains no:

- `hooks/` subdirectory
- Hook scripts (the three `django-forge-v2-*` scripts live one directory up, in `.claude/hooks/`)
- `templates/` for boilerplate state.json or artifact files
- `agents/` subdirectory or sub-agent definitions for Foreman/Worker/Judge
- `settings.json` or per-skill config
- README.md or installation notes
- Tests for the scripts
- The `.active` marker location is created at runtime in the project root, not stored in the skill

---

## 4. Self-Containment Audit (Critical Section)

### 4.1 Are hooks defined in SKILL.md frontmatter?

**No.** The frontmatter is minimal (name, description, argument-hint). The skill body refers to hooks as if they exist, but their registration is external.

### 4.2 Where are the hooks actually defined?

In `/home/cmoore/programming/talent_ai/.claude/settings.local.json` under the `"hooks"` key. The settings file currently registers these project-wide hooks (none of them django-forge-v2 specific):

```json
"hooks": {
  "PreCompact": [{"hooks": [{"type": "command", "command": ".../precompact_export.sh", "timeout": 30}]}],
  "Stop": [
    {"hooks": [{"type": "command", "command": ".../context_warning.sh", "timeout": 5}]},
    {"hooks": [{"type": "command", "command": "python3 .../stop_self_reflection.py", "timeout": 5}]}
  ],
  "PreToolUse": [
    {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 .../git-push-intercept.py", "timeout": 10}]},
    {"matcher": "Bash", "hooks": [{"type": "command", "command": ".../block_ephemeral_file_patterns.sh", "timeout": 10}]},
    {"matcher": "Bash", "hooks": [{"type": "command", "command": ".../block_ai_attribution.sh", "timeout": 10}]}
  ]
}
```

**Important nuance:** the three skill-specific hook scripts `django-forge-v2-pretooluse.py`, `django-forge-v2-sessionstart.sh`, and `django-forge-v2-stop.py` exist as files in `.claude/hooks/` but are **NOT registered in settings.local.json** at the moment of this audit. So either:

- they were registered previously and de-registered, or
- they were intended to be registered globally but currently are not, or
- there is another `settings.json` (project-level, not local) that registers them and was not visible in this filesystem snapshot.

Either way: the design intent is clear — these hooks are skill-scoped at runtime by checking for the `.django-forge-v2/.active` marker file, and they live in the **project hooks directory**, not the **skill directory**.

### 4.3 Skill-scoping mechanism (the "marker file" pattern)

Each of the three hook scripts opens with a comment like:

> Skill-scoped: Only fires when .django-forge-v2/.active marker exists.

So the hooks are technically global (registered project-wide) but exit early if the marker file is absent. The skill creates `.django-forge-v2/.active` on activation and removes it on completion or abort.

This is how DjangoForge v2 simulates "skill-attached hooks" without having actual frontmatter-declared hooks. It is **not** how 2026 self-contained skills are supposed to work — modern skills declare hooks directly in SKILL.md frontmatter so the hook is scoped to the skill's lifecycle automatically.

### 4.4 Hook script anatomy (each script is OUTSIDE the skill folder)

The three skill-supporting hook scripts live at:

- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-pretooluse.py`
  - **Trigger:** PreToolUse on Bash (assumed, based on script content)
  - **Purpose:** Blocks `sed` commands, blocks unapproved Python replace scripts, blocks "top N" arbitrary retrieval patterns
  - **Skill-scope check:** exits early if `.django-forge-v2/.active` not present in the main repo
  - **Status message on block:** exit code 2 with stderr explanation

- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-sessionstart.sh`
  - **Trigger:** SessionStart with `source == "compact"`
  - **Purpose:** Re-inject context from `state.json` after compaction so the workflow can resume coherently
  - **Skill-scope check:** exits 0 if `source != "compact"`, then again if marker absent
  - **Behavior:** reads state.json, prints critical fields (`what_we_are_building`, `what_we_are_NOT_building`, `current_phase`, `critical_learnings`, `pending_tasks`) to stdout for re-ingestion

- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-stop.py`
  - **Trigger:** Stop
  - **Purpose:** "Check Previous Phases" enforcement — verifies all previous phases have their required artifacts (per `references/phase_requirements.md`) before allowing the session to stop or progress
  - **Skill-scope check:** exits 0 if marker file absent
  - **Block mechanism:** exit code 2 with message naming the missing artifact

None of these scripts are in the skill folder. **All three are deviations from the self-contained convention.**

### 4.5 Are scripts inside the skill folder?

**Partially.** The two non-hook scripts (`verify_branch_sync.sh`, `trace_dependencies.py`) live at `skills/django-forge-v2/scripts/` and are properly self-contained. Only the **hook** scripts are outside.

### 4.6 Are references inside the skill folder?

**Yes, fully.** Both `agent_teams_usage.md` and `phase_requirements.md` are in `skills/django-forge-v2/references/`. The phase_requirements file is the source of truth for what artifacts the Stop hook checks — but the hook script that does the checking lives outside, so the contract between hook and reference is implicit (and the hook would need to know the path to the skill's references/ if it consumes them; from inspection of `django-forge-v2-stop.py` first 30 lines, the hook appears to encode artifact requirements directly, so the reference doc is documentation rather than runtime data).

### 4.7 External skill dependencies

DjangoForge v2 invokes another skill in Phase 1 step 1.2:

> Use the git-worktrees-skill to create worktree for issue {issue_number}

This is a **cross-skill dependency**. By the modern convention, every skill must contain its own copy of every resource it uses. To self-contain this, the recreated skill on the Cisco side either:

- imports the worktree-creation logic as a script under its own `scripts/` directory, or
- inlines the worktree-creation steps directly in SKILL.md, or
- accepts the cross-skill dependency and explicitly bundles `git-worktrees-skill` alongside.

### 4.8 Self-containment scorecard

| Component | Self-contained? | Notes |
|---|---|---|
| SKILL.md | Yes | In skill folder |
| references/ | Yes | In skill folder |
| Non-hook scripts | Yes | In skill folder |
| Stop hook | **No** | Lives in `.claude/hooks/`, registered in settings.local.json |
| PreToolUse hook | **No** | Same as above |
| SessionStart hook | **No** | Same as above |
| Hook registration | **No** | In `settings.local.json`, not in SKILL.md frontmatter |
| Worktree creation | **No** | Delegated to `git-worktrees-skill` |
| Activation marker | N/A | Created/removed at runtime in main repo, not a static asset |
| Agent definitions (Foreman/Worker/Judge) | N/A | Spawned ad hoc via prompt; no agent files |

Net assessment: **roughly 60% self-contained.** The skill body and supporting reference/script assets are in the right place, but the entire enforcement layer (hooks) and the worktree-creation step are external.

---

## 5. Dependency Map (What the Skill Assumes Exists)

### 5.1 Tooling

- **`git`** — for `fetch`, `rev-parse`, `merge-base`, `rev-list`, `worktree`, `branch`, `add`, `commit`
- **`gh`** (GitHub CLI) — for `issue view`, `issue list`, `issue edit`, `pr create`, `pr edit`. Authenticated against the talent_ai GitHub repo.
- **`bash`** (verify_branch_sync.sh uses `set -euo pipefail`)
- **`python3`** (trace_dependencies.py)
- **`poetry`** — Phase 7 `test_results.md` examples show `poetry run python manage.py test`
- **Standard Unix tools** — `cat`, basic shell

### 5.2 Environment

- **`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`** — must be set in the shell before launching Claude Code, otherwise Agent Teams mode silently degrades to hierarchical (with a warning)

### 5.3 Repository / project conventions

- **Single GitHub repo** — the skill assumes one upstream repo for both issues and PRs
- **Issues are numbered** — referenced as `#N` throughout
- **Issue body conventions** — dependency syntax `Depends on #X`, `Blocked by #X`, `After #X`, `Requires #X`, `Prerequisite: #X`
- **Branch naming** — implied by git-worktrees-skill, not specified here
- **Project epoch date** — `2026-01-01` cited as the Search Architecture epoch for date-based dependency tracing; this is talent_ai-specific
- **CLAUDE.md exists at repo root** — Phase 2 reads it for project standards
- **`dev_docs/git-workflow-requirements.md`** — referenced in Hard Rule #14 ("Draft PR early"); a document the team maintains
- **Working directory layout** — Phase 1.4 creates `.django-forge-v2/issue-{N}/` in the **main repo**, not the worktree; this is a deliberate split

### 5.4 Project-specific systems referenced

- **Django ORM, manage.py, migrations** — Phase 7 testing assumes Django test runner
- **Phoenix theme** — referenced via the `phoenix-theme-skill` dependency in the broader project (DjangoForge v1 description mentions it; v2 inherits the assumption that UI work uses Phoenix components and HTMX)
- **HTMX** — described as preferred over JavaScript in v1 description; v2 inherits the convention
- **Specific module paths in state.json examples** — `integrations/jobdiva/search/group_converter.py`, `recruitment/candidates/services/hybrid_search.py`. These are talent_ai code paths and are illustrative only.

### 5.5 Skill dependencies (other Claude Code skills)

- **`git-worktrees-skill`** — invoked in Phase 1.2 to create a worktree for the issue. **This is the only hard cross-skill dependency.**

### 5.6 Dependencies that are NOT assumed

- No CI system assumptions
- No specific cloud provider assumptions (Azure/GCP/AWS)
- No database schema assumptions (the django-database-query-skill exists separately)
- No specific test framework beyond Django's built-in test runner + optional Playwright
- No specific code-formatter or linter

---

## 6. Django-Specific vs. Framework-Agnostic Components

This is the most important section for adaptation. The receiving session is building an Angular/Java EPNM equivalent, so the skill needs to be split into "keep" and "replace" buckets.

### 6.1 Framework-agnostic (KEEP, possibly with light edits)

| Component | Why it's portable |
|---|---|
| The 8-phase workflow shape | Setup → Docs → Codebase → Plan → Approve → Implement → Test → Git is generic to any code-change flow |
| Phase-gate enforcement via Stop hook | Hook contract (exit code 2 to block) is harness-level, not language-level |
| `verify_branch_sync.sh` | Pure git, no language tie-in |
| `trace_dependencies.py` | Pure GitHub API + regex, language-agnostic |
| Issue-vs-Reality discipline | Universal pattern; relevant any time issue text can drift from code |
| Worktree-mandatory rule | Pure git pattern |
| Session folder on main repo, not worktree | Pure git pattern |
| `.active` marker activation pattern | Pure filesystem; hook scoping is harness-level |
| State.json schema (most fields) | Generic; only specific path examples are Django-coded |
| Agent Teams composition (Foreman / Code-Worker / Test-Worker / Judge) | Roles are generic to any code-implementation effort |
| `--legacy` hierarchical fallback | Generic |
| Wave execution with dependency tracking | Generic |
| Recursive dependency chain via `Depends on #X` parsing | Generic GitHub convention |
| Date-based dependency tracing | Generic |
| Git operations split (Claude does all but push) | Generic policy |
| User-approval gate before implementation (Phase 5) | Generic |
| Judge evaluations per task | Generic |
| Dependency-trace-only retrieval rule (no "top 50 issues") | Generic discipline |
| PreToolUse blocking pattern (block sed, block unapproved replace scripts) | Generic, though specific blocked commands may differ per stack |

### 6.2 Django/Python-specific (REPLACE for EPNM)

| Component | What to replace it with for EPNM (Angular frontend, Java backend) |
|---|---|
| `poetry run python manage.py test` (Phase 7) | Maven/Gradle test runner for Java side; `ng test` / Karma / Jest for Angular side |
| Django ORM / models / migrations references | Java persistence layer (JPA / Hibernate / MyBatis — depends on EPNM stack); Angular services for frontend state |
| "Models before queries" rule (from v1 description) | Equivalent: read DTOs / entities / API contracts before writing query/service code |
| Phoenix theme / HTMX preferences | Replace with Angular component library / design system used by EMS (e.g., Angular Material, PrimeNG, or the EMS-specific component kit) |
| Django test patterns | JUnit / Mockito for Java; Jasmine / Karma / Jest / Playwright for Angular |
| `dev_docs/git-workflow-requirements.md` reference | Cisco / EPNM equivalent project-standards doc, if one exists; otherwise inline the rules |
| Specific code path examples in state.json (`integrations/jobdiva/...`) | Replace with EPNM module paths once known |
| `python -m py_compile` (in settings.local allowlist) | Java compile / Angular build invocations |
| `phoenix-theme-skill`, `django-database-query-skill` references | EMS-equivalent skills if they exist, or remove the references |
| Project epoch date (`2026-01-01`) | EPNM-engagement-specific epoch |

### 6.3 Convention-shift items (KEEP the pattern, MOVE the location)

These are the items that should be kept structurally but relocated to comply with the modern self-contained convention:

| Current location (DjangoForge v2) | Modern location (recreated skill) |
|---|---|
| Hook scripts in `.claude/hooks/django-forge-v2-*.{py,sh}` | Hook scripts in `.claude/skills/<skill-name>/hooks/*.{py,sh}` |
| Hook registration in `settings.local.json` | Hook declarations in SKILL.md frontmatter under a `hooks:` key |
| Worktree creation delegated to `git-worktrees-skill` | Either inline the worktree commands in SKILL.md, or copy the worktree script into the new skill's `scripts/` directory |
| Activation marker pattern (`.django-forge-v2/.active` + scope-check at top of every hook script) | If hooks are declared in frontmatter, the harness handles skill-scoping automatically and the marker pattern becomes unnecessary |

---

## 7. The "Check Previous Phases" Pattern (Worth Calling Out)

This is the single most important enforcement mechanism in DjangoForge v2 and is what differentiates v2 from v1. It works as follows:

1. Every phase produces required artifacts at known paths (specified in `references/phase_requirements.md`).
2. The Stop hook fires whenever the session would otherwise stop or wait for input.
3. The Stop hook reads `state.json` to determine the current phase, then verifies that **every prior phase's artifacts exist and meet the minimum size threshold**.
4. If any artifact is missing or under-sized, the hook exits with code 2 and the harness blocks the stop, forcing Claude to keep working until the artifact exists.
5. This makes "I'll skip Phase 3 and go straight to planning" structurally impossible — the Stop hook will refuse to let the session settle until Phase 3 artifacts are present.

For the EPNM recreation, this pattern is fully portable. The artifact list per phase will need to be retuned (e.g., "issue_vs_reality.md" might become something different for EPNM-style work where there may not be GitHub issues at all), but the pattern is keep-as-is.

---

## 8. State.json — The Survival Mechanism

The state.json file is critical because it is what the SessionStart hook reads after compaction to re-establish the agent's mental model. The full schema (from SKILL.md verbatim):

```json
{
  "issue_number": 123,
  "issue_title": "...",
  "worktree_path": "/home/user/talent_ai-issue-123",
  "complexity": "HIGH",
  "current_phase": "implementation",
  "completed_phases": ["setup", "docs", "codebase", "planning", "approval"],
  "what_we_are_building": "Boolean group UI for JobDivaCandidateSearch",
  "what_we_are_NOT_building": "CandidateHybridSearch modifications",
  "files_being_modified": ["integrations/jobdiva/search/group_converter.py"],
  "files_NOT_to_touch": ["recruitment/candidates/services/hybrid_search.py"],
  "critical_learnings": [
    "Issue text was OUTDATED - written before PRs 1356/1377/1407 merged"
  ],
  "user_decisions": [{"decision": "plan_approved", "value": true}],
  "related_prs": [1356, 1377],
  "current_wave": 2,
  "pending_tasks": ["TASK-004"],
  "completed_tasks": ["TASK-001", "TASK-002", "TASK-003"],
  "agent_mode": "teams"
}
```

Two design notes worth carrying forward:

- The **negative-space fields** (`what_we_are_NOT_building`, `files_NOT_to_touch`) are as important as the positive-space fields. They prevent scope creep and protect adjacent code from incidental edits during reworks.
- The **`critical_learnings` array** captures lessons mid-flight (e.g., "issue text was outdated") so they survive compaction. This is genuinely valuable and is one of the more clever pieces of v2's design.

For the EPNM recreation, the state.json schema should be retained almost verbatim. Only `worktree_path` (which is repo-name-specific in its example) and the file-path examples need to change.

---

## 9. Hard Rules Summary (15 Rules, Verbatim Themes)

DjangoForge v2 codifies 15 hard rules. Grouped:

**Enforcement (1-6):** Hooks enforce compliance with exit code 2; no `sed`; no arbitrary "top N" retrieval; no Python replace scripts without permission; Issue-vs-Reality artifact required before planning; branch must be current.

**Workflow (7-10):** Worktrees mandatory; session folder lives on main; Agent Teams default with `--legacy` flag for hierarchical; state.json survives compaction.

**Quality (11-14):** Judge evaluates every task (HIGH complexity); tests before git; explicit user approval; draft PR early.

**Git (15):** Claude does ALL git operations except push; user does ONLY push.

For the EPNM recreation, all 15 are portable in spirit. Specifics like "no sed" should be reviewed against the EPNM stack — sed is a generic concern, but the EPNM equivalent might add things like "no manual XML edits to spring-config.xml without approval" or "no raw npm install without lockfile review."

---

## 10. Activation Procedure (How a Session Starts)

From SKILL.md "Session Start Checklist":

1. **Ask for context** — "Do you have anything to share before we begin? Constraints, preferences, related work?"
2. **Create worktree** (invoke git-worktrees-skill)
3. **Create session folder** on main repo (not worktree)
4. **Create marker file** `.django-forge-v2/.active`
5. **Verify branch is current** (run `verify_branch_sync.sh`)
6. **Wait for user** before proceeding to exploration

Notably, step 1 is a hard "ask first" gate — even with auto-mode, the skill expects a context-collection turn before any work begins.

For the EPNM recreation, the equivalent step 1 should be retained. EPNM work is likely to involve more upfront constraint collection than typical Django issue work (network device specifics, EMS module boundaries, etc.).

---

## 11. Notable Omissions / Things the Skill Does NOT Do

- **No automated PR-merge.** The skill creates and updates the PR but never merges. Merge is a human decision.
- **No automated dependency updates.** The skill doesn't run `poetry update` or similar.
- **No automated rebase/conflict resolution.** If the branch diverges, the skill blocks (exit code 2 from `verify_branch_sync.sh`) and tells the user to `git pull --rebase`.
- **No MCP integrations.** The skill is pure CLI (gh, git, python). No MCP tool calls are wired in.
- **No agent persistence.** Foreman / Worker / Judge are spawned per-session and have no memory across sessions; only state.json persists.
- **No automated rollback.** If implementation goes badly, the recovery is "tell the user, let them decide."

---

## 12. Recommendations for the EPNM Recreation

Based on this audit, the receiving Claude session on the Cisco machine should consider the following when invoking SkillForge:

1. **Make hooks self-contained from day one.** Declare them in SKILL.md frontmatter, not in `settings.json`. Put the hook scripts in `<skill-folder>/hooks/`.

2. **Inline or duplicate the worktree-creation script.** Don't take a cross-skill dependency on a separate worktree skill unless that skill is also bundled.

3. **Drop the `.active` marker pattern.** With frontmatter-declared hooks, the harness scopes hooks automatically and the marker becomes redundant.

4. **Keep the 8-phase shape.** Setup → Docs → Codebase → Plan → Approve → Implement → Test → Git is the right shape for any non-trivial code-change flow, and the EPNM-to-EMS conversion is a long sequence of many such flows.

5. **Replace Django artifacts with Angular/Java equivalents in `phase_requirements.md`.** The artifact contract is what the Stop hook enforces, so getting it right at this layer is high-leverage.

6. **Retain Issue-vs-Reality discipline even if EPNM work is not strictly issue-driven.** The pattern generalizes to "spec-vs-reality" or "ticket-vs-reality." For UI conversion work, this becomes "old-screen-vs-new-screen" — explicitly documenting what the legacy EPNM UI does versus what the new EMS UI must do is structurally identical.

7. **Retain state.json with negative-space fields.** `what_we_are_NOT_building` and `files_NOT_to_touch` are unusually valuable for UI-conversion work, where it is easy to over-edit adjacent components.

8. **Decide upfront on the agent-teams story.** If the Cisco machine doesn't have `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` enabled or if Cisco's environment policy disallows experimental flags, build the skill in hierarchical-default mode and skip the Agent Teams branching.

9. **Replace the `dev_docs/git-workflow-requirements.md` reference with whatever Cisco's equivalent is** — or inline the workflow expectations directly into SKILL.md.

10. **Consider whether GitHub is even the right issue source.** If EPNM work is tracked in Cisco's own ticketing system (Jira / Cisco internal), the `gh issue view` calls become Jira API calls, and the dependency-tracing patterns shift accordingly. The recursive-chain regex `Depends on #X` may need to become `Depends on EPNM-1234` or similar.

---

## 13. Quick-Reference File Map

For the receiving session, here are the absolute paths to the source-of-truth files in the DjangoForge v2 skill:

- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/SKILL.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/references/agent_teams_usage.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/references/phase_requirements.md`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/verify_branch_sync.sh`
- `/home/cmoore/programming/talent_ai/.claude/skills/django-forge-v2/scripts/trace_dependencies.py`

And the **out-of-skill** files that the receiving session should be aware are NOT in the skill but are part of the system:

- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-pretooluse.py`
- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-sessionstart.sh`
- `/home/cmoore/programming/talent_ai/.claude/hooks/django-forge-v2-stop.py`
- `/home/cmoore/programming/talent_ai/.claude/settings.local.json` (where project-level hooks are registered, though the django-forge-v2 hooks are not currently registered in this snapshot)

These four files would all be folded into the recreated skill folder under the modern self-contained convention.

---

## 14. One-Sentence Summary

DjangoForge v2 is a worktree-mandatory, marker-file-activated, 8-phase orchestration skill whose enforcement layer (hook scripts + settings.local.json registration) lives outside the skill folder and whose only true cross-skill dependency is `git-worktrees-skill` — making it ~60% self-contained by 2026 standards, and the EPNM recreation should preserve the workflow shape and state.json schema while moving all hooks into `<skill>/hooks/` declared via SKILL.md frontmatter, replacing Django/Phoenix/HTMX-specific bits with Angular/Java equivalents, and inlining or bundling any worktree-creation logic.
