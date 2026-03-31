# Claude Code Features Update: January – March 2026

> **Research Date:** 2026-03-28
> **Researcher:** skill-forge-updater parallel research agents
> **Covers:** v2.1.0 (Jan 7) through v2.1.86 (Mar 27)
> **Previous Coverage:** 2026-02-11 (through early Feb 2026)

---

## Executive Summary

1. **Hook system exploded from 14 to 26+ events** — New events: `TaskCreated`, `WorktreeCreate/Remove`, `PostCompact`, `Elicitation/ElicitationResult`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `FileChanged`, `StopFailure`. New handler type: `"type": "http"` for webhook-style hooks. New `if` field for conditional filtering.

2. **New skill frontmatter fields** — `effort` (model effort override), `initialPrompt` (auto-submit first turn), `paths:` (YAML glob list for path matching), plus `disallowedTools` and `maxTurns` for agents. **Skill description cap reduced to 250 characters** (was 1024).

3. **Worktree isolation for agents** — `isolation: "worktree"` gives each agent its own git worktree, eliminating merge conflicts. `--worktree` CLI flag. `EnterWorktree`/`ExitWorktree` tools.

4. **Named agents with SendMessage** — Agents get addressable names via `name` parameter, enabling direct inter-agent communication with `SendMessage({to: "agent-name"})`.

5. **`auto` permission mode** — AI-powered classifier auto-approves safe operations and blocks dangerous ones. Research preview. Configurable via `autoMode` settings.

6. **Plugin system matured** — `source: 'settings'` inline plugins, `git-subdir` source, `/reload-plugins`, `managed-settings.d/` drop-in directory, `blockedMarketplaces`, `claude plugin validate`.

7. **Remote/Cloud execution** — Remote Control bridges terminal to claude.ai/code. Scheduled cloud tasks via `/schedule`. `/loop` for recurring local tasks. Channels for external system push.

8. **1M context window** for Opus 4.6 (was 200K). 64K default output, 128K max. Sonnet 4.6 added.

9. **`/batch` command** — Codebase-wide parallel changes with per-file agents in isolated worktrees.

10. **Auto-memory** — Claude automatically saves context to `MEMORY.md`. `/memory` command.

---

## Detailed Changes by Category

### New Skill Frontmatter Fields

| Field | Version | Description |
|---|---|---|
| `effort` | v2.1.80 (Mar 20) | Override model effort level: low, medium, high |
| `initialPrompt` | v2.1.83 (Mar 25) | Auto-submit first turn when agent spawned |
| `paths:` | v2.1.84 (Mar 26) | YAML list of glob patterns for path-based activation |
| `disallowedTools` | v2.1.78 (Mar 18) | Per-agent tool restrictions in frontmatter |
| `maxTurns` | v2.1.78 (Mar 18) | Limit agent turns in frontmatter |

**BREAKING**: Skill description cap reduced from 1024 to **250 characters** (v2.1.86, Mar 27). Front-load the key use case.

### New Hook Events (Added Since Feb 2026)

| Event | Version | Blocking | Fires When |
|---|---|---|---|
| `TaskCreated` | v2.1.84 (Mar 26) | Yes | Task being created via TaskCreate |
| `WorktreeCreate` | v2.1.77 (Mar 17) | Yes | Worktree being created |
| `WorktreeRemove` | v2.1.77 (Mar 17) | Yes | Worktree being removed |
| `PostCompact` | v2.1.76 (Mar 14) | No | After context compaction completes |
| `Elicitation` | v2.1.76 (Mar 14) | Yes | MCP server requests user input |
| `ElicitationResult` | v2.1.76 (Mar 14) | No | After user responds to MCP elicitation |
| `InstructionsLoaded` | v2.1.69 (Mar 5) | No | CLAUDE.md or rules file loaded |
| `ConfigChange` | v2.1.49 (Feb 19) | No | Configuration file changes during session |
| `CwdChanged` | v2.1.83 (Mar 25) | No | Working directory changes |
| `FileChanged` | v2.1.83 (Mar 25) | No | Watched file changes on disk |
| `StopFailure` | v2.1.78 (Mar 18) | No | Turn ends due to API error |

### New Hook Handler Type: HTTP

```json
{
  "type": "http",
  "url": "https://hooks.example.com/claude",
  "timeout": 30000,
  "allowedEnvVars": ["WEBHOOK_TOKEN"]
}
```

POST event data as JSON. Response uses same format as command hooks. Added v2.1.63 (Feb 28).

### Conditional Hook `if` Field (v2.1.85)

