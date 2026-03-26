---
name: git-worktrees-skill
description: Git worktree management for parallel Claude Code development. This skill should be used when users want to work on multiple branches simultaneously, set up isolated development environments for parallel tasks, review PRs without switching branches, or manage multiple Claude Code sessions working on different features concurrently. Triggers include requests like "create a worktree", "set up parallel development", "I want to work on two things at once", or "help me review a PR without losing my current work".
---

# Git Worktrees Skill

## Safety Policy - READ FIRST

**This skill is designed to be non-destructive.** The scripts in this skill:

- **DO NOT delete branches** - Ever. Branch deletion is manual-only.
- **DO NOT force-push** - No destructive git operations.
- **DO NOT delete files** - Only worktree directories (which are copies).
- **ALWAYS require confirmation** - Before removing anything.

### Claude Instructions (CRITICAL)

When using this skill, Claude MUST follow these rules:

#### Safety Rules

1. **NEVER delete branches** unless the user explicitly says "delete the branch" or "delete branch X"
2. **NEVER run `git branch -d` or `git branch -D`** without direct user instruction
3. **ALWAYS ask for confirmation** before running `remove_worktree.sh`
4. **NEVER assume cleanup is desired** - Only remove worktrees when explicitly asked

#### GitHub CLI Rules

1. **NEVER specify `--repo` with `gh` commands** - The CLI automatically detects the current repository
2. **Use simple commands:** `gh issue view 123` NOT `gh issue view 123 --repo owner/repo`
3. **Same for PRs:** `gh pr view 456` NOT `gh pr view 456 --repo owner/repo`
4. **The current working directory IS the repo context** - Don't override it

#### Communication Rules - Narrate Everything

Before running ANY command, Claude MUST explain:

1. **What** - The specific command being run
2. **Why** - The purpose and what it accomplishes
3. **Effect** - What will change (directories created, branches checked out, etc.)
4. **Risks** - Any potential issues (e.g., "will run poetry install which may take a minute")

**Example of correct narration:**
```
User: "Create a worktree for PR 445"

Claude: "I'll create a worktree for PR #445. Here's what will happen:

1. Fetch PR #445's branch from GitHub
2. Create a new directory: ../talent_ai-pr-445/
3. Check out the PR's branch in that directory
4. Run `poetry install` to set up dependencies (may take 1-2 minutes)

The worktree will be a separate working directory - your current work here is untouched.

Should I proceed?"
```

#### Error Handling Rules

When a command fails, Claude MUST:

1. **Read the full error message** - Don't guess at the cause
2. **Investigate the actual problem** - Run diagnostic commands if needed
3. **Explain what went wrong** - In plain language
4. **Propose a fix** - With user approval before attempting

**Example of correct error handling:**
```
[Script fails with exit code 1]

Claude: "The command failed. Let me investigate...

[Runs diagnostic commands]

The issue is: Branch 'feature-x' is already checked out in another worktree at ../talent_ai-feature-x.

Git doesn't allow the same branch in multiple worktrees. Options:
1. Use a different branch name
2. Remove the existing worktree first

Which would you prefer?"
```

**WRONG:** "The script failed. Let me try again with --force."

#### Example Workflows

**Good - Creating a worktree:**
```
User: "Set up a worktree for the new auth feature"

Claude: "I'll create a worktree for a new 'auth-feature' branch.

This will:
- Create directory: ../talent_ai-auth-feature/
- Create new branch 'auth-feature' based on your current branch
- Install dependencies with poetry

Your current work stays untouched. Should I proceed?"

User: "yes"

Claude: [Runs create_worktree.sh, shows output]

"Done! The worktree is ready at ../talent_ai-auth-feature/

To work in it:
  cd ../talent_ai-auth-feature
  claude

The branch 'auth-feature' is now checked out there."
```

**Good - Removing a worktree:**
```
User: "Remove the worktree for feature-x"

Claude: "I'll remove the worktree at ../talent_ai-feature-x.

Important notes:
- This removes the DIRECTORY only
- The branch 'feature-x' will still exist
- Any uncommitted changes in that worktree will be lost

Should I proceed?"
```

