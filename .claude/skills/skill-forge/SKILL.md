---
name: skill-forge
description: |
  Create Claude Code skills, agents, and hooks with 2026 best practices.

  WHEN to use: User wants to create a new skill, agent, or hook. User asks about skill structure, best practices, or needs help understanding skill features. User wants to scaffold a skill project.

  WHEN NOT to use: User is working on an existing skill and just needs edits. User is asking general Claude Code questions not about skill creation.
---

# Skill-Forge

Create skills, agents, and hooks following 2026 best practices.

---

## MANDATORY: Pre-Flight Checks (Run EVERY Time)

**Before doing ANYTHING else, run these two checks. They are non-negotiable.**

### Check 1: Agent Write Permissions

```bash
python3 .claude/skills/skill-forge/scripts/check_agent_write_permissions.py
```

If status is "missing", **STOP and tell the user**. They need to add this to `.claude/settings.local.json` under `permissions.allow`:
```
Write($CLAUDE_PROJECT_DIR/.claude/skills/skill-forge/**)
```

This permission is required for the self-update agent to write research files. Without it, skill-forge cannot keep itself current.

### Check 2: Staleness Check

```bash
python3 .claude/skills/skill-forge/scripts/check_staleness.py
```

If stale (>30 days since last update), **show the user the report** and offer:
> "Skill-forge references are {X} days old. Would you like me to run the skill-forge-updater agent to refresh them before we proceed?"

If the user says yes, invoke the `skill-forge-updater` agent and wait for it to complete before proceeding with the skill creation workflow.

If the user says no or it's not stale, proceed normally.

---

## MANDATORY: Follow This Workflow Exactly

**DO NOT skip steps. DO NOT jump to generating files. DO NOT assume what the user wants.**

When skill-forge is invoked (after pre-flight checks pass):

1. **FIRST** - Ask the onboarding question (Step 0) and WAIT for the user's answer
2. **SECOND** - Read the required reference files based on what they want to build
3. **THIRD** - Go through the questionnaire (Step 1) to deeply understand their needs
4. **FOURTH** - Plan what's needed (Step 2) with user input
5. **FIFTH** - Only THEN generate the files (Step 3)

**Why this matters:**
- Many users don't know all the features available (hooks, agents, scripts, etc.)
- The questionnaire helps them think through their needs and produces better skills
- Skipping steps produces mediocre, generic skills instead of tailored solutions
- The Stop hook will block completion if references weren't read

---

## Hard Rules

1. Agents always go at `.claude/agents/`, never nested inside skill folders
2. Use strict schema for frontmatter (name, description required)
3. Use "Hard Rules" as section name (not "Hard Constraints", "Core Philosophy", etc.)
4. Estimate tokens as character count / 4
5. Warn if SKILL.md exceeds ~5K tokens, but don't block
6. Always help write "WHEN to use" and "WHEN NOT to use" in descriptions
7. References must be one level deep from SKILL.md (no nested references)
8. Help users understand options without being tedious—ask follow-up questions based on their answers, don't dump all options at once
9. Document all available fields in generated skills so users know what's possible, even if not all are used
10. **Read relevant references before generating** - skill-forge eats its own cooking

## Eating Our Own Cooking

Skill-forge enforces its own best practices via a Stop hook (`.claude/hooks/skill-forge-references.py`).

Before generating output, you MUST read the relevant references. **Use these exact paths:**

- **Creating a skill?** → Read `.claude/skills/skill-forge/references/2026-02-11_skill_structure.md` and `.claude/skills/skill-forge/references/2026-02-11_scripts_context.md`
- **Creating an agent?** → Read `.claude/skills/skill-forge/references/2026-02-11_agents_subagents.md`
- **Creating hooks?** → Read `.claude/skills/skill-forge/references/2026-02-11_hooks_system.md`

**IMPORTANT:** References are at `.claude/skills/skill-forge/references/`, NOT at `.claude/hooks/references/`.