Per-hook filtering beyond group-level matcher:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "if": "Bash(git *)",
        "command": ".claude/hooks/check-git-policy.sh"
      }]
    }]
  }
}
```

### Agent Tool Evolution

The `Agent` tool now replaces/enhances the `Task` tool with these parameters:

| Parameter | Type | Description |
|---|---|---|
| `description` | string | Short (3-5 word) summary |
| `prompt` | string | Detailed instructions |
| `subagent_type` | string | Agent type (built-in or custom) |
| `name` | string | Addressable name for SendMessage |
| `isolation` | `"worktree"` | Git worktree isolation |
| `mode` | enum | Permission mode (default, plan, acceptEdits, dontAsk, auto, bypassPermissions) |
| `model` | enum | Model override (sonnet, opus, haiku) |
| `run_in_background` | boolean | Async execution |
| `team_name` | string | Team assignment |

### Task Management Tools (Separated from Agent)

| Tool | Purpose |
|---|---|
| `TaskCreate` | Create structured tasks with subject, description, activeForm, metadata |
| `TaskUpdate` | Update status, owner, dependencies (blocks/blockedBy) |
| `TaskGet` | Read latest task state |
| `TaskList` | List all tasks |
| `TaskOutput` | Read task output |
| `TaskStop` | Stop a running task |

### Permission Modes (Updated)

| Mode | Description |
|---|---|
| `default` | Standard permission prompts |
| `acceptEdits` | Auto-accept file changes |
| `plan` | Read-only analysis |
| `auto` | AI classifier (research preview) |
| `dontAsk` | Deny everything not pre-approved |
| `bypassPermissions` | Skip all checks (isolated environments) |

Note: `delegate` mode from Agent Teams documentation may have been rolled into the team_name mechanism.

### Plugin System Updates

- `source: 'settings'` — inline plugin declarations in settings.json (v2.1.80)
- `git-subdir` source — sparse checkout from repo subdirectories (v2.1.69)
- `/reload-plugins` — live reload without restart (v2.1.69)
- `managed-settings.d/` — drop-in policy fragments (v2.1.83)
- `blockedMarketplaces` — org-level denylist (v2.1.85)
- `claude plugin validate` — validate plugin structure (v2.1.77)
- `${CLAUDE_PLUGIN_DATA}` — persistent plugin state directory (v2.1.78)

### `/batch` Command (v2.1.63)

Three-phase codebase-wide changes:
1. Research & Plan — decompose into 5-30 independent units
2. Execution — one agent per isolated worktree
3. Tracking — real-time status table

### Remote & Cloud Execution

| Feature | Version | Description |
|---|---|---|
| Remote Control | v2.1.51 | Bridge terminal to claude.ai/code |
| `/schedule` | March 2026 | Cloud-scheduled recurring tasks |
| `/loop` | v2.1.71 | Local recurring prompts |
| Channels | v2.1.80 | External system message push |
| `/teleport` | v2.1.0 | Move session between terminal and web |

### Model Updates

| Model | Context | Output Default | Output Max |
|---|---|---|---|
| Opus 4.6 | 1M tokens | 64K tokens | 128K tokens |
| Sonnet 4.6 | Standard | Standard | Standard |
| Haiku 4.5 | Standard | Standard | Standard |

### New CLI Commands & Flags

| Command/Flag | Description |
|---|---|
| `/voice` | Push-to-talk voice mode |
| `/effort` | Set model effort (low/medium/high) |
| `/simplify` | Simplify code while preserving behavior |
| `/batch` | Parallel codebase-wide changes |
| `/loop` | Recurring prompts |
| `/branch` | Fork conversation (renamed from /fork) |
| `/reload-plugins` | Live reload plugins |
| `--worktree` / `-w` | Create isolated git worktree for session |
| `--bare` | Skip hooks/LSP/plugins for scripted calls |
| `--console` | Authenticate via Anthropic Console |
| `-n` / `--name` | Set session display name |

---

## Impact on Skill Creation

### What Skill-Forge Users Need to Know

1. **Description cap is 250 chars** — Front-load the most important trigger condition. The WHEN + WHEN NOT pattern still works but must be much more concise.

2. **New frontmatter fields to offer** — When helping users create skills, ask about `effort`, `initialPrompt`, and `paths:` fields.

3. **Hook HTTP type** — For teams with webhook infrastructure, suggest HTTP hooks instead of command hooks for simpler deployment.

4. **Conditional `if` field** — No longer need separate hook entries for different Bash commands; use `if` for granular filtering.

5. **Worktree isolation** — When creating agents that do parallel work, suggest `isolation: "worktree"` to prevent merge conflicts.

6. **Named agents with SendMessage** — New coordination pattern: name your agents and have them communicate directly instead of only through the parent.

7. **Task management is separate** — TaskCreate/TaskUpdate are standalone tools; don't confuse with Agent tool for spawning.

8. **Plugin distribution** — Skills can now be shared via plugins with `source: 'settings'` or `git-subdir` patterns.

9. **`auto` mode** — When configuring permissions, offer `auto` as an option for teams that want AI-powered approval.

10. **`managed-settings.d/`** — For enterprise users, suggest drop-in fragments instead of one monolithic managed-settings.json.

---

## Release Timeline

| Date | Version | Key Feature |
|---|---|---|
| Jan 7 | v2.1.0 | Skills hot reload, forked context, teleport |
| Late Jan | v2.1.32-34 | Agent Teams (experimental) |
| Feb 19 | v2.1.49 | `--worktree` flag, ConfigChange hook |
| Feb 20 | v2.1.50 | Worktree isolation in agents |
| Feb 24 | v2.1.51 | Remote Control |
| Feb 26 | v2.1.59 | Auto-memory |
| Feb 28 | v2.1.63 | /batch, /simplify, HTTP hooks |
| Mar 5 | v2.1.69 | InstructionsLoaded hook, /reload-plugins |
| Mar 7 | v2.1.71 | /loop cron command |
| Mar 10 | v2.1.72 | ExitWorktree tool, effort simplified |
| Mar 13 | v2.1.75 | 1M context Opus 4.6 |
| Mar 14 | v2.1.76 | PostCompact hook, MCP elicitation hooks |
| Mar 17 | v2.1.77 | Opus 64K/128K output, WorktreeCreate/Remove hooks |
| Mar 18 | v2.1.78 | StopFailure hook, disallowedTools/maxTurns frontmatter |
| Mar 20 | v2.1.80 | Channels, effort frontmatter, settings plugins |
| Mar 25 | v2.1.83 | managed-settings.d/, CwdChanged/FileChanged hooks |
| Mar 26 | v2.1.84-85 | Hook `if` field, TaskCreated hook, initialPrompt |
| Mar 27 | v2.1.86 | Description cap 250 chars, Read dedup |
