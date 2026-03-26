# Session 1 Kickoff: Skill Structure & SKILL.md Patterns

## Your Mission

You are a research worker for Phase 2 of the skill-forge project. Your job is to research **best practices for Claude Code skill structure and SKILL.md patterns** from official sources and current 2026 documentation.

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

1. **Official Skill Structure**
   - Directory organization
   - Required vs optional files
   - SKILL.md placement
   - Supporting files (scripts/, references/, assets/)

2. **SKILL.md Format**
   - YAML frontmatter fields (all of them)
   - Required vs optional fields
   - Markdown body structure
   - Best practices for instruction writing

3. **Frontmatter Deep Dive**
   - `name` field patterns
   - `description` field - triggering patterns
   - `allowed-tools` - tool restrictions
   - `disable-model-invocation` - when to use
   - `user-invocable` - when to use
   - Any other fields

4. **Skill Triggering**
   - How Claude decides to load a skill
   - Description writing for optimal triggering
   - When to use manual vs auto invocation

5. **Skills vs Commands vs Agents**
   - When to use each
   - How they relate to each other
   - Conversion patterns

6. **Skill Invocation Patterns**
   - User invocation via /command
   - Model invocation (auto-loading)
   - Arguments and parameters

## Sources to Check

**Required:**
- https://github.com/anthropics/skills - Main repo README and docs
- https://github.com/anthropics/skills/tree/main/skills/skill-creator - The skill-creator skill
- Claude Code official documentation on skills

**Web Search:**
- "Claude Code skill structure 2026"
- "Claude Code SKILL.md best practices"
- "Claude Code skill triggering"
- "anthropic skills documentation"

## Output Requirements

Create your research document at:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase2_session1_skill_structure.md
```

Use this structure:
```markdown
# Phase 2 Session 1: Skill Structure & SKILL.md Patterns

## Executive Summary
[5-7 key findings]

## Sources Consulted
| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
...

## Detailed Findings

### Skill Directory Structure
[Everything about organization]

### SKILL.md Format
[Complete format documentation]

### Frontmatter Fields
[Every field with examples]

### Skill Triggering
[How triggering works]

### Skills vs Commands vs Agents
[Comparison and guidance]

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