The hook will block completion if required references weren't consulted. This solves the "LLM skips steps" problem with deterministic enforcement.

## Workflow

### Step 0: Onboarding (MANDATORY - DO NOT SKIP)

**STOP. Before doing anything else, ask this EXACT question and WAIT for the user's response:**

> **"How would you like to start?"**
> 1. **Help me understand** - I'm not sure what skills can do, explain the options
> 2. **Quick overview** - Give me a brief list of features, then I'll describe what I need
> 3. **I know what I want** - Let me describe my requirements

**DO NOT proceed until the user responds. DO NOT assume option 3.**

---

**If user chooses 1 (help):** Enter education mode.

Explain what skill-forge can create:
- **Skills** - SKILL.md files that give Claude specialized knowledge or workflows
- **Agents** - Standalone workers that Claude can delegate tasks to
- **Hooks** - Deterministic enforcement rules that block/allow actions
- **Scripts** - Python/Bash for exact operations Claude shouldn't improvise

Ask about their pain point or goal. Help them brainstorm. Read `.claude/skills/skill-forge/references/2026-02-11_skill_structure.md` to understand patterns and share relevant examples.

---

**If user chooses 2 (overview):** Provide this feature list, then ask what interests them:

| Feature | What It Does | Example Use Case |
|---------|-------------|------------------|
| **Skills** | SKILL.md + scripts/, references/ | Domain knowledge, guided workflows |
| **Agents** | Delegated workers at `.claude/agents/` | Research, implementation, quality checks |
| **Hooks** | Compliance enforcement (exit code 2 blocks) | Prevent commits without tests, enforce reviews |
| **Scripts** | Deterministic Python/Bash operations | Token estimation, validation, scaffolding |
| **Subagents** | Parallel exploration via Task tool | Research multiple topics simultaneously |
| **Agent Teams** | Peer-to-peer agent coordination | Complex multi-agent workflows |

After showing this, ask: "What sounds most relevant to what you're trying to build?"

---

**If user chooses 3 (ready):** Proceed to Step 1, but STILL ask the core questions. Even experienced users benefit from the questionnaire.

### Step 1: Understand (MANDATORY - DO NOT SKIP)

**Before generating anything, you MUST understand deeply what the user needs.**

Ask these questions ONE AT A TIME, waiting for answers:

**Question 1:** "What should this skill/agent/hook do? Describe the problem it solves."

**Question 2:** "When should Claude automatically use this? What triggers would indicate it's relevant?"

**Question 3:** "When should Claude NOT use this? What might seem related but isn't?"

---

**Based on their answers, ask follow-up questions:**

