# Phase 2 Session 3: Hooks System Patterns

## Executive Summary

1. **14 Hook Events Available** - Claude Code supports SessionStart, SessionEnd, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, PreCompact, Stop, Notification, SubagentStart, SubagentStop, TeammateIdle, TaskCompleted, and Setup (triggered via CLI flags).

2. **Three Hook Types** - Command hooks (shell scripts), Prompt hooks (LLM single-turn evaluation), and Agent hooks (subagent with tool access for multi-turn verification).

3. **Deterministic Control Layer** - Hooks provide deterministic "must-do" rules that complement "should-do" suggestions in CLAUDE.md. They fire every time conditions are met, regardless of LLM decisions.

4. **Input Modification Capability** - Since v2.0.10, PreToolUse hooks can modify tool inputs via `updatedInput` field, enabling transparent sandboxing and automatic security enforcement without blocking.

5. **Async Background Execution** - Command hooks support `"async": true` for non-blocking operations like logging, notifications, and metrics collection.

6. **Decision Control** - Hooks can `allow`, `deny`, or `ask` for permission decisions. Exit code 2 blocks operations with stderr fed to Claude as feedback.

7. **Hierarchical Configuration** - Settings cascade from managed policy (highest) > project settings > local settings > user settings (lowest), with security-sensitive changes requiring /hooks menu review.

---

## Sources Consulted

| Source | URL | Last Updated | Notes |
|--------|-----|--------------|-------|
| Claude Code Hooks Reference (Official) | https://code.claude.com/docs/en/hooks | 2026 | Primary documentation |
| Claude Code Hooks Guide (Official) | https://code.claude.com/docs/en/hooks-guide | 2026 | Workflow automation guide |
| Claude Agent SDK Hooks | https://platform.claude.com/docs/en/agent-sdk/hooks | 2026 | SDK implementation |
| Anthropic Blog: How to Configure Hooks | https://claude.com/blog/how-to-configure-hooks | 2025 | Official tutorial |
| GitHub: claude-code-hooks-mastery | https://github.com/disler/claude-code-hooks-mastery | 2026 | Comprehensive examples |
| ClaudeLog Hooks Reference | https://claudelog.com/mechanics/hooks/ | 2026 | Community docs |
| DataCamp Hooks Tutorial | https://www.datacamp.com/tutorial/claude-code-hooks | 2025 | Practical guide |
| Claude Code Changelog | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md | 2026 | Version history |
| ClaudeFast Hooks Guide | https://claudefa.st/blog/tools/hooks/hooks-guide | 2026 | All 12 lifecycle events |

---

## Detailed Findings

### Hook Events

| Event | Trigger | Blocking | Matcher Support | Use Case |
|-------|---------|----------|-----------------|----------|
| **SessionStart** | Session begins or resumes | NO | `startup`, `resume`, `clear`, `compact` | Environment setup, context loading |
| **SessionEnd** | Session terminates | NO | `clear`, `logout`, `prompt_input_exit`, `other` | Cleanup, final logging |
| **UserPromptSubmit** | User presses enter | YES | None (always fires) | Validation, context injection |
| **PreToolUse** | Before tool execution | YES | Tool name regex | Security checks, auto-approval, input modification |
| **PostToolUse** | After tool succeeds | NO* | Tool name regex | Auto-formatting, linting, logging |
| **PostToolUseFailure** | After tool fails | NO | Tool name regex | Error recovery, debugging logs |
| **PermissionRequest** | Permission dialog appears | YES | Tool name regex | Intelligent auto-approve/deny |
| **PreCompact** | Before context compaction | NO | `manual`, `auto` | Transcript backup, preserve decisions |
| **Stop** | Claude finishes response | YES | None (always fires) | Task completion enforcement |
| **Notification** | Claude sends notification | NO | `permission_prompt`, `idle_prompt`, `auth_success` | Desktop alerts, TTS |
| **SubagentStart** | Subagent spawned | NO | Agent type | Subagent initialization, tracking |
| **SubagentStop** | Subagent finishes | YES | Agent type | Validation of subagent output |
| **TeammateIdle** | Agent team member idle | YES (exit code only) | None | Multi-agent workflow control |
| **TaskCompleted** | Task marked complete | YES | None (always fires) | Completion criteria enforcement |
| **Setup** | `--init`, `--init-only`, `--maintenance` flags | NO | `init`, `maintenance` | One-time installation tasks |

