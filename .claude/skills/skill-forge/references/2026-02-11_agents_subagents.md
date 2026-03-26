# Phase 2 Session 2: Agents & Subagents Patterns

> **Research Date:** 2026-02-11
> **Research Focus:** External documentation on Claude Code agents, subagents, and Agent Teams
> **Researcher:** Session 2 Worker

---

## Executive Summary

1. **Task Tool is the core mechanism** for spawning subagents - requires `description`, `prompt`, and `subagent_type` parameters; supports `model`, `resume`, and `run_in_background` options

2. **Three built-in subagent types exist**: Explore (fast, read-only, Haiku), Plan (research mode, read-only), and general-purpose (full access, Sonnet) - plus custom agents via agent.md files

3. **Agent Teams (TeammateTool) launched February 2026** with Opus 4.6 - enables peer-to-peer agent communication vs subagents' report-back-only pattern; requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

4. **Custom agents use Markdown with YAML frontmatter** supporting 11+ configuration fields: name, description, tools, disallowedTools, model, permissionMode, skills, memory, hooks, maxTurns, mcpServers

5. **Skills differ from agents fundamentally**: Skills change what an agent *knows* (composable context); Agents change *who is doing the work* (separate workers with isolated tools/context)

6. **Six coordination patterns documented**: Parallel Specialists, Pipeline (Sequential), Swarm (Self-Organizing), Research+Implementation, Plan Approval, and Coordinated Multi-File Refactoring

7. **Decision criterion for subagents vs teams**: "Do workers need to talk to each other?" - If yes, use Agent Teams; if workers just report results, use subagents

---

## Sources Consulted

| Source | URL | Type | Notes |
|--------|-----|------|-------|
| Claude Code Subagents Docs | https://code.claude.com/docs/en/sub-agents | Official | Primary reference for subagent configuration |
| Claude Code Agent Teams Docs | https://code.claude.com/docs/en/agent-teams | Official | Primary reference for Agent Teams |
| Claude Agent SDK Docs | https://platform.claude.com/docs/en/agent-sdk/subagents | Official | SDK integration patterns |
| Claude Code Skills Docs | https://code.claude.com/docs/en/skills | Official | Skills architecture and integration |
| Agent Skills Blog | https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills | Official | Skills deep dive (Dec 2025) |
| Building Agents SDK Blog | https://claude.com/blog/building-agents-with-the-claude-agent-sdk | Official | SDK architecture (Sep 2025) |
| Swarm Orchestration Gist | https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea | Community | Comprehensive pattern reference |
| Task Tool Deep Dive Gist | https://gist.github.com/johnlindquist/d22c70fd70660b4f6fb4d0b05d0792d2 | Community | Task tool implementation details |
| Addy Osmani Swarms Blog | https://addyosmani.com/blog/claude-code-agent-teams/ | Community | Practical Agent Teams guide |
| ClaudeLog Custom Agents | https://claudelog.com/mechanics/custom-agents/ | Community | Agent configuration reference |
| Daniel Miessler Skills Guide | https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents | Community | Skills vs Agents decision framework |
| VoltAgent Subagents Repo | https://github.com/VoltAgent/awesome-claude-code-subagents | Community | 126+ subagent examples |

---

## Detailed Findings

### Task Tool

The Task tool is Claude Code's mechanism for spawning and invoking subagents.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `description` | string | **Yes** | Short (3-5 word) summary of the task |
| `prompt` | string | **Yes** | Detailed instructions for the subagent |
| `subagent_type` | string | **Yes** | Type of agent to spawn (built-in or custom) |
| `model` | enum | No | Override model: `sonnet`, `opus`, `haiku`, or `inherit` |
| `resume` | string | No | Agent ID to resume previous execution |
| `run_in_background` | boolean | No | Run without blocking main conversation |

#### Task Output Schema

