---
description: Implement Django issue following team standards workflow
argument-hint: <issue-number or description>
---

# Pre-Flight Check: BayOne Marketplace Installation

**CRITICAL: Check if BayOne Solutions marketplace and django-team-standards skill are installed BEFORE starting work.**

## Step 1: Check if BayOne Marketplace is Installed

```bash
ls -la ~/.claude/plugins/marketplaces/bayone-solutions-skills/.claude-plugin/marketplace.json
```

**If file EXISTS:** Marketplace is installed ✅ - Skip to Step 3

**If file DOES NOT EXIST:** Marketplace is NOT installed ❌ - Continue to Step 2

## Step 2: Install BayOne Marketplace (if not installed)

**Inform user:** "BayOne Solutions marketplace is not installed. Installing now..."

```bash
# Clone the BayOne Solutions marketplace
git clone https://github.com/BayOne-Solutions/SKILLS.git \
  ~/.claude/plugins/marketplaces/bayone-solutions-skills
```

**Verify installation:**
```bash
ls -la ~/.claude/plugins/marketplaces/bayone-solutions-skills/.claude-plugin/marketplace.json
```

**If successful:** Display "✅ BayOne Solutions marketplace installed successfully!"

**If failed:** Display error and ask user to manually install:
```
❌ Failed to install BayOne marketplace automatically.

Please install manually:
git clone https://github.com/BayOne-Solutions/SKILLS.git \
  ~/.claude/plugins/marketplaces/bayone-solutions-skills

Then restart Claude Code and try again.
```

**STOP here if installation failed. Do NOT proceed.**

## Step 3: Verify django-team-standards Skill is Available

```bash
ls -la ~/.claude/plugins/marketplaces/bayone-solutions-skills/django-team-standards/SKILL.md
```

**If file EXISTS:** Skill is available ✅ - Continue to Phase 0

**If file DOES NOT EXIST:** Display error:
```
❌ django-team-standards skill not found in BayOne marketplace.

The marketplace was installed but the skill is missing.
Please check the marketplace repository or contact support.
```

**STOP here if skill not found. Do NOT proceed.**

## Step 4: Ready to Start

**Display to user:**
```
✅ BayOne Solutions marketplace: Installed
✅ django-team-standards skill: Available

Starting django-team-standards workflow...
```

---

# Start of Workflow

You are implementing a Django issue following the django-team-standards workflow.

**ISSUE TO WORK ON:** $ARGUMENTS

If $ARGUMENTS is a number (e.g., "193"), fetch the issue details using: `gh issue view $ARGUMENTS`
If $ARGUMENTS is text, use it as the issue description directly.

---

# CRITICAL: Comprehensive Issue Content Extraction ⚠️

**BEFORE any planning or implementation, you MUST extract and understand ALL guidance from the issue description.**

## Issue Content Parsing Checklist

When fetching an issue, **carefully parse the ENTIRE body** for these sections:

### 1. Core Requirements
- [ ] **Summary/Overview** - What the issue is asking for
- [ ] **User Story** - Who needs this and why ("As a... I want... So that...")
- [ ] **Acceptance Criteria** - Explicit success conditions
- [ ] **Scope** - What is in/out of scope
- [ ] **Dependencies** - Other issues or PRs this depends on

### 2. Technical Guidance (DO NOT SKIP!)
- [ ] **Considerations** - Special factors to account for
- [ ] **Know-Hows** - Specific technical approaches or patterns to follow
- [ ] **Claude Prompts/Examples** - Pre-written prompts or code examples provided
- [ ] **Implementation Hints** - Suggested approaches or solutions
- [ ] **Edge Cases** - Specific edge cases to handle
- [ ] **Error Handling** - Expected error scenarios and responses
- [ ] **Security Considerations** - Security requirements or warnings

