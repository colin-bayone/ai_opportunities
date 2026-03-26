# Session 4 Kickoff: Scripts, Context & Progressive Disclosure

## Your Mission

You are a research worker for Phase 2 of the skill-forge project. Your job is to research **best practices for scripts, context management, and progressive disclosure in Claude Code** from official sources and current 2026 documentation.

## Important: External Research Only

- Focus on official documentation, GitHub repos, and web research
- Local skills investigation is Phase 3 - we're doing Phase 2 now

## Research Principles

1. **Recency wins** - More recent documentation takes precedence
2. **Anthropic docs win** - Official sources override community content
3. **Calibrate for 2025/2026** - Note when patterns have changed
4. **Be exhaustive** - Document everything, not just highlights

## Your Research Scope

### Topics to Research

1. **Script Integration in Skills**
   - scripts/ directory patterns
   - Python script patterns
   - Bash script patterns
   - How skills invoke scripts
   - Script input/output patterns

2. **When Scripts vs LLM**
   - Decision criteria
   - Fragile operations needing scripts
   - Determinism requirements
   - Freedom levels (high/medium/low)

3. **Progressive Disclosure**
   - 3-tier loading (metadata → SKILL.md → resources)
   - How to structure for progressive loading
   - Token budget considerations
   - When to put content inline vs references

4. **Context Management**
   - Context window as shared resource
   - How to minimize context usage
   - Subagent context isolation
   - Compaction behavior
   - PreCompact hook for context preservation

5. **Reference Files**
   - references/ directory patterns
   - How to organize references
   - Linking from SKILL.md
   - Index files patterns

6. **CLAUDE.md Patterns**
   - What goes in CLAUDE.md
   - Project vs user level
   - Keeping it focused ("ruthlessly pruned")
   - Integration with skills

7. **Settings Integration**
   - settings.json patterns
   - Permissions integration
   - Environment variables
   - Scope hierarchy (managed, project, user, local)

8. **Token Efficiency Patterns**
   - Minimizing context usage
   - When to load vs not load
   - Fan-out patterns
   - Scoped investigation

## Sources to Check

**Required:**
- Claude Code best practices documentation
- Claude Code settings documentation
- https://github.com/anthropics/skills - Look at skill-creator and how it teaches progressive disclosure
- https://github.com/anthropics/skills/tree/main/skills/skill-creator

**Web Search:**
- "Claude Code progressive disclosure"
- "Claude Code context management"
- "Claude Code script integration"
- "Claude Code token efficiency"
- "Claude Code best practices 2026"

## Output Requirements

Create your research document at:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase2_session4_scripts_context.md
```

Use this structure:
```markdown
# Phase 2 Session 4: Scripts, Context & Progressive Disclosure

## Executive Summary
[5-7 key findings]

## Sources Consulted
| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
...

## Detailed Findings

### Script Integration
[Complete documentation]

### When Scripts vs LLM
[Decision criteria and examples]

### Progressive Disclosure
[3-tier loading with examples]

### Context Management
[All patterns and strategies]

### Reference Files
[Organization patterns]

### CLAUDE.md Patterns
[Best practices]

### Settings Integration
[Configuration patterns]

### Token Efficiency
[All efficiency patterns]

## Patterns Catalog
1. Pattern: [name]
   - Description: ...
   - When to use: ...
   - Example: ...
...

## Recency Notes
[What changed in 2025/2026]

## Recommendations for Skill-Forge
[What skill-forge should implement]
```

## Do NOT

- Do NOT create the skill-forge skill
- Do NOT summarize superficially - be exhaustive