```json
{
  "result": "string - final text response",
  "usage": {
    "input_tokens": "number",
    "output_tokens": "number"
  },
  "total_cost_usd": "number (optional)",
  "duration_ms": "number (optional)"
}
```

#### Invocation Patterns

**Automatic Invocation**: Claude evaluates task requirements against subagent descriptions and delegates when appropriate.

**Explicit Invocation**: Name the subagent in the prompt:
```
"Use the code-reviewer agent to check the authentication module"
```

**Parallel Invocation**: Launch multiple agents concurrently in a single message with multiple Task tool calls.

**Resume Pattern**:
1. Capture `session_id` from first query's ResultMessage
2. Extract `agentId` from Task tool results
3. Pass `resume: sessionId` in subsequent query

#### Key Constraints

- Subagents **cannot spawn their own subagents** (prevents infinite nesting)
- Each invocation creates **fresh context** unless explicitly resumed
- Transcripts persist at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`

---

### Built-in Subagents

#### Explore

| Property | Value |
|----------|-------|
| **Model** | claude-haiku-4-5 |
| **Mode** | READ-ONLY |
| **Speed** | 2-5 seconds |
| **Cost** | Low |
| **Tools** | Glob, Grep, Read, Bash (read-only) |

**Purpose**: Fast codebase exploration without modification risk.

**Allowed Bash Commands**: `ls`, `find`, `cat`, `head`, `tail`, `git status`, `git log`, `git diff`, `git show`, `wc`, `file`, `which`, `pwd`, `echo`

**Blocked Operations**: `rm`, `mv`, `cp`, `mkdir`, `touch`, `git commit`, `git push`, `npm install`, any write operations

**Thoroughness Levels**:
- `quick`: Single strategy, first matches
- `medium`: Multiple strategies, moderate depth
- `very thorough`: Exhaustive search, multiple patterns

#### Plan

| Property | Value |
|----------|-------|
| **Model** | claude-sonnet-4 |
| **Mode** | READ-ONLY |
| **Tools** | Read, Grep, Glob (no modifications) |

**Purpose**: Research agent used during plan mode to gather context before presenting implementation plans.

#### General-Purpose

| Property | Value |
|----------|-------|
| **Model** | claude-sonnet-4 |
| **Mode** | FULL ACCESS |
| **Speed** | 10-30 seconds |
| **Tools** | All available tools |

**Purpose**: Complex multi-step tasks requiring both exploration and code modifications.

---

### Custom Subagents

#### agent.md File Format

```markdown
---
name: code-reviewer
description: Expert code review specialist for quality and security
tools: Read, Grep, Glob, Bash
model: opus
permissionMode: default
---

