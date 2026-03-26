# GitHub Issue Creator Skill - Setup Instructions

## Overview

This skill helps Claude create well-structured GitHub issues for your Django development team, following BayOne's workflow and referencing your internal best practices documentation.

## File Structure

Create this structure in `/mnt/skills/user/github-issue-creator/`:

```
/mnt/skills/user/github-issue-creator/
├── SKILL.md                          # Main skill documentation (DONE)
├── README.md                         # This file
├── references/                       # YOU manually add your .md docs here
│   ├── azure_openai_best_practices.md
│   ├── azure_services_best_practices.md
│   ├── azure_storage_best_practices.md
│   ├── ai_ml_integration_best_practices.md
│   ├── audit_logging_best_practices.md
│   ├── authentication_authorization_best_practices.md
│   ├── cdn_sri_best_practices.md
│   ├── celery_best_practices.md
│   ├── channels_websockets_best_practices.md
│   ├── custom_middleware_best_practices.md
│   ├── django_best_practices.md
│   ├── django_rest_framework_best_practices.md
│   ├── django_templates_best_practices.md
│   ├── htmx_best_practices.md
│   ├── performance_monitoring_best_practices.md
│   ├── pii_detection_best_practices_review_guide.md
│   ├── postgresql_best_practices_v2.md
│   ├── redis_best_practices.md
│   ├── soc2_considerations.md
│   └── web_security_best_practices.md
├── templates/                        # Issue templates (DONE)
│   ├── bug_template.md
│   ├── feature_template.md
│   └── tech_debt_template.md
└── examples/                         # Example issues (DONE)
    ├── example_bug_issue.md
    └── example_feature_issue.md
```

## Setup Steps

### 1. Create Directory Structure

```bash
# Navigate to skills directory
cd /mnt/skills/user/

# Create the skill directory
mkdir -p github-issue-creator/references
mkdir -p github-issue-creator/templates
mkdir -p github-issue-creator/examples
```

### 2. Copy Files from Claude's Output

Copy these files from `/mnt/user-data/outputs/`:

```bash
# Main skill documentation
cp /mnt/user-data/outputs/SKILL.md github-issue-creator/

# Templates
cp /mnt/user-data/outputs/bug_template.md github-issue-creator/templates/
cp /mnt/user-data/outputs/feature_template.md github-issue-creator/templates/
cp /mnt/user-data/outputs/tech_debt_template.md github-issue-creator/templates/

# Examples
cp /mnt/user-data/outputs/example_bug_issue.md github-issue-creator/examples/
cp /mnt/user-data/outputs/example_feature_issue.md github-issue-creator/examples/

# This README
cp /mnt/user-data/outputs/README.md github-issue-creator/
```

### 3. Add Your Best Practices Documentation

**MANUAL STEP:** Copy your 20 best practices .md files into the `references/` directory.