**Bad - No explanation:**
```
User: "Create a worktree"
Claude: [Just runs the script without explaining anything]
```

## Overview

Git worktrees enable parallel development by allowing multiple branches to be checked out in separate directories simultaneously. This is particularly powerful with Claude Code, enabling independent AI sessions to work on different features, bugs, or reviews without interference.

**Key benefits:**
- Run multiple Claude Code sessions in parallel on different branches
- Review PRs without stashing/switching branches
- Isolate long-running tasks from your main development
- Shared git history means all worktrees stay synchronized

## Quick Start

### Create a Worktree for a New Feature

```bash
# From your main repo
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh feature-name

# This creates ../talent_ai-feature-name with a new branch
# Then sets up the development environment (poetry install, etc.)
```

### Create a Worktree for PR Review

```bash
# Checkout existing PR branch into a worktree
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh pr-422 --pr 422

# This fetches the PR and creates a worktree for it
```

### List All Worktrees

```bash
.claude/skills/git-worktrees-skill/scripts/list_worktrees.sh

# Shows all worktrees with their branches and status
```

### Remove a Worktree

```bash
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh feature-name

# Removes the worktree DIRECTORY only
# The branch is NOT deleted - you must do that manually if desired
```

## Core Workflows

### Workflow 1: Parallel Feature Development

When working on multiple features simultaneously:

1. **Create worktrees for each feature:**
   ```bash
   .claude/skills/git-worktrees-skill/scripts/create_worktree.sh auth-refactor
   .claude/skills/git-worktrees-skill/scripts/create_worktree.sh email-notifications
   ```

2. **Launch Claude Code in each:**
   ```bash
   # Terminal 1
   cd ../talent_ai-auth-refactor && claude

   # Terminal 2
   cd ../talent_ai-email-notifications && claude
   ```

3. **Work independently** - Each session has full isolation

4. **Clean up after merging:**
   ```bash
   .claude/skills/git-worktrees-skill/scripts/remove_worktree.sh auth-refactor
   # Branch still exists - delete manually if desired:
   # git branch -d auth-refactor
   ```

### Workflow 2: PR Review Without Context Switching

To review a PR while keeping your current work intact:

1. **Create worktree for the PR:**
   ```bash
   .claude/skills/git-worktrees-skill/scripts/create_worktree.sh review-422 --pr 422
   ```

2. **Review in the worktree:**
   ```bash
   cd ../talent_ai-review-422
   claude
   # Use pr-review-workflow-skill in this session
   ```

3. **Your main work is untouched** - Continue where you left off

### Workflow 3: Bug Fix While Feature in Progress

When you need to fix a bug but have uncommitted feature work:

1. **Create worktree from main:**
   ```bash
   .claude/skills/git-worktrees-skill/scripts/create_worktree.sh hotfix-login --base main
   ```

2. **Fix the bug in isolation:**
   ```bash
   cd ../talent_ai-hotfix-login
   claude
   # Fix and commit
   ```

3. **Continue feature work** - Your main repo is unchanged

## Script Reference

All scripts are in the `scripts/` directory:

### create_worktree.sh

Creates a new worktree with optional environment setup.

```bash
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh <name> [options]

Options:
  --base <branch>   Base branch (default: current branch)
  --pr <number>     Fetch and checkout a PR branch
  --no-setup        Skip environment setup (poetry install, etc.)
  --path <dir>      Custom parent directory (default: parent of repo)

Examples:
  .claude/skills/git-worktrees-skill/scripts/create_worktree.sh new-feature
  .claude/skills/git-worktrees-skill/scripts/create_worktree.sh pr-review --pr 445
  .claude/skills/git-worktrees-skill/scripts/create_worktree.sh hotfix --base main
```

### list_worktrees.sh

Lists all worktrees with status information.

```bash
.claude/skills/git-worktrees-skill/scripts/list_worktrees.sh [options]

Options:
  --verbose         Show detailed info (commits behind, uncommitted changes)
  --json            Output as JSON for scripting

Output includes:
  - Path to each worktree
  - Current branch
  - Commits ahead/behind main
  - Whether there are uncommitted changes
```

