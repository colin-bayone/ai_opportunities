#!/bin/bash
# Classify PR files by type (docs, tests, infrastructure, migrations, core)
# Usage: ./classify_files.sh <PR_NUMBER>

set -e

PR_NUMBER=$1
if [ -z "$PR_NUMBER" ]; then
    echo "Usage: $0 <PR_NUMBER>"
    exit 1
fi

# Check if staleness analysis exists
STATUS_FILE="/tmp/pr_${PR_NUMBER}_file_status.txt"
if [ -f "$STATUS_FILE" ]; then
    echo "=== Using files from staleness analysis (NEW/MODIFIED only) ==="
    FILES=$(grep -E "^(NEW|MODIFIED):" "$STATUS_FILE" | sed 's/^[^:]*: //')
else
    echo "=== Analyzing all PR files ==="
    FILES=$(gh pr view "$PR_NUMBER" --json files --jq '.files[].path')
fi

echo ""
echo "📚 Classifying files..."
echo ""

# Initialize counters
DOCS=0
INFRA=0
TESTS=0
MIGRATIONS=0
CORE=0

# Initialize file lists
echo "" > "/tmp/pr_${PR_NUMBER}_docs.txt"
echo "" > "/tmp/pr_${PR_NUMBER}_infra.txt"
echo "" > "/tmp/pr_${PR_NUMBER}_tests.txt"
echo "" > "/tmp/pr_${PR_NUMBER}_migrations.txt"
echo "" > "/tmp/pr_${PR_NUMBER}_core.txt"

# Classify each file
while IFS= read -r file || [ -n "$file" ]; do
    if [[ "$file" =~ \.md$ ]] || [[ "$file" =~ README ]] || [[ "$file" =~ docs/ ]]; then
        echo "📚 DOC: $file"
        echo "$file" >> "/tmp/pr_${PR_NUMBER}_docs.txt"
        ((DOCS++)) || true
    elif [[ "$file" =~ __init__\.py$ ]] || [[ "$file" =~ apps\.py$ ]] || [[ "$file" =~ settings ]] || [[ "$file" =~ setup\.py$ ]] || [[ "$file" =~ requirements\.txt$ ]] || [[ "$file" =~ pyproject\.toml$ ]] || [[ "$file" =~ poetry\.lock$ ]]; then
        echo "🏗️  INFRA: $file"
        echo "$file" >> "/tmp/pr_${PR_NUMBER}_infra.txt"
        ((INFRA++)) || true
    elif [[ "$file" =~ test_ ]] || [[ "$file" =~ _test\. ]] || [[ "$file" =~ tests/ ]] || [[ "$file" =~ /test/ ]]; then
        echo "🧪 TEST: $file"
        echo "$file" >> "/tmp/pr_${PR_NUMBER}_tests.txt"
        ((TESTS++)) || true
    elif [[ "$file" =~ migrations/ ]] && [[ "$file" =~ \.py$ ]]; then
        echo "🗄️  MIGRATION: $file"
        echo "$file" >> "/tmp/pr_${PR_NUMBER}_migrations.txt"
        ((MIGRATIONS++)) || true
    else
        echo "💻 CORE: $file"
        echo "$file" >> "/tmp/pr_${PR_NUMBER}_core.txt"
        ((CORE++)) || true
    fi
done <<< "$FILES"

echo ""
echo "=== File Classification Summary ==="
echo "📚 Documentation: $DOCS files"
echo "🏗️  Infrastructure: $INFRA files"
echo "🧪 Tests: $TESTS files"
echo "🗄️  Migrations: $MIGRATIONS files"
echo "💻 Core Code: $CORE files"
echo ""
echo "Total files to review: $((DOCS + INFRA + TESTS + MIGRATIONS + CORE))"
echo ""
echo "📁 Detailed lists saved to:"
echo "  - /tmp/pr_${PR_NUMBER}_docs.txt"
echo "  - /tmp/pr_${PR_NUMBER}_infra.txt"
echo "  - /tmp/pr_${PR_NUMBER}_tests.txt"
echo "  - /tmp/pr_${PR_NUMBER}_migrations.txt"
echo "  - /tmp/pr_${PR_NUMBER}_core.txt"
