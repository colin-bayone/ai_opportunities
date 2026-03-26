# Phase 3: Local Skills Investigation

**Session:** 2026-02-11_skill-forge-creation
**Purpose:** Investigate existing local .claude/ skills, agents, scripts, hooks

---

## Context

Phase 1 researched new Claude Code features (Dec 2025 - Feb 2026).
Phase 2 researched best practices from official docs and external sources.
Phase 3 investigates local patterns - what's already built, what works, what needs updating.

These skills were built over the span of a year and haven't been updated in months. Patterns may be good or outdated. Compare against Phase 2 best practices.

---

## 4-Session Delegation

### Session 1: django-forge Deep Dive
**Focus:** Most complex skill - 14 agents, scripts, references

**Files to analyze:**
- `.claude/skills/django-forge/SKILL.md`
- `.claude/skills/django-forge/agents/*.md` (14 files)
- `.claude/skills/django-forge/scripts/*.py` (4 files)
- Sample references (2-3 files for pattern understanding)

**Research questions:**
- How does the SKILL.md orchestrate the agent swarm?
- What are the agent roles and coordination patterns?
- How do scripts integrate (state_manager.py, etc.)?
- What patterns are good? What's outdated vs Phase 2 best practices?

**Output:** `research/phase3_session1_django_forge.md`

---

### Session 2: PR Review + Git Worktrees Skills
**Focus:** Script-heavy workflow skills + hooks integration

**Files to analyze:**
- `.claude/skills/pr-review-workflow-skill/SKILL.md`
- `.claude/skills/pr-review-workflow-skill/scripts/*.sh` (6 files)
- `.claude/skills/git-worktrees-skill/SKILL.md`
- `.claude/skills/git-worktrees-skill/scripts/*.sh` (4 files)
- `.claude/hooks/README.md`
- `.claude/hooks/*.sh` (2 files)

**Research questions:**
- How do these skills use bash scripts?
- How do hooks integrate with pr-review workflow?
- What's the balance of script vs LLM reasoning?
- What patterns are good? What's outdated?

**Output:** `research/phase3_session2_pr_review_git_worktrees.md`

---

### Session 3: Phoenix Theme Skill + Standalone Agents
**Focus:** Data catalog skill + standalone agent family

**Files to analyze:**
- `.claude/skills/phoenix-theme-skill/SKILL.md`
- `.claude/skills/phoenix-theme-skill/data/components/_master_index.json`
- Sample component _index.json and HTML files (pattern understanding)
- `.claude/agents/phoenix-*.md` (7 files)
- `.claude/agents/architect.md`, `.claude/agents/judge.md`, `.claude/agents/foreman.md` (comparison)

**Research questions:**
- How does the data catalog work?
- How do standalone agents relate to skills?
- What frontmatter patterns are used?
- What patterns are good? What's outdated?

**Output:** `research/phase3_session3_phoenix_agents.md`

---

### Session 4: Cross-Cutting Patterns + Other Skills
**Focus:** Settings, commands, prompts, and other skills

**Files to analyze:**
- `.claude/settings.local.json`
- `.claude/commands/*.md`
- `.claude/prompts/*.md`
- `.claude/skills/airflow-skill/SKILL.md`
- `.claude/skills/azure-expert-skill/SKILL.md`
- `.claude/skills/docker-expert-skill/SKILL.md`
- `.claude/skills/django-database-query-skill/SKILL.md`

**Research questions:**
- What settings patterns are used?
- How do commands and prompts relate to skills?
- What patterns appear across multiple skills?
- What's consistent vs inconsistent?

**Output:** `research/phase3_session4_cross_cutting.md`

---

## Output Structure

Each session should produce:

```markdown
# Phase 3 Session [X]: [Topic]

## Executive Summary
[Key findings - 5-7 bullets]

## Files Analyzed
[List of files read]

## Detailed Analysis

### [Component 1]
- Structure
- Patterns used
- Integration points

### [Component 2]
...

## Good Patterns (Keep)
[Patterns that align with Phase 2 best practices]

## Outdated Patterns (Update)
[Patterns that don't align with 2026 best practices]

## Unique Patterns (Consider)
[Interesting patterns not covered in Phase 2]

## Recommendations for Skill-Forge
[What skill-forge should learn from this]
```

---

## Success Criteria

Each session must:
1. Read all specified files
2. Compare against Phase 2 best practices
3. Identify good vs outdated patterns
4. Extract unique patterns worth considering
5. Provide skill-forge recommendations