- Does this need deterministic scripts? (For fragile tasks where Claude shouldn't improvise)
- Does this need reference documentation? (For complex domains with lots of detail)
- Does this need multiple agents? (For workflows with distinct roles)
- Should hooks enforce rules? (For compliance, safety, or quality gates)
- Does this skill produce artifacts? (If yes, use dedicated output folder)

**If they mention agents, ask:**
- What model? (haiku = fast/cheap, sonnet = balanced, opus = complex reasoning)
- Read-only or can edit? (permissionMode: plan vs default)
- Do agents need to talk to each other? (Subagents vs Agent Teams)

---

**Help write the description.** The "WHEN to use" and "WHEN NOT to use" pattern achieves 84% auto-activation vs 20% baseline.

Draft a description WITH the user:

```yaml
description: |
  [What it does - one sentence]
  WHEN to use: [Specific triggers - user mentions X, asks about Y, wants to Z]
  WHEN NOT to use: [Exclusions - things that seem related but aren't]
```

**Get their approval on the description before proceeding.**

### Step 2: Plan

Based on answers, identify what's needed:
- SKILL.md structure
- scripts/ folder (Python or Bash)
- references/ folder (detailed docs loaded on-demand)
- Agents at `.claude/agents/`
- Hooks at `.claude/hooks/`

**If user wants hooks**, explain trade-offs:
- Pro: Deterministic enforcement, solves "LLM skips steps" problem
- Con: More complexity, requires exit code 2 pattern
- Recommend for: Compliance workflows, quality gates, safety-critical operations

**Ask about hook scoping:**
- "Should this hook fire on every session, or only when this skill is active?"
- **Global hooks:** Fire always (security gates, formatting, logging)
- **Skill-scoped hooks:** Fire only when skill is in use (workflow enforcement)

**For skill-scoped Stop hooks, use the marker file pattern:**
1. Skill creates marker file at start (e.g., `claude/<skill-name>/.active`)
2. Hook checks for marker; exits 0 immediately if not present
3. Skill removes marker when workflow is complete
4. This prevents the hook from blocking unrelated sessions

**If user wants agents**, walk through configuration:

1. **Communication pattern:**
   - Do agents need to talk to each other? (Yes = consider Agent Teams, 7x tokens in plan mode)
   - Default to traditional subagents (lower cost, simpler)

2. **Model selection** (help them choose):
   - What's the task complexity? (Simple exploration = haiku, Complex reasoning = opus)
   - Is cost a concern? (Yes = haiku/sonnet, No = opus for quality)
   - Is speed critical? (Yes = haiku, No = sonnet/opus)

3. **Tool access:**
   - Read-only agent? → `tools: Read, Grep, Glob` + `permissionMode: plan`
   - Implementation agent? → Include Edit, Write, Bash
   - Should it spawn subagents? → Include or exclude Task tool

4. **Additional configuration** (ask if relevant):
   - Need persistent memory? → Set `memory: project` or `user`
   - Need skills preloaded? → Add `skills: [skill-names]`
   - Need turn limits? → Set `maxTurns`
   - Need agent-specific hooks? → Add `hooks` section

**If user wants scripts**, ask about fragility:
- High freedom (flexible tasks) → Text instructions in SKILL.md
- Medium freedom (guided operations) → Parameterized scripts
- Low freedom (exact sequence required) → Deterministic scripts with no parameters

### Step 3: Generate

**First, show the user the plan:**
```bash
python scripts/scaffold.py <skill-name> .claude/skills/<skill-name> --with-scripts --with-references --with-hooks --plan
```

**Show the user where files will be created and confirm before proceeding:**
- Skill directory: `.claude/skills/<skill-name>/`
- SKILL.md location
- scripts/ location
- references/ location
- Hook location (at `.claude/hooks/`, NOT inside skill folder)
- Settings file location

**After user confirms, create the files:**
```bash
python scripts/scaffold.py <skill-name> .claude/skills/<skill-name> --with-scripts --with-references --with-hooks
```

For agents, create at `.claude/agents/<agent-name>.md`

For hooks, create at `.claude/hooks/<hook-name>.py`

**For skills that produce artifacts** (documents, reports, analysis):
- Use a dedicated output hierarchy under the skill: `claude/<skill-name>/`
- NOT scattered at the root under session folders like `claude/<date>_<topic>/`
- Per-run subfolders under the skill folder are fine
- This makes artifacts findable and hooks can reliably locate them
- Example: `claude/meeting-analyzer/meeting_kickoff_2026-02-17/` (per-run subfolder under skill)

**IMPORTANT:** Always use absolute paths in generated skills. For example:
- `.claude/skills/<skill-name>/references/file.md` (not `references/file.md`)
- `.claude/skills/<skill-name>/scripts/helper.py` (not `scripts/helper.py`)

Fill in generated templates with user's content.

### Step 3.5: Configure Settings (IMPORTANT)

**After generating files, help the user configure settings.local.json.**

For skills with hooks, add hook configuration:
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/.claude/hooks/<hook-name>.py",
            "timeout": 10000,
            "statusMessage": "Running <hook-name>..."
          }
        ]
      }
    ]
  }
}
```

For skills with scripts that need permissions:
```json
{
  "permissions": {
    "allow": [
      "Bash(python3 $CLAUDE_PROJECT_DIR/.claude/skills/<skill-name>/scripts/*)",
      "Read",
      "Glob",
      "Grep"
    ]
  }
}
```

**Show the user the exact settings.local.json entries needed and confirm before adding them.**

**If settings.local.json doesn't exist, create it. If it exists, merge the new entries.**

### Step 4: Validate

Run validation:
```bash
python scripts/validate.py .claude/skills/<skill-name>
```

Check:
- Frontmatter schema (name, description required)
- Token estimate (warn if >5K)
- Agent location (must be at `.claude/agents/`)
- No nested references (all should link directly from SKILL.md)
- Table of contents present in references >100 lines

If tokens exceed threshold:
- Suggest moving detailed content to references/
- Warn that references are on-demand and may not always be called
- Offer to generate hooks that ensure critical references get loaded

**Generating reference-loading hooks** (if user wants guaranteed loading):

Create a PreToolUse or SessionStart hook that checks if critical references were read:

```bash
# .claude/hooks/ensure_references.sh
#!/bin/bash
INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id')
TRANSCRIPT="$HOME/.claude/projects/*/sessions/$SESSION_ID/transcript.jsonl"

