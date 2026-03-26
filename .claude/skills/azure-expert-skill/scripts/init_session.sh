#!/bin/bash
# init_session.sh - Create Azure session folder structure
# Usage: ./init_session.sh "<topic>"
# Example: ./init_session.sh "production_deployment"

set -e

# Get topic from argument
TOPIC="${1:-azure_session}"

# Sanitize topic: lowercase, replace spaces with underscores
TOPIC=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd '[:alnum:]_')

# Get current date
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%Y%m%d_%H%M)

# Create session folder name
SESSION_FOLDER="claude/${DATE}_AZURE_${TOPIC}"

# Check if folder already exists
if [ -d "$SESSION_FOLDER" ]; then
    echo "Session folder already exists: $SESSION_FOLDER"
    echo "Use existing folder? (y/n)"
    read -r response
    if [ "$response" != "y" ]; then
        echo "Aborting."
        exit 1
    fi
else
    # Create the main folder
    mkdir -p "$SESSION_FOLDER"
fi

# Create subdirectories
mkdir -p "$SESSION_FOLDER/planning"
mkdir -p "$SESSION_FOLDER/goals"
mkdir -p "$SESSION_FOLDER/progress"
mkdir -p "$SESSION_FOLDER/decisions"
mkdir -p "$SESSION_FOLDER/research"
mkdir -p "$SESSION_FOLDER/issues_and_improvements"
mkdir -p "$SESSION_FOLDER/documentation/markdown"
mkdir -p "$SESSION_FOLDER/documentation/json"
mkdir -p "$SESSION_FOLDER/documentation/csv"
mkdir -p "$SESSION_FOLDER/exports"
mkdir -p "$SESSION_FOLDER/scripts"
mkdir -p "$SESSION_FOLDER/agent_logs"
mkdir -p "$SESSION_FOLDER/source"

# Create agent log files
touch "$SESSION_FOLDER/agent_logs/resource_explorer.log"
touch "$SESSION_FOLDER/agent_logs/network_analyzer.log"
touch "$SESSION_FOLDER/agent_logs/config_exporter.log"
touch "$SESSION_FOLDER/agent_logs/cost_estimator.log"
touch "$SESSION_FOLDER/agent_logs/deploy_debugger.log"
touch "$SESSION_FOLDER/agent_logs/research_agent.log"
touch "$SESSION_FOLDER/agent_logs/documentation_generator.log"
touch "$SESSION_FOLDER/agent_logs/container_executor.log"
touch "$SESSION_FOLDER/agent_logs/browser_handoff.log"

# Create command log
cat > "$SESSION_FOLDER/command_log.md" << EOF
# Azure Session Command Log

**Session:** ${DATE}_AZURE_${TOPIC}
**Created:** $(date '+%Y-%m-%d %H:%M:%S')

---

## Commands Executed

| Timestamp | Agent | Command | Result |
|-----------|-------|---------|--------|
EOF

# Create initial progress file
cat > "$SESSION_FOLDER/progress/00_session_started_${TIMESTAMP}.md" << EOF
# Session Started

**Topic:** ${TOPIC}
**Date:** ${DATE}
**Time:** $(date '+%H:%M:%S')

## Status

- Session folder created
- Agent logs initialized
- Awaiting user instructions

## Next Steps

1. Verify Azure CLI authentication
2. Confirm target resource group(s)
3. Determine documentation format preference
4. Begin exploration
EOF

echo "Session folder created: $SESSION_FOLDER"
echo ""
echo "Structure:"
tree "$SESSION_FOLDER" 2>/dev/null || find "$SESSION_FOLDER" -type d | head -20
echo ""
echo "Ready to begin Azure work."
