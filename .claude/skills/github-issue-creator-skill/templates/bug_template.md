# Issue: [Action-Oriented Bug Title]

**Dependencies:** [List any prerequisite issues or state "None"]  
**Estimated Complexity:** [Low/Medium/High] - [Brief complexity reasoning]

---

## Bug Description

[Clear description of what's broken. What's the incorrect behavior?]

**Impact:**
- **Users Affected:** [Who experiences this? Staff? External? Specific role?]
- **Business Impact:** [Revenue? User experience? Compliance risk?]
- **Severity Explanation:** [Why this matters]

**Current Behavior:**
[What actually happens]

**Expected Behavior:**
[What should happen instead]

---

## Current State

**Technical Explanation:**
[Why is this happening? What code is causing the issue?]

**Affected Components:**
- `path/to/affected/file1.py` - [Brief description]
- `path/to/affected/file2.py` - [Brief description]

**Root Cause:**
[If known, explain the underlying cause]

**Why It's a Bug:**
[Reference violated best practices or design principles]

---

## Technical Approach

### Implementation Strategy

[High-level approach to fix the bug]

**Pattern to Use:**
```python
# Show the pattern, not complete implementation
def corrected_approach():
    # Key change: [explanation]
    # Pattern: [Django pattern name]
    pass
```

**Before/After:**
```python
# Before (problematic)
def old_way():
    # Problem: [what's wrong]
    pass

# After (fixed)
def new_way():
    # Solution: [what fixes it]
    pass
```

### Best Practices References

This fix should follow:
- [ ] `[relevant_doc].md` - [Specific section]
- [ ] `[relevant_doc].md` - [Specific section]

**Think about:**
- [Design decision question 1?]
- [Design decision question 2?]

---

## Tasks

### 1. [Task Name]

**File:** `path/to/file.py`

[Task description with pattern guidance]

**Pattern:**
```python
# Pseudocode showing approach
def implementation_pattern():
    # Step 1: [what]
    # Step 2: [what]
    # Think about: [decision point]
    pass
```

---

### 2. [Task Name]

**File:** `path/to/file.py`

[Task description]

**Pattern:**
```python
# Key pattern to use
```

---

[Additional tasks as needed - typically 2-5 total]

---

## Testing

### Manual Testing Flow

1. [Step to reproduce the bug]
2. [Step to verify fix]
3. [Step to check for regressions]

**Verification:**
- [ ] Bug no longer reproduces
- [ ] [Specific behavior works correctly]
- [ ] No regressions in [related functionality]

### Edge Cases

Test these scenarios:
- [Edge case 1]
- [Edge case 2]
- [Edge case 3]

### Django Shell Testing

```python
python manage.py shell
>>> # Commands to test the fix
>>> # Verify expected behavior
```

---

## Acceptance Criteria

**Functionality:**
- [ ] Bug no longer reproduces following original steps
- [ ] [Specific expected behavior works]
- [ ] Edge cases handled properly
- [ ] Error messages clear and helpful

**Code Quality:**
- [ ] Follows Django best practices
- [ ] No N+1 queries introduced
- [ ] Tests added and passing
- [ ] Code follows referenced best practices

**Testing:**
- [ ] Unit tests cover the fix
- [ ] Integration tests verify end-to-end
- [ ] Manual testing completed
- [ ] No regressions detected

[If relevant, add SOC2 section:]

**Compliance:**
- [ ] Audit logging implemented (if security-related)
- [ ] PII properly masked in logs
- [ ] Access control maintained
- [ ] Complies with `soc2_considerations.md`

---

## Notes

### Using Claude Code Effectively

**For Bug Investigation:**
[How Claude Code can help investigate the bug]

**For Implementation:**
[How Claude Code can assist with the fix]

**For Testing:**
[How Claude Code can help write tests]

### Django Patterns Reference

**[Relevant Pattern Name]:**
[Explanation of Django pattern to use]

**[Another Pattern]:**
[Explanation]

### Common Pitfalls

Watch out for:
1. **[Pitfall 1]:** [Why it's a problem]
2. **[Pitfall 2]:** [Why it's a problem]
3. **[Pitfall 3]:** [Why it's a problem]

### Migration Strategy

[If model changes required:]

**Developer Actions:**
1. Make model changes locally
2. Test on Docker postgres
3. Generate migration: `python manage.py makemigrations`
4. Test migration locally
5. **Ask Colin to review model changes**
6. **Colin runs migration on main**

[Optional sections:]

### Security Considerations

[If security-related:]
- **Attack Vector:** [How this could be exploited]
- **Mitigation:** [How fix prevents exploitation]
- **Compliance:** [Relevant standards]

### Performance Impact

[If performance-related:]
- **Before:** [Metrics]
- **After:** [Expected metrics]
- **Measurement:** [How to verify]

---

## Related Issues

- Related to [Issue description]
- Caused by [Issue description]
- Blocks [Issue description]

---

## Additional Context

[Any additional information, screenshots, logs, etc.]
