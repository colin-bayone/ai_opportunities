# Phase 3 Session 3: Phoenix Theme Skill + Standalone Agents

## Your Mission

You are investigating the **phoenix-theme-skill** (a UI component catalog) and the **standalone phoenix-* agents** in `.claude/agents/`. Also compare with other standalone agents.

## Context

- Phase 1 researched new Claude Code features (Dec 2025 - Feb 2026)
- Phase 2 researched best practices from official docs
- Phase 3 (you) investigates local patterns

These were built over a year and haven't been updated in months. Compare against current best practices.

## Files to Analyze (Read All)

**Phoenix Theme Skill:**
```
.claude/skills/phoenix-theme-skill/SKILL.md
.claude/skills/phoenix-theme-skill/data/components/_master_index.json
```

**Sample Data Files (for pattern understanding, not all 100+):**
```
.claude/skills/phoenix-theme-skill/data/components/modules_components_alerts/_index.json
.claude/skills/phoenix-theme-skill/data/components/modules_components_alerts/00_alert_subtle_examples.html
.claude/skills/phoenix-theme-skill/data/components/modules_components_card/_index.json
.claude/skills/phoenix-theme-skill/data/components/modules_components_card/00_basic_example.html
```

**All 7 Phoenix Standalone Agents:**
```
.claude/agents/phoenix-catalog-explorer.md
.claude/agents/phoenix-chart-advisor.md
.claude/agents/phoenix-django-explorer.md
.claude/agents/phoenix-implementation-planner.md
.claude/agents/phoenix-pattern-validator.md
.claude/agents/phoenix-screenshot-analyzer.md
.claude/agents/phoenix-template-generator.md
```

**Comparison Agents (different patterns):**
```
.claude/agents/architect.md
.claude/agents/judge.md
.claude/agents/foreman.md
```

## Research Questions

1. **Phoenix Theme Skill Architecture**
   - How does SKILL.md work with the data catalog?
   - What's the purpose of _master_index.json?
   - How are components organized and discovered?

2. **Data Catalog Pattern**
   - How does progressive disclosure work with 100+ files?
   - What's in the _index.json files?
   - How does the skill know which component to load?

3. **Standalone Agent Patterns**
   - How do phoenix-* agents relate to the skill?
   - What frontmatter patterns are used?
   - How do they coordinate?

4. **Frontmatter Comparison**
   - What fields are used across agents?
   - Tools, permissions, skills references?
   - Differences between phoenix and other agents?

5. **Comparison to Best Practices**
   - What aligns with 2026 best practices?
   - What's outdated?
   - Could Agent Teams improve this?

## Output

Write your analysis to:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase3_session3_phoenix_agents.md
```

Use this structure:
```markdown
# Phase 3 Session 3: Phoenix Theme Skill + Standalone Agents

## Executive Summary
[5-7 key findings]

## Files Analyzed
[List all files you read]

## Detailed Analysis

### Phoenix Theme Skill
[SKILL.md and data catalog analysis]

### Data Catalog Pattern
[_master_index.json, _index.json patterns]

### Phoenix Agents
| Agent | Purpose | Tools | Frontmatter Fields |
|-------|---------|-------|-------------------|
...

### Comparison with Other Agents
[architect, judge, foreman patterns]

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

- Do NOT read all 100+ HTML files (samples are enough)
- Do NOT modify any files
- Do NOT create skill-forge
- Do NOT summarize superficially - be exhaustive