*PostToolUse can inject context but cannot undo execution.

#### Event-Specific Input Fields

**Common fields (all events):**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/directory",
  "permission_mode": "default|plan|acceptEdits|dontAsk|bypassPermissions",
  "hook_event_name": "EventName"
}
```

**Tool-related events (PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest):**
- `tool_name`: Name of the tool being called
- `tool_input`: Arguments passed to tool (varies by tool)
- `tool_use_id`: Unique identifier for correlating events
- `tool_response`: Result from execution (PostToolUse only)
- `error`: Failure message (PostToolUseFailure only)
- `is_interrupt`: Whether caused by interrupt (PostToolUseFailure only)
- `permission_suggestions`: "Always allow" options (PermissionRequest only)

**Tool input schemas by tool:**
| Tool | Key Fields |
|------|------------|
| Bash | `command`, `description`, `timeout`, `run_in_background` |
| Write | `file_path`, `content` |
| Edit | `file_path`, `old_string`, `new_string`, `replace_all` |
| Read | `file_path`, `offset`, `limit` |
| Glob | `pattern`, `path` |
| Grep | `pattern`, `path`, `glob`, `output_mode`, `-i`, `multiline` |
| WebFetch | `url`, `prompt` |
| WebSearch | `query`, `allowed_domains`, `blocked_domains` |
| Task | `prompt`, `description`, `subagent_type`, `model` |

**Lifecycle events:**
- **SessionStart**: `source` (startup/resume/clear/compact), `model`, optional `agent_type`
- **SessionEnd**: `reason` (clear/logout/prompt_input_exit/bypass_permissions_disabled/other)
- **UserPromptSubmit**: `prompt` (user's text)
- **Stop/SubagentStop**: `stop_hook_active` (boolean - critical for loop prevention)
- **SubagentStart/SubagentStop**: `agent_id`, `agent_type`, `agent_transcript_path`
- **TeammateIdle**: `teammate_name`, `team_name`
- **TaskCompleted**: `task_id`, `task_subject`, `task_description`, optional `teammate_name`, `team_name`
- **Notification**: `message`, `title`, `notification_type`
- **PreCompact**: `trigger` (manual/auto), `custom_instructions`

---

### Hook Types

#### Command Hooks (`type: "command"`)
Execute shell scripts receiving JSON via stdin, returning decisions through exit codes and stdout.

```json
{
  "type": "command",
  "command": "/path/to/script.sh",
  "timeout": 60,
  "async": false
}
```

**Features:**
- Full shell environment access
- JSON input via stdin
- Exit codes control behavior
- Support async execution
- Environment variables: `$CLAUDE_PROJECT_DIR`, `$CLAUDE_ENV_FILE`, `$CLAUDE_CODE_REMOTE`

**When to use:** Security blocking, file validation, auto-formatting, logging, notifications, context injection.

#### Prompt Hooks (`type: "prompt"`)
Send hook input to Claude model for single-turn LLM evaluation, returning structured yes/no decisions.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if this task is complete. $ARGUMENTS",
  "timeout": 30
}
```

**Response format:**
```json
{
  "ok": true,
  "reason": "explanation when false"
}
```

**Supported events:** PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, UserPromptSubmit, Stop, SubagentStop, TaskCompleted.

**When to use:** Intelligent completion verification, context-aware decisions, task validation.

