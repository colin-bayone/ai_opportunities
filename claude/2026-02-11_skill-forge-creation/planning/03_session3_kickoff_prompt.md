# Session 3 Kickoff: Hooks System Patterns

## Your Mission

You are a research worker for Phase 2 of the skill-forge project. Your job is to research **best practices for Claude Code hooks** from official sources and current 2026 documentation.

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

1. **Hook Events (All of Them)**
   - SessionStart
   - SessionEnd
   - UserPromptSubmit
   - PreToolUse
   - PostToolUse
   - PostToolUseFailure
   - PermissionRequest
   - PreCompact
   - Stop
   - Notification
   - SubagentStart
   - SubagentStop
   - TeammateIdle
   - TaskCompleted
   - Any others

2. **Hook Types**
   - Command hooks (shell scripts)
   - Prompt hooks (LLM evaluation)
   - Agent hooks (subagent verification)
   - When to use each type

3. **Hook Configuration**
   - settings.json format
   - Hook nesting structure
   - Matchers and filtering
   - Location hierarchy (user, project, local, managed)

4. **Hook Input/Output**
   - JSON input format
   - Event-specific fields
   - Exit codes and meaning
   - Output format for decisions
   - hookSpecificOutput patterns

5. **Decision Control**
   - block/allow/ask decisions
   - permissionDecision patterns
   - suggestedInput modification
   - continue flag

6. **Async Hooks**
   - When to use async
   - Configuration
   - Output handling

7. **Hook Use Cases**
   - Skill enforcement
   - Quality gates
   - Security enforcement
   - Auto-formatting
   - Notifications
   - Context injection

8. **Security Considerations**
   - Input validation
   - Path traversal prevention
   - Credential handling

## Sources to Check

**Required:**
- Claude Code hooks documentation
- Claude Code hooks guide
- https://github.com/anthropics/skills (any hook examples)

**Web Search:**
- "Claude Code hooks 2026"
- "Claude Code PreToolUse hook"
- "Claude Code PostToolUse hook"
- "Claude Code hook patterns"
- "Claude Code async hooks"

## Output Requirements

Create your research document at:
```
/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-11_skill-forge-creation/research/phase2_session3_hooks_system.md
```

Use this structure:
```markdown
# Phase 2 Session 3: Hooks System Patterns

## Executive Summary
[5-7 key findings]

## Sources Consulted
| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
...

## Detailed Findings

### Hook Events
| Event | Trigger | Use Case |
|-------|---------|----------|
...

### Hook Types
[Command, Prompt, Agent with examples]

### Configuration
[settings.json format and patterns]

### Input/Output Format
[Complete format documentation]

### Decision Control
[All decision patterns]

### Async Hooks
[Configuration and usage]

### Use Cases
[Detailed examples for each]

### Security
[Best practices]

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
