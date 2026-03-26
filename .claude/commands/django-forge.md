---
description: Multi-agent skill for end-to-end GitHub issue implementation
argument-hint: <issue-number>
---

# Django Forge

Invoke the django-forge skill to implement a GitHub issue.

**ISSUE:** $ARGUMENTS

## STOP - READ THIS FIRST

You are about to execute the Django Forge workflow. These rules are **NON-NEGOTIABLE** and have been repeatedly violated:

1. **WORKTREE FIRST** - Create git worktree BEFORE any file operations. No exceptions.
2. **CREATE state.json IMMEDIATELY** - After session folder, create `orchestration/state.json` BEFORE exploration.
3. **DRAFT PR AFTER FIRST FILE EDIT** - The moment you Write/Edit your FIRST file, create a draft PR.
4. **ACTUALLY CHECK CHECKPOINTS** - When you reach a checkpoint, STOP and verify each box.
5. **NO SHORTCUTS** - Follow phases in order. Even for LOW complexity issues.
6. **USE SUB-AGENTS** - If you're not spawning agents, you're doing it wrong.

### Available Agents - USE THEM

| Agent | When to Use |
|-------|-------------|
| `git-operations-handler` | ALL git operations - always |
| `traffic-controller` | Workflow compliance - always |
| `docs-explorer` | Documentation exploration - always |
| `model-explorer` | Database/model work |
| `view-explorer` | Views/services/URLs |
| `template-explorer` | UI/template changes |
| `codebase-explorer` | Cross-cutting patterns |
| `architect` + `engineer` | Planning (HIGH complexity) |
| `planner` | Planning (MEDIUM/LOW complexity) |
| `foreman` + `code-worker` + `test-worker` | Implementation (HIGH) |
| `judge` | Quality evaluation (HIGH, optional MEDIUM) |
| `playwright-tester` | UI testing |
| `research-agent` | Web search for best practices |

Use agents when the workflow calls for them. Don't skip agent steps to "save time."

**Violations are unacceptable. Be precise. Be methodical. Self-check at every step.**

---

## What This Does

Django Forge coordinates 14 specialized AI agents through an 8-phase workflow:

1. **Setup** - Fetch issue, assess complexity, create session folder
2. **Documentation** - Read CLAUDE.md and project docs
3. **Exploration** - Run model/view/template/codebase explorers in parallel
4. **Planning** - Decompose into tasks (Architect + Engineer for HIGH complexity, Planner for MEDIUM/LOW)
5. **Approval** - Present plan to user, get explicit approval
6. **Implementation** - Multi-agent swarm executes tasks in waves, Judge evaluates each
7. **Testing** - Run automated tests, Playwright UI tests if applicable
8. **Git** - Create branch, commit, open PR (no AI attribution)

## Invoke the Skill

```
Skill: django-forge
```

## Skill Location

`.claude/skills/django-forge/SKILL.md` - Read this file for workflow commands
