# Git Worktree Best Practices

Comprehensive guide to effective git worktree usage, especially with Claude Code for parallel AI-assisted development.

## Understanding Git Worktrees

### How Worktrees Work

A git worktree is an additional working directory linked to your repository. Unlike cloning, worktrees:

1. **Share the same `.git` database** - All commits, branches, refs, and history
2. **Have isolated working directories** - Each has its own checked-out files
3. **Use minimal disk space** - Only file copies, not full repo duplication
4. **Stay synchronized** - Changes in one are immediately visible to others

### The `.git` File vs Directory

In a worktree, instead of a `.git` directory, you'll find a `.git` file:
```
# Content of .git file in worktree
gitdir: /path/to/main/repo/.git/worktrees/worktree-name
```

This links the worktree to the main repository's git database.

### Branch Exclusivity

Git enforces **one branch per worktree**. This prevents conflicts:
- Cannot checkout `feature-a` in two worktrees simultaneously
- Attempting to do so produces an error
- Use `git worktree list` to see which branches are where

## Claude Code Integration Patterns

### Pattern 1: Feature + Review Parallel

Run feature development and PR reviews simultaneously:

```
Terminal 1 (feature work):
  cd /home/user/project
  claude
  # Continue building feature

Terminal 2 (PR review):
  cd /home/user/project-pr-review
  claude
  # Review PR without interrupting feature work
```

### Pattern 2: Long-Running Task Isolation

For tasks Claude works on over extended periods:

```bash
# Create isolated worktree for long task
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh data-migration

# Start Claude on the long task
cd ../project-data-migration
claude
# "Migrate all user data to new schema, test thoroughly"

# Meanwhile, continue other work in main repo
cd ../project
claude
# Quick bug fixes, other features
```

### Pattern 3: Experimental Sandbox

Test risky changes without affecting main work:

```bash
# Create experimental worktree
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh experiment --base main

# Try risky refactoring
cd ../project-experiment
claude
# "Refactor auth system to use new pattern"

# If it works: merge
# If it fails: just delete the worktree
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh experiment
```

## Workflow Recommendations

### Naming Conventions

Use descriptive, consistent names:

| Pattern | Example | Use Case |
|---------|---------|----------|
| `feature-*` | `feature-auth-refactor` | New features |
| `fix-*` | `fix-login-bug` | Bug fixes |
| `pr-*` | `pr-445-review` | PR reviews |
| `exp-*` | `exp-new-architecture` | Experiments |
| `hotfix-*` | `hotfix-prod-crash` | Urgent fixes |

### Recommended Number of Worktrees

**Optimal: 2-4 worktrees**

- 1 main development worktree
- 1 PR review worktree (reusable)
- 1-2 for parallel features/fixes

**Avoid:**
- More than 5 active worktrees (cognitive overhead)
- Worktrees that sit idle for weeks
- One worktree per tiny task

### Lifecycle Management

1. **Create** when starting a significant task
2. **Work** until task is complete
3. **Push** changes to remote
4. **Merge** PR through normal process
5. **Delete** worktree after merge
6. **Prune** periodically: `git worktree prune`

## Environment Considerations

### What Each Worktree Needs

Each worktree requires its own:

| Component | Reason | Setup |
|-----------|--------|-------|
| Dependencies | Different branches may have different deps | `poetry install` |
| Node modules | Same reason | `npm install` |
| Virtual envs | Isolation | Automatic with Poetry |
| Build artifacts | Branch-specific builds | Run build |
| .env files | May need to copy | Use `--copy-env` |

### Environment File Handling

**Option 1: Copy from main** (recommended for consistent config)
```bash
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh feature-x
# Auto-copies .env.local
```

**Option 2: Symlink** (for always-current config)
```bash
ln -s /path/to/main/.env.local .env.local
```

**Option 3: Worktree-specific** (for testing different configs)
```bash
# Create custom .env.local in worktree
```

