# Claude Code Skill Compliance Enforcement

This directory contains hooks that provide **deterministic enforcement** of skill compliance. Unlike prompting-based approaches, these hooks use exit codes to block actions when required steps are not completed.

## The Problem

Claude Code skills are just prompts. The model can:
- Read the skill instructions
- Appear to follow them
- Actually skip steps while producing output that looks compliant

More prompting doesn't fix this. The model can ignore checklists, verification statements, and completion gates just as easily as it ignores the original instructions.

## The Solution: Hook-Based Enforcement

Hooks are external shell scripts that run at specific lifecycle points. They provide deterministic enforcement because:

1. **Exit code 0**: Action proceeds
2. **Exit code 2**: Action is **BLOCKED** and error message is injected into conversation

The model cannot bypass exit code 2. It's enforced by the Claude Code runtime, not by the model itself.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Skill Execution                          │
│                                                              │
│  Step 1 ──► log_compliance.sh ──► /tmp/pr_N_compliance.log  │
│  Step 2 ──► log_compliance.sh ──► /tmp/pr_N_compliance.log  │
│  Step 3 ──► log_compliance.sh ──► /tmp/pr_N_compliance.log  │
│     ...                                                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  Action Attempt (e.g., PR approval)          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   PreToolUse Hook                            │
│                                                              │
│  verify_compliance.sh reads /tmp/pr_N_compliance.log        │
│                                                              │
│  Missing steps? ──► exit 2 ──► ACTION BLOCKED               │
│  All steps OK?  ──► exit 0 ──► Action proceeds              │
└─────────────────────────────────────────────────────────────┘
```

## Files

| File | Purpose |
|------|---------|
| `verify_pr_review_compliance.sh` | Blocks PR approval if skill steps incomplete |
| `block_ai_attribution.sh` | Blocks commits/PRs containing AI/Claude attribution |
| `README.md` | This documentation |

---

## AI Attribution Blocker

The `block_ai_attribution.sh` hook enforces the CLAUDE.md requirement:
- Never mention Claude, Claude Code, or AI in commit messages
- Never add Co-Authored-By or attribution to Claude/AI

### Blocked Patterns

The hook detects and blocks:
- "Claude" or "Anthropic"
- "Generated with"
- "Co-Authored-By: Claude" or "Co-Authored-By: Anthropic"
- "🤖 Generated" emoji patterns
- "AI assistant", "AI-generated", "AI generated"

### Configuration

Add to `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "tool == \"Bash\" && tool_input.command matches \"git commit\"",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block_ai_attribution.sh",
            "timeout": 10
          }
        ]
      },
      {
        "matcher": "tool == \"Bash\" && tool_input.command matches \"gh pr create\"",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block_ai_attribution.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### Testing

```bash
# Test with a commit message containing attribution
echo '{"command": "git commit -m \"feat: Add feature\n\nCo-Authored-By: Claude\""}' | .claude/hooks/block_ai_attribution.sh
echo $?  # Should be 2 (blocked)

# Test with a clean commit message
echo '{"command": "git commit -m \"feat: Add feature\""}' | .claude/hooks/block_ai_attribution.sh
echo $?  # Should be 0 (allowed)
```

---

## Extending to Other Skills

### Step 1: Define Required Steps

Identify the steps that MUST be completed. Be specific about what cannot be skipped.

```bash
# Example for a deployment skill
REQUIRED_STEPS=(
    "CHECK_BRANCH_STATUS"
    "RUN_TESTS"
    "BUILD_DOCKER_IMAGE"
    "PUSH_TO_REGISTRY"
    "VERIFY_DEPLOYMENT"
)
```

### Step 2: Create Logging Script

Create a helper script in your skill's `scripts/` directory:

```bash
#!/bin/bash
# scripts/log_compliance.sh

PR_NUMBER="$1"
STEP_MARKER="$2"
LOG_FILE="/tmp/skill_${PR_NUMBER}_compliance.log"

echo "$STEP_MARKER" >> "$LOG_FILE"
echo "Logged: $STEP_MARKER"
```

### Step 3: Add Logging to Skill

In your skill's markdown, add logging calls after each required step:

```markdown
#### Step 1: Check Branch Status

```bash
git status
./scripts/log_compliance.sh <ID> CHECK_BRANCH_STATUS
```
```

### Step 4: Create Verification Hook

Create a hook that checks for all required steps:

```bash
#!/bin/bash
# .claude/hooks/verify_my_skill_compliance.sh

# Read tool input
TOOL_INPUT=$(cat)

# Extract relevant ID from command
ID=$(extract_id_from_command "$TOOL_INPUT")

LOG_FILE="/tmp/skill_${ID}_compliance.log"

REQUIRED_STEPS=(
    "STEP_ONE"
    "STEP_TWO"
    "STEP_THREE"
)

for step in "${REQUIRED_STEPS[@]}"; do
    if ! grep -q "^$step$" "$LOG_FILE" 2>/dev/null; then
        echo "BLOCKED: Missing step $step" >&2
        exit 2  # BLOCK ACTION
    fi
done

exit 0  # Allow action
```

### Step 5: Configure Hook

Add to `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/verify_my_skill_compliance.sh"
          }
        ]
      }
    ]
  }
}
```

## Hook Events Reference

| Event | When It Fires | Use Case |
|-------|---------------|----------|
| `PreToolUse` | Before any tool executes | Block actions if preconditions not met |
| `PostToolUse` | After tool completes | Validate outputs, log audit trail |
| `Stop` | When Claude finishes responding | End-of-turn quality gates |
| `SubagentStop` | When subagent completes | Verify subagent work before continuing |

## Exit Codes

| Code | Effect |
|------|--------|
| `0` | Success - action proceeds |
| `2` | **BLOCK** - action stopped, error message sent to Claude |
| Other | Treated as non-blocking error |

## Best Practices

1. **Be specific about required steps** - Don't make every action a required step. Focus on the ones that get skipped.

2. **Use descriptive markers** - `PHASE2_REVIEW_CORE_FILES` is better than `STEP_5`.

3. **Log early in each step** - Log at the START of a step, not the end. This catches cases where the model starts but doesn't finish.

4. **Provide clear error messages** - When blocking, tell the model exactly what's missing and how to fix it.

5. **Test your hooks** - Run the hook script manually to verify it works:
   ```bash
   echo '{"command": "gh pr review 123 --approve"}' | ./verify_pr_review_compliance.sh
   echo $?  # Should be 2 if no compliance log exists
   ```

## Debugging

### Check compliance log
```bash
cat /tmp/pr_<NUMBER>_skill_compliance.log
```

### Test hook manually
```bash
echo '{"command": "gh pr review 123 --approve"}' | .claude/hooks/verify_pr_review_compliance.sh
```

### Reset for new attempt
```bash
rm /tmp/pr_<NUMBER>_skill_compliance.log
```

## Limitations

1. **Hooks only trigger on tool use** - If the model produces output without using tools, hooks don't fire.

2. **Logging requires model cooperation** - The model must call the logging script. A malicious or buggy model could skip logging. However, without the log entries, the hook will block the final action.

3. **Log file persistence** - Logs are in `/tmp/` and may be cleared on reboot. For long-running workflows, consider a more persistent location.

## References

- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [ROUTINE-PLANNER Verifier Pattern](https://digitalthoughtdisruption.com/2025/08/20/routine-planner-deterministic-agent-plan-builder/)
- [Trail of Bits Security Skills](https://github.com/trailofbits/skills)
