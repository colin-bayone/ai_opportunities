---
name: django-forge
description: |
  End-to-end Django issue implementation with async sub-agents. Use when working on GitHub issues
  that require code implementation. This skill coordinates exploration, planning, and a multi-agent
  implementation swarm (Architect, Engineer, Foreman, Workers, Judge) to deliver high-quality code.

  Key features:
  - Never assumes - always asks for user feedback and input
  - Models before queries - always reads models before writing query code
  - HTMX over JavaScript - prefers OOB swaps or WebSockets
  - Phoenix theme awareness - uses Phoenix components for UI
  - Research capability - searches for current best practices (date-aware)
  - Library freshness validation - only uses maintained libraries (1 year + v1.0+)
  - Multi-agent implementation with quality gates
---

# Django Forge Skill

## ⚠️ CRITICAL: READ THIS ENTIRE SKILL BEFORE PROCEEDING ⚠️

**STOP. Before doing ANYTHING with this skill, you MUST:**

1. **Read this entire SKILL.md file from start to finish**
2. **Understand the complete workflow and all phases**
3. **Understand that WORKTREES ARE MANDATORY - there is NO alternative**

**Why this matters:** This skill coordinates complex multi-phase work across multiple files.
Skipping steps, taking shortcuts, or not understanding the full workflow WILL cause problems
that are difficult to recover from (lost work, branch conflicts, mixed changes).

**WORKTREES ARE NON-NEGOTIABLE:**
- Every issue implementation MUST use a git worktree
- Working on a branch in the main directory is a **complete violation of protocol**
- This enables parallel work across multiple Claude sessions without conflicts
- Even "simple" issues require worktrees - complexity is not the deciding factor

If you proceed without reading this skill completely, or without creating a worktree first,
you are setting up the user for failure. Do not do this.

---

## ⚠️ CORE PURPOSE: MULTI-AGENT ARCHITECTURE ⚠️

**This skill exists to coordinate PARALLEL ASYNC SUB-AGENTS.**

You MUST invoke sub-agents for:
- **Exploration**: `docs-explorer`, `model-explorer`, `view-explorer`, `template-explorer`, `test-explorer`
- **Planning**: `architect` + `engineer` (HIGH complexity) or `planner` (MEDIUM/LOW)
- **Implementation**: `foreman` → spawns `code-worker` and `test-worker` agents
- **Quality**: `judge` evaluates EVERY completed task

**If you are doing exploration, planning, or implementation yourself instead of spawning agents, you are VIOLATING this skill.**

The speed and quality benefits come from:
1. Parallel agent execution (multiple explorers run simultaneously)
2. Specialized agents with focused prompts
3. Quality gates enforced by the Judge agent

DO NOT skip agent invocation because "it's faster to do it directly." That defeats the entire purpose.

---

## Overview

This skill provides end-to-end implementation for Django GitHub issues using a coordinated multi-agent system. It emphasizes user involvement, thorough exploration, and quality-gated implementation.

## When to Use This Skill

Use proactively when:
- User mentions "work on issue #X" or "implement issue #X"
- User has a GitHub issue that needs coding
- User wants to implement a feature or fix a bug
- The `/django-issue` slash command is invoked

## Hard Rules

### Implementation Rules

1. **NEVER write query code without reading models first**
   - Model exploration MUST complete before any QuerySet code
   - Understand relationships, field types, constraints

2. **HTMX over JavaScript**
   - Use OOB swaps for dynamic updates
   - Use WebSockets (Channels) for real-time features
   - JavaScript only for Phoenix theme requirements

3. **No scope creep**
   - Stay focused on the issue
   - If additional work needed, suggest new issues
   - Don't "improve" unrelated code

4. **Service layer pattern**
   - Business logic in services/, not views
   - Views handle HTTP concerns only
   - Services are testable and reusable

5. **Phoenix theme for UI**
   - Use Phoenix components from catalog
   - Follow Font Awesome 5 icons (not FA6)
   - No custom CSS when Phoenix has it

### User Interaction Rules

6. **Never assume - always ask**
   - When requirements unclear, ask user
   - When multiple valid approaches, present options with pros/cons
   - When conflicts found, surface to user

7. **Max 3 questions per message**
   - Don't overwhelm with questions
   - Group related questions together
   - Prioritize blocking questions

