#!/bin/bash
# log_command.sh - Log Azure CLI command to master command log
# Usage: ./log_command.sh "<session_folder>" "<agent_name>" "<command>" "<result>"
# Example: ./log_command.sh "claude/2026-01-06_AZURE_staging" "resource_explorer" "az resource list -g rg" "success"

set -e

SESSION_FOLDER="${1:-.}"
AGENT_NAME="${2:-unknown}"
COMMAND="${3:-No command}"
RESULT="${4:-pending}"

COMMAND_LOG="${SESSION_FOLDER}/command_log.md"

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Check if log file exists
if [ ! -f "$COMMAND_LOG" ]; then
    echo "Error: Command log not found: $COMMAND_LOG"
    echo "Run init_session.sh first."
    exit 1
fi

# Escape pipe characters in command for markdown table
ESCAPED_COMMAND=$(echo "$COMMAND" | sed 's/|/\\|/g')

# Append to command log
echo "| ${TIMESTAMP} | ${AGENT_NAME} | \`${ESCAPED_COMMAND}\` | ${RESULT} |" >> "$COMMAND_LOG"

echo "Command logged: $COMMAND"