You are a senior code reviewer ensuring high standards...
```

#### Directory Placement & Priority

| Type | Location | Scope | Priority |
|------|----------|-------|----------|
| CLI flag | `--agents` JSON | Session-only | Highest |
| Project | `.claude/agents/` | Current project | High |
| User | `~/.claude/agents/` | All projects | Lower |
| Plugin | `<plugin>/agents/` | Where plugin enabled | Lowest |

---

### Agent Frontmatter Deep Dive

#### Complete Field Reference

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | **Yes** | string | Unique identifier (lowercase letters, hyphens, max 64 chars) |
| `description` | **Yes** | string | Natural language purpose statement; determines when Claude delegates |
| `tools` | No | string/array | Allowlist of available tools; inherits all if omitted |
| `disallowedTools` | No | string/array | Denylist removing tools from inherited/specified set |
| `model` | No | enum | `sonnet`, `opus`, `haiku`, or `inherit` (default) |
| `permissionMode` | No | enum | Permission handling mode |
| `skills` | No | array | Skills to inject into subagent context at startup |
| `memory` | No | enum | Persistent memory scope: `user`, `project`, or `local` |
| `hooks` | No | object | Lifecycle hooks for validation and automation |
| `maxTurns` | No | number | Maximum agentic turns before stopping |
| `mcpServers` | No | array | MCP servers available to subagent |
| `color` | No | string | Display color for agent identification |

#### permissionMode Values

| Mode | Behavior |
|------|----------|
| `default` | Standard permission checking with user prompts |
| `acceptEdits` | Auto-accept file modifications |
| `dontAsk` | Auto-deny permission requests (allowed tools still work) |
| `delegate` | Coordination mode for agent team leads |
| `bypassPermissions` | Skip all checks (use cautiously) |
| `plan` | Read-only exploration mode |

#### tools Field Patterns

**Basic list**:
```yaml
tools: Read, Grep, Glob, Bash
```

**Restricting Subagent Spawning**:
```yaml
tools: Task(worker, researcher), Read, Bash
```

**Bash Patterns**:
```yaml
tools: Bash(git:*), Bash(npm:*), Read
```

#### memory Field

| Scope | Location |
|-------|----------|
| `user` | `~/.claude/agent-memory/<name>/` |
| `project` | `.claude/agent-memory/<name>/` |
| `local` | `.claude/agent-memory-local/<name>/` |

Subagent automatically reads first 200 lines of `MEMORY.md` at startup.

#### hooks Field

```yaml
hooks:
  PreToolUse:
    - matcher: "Edit"
      type: command
      command: "./scripts/validate-edit.sh"
  PostToolUse:
    - type: command
      command: "./scripts/format-code.sh"
  Stop:
    - type: command
      command: "./scripts/cleanup.sh"
```

**Hook Exit Codes**:
- `0`: Allow operation
- `2`: Block operation; passes stderr message to Claude

---

### Agent Teams (Peer-to-Peer)

#### Overview

Agent Teams coordinate multiple Claude Code instances working collaboratively. Released February 6, 2026 with Opus 4.6.

**Key Difference from Subagents**: Teammates talk to each other directly. Subagents only report back to the caller.

#### Architecture

| Component | Function |
|-----------|----------|
| **Team Lead** | Primary session - creates teams, spawns teammates, coordinates work |
| **Teammates** | Separate Claude instances handling assigned tasks independently |
| **Task List** | Shared work items at `~/.claude/tasks/{team-name}/` |
| **Mailbox** | Messaging infrastructure at `~/.claude/teams/{team-name}/inboxes/` |

#### Configuration & Enablement

**Enable via settings.json**:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

**Display Modes**:

| Mode | Description | Navigation |
|------|-------------|------------|
| `in-process` (default) | All teammates in main terminal | Shift+Up/Down |
| `tmux` | Individual panes per teammate | Click panes |
| `iterm2` | Split panes (macOS only) | Click panes |

#### Starting Teams

**Natural Language**:
```
"Create an agent team to explore this from different angles"
"Spawn 4 teammates to refactor these modules in parallel"
```

**Programmatic**:
```javascript
// Create team
Teammate({ operation: "spawnTeam", team_name: "project-x" })