8. **Checkpoint before major actions**
   - Get approval before implementation starts
   - Verify each major task completion with user
   - Confirm PR creation

9. **Sequential presentation for complex items**
   - Don't dump all information at once
   - Present phase by phase for complex issues
   - Wait for user acknowledgment before proceeding
   - Break down long explanations into digestible chunks

10. **User override capability**
    - All major decisions shown to user with option to override
    - Architect/Engineer vs Planner choice can be overridden
    - Explorer selection can be overridden
    - Complexity assessment can be overridden
    - Transparency is key - explain WHY a decision was made

### Research Rules

11. **Current date context**
    - Always get current date before research
    - Include year in search terms (e.g., "Django HTMX 2026")
    - Verify information freshness

12. **Library freshness**
    - Must be updated within 1 year of current date
    - Must have version >= 1.0.0
    - Check before recommending ANY third-party library
    - Run: `python .claude/skills/django-forge/scripts/check_library_freshness.py`

13. **Don't reinvent solved problems**
    - For common patterns (auth, pagination, caching), check Django built-ins first
    - For solved problems, check well-maintained libraries second
    - Custom implementations are perfectly fine for business logic and features
    - The goal: avoid rewriting what's already been done well, not avoid custom code

### Quality Rules

14. **Test everything**
    - Run existing tests after changes
    - Write new tests for new code
    - Manual testing before PR

15. **Follow existing patterns**
    - Match project coding style
    - Use existing utilities (get_logger, services, etc.)
    - Reference best practices docs

16. **SOC2 compliance**
    - Audit logging for sensitive operations
    - PII handled properly
    - Access control enforced
    - No sensitive data in logs

17. **Code completeness**
    - No truncated implementations ("// ... rest of code")
    - No hacky workarounds without user approval
    - Idempotent operations where applicable
    - DRY principle - no code duplication

---

## Session Start Protocol

**CRITICAL:** Before starting any work on an issue, ALWAYS:

1. **Ask user for context first**
   ```
   "Before we begin, do you have anything you'd like to share?
   - Any context about this issue?
   - Constraints or preferences?
   - Related work in progress?"
   ```

2. **Ask about git push permissions**
   ```
   "Who should handle git push operations?
   - Me (Claude) - I'll push directly
   - You (User) - I'll provide push commands for you to run"
   ```
   **Store this answer and follow it for ALL push operations throughout the session.**
   If user handles pushes: provide one-liner commands and WAIT for confirmation before continuing.

3. **Create worktree BEFORE any code changes** (MANDATORY)

   **HARD RULE: NEVER create/modify code files on main branch. ALWAYS create a worktree FIRST.**

   Invoke the `git-worktrees-skill` to create the worktree for this issue.

   ```
   "I'll create a git worktree for this issue using the git-worktrees-skill."
   ```

   **Why worktrees are mandatory:**
   - Multiple Claude sessions can work simultaneously without conflicts
   - Branch switching in a shared directory causes lost work and merge nightmares
   - Even "simple" or "quick" issues can conflict with parallel work
   - The cost of creating a worktree is trivial; the cost of NOT using one is high

   **Create the worktree BEFORE any exploration or implementation.**

   **IMPORTANT:** After creating the worktree, continue working in the SAME Claude session.
   All subsequent file operations (Write, Edit, Read) should use the worktree path.
   Do NOT ask the user to start a new Claude session - the skill continues in the current session.

4. **Worktree permissions are pre-configured**

   The main repo's `.claude/settings.local.json` has wildcard permissions for all worktrees:
   ```
   Read/Write/Edit(//home/cmoore/programming/talent_ai-*/**)
   ```
   No additional permissions file needed in the worktree.

5. **Create session folder** (always required)

   Create the session folder structure (see Phase 1, Step 1.4 for full structure):
   ```
   .django-forge/issue-{number}/
   ├── orchestration/
   ├── exploration/
   ├── implementation/
   ├── testing/
   └── git/
   ```
   This can be created in main before the worktree, or inside the worktree after creation.

6. **Draft PR after first file edit** (per git-workflow-requirements.md)

   **IMMEDIATELY after the first file is edited**, open a Draft PR:
   ```bash
   gh pr create --draft --title "WIP: Issue #{number} - {brief description}" \
     --body "Work in progress for #{number}. Draft PR opened per workflow requirements."
   ```

   This is required by `docs/git-workflow-requirements.md` - see "Step 6: Open Draft PR".

