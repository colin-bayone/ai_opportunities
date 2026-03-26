# Scope Creep Reference Guide

This guide helps identify and handle scope creep during PR reviews.

## What is Scope Creep?

Scope creep occurs when a PR includes changes beyond what was specified in the linked issue. While some additional work is acceptable, significant deviations should be documented and discussed.

## Acceptable Scope Additions

These are generally acceptable and don't need special discussion:

### ✅ Documentation
- Additional README sections
- Expanded docstrings
- Code comments for clarity
- Usage examples beyond requirements

### ✅ Testing
- Extra test cases beyond requirements
- Edge case testing
- Integration tests for better coverage

### ✅ Code Quality
- Minor refactoring for readability
- Variable/function renaming for clarity
- Code formatting improvements
- Removal of unused imports

## Scope Creep That Must Be Noted

These should be documented in the review but may be acceptable:

### ⚠️ Features Marked as Future Work
**Example**: Issue says "Phase 2 will add filtering" but PR implements filtering

**Action**: 
- Note in review: "PR includes filtering feature marked for Phase 2"
- Assess quality of implementation
- Decide: Accept with note, or request removal

### ⚠️ Unmentioned Functionality
**Example**: Issue asks for user profile page, PR adds profile editing too

**Action**:
- Document the additional feature
- Verify it doesn't conflict with planned work
- Consider: Is it a natural extension or separate feature?

### ⚠️ Bug Fixes Beyond Issue Scope
**Example**: While implementing feature X, developer fixed unrelated bug Y

**Action**:
- Note the bug fix
- Verify fix is correct
- Consider: Should it be a separate PR?

### ⚠️ Refactoring Unrelated Code
**Example**: Issue is about forms, but PR refactors unrelated utility functions

**Action**:
- Understand the motivation
- Assess risk of changes
- Consider: Is refactoring necessary for the feature?

### ⚠️ UI/UX Changes Not Specified
**Example**: Issue doesn't mention styling, but PR adds significant CSS

**Action**:
- Review design changes
- Check consistency with existing UI
- Consider: Should design be reviewed separately?

## Scope Creep That Often Requires Action

These typically need discussion with the developer:

### 🔴 Breaking Changes
**Example**: PR changes existing API that other code depends on

**Action**:
- **Block**: Request removal or separate PR
- Ensure breaking changes are planned and coordinated
- Check for deprecated functionality to maintain

### 🔴 Major Architectural Changes
**Example**: Issue asks for feature, PR restructures entire module

**Action**:
- **Pause review**: Needs architectural discussion
- Should be planned and reviewed separately
- May need team consensus

### 🔴 Security-Sensitive Changes
**Example**: PR includes authentication logic not in requirements

**Action**:
- **Requires security review**: Don't approve without it
- May need separate security-focused PR
- Ensure team security expert reviews

### 🔴 Dependencies on Unmerged Work
**Example**: PR includes changes from another pending PR

**Action**:
- **Block**: Request rebase or wait for dependency to merge
- See dependency violation patterns below

## How to Communicate Scope Creep

### For Acceptable Additions
```markdown
## Scope Notes
This PR includes some work beyond the issue requirements, which is acceptable:
- ✅ Additional test coverage for edge cases
- ✅ Expanded documentation with examples
These additions improve quality and are in scope.
```

### For Noted Additions
```markdown
## Scope Notes
This PR includes functionality beyond the original issue:
- ⚠️ Filtering feature (marked for Phase 2 in issue)
- ⚠️ Profile editing (not mentioned in issue)

**Assessment**: Implementation quality is good and doesn't conflict with roadmap. 
Accepting this time, but please stick to issue requirements in future PRs.

**Recommendation**: For future work, either:
1. Ask before adding features, or
2. Note additions in PR description
```

### For Problematic Additions
```markdown
## Scope Issues - Action Required

This PR includes changes that need to be addressed:

1. **Breaking API Changes** (lines 45-67 in api.py)
   - Changes method signatures that external code uses
   - **Action**: Please remove or create separate PR with deprecation plan

2. **Architectural Restructure** (entire services/ directory)
   - Major refactoring not mentioned in issue
   - **Action**: Needs team discussion before merging

Please address these issues and update the PR.
```

## Real-World Examples

### Example 1: Documentation Addition (Acceptable)
**Issue**: Add user registration endpoint
**PR Also Includes**: API documentation with examples
**Assessment**: ✅ Accept - improves usability

### Example 2: Feature Marked for Next Phase (Note)
**Issue**: Implement basic search, "Next phase: add filters"
**PR Also Includes**: Filter implementation
**Assessment**: ⚠️ Note - quality is good, discuss with PM

### Example 3: Unrelated Refactoring (Discuss)
**Issue**: Fix login bug
**PR Also Includes**: Restructure entire auth module
**Assessment**: 🔴 Discuss - scope creep is too large

### Example 4: Dependency Violation (Block)
**Issue**: Feature B depends on Feature A
**PR**: Includes both Feature A and B (Feature A not yet merged)
**Assessment**: 🔴 Block - wait for Feature A to merge, then rebase

## Decision Framework

Use this flowchart to decide how to handle scope creep:

1. **Is it in the issue?**
   - Yes → Not scope creep
   - No → Continue

2. **Is it docs/tests/minor cleanup?**
   - Yes → ✅ Accept
   - No → Continue

3. **Was it marked as future work in issue?**
   - Yes → ⚠️ Note and assess
   - No → Continue

4. **Is it a breaking change or major architectural change?**
   - Yes → 🔴 Discuss/Block
   - No → Continue

5. **Is implementation quality high and doesn't conflict with roadmap?**
   - Yes → ⚠️ Note with warning
   - No → 🔴 Request removal

## Best Practices for Reviewers

1. **Read the full issue first** - Know what's in and out of scope
2. **Check for "Future" sections** - These are explicitly out of scope
3. **Document all additions** - Even if acceptable
4. **Be consistent** - Set clear expectations for the team
5. **Provide options** - Give developer choices when possible
6. **Consider timing** - Sometimes accepting scope creep saves time
7. **Think about precedent** - What behavior are you encouraging?

## Red Flags

Watch for these patterns that indicate systematic issues:

- **Repeated offender**: Same developer consistently adds scope
- **Time pressure excuse**: "We needed it anyway so I added it"
- **Bundling unrelated fixes**: Multiple bugs fixed in one PR
- **Kitchen sink PRs**: Everything in one massive change
- **Ignoring feedback**: Developer continues after being asked to stick to scope

These patterns need team-level discussion and process improvements.
