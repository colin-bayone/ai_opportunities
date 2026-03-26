#!/bin/bash
# log_agent_activity.sh - Log agent activity to agent-specific log file
# Usage: ./log_agent_activity.sh "<session_folder>" "<agent_name>" "<comment>" "<command>"
# Example: ./log_agent_activity.sh "claude/2026-01-06_AZURE_staging" "resource_explorer" "Listing resources" "az resource list -g rg"

set -e

SESSION_FOLDER="${1:-.}"
AGENT_NAME="${2:-unknown}"
COMMENT="${3:-No comment}"
COMMAND="${4:-No command}"

# Validate agent name
VALID_AGENTS="resource_explorer network_analyzer config_exporter cost_estimator deploy_debugger research_agent documentation_generator"
if [[ ! " $VALID_AGENTS " =~ " $AGENT_NAME " ]]; then
    echo "Warning: Unknown agent name: $AGENT_NAME"
fi

# Create log file path
LOG_FILE="${SESSION_FOLDER}/agent_logs/${AGENT_NAME}.log"

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Check if log file exists, create header if not
if [ ! -f "$LOG_FILE" ]; then
    mkdir -p "$(dirname "$LOG_FILE")"
    cat > "$LOG_FILE" << EOF
================================================================================
AGENT: ${AGENT_NAME}
SESSION: $(basename "$SESSION_FOLDER")
================================================================================

EOF
fi

# Append log entry
cat >> "$LOG_FILE" << EOF
[${TIMESTAMP}] ${COMMENT}
                      | ${COMMAND}

EOF

# Also log to master command log if command is an Azure CLI command
if [[ "$COMMAND" == az* ]]; then
    COMMAND_LOG="${SESSION_FOLDER}/command_log.md"
    if [ -f "$COMMAND_LOG" ]; then
        echo "| ${TIMESTAMP} | ${AGENT_NAME} | \`${COMMAND}\` | pending |" >> "$COMMAND_LOG"
    fi
fi

echo "Logged to: $LOG_FILE"