#### Agent Hooks (`type: "agent"`)
Spawn subagent with tool access (Read, Grep, Glob) for multi-turn verification before returning decisions.

```json
{
  "type": "agent",
  "prompt": "Verify all tests pass. Run the test suite and check results. $ARGUMENTS",
  "timeout": 120
}
```

**Features:**
- Up to 50 turns of tool usage
- Access to Read, Grep, Glob tools
- Returns same `{"ok": true/false, "reason": "..."}` structure
- Default 60-second timeout

**When to use:** Test verification, complex validation requiring codebase inspection, quality gates.

**Not supported:** TeammateIdle does not support prompt-based or agent-based hooks.

---

### Configuration

#### Settings File Locations (Priority Order)

| Location | Scope | Priority | Shareable |
|----------|-------|----------|-----------|
| Managed policy settings | Enterprise | Highest | Org-wide |
| `.claude/settings.json` | Project | High | Yes (version control) |
| `.claude/settings.local.json` | Project | Medium | No (personal) |
| `~/.claude/settings.json` | All projects | Lowest | No (user) |
| Plugin `hooks/hooks.json` | When plugin enabled | Variable | With plugin |
| Skill/agent frontmatter | While component active | Variable | With skill |

#### Basic Configuration Structure

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "regex_pattern",
        "hooks": [
          {
            "type": "command|prompt|agent",
            "command": "script_path",
            "prompt": "evaluation_prompt",
            "timeout": 600,
            "statusMessage": "Custom message",
            "once": false,
            "async": false
          }
        ]
      }
    ]
  }
}
```

#### Hook Configuration Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `type` | string | required | `"command"`, `"prompt"`, or `"agent"` |
| `command` | string | - | Shell command (command hooks) |
| `prompt` | string | - | Evaluation prompt (prompt/agent hooks) |
| `timeout` | number | 600000 (10 min) | Max execution time in ms (was 60s before 2026) |
| `statusMessage` | string | - | Custom status displayed during execution |
| `once` | boolean | false | Run only once per session |
| `async` | boolean | false | Run in background (command hooks only) |

#### Matcher Patterns

Matchers are **case-sensitive regex** patterns:

| Pattern | Matches |
|---------|---------|
| `""` or omitted | All tools |
| `"Bash"` | Exact tool name |
| `"Write\|Edit"` | Multiple tools (no spaces around `\|`) |
| `"Edit\|MultiEdit\|Write"` | File modification tools |
| `"mcp__memory__.*"` | All tools from memory MCP server |
| `"mcp__.*__write.*"` | Any "write" tool from any MCP server |
| `"Bash(npm test*)"` | Bash with specific command pattern |

**MCP tool naming:** `mcp__<server>__<tool>` (e.g., `mcp__github__search_repositories`)

**Event-specific matchers:**
| Event | Matcher Values |
|-------|---------------|
| SessionStart | `startup`, `resume`, `clear`, `compact` |
| SessionEnd | `clear`, `logout`, `prompt_input_exit`, `other` |
| PreCompact | `manual`, `auto` |
| Setup | `init`, `maintenance` |
| Notification | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` |
| SubagentStart/Stop | Agent type name |

---

### Input/Output Format

#### Exit Codes

| Code | Interpretation | JSON Processing | When Blocking |
|------|----------------|-----------------|---------------|
| 0 | Success; allow action | Parse stdout JSON | - |
| 2 | Blocking error; deny action | Ignore JSON; use stderr | PreToolUse, PermissionRequest, UserPromptSubmit, Stop, TaskCompleted, TeammateIdle |
| Other | Non-blocking error | Show stderr in verbose mode | - |

Exit code 2 is the primary enforcement mechanism.

#### JSON Output Structure

**Universal fields (all events):**
```json
{
  "continue": true,
  "stopReason": "message when continue=false",
  "suppressOutput": false,
  "systemMessage": "warning injected to user",
  "hookSpecificOutput": { }
}
```

