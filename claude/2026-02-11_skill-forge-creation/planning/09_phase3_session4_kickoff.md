# Phase 3 Session 4: Cross-Cutting Patterns + Other Skills

## Your Mission

You are investigating **cross-cutting patterns** across the .claude/ folder: settings, commands, prompts, and other skills not covered by Sessions 1-3.

## Context

- Phase 1 researched new Claude Code features (Dec 2025 - Feb 2026)
- Phase 2 researched best practices from official docs
- Phase 3 (you) investigates local patterns

These were built over a year and haven't been updated in months. Compare against current best practices.

## Files to Analyze (Read All)

**Settings:**
```
.claude/settings.local.json
```

**Commands:**
```
.claude/commands/ (list directory and read all .md files)
```

**Prompts:**
```
.claude/prompts/django-forge-kickoff.md
.claude/prompts/django-forge-pr-review.md
```

**Other Skills (SKILL.md only):**
```
.claude/skills/airflow-skill/SKILL.md
.claude/skills/azure-expert-skill/SKILL.md
.claude/skills/docker-expert-skill/SKILL.md
.claude/skills/django-database-query-skill/SKILL.md
.claude/skills/github-issue-creator-skill/SKILL.md
.claude/skills/concept-tutor-skill/SKILL.md
.claude/skills/brainstorm-skill/SKILL.md
.claude/skills/talent-docs-skill/SKILL.md
.claude/skills/meeting-git-issue-extractor/SKILL.md
```

## Research Questions

1. **Settings Patterns**
   - What's in settings.local.json?
   - What permissions patterns are used?
   - Environment variables?

2. **Commands vs Skills**
   - What commands exist?
   - How do they differ from skills?
   - Should they be migrated to skills?

3. **Prompts Pattern**
   - What are prompts used for?
   - How do they relate to skills?

4. **Cross-Skill Patterns**
   - What patterns appear across multiple skills?
   - Description writing patterns?
   - Frontmatter consistency?
   - Directory structure consistency?

5. **Skill Variety**
   - What different skill types exist?
   - Simple vs complex patterns?
   - What makes each unique?

6. **Comparison to Best Practices**
   - What aligns with 2026 best practices?
   - What's inconsistent?
   - What standardization is needed?

## Output

Write your analysis to:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase3_session4_cross_cutting.md
```

Use this structure:
```markdown
# Phase 3 Session 4: Cross-Cutting Patterns

## Executive Summary
[5-7 key findings]

## Files Analyzed
[List all files you read]

## Detailed Analysis

### Settings Patterns
[settings.local.json analysis]

### Commands Analysis
| Command | Purpose | Should Migrate to Skill? |
|---------|---------|--------------------------|
...

### Prompts Pattern
[How prompts are used]

### Cross-Skill Patterns
[Common patterns across skills]

### Skill Catalog
| Skill | Type | Complexity | Unique Features |
|-------|------|------------|-----------------|
...

## Good Patterns (Keep)
[Patterns that align with best practices]

## Outdated Patterns (Update)
[Patterns that need modernizing]

## Inconsistencies Found
[Things that should be standardized]

## Recommendations for Skill-Forge
[What skill-forge should learn]
```

## Do NOT

- Do NOT modify any files
- Do NOT create skill-forge
- Do NOT summarize superficially - be exhaustive
