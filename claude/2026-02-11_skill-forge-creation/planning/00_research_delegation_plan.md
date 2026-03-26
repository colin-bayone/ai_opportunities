# Skill-Forge Research Delegation Plan

**Session:** 2026-02-11_skill-forge-creation
**Master Session:** This document coordinates Phase 2 research across 4 Claude Code worker sessions

---

## Phase 2: Best Practices Research (EXTERNAL ONLY)

**Scope:** Claude Code patterns and best practices for 2026/late 2025
**Sources:** Official Anthropic docs, GitHub repos, web research
**NOT in scope:** Local .claude/ folder (that's Phase 3)

### Research Principles

1. **Recency wins** - More recent documentation always takes precedence
2. **Anthropic docs win** - Official sources override community content
3. **Calibrate for 2025/2026** - Some content may be outdated, note when patterns have changed
4. **Be exhaustive** - Capture everything, not just highlights

### Primary Sources

- https://github.com/anthropics/skills
- https://github.com/anthropics/skills/tree/main/skills/skill-creator
- Claude Code official documentation
- Anthropic blog posts and announcements
- Web search for current patterns

---

## 4-Session Delegation

### Session 1: Skill Structure & SKILL.md Patterns
**Focus:** How to build skills - structure, frontmatter, instructions

**Research:**
- Official skill structure documentation
- SKILL.md format and frontmatter fields
- Skill triggering via description
- Skill invocation patterns (user vs model)
- allowed-tools and tool restrictions
- Skill directory organization
- When to use skills vs commands vs agents

**Sources to check:**
- https://github.com/anthropics/skills (README, docs)
- https://github.com/anthropics/skills/tree/main/skills/skill-creator
- Official Claude Code skill documentation
- Web: "Claude Code skill best practices 2026"

**Output:** `research/phase2_session1_skill_structure.md`

---

### Session 2: Agents & Subagents Patterns
**Focus:** Task tool, subagents, Agent Teams, multi-agent coordination

**Research:**
- Task tool usage and parameters
- Built-in subagent types (Explore, Plan, etc.)
- Custom subagent creation (agent.md files)
- Agent frontmatter patterns (tools, permissions, skills, model)
- Agent Teams (peer-to-peer) patterns
- Subagents vs Agent Teams decision criteria
- Parallel execution patterns
- Agent coordination and handoffs
- Context isolation between agents

**Sources to check:**
- Claude Code subagent documentation
- Claude Code Agent Teams documentation
- Agent SDK documentation
- Web: "Claude Code agent patterns 2026"
- Web: "Claude Code Agent Teams examples"

**Output:** `research/phase2_session2_agents_subagents.md`

---

### Session 3: Hooks System Patterns
**Focus:** All hook types, configuration, enforcement, async

**Research:**
- All hook events (PreToolUse, PostToolUse, SessionStart, Stop, etc.)
- Hook types: command, prompt, agent
- Hook configuration in settings.json
- Hook matchers and filtering
- Async hooks patterns
- Hook input/output format
- Decision control (block, allow, ask)
- Security considerations
- Hooks for skill enforcement
- Hooks for quality gates

**Sources to check:**
- Claude Code hooks documentation
- Claude Code hooks guide
- Web: "Claude Code hooks best practices 2026"
- Web: "Claude Code PreToolUse examples"

**Output:** `research/phase2_session3_hooks_system.md`

---

### Session 4: Scripts, Context & Progressive Disclosure
**Focus:** Script integration, context management, token efficiency

**Research:**
- Script integration in skills (Python, Bash)
- When to use scripts vs LLM reasoning
- Script input/output patterns
- Progressive disclosure (3-tier loading)
- Context window management
- Token budget considerations
- Reference files organization
- When to load resources
- CLAUDE.md patterns
- Settings integration (permissions, environment)

**Sources to check:**
- Claude Code best practices documentation
- Claude Code settings documentation
- anthropic/skills examples with scripts
- Web: "Claude Code progressive disclosure"
- Web: "Claude Code context management"

**Output:** `research/phase2_session4_scripts_context.md`

---

## Coordination Protocol

### For Each Worker Session

1. **Read your scope** from this plan
2. **Do web research** - search for current 2026 patterns
3. **Fetch official docs** - prioritize Anthropic sources
4. **Check GitHub repos** - anthropic/skills, skill-creator
5. **Document EVERYTHING** - be exhaustive
6. **Note recency** - when was each source last updated?
7. **Flag outdated patterns** - if something seems old, note it

### Output Structure

```markdown
# Phase 2 Session [X]: [Topic]

## Executive Summary
[Key findings - 5-7 bullets]

## Sources Consulted
| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
...

## Detailed Findings

### [Subtopic 1]
[Comprehensive documentation]

### [Subtopic 2]
[Comprehensive documentation]

## Patterns Catalog
1. Pattern: [name]
   - Description: ...
   - When to use: ...
   - Example: ...

2. Pattern: [name]
   ...

## Recency Notes
[What's new in 2025/2026 vs older patterns]

## Recommendations for Skill-Forge
[What skill-forge should implement based on this research]
```

---

## Success Criteria

Each session must produce:
1. **Exhaustive documentation** of their topic area
2. **Source citations** with recency notes
3. **Pattern catalog** for skill-forge to use
4. **Recency calibration** - what's current vs outdated
5. **Clear recommendations** for skill-forge implementation

---

## What Comes Next

After Phase 2 completes (all 4 sessions):
- Master session synthesizes findings
- **Phase 3**: Investigate local .claude/ skills, agents, scripts
- Then: Design and build skill-forge