7. **Wait for user input before proceeding**
   - Don't assume and start exploring
   - User may have critical context
   - User may want to adjust approach

---

## Workflow Phases

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 1: Session Setup                                                  │
│   - Get current date context                                            │
│   - Fetch issue from GitHub                                             │
│   - Create worktree (MANDATORY - see Session Start Protocol)            │
│   - Create .claude/settings.local.json if worktree (optional)           │
│   - Create .django-forge/issue-{number}/ session folder                 │
│   - Initialize state tracking                                           │
│   - Determine issue complexity (HIGH/MEDIUM/LOW)                        │
│   - Draft PR after first file edit (per git-workflow-requirements.md)   │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 2: Documentation Exploration (docs-explorer agent - Sonnet)       │
│   - Read CLAUDE.md and project standards                                │
│   - Find relevant documentation                                         │
│   - Extract patterns and conventions                                    │
│   - Identify related best practices docs                                │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 3: Codebase Exploration (PARALLEL agents - Opus)                  │
│   Smart selection based on issue type:                                  │
│   - model-explorer: Django models (ALWAYS for DB-related issues)        │
│   - view-explorer: Views, services, URLs                                │
│   - template-explorer: Templates, forms, UI (for UI issues)             │
│   - test-explorer: Existing tests, patterns                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 4: Planning (HYBRID - based on complexity)                        │
│                                                                         │
│   HIGH complexity: Architect → Engineer (separate agents)               │
│   MEDIUM/LOW:      Planner (combined agent)                             │
│                                                                         │
│   Output: task-manifest.md, technical-design.md, success-criteria.md    │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 5: User Approval Checkpoint                                       │
│   - Present plan summary to user                                        │
│   - Surface any conflicts or questions                                  │
│   - Present options with pros/cons for decisions                        │
│   - Get EXPLICIT approval before proceeding                             │
│   - Options: Approve / Revise / Ask Questions / Abort                   │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 6: Implementation Swarm                                           │
│                                                                         │
│   FOREMAN coordinates:                                                  │
│   ├── Wave 1: Independent tasks (parallel Workers)                      │
│   ├── Wave 2: Dependent tasks (parallel where possible)                 │
│   └── Wave N: Integration tasks                                         │
│                                                                         │
│   JUDGE evaluates each completed task:                                  │
│   ├── APPROVED → Next wave                                              │
│   ├── REWORK_REQUIRED → Back to Worker with feedback                    │
│   └── BLOCKED → Escalate to user (always)                               │
│                                                                         │
│   Worker models: Opus for code, Sonnet for tests/docs                   │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 7: Testing & Verification                                         │
│   - Run Django tests                                                    │
│   - Execute manual testing checklist                                    │
│   - Fix any failures (return to Phase 6 if needed)                      │
│   - Final quality check                                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 8: Git Operations & PR Finalization                               │
│   - Stage and commit final changes                                      │
│   - Update Draft PR description (branch/PR created in Phase 1)          │
│   - Convert Draft PR to Ready for Review                                │
│   - Final review with user                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Session Setup

### Step 1.1: Get Current Date Context

```bash
python .claude/skills/django-forge/scripts/get_current_date.py
```

This provides:
- Current date for time-aware searches
- Library freshness cutoff date
- Search term suggestions

### Step 1.2: Fetch Issue from GitHub

```bash
gh issue view {issue_number} --json number,title,state,body,assignees,labels
```

Parse and extract:
- Issue number and title
- Full description and requirements
- Current state (open/closed)
- Labels for complexity hints

### Step 1.3: Determine Issue Complexity

**HIGH complexity** → Full agent swarm
- Multiple files/modules affected
- Database schema changes
- Both frontend and backend work
- New feature implementation
- Complex business logic
- Integration with external systems

**MEDIUM complexity** → Single explorer + lightweight planning
- Single feature area
- Modifications to existing patterns
- Template/UI changes only
- Service layer additions

**LOW complexity** → Direct exploration + inline planning (NO agents)
- Bug fixes
- Small tweaks
- Follow-up issues to existing work
- Documentation updates
- Test additions

### Step 1.3b: Check for Follow-Up Issues