### remove_worktree.sh

Safely removes a worktree directory. **Does NOT delete branches.**

```bash
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh <name>

What it does:
  - Removes the worktree directory only
  - Warns if uncommitted changes exist
  - Warns if unpushed commits exist
  - Requires y/N confirmation before removal

What it does NOT do:
  - Delete any branches
  - Force any operations
  - Run without user confirmation

After removal, to delete the branch manually (if desired):
  git branch -d <branch-name>    # Safe delete (only if merged)
  git branch -D <branch-name>    # Force delete
```

### setup_env.sh

Sets up development environment in a worktree.

```bash
.claude/skills/git-worktrees-skill/scripts/setup_env.sh [options]

Automatically detects and runs:
  - poetry install (if pyproject.toml exists)
  - npm install / yarn (if package.json exists)
  - pip install -r requirements.txt (if requirements.txt exists)

Options:
  --skip-deps       Skip dependency installation
  --migrate         Run Django migrations after setup
  --copy-env        Copy .env files from main worktree
```

## Important Concepts

### Shared Git History

All worktrees share the same `.git` database:
- Commits made in any worktree are visible to all
- Push/pull affects all worktrees
- Branches created in one are available in all

### One Branch Per Worktree

Git enforces that each worktree must be on a different branch:
- Cannot have two worktrees on the same branch
- Attempting to checkout an already-checked-out branch will fail
- Use `git worktree list` to see what's checked out where

### Environment Independence

Each worktree needs its own:
- Installed dependencies (node_modules, .venv, etc.)
- Environment files (.env.local)
- Build artifacts

The `create_worktree.sh` script handles this automatically.

### Naming Convention

Worktrees are created as sibling directories with prefix:
```
/home/user/programming/
├── talent_ai/                    # Main repo
├── talent_ai-feature-a/          # Worktree for feature-a branch
├── talent_ai-pr-422/             # Worktree for PR 422 review
└── talent_ai-hotfix/             # Worktree for hotfix
```

## Best Practices

### DO:
- Use descriptive worktree names matching the task
- Clean up worktree directories after merging PRs
- Run `git fetch` in main repo to sync all worktrees
- Use separate terminal tabs/windows for each worktree session

### DON'T:
- Create too many worktrees (3-4 is usually plenty)
- Forget to install dependencies in new worktrees
- Leave stale worktrees around indefinitely
- Try to checkout the same branch in multiple worktrees

## Claude Code Integration

### Launching Multiple Sessions

Each worktree can have its own Claude Code session:

```bash
# Main feature development
cd /home/cmoore/programming/talent_ai
claude

# Parallel PR review (different terminal)
cd /home/cmoore/programming/talent_ai-pr-review
claude

# Hotfix (different terminal)
cd /home/cmoore/programming/talent_ai-hotfix
claude
```

### Session Independence

Each Claude Code session:
- Has its own conversation context
- Can make independent edits
- Uses the same skills and settings (from main .claude/)
- Doesn't interfere with other sessions

### Recommended Workflow

1. **Main worktree** - Primary development work
2. **Review worktree** - PR reviews (reuse for multiple PRs)
3. **Hotfix worktree** - Quick fixes (create/remove as needed)

## Troubleshooting

### "Branch is already checked out"

```bash
git worktree list  # See what's checked out where
```

Either use a different branch or remove the existing worktree.

### "Worktree not found"

The worktree directory was deleted without using `git worktree remove`:

```bash
git worktree prune  # Clean up stale worktree references
```

### Poetry/npm not finding packages

Run environment setup in the worktree:

```bash
cd ../talent_ai-feature-name
.claude/skills/git-worktrees-skill/scripts/setup_env.sh
```

### Changes not showing in other worktree

Git history is shared, but working directory changes are not:

```bash
# In worktree A: commit changes
git add . && git commit -m "changes"

# In worktree B: fetch to see the commit
git fetch origin
```

## References

For detailed best practices and advanced patterns, see:
- `references/worktree_best_practices.md` - Comprehensive guide
