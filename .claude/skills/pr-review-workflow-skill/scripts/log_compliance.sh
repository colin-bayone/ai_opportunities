#!/bin/bash
# =============================================================================
# Skill Compliance Logging Helper
# =============================================================================
#
# Logs completion markers for the PR review skill compliance verification.
#
# Usage:
#   ./scripts/log_compliance.sh <PR_NUMBER> <STEP_MARKER>
#
# Example:
#   ./scripts/log_compliance.sh 1263 PHASE1_GATHER_PR_INFO
#
# The markers are checked by the verification hook before allowing PR approval.
# =============================================================================

set -euo pipefail

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <PR_NUMBER> <STEP_MARKER>" >&2
    exit 1
fi

PR_NUMBER="$1"
STEP_MARKER="$2"
LOG_FILE="/tmp/pr_${PR_NUMBER}_skill_compliance.log"

# Create log file if it doesn't exist
touch "$LOG_FILE"

# Check if marker already exists
if grep -q "^${STEP_MARKER}$" "$LOG_FILE" 2>/dev/null; then
    echo "Step already logged: $STEP_MARKER"
else
    echo "$STEP_MARKER" >> "$LOG_FILE"
    echo "Logged: $STEP_MARKER"
fi

# Show current progress
echo ""
echo "Compliance progress for PR #$PR_NUMBER:"
cat "$LOG_FILE" | while read line; do
    echo "  + $line"
done