**Top-level `decision` (UserPromptSubmit, PostToolUse, PostToolUseFailure, Stop, SubagentStop):**
```json
{
  "decision": "block",
  "reason": "Why action blocked"
}
```

#### PreToolUse hookSpecificOutput

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "explanation",
    "updatedInput": {
      "command": "modified-command",
      "file_path": "/sandbox/path"
    },
    "additionalContext": "Context injected as <system-reminder>"
  }
}
```

**Field details:**
- `permissionDecision`: `allow` (proceed), `deny` (block with reason), `ask` (show permission dialog)
- `updatedInput`: Modify tool parameters before execution (requires `permissionDecision: "allow"`)
- `additionalContext`: Text injected into Claude's context as `<system-reminder>` tag

**Deprecated fields:** `decision` and `reason` (use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason`)

#### PermissionRequest hookSpecificOutput

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny|ask",
      "updatedInput": { },
      "updatedPermissions": [ ],
      "message": "denial_reason",
      "interrupt": false
    }
  }
}
```

#### Prompt/Agent Hook Response

```json
{
  "ok": true,
  "reason": "explanation when false"
}
```

---

### Decision Control

#### Permission Decision Flow

Evaluated in order:
1. **Deny** rules (any match = block immediately)
2. **Ask** rules (prompt user)
3. **Allow** rules (auto-approve)
4. **Default** = Ask

Any `deny` decision blocks regardless of other rules.

#### Blocking Operations

**Using exit code 2:**
```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')

if [[ "$COMMAND" == *"rm -rf"* ]]; then
    echo "BLOCKED: Dangerous rm command" >&2
    exit 2
fi
exit 0
```

**Using JSON decision:**
```python
import json
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if file_path.endswith(".env"):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": data["hook_event_name"],
            "permissionDecision": "deny",
            "permissionDecisionReason": "Cannot modify .env files"
        }
    }))
    sys.exit(0)

sys.exit(0)
```

#### Input Modification

Redirect file paths to sandbox:
```python
import json
import sys

data = json.load(sys.stdin)
if data["tool_name"] == "Write":
    original_path = data["tool_input"].get("file_path", "")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": data["hook_event_name"],
            "permissionDecision": "allow",
            "updatedInput": {
                **data["tool_input"],
                "file_path": f"/sandbox{original_path}"
            }
        }
    }))
sys.exit(0)
```

#### Stop Hook Loop Prevention

**Critical:** Check `stop_hook_active` to prevent infinite loops:
```bash
#!/bin/bash
INPUT=$(cat)
STOP_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false')

if [ "$STOP_ACTIVE" = "true" ]; then
    exit 0  # Already in stop hook, don't recurse
fi

# Your verification logic here
```

---

### Async Hooks

#### Configuration

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/run-tests.sh",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

#### Behavior

- Runs in background; doesn't block Claude
- Cannot return blocking decisions (`decision`, `permissionDecision`, `continue` ignored)
- Output delivered on next conversation turn
- Each execution creates separate background process
- No deduplication across multiple firings

#### Supported Events

Only `type: "command"` hooks support async. Prompt-based hooks cannot run asynchronously.

Best for PostToolUse and PostToolUseFailure events.

#### When to Use

**Good for:**
- Logging and metrics collection
- Notifications (Slack, email, Pushover)
- Memory storage operations
- Non-critical post-processing (analytics, backups)

**Not suitable for:**
- Formatting (must complete before next edit)
- Validation (must block on failure)
- Any hook needing to modify input/output

---

### Use Cases

#### 1. Skill Enforcement

Force tool usage patterns:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/enforce_skill_rules.py"
          }
        ]
      }
    ]
  }
}
```

#### 2. Quality Gates

**Test verification before stop:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "agent",
            "prompt": "Verify all tests pass. Run the test suite and check results.",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

**Task completion enforcement:**
```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "npm test || exit 2"
          }
        ]
      }
    ]
  }
}
```

