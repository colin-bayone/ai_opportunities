# Phase 3 Session 2: PR Review + Git Worktrees Skills

## Your Mission

You are investigating two workflow-oriented skills that heavily use **bash scripts**: **pr-review-workflow-skill** and **git-worktrees-skill**. Also analyze the **hooks** that integrate with PR review.

## Context

- Phase 1 researched new Claude Code features (Dec 2025 - Feb 2026)
- Phase 2 researched best practices from official docs
- Phase 3 (you) investigates local patterns

These skills were built over a year and haven't been updated in months. Compare what you find against current best practices.

## Files to Analyze (Read All)

**PR Review Workflow Skill:**
```
.claude/skills/pr-review-workflow-skill/SKILL.md
.claude/skills/pr-review-workflow-skill/scripts/classify_files.sh
.claude/skills/pr-review-workflow-skill/scripts/check_staleness.sh
.claude/skills/pr-review-workflow-skill/scripts/log_compliance.sh
.claude/skills/pr-review-workflow-skill/scripts/generate_review_template.sh
.claude/skills/pr-review-workflow-skill/scripts/gather_pr_info.sh
.claude/skills/pr-review-workflow-skill/scripts/prepare_local_env.sh
```

**Git Worktrees Skill:**
```
.claude/skills/git-worktrees-skill/SKILL.md
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh
.claude/skills/git-worktrees-skill/scripts/list_worktrees.sh
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh
.claude/skills/git-worktrees-skill/scripts/setup_env.sh
.claude/skills/git-worktrees-skill/references/worktree_best_practices.md
```

**Hooks (PR review integration):**
```
.claude/hooks/README.md
.claude/hooks/block_ai_attribution.sh
.claude/hooks/verify_pr_review_compliance.sh
```

## Research Questions

1. **PR Review Workflow Architecture**
   - What phases does the workflow have?
   - How does it use scripts vs LLM reasoning?
   - What's the triggering pattern in description?

2. **Git Worktrees Architecture**
   - How simple vs complex is this skill?
   - What's the script-to-instruction ratio?

3. **Script Patterns**
   - What patterns do the bash scripts follow?
   - How do scripts communicate (args, stdout, exit codes)?
   - Error handling patterns?

4. **Hook Integration**
   - How do hooks work with pr-review?
   - What does block_ai_attribution.sh do?
   - What does verify_pr_review_compliance.sh check?

5. **Comparison to Best Practices**
   - What aligns with 2026 best practices?
   - What's outdated?
   - What's the right balance of script vs LLM?

## Output

Write your analysis to:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase3_session2_pr_review_git_worktrees.md
```

Use this structure:
```markdown
# Phase 3 Session 2: PR Review + Git Worktrees Skills

## Executive Summary
[5-7 key findings]

## Files Analyzed
[List all files you read]

## Detailed Analysis

### PR Review Workflow Skill
[SKILL.md analysis]

### Git Worktrees Skill
[SKILL.md analysis]

### Script Patterns
| Script | Purpose | Input | Output | Error Handling |
|--------|---------|-------|--------|----------------|
...

### Hooks Integration
[Analysis of each hook]

## Good Patterns (Keep)
[Patterns that align with best practices]

## Outdated Patterns (Update)
[Patterns that need modernizing]

## Unique Patterns (Consider)
[Interesting patterns worth keeping]

## Recommendations for Skill-Forge
[What skill-forge should learn]
```

## Do NOT

- Do NOT modify any files
- Do NOT create skill-forge
- Do NOT summarize superficially - be exhaustive
