#!/bin/bash
# Prepare local environment for PR review
# Ensures local main is clean and up to date before staleness check
# Usage: ./prepare_local_env.sh

set -e

echo "=== Preparing Local Environment for PR Review ==="
echo ""

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "❌ ERROR: Not in a git repository"
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📍 Current branch: $CURRENT_BRANCH"
echo ""

# Checkout main branch
echo "🔄 Checking out main branch..."
if ! git checkout main 2>/dev/null; then
    echo "❌ ERROR: Failed to checkout main branch"
    echo "   Make sure 'main' branch exists in your repository"
    exit 1
fi

echo "✅ Checked out main branch"
echo ""

# Check for staged or uncommitted changes
echo "🔍 Checking for uncommitted changes..."
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  WARNING: You have staged or uncommitted changes in your local repository."
    echo ""
    echo "Please resolve these changes before proceeding:"
    echo "  1. Commit your changes: git commit -m 'your message'"
    echo "  2. Stash your changes: git stash"
    echo "  3. Discard your changes: git reset --hard HEAD"
    echo ""
    echo "Uncommitted files:"
    git status --short
    echo ""
    exit 1
fi

echo "✅ No uncommitted changes"
echo ""

# Check if there are untracked files that might interfere
UNTRACKED_COUNT=$(git ls-files --others --exclude-standard | wc -l)
if [ "$UNTRACKED_COUNT" -gt 0 ]; then
    echo "ℹ️  Note: You have $UNTRACKED_COUNT untracked file(s)"
    echo "   These won't affect the review but consider cleaning up if needed"
    echo ""
fi

# Pull latest changes from origin/main
echo "📥 Pulling latest changes from origin/main..."
if ! git pull origin main; then
    echo ""
    echo "❌ ERROR: Failed to pull from origin/main"
    echo ""
    echo "This could be due to:"
    echo "  1. Merge conflicts - resolve conflicts and try again"
    echo "  2. No remote 'origin' configured"
    echo "  3. Network issues"
    echo ""
    echo "Please resolve the issue and run this script again."
    exit 1
fi

echo ""
echo "✅ Successfully pulled latest changes"
echo ""

# Show current commit
CURRENT_COMMIT=$(git rev-parse --short HEAD)
CURRENT_COMMIT_MSG=$(git log -1 --pretty=format:"%s")
echo "📌 Current main is at: $CURRENT_COMMIT"
echo "   $CURRENT_COMMIT_MSG"
echo ""

echo "✅ Local environment is ready for PR review!"
echo ""
echo "Next steps:"
echo "  1. Run: ./scripts/gather_pr_info.sh <PR_NUMBER>"
echo "  2. Run: ./scripts/check_staleness.sh <PR_NUMBER>"