### 3. Constraints & Limitations
- [ ] **Do NOT** sections - Explicit things to avoid
- [ ] **Breaking Changes** - What NOT to break
- [ ] **Performance Requirements** - Speed, memory, or scalability needs
- [ ] **Compatibility** - Browser, version, or backward compatibility needs

### 4. Design & UX Guidance
- [ ] **UI/UX Requirements** - Design specifications
- [ ] **Screenshots/Mockups** - Visual references (note: describe if present)
- [ ] **User Flow** - Step-by-step user interaction

### 5. Testing Requirements
- [ ] **Test Cases** - Specific tests to write
- [ ] **Test Data** - Sample data or fixtures needed
- [ ] **Manual Testing Steps** - How to verify manually

### 6. Documentation Requirements
- [ ] **Docs to Update** - Existing docs needing changes
- [ ] **New Docs Needed** - Documentation to create

## How to Extract Issue Content

```bash
# Get FULL issue content including body
gh issue view $ARGUMENTS --json title,body,labels,comments --jq '.'
```

**Parse the body field carefully. Issues often contain:**

```markdown
## Example Issue Structure

### Summary
[High-level description]

### Considerations
- Consider X when implementing Y
- Make sure to handle Z edge case
- Performance is critical here because...

### Know-Hows
1. Use the existing `ServiceClass` pattern
2. Follow the pattern in `module/example.py`
3. Reference implementation in PR #123

### Claude Prompt
```python
# Here is a starting point for implementation:
class NewFeature:
    def __init__(self):
        pass
```

### Examples
```python
# This is how it should work:
result = new_feature.process(input)
assert result.status == 'success'
```

### Edge Cases
- Empty input should return []
- Invalid format should raise ValidationError
- Large files (>10MB) need streaming

### Do NOT
- Do NOT modify the existing API contract
- Do NOT add new dependencies without approval
- Do NOT change the database schema (Phase 2)
```

## Store Extracted Guidance

Create a mental checklist of ALL guidance extracted from the issue:

```
ISSUE #XXX EXTRACTED GUIDANCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 REQUIREMENTS:
   - [List all explicit requirements]

💡 CONSIDERATIONS:
   - [List all considerations from issue]

🔧 KNOW-HOWS:
   - [List all technical approaches specified]

📝 CLAUDE PROMPTS/EXAMPLES:
   - [Note any code snippets or prompts provided]

⚠️ EDGE CASES:
   - [List all edge cases mentioned]

🚫 DO NOT:
   - [List all explicit restrictions]

✅ ACCEPTANCE CRITERIA:
   - [List all success conditions]
```

**This extracted guidance MUST be referenced throughout planning and implementation!**

---

# Reference Files Selection Based on Issue Type ⭐

**CRITICAL: Select and read relevant reference files BEFORE planning!**

Reference files location: `.claude/skills/pr-review-workflow-skill/references/`

## Reference File Selection Matrix

Based on the issue content, READ the appropriate reference files:

| Issue Type/Keywords | Reference Files to Read |
|---------------------|------------------------|
| **Models, ORM, QuerySets** | `django_best_practices.md` |
| **API, REST, Endpoints** | `django_rest_framework_best_practices.md` |
| **Azure OpenAI, AI Foundry, LLM** | `azure_openai_best_practices.md`, `ai_ml_integration_best_practices.md` |
| **Azure Storage, Blob, CDN** | `azure_storage_best_practices.md`, `cdn_sri_best_practices.md` |
| **Azure Services, Email, Search** | `azure_services_best_practices.md` |
| **Authentication, SSO, Permissions** | `authentication_authorization_best_practices.md` |
| **Audit Logs, SOC2, Compliance** | `audit_logging_best_practices.md`, `soc2_considerations.md` |
| **Celery, Tasks, Background Jobs** | `celery_best_practices.md` |
| **Redis, Cache, Sessions** | `redis_best_practices.md` |
| **WebSockets, Channels, Real-time** | `channels_websockets_best_practices.md` |
| **Templates, UI, Frontend** | `django_templates_best_practices.md`, `htmx_best_practices.md` |
| **File Upload, Validation** | `file_validation_best_practices.md` |
| **PostgreSQL, Database, Queries** | `postgresql_best_practices_v2.md` |
| **Middleware, Request/Response** | `custom_middleware_best_practices.md` |
| **Performance, Metrics, Monitoring** | `performance_monitoring_best_practices.md` |
| **PII, Data Privacy, Masking** | `pii_detection_best_practices_review_guide.md` |
| **Security, XSS, CSRF, Headers** | `web_security_best_practices.md` |
| **Scope, Feature Creep, Boundaries** | `scope_creep_guide.md` |