If the issue references a parent issue (e.g., "Depends on #905", "Part 2 of #XXX"):
1. Check if parent issue is merged
2. Read the parent's implementation to understand what exists
3. This often means the current issue is LOW complexity even if it looks bigger

### Step 1.3c: Adaptive Workflow by Complexity

**⚠️ CRITICAL: The workflow ADAPTS based on complexity. Do NOT use sledgehammer for thumbtack.**

| Complexity | Exploration | Planning | Implementation |
|------------|-------------|----------|----------------|
| **LOW** | Direct Glob/Grep/Read (NO agents) | Inline in conversation | Direct coding |
| **MEDIUM** | Single Explore agent | Planner agent (haiku) | Direct coding |
| **HIGH** | Full parallel explorer swarm | Architect + Engineer (opus) | Foreman + Workers |

### Step 1.4: Create Session Folder

```
.django-forge/issue-{number}/
├── orchestration/
│   └── state.json
├── exploration/
│   ├── docs_findings.md
│   ├── models_findings.md
│   ├── views_findings.md
│   ├── templates_findings.md
│   └── tests_findings.md
├── implementation/
│   ├── task-manifest.md
│   ├── technical-design.md
│   ├── success-criteria.md
│   ├── task-log.json
│   ├── completed-work/
│   ├── judge-evaluation.md
│   └── rework-queue.json
├── testing/
│   ├── test_results.md
│   └── manual_checklist.md
└── git/
    ├── git_state.md
    └── pr_description.md
```

### Step 1.5: Initialize State

Create `orchestration/state.json`:

```json
{
  "session_id": "<uuid>",
  "issue_number": 123,
  "issue_title": "Issue title",
  "complexity": "HIGH",
  "created_at": "<ISO timestamp>",
  "current_phase": "setup",
  "completed_phases": [],
  "user_decisions": [],
  "last_activity": "<ISO timestamp>"
}
```

---

## Phase 2: Documentation Exploration

**Adapt based on complexity:**

### For LOW Complexity
Skip the docs-explorer agent. Instead, directly read:
```
Read CLAUDE.md (if not already in context)
```
That's it. Don't spawn an agent for a 50-line bug fix.

### For MEDIUM Complexity
Quick targeted read:
```
Read CLAUDE.md
Glob for any docs matching the feature area (e.g., docs/*location*, docs/*search*)
```

### For HIGH Complexity
Invoke the `docs-explorer` agent:
```
Task(subagent_type="docs-explorer", model="sonnet", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}
  Explore project documentation and output findings to exploration/docs_findings.md
")
```

---

## Phase 3: Codebase Exploration

**Adapt based on complexity:**

### For LOW Complexity
**DO NOT spawn explorer agents.** Use direct tools:

```
# Find the specific files you need to modify
Glob for files matching the issue area (e.g., "**/location*.js", "**/search*.html")
Read the specific files identified
Grep for specific functions/classes mentioned in the issue
```

For follow-up issues, read the parent issue's implementation:
```
# If issue #906 depends on #905, find what #905 added
Grep for "Issue #905" or "issue-905" in recent commits
Read those files directly
```

This should take < 5 tool calls, not 50k tokens.

### For MEDIUM Complexity
Use a **single** Explore agent with targeted scope:

```
Task(subagent_type="Explore", model="haiku", prompt="
  Find files related to {specific feature area}.
  Focus on: {2-3 specific things to find}
  Keep exploration brief - just identify the key files.
")
```

### For HIGH Complexity
Invoke explorer agents **in parallel** based on issue type:

| Issue Type | Invoke These Explorers |
|------------|---------------------|
| Database/Model changes | model-explorer (required), view-explorer, test-explorer |
| API/Backend only | model-explorer (required), view-explorer, test-explorer |
| UI/Template changes | view-explorer, template-explorer, test-explorer |
| Full-stack feature | ALL explorers |

```
Task(subagent_type="model-explorer", model="opus", prompt="...")
Task(subagent_type="view-explorer", model="opus", prompt="...")
Task(subagent_type="template-explorer", model="opus", prompt="...")
Task(subagent_type="test-explorer", model="opus", prompt="...")
```

═══════════════════════════════════════════════════════════════════════════════
**CHECKPOINT: BEFORE PHASE 4**

For LOW: □ Did you identify the files to modify using Glob/Grep/Read?
For MEDIUM: □ Did you run ONE targeted Explore agent?
For HIGH: □ Did you invoke the relevant explorer agents IN PARALLEL?