# Check if critical reference was loaded
if ! grep -q "references/critical.md" $TRANSCRIPT 2>/dev/null; then
    echo "Must read references/critical.md before proceeding" >&2
    exit 2
fi
exit 0
```

Or use a Stop hook to verify references were consulted before task completion.

### Step 5: Iterate

Support refinement:
- Test skill invocation
- Adjust triggering description
- Add/remove agents or hooks as needed

## Scripts

- `scripts/estimate_tokens.py` - Estimate tokens (char/4)
- `scripts/validate.py` - Validate skill structure
- `scripts/scaffold.py` - Generate skill/agent/hook scaffolds
- `scripts/check_staleness.py` - Check if skill-forge references are stale (>30 days)
- `scripts/check_agent_write_permissions.py` - Verify agents can write to references/

## Kickoff Prompts

Example prompts for different user situations. Read these to understand how users might approach skill-forge:

- `kickoff-prompts/01_i_know_what_i_want.md` - User has clear vision, ready to build
- `kickoff-prompts/02_help_me_understand.md` - User has pain point, needs guidance
- `kickoff-prompts/03_multi_agent_workflow.md` - User needs coordinated agents
- `kickoff-prompts/04_compliance_enforcement.md` - User needs deterministic hooks

## References

Detailed patterns from 2026-02-11 research. **All references are at `.claude/skills/skill-forge/references/`**

**Latest (2026-03-28 update):**
- `.claude/skills/skill-forge/references/2026-03-28_new_features_update.md` - All changes Jan–Mar 2026: 26+ hook events, HTTP hooks, new frontmatter fields, 250 char description cap, worktree isolation, auto mode, /batch, plugin system, 1M context

**Original Research (2026-02-11):**
- `.claude/skills/skill-forge/references/2026-02-11_new_features.md` - Summary of Dec 2025 - Feb 2026 features
- `.claude/skills/skill-forge/references/2026-02-11_skill_structure.md` - SKILL.md format, frontmatter, triggering, 8 implementation patterns
- `.claude/skills/skill-forge/references/2026-02-11_agents_subagents.md` - Agent tool, Agent Teams, 6 coordination patterns, model selection
- `.claude/skills/skill-forge/references/2026-02-11_hooks_system.md` - Hook events, 3 types, 8 enforcement patterns (see 2026-03-28 update for current count)
- `.claude/skills/skill-forge/references/2026-02-11_scripts_context.md` - Progressive disclosure, degrees of freedom, token management

**Self-Update System:**
- `.claude/skills/skill-forge/VERSION.md` - Version tracking, update history, known gaps
- `.claude/agents/skill-forge-updater.md` - Self-update agent with parallel research capabilities
- `.claude/hooks/skill-forge-preflight.py` - Enforces pre-flight checks via Stop hook

**Local Patterns (Phase 3 research):**
- `.claude/skills/skill-forge/references/2026-02-11_django_forge_patterns.md` - 14-agent swarm, blackboard pattern, wave execution
- `.claude/skills/skill-forge/references/2026-02-11_pr_review_patterns.md` - Hook compliance, 16-step verification, safety policies
- `.claude/skills/skill-forge/references/2026-02-11_phoenix_patterns.md` - Data catalog pattern, hierarchical indexes, questionnaires
- `.claude/skills/skill-forge/references/2026-02-11_cross_cutting_patterns.md` - Standardization findings, command/skill overlap

## Frontmatter Schema

**IMPORTANT:** Only use officially supported fields. Using unsupported fields may cause validation errors.

### Supported Fields (SKILL.md)

All fields are optional, but `description` is strongly recommended.

```yaml
# Identity & Triggering
name: skill-name                 # 1-64 chars, lowercase + hyphens. Becomes /slash-command name
description: |                   # RECOMMENDED: Claude uses this to auto-trigger. MAX 250 CHARS.
  What this skill does.
  WHEN to use: [triggers]
  WHEN NOT to use: [exclusions]

