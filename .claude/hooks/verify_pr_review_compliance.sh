#!/bin/bash
# =============================================================================
# PR Review Skill Compliance Verification Hook
# =============================================================================
#
# This hook enforces deterministic compliance with the pr-review-workflow-skill.
# It blocks PR approval if required skill steps were not completed.
#
# Exit codes:
#   0 - All steps verified, allow action
#   2 - Compliance check failed, BLOCK action and notify Claude
#
# Usage:
#   Called automatically by Claude Code hooks system when attempting to
#   approve a PR via 'gh pr review --approve'
#
# =============================================================================

set -euo pipefail

# Read tool input from stdin (JSON format)
TOOL_INPUT=$(cat)

# Extract PR number from the command being run
# The input comes as the bash command string
COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')

# Try to extract PR number from various command patterns
PR_NUMBER=""
if [[ "$COMMAND" =~ gh[[:space:]]+pr[[:space:]]+review[[:space:]]+([0-9]+) ]]; then
    PR_NUMBER="${BASH_REMATCH[1]}"
fi

# If we couldn't extract PR number, allow the command (might not be a PR review)
if [[ -z "$PR_NUMBER" ]]; then
    exit 0
fi

LOG_FILE="/tmp/pr_${PR_NUMBER}_skill_compliance.log"

# If no log file exists, the skill wasn't followed at all
if [[ ! -f "$LOG_FILE" ]]; then
    echo "========================================" >&2
    echo "BLOCKED: PR Review Skill Compliance Check Failed" >&2
    echo "========================================" >&2
    echo "" >&2
    echo "No skill compliance log found for PR #$PR_NUMBER" >&2
    echo "" >&2
    echo "You MUST use the pr-review-workflow-skill to review PRs." >&2
    echo "" >&2
    echo "To invoke the skill, use:" >&2
    echo "  Skill(pr-review-workflow-skill)" >&2
    echo "" >&2
    echo "Or tell the user:" >&2
    echo "  'I need to follow the PR review workflow skill to review this PR properly.'" >&2
    echo "" >&2
    echo "The skill requires completing all phases (Pre-Review, Code Review," >&2
    echo "Decision) with compliance markers before approval is allowed." >&2
    echo "" >&2
    echo "Quick reviews and rubber-stamp approvals are not permitted." >&2
    echo "========================================" >&2
    exit 2
fi

# Define required steps for each phase
# Phase 1: Pre-Review Analysis
PHASE1_STEPS=(
    "PHASE1_GATHER_PR_INFO"
    "PHASE1_READ_LINKED_ISSUE"
    "PHASE1_PREPARE_LOCAL_ENV"
    "PHASE1_CHECK_STALENESS"
    "PHASE1_CLASSIFY_FILES"
    "PHASE1_SCOPE_CHECK"
    "PHASE1_COMPLETE"
)

# Phase 2: Code Review
PHASE2_STEPS=(
    "PHASE2_CREATE_WORKTREE"
    "PHASE2_CHECK_DEPENDENCIES"
    "PHASE2_LOAD_BEST_PRACTICES"
    "PHASE2_REVIEW_CORE_FILES"
    "PHASE2_RUN_TESTS"
    "PHASE2_IDENTIFY_ISSUES"
    "PHASE2_COMPLETE"
)

# Phase 3: Decision (only required before approval)
PHASE3_STEPS=(
    "PHASE3_DETERMINE_DECISION"
    "PHASE3_COMPLETE"
)

MISSING_STEPS=()
COMPLETED_STEPS=()

# Check Phase 1 steps
for step in "${PHASE1_STEPS[@]}"; do
    if grep -q "^$step$" "$LOG_FILE" 2>/dev/null; then
        COMPLETED_STEPS+=("$step")
    else
        MISSING_STEPS+=("$step")
    fi
done

# Check Phase 2 steps
for step in "${PHASE2_STEPS[@]}"; do
    if grep -q "^$step$" "$LOG_FILE" 2>/dev/null; then
        COMPLETED_STEPS+=("$step")
    else
        MISSING_STEPS+=("$step")
    fi
done

# Check Phase 3 steps
for step in "${PHASE3_STEPS[@]}"; do
    if grep -q "^$step$" "$LOG_FILE" 2>/dev/null; then
        COMPLETED_STEPS+=("$step")
    else
        MISSING_STEPS+=("$step")
    fi
done

# If any steps are missing, block the action
if [[ ${#MISSING_STEPS[@]} -gt 0 ]]; then
    echo "========================================" >&2
    echo "BLOCKED: PR Review Skill Compliance Check Failed" >&2
    echo "========================================" >&2
    echo "" >&2
    echo "PR #$PR_NUMBER cannot be approved - missing required steps:" >&2
    echo "" >&2
    for step in "${MISSING_STEPS[@]}"; do
        echo "  - $step" >&2
    done
    echo "" >&2
    echo "Completed steps:" >&2
    for step in "${COMPLETED_STEPS[@]}"; do
        echo "  + $step" >&2
    done
    echo "" >&2
    echo "You MUST complete all skill phases before approving." >&2
    echo "Go back and execute the missing steps, ensuring each" >&2
    echo "step writes its marker to the compliance log." >&2
    echo "========================================" >&2
    exit 2
fi

# All steps verified
echo "PR Review Skill Compliance: VERIFIED" >&2
echo "All ${#COMPLETED_STEPS[@]} required steps completed for PR #$PR_NUMBER" >&2
exit 0