IF UNCHECKED: STOP. Complete exploration before proceeding.
═══════════════════════════════════════════════════════════════════════════════

---

## Phase 4: Planning

**Adapt based on complexity:**

### For LOW Complexity
**DO NOT spawn a planner agent.** Plan inline in the conversation:

```
Based on my exploration, here's the plan:

**Files to modify:** {list 1-3 files}
**Changes needed:**
1. {specific change}
2. {specific change}

**Approach:** {1-2 sentences}

Do you approve?
```

That's it. No task-manifest.md, no technical-design.md for a 40-line change.

### For MEDIUM Complexity
Use a lightweight planner:

```
Task(subagent_type="planner", model="haiku", prompt="
  Issue: #{issue_number} - {issue_title}
  Files identified: {list from exploration}

  Create a brief implementation plan (keep it concise).
")
```

### For HIGH Complexity
**Step 4.1:** Invoke the `architect` agent:
```
Task(subagent_type="architect", model="opus", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}
  Read exploration findings and create task-manifest.md and success-criteria.md
")
```

**Step 4.2:** After Architect completes, invoke the `engineer` agent:
```
Task(subagent_type="engineer", model="opus", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}
  Review Architect output and create technical-design.md
")
```

---

## Phase 5: User Approval Checkpoint

**CRITICAL: Never proceed without explicit user approval**

Present to user:
1. Task summary (what will be done)
2. Technical approach (how it will be done)
3. Any conflicts or questions found
4. Options with pros/cons for decisions

Ask user to choose:
- **Approve** - Proceed to implementation
- **Revise** - Modify plan based on feedback
- **Ask Questions** - Clarify before deciding
- **Abort** - Cancel workflow

Update `state.json` with user decision.

---

## Phase 6: Implementation

**Adapt based on complexity:**

### For LOW Complexity
**DO NOT spawn Foreman/Workers/Judge.** Just write the code directly:

```
Edit the identified files
Write the code changes
Run syntax check: python -m py_compile {file}
```

For a 40-line change, you don't need a swarm. Just make the edit.

### For MEDIUM Complexity
Write the code directly. Use Judge only if the changes are substantial:

```
# Make the changes directly
Edit {file1}
Edit {file2}

# Optional: Quick self-review
# If changes are > 100 lines, consider a quick Judge check
```

### For HIGH Complexity
Use the full Foreman → Workers → Judge swarm:

**Step 6.1:** Invoke the `foreman` agent to orchestrate implementation:

```
Task(subagent_type="foreman", model="opus", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}

  Read task-manifest.md and coordinate implementation waves.
  Spawn worker agents in parallel for each wave.
  Track progress in implementation/task-log.json
")
```

The Foreman will:
1. Parse task-manifest.md for execution plan
2. Determine wave order based on dependencies
3. Spawn Workers in parallel (up to 10)
4. Collect completed work to `implementation/completed-work/<task-id>.md`

**Step 6.2:** Invoke the Judge for EACH Completed Task

**CRITICAL: After each wave completes, invoke the `judge` agent.**

```
Task(subagent_type="judge", model="opus", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}

  Evaluate completed tasks in implementation/completed-work/
  against success-criteria.md.

  For each task, return: APPROVED, REWORK_REQUIRED, or BLOCKED
  Write evaluation to implementation/judge-evaluation.md
")
```

**DO NOT proceed to Phase 7 until Judge has evaluated ALL tasks.**

### Judge Verdicts

- **APPROVED** - Task meets all success criteria → proceed
- **REWORK_REQUIRED** - Issues found → send back to Worker with feedback
- **BLOCKED** - Cannot proceed → escalate to user immediately

### Loop Prevention

- Max 3 rework iterations per task
- If task still fails after 3 attempts → escalate to user

**ALL blocked tasks go to user for decision.**

═══════════════════════════════════════════════════════════════════════════════
**CHECKPOINT: BEFORE PHASE 7**

For LOW/MEDIUM: □ Did you make the code changes?
For HIGH:
□ Did you invoke the foreman agent?
□ Did you invoke the judge agent for EACH completed wave?
□ Did Judge return APPROVED for ALL tasks?
□ Does implementation/judge-evaluation.md exist?