# Invocation Control
disable-model-invocation: false  # true = manual /name only, prevents auto-triggering
user-invocable: true             # false = hides from slash menu (Claude-only background knowledge)
argument-hint: [file] [options]  # Autocomplete hint showing expected arguments

# Execution Context
context: fork                    # fork = runs skill in isolated subagent context
agent: Explore                   # Subagent type when context: fork (Explore, Plan, general-purpose)
model: sonnet                    # Model override: sonnet, opus, haiku, inherit
effort: medium                   # Model effort level: low, medium, high (v2.1.80)

# Tool Access
allowed-tools: Read, Grep, Bash(git:*)  # Pre-approved tools, supports wildcards

# Path-Based Activation (v2.1.84)
paths:                           # YAML list of glob patterns — skill activates for matching files
  - "src/components/**/*.tsx"
  - "*.css"

# Lifecycle Hooks (skill-scoped)
hooks:                           # Hook automation scoped to this skill
  PreToolUse:
    - matcher: "Edit"
      type: command
      command: "./validate.sh"
```

**CRITICAL: Description cap is 250 characters** (reduced from 1024 in v2.1.86). Front-load the most important trigger condition.

**NOT SUPPORTED (will cause validation errors):**
- `license`, `version`, `compatibility`, `metadata`, `mode`

**Invocation Matrix** (help users understand combinations):

| disable-model-invocation | user-invocable | Result |
|--------------------------|----------------|--------|
| false | true | Default: auto-invoke + manual invoke |
| true | true | Manual only via `/name` |
| false | false | Auto-invoke only (background knowledge) |
| true | false | Effectively disabled |

### Agent Frontmatter

All agents go at `.claude/agents/<name>.md`. When helping users create agents, walk through these fields:

```yaml
# Required
name: agent-name                 # 1-64 chars, lowercase + hyphens
description: |                   # Determines when Claude delegates to this agent
  What this agent does.
  Invoke when: [conditions]

# Model Selection (help user choose)
model: sonnet                    # See model guidance below
effort: medium                   # Model effort: low, medium, high (v2.1.80)

# Tool Access
tools: Read, Grep, Glob, Edit    # Allowlist; inherits all if omitted
disallowedTools: Task            # Denylist; removes from inherited/specified set

# Execution Control
permissionMode: default          # See permission modes below
maxTurns: 20                     # Maximum agentic turns before stopping
isolation: worktree              # Run in isolated git worktree (v2.1.50)
initialPrompt: "Start analyzing" # Auto-submit first turn (v2.1.83)

# Context Enhancement
skills:                          # Skills preloaded into agent context
  - my-skill
  - another-skill
memory: project                  # Persistent memory: user, project, or local