#### 3. Security Enforcement

**Block dangerous commands:**
```python
#!/usr/bin/env python3
import json, sys, re

DANGEROUS = [r'\brm\s+.*-[a-z]*r', r'sudo\s+rm', r'chmod\s+777']
data = json.load(sys.stdin)

if data.get('tool_name') == 'Bash':
    cmd = data.get('tool_input', {}).get('command', '')
    if any(re.search(p, cmd) for p in DANGEROUS):
        print("BLOCKED: Dangerous command pattern", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
```

**Protected file patterns:**
```bash
#!/bin/bash
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
PROTECTED_PATTERNS=(".env" "package-lock.json" ".git/" "credentials" "secrets")

for pattern in "${PROTECTED_PATTERNS[@]}"; do
    if [[ "$FILE_PATH" == *"$pattern"* ]]; then
        echo "Blocked: $FILE_PATH matches protected pattern '$pattern'" >&2
        exit 2
    fi
done
exit 0
```

#### 4. Auto-Formatting

**Prettier on file writes:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

**Black formatter for Python:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "black $CLAUDE_FILE_PATHS"
          }
        ]
      }
    ]
  }
}
```

#### 5. Notifications

**macOS notification:**
```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**Linux notification:**
```json
{
  "hooks": {
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' 'Needs your attention'"
          }
        ]
      }
    ]
  }
}
```

#### 6. Context Injection

**Session start context:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "git status --short && echo '---' && cat TODO.md"
          }
        ]
      }
    ]
  }
}
```

**Re-inject after compaction:**
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Use Bun not npm. Run bun test before committing. Current: auth refactor.'"
          }
        ]
      }
    ]
  }
}
```

#### 7. Logging and Audit

**Command logging:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/command-log.txt",
            "async": true
          }
        ]
      }
    ]
  }
}
```

**Structured JSON logging:**
```python
import json
import sys
from datetime import datetime

data = json.load(sys.stdin)
hook_data = {
    "timestamp": datetime.now().isoformat(),
    "hook_name": data.get("hook_event_name"),
    "tool_name": data.get("tool_name"),
    "session_id": data.get("session_id")
}

with open("logs/hooks.json", "a") as f:
    f.write(json.dumps(hook_data) + "\n")
```

#### 8. Auto-Approval Patterns

**Auto-approve read-only tools:**
```python
import json
import sys

data = json.load(sys.stdin)
READ_ONLY_TOOLS = ["Read", "Glob", "Grep", "LS"]

if data["tool_name"] in READ_ONLY_TOOLS:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": data["hook_event_name"],
            "permissionDecision": "allow",
            "permissionDecisionReason": "Read-only tool auto-approved"
        }
    }))
sys.exit(0)
```

**Auto-approve npm test:**
```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Bash(npm test*)",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"hookSpecificOutput\":{\"hookEventName\":\"PermissionRequest\",\"decision\":{\"behavior\":\"allow\"}}}'"
          }
        ]
      }
    ]
  }
}
```

---

### Security Considerations

#### Critical Security Practices

1. **Hooks run with full user permissions** - No sandbox; access everything your account can access

2. **Validate and sanitize all inputs:**
   ```bash
   # Always quote shell variables
   FILE_PATH="$FILE_PATH"  # Correct
   FILE_PATH=$FILE_PATH    # WRONG - vulnerable to injection
   ```

3. **Check for path traversal:**
   ```bash
   if [[ "$FILE_PATH" == *".."* ]]; then
       echo "Path traversal blocked" >&2
       exit 2
   fi
   ```

4. **Use absolute paths:**
   ```json
   {
     "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/script.sh"
   }
   ```

5. **Skip sensitive files:**
   - `.env`, `.env.*`
   - `.git/`
   - `credentials.json`, `secrets.*`
   - SSH keys, API keys

6. **Direct edits require review:**
   - Changes to settings files don't take effect immediately
   - Claude Code captures snapshots at startup
   - Use `/hooks` menu to review and apply changes

#### Defense in Depth

```json
{
  "disableAllHooks": true,
  "allowManagedHooksOnly": true
}
```

- `disableAllHooks`: Prevents all hooks from executing
- `allowManagedHooksOnly`: Only managed/SDK hooks execute; user/plugin hooks blocked

#### Shell Profile Issues

Wrap unconditional echo statements to avoid corrupting hook JSON:
```bash
if [[ $- == *i* ]]; then
    echo "Interactive shell message"