IF ANY BOX IS UNCHECKED: STOP. Go back and complete the work. Do not proceed.
═══════════════════════════════════════════════════════════════════════════════

---

## Phase 7: Testing & Verification

### Step 7.1: Run Automated Tests

```bash
poetry run python manage.py test
```

If tests fail, return to Phase 6, fix the issues, re-run Judge, then return here.

### Step 7.2: Generate Manual Testing Checklist

Create `testing/manual_checklist.md` based on success-criteria.md:
- [ ] Navigate to affected pages
- [ ] Test each implemented feature
- [ ] Verify no JavaScript errors in console
- [ ] Test edge cases

### Step 7.3: Invoke Playwright for UI/UX Changes (MANDATORY)

**⚠️ If the issue involves ANY UI/UX changes (templates, CSS, JS), you MUST run Playwright tests.**

**STOP AND ASK (required before Playwright):**
```
"I need to run Playwright UI tests. Please confirm:
1. Did we modify any Python files (views.py, models.py, urls.py, etc.)?
   → If YES: Server MUST be restarted before testing!
2. Is the dev server running from the worktree?
   → If not, please start (or restart) it:
   cd {worktree_path} && poetry run python run.py local
3. Let me know when ready."
```
**Include the full worktree path so the user knows where to run from.**
**CRITICAL: Python changes require server restart. CSS/HTML-only changes do not.**
**WAIT for user confirmation before proceeding. Do NOT skip this step.**

**Choose the right Playwright agent:**

| Agent | Use When | Model |
|-------|----------|-------|
| `playwright-quick` | Quick verification, screenshot capture, simple pass/fail | Sonnet (fast) |
| `playwright-tester` | Comprehensive testing, multi-step workflows, detailed reports | Opus |

**Default to `playwright-quick`** for most UI changes. Use `playwright-tester` for complex multi-page flows.

```
Task(subagent_type="playwright-quick", prompt="
  Session folder: {session_path}
  Issue: #{issue_number} - {issue_title}

  Test UI/UX changes with Playwright.
  Output screenshots to: {session_path}/testing/playwright/screenshots/
")
```

**Prerequisites for Playwright (verify before invoking):**
- User confirmed dev server is running
- `DEV_AUTH_ENABLED=True` in `.env.local`

**Skip Playwright ONLY if the issue has ZERO UI/template changes. If in doubt, run it.**

### Step 7.4: If Tests Fail

1. Analyze failures
2. Return to Phase 6 - invoke workers to fix
3. Invoke Judge on fixes
4. Re-run tests
5. Continue when ALL tests pass

═══════════════════════════════════════════════════════════════════════════════
**CHECKPOINT: BEFORE PHASE 8**

□ Did all Django tests pass?
□ **UI CHANGES? → Did you ask user about dev server and run Playwright?** (MANDATORY for ANY template/CSS/JS changes)
□ Did Playwright tests pass (if applicable)?
□ Does testing/manual_checklist.md exist?

IF ANY BOX IS UNCHECKED: STOP. Go back and complete testing. Do not proceed.
═══════════════════════════════════════════════════════════════════════════════

---

## Phase 8: Git Operations & PR Finalization

Worktree was created in Session Start Protocol (step 2).
Draft PR was created after first file edit (step 5).
This phase handles final commits and PR finalization.

### Commit Final Changes

```bash
git add .
git commit -m "feat(app): Brief description - Issue #{number}"
```

### Update and Finalize PR

Convert the Draft PR to Ready for Review:
```bash
gh pr ready
```

Update PR description if needed:
```bash
gh pr edit --body-file git/pr_description.md
```

### PR Description Template

```markdown
## Summary
[Brief description of changes]

## Changes Made
- [Change 1]
- [Change 2]

## Testing
- [x] Unit tests passing
- [x] Manual testing completed
- [x] Playwright tests passing (if UI changes)

## Issue
Closes #{number}
```

### Worktree Cleanup

**After PR is merged**, clean up the worktree using `git-worktrees-skill`:
```
"The PR has been merged. I'll clean up the worktree using git-worktrees-skill."
```

This removes the worktree directory and associated branch reference.

---

## Sub-Agent Definitions