# Hooks (agent-specific — NOT available in plugin agents for security)
hooks:
  PreToolUse:
    - matcher: "Edit"
      type: command
      command: "./validate.sh"

# MCP Integration (NOT available in plugin agents for security)
mcpServers:                      # MCP servers available to this agent
  - my-mcp-server
```

**Model Selection Guidance** (ask user about their needs):

| Model | Cost | Speed | Best For |
|-------|------|-------|----------|
| `haiku` | Low | Fast (2-5s) | Read-only exploration, simple tasks, high volume |
| `sonnet` | Medium | Medium (10-30s) | Balanced work, most implementation tasks |
| `opus` | High | Slower | Complex reasoning, security review, architecture decisions |
| `inherit` | - | - | Use same model as parent (default) |

**Permission Modes** (explain trade-offs):

| Mode | Behavior | Use When |
|------|----------|----------|
| `default` | Standard permission prompts | Normal operation |
| `plan` | Read-only, no modifications | Research/exploration agents |
| `acceptEdits` | Auto-accept file changes | Trusted implementation workers |
| `auto` | AI classifier approves/blocks (research preview) | Teams wanting smart auto-approval |
| `dontAsk` | Auto-deny permission requests | Restricted agents (allowed tools still work) |
| `bypassPermissions` | Skip all checks | Use cautiously, testing only |

**Memory Scopes** (if user needs persistence):

| Scope | Location | Use When |
|-------|----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | Personal preferences across projects |
| `project` | `.claude/agent-memory/<name>/` | Project-specific learned context |
| `local` | `.claude/agent-memory-local/<name>/` | Machine-specific, not committed |

### Hook Configuration

When user wants hooks, create at `.claude/hooks/` or in settings.json:

```yaml
# Hook in settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",              # Regex pattern for tool name
        "hooks": [
          {
            "type": "command",          # command, prompt, agent, or http
            "command": ".claude/hooks/validate.sh",
            "timeout": 60000,           # ms, default 600000 (10 min)
            "async": false,             # true = non-blocking background
            "if": "Bash(git *)"         # Conditional filter (v2.1.85)
          }
        ]
      }
    ]
  }
}
```

**Hook Types** (4 available):
- `command` — Shell script, receives JSON via stdin, exit codes control behavior
- `prompt` — Single-turn LLM evaluation, returns `{"ok": true/false, "reason": "..."}`
- `agent` — Multi-turn subagent with tool access (Read, Grep, Glob), 60s timeout
- `http` — POST event data as JSON to HTTP endpoint (v2.1.63)

**Hook Events** (26+ available — see `2026-03-28_new_features_update.md` for full list):

| Event | Blocking | Use For |
|-------|----------|---------|
| `PreToolUse` | Yes | Security checks, input modification, auto-approval |
| `PostToolUse` | No | Auto-formatting, logging, quality checks |
| `Stop` | Yes | Task completion verification |
| `StopFailure` | No | Handle API errors at turn end |
| `SessionStart` | No | Context injection, environment setup |
| `SessionEnd` | No | Cleanup, final logging |
| `UserPromptSubmit` | Yes | Prompt validation |
| `SubagentStart/Stop` | No/Yes | Subagent tracking, output validation |
| `TaskCreated` | Yes | Block/validate task creation |
| `TaskCompleted` | Yes | Completion criteria enforcement |
| `TeammateIdle` | Yes | Multi-agent workflow control |
| `WorktreeCreate/Remove` | Yes | Worktree lifecycle |
| `PreCompact/PostCompact` | No | Context preservation |
| `InstructionsLoaded` | No | Detect CLAUDE.md loading |
| `ConfigChange` | No | React to settings changes mid-session |
| `CwdChanged/FileChanged` | No | Working directory and file watchers |
| `Elicitation/ElicitationResult` | Yes/No | MCP server user input |

**Exit Codes** (for command hooks):
- `0` = Allow, continue
- `2` = Block action, stderr message fed to Claude
- Other = Non-blocking error
