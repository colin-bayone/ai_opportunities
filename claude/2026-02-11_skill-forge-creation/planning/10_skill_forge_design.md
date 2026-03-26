# Skill-Forge Design Document

**Date:** 2026-02-11
**Status:** Final design, ready for implementation

---

## Overview

Skill-forge is a Claude Code skill that helps users create skills, agents, and hooks. It replaces the existing skill-creator with improvements based on 2026 best practices and lessons from local skill patterns.

---

## Scope

Skill-forge creates:
- **Skills** - SKILL.md + scripts/ + references/
- **Agents** - agent.md files at `.claude/agents/`
- **Hooks** - Compliance and enforcement hooks

---

## Workflow

### Step 0: Onboarding

Ask user one question with three paths:
1. "I need help understanding what's possible" → Education mode
2. "Give me a quick list of features" → Feature summary
3. "I know what I want" → Skip to Step 1

**Education mode:** Explain features briefly, show short examples, support brainstorming.

### Step 1: Understand

Ask what they want to build. If education mode, help them figure it out here.

Key questions:
- What does this skill do?
- When should Claude invoke it automatically? (Help write "WHEN + WHEN NOT" description)
- Will it need deterministic scripts or is LLM reasoning enough?
- Does it need multiple agents? What roles?
- Should hooks enforce compliance?

### Step 2: Plan

Identify what's needed based on answers:
- SKILL.md structure and content
- Scripts (if any)
- References (if any)
- Agents (if any) - always at `.claude/agents/`
- Hooks (if any) - explain trade-offs, let user decide

### Step 3: Generate

Create the files:
- SKILL.md with proper frontmatter
- scripts/ folder with Python/Bash as needed
- references/ folder if needed
- agent.md files at `.claude/agents/`
- Hook scripts at `.claude/hooks/`

### Step 4: Validate

Run checks:
- Frontmatter schema validation
- Token estimation (character count / 4)
- Warn if SKILL.md exceeds ~5K tokens
- Suggest splitting to references if needed (with caveat that references may not get called)
- Offer to generate hooks that ensure critical references get loaded

### Step 5: Iterate

Support refinement based on real usage.

---

## Standards (Strict Schema)

### SKILL.md Frontmatter

Required:
```yaml
name: skill-name  # 1-64 chars, lowercase alphanumeric + hyphens
description: |
  What this skill does.

  WHEN to use: [triggers]
  WHEN NOT to use: [exclusions]
```

Optional:
```yaml
disable-model-invocation: false
user-invocable: true
allowed-tools: [tool1, tool2]
model: sonnet
```

### Section Naming

Use consistent names:
- "Hard Rules" (not "Hard Constraints", "Core Philosophy", "Safety Rules")
- "Workflow" for step-by-step processes
- "References" for linking to reference files

### Agent Location

All agents at `.claude/agents/`, never nested inside skill folders.

### Agent Frontmatter

```yaml
name: agent-name
description: What this agent does and when to invoke it
model: sonnet  # or opus, haiku
tools: [Read, Edit, Bash]  # if restricting
permissionMode: default  # or plan, acceptEdits, etc.
```

---

## Scripts

### Token Estimation Script

`scripts/estimate_tokens.py`
- Read file content
- Return character count / 4 as rough token estimate
- Warn threshold: ~5000 tokens (~20000 characters)

### Scaffolding Script

`scripts/scaffold.py`
- Generate SKILL.md from template
- Generate agent.md files
- Generate hook scripts
- Create directory structure

### Validation Script

`scripts/validate.py`
- Check frontmatter schema
- Check naming conventions
- Check token limits
- Report issues

---

## Agent Teams

Skill-forge itself uses traditional subagents (not Agent Teams).

When helping users:
- Default to subagent patterns
- Ask user if they want Agent Team-enabled skills
- Explain 7x token cost in plan mode (official)
- Only recommend teams when workers need to talk to each other

---

## Hooks

When user wants hooks:
1. Explain trade-offs briefly
2. Offer to generate compliance hooks (exit code 2 blocking)
3. Offer reference-loading enforcement hooks
4. Generate with explanation of what each hook does

---

## Progressive Disclosure

Skill-forge practices what it preaches:
- SKILL.md under 5K tokens
- Detailed patterns in references/
- Research docs as dated references (2026-02-11)

---

## File Structure

```
.claude/skills/skill-forge/
├── SKILL.md                          # Main skill (<5K tokens)
├── scripts/
│   ├── estimate_tokens.py            # Token estimation
│   ├── scaffold.py                   # File generation
│   └── validate.py                   # Validation checks
└── references/
    ├── 2026-02-11_skill_structure.md           # Phase 2 Session 1
    ├── 2026-02-11_agents_subagents.md          # Phase 2 Session 2
    ├── 2026-02-11_hooks_system.md              # Phase 2 Session 3
    ├── 2026-02-11_scripts_context.md           # Phase 2 Session 4
    ├── 2026-02-11_django_forge_patterns.md     # Phase 3 Session 1
    ├── 2026-02-11_pr_review_patterns.md        # Phase 3 Session 2
    ├── 2026-02-11_phoenix_patterns.md          # Phase 3 Session 3
    ├── 2026-02-11_cross_cutting_patterns.md    # Phase 3 Session 4
    └── 2026-02-11_new_features.md              # Phase 1 summary
```

---

## Implementation Order

1. Create directory structure
2. Copy/adapt research docs as dated references
3. Build scripts (estimate_tokens.py, scaffold.py, validate.py)
4. Build SKILL.md with workflow and standards
5. Test with sample skill creation