These are the files already in your context that need to be manually placed:
- azure_openai_best_practices.md
- azure_services_best_practices.md
- azure_storage_best_practices.md
- ai_ml_integration_best_practices.md
- audit_logging_best_practices.md
- authentication_authorization_best_practices.md
- cdn_sri_best_practices.md
- celery_best_practices.md
- channels_websockets_best_practices.md
- custom_middleware_best_practices.md
- django_best_practices.md
- django_rest_framework_best_practices.md
- django_templates_best_practices.md
- htmx_best_practices.md (you'll need to create/add this)
- performance_monitoring_best_practices.md
- pii_detection_best_practices_review_guide.md
- postgresql_best_practices_v2.md
- redis_best_practices.md
- soc2_considerations.md
- web_security_best_practices.md

## How to Use the Skill

### Basic Usage

When you need to create an issue, tell Claude:

```
Use the github-issue-creator skill to create a [bug/feature/tech-debt] issue for [description].
```

Claude will:
1. Narrate its progress through each step
2. Read the appropriate template
3. Identify relevant best practices docs from `/references/`
4. Author the issue following your team's patterns
5. Include all required sections
6. Provide the markdown ready to paste into GitHub

For complex issues, Claude can optionally use a multi-agent approach with separate Analyzer, Author, and Reviewer agents.

### Example Prompts

**For a bug:**
```
Use the github-issue-creator skill to create a bug issue. External users can access internal admin pages due to missing permission checks on the ReportViewSet.
```

**For a feature:**
```
Use the github-issue-creator skill to create a feature issue. We need to implement candidate search with filters for skills, experience, and location. This should use Django FBV initially and connect to existing templates.
```

**For tech debt:**
```
Use the github-issue-creator skill to create a tech debt issue. Our authentication views use inconsistent patterns - some are FBV, some are CBV, and we're mixing django-allauth views with custom views. We need to standardize.
```

### Advanced Usage

**With specific best practices focus:**
```
Create a feature issue for WebSocket-based live notifications. Make sure to reference channels_websockets_best_practices.md and redis_best_practices.md for the channel layer setup.
```

**For security issues:**
```
Create a HIGH PRIORITY bug issue. We're not masking PII in Celery task logs. Reference pii_detection_best_practices and soc2_considerations docs.
```

**Breaking down large features:**
```
I need to create a series of issues for implementing candidate AI matching. Break this into 3-4 issues with clear dependencies. Start with foundation/infrastructure, then core features, then UI integration.
```

### Review Mode

You can also use the skill to review existing issue drafts:

```
Review this issue draft using the github-issue-creator skill. Check that it follows our standards, references appropriate docs, and has testable acceptance criteria.

[paste your draft]
```

## What the Skill Provides

### Issue Quality Standards

Every issue will include:
- **Clear title** (action-oriented, 50-70 chars)
- **Dependencies** explicitly stated
- **Description** with what/why/impact
- **Technical Approach** with architecture and patterns
- **Tasks** with file paths and pseudocode (2-5 tasks)
- **Testing** with manual steps and edge cases
- **Acceptance Criteria** as checkboxes
- **Notes** with Django patterns, Claude Code tips, and pitfalls

### Workflow Integration

Issues are designed for developers who:
- Use `gh issue view` to retrieve issue details
- Work with Claude Code for implementation
- Create feature branches: `feature/issue-{number}-brief-description`
- Open Draft PRs after first commits
- Make daily commits
- Ask Colin to review model changes (don't run migrations on main)
- Follow the 4-hour rule for getting unstuck

### Compliance Built-In

Issues automatically include:
- SOC2 considerations when relevant
- PII masking requirements
- Audit logging specifications
- Access control requirements
- References to compliance documentation

## Customization

### Adding New Templates

If you need additional template types (e.g., documentation, infrastructure):

1. Create the template in `/templates/`
2. Follow the same structure as existing templates
3. Update `SKILL.md` to reference the new template

### Adding Best Practices Docs

When you create new best practices documentation:

1. Add it to `/references/`
2. Update the domain mapping in `SKILL.md` Step 2
3. Reference it in relevant template examples

### Updating Workflow

If your Git workflow changes:

1. Update the "Workflow Integration" section in `SKILL.md`
2. Update any workflow-specific guidance in templates
3. Update examples to reflect new patterns

## Maintenance

### Keeping Examples Current

As your codebase evolves:
- Update file paths in examples if structure changes
- Refresh example URLs/endpoints if they change
- Add new examples for common issue patterns

### Reviewing Issue Quality

Periodically check created issues against:
- Are developers able to complete them?
- Are acceptance criteria actually testable?
- Are best practices references still accurate?
- Do testing steps work with current infrastructure?

### Team Feedback

Gather feedback from developers:
- What issues were clear vs confusing?
- What additional guidance would help?
- What common patterns should be templated?

## Troubleshooting

### "Claude doesn't reference my best practices docs"

**Fix:** Make sure the files are in `/references/` and Claude can access them. Use `file_read` to verify:

```
Read the contents of /mnt/skills/user/github-issue-creator/references/django_best_practices.md
```

### "Issues are too vague"

**Fix:** Be more specific in your prompt about what you're building:
- Include technical details you know
- Mention specific files or components
- Reference related features or issues

### "Issues are too detailed"

**Fix:** The skill should trust Claude Code to implement. If issues have large code blocks:
- Review and adjust templates
- Remind Claude to show patterns, not solutions
- Use "Think about:" questions instead of prescriptive code

### "Testing steps don't work"

**Fix:** Templates assume certain infrastructure exists. Update examples to:
- Use actual URLs from your app
- Reference actual models and fields
- Use admin sections that exist
- Avoid theoretical testing steps

## Benefits

Using this skill ensures:

✅ **Consistency** - All issues follow the same structure  
✅ **Completeness** - No missing sections or unclear acceptance criteria  
✅ **Workflow Integration** - Issues work with your Git workflow and Claude Code  
✅ **Best Practices** - Automatic referencing of your documentation  
✅ **Compliance** - SOC2 and security considerations built-in  
✅ **Developer-Friendly** - Written for advanced Django devs using Claude Code  
✅ **Testable** - Acceptance criteria are concrete and verifiable  

## Next Steps

After setup:

1. ✅ Copy all files to the skill directory
2. ✅ Add your best practices docs to `/references/`
3. ✅ Test with a simple issue creation request
4. ✅ Review the output and adjust templates if needed
5. ✅ Share with your team and gather feedback
6. ✅ Iterate on templates based on real usage

## Support

If you need to modify the skill:
- Update `SKILL.md` for workflow or documentation changes
- Update templates for structure or section changes
- Add new examples for common patterns
- Keep examples consistent with actual codebase

---

**Version:** 1.0  
**Created:** 2025-11  
**Author:** Colin (BayOne Solutions)