fi
```

---

## Patterns Catalog

### Pattern 1: Security Gate
- **Description:** Block dangerous operations before execution
- **When to use:** PreToolUse for commands containing `rm -rf`, `sudo`, protected file paths
- **Example:**
  ```json
  {
    "hooks": {
      "PreToolUse": [{
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "python security-gate.py"}]
      }]
    }
  }
  ```

### Pattern 2: Auto-Format on Save
- **Description:** Run formatters after file modifications
- **When to use:** PostToolUse with `Write|Edit` matcher
- **Example:**
  ```json
  {
    "hooks": {
      "PostToolUse": [{
        "matcher": "Write|Edit",
        "hooks": [{"type": "command", "command": "prettier --write $(jq -r '.tool_input.file_path')"}]
      }]
    }
  }
  ```

### Pattern 3: Completion Verification
- **Description:** Verify task completion before allowing stop
- **When to use:** Stop hook with prompt or agent type
- **Example:**
  ```json
  {
    "hooks": {
      "Stop": [{
        "hooks": [{
          "type": "prompt",
          "prompt": "Check if all tasks are complete. Return {\"ok\": false, \"reason\": \"what remains\"} if not."
        }]
      }]
    }
  }
  ```

### Pattern 4: Context Re-injection
- **Description:** Restore critical context after compaction
- **When to use:** SessionStart with `compact` matcher
- **Example:**
  ```json
  {
    "hooks": {
      "SessionStart": [{
        "matcher": "compact",
        "hooks": [{"type": "command", "command": "cat .claude/critical-context.md"}]
      }]
    }
  }
  ```

### Pattern 5: Transparent Sandboxing
- **Description:** Redirect operations to safe directories without blocking
- **When to use:** PreToolUse with `updatedInput`
- **Example:**
  ```python
  print(json.dumps({
      "hookSpecificOutput": {
          "hookEventName": "PreToolUse",
          "permissionDecision": "allow",
          "updatedInput": {"file_path": f"/sandbox{original_path}"}
      }
  }))
  ```

### Pattern 6: Async Telemetry
- **Description:** Non-blocking logging and metrics
- **When to use:** PostToolUse with `async: true`
- **Example:**
  ```json
  {
    "hooks": {
      "PostToolUse": [{
        "hooks": [{
          "type": "command",
          "command": "python send-metrics.py",
          "async": true
        }]
      }]
    }
  }
  ```

### Pattern 7: Branch Protection
- **Description:** Block edits on protected branches
- **When to use:** PreToolUse for file operations
- **Example:**
  ```bash
  [ "$(git branch --show-current)" != "main" ] || { echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Cannot edit on main branch"}}'; exit 0; }
  ```

### Pattern 8: Multi-Agent Coordination
- **Description:** Track and validate subagent activity
- **When to use:** SubagentStart, SubagentStop, TeammateIdle, TaskCompleted
- **Example:**
  ```json
  {
    "hooks": {
      "SubagentStop": [{
        "hooks": [{
          "type": "command",
          "command": "python validate-subagent-output.py"
        }]
      }]
    }
  }
  ```

### Pattern 9: Skill-Scoped Stop Hook
- **Description:** Stop hook that only fires when a specific skill is active
- **When to use:** Workflow enforcement for skills that produce artifacts
- **Problem it solves:** Prevents hook from blocking unrelated sessions
- **Implementation:**
  1. Skill creates marker file at start: `claude/<skill-name>/.active`
  2. Hook checks for marker first; exits 0 if not present
  3. Skill removes marker when workflow complete
- **Example:**
  ```python
  #!/usr/bin/env python3
  import json, sys
  from pathlib import Path

  data = json.load(sys.stdin)
  project_dir = Path(data.get("cwd", "."))

  # Only fire when skill is active
  marker = project_dir / "claude" / "my-skill" / ".active"
  if not marker.exists():
      sys.exit(0)  # Not active, allow completion

  # Collect verification issues
  issues = []

  # Your verification logic here
  # Example: check required files exist
  # if not (project_dir / "claude/my-skill/required_file.md").exists():
  #     issues.append("Missing required_file.md")

  if issues:
      print("Workflow incomplete: " + str(issues), file=sys.stderr)
      sys.exit(2)
  sys.exit(0)
  ```

### Pattern 10: Proof via Artifact
- **Description:** Verify workflow steps by checking output files exist, not transcript parsing
- **When to use:** Verifying that required workflow steps were completed
- **Problem it solves:** Transcript parsing is fragile (JSON format changes, spacing). Output files are reliable proof.
- **Anti-pattern (DON'T DO THIS):**
  ```python
  # FRAGILE: Searching transcript for JSON strings
  content = transcript.read_text()
  if '"subagent_type":"Explore"' not in content:
      sys.exit(2)  # Breaks if spacing changes!
  ```
- **Correct pattern:**
  ```python
  from pathlib import Path

  # Setup: meeting_folder is the folder being verified, issues collects problems
  meeting_folder = Path("claude/meeting-analyzer/meeting_kickoff_2026-02-17")
  issues = []

  # ROBUST: Check for output file that proves step was done
  context_file = meeting_folder / "00_context_discovery.md"
  if not context_file.exists() or len(context_file.read_text()) < 50:
      issues.append("Missing context discovery file")
  ```
- **For content verification, use section headers not phrases:**
  ```python
  import re

  # FRAGILE: Exact phrase matching
  if "transcription note" not in content.lower():  # Breaks if wording varies
      pass  # This approach is brittle

  # ROBUST: Section header matching
  if not re.search(r"^#{1,3}\s+[Tt]ranscription", content, re.MULTILINE):
      issues.append("Missing Transcription section header")
  ```

### Pattern 11: Flexible Document Matching
- **Description:** Match document types by pattern, not hardcoded filenames
- **When to use:** Skills that produce numbered documents where numbering may vary
- **Problem it solves:** Hardcoded `01_speaker_notes.md` fails if document is numbered `02_`
- **Anti-pattern:**
  ```python
  REQUIRED = ["00_breakdown", "01_speaker_notes", "03_sentiment"]  # Breaks if numbering varies!
  ```
- **Correct pattern:**
  ```python
  import re
  from pathlib import Path

  # Setup: folder is the meeting folder to verify, issues collects problems
  folder = Path("claude/meeting-analyzer/meeting_kickoff_2026-02-17")
  issues = []

  REQUIRED_PATTERNS = [
      r"\d+_meeting_breakdown\.md$",
      r"\d+_speaker_notes\.md$",
      r"\d+_sentiment.*\.md$",
  ]

  files = [f.name for f in folder.iterdir() if f.is_file()]
  for pattern in REQUIRED_PATTERNS:
      if not any(re.search(pattern, f) for f in files):
          issues.append(f"Missing document matching {pattern}")
  ```

---

## Recency Notes

### 2026 Changes

1. **Setup Hook Event** - New event triggered via `--init`, `--init-only`, or `--maintenance` CLI flags (v2.1.10+)

2. **Timeout Increase** - Default timeout changed from 60 seconds to 10 minutes

3. **TeammateIdle & TaskCompleted** - New hook events for multi-agent workflows

4. **Async Hooks** - `async: true` support for non-blocking hooks (v2.1.0+)

5. **additionalContext** - PreToolUse hooks can return `additionalContext` to inject into model context (v2.1.9+)

6. **PermissionRequest Enhancements** - Hooks can now process 'always allow' suggestions (v2.0.45+)

7. **agent_type in SessionStart** - Populated if `--agent` is specified

8. **Plugin Hook Types** - Support for prompt and agent hook types from plugins (previously only command hooks)

### Deprecated

- `decision` and `reason` fields for PreToolUse (use `hookSpecificOutput.permissionDecision` and `hookSpecificOutput.permissionDecisionReason`)
- `approve` and `block` values (use `allow` and `deny`)

---

## Recommendations for Skill-Forge

### Must Implement

1. **PreToolUse Hooks** - For skill rule enforcement and security validation
2. **Stop Hooks** - For task completion verification
3. **SessionStart Hooks** - For skill context injection after compaction
4. **Configuration Templates** - Generate settings.json patterns for common use cases

### Should Implement

1. **PostToolUse Hooks** - For auto-formatting and quality checks
2. **Async Logging** - For telemetry without blocking workflow
3. **Input Modification** - For transparent sandboxing and security enforcement

### Consider Implementing

1. **Agent-based Verification** - For complex completion criteria
2. **Multi-Agent Hooks** - SubagentStart/Stop, TeammateIdle, TaskCompleted for orchestration
3. **Prompt Hooks** - For intelligent, context-aware decisions

### Configuration Best Practices to Enforce

1. Use project-level `.claude/settings.json` for team-wide rules
2. Validate all inputs; quote shell variables
3. Check `stop_hook_active` in Stop hooks
4. Use exit code 2 for blocking, not other non-zero codes
5. Keep hooks small, explicit, and security-first
6. Test hooks independently with sample JSON before deployment

---

## Appendix: SDK Hook Implementation

### TypeScript SDK

```typescript
import { query, HookCallback, PreToolUseHookInput } from "@anthropic-ai/claude-agent-sdk";

const securityHook: HookCallback = async (input, toolUseID, { signal }) => {
  if (input.hook_event_name !== "PreToolUse") return {};

  const preInput = input as PreToolUseHookInput;
  const command = preInput.tool_input.command as string;

  if (command?.includes("rm -rf")) {
    return {
      hookSpecificOutput: {
        hookEventName: input.hook_event_name,
        permissionDecision: "deny",
        permissionDecisionReason: "Dangerous command blocked"
      }
    };
  }
  return {};
};

for await (const message of query({
  prompt: "Your prompt",
  options: {
    hooks: {
      PreToolUse: [{ matcher: "Bash", hooks: [securityHook] }]
    }
  }
})) {
  console.log(message);
}
```

### Python SDK

```python
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

async def security_hook(input_data, tool_use_id, context):
    if input_data["hook_event_name"] != "PreToolUse":
        return {}

    command = input_data.get("tool_input", {}).get("command", "")

    if "rm -rf" in command:
        return {
            "hookSpecificOutput": {
                "hookEventName": input_data["hook_event_name"],
                "permissionDecision": "deny",
                "permissionDecisionReason": "Dangerous command blocked"
            }
        }
    return {}

async for message in query(
    prompt="Your prompt",
    options=ClaudeAgentOptions(
        hooks={
            "PreToolUse": [HookMatcher(matcher="Bash", hooks=[security_hook])]
        }
    )
):
    print(message)
```

### SDK vs CLI Hook Differences

| Feature | CLI (settings.json) | SDK |
|---------|---------------------|-----|
| Configuration | JSON files | Code objects |
| Hook types | command, prompt, agent | callback functions |
| Async support | `async: true` flag | Native async/await |
| Python PostToolUseFailure | Supported | Not supported |
| SessionStart/End (Python) | Supported | Not supported |
| Notification (Python) | Supported | Not supported |
