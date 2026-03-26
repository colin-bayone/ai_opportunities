# Session 2 Kickoff: Agents & Subagents Patterns

## Your Mission

You are a research worker for Phase 2 of the skill-forge project. Your job is to research **best practices for Claude Code agents, subagents, and Agent Teams** from official sources and current 2026 documentation.

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

1. **Task Tool**
   - All parameters
   - Built-in subagent types
   - How to invoke
   - Return values and output handling

2. **Built-in Subagents**
   - Explore subagent
   - Plan subagent
   - General-purpose subagent
   - Any other built-in types
   - When to use each

3. **Custom Subagents**
   - agent.md file format
   - Frontmatter fields (all of them)
   - Directory placement (~/.claude/agents vs .claude/agents)
   - How Claude discovers and uses them

4. **Agent Frontmatter Deep Dive**
   - `name` and `description`
   - `tools` - allowlist patterns
   - `disallowedTools` - blocklist patterns
   - `permissionMode` - all modes and when to use
   - `model` - model specification
   - `skills` - skill loading in agents
   - `memory` - persistent memory
   - `hooks` - agent-specific hooks
   - `maxTurns` - turn limits
   - `context` - fork isolation

5. **Agent Teams (Peer-to-Peer)**
   - How Agent Teams work
   - Team lead vs teammates
   - Shared task list
   - Direct messaging
   - When to use Agent Teams vs subagents
   - Configuration and enablement
   - Token cost considerations

6. **Agent Coordination Patterns**
   - Sequential patterns
   - Parallel patterns
   - Swarm patterns
   - Handoff patterns
   - Context sharing

7. **Subagents vs Agent Teams Decision**
   - Decision criteria
   - Cost tradeoffs
   - Use case examples

## Sources to Check

**Required:**
- Claude Code subagent documentation
- Claude Code Agent Teams documentation
- Agent SDK documentation
- https://github.com/anthropics/skills (any agent examples)

**Web Search:**
- "Claude Code subagent 2026"
- "Claude Code Agent Teams"
- "Claude Code Task tool"
- "Claude Code agent patterns"
- "Claude Code peer-to-peer agents"

## Output Requirements

Create your research document at:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase2_session2_agents_subagents.md
```

Use this structure:
```markdown
# Phase 2 Session 2: Agents & Subagents Patterns

## Executive Summary
[5-7 key findings]

## Sources Consulted
| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
...

## Detailed Findings

### Task Tool
[Complete documentation]

### Built-in Subagents
[All types with usage]

### Custom Subagents
[agent.md format and patterns]

### Agent Frontmatter
[Every field with examples]

### Agent Teams
[Complete documentation]

### Coordination Patterns
[All patterns with examples]

### Subagents vs Agent Teams
[Decision criteria]

## Patterns Catalog
1. Pattern: [name]
   - Description: ...
   - When to use: ...
   - Example: ...
...

## Recency Notes
[What changed in 2025/2026, especially Agent Teams]

## Recommendations for Skill-Forge
[What skill-forge should implement]
```

## Do NOT

- Do NOT create the skill-forge skill
- Do NOT summarize superficially - be exhaustive
