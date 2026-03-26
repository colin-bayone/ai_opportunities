#!/bin/bash
# =============================================================================
# AI Attribution Blocker Hook
# =============================================================================
#
# Blocks commits and PRs that contain AI/Claude attribution.
# This enforces the CLAUDE.md requirement:
#   - Never mention Claude, Claude Code, or AI in commit messages
#   - Never add Co-Authored-By or attribution to Claude/AI
#
# Exit codes:
#   0 - No attribution found, allow action
#   2 - Attribution detected, BLOCK action
#
# Usage:
#   Called automatically by Claude Code hooks system when attempting to
#   run 'git commit' or 'gh pr create' commands.
#
# =============================================================================

set -euo pipefail

# Read tool input from stdin (JSON format)
TOOL_INPUT=$(cat)

# Extract the command being run
COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')

# Convert \n sequences to actual newlines for heredoc parsing
COMMAND_EXPANDED=$(echo "$COMMAND" | sed 's/\\n/\n/g')

# Patterns to block (case-insensitive matching)
# These are specific attribution patterns found in actual PRs, not general mentions
BLOCKED_PATTERNS=(
    "noreply@anthropic\.com"
    "🤖 generated with"
    "generated with \[claude code\]"
)

# Function to check for blocked patterns
check_for_attribution() {
    local text="$1"
    local text_lower=$(echo "$text" | tr '[:upper:]' '[:lower:]')

    for pattern in "${BLOCKED_PATTERNS[@]}"; do
        if echo "$text_lower" | grep -qiE "$pattern"; then
            return 0  # Found attribution
        fi
    done
    return 1  # No attribution found
}

# Extract message/body content based on command type
MESSAGE=""

if [[ "$COMMAND" =~ git[[:space:]]+commit ]]; then
    # Check heredoc style FIRST: git commit -m "$(cat <<'EOF' ... EOF)"
    if [[ "$COMMAND" =~ \$\(cat ]]; then
        # Extract content between EOF markers
        MESSAGE=$(echo "$COMMAND_EXPANDED" | sed -n '/<<.*EOF/,/EOF/p' | grep -v 'EOF' | grep -v '<<')
    # Then check simple -m "message" or -m 'message'
    elif [[ "$COMMAND" =~ -m[[:space:]]+[\"\']([^\"\']+)[\"\'] ]]; then
        MESSAGE="${BASH_REMATCH[1]}"
    fi
fi

if [[ "$COMMAND" =~ gh[[:space:]]+pr[[:space:]]+create ]]; then
    # Check heredoc style FIRST
    if [[ "$COMMAND" =~ \$\(cat ]]; then
        # Extract content between EOF markers
        MESSAGE=$(echo "$COMMAND_EXPANDED" | sed -n '/<<.*EOF/,/EOF/p' | grep -v 'EOF' | grep -v '<<')
    # Then check simple --body "content"
    elif [[ "$COMMAND" =~ --body[[:space:]]+[\"\']([^\"\']+)[\"\'] ]]; then
        MESSAGE="${BASH_REMATCH[1]}"
    fi

    # Also check --title
    if [[ "$COMMAND" =~ --title[[:space:]]+[\"\']([^\"\']+)[\"\'] ]]; then
        TITLE="${BASH_REMATCH[1]}"
        MESSAGE="$MESSAGE $TITLE"
    fi
fi

# If we couldn't extract a message, allow the command
if [[ -z "$MESSAGE" ]]; then
    exit 0
fi

# Check for blocked patterns
if check_for_attribution "$MESSAGE"; then
    echo "========================================" >&2
    echo "BLOCKED: AI Attribution Detected" >&2
    echo "========================================" >&2
    echo "" >&2
    echo "Your commit message or PR body contains AI/Claude attribution." >&2
    echo "" >&2
    echo "Per CLAUDE.md requirements:" >&2
    echo "  - Never mention Claude, Claude Code, or AI in commit messages" >&2
    echo "  - Never add Co-Authored-By or attribution to Claude/AI" >&2
    echo "" >&2
    echo "Please remove the following patterns:" >&2
    echo "  - 'noreply@anthropic.com' (Co-Authored-By email)" >&2
    echo "  - '🤖 Generated with' (emoji attribution)" >&2
    echo "  - 'Generated with [Claude Code]' (markdown link)" >&2
    echo "" >&2
    echo "Rewrite your message without AI attribution and try again." >&2
    echo "========================================" >&2
    exit 2
fi

# No attribution found
exit 0
