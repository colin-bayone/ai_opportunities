#!/bin/bash
# Check for branch staleness and classify files
# Usage: ./check_staleness.sh <PR_NUMBER>

set -e

PR_NUMBER=$1
if [ -z "$PR_NUMBER" ]; then
    echo "Usage: $0 <PR_NUMBER>"
    exit 1
fi

# Ensure we're in the project root (git repository root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Checking Branch Staleness for PR #$PR_NUMBER ==="
echo ""

# Fetch latest main
echo "🔄 Fetching latest main..."
git fetch origin main

# Get head and base branch names
BRANCH_INFO=$(gh pr view "$PR_NUMBER" --json headRefName,baseRefName)
HEAD_BRANCH=$(echo "$BRANCH_INFO" | python3 -c "import sys, json; print(json.load(sys.stdin)['headRefName'])")
BASE_BRANCH=$(echo "$BRANCH_INFO" | python3 -c "import sys, json; print(json.load(sys.stdin)['baseRefName'])")

echo "Head Branch: $HEAD_BRANCH"
echo "Base Branch: $BASE_BRANCH"
echo ""

# Fetch the head branch
git fetch origin "$HEAD_BRANCH"

# Check commits ahead/behind
echo "📊 Checking commit status..."
COMMIT_COUNTS=$(git rev-list --left-right --count "origin/$BASE_BRANCH...origin/$HEAD_BRANCH" 2>/dev/null || echo "0 0")
BEHIND=$(echo "$COMMIT_COUNTS" | awk '{print $1}')
AHEAD=$(echo "$COMMIT_COUNTS" | awk '{print $2}')

echo "Commits in $BASE_BRANCH not in branch: $BEHIND"
echo "Commits in branch not in $BASE_BRANCH: $AHEAD"
echo ""

if [ "$BEHIND" -gt 0 ]; then
    echo "⚠️  BRANCH IS STALE (behind by $BEHIND commits)"
    echo ""

    # Find the merge-base (common ancestor) between base and head branches
    MERGE_BASE=$(git merge-base "origin/$BASE_BRANCH" "origin/$HEAD_BRANCH")
    echo "📍 Merge-base (common ancestor): $MERGE_BASE"
    echo ""

    # Save all PR files
    gh pr view "$PR_NUMBER" --json files --jq '.files[].path' > "/tmp/pr_${PR_NUMBER}_files.txt"

    echo "🔍 Classifying files..."
    echo "" > "/tmp/pr_${PR_NUMBER}_file_status.txt"

    while read -r file; do
        # Check if file exists in merge-base
        if git cat-file -e "$MERGE_BASE:$file" 2>/dev/null; then
            # File exists in merge-base, check if it was modified
            if git diff --quiet "$MERGE_BASE" "origin/$HEAD_BRANCH" -- "$file" 2>/dev/null; then
                # No changes from merge-base = already merged to main (shouldn't happen in stale branches)
                echo "UNCHANGED: $file" | tee -a "/tmp/pr_${PR_NUMBER}_file_status.txt"
            else
                # Changed from merge-base = legitimate modification
                echo "MODIFIED: $file" | tee -a "/tmp/pr_${PR_NUMBER}_file_status.txt"
            fi
        else
            # File doesn't exist in merge-base = new file
            echo "NEW: $file" | tee -a "/tmp/pr_${PR_NUMBER}_file_status.txt"
        fi
    done < "/tmp/pr_${PR_NUMBER}_files.txt"

    echo ""
    echo "=== Summary ==="
    UNCHANGED_COUNT=$(grep -c "^UNCHANGED:" "/tmp/pr_${PR_NUMBER}_file_status.txt" 2>/dev/null || echo "0")
    MODIFIED_COUNT=$(grep -c "^MODIFIED:" "/tmp/pr_${PR_NUMBER}_file_status.txt" 2>/dev/null || echo "0")
    NEW_COUNT=$(grep -c "^NEW:" "/tmp/pr_${PR_NUMBER}_file_status.txt" 2>/dev/null || echo "0")

    echo "UNCHANGED files (in PR but not modified from base): $UNCHANGED_COUNT"
    echo "MODIFIED files (existed in base and were changed): $MODIFIED_COUNT"
    echo "NEW files (didn't exist in base): $NEW_COUNT"
    echo ""
    echo "📁 Detailed classification saved to: /tmp/pr_${PR_NUMBER}_file_status.txt"
else
    echo "✅ Branch is up to date with $BASE_BRANCH"
fi

# Check for deletions
echo ""
echo "🗑️  Checking for deletions..."
DELETIONS=$(gh pr view "$PR_NUMBER" --json deletions | python3 -c "import sys, json; print(json.load(sys.stdin)['deletions'])")

if [ "$DELETIONS" -gt 0 ]; then
    echo "⚠️  PR shows $DELETIONS deletions"
    echo ""
    echo "Deleted files:"
    gh pr view "$PR_NUMBER" --json files --jq '.files[] | select(.status == "removed") | .path' | while read -r file; do
        echo "  - $file"
        if git cat-file -e "origin/$BASE_BRANCH:$file" 2>/dev/null; then
            echo "    ⚠️  WARNING: File exists in $BASE_BRANCH but deleted in PR - verify intentional"
        fi
    done
else
    echo "✅ No deletions in this PR"
fi

echo ""
echo "✅ Staleness check complete"
