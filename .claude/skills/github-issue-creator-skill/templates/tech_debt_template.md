# Issue: [Refactoring/Improvement Title]

**Dependencies:** [List prerequisite issues or state "None"]  
**Estimated Complexity:** [Low/Medium/High] - [Brief reasoning]

---

## Description

[Clear explanation of what needs refactoring/improving and why]

**Current Problem:**
[What's wrong with the current implementation]

**Proposed Improvement:**
[What should change]

**Benefits:**
- [Primary benefit - e.g., improved performance]
- [Secondary benefit - e.g., better maintainability]
- [Additional benefits - add as many as relevant to justify the refactoring]

---

## Current State

### What Exists Now

**File:** `path/to/current/file.py`

**Current Pattern:**
```python
# Current implementation pattern
def current_approach():
    # Problem: [what's wrong]
    # Impact: [why it matters]
    pass
```

**Issues with Current Approach:**
1. [Primary technical problem]
2. [Maintainability concern]
3. [Performance or scalability issue]
4. [Additional issues as needed to make the case for refactoring]

### Why This is Technical Debt

[Explanation of how this violates best practices or creates problems]

**Violated Best Practices:**
- `[doc_name].md` - [Specific principle violated]
- `[doc_name].md` - [Specific principle violated]

---

## Technical Approach

### Proposed Pattern

**New Structure:**
```python
# Improved implementation pattern
def improved_approach():
    # Solution: [how this fixes problems]
    # Benefits: [what this enables]
    pass
```

### Architecture Changes

[If structure changes]

```
Current:
Old Structure
     ↓
Problems

Proposed:
New Structure
     ↓
Benefits
```

**Key Improvements:**
- **[Primary Change]:** [What improves and how]
- **[Secondary Change]:** [Impact on code quality or performance]
- **[Additional Changes]:** [List as many improvements as the refactoring provides]

### Best Practices Alignment

This refactoring follows:
- [ ] `[doc_name].md` - [Specific section]
- [ ] `[doc_name].md` - [Specific section]

**Think about:**
- [Migration strategy concern?]
- [Backwards compatibility concern?]
- [Performance trade-off?]

---

## Tasks

### 1. [Refactoring Task]

**File:** `path/to/file.py`

[What needs to change]

**Migration Pattern:**
```python
# Pattern for migrating from old to new
def migration_approach():
    # Step 1: [preserve old]
    # Step 2: [add new]
    # Step 3: [switch over]
    # Step 4: [remove old]
    pass
```

**Think about:**
- [Backwards compatibility?]
- [Data migration needed?]

---

### 2. [Update Dependencies]

**Files:**
- `path/to/dependent/file1.py`
- `path/to/dependent/file2.py`

[What needs updating in dependent code]

---

### 3. [Testing/Verification]

**File:** `path/to/test/file.py`

[Test coverage needed]

**Pattern:**
```python
# Test pattern for new approach
def test_new_pattern():
    # Verify: [what to check]
    # Edge case: [what to test]
    pass
```

---

[Continue for 2-5 tasks total]

---

## Migration Strategy

### Phase 1: Add New Pattern

[How to introduce new pattern without breaking existing]

### Phase 2: Migrate Existing Usage

[How to transition from old to new]

**Migration Checklist:**
- [ ] Identify all usages of old pattern
- [ ] Create new implementation
- [ ] Test new implementation
- [ ] Switch usages one at a time
- [ ] Verify no regressions

### Phase 3: Remove Old Pattern

[When and how to deprecate old pattern]

**Deprecation:**
- Mark old pattern as deprecated
- Log warnings when used
- Remove after [timeframe]

### Backwards Compatibility

[How to maintain compatibility during migration]

---

## Testing

### Verification Steps

1. [Test that new pattern works]
2. [Test that existing functionality preserved]
3. [Test that migration path works]
4. [Test edge cases]

### Regression Testing

**Critical Paths to Test:**
- [Path 1: what to verify]
- [Path 2: what to verify]
- [Path 3: what to verify]

### Performance Testing

[If performance-related:]

**Metrics to Compare:**
- **Before:** [Current metric]
- **After:** [Expected metric]
- **Measurement:** [How to measure]

### Django Shell Verification

```python
python manage.py shell
>>> # Commands to verify refactoring
>>> # Compare old vs new behavior
```

---

## Acceptance Criteria

**Functionality:**
- [ ] New pattern implemented correctly
- [ ] All existing functionality preserved
- [ ] Migration path works smoothly
- [ ] No regressions introduced

**Code Quality:**
- [ ] Follows Django best practices
- [ ] Code is more maintainable
- [ ] Follows referenced best practices docs
- [ ] Comments explain complex logic

**Performance:**
- [ ] [Performance metric maintained/improved]
- [ ] No N+1 queries introduced
- [ ] Query optimization verified

**Testing:**
- [ ] Tests updated for new pattern
- [ ] Tests pass with old data
- [ ] Edge cases covered
- [ ] Regression tests added

**Migration:**
- [ ] Migration strategy documented
- [ ] Backwards compatibility maintained (if required)
- [ ] Deprecation path clear
- [ ] No breaking changes (or clearly documented)

---

## Notes

### Using Claude Code Effectively

**For Refactoring:**
[How Claude Code can help with refactoring]

**For Migration:**
[How Claude Code can assist with migration]

**For Testing:**
[How Claude Code can help verify no regressions]

### Django Patterns Reference

**[Old Pattern Name]:**
[Why it was problematic]

**[New Pattern Name]:**
[Why it's better and how it works]

**Migration Pattern:**
[Standard Django migration approach for this type of change]

### Common Pitfalls

1. **[Pitfall 1]:** [How to avoid]
2. **[Pitfall 2]:** [How to avoid]
3. **[Pitfall 3]:** [How to avoid]

### Design Decisions

**[Decision Point]:**
- **Option A:** [Pros/cons]
- **Option B:** [Pros/cons]
- **Recommendation:** [Choice and reasoning]

### Risk Assessment

**What Could Go Wrong:**
- **Risk 1:** [Mitigation]
- **Risk 2:** [Mitigation]
- **Risk 3:** [Mitigation]

**Rollback Plan:**
[How to revert if issues arise]

### Performance Impact

**Expected Improvements:**
- [Metric 1: improvement]
- [Metric 2: improvement]

**Potential Costs:**
- [Trade-off 1: if any]
- [Trade-off 2: if any]

### Future Considerations

This refactoring enables:
- [Future improvement or feature]
- [Additional capability]
- [More possibilities - list as many as relevant]

---

## Related Issues

- Addresses technical debt from [Issue description]
- Enables [Issue description]
- Related to [Issue description]

---

## Additional Context

[Any additional information, before/after examples, performance data, etc.]