// Spawn teammates via Task tool with team_name
Task({
  team_name: "project-x",
  name: "worker-1",
  subagent_type: "general-purpose",
  prompt: "...",
  run_in_background: true
})
```

#### Shared Task List

**Task States**: `pending` -> `in-progress` -> `completed`

**Dependency Management**:
```javascript
TaskCreate({ subject: "Phase 1", description: "..." })
TaskCreate({ subject: "Phase 2", description: "..." })
TaskUpdate({ taskId: "2", addBlockedBy: ["1"] })
// Task #2 auto-unblocks when #1 completes
```

#### Direct Messaging

**Write to Specific Teammate**:
```javascript
Teammate({
  operation: "write",
  target_agent_id: "worker-1",
  value: "Status update: Task #2 unblocked"
})
```

**Broadcast to All** (expensive - use sparingly):
```javascript
Teammate({
  operation: "broadcast",
  name: "team-lead",
  value: "Critical: Halt current work..."
})
```

#### Environment Variables (Available to Teammates)

- `CLAUDE_CODE_TEAM_NAME`
- `CLAUDE_CODE_AGENT_NAME`
- `CLAUDE_CODE_AGENT_ID`
- `CLAUDE_CODE_AGENT_COLOR`
- `CLAUDE_CODE_PLAN_MODE_REQUIRED`

#### Limitations (Experimental)

- No session resumption for in-process teammates
- One team per session maximum
- No nested teams (only leads spawn teammates)
- Lead role is permanent
- Split panes unsupported in VS Code integrated terminal, Windows Terminal, Ghostty

---

### Coordination Patterns

#### 1. Parallel Specialists (Leader Pattern)

**Purpose**: Multiple agents analyze simultaneously without dependencies.

```javascript
Task({ subagent_type: "security-reviewer", prompt: "...", run_in_background: true })
Task({ subagent_type: "performance-checker", prompt: "...", run_in_background: true })
Task({ subagent_type: "architecture-reviewer", prompt: "...", run_in_background: true })
```

#### 2. Pipeline (Sequential Dependencies)

**Purpose**: Work flows through stages; each depends on previous completion.

```javascript
TaskUpdate({ taskId: "2", addBlockedBy: ["1"] })
TaskUpdate({ taskId: "3", addBlockedBy: ["2"] })
```

**Flow**: Research -> Plan -> Implement -> Test

#### 3. Swarm (Self-Organizing)

**Purpose**: Workers autonomously claim tasks from shared pool.

1. Create independent tasks (no dependencies)
2. Spawn multiple workers with identical prompt logic
3. Workers implement claim-work-complete loop

#### 4. Research + Implementation

```javascript
const research = await Task({
  subagent_type: "Explore",
  prompt: "Research OAuth2 patterns..."
})

Task({
  subagent_type: "general-purpose",
  prompt: `Implement based on: ${research.content}`
})
```

#### 5. Plan Approval Workflow

1. Spawn worker with plan mode
2. Worker generates plan, triggers `plan_approval_request`
3. Leader reviews and approves/rejects
4. Worker proceeds only after approval

#### 6. Coordinated Multi-File Refactoring

```javascript
TaskCreate({ subject: "Refactor User model" })          // Task #1
TaskCreate({ subject: "Refactor Session controller" })  // Task #2
TaskCreate({ subject: "Update specs" })                 // Task #3
TaskUpdate({ taskId: "3", addBlockedBy: ["1", "2"] })
```

---

### Subagents vs Agent Teams

#### Decision Criteria

| Question | Answer | Use |
|----------|--------|-----|
| Do workers need to talk to each other? | No | Subagents |
| Do workers need to talk to each other? | Yes | Agent Teams |
| Is this a focused task with single result? | Yes | Subagents |
| Does work require discussion/collaboration? | Yes | Agent Teams |
| Is token budget a concern? | Yes | Subagents |

#### Comparison Matrix

| Aspect | Subagents | Agent Teams |
|--------|-----------|-------------|
| **Communication** | Report to main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages everything | Shared task list with self-coordination |
| **Context** | Own window; results summarized back | Own window; fully independent |
| **Token Cost** | No documented multiplier | 7x in plan mode (official); implementation mode undocumented |
| **Best For** | Focused tasks | Complex parallel work |

---

### Skills vs Agents

| Aspect | Skills | Agents |
|--------|--------|--------|
| **Purpose** | Change what the agent knows | Change who is doing the work |
| **Execution** | Run inline within current conversation | Fully encapsulated with isolated tools |
| **Storage** | `.claude/skills/` or `~/.claude/skills/` | `.claude/agents/` or `~/.claude/agents/` |
| **Invocation** | `/skill-name` or auto-triggered | Task tool with subagent_type |

**Key Insight**: "Skills prepare Claude to solve a problem, rather than solving it directly."

---

## Patterns Catalog

### Pattern 1: Read-Only Explorer

```yaml
---
name: safe-explorer
description: Explores codebase without making changes
tools: Read, Grep, Glob
model: haiku
permissionMode: plan
---
```

### Pattern 2: Specialized Reviewer

```yaml
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash(git diff:*)
model: opus
---
You are a security specialist. Focus on:
- OWASP Top 10 vulnerabilities
- Authentication/authorization flaws
- Input validation gaps
- Secrets exposure
```

### Pattern 3: Implementation Worker

```yaml
---
name: implementation-worker
description: Implements code changes following project patterns
tools: Read, Edit, Write, Grep, Glob, Bash
model: sonnet
---
```

### Pattern 4: Context-Preserving Researcher

```yaml
---
name: research-agent
description: Researches topics with persistent memory
tools: Read, Grep, WebSearch, WebFetch
model: sonnet
memory: project
---
```

### Pattern 5: Coordinated Team Lead

```yaml
---
name: team-coordinator
description: Coordinates implementation workers
tools: Task, Teammate, Read
permissionMode: delegate
model: opus
---
You are a coordinator. Never implement directly.
Spawn specialized workers and coordinate their output.
```

### Pattern 6: Skill-Powered Specialist

```yaml
---
name: frontend-specialist
description: Frontend development following team conventions
tools: Read, Edit, Write, Bash(npm:*)
skills:
  - react-patterns
  - accessibility-guidelines