## Always Read These (Core References)

For EVERY issue, always reference:
1. `django_best_practices.md` - Core Django patterns
2. `soc2_considerations.md` - Compliance checklist (we're SOC2 compliant)
3. `scope_creep_guide.md` - Prevent scope creep

## Reference File Reading Protocol

```bash
# List available reference files
ls -la .claude/skills/pr-review-workflow-skill/references/

# Read relevant files based on issue type
# Example: For an Azure OpenAI issue
cat .claude/skills/pr-review-workflow-skill/references/azure_openai_best_practices.md
cat .claude/skills/pr-review-workflow-skill/references/ai_ml_integration_best_practices.md
```

## Document Reference Usage

When creating your plan, explicitly note which reference files you consulted:

```markdown
## References Consulted
- ✅ `django_best_practices.md` - Applied: query optimization patterns
- ✅ `azure_openai_best_practices.md` - Applied: AI Foundry integration pattern
- ✅ `soc2_considerations.md` - Applied: audit logging requirements
```

# Phase 0: Issue Status Check ⚠️

**IMPORTANT: Check if issue is already closed BEFORE doing any work!**

If $ARGUMENTS is a number, check the issue status and related PRs first:

## Step 1: Check Issue Status
```bash
gh issue view $ARGUMENTS --json state,closedAt,title --jq '{state: .state, closedAt: .closedAt, title: .title}'
```

## Step 2: Check for Related PRs
```bash
# Find PRs that reference this issue
gh pr list --search "fixes #$ARGUMENTS OR closes #$ARGUMENTS OR resolves #$ARGUMENTS" --json number,title,state,url --limit 5

# Also check PRs linked to the issue
gh issue view $ARGUMENTS --json closedBy --jq '.closedBy'
```

## Step 3: If PR exists, get PR details and comments
```bash
# Get PR comments (implementation notes, review feedback, decisions)
gh pr view [PR_NUMBER] --json comments,reviews --jq '{comments: [.comments[] | {author: .author.login, body: .body}], reviews: [.reviews[] | {author: .author.login, state: .state, body: .body}]}'

# Get PR file changes (what was actually implemented)
gh pr view [PR_NUMBER] --json files --jq '.files[] | {path: .path, additions: .additions, deletions: .deletions}'
```

## Step 4: Analyze and Present to User

**If issue state is "CLOSED":**
1. Display to user:
   - ⚠️ **Issue #XXX was already closed on [date]**
   - Title: [issue title]
   - PR that closed it: [PR number and link if found]
   - Key implementation details from PR comments (if any):
     * Design decisions made
     * Review feedback addressed
     * Edge cases handled
     * Testing approach used

2. Ask user what they want to do:
   - **Option 1**: Review/audit the existing implementation (read-only analysis, use PR comments for context)
   - **Option 2**: Reopen the issue to make additional changes (explain what needs changing)
   - **Option 3**: Exit (issue already complete)

3. **WAIT FOR USER RESPONSE** - Do NOT proceed with implementation phases unless user explicitly chooses Option 1 or 2

4. **If Option 1 (Review/Audit):**
   - Use PR comments and file changes to understand what was implemented
   - Focus audit on areas mentioned in PR reviews
   - Check if review feedback was properly addressed
   - Verify testing coverage matches PR discussion

5. **If Option 2 (Reopen):**
   - Read PR comments to understand previous implementation
   - Identify what needs to change (bug fix, enhancement, refactor)
   - Build on existing work rather than reimplementing from scratch

**If issue state is "OPEN":**
- Check if there's an open PR attempting to fix it
- If yes: Review PR comments/feedback to understand current approach and blockers
- Continue to Phase 1 (Documentation Discovery)

---

# Phase 1: Documentation Discovery and Validation

Read and validate documentation:
1. Read `CLAUDE.md` - Project structure, workflows, development principles
2. Read `pyproject.toml` - Dependencies, Python version, package constraints
3. Read `talent_ai_project/settings/base.py` - Configuration, installed apps
4. Search `docs/` for feature-specific documentation related to this issue
5. Cross-validate docs against actual codebase
6. Note documentation gaps (track but don't block)
7. Ask user for clarification when docs conflict with code

# Phase 2: Library & Framework Best Practices Validation

**Check if the issue requires external libraries or framework-specific features:**

1. **Identify Requirements:**
   - Does the issue need a new library? (e.g., charts, date handling, file processing)
   - Does it use existing libraries? (Django, DRF, Phoenix theme, etc.)
   - Are there framework-specific features involved? (authentication, forms, etc.)

2. **Check Existing Dependencies First:**
   - Review `pyproject.toml` for existing libraries that might solve this
   - Example: Need date parsing? Check if `python-dateutil` is already installed
   - Example: Need file validation? We have `magika` (don't add `python-magic`)

3. **Validate Latest Best Practices (if using external libraries):**
   - **For Django features:** Search official Django 4.2+ docs for latest patterns
   - **For DRF features:** Check Django REST Framework 3.16+ docs
   - **For Frontend (Phoenix theme):** Check Phoenix theme docs for components/utilities
   - **For Python libraries:** Search PyPI and official docs for latest stable version

4. **Web Search for Latest Patterns (when needed):**
   Use WebSearch for:
   - "Django 4.2 best practice for [feature]"
   - "Django REST Framework 3.16 [feature] example"
   - "Phoenix theme [component] documentation"
   - "[library-name] latest version 2025 best practice"

5. **Present Findings to User:**
   If you find:
   - **Better alternative to proposed approach** → Present both options with pros/cons
   - **Deprecated pattern in issue** → Suggest modern replacement
   - **New library needed** → Ask for approval with:
     * Library name and version
     * Why it's needed (what problem it solves)
     * Alternatives considered
     * Maintenance status (active, last update)
     * License compatibility

6. **Document Decisions:**
   Record in plan:
   - Libraries/versions used
   - Why chosen over alternatives
   - Any deprecated patterns avoided

**Examples:**

```
Issue mentions: "Add date picker using flatpickr"
→ Check: Does Phoenix theme have built-in date picker?
→ Search: "Phoenix theme date picker component"
→ If Phoenix has it: Recommend using built-in component
→ If not: Verify flatpickr is best choice for 2025

Issue mentions: "Add file upload validation"
→ Check pyproject.toml: We have 'magika' for content-based validation
→ Don't add python-magic (redundant)
→ Use existing core.validation.validate_file()

Issue mentions: "Implement JWT authentication"
→ Search: "Django 4.2 JWT authentication best practice 2025"
→ Check: Is djangorestframework-simplejwt still recommended?
→ Present: Options (simplejwt vs alternatives) with pros/cons
```

# Phase 3: Issue Discovery and Classification

**SCOPE: Only flag issues DIRECTLY related to the current issue's functionality**

While exploring code that you'll modify for this issue:
- Files you need to create/modify
- Dependencies/imports used by this functionality
- Similar patterns in the codebase

**Scan for:**
- TODO/FIXME comments without context
- Deprecated function usage (old logging patterns in related files)
- Hardcoded secrets or credentials
- Missing error handling in related code
- SQL injection vulnerabilities in queries you'll touch
- Performance anti-patterns (N+1 queries, missing indexes)
- Inconsistent logging (using `logging.getLogger` instead of `get_logger`)
- Missing validation (extension-based vs Magika content-based)
- Code duplication in files you're modifying
- Unused imports in files you'll touch
- Missing audit logging for sensitive operations

**Classify by severity:**
- **Critical**: SQL injection, hardcoded secrets, security vulnerabilities
- **High**: Deprecated security functions, missing auth checks, PII leakage
- **Medium**: Deprecated functions, N+1 queries, missing validation
- **Low**: TODO comments, code duplication, unused imports

**Present issues to user** with options:
- Fix now (stop current work, fix immediately)
- Document in PR (add to PR description)
- Create separate issue (file GitHub issue)
- Document in commit (note in commit message)
- Ignore (skip with reason)

# Phase 4: Planning and Approval ⭐

**CRITICAL: No code until user approves plan!**

## Pre-Planning Validation

**BEFORE writing the plan, verify you have:**

1. ✅ Extracted ALL guidance from issue (see "Comprehensive Issue Content Extraction" section)
2. ✅ Read relevant reference files (see "Reference Files Selection" section)
3. ✅ Identified any Claude prompts/examples provided in the issue
4. ✅ Listed all "Do NOT" constraints from the issue
5. ✅ Noted all edge cases mentioned in the issue

**If any of these are missing, GO BACK and complete them before planning!**

## Plan Template

Create detailed implementation plan that **explicitly references issue guidance**:

```markdown
# Implementation Plan for Issue #XXX

## Issue Guidance Summary ⚠️

### From Issue Description:
**Considerations mentioned:**
- [List each consideration from the issue]

**Know-Hows specified:**
- [List each know-how from the issue]

**Edge Cases to handle:**
- [List each edge case from the issue]

**Explicit Restrictions (Do NOT):**
- [List each restriction from the issue]

**Claude Prompts/Examples provided:**
- [Reference any code snippets or prompts from the issue]

### Reference Files Consulted:
- ✅ `[filename].md` - Applied: [what pattern/guideline was used]
- ✅ `[filename].md` - Applied: [what pattern/guideline was used]

---

## Summary
[Brief description of what we're building and why]

## How This Plan Addresses Issue Guidance

| Issue Requirement/Consideration | How Plan Addresses It |
|--------------------------------|----------------------|
| [Consideration 1 from issue] | [How implementation handles it] |
| [Know-how 1 from issue] | [How it's incorporated] |
| [Edge case 1 from issue] | [How it's tested/handled] |

## Components to Create/Modify

### 1. Model: `domain/app/models.py`
- **Purpose**: [What this model represents]
- **Key Fields**: [List important fields]
- **Business Rules**: [Any special logic]
- **Uses**: Django ORM, UUID primary keys, immutability if needed
- **Issue Alignment**: [How this follows issue guidance]

### 2. Service: `domain/app/services.py`
- **Purpose**: [Business logic this service handles]
- **Key Methods**: [List main methods]
- **Dependencies**: [What it uses - logging, validation, storage, etc.]
- **Pattern**: Module-level instance for easy import
- **Issue Alignment**: [How this follows issue guidance]

### 3. Tests: `domain/app/tests.py`
- **Coverage**: [What scenarios will be tested]
- **Test Types**: Unit tests for service layer, integration tests
- **Test Data**: [What test fixtures needed]
- **Edge Cases from Issue**: [Explicitly list edge cases from issue that will be tested]

## Existing Infrastructure Usage
- ✅ Logging: `core.diagnostics.logging.get_logger()`
- ✅ Validation: `core.validation.validate_file()` (if file handling)
- ✅ Storage: `core.storage` (if file storage)
- [ ] New dependency needed: [If any - requires approval]

## Issue-Specified Code/Prompts

If the issue included Claude prompts or example code, show how they're being used:

```python
# From issue - using as starting point:
[paste relevant code from issue]

# Modifications needed:
# - [Change 1]
# - [Change 2]
```

## Testing Strategy
- Unit tests for each service method
- Integration tests for full workflow
- **Edge cases from issue**:
  - [ ] [Edge case 1 from issue]
  - [ ] [Edge case 2 from issue]
- Performance considerations: [If relevant]

## Compliance with Issue Restrictions

**Verifying "Do NOT" compliance:**
- ❌ [Restriction 1]: Plan does NOT violate this because [reason]
- ❌ [Restriction 2]: Plan does NOT violate this because [reason]

## Potential Risks
- [List any concerns or unknowns]
- [Migration complexity if database changes]
- [Breaking changes to existing code]

## Documentation Updates Needed
- [List what docs to create/update after implementation]
```

**Present plan to user and wait for approval:**
- Highlight how plan addresses EACH consideration from issue
- Show how know-hows are incorporated
- Confirm edge cases will be tested
- Verify no "Do NOT" restrictions are violated
- Ask specific questions about any unclear guidance
- Get explicit "yes", "approved", "go ahead", "implement it"

# Phase 5: Implementation with Standards Enforcement

**Only start after plan approved!**

## Implementation Checkpoint: Issue Guidance Verification

**During implementation, continuously verify against issue guidance:**

### Before Each Component Implementation:
1. Re-read the relevant section of the issue
2. Check if any considerations apply to this component
3. Verify know-hows are being followed
4. Ensure edge cases will be handled

### Implementation Notes Format:
When implementing, document how you're following issue guidance:

```python
# Implementation Note: Following issue guidance
# - Consideration: "Use streaming for large files" → Using chunked_upload()
# - Know-how: "Follow pattern in extraction_service.py" → Applied same structure
# - Edge case: "Empty input returns []" → Handled in lines 45-48
```

## Required Standards

### 1. Environment
Always use: `DJANGO_ENVIRONMENT=local poetry run python manage.py <command>`

### 2. Service Layer (Required for Business Logic)
```python
from core.diagnostics.logging import get_logger

logger = get_logger('domain.app_name.service_name')

class ServiceName:
    """
    Service for [business capability].

    Business Logic:
    - [What this service does]

    Example:
        from domain.app_name.services import service_name
        result = service_name.method_name(param1, param2)
    """

    def method_name(self, param1, param2):
        """What this method does."""
        logger.info("Starting operation", param1=param1)
        # Implementation
        logger.audit('operation_completed', param1=param1, param2=param2)
        return result

# Module-level instance for easy import
service_name = ServiceName()
```

### 3. Logging (ALWAYS use centralized logger)
```python
from core.diagnostics.logging import get_logger

logger = get_logger('domain.app_name.module')

# Standard logging (PII automatically masked)
logger.info("Processing file", user_id=123, file_size=1024)

# Audit logging (for sensitive operations)
logger.audit('action_name', user_id=user.id, resource_id=resource.id)

# Performance monitoring
logger.performance('operation_name', duration=duration)

# Security events
logger.security_event('event_type', severity='high', details=info)
```

### 4. File Validation (ALWAYS use Magika)
```python
from core.validation import validate_file
from core.validation.exceptions import FileValidationError

try:
    validate_file(
        uploaded_file,
        allowed_types=['pdf', 'docx', 'txt'],
        max_size_mb=10
    )
except FileValidationError as e:
    logger.error("File validation failed", error=str(e))
    raise
```

### 5. Models (Django Best Practices)
```python
from django.db import models
import uuid

class ModelName(models.Model):
    """What this model represents."""

    # UUID primary key (better for distributed systems, SOC2)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Timestamps (always include)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'table_name'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at', 'user']),
        ]
```

**For Immutable Models:**
```python
def save(self, *args, **kwargs):
    """Prevent updates to existing records."""
    if not self._state.adding:
        raise ValidationError("Cannot update existing record")
    super().save(*args, **kwargs)

def delete(self, *args, **kwargs):
    """Prevent deletion."""
    raise ValidationError("Cannot delete records")
```

### 6. API Endpoints (if needed)
- Token authentication
- Rate limiting
- Pagination (limit/offset, 50 per page)
- Audit logging
- Generic user error messages (SOC2)
- Detailed internal logging

# Phase 6: Testing and Validation ⭐

## Comprehensive Tests (NOT superficial!)

```python
# ❌ BAD: Superficial test
def test_create(self):
    obj = service.create()
    self.assertIsNotNone(obj)  # Too weak!

# ✅ GOOD: Comprehensive test
def test_create_with_all_fields(self):
    """Test creation with all required fields."""
    obj = service.create(field1='value1', field2='value2')

    # Verify all fields
    self.assertEqual(obj.field1, 'value1')
    self.assertEqual(obj.field2, 'value2')
    self.assertIsNotNone(obj.created_at)

    # Verify in database
    self.assertTrue(Model.objects.filter(id=obj.id).exists())

    # Test error case
    with self.assertRaises(ValueError):
        service.create(field1=None)  # Should fail
```

## Run Tests
```bash
DJANGO_ENVIRONMENT=local poetry run python manage.py test domain.app_name
```

All tests must pass (0 failures, 0 errors)

# Phase 7: Final Validation Checklist

## Issue Guidance Compliance (CRITICAL!)

**Verify ALL issue guidance was followed:**

### Considerations Check:
- [ ] Each consideration from issue was addressed in implementation
- [ ] Document where each consideration is handled

### Know-Hows Check:
- [ ] Each know-how from issue was incorporated
- [ ] Patterns match those specified in issue

### Edge Cases Check:
- [ ] Each edge case from issue has a corresponding test
- [ ] Edge case handling verified manually

### Restrictions Check:
- [ ] No "Do NOT" restrictions were violated
- [ ] Breaking changes avoided (if specified)

### Claude Prompts/Examples Check:
- [ ] Any code provided in issue was used/adapted appropriately
- [ ] Deviations from provided examples are justified

---

## Technical Standards Compliance

- [ ] Uses `get_logger()` from `core.diagnostics.logging`
- [ ] Uses `validate_file()` from `core.validation` (if files)
- [ ] Relies on automatic PII masking
- [ ] Follows domain-driven structure
- [ ] Business logic in `services/`, not views/models
- [ ] Generic errors to users, detailed in logs (SOC2)
- [ ] Tests written and passing
- [ ] Migrations created (not applied to non-local without approval)
- [ ] Documentation updated
- [ ] No hardcoded secrets
- [ ] Only existing dependencies used (or user approved new ones)
- [ ] Tests are comprehensive (not superficial)
- [ ] Manual testing completed
- [ ] Database state verified
- [ ] Logs checked (no PII exposure)

## Reference File Compliance

- [ ] All patterns from consulted reference files were followed
- [ ] No anti-patterns from reference files present in code

# Phase 8: Issue Resolution Tracking

For each flagged issue from Phase 3:
- **Fix now**: Verify fix applied and tested
- **Document in PR**: Add to PR description
- **Create issue**: Create GitHub issue with severity label
- **Document in commit**: Include in commit message
- **Ignore**: Note reason internally

---

## Usage Examples

```
/django-issue 193
/django-issue Add audit logging foundation for SOC2 compliance
/django-issue Fix user authentication bug in login flow
```

When executing, follow all 8 phases in order.
Do NOT skip phases. Do NOT start Phase 5 (Implementation) until plan is explicitly approved in Phase 4.
