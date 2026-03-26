---
name: github-issue-creator
description: Creates comprehensive, well-structured GitHub issues for Django development teams working with Claude Code, following established workflow patterns and referencing internal best practices documentation. Use when converting PR feedback into issues, breaking down features into tasks, creating bug reports, or documenting technical debt.
---

# GitHub Issue Creator

This skill creates comprehensive GitHub issues for Django developers working with Claude Code, following BayOne's workflow and referencing internal best practices documentation.

## When to Use This Skill

Use this skill to:
- Convert PR review feedback into actionable issues
- Break down large features into developer-ready tasks
- Create bug reports with proper technical context
- Document technical debt or refactoring needs
- Ensure issues reference appropriate best practices docs

## Workflow Context

Issues created by this skill integrate with the target workflow:

**Developer's workflow:**
1. Retrieves issue with `gh issue view {number}`
2. Works with Claude Code for implementation
3. Creates feature branch: `feature/issue-{number}-brief-description`
4. Opens Draft PR after first commits
5. Makes daily commits (minimum one per day)
6. Asks team lead to review model changes (developers don't run migrations on main)
7. Follows 4-hour rule (reach out if stuck >4 hours)

**Critical workflow rules:**
- Model changes: Developer creates locally, tests on Docker postgres, asks for review before migration
- Daily commits required (via Draft PR, PR update, or completed PR)
- No silent work - team visibility mandatory
- Getting unstuck: 4-hour rule, use Claude Code, coordinate with team

## Issue Creation Process

**Before Starting:**
- Trust the skill guidance and templates - minimize upfront questions
- Proceed with creating the issue based on available context
- DON'T ask obvious questions that the skill or documentation already answers
- DO ask when there's a genuinely important architectural decision or ambiguity
- When asking, always suggest options in the context of this specific repo
- Start with a draft and iterate rather than extensive upfront questioning

### Step 1: Narrate and Determine Issue Type

Begin by narrating: "I'll create a [type] issue for [brief description]. Let me identify the appropriate template and relevant documentation."

**Issue types:**
- **Bug**: Broken functionality, incorrect behavior, security vulnerability
- **Feature**: New functionality, enhancement, user-facing improvement
- **Tech Debt**: Refactoring, optimization, code quality improvement

### Step 2: Identify Relevant Documentation

Analyze the issue domain and read relevant best practices from `.claude/skills/github-issue-creator-skill/references/`:

**Documentation mapping:**
- Authentication/Authorization → `.claude/skills/github-issue-creator-skill/references/authentication_authorization_best_practices.md`
- API/REST endpoints → `.claude/skills/github-issue-creator-skill/references/django_rest_framework_best_practices.md`
- Database/queries → `.claude/skills/github-issue-creator-skill/references/postgresql_best_practices_v2.md`
- Performance issues → `.claude/skills/github-issue-creator-skill/references/performance_monitoring_best_practices.md`
- Security concerns → `.claude/skills/github-issue-creator-skill/references/web_security_best_practices.md`, `.claude/skills/github-issue-creator-skill/references/soc2_considerations.md`
- PII/Privacy → `.claude/skills/github-issue-creator-skill/references/pii_detection_best_practices_review_guide.md`
- Templates/UI → `.claude/skills/github-issue-creator-skill/references/django_templates_best_practices.md`, `.claude/skills/github-issue-creator-skill/references/htmx_best_practices.md`
- Background jobs → `.claude/skills/github-issue-creator-skill/references/celery_best_practices.md`
- Caching → `.claude/skills/github-issue-creator-skill/references/redis_best_practices.md`
- WebSockets → `.claude/skills/github-issue-creator-skill/references/channels_websockets_best_practices.md`
- AI/ML → `.claude/skills/github-issue-creator-skill/references/ai_ml_integration_best_practices.md`
- Middleware → `.claude/skills/github-issue-creator-skill/references/custom_middleware_best_practices.md`
- Audit logging → `.claude/skills/github-issue-creator-skill/references/audit_logging_best_practices.md`
- CDN/Assets → `.claude/skills/github-issue-creator-skill/references/cdn_sri_best_practices.md`
- Azure services → `.claude/skills/github-issue-creator-skill/references/azure_openai_best_practices.md`, `.claude/skills/github-issue-creator-skill/references/azure_storage_best_practices.md`, `.claude/skills/github-issue-creator-skill/references/azure_services_best_practices.md`
- General Django → `.claude/skills/github-issue-creator-skill/references/django_best_practices.md`

Narrate which documentation is being referenced: "Based on the issue domain, I'll reference [doc1] and [doc2] to ensure the issue follows established patterns."

Read the identified documentation files before proceeding.

### Step 3: Load Appropriate Template

Load the template from `/templates/`:
- `bug_template.md` - For bugs, defects, security issues
- `feature_template.md` - For new features and enhancements
- `tech_debt_template.md` - For refactoring and optimization

Narrate: "Loading [template_name] to structure the issue."

### Step 4: Author the Issue

**CRITICAL: Issue Naming Format**
- Always use: `# Issue: [Descriptive Title]`
- NEVER use: `# Issue 1:`, `# Issue #1:`, or any numbered format
- GitHub will assign the actual issue number when created
- The templates show the correct format - follow them exactly

Follow template structure with these principles:

**Content Guidelines:**
- Trust Claude Code to implement (show patterns, not complete solutions)
- Include "Think about:" questions for design decisions
- Provide practical pseudocode (<30 lines per example)
- Reference specific files with full paths from project root
- Keep examples focused on patterns
- Target 150-250 lines total
- Use as many bullet points as needed (not fixed to 3 items)

**Required sections:**
1. **Header** - Title (action-oriented, 50-70 chars), Dependencies, Estimated Complexity
2. **Description** - What, why, impact, technical context
3. **Technical Approach** - Architecture overview, key components, patterns
4. **Tasks** - 2-5 numbered tasks with file paths and pseudocode patterns
5. **Testing** - Manual testing flow, edge cases, verification steps
6. **Acceptance Criteria** - Checkboxes covering functionality and quality
7. **Notes** - Django patterns, Claude Code tips, design decisions, pitfalls

**Code Example Patterns:**

**What to Include (GOOD):**
- ✅ Short pseudocode showing structure (<30 lines)
- ✅ Method signatures and key patterns
- ✅ Specific Django patterns (e.g., `select_related` usage)
- ✅ Design questions ("Think about: AND vs OR logic?")

**What Crosses the Line (BAD):**
- ❌ Complete implementations with all fields/methods defined
- ❌ Full model class definitions (just show key fields/patterns)
- ❌ Complete test code (show test scenarios in prose)
- ❌ Large code blocks (>30 lines)
- ❌ Copy-paste ready solutions

**Examples:**

Good (pattern-focused):
```python
# Pattern: Use select_related for ForeignKey lookups
def get_queryset(self):
    return Model.objects.select_related('fk1', 'fk2').filter(...)
```

Good (pseudocode with design questions):
```python
def filter_candidates(candidates, filters):
    # Start with all candidates
    # For each filter present:
    #   Apply filter logic
    #   Narrow result set
    # Return filtered list

    # Think about: AND vs OR logic for multi-select filters?
```

Bad (too complete):
```python
# Don't provide complete model with all fields:
class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(...)
    action = models.CharField(...)
    # ... 20 more fields with complete definitions

    def save(self, *args, **kwargs):
        # ... complete save implementation
```

Narrate progress: "I've drafted the Description and Technical Approach. Now creating the Tasks section with [X] tasks covering [areas]."

### Step 5: Review Against Quality Checklist

Before finalizing, verify:
- [ ] Title clear and actionable
- [ ] Issue naming format correct: `# Issue: [Title]` (NO numbers like "Issue 1:")
- [ ] Dependencies explicitly stated
- [ ] At least one best practices doc referenced with FULL PATH (`.claude/skills/github-issue-creator-skill/references/...`)
- [ ] File paths correct and specific (from project root)
- [ ] Code examples show patterns, NOT complete solutions (<30 lines)
- [ ] Testing steps use existing infrastructure (real URLs, actual models)
- [ ] Acceptance criteria testable
- [ ] SOC2 considerations included (if relevant)
- [ ] "Using Claude Code Effectively" section included (written FOR Claude Code to read)
- [ ] Design decisions explained in Notes
- [ ] No time estimates
- [ ] No "assigned to" or priority labels
- [ ] No emojis
- [ ] No giant code blocks (>30 lines)
- [ ] Lists flexible (not fixed to 3 items)

Narrate: "Reviewing against checklist... [findings]. Making adjustments to [areas]."

### Step 6: Write Issue to File

**IMPORTANT:** NEVER paste the issue content directly into chat. ALWAYS write the issue to a markdown file.

Write the completed issue to a file in the session folder or a designated location:
- File path: `.django-workflow/issues/issue-{brief-slug}.md` or similar
- If no session folder exists, use: `docs/issues/draft-issue-{brief-slug}.md`

After writing the file, inform the user:
- Where the file was saved
- Ask if they want to review it

Narrate: "Issue written to [file_path]. This [type] issue covers [scope] and references [docs]. It includes [X] tasks and [Y] acceptance criteria. Would you like to review it before I create it on GitHub?"

### Step 7: WAIT FOR EXPLICIT PERMISSION

**CRITICAL - MANDATORY STEP:**

**NEVER run `gh issue create` without explicit user permission.**

After writing the issue to a file:
1. Tell the user where the file is saved
2. Ask: "Would you like to review it before I create it on GitHub?"
3. WAIT for the user to either:
   - Review and approve: "Yes, create it" / "Looks good, go ahead" / explicit approval
   - Request changes: Make the changes, then ask again
   - Reject: Do not create the issue

**What counts as permission:**
- "Yes, create it"
- "Go ahead"
- "Looks good, create the issue"
- "Create it on GitHub"
- Any explicit affirmation to create

**What does NOT count as permission:**
- "Yes" (to a different question, like "should we proceed with the rename?")
- Silence
- "Looks good" (without explicit instruction to create)
- Implied approval

**If in doubt, ask explicitly:** "Do you want me to run `gh issue create` now?"

This step exists because creating GitHub issues is an irreversible action that affects the repository. The user MUST have the opportunity to review the issue content before it goes live.

## Using Sub-Agents (Optional)

For complex issues, consider a two-agent workflow:

**Agent 1 (Analyzer):**
- Analyzes the issue request
- Identifies relevant documentation
- Determines scope and complexity
- Creates outline with key sections

**Agent 2 (Author):**
- Receives outline from Agent 1
- Drafts complete issue following template
- Includes code patterns and examples
- Writes Testing and Notes sections

**Agent 3 (Reviewer):**
- Receives draft from Agent 2
- Checks against quality checklist
- Verifies documentation references accurate
- Ensures acceptance criteria testable
- Suggests improvements

To use sub-agents:
1. Create Agent 1 to analyze and outline
2. Create Agent 2 to draft from outline
3. Create Agent 3 to review and refine
4. Present final issue to user

Narrate sub-agent usage: "Using multi-agent approach: Agent 1 analyzing scope, Agent 2 drafting content, Agent 3 reviewing quality."

## Template Structure Guidance

### Bug Template Elements

**Bug Description:**
- Current vs expected behavior
- Security/business impact
- Affected users/systems

**Proposed Fix:**
- Implementation approach
- Code patterns to use
- Best practices to follow
- "Think about:" design questions

**Testing Strategy:**
- Steps to reproduce and verify fix
- Edge cases to test
- Regression prevention

### Feature Template Elements

**Description:**
- Feature goal and user benefit
- Technical scope
- Integration points
- Use as many bullets as needed to clearly communicate

**Technical Approach:**
- Architecture overview (text diagrams encouraged)
- Key components and roles
- Data flow or interaction patterns

**Implementation Guidance:**
- Django patterns to use
- Code organization strategies
- "Think about:" design questions

### Tech Debt Template Elements

**Current State:**
- What exists now
- Why it's problematic
- Technical debt classification

**Proposed Improvement:**
- What should change
- Benefits and impact
- Migration strategy

**Risk Assessment:**
- What could go wrong
- Mitigation strategies
- Rollback plan

## Best Practices for Issue Writing

### DO:
- Show Django patterns and method signatures
- Include "Think about:" sections for design decisions
- Reference specific best practices doc sections
- Provide clear file paths from project root
- Include architecture/flow diagrams (text-based)
- Add "Using Claude Code Effectively" section
- List common pitfalls to avoid
- Cover SOC2 requirements when relevant
- Make testing steps actually doable with existing infrastructure
- Trust Claude Code to implement details
- Use flexible list lengths (not fixed to 3 items)

### DON'T:
- Write large code blocks (>30 lines)
- Provide copy-paste solutions
- Include time estimates
- Add "assigned to" or priority levels
- Reference specific issue numbers
- Use emojis
- Tell developers to run migrations on main
- Explain basic Django concepts
- Make testing steps theoretical
- Over-specify implementation details
- Limit lists to exactly 3 items

## Code Example Guidelines

### Pattern-Focused Examples (Good)

Show method signatures and key logic:
```python
# Pattern: Use select_related for ForeignKey lookups
def get_queryset(self):
    return Candidate.objects.select_related(
        'client_group',
        'created_by'
    ).filter(...)
```

### Pseudocode with Design Questions (Good)

```python
def filter_candidates(candidates, filters):
    # Parse filter parameters
    # Apply each filter type:
    #   - Skills filter (think about: AND vs OR logic?)
    #   - Experience range
    #   - Location matching
    # Return filtered results
    pass
```

### Avoid Complete Implementations (Bad)

Don't write 50+ line complete class implementations.

## Testing Section Guidelines

### Manual Testing Steps

Use actual URLs and admin paths:
```
1. Navigate to /candidates/search/
2. Log in as test user (create via admin if needed)
3. Select filters: Python, Django skills
4. Click "Search" button
5. Verify: Only candidates with both skills appear
6. Check stats badges update correctly
```

### Django Shell Testing

When appropriate:
```python
python manage.py shell
>>> from myapp.models import Model
>>> obj = Model.objects.first()
>>> obj.new_method()  # Test new functionality
>>> # Verify expected behavior
```

### Test Coverage Requirements

Include:
- Manual testing flow (step-by-step with real URLs)
- Edge cases (empty results, missing data, boundary conditions)
- Error scenarios (invalid input, permission denials)
- Integration testing (if multiple components interact)

## SOC2 Considerations

### When to Include SOC2 Section

Always include for:
- Authentication/authorization changes
- User data handling or PII processing
- Audit logging implementation
- Access control modifications
- Security features or fixes
- Admin interface changes

**SOC2 Checklist Items:**
- [ ] Audit logging implemented for sensitive operations
- [ ] PII properly masked in logs
- [ ] Access control enforced (multi-tenancy, roles)
- [ ] Input validation prevents injection attacks
- [ ] Changes don't bypass security controls
- [ ] Complies with `soc2_considerations.md`

### Example SOC2 Section

```markdown
## SOC2 Compliance

**Audit Logging:**
- Log candidate access with user_id and timestamp
- Use AuditService for immutable logs
- Capture failed access attempts

**Access Control:**
- Filter candidates by client_group_id
- Use @filter_by_client_group decorator
- Verify permissions before data display

Reference: `soc2_considerations.md` - "Audit Logging" section
```

## Architecture Communication

### Text-Based Diagrams

Use simple ASCII/text diagrams:
```
User Request
     ↓
Django FBV (candidate_search_view)
     ↓
Filter Service → Mock Data Generator
     ↓
Calculate Stats
     ↓
Render Template → Components
```

### Component Relationships

Explain how pieces connect:
```
**Key Components:**
- View: Handles requests, coordinates logic
- Service: Business logic, filtering operations
- Models: Data access, validation
- Templates: Display, user interaction
- Forms: Input validation, data cleaning
```

## Using Claude Code Effectively

### Always Include This Section

This section serves two audiences:
- **20% Human developers** who might read the issue before starting work
- **80% Claude Code itself** when it reads the issue during implementation

Write this section as if speaking directly to Claude Code, pointing it to relevant resources and patterns.

**What to Include:**

**Point to Reference Materials:**
- "Review `.claude/skills/github-issue-creator-skill/references/django_best_practices.md` for Django patterns"
- "Check existing `core/storage/models.py` for the StoredFile pattern to follow"
- "Reference the AuditLog model in `core/diagnostics/models.py` for immutability pattern"

**Highlight Non-Obvious Considerations:**
- "Consider async/sync tradeoffs - bulk operations need 1:1 mapping integrity"
- "Note that JobDiva's bulk endpoint doesn't return IDs, so use synthetic bulk (loop single creates)"
- "Remember to handle both simple candidate creation AND resume-based creation"

**Suggest Validation Approaches:**
- "Use django-debug-toolbar to verify N+1 queries aren't introduced"
- "Test with 75 diverse candidates to ensure filters work with realistic data"
- "Verify QuerySet uses select_related/prefetch_related appropriately"

### Example Section

```markdown
## Using Claude Code Effectively

**Reference Materials:**
- Review `.claude/skills/github-issue-creator-skill/references/audit_logging_best_practices.md` for audit log patterns
- Check existing `core/diagnostics/models.py` → `AuditLog` class for immutability implementation
- Reference `.claude/skills/github-issue-creator-skill/references/django_best_practices.md` for model design patterns

**Key Patterns to Follow:**
- The AuditLog model demonstrates immutability via overriding `save()` to prevent updates
- Use `DateTimeField(auto_now_add=True)` for immutable timestamps
- Follow the existing audit service pattern in `core/diagnostics/services/`

**Testing Approach:**
- Generate diverse test data covering edge cases (null values, long strings, special characters)
- Use django-debug-toolbar to verify no N+1 queries introduced
- Test both normal flow and error scenarios (invalid input, missing required fields)

**Non-Obvious Considerations:**
- This model will store PII - ensure fields are appropriately marked for masking in logs
- Consider data retention - audit logs grow indefinitely, may need archival strategy later
```

## Notes Section Patterns

### Design Decisions

Explain architectural choices with options:
```markdown
### Filter Architecture Decisions

**Skills Filter - AND vs OR:**
- **AND**: Candidate must have ALL selected skills (more restrictive, precise)
- **OR**: Candidate has ANY selected skill (broader matches)

Document chosen approach in code. Consider use case requirements.
```

### Django Patterns

Reference Django best practices:
```markdown
### Django Patterns Reference

**Function-Based Views:**
Standard pattern for straightforward request handling.
Keep logic in view, delegate complex operations to helper functions.

**Context Building:**
Build context dict with all data templates need.
Better to include more than less - templates ignore unused context.
```

### Common Pitfalls

Warn about known issues:
```markdown
### Common Pitfalls

1. **Over-filtering:** Filters too restrictive → no results shown
2. **Filter state loss:** Pagination clears active filters
3. **Stats miscalculation:** Counting wrong subset after filtering
4. **Template expectations:** Context missing keys templates expect
5. **N+1 queries:** Missing select_related/prefetch_related
```

### Future Migration Path

When building foundations for future enhancement:
```markdown
### Future Migration Path

This FBV will later evolve into:
- CBV with class structure for reusability
- HTMX integration for dynamic filtering
- Registry pattern for AI matching
- Real database models (currently mock data)

For now: Keep implementation simple, make it work, document patterns.
```

## File Path Conventions

Always use full paths from project root:

**Good:**
- `recruitment/candidates/views.py`
- `core/accounts/models.py`
- `config/settings/base.py`

**Bad:**
- `views.py` (ambiguous)
- `the models file` (not specific)
- `somewhere in accounts` (not helpful)

## Acceptance Criteria Patterns

### Structure by Category

Group criteria logically:
```markdown
## Acceptance Criteria

**Functionality:**
- [ ] Feature works as described
- [ ] Edge cases handled properly
- [ ] Error messages clear and helpful
- [ ] [Additional items as needed]

**Code Quality:**
- [ ] Follows Django best practices
- [ ] No N+1 queries introduced
- [ ] Tests added and passing
- [ ] Code documented where complex

**Compliance:**
- [ ] Audit logging implemented
- [ ] PII properly masked
- [ ] Access control enforced
```

### Make Criteria Verifiable

Write testable, measurable criteria:

**Good (verifiable):**
- "Stats badges show correct counts after filtering (verify with test data)"
- "Query count < 10 for list view (measure with django-debug-toolbar)"
- "Audit log entry created with user_id, action, timestamp fields"

**Bad (vague):**
- "Stats work properly"
- "Performance is acceptable"
- "Audit logging works"

## Narration Guidelines

Throughout issue creation, narrate progress to maintain transparency:

**At each major step:**
- "Analyzing issue request... This is a [type] issue requiring [scope]"
- "Loading template: [template_name]"
- "Reading documentation: [doc1], [doc2] to ensure alignment with best practices"
- "Drafting Description section covering [aspects]"
- "Creating Tasks section with [X] tasks: [brief list]"
- "Writing Testing section with manual steps and [Y] edge cases"
- "Reviewing against quality checklist... Adjusting [areas]"
- "Issue complete: [summary of what was created]"

**During sub-agent workflow:**
- "Using multi-agent approach for complex issue"
- "Agent 1 (Analyzer): Determining scope and relevant documentation"
- "Agent 2 (Author): Drafting issue following template structure"
- "Agent 3 (Reviewer): Checking quality and completeness"
- "Final issue ready with [details]"

## Advanced Patterns

### Breaking Down Large Features

When a feature requires multiple issues:
1. Create parent tracking issue (epic) with overview
2. Break into 3-5 sub-issues (or as many as needed)
3. Define dependencies clearly between issues
4. Ensure each sub-issue stands alone
5. Order by progressive complexity (simple → complex)

### Dependency Management

**Explicit format:**
```markdown
**Dependencies:**
- Issue: Refactor Candidate Search into Modular Template Components
- Requires: Bootstrap 5 upgrade completed
- Blocks: HTMX Integration for Dynamic Filtering
```

### Migration Considerations

For model changes:
```markdown
## Migration Strategy

**Developer Actions:**
1. Make model changes locally
2. Test on Docker postgres
3. Generate migration: `python manage.py makemigrations`
4. Test migration locally: `python manage.py migrate`
5. Ask [team lead] to review model changes
6. **[Team lead] runs migration on main**

**Backwards Compatibility:**
- New fields nullable or have defaults
- No required fields without defaults
- Add fields before removing old ones
```

### Security Issue Patterns

For security bugs:
```markdown
## Security Impact

**Severity:** [High/Medium/Low]
**Type:** [Privilege Escalation/XSS/CSRF/Injection/etc]

**Potential Impact:**
- Unauthorized access to [resource]
- Data exposure of [type]
- Compliance violation: [regulation]

**Attack Vector:**
[How this could be exploited]

**Mitigation Priority:**
[Why immediate attention needed]
```

## Troubleshooting

### Issue Too Vague

**Add:**
- More technical context with specifics
- Exact file names and paths
- Code pattern examples
- Clearer acceptance criteria

### Issue Too Detailed

**Remove:**
- Complete code implementations
- Step-by-step tutorials
- Basic Django explanations
- Overly prescriptive implementation details

### Missing Documentation References

**Common patterns:**
- Model work → `django_best_practices.md`
- API work → `django_rest_framework_best_practices.md`
- Security → `web_security_best_practices.md` + `soc2_considerations.md`
- All work touching sensitive data → `soc2_considerations.md` (audit logging)

### Testing Steps Don't Work

**Verify:**
- URLs actually exist in current application
- Admin sections configured and accessible
- Models have necessary fields
- Test users have required permissions

## Examples Reference

See `/examples/` for complete issue examples:
- `example_bug_issue.md` - Security bug with multi-layer enforcement
- `example_feature_issue.md` - Feature with mock data and filtering

Study these examples to understand:
- Complete issue structure
- Balance between guidance and flexibility
- Code example patterns
- Testing approach
- Notes section content