---
```

---

## Recency Notes

### February 2026 Changes

- **Agent Teams (TeammateTool)** officially launched with Opus 4.6 (February 6, 2026)
- Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to enable
- Still experimental with known limitations

### Late 2025 Changes

- **Agent Skills** published as open standard (December 18, 2025)
- **Claude Agent SDK** renamed from Claude Code SDK (September 2025)
- **Plugins** introduced for packaging subagents, skills, commands, hooks (October 2025)
- **PreToolUse input modification** added in v2.0.10

---

## Recommendations for Skill-Forge

### 1. Core Agent Infrastructure

- **agent.md generator** with complete frontmatter support
- **Directory management** for both `.claude/agents/` and `~/.claude/agents/`
- **Tool restriction patterns** including Task() syntax for controlling subagent spawning

### 2. Built-in Templates

Provide templates for common patterns:
- Read-only explorer
- Implementation worker
- Specialized reviewer
- Research agent with memory
- Team coordinator

### 3. Frontmatter Validation

Validate all fields:
- `name`: lowercase, hyphens, max 64 chars
- `description`: meaningful for auto-delegation
- `tools`: valid tool names with patterns
- `model`: valid enum values
- `permissionMode`: valid modes

### 4. Skills Integration

- Support `skills` field for preloading skill context
- Understand relationship: Skills = what agent knows; Agents = who does work

### 5. Hook Integration

- Support agent-specific hooks in frontmatter
- Document SubagentStart/SubagentStop lifecycle events

### 6. Agent Teams Awareness

- Document Agent Teams as future capability
- Design agents that work well in team contexts
- Consider `permissionMode: delegate` for coordinator agents

---

## Appendix: Quick Reference

### Task Tool Invocation

```javascript
Task({
  subagent_type: "Explore",         // Required
  description: "Find auth code",     // Required (3-5 words)
  prompt: "Search for auth...",      // Required
  model: "haiku",                    // Optional
  run_in_background: true,           // Optional
  resume: "agent-id-123"             // Optional
})
```

### Agent.md Minimal Template

```yaml
---
name: my-agent
description: Does X when Y
---
Your instructions here.
```

### Agent.md Complete Template

```yaml
---
name: my-agent
description: Does X when Y
tools: Read, Grep, Glob, Edit, Write, Bash
disallowedTools: Task
model: sonnet
permissionMode: default
skills:
  - my-skill
memory: project
hooks:
  PreToolUse:
    - matcher: "Edit"
      type: command
      command: "./validate.sh"
maxTurns: 20
mcpServers:
  - my-mcp-server
---
Your detailed instructions here.
```

### Enable Agent Teams

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```
