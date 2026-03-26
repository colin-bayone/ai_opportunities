#!/bin/bash
# Gather comprehensive PR information
# Usage: ./gather_pr_info.sh <PR_NUMBER>

set -e

PR_NUMBER=$1
if [ -z "$PR_NUMBER" ]; then
    echo "Usage: $0 <PR_NUMBER>"
    exit 1
fi

echo "=== Gathering PR Information for #$PR_NUMBER ==="
echo ""

# Get comprehensive PR metadata
echo "📋 PR Metadata:"
gh pr view "$PR_NUMBER" --json title,body,author,headRefName,baseRefName,additions,deletions,changedFiles,files,commits,createdAt,updatedAt

# Save diff for analysis
echo ""
echo "💾 Saving diff to /tmp/pr_${PR_NUMBER}_diff.txt"
gh pr diff "$PR_NUMBER" > "/tmp/pr_${PR_NUMBER}_diff.txt"

echo ""
echo "✅ PR info gathered successfully"