| Agent | Model | Location | Purpose |
|-------|-------|----------|---------|
| docs-explorer | Sonnet | `.claude/agents/docs-explorer.md` | Documentation discovery |
| model-explorer | Opus | `.claude/agents/model-explorer.md` | Django model analysis |
| view-explorer | Opus | `.claude/agents/view-explorer.md` | Views/services analysis |
| template-explorer | Opus | `.claude/agents/template-explorer.md` | Template/UI analysis |
| codebase-explorer | Opus | `.claude/agents/codebase-explorer.md` | Deep codebase investigation |
| research-agent | Sonnet | `.claude/agents/research-agent.md` | Web search for modern practices |
| architect | Opus | `.claude/agents/architect.md` | Strategic task decomposition |
| engineer | Opus | `.claude/agents/engineer.md` | Technical design |
| planner | Opus | `.claude/agents/planner.md` | Combined planning (medium/low) |
| foreman | Opus | `.claude/agents/foreman.md` | Worker swarm orchestration |
| code-worker | Opus | `.claude/agents/code-worker.md` | Code implementation |
| test-worker | Sonnet | `.claude/agents/test-worker.md` | Test writing |
| judge | Opus | `.claude/agents/judge.md` | Quality evaluation |
| playwright-quick | Sonnet | `.claude/agents/playwright-quick.md` | Fast UI verification, screenshots, pass/fail |
| playwright-tester | Opus | `.claude/agents/playwright-tester.md` | Comprehensive UI testing with detailed reports |
| traffic-controller | Haiku | `.claude/agents/traffic-controller.md` | Workflow compliance |
| git-handler | Haiku | `.claude/agents/git-operations-handler.md` | Git operations |

---

## Scripts Reference

### get_current_date.py

```bash
# Full context
python .claude/skills/django-forge/scripts/get_current_date.py

# For web searches
python .claude/skills/django-forge/scripts/get_current_date.py --format search
```

### check_library_freshness.py

```bash
# Check a library
python .claude/skills/django-forge/scripts/check_library_freshness.py \
    django-htmx --github adamchainz/django-htmx
```

### state_manager.py

```bash
# Load state
python .claude/skills/django-forge/scripts/state_manager.py load {issue_number}

# Update phase
python .claude/skills/django-forge/scripts/state_manager.py advance {issue_number} exploration
```

---

## Resumption Support

When skill is invoked, check for existing session:

1. Look for `.django-forge/issue-{number}/`
2. If found, read `orchestration/state.json`
3. Ask user: "Resume from Phase {current_phase}?"
4. If yes, continue from saved state
5. If no, offer to start fresh

---

## Research Protocol

When user is uncertain or asks "how should I...":

1. **Get current date**
   ```bash
   python .claude/skills/django-forge/scripts/get_current_date.py --format search
   ```

2. **Search with year**
   ```
   "Django [topic] 2026"
   "HTMX [pattern] after:2025-01-02"
   ```

3. **Verify library freshness**
   ```bash
   python .claude/skills/django-forge/scripts/check_library_freshness.py \
       [package] --github [owner/repo]
   ```

4. **Present options with pros/cons**
   - Show common approaches
   - Reference official docs
   - Let user choose

---

## Integration Points

### With django-database-query-skill
**Location:** `.claude/skills/django-database-query-skill/`
**When to use:** During model exploration (Phase 3)
- Creates schema catalog files with accurate table/column names
- Prevents hallucinations about database structure
- Provides database-level truth that model-explorer builds on

**Integration pattern:**
```
During Phase 3 (Codebase Exploration):
  1. model-explorer invokes django-database-query-skill
  2. Schema catalog created/updated
  3. model-explorer adds Django ORM analysis on top
  4. Combined output used for query code
```

### With phoenix-theme-skill
**Location:** `.claude/skills/phoenix-theme-skill/`
**When to use:** During template exploration and implementation
- Source of truth for Phoenix Bootstrap components
- Component catalog with examples
- Playwright screenshots for UI testing
- Font Awesome 5 icon reference

**Integration pattern:**
```
During Phase 3 (Template exploration):
  - template-explorer analyzes existing codebase usage
  - References phoenix-theme-skill for component guidance

During Phase 6 (Implementation):
  - code-worker references phoenix-theme-skill for new UI

During Phase 7 (UI/UX Testing):
  - playwright-tester uses phoenix-theme-skill screenshot utilities
  - References component expectations for validation
  - Leverages dev auth bypass pattern from PR #820
```

