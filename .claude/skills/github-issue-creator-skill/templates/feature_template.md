# Issue: [Feature Title]

**Dependencies:** [List prerequisite issues or state "None"]  
**Estimated Complexity:** [Low/Medium/High] - [Brief reasoning]

---

## Description

[Clear explanation of what this feature builds]

**What This Builds:**
- [Key component or deliverable]
- [Another key component]
- [Additional components as needed]

**What This Enables:**
- [Primary capability unlocked]
- [Additional capabilities]
- [Further benefits - add as many as relevant]

**Why This Matters:**
[Business value and technical context. Why now?]

---

## Technical Approach

### Architecture Overview

```
[Text-based architecture diagram showing flow]
Component A
     ↓
Component B
     ↓
Component C
```

**Key Components:**
- **[Component Name]:** [Role and responsibility]
- **[Another Component]:** [Role and responsibility]
- **[Additional Components]:** [Add as many as needed to clearly explain architecture]

### Design Pattern

[Django pattern or architectural pattern to use]

**Pattern Structure:**
```python
# High-level pattern
class ComponentPattern:
    # Key methods and their purposes
    def method_name(self):
        # Pattern: [what pattern]
        pass
```

**Think about:**
- [Design decision 1?]
- [Design decision 2?]
- [Design decision 3?]

---

## Tasks

### 1. [Task Name]

**Create:** `path/to/new/file.py`

[Task description]

**Pattern:**
```python
# Pseudocode showing structure
def implementation_pattern():
    # Step 1: [what]
    # Step 2: [what]
    # Step 3: [what]
    pass
```

**Think about:**
- [Consideration 1?]
- [Consideration 2?]

**File path:** `path/to/new/file.py`

---

### 2. [Task Name]

**Update:** `path/to/existing/file.py`

[Task description]

**Pattern:**
```python
# Key pattern to add
```

**File path:** `path/to/existing/file.py`

---

### 3. [Task Name]

[Continue for 2-5 tasks total]

---

## Testing

### Manual Testing Flow

1. [Action step]
2. [Action step]
3. [Verification step]
4. [Verification step]

**Expected Behavior:**
- [What should happen at each step]
- [What user should see]

### Test Scenarios

**Scenario 1: [Name]**
1. [Steps]
2. [Expected result]

**Scenario 2: [Name]**
1. [Steps]
2. [Expected result]

### Edge Cases

Test these scenarios:
- [Edge case 1: what to test]
- [Edge case 2: what to test]
- [Edge case 3: what to test]

### Django Shell Testing

[If applicable:]
```python
python manage.py shell
>>> # Test code
>>> # Verification steps
```

---

## Acceptance Criteria

**Functionality:**
- [ ] Feature works as described
- [ ] All components integrate correctly
- [ ] Edge cases handled
- [ ] Error handling in place

**User Experience:**
- [ ] UI is intuitive and clear
- [ ] Loading states shown
- [ ] Error messages helpful
- [ ] Responsive on mobile/desktop

**Code Quality:**
- [ ] Follows Django best practices
- [ ] No N+1 queries
- [ ] Efficient QuerySets (select_related/prefetch_related)
- [ ] Code follows `django_best_practices.md`

**Testing:**
- [ ] Unit tests added and passing
- [ ] Integration tests cover main flow
- [ ] Manual testing completed
- [ ] Edge cases verified

**Documentation:**
- [ ] Code comments for complex logic
- [ ] Docstrings for public methods
- [ ] [Any user-facing docs updated]

[If relevant:]

**Compliance:**
- [ ] Audit logging implemented
- [ ] PII masked in logs
- [ ] Multi-tenancy respected (client_group filtering)
- [ ] Access control enforced
- [ ] Follows `soc2_considerations.md`

---

## Notes

### Using Claude Code Effectively

**For [Component] Implementation:**
[How Claude Code can help with specific component]

**For [Data/Logic] Generation:**
[How Claude Code can assist]

**For Testing:**
[How Claude Code can help write tests]

### Django Patterns Reference

**[Pattern Name]:**
[Explanation of Django pattern]

**[Another Pattern]:**
[Explanation]

**[Data Pattern]:**
[If mock data or fixtures involved]

### Common Pitfalls

1. **[Pitfall 1]:** [Description and how to avoid]
2. **[Pitfall 2]:** [Description and how to avoid]
3. **[Pitfall 3]:** [Description and how to avoid]

### Design Decisions

**[Decision Area]:**
[Options and recommendation]

**Think about:**
- [Consideration that affects choice]
- [Trade-off to consider]

**[Another Decision]:**
[Options and reasoning]

### Future Migration Path

[If this is a foundation for future work:]

This [component] will later [evolution]:
- [Future capability 1]
- [Future capability 2]
- [Future capability 3]

For now: [Current scope and why]

### Performance Considerations

[If relevant:]
- **Current approach:** [Why chosen]
- **Scale considerations:** [When to optimize]
- **Monitoring:** [What to watch]

### Integration Points

[If integrating with existing systems:]
- **[System/Component]:** [How this connects]
- **[System/Component]:** [How this connects]

---

## Related Issues

- Depends on [Issue description]
- Blocks [Issue description]
- Related to [Issue description]

---

## Additional Context

[Any mockups, diagrams, examples, or additional information]
