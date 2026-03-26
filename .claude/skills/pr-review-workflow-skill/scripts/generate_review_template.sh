#!/bin/bash
# Generate a review template for approval or change requests
# Usage: ./generate_review_template.sh <PR_NUMBER> <approval|changes>

set -e

PR_NUMBER=$1
REVIEW_TYPE=$2

if [ -z "$PR_NUMBER" ] || [ -z "$REVIEW_TYPE" ]; then
    echo "Usage: $0 <PR_NUMBER> <approval|changes>"
    exit 1
fi

OUTPUT_FILE="/tmp/pr_${PR_NUMBER}_review_${REVIEW_TYPE}.md"

if [ "$REVIEW_TYPE" == "approval" ]; then
    cat > "$OUTPUT_FILE" << 'EOF'
# PR Review - Approved

## Summary
[Brief overview of what PR does]

## What Was Reviewed
[List all components checked]
- Models: [specific models reviewed]
- Services: [specific services reviewed]
- Views: [specific views reviewed]
- Tests: [what was tested]

## Code Quality Assessment

### Django Best Practices ✅
- [Specific practices verified, e.g., "Proper use of ForeignKey with on_delete"]
- [List key quality points]

### Performance ✅
- [Performance considerations noted]
- [Query optimization checked]

## Testing
✅ [Specific test results]
- All existing tests pass
- New tests cover new functionality
- [Specific test commands run]

## Scope Notes
[If scope creep exists, document it here]
- Acceptable: Documentation expanded beyond requirements
- Noted: [Any features beyond issue scope]

## Changes Needed During Review
[If you identified issues that developer fixed]

## Approval Decision
[Clear statement of why approving]

---
**Django Best Practices:** ✅ Followed
**Tests:** ✅ All passing
**Scope:** ✅ [Acceptable/Noted/Addressed]
**Ready to Merge:** ✅ Yes
EOF

elif [ "$REVIEW_TYPE" == "changes" ]; then
    cat > "$OUTPUT_FILE" << 'EOF'
# PR Review - Changes Requested

## Issues Found

### Critical
[List blocking issues]

### Non-Critical
[List nice-to-have improvements]

## Scope Issues
[If scope creep needs addressing]

## Requested Changes
1. [Specific change needed]
2. [Specific change needed]

## Next Steps
[What developer should do]

Please address these issues and re-request review when ready.
EOF

else
    echo "Error: Review type must be 'approval' or 'changes'"
    exit 1
fi

echo "✅ Review template generated: $OUTPUT_FILE"
echo ""
echo "Edit this file with your review details, then use:"
echo "  gh pr review $PR_NUMBER --approve --body-file $OUTPUT_FILE"
echo "or:"
echo "  gh pr review $PR_NUMBER --request-changes --body-file $OUTPUT_FILE"