### Database Considerations

For Django projects with shared database:
- All worktrees can use same database
- Be careful with conflicting migrations
- Consider separate databases for experimental work

```bash
# Use different database for experiment
export DATABASE_URL=postgresql://localhost/myapp_experiment
./manage.py migrate
```

## Advanced Patterns

### Worktree for Each Issue

For teams using issue-per-branch workflow:

```bash
# Start issue #123
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh issue-123 --base main

# Work on it
cd ../project-issue-123
claude
# "Implement feature described in issue #123"

# When done, push and create PR
git push -u origin issue-123
gh pr create

# After merge, cleanup
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh issue-123
```

### Reusable Review Worktree

Keep one worktree for all PR reviews:

```bash
# Create once
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh review --base main

# For each review
cd ../project-review
gh pr checkout 445
# Review...

# After review, reset for next one
git checkout main
git pull
```

### Parallel Feature Development

Work on multiple related features:

```bash
# Feature A depends on main
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh feature-a --base main

# Feature B depends on feature A
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh feature-b --base feature-a

# When feature-a merges, rebase feature-b
cd ../project-feature-b
git rebase origin/main
```

## Troubleshooting

### Common Issues

**"fatal: 'feature-x' is already checked out"**
```bash
# Find where it's checked out
git worktree list
# Either use different branch or remove that worktree
```

**"fatal: not a git repository"**
```bash
# Make sure you're in a worktree directory
# Check if .git file exists and points correctly
cat .git
```

**Worktree deleted but git still references it**
```bash
# Clean up stale references
git worktree prune
```

**Dependencies out of sync**
```bash
# Re-run setup
.claude/skills/git-worktrees-skill/scripts/setup_env.sh
```

### Recovery Scenarios

**Accidentally deleted worktree directory:**
```bash
# Clean up git's reference
git worktree prune

# Recreate if needed
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh feature-x
```

**Worktree has conflicts after pull:**
```bash
# Resolve normally
cd ../project-feature-x
git status
# Fix conflicts
git add .
git commit
```

**Need to move worktree:**
```bash
# Git worktree move command
git worktree move ../old-location ../new-location
```

## Performance Tips

### Disk Space

Worktrees are lightweight but dependencies add up:
- `node_modules/` can be 500MB+ per worktree
- Python virtualenvs: 100-500MB
- Consider cleaning unused worktrees promptly

### Git Operations

**Fetch once, all worktrees benefit:**
```bash
# In main repo
git fetch --all

# All worktrees now see new remote refs
```

**Avoid fetching in each worktree:**
```bash
# Don't do this in every worktree
cd ../project-feature-a && git fetch
cd ../project-feature-b && git fetch
cd ../project-review && git fetch

# Do this once from main
cd ../project && git fetch --all
```

## Integration with Claude Code

### Conversation Isolation

Each Claude Code session in a worktree:
- Has completely separate conversation history
- Maintains its own context
- Can be working on different tasks

### Skill Availability

Skills from main `.claude/` directory are available in all worktrees because:
- Worktrees share the repository
- `.claude/` is part of the repo
- Settings propagate automatically

### Best Practices with Claude

1. **Be explicit about context** - Claude in worktree doesn't know about other sessions
2. **Use TODO lists** - Track progress within each session
3. **Commit frequently** - Makes work visible across worktrees
4. **Document in commits** - Other sessions can see commit messages

## Security Considerations

### Credential Handling

Git credentials work across all worktrees (shared `.git`):
- SSH keys: shared
- Git credential helper: shared
- Personal access tokens: shared

### Sensitive Files

Be careful with:
- `.env` files with secrets - don't commit
- API keys - same precautions as main repo
- Database credentials - manage per-worktree if different DBs

### Code Isolation

Worktrees provide **working directory isolation**, not security isolation:
- All worktrees can access same Git history
- All worktrees share remotes
- No permission boundaries between worktrees