### With github-issue-creator-skill
**Location:** `.claude/skills/github-issue-creator-skill/`
**When to use:** During implementation if scope creep is identified
- Create new issues for out-of-scope work discovered during implementation
- Use templates for consistent issue formatting
- Reference best practices documentation
- Quality standards for issue creation

**Integration pattern:**
```
If during implementation:
  - Scope creep item identified
  - Technical debt discovered
  - Enhancement opportunity found
Then:
  - Note it in session findings
  - Ask user: "Create a new issue for this?"
  - If yes, invoke github-issue-creator-skill
  - Continue with original scope
```

### With git-worktrees-skill
**Location:** `.claude/skills/git-worktrees-skill/`
**When to use:** At session start when user wants isolated development
- Creates separate working directory for the issue
- Keeps main branch clean during development
- Enables parallel work on multiple issues
- Easy cleanup after PR merge

**Integration pattern:**
```
At session start:
  - Offer worktree option to user
  - If accepted, invoke git-worktrees-skill
  - Create worktree: worktrees/issue-{number}/
  - Continue implementation in worktree
  - All git operations happen in worktree
```

### With meeting-git-issue-extractor
**Location:** `.claude/skills/meeting-git-issue-extractor/`
- Session folder patterns borrowed from this skill
- State management approach (state.json)
- User interaction patterns (max 3 questions)
- Async sub-agent patterns

### With git-workflow-requirements.md
**Location:** `docs/git-workflow-requirements.md`
- Branch naming: `feature/issue-{number}-{description}`
- PR requirements: Draft PR after first changes
- Daily commit rules
- No AI attribution in commits

### With existing agents
**Location:** `.claude/agents/`
- `docs-explorer.md` - Used in Phase 2 for documentation
- `git-operations-handler.md` - Used in Phase 8 for git/PR operations

---

## Example Session

```
User: Work on issue #456

Claude: I'll help you implement issue #456.

Before we begin, do you have anything you'd like to share?
- Any context about this issue?
- Constraints or preferences?
- Related work in progress?

I'll create a git worktree for this issue using the git-worktrees-skill.

User: No additional context. Go ahead.

Claude: Got it. Creating worktree and setting up the session now.

[Phase 1: Setup]
- Fetching issue details...
- Issue: "Add skill filtering to candidate search"
- Complexity: HIGH (multiple files, UI + backend)

I've assessed this as HIGH complexity because it involves multiple files and
both UI and backend changes. Do you agree, or would you like to override this?

User: That's correct.

[Phase 2: Documentation]
- Launching docs-explorer...
- Found relevant patterns in CLAUDE.md
- Identified htmx_best_practices.md

[Phase 3: Codebase Exploration]
- Launching 4 explorers in parallel:
  - model-explorer: CandidateSkill, Skill models
  - view-explorer: candidate_search_view
  - template-explorer: search.html, components
  - test-explorer: TestCandidateSearch

[Phase 4: Planning - HIGH complexity]
- Architect creating task breakdown...
- Engineer adding technical details...

[Phase 5: User Approval]

I've analyzed the issue. Here's my implementation plan:

**Tasks:**
1. Add skill filter field to CandidateSearchForm
2. Update candidate_search_view to handle skill filtering
3. Add HTMX partial for skill selection
4. Write tests for skill filtering

**Technical Approach:**
- Use HTMX hx-get for dynamic skill loading
- Filter via CandidateSkill.objects.filter(skill__in=[...])
- Follow existing filter pattern from location filtering

**Questions for you:**
1. Should skills filter with AND logic (all skills required) or OR logic (any skill)?

Do you approve this plan?
- [Approve] [Revise] [Ask Questions] [Abort]

User: AND logic. Approve.

[Phase 6: Implementation Swarm]
- Foreman spawning workers...
- Wave 1: Form field (TASK-001)
- Judge: APPROVED
- Wave 2: View logic (TASK-002)
- Judge: REWORK_REQUIRED - missing select_related
- Rework submitted...
- Judge: APPROVED
...

[Phase 7: Testing]
- Running tests... All passing
- Manual checklist ready

[Phase 8: Git & PR]
- Committing final changes to worktree branch
- Converting Draft PR to Ready for Review: https://github.com/...
- Cleaning up worktree via git-worktrees-skill

Implementation complete! Please review the PR.
```

---

## Slash Command

Also invocable via: `/django-issue {number}`
