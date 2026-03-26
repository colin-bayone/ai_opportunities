---
name: pr-review-workflow
description: Comprehensive GitHub PR review workflow for Django projects with systematic staleness checking, scope analysis, and quality assessment. This skill should be used when users want to review a PR, approve a pull request, check PR code quality, or conduct code review. Triggers include requests like "review PR #123", "help me review this pull request", "approve PR", "check this PR", "do a code review on PR", or "review and approve". Use for (1) Analyzing PR metadata and context, (2) Checking for branch staleness and duplicate files, (3) Identifying scope creep, (4) Reviewing Django code quality, (5) Running tests and migrations, (6) Generating structured review feedback.
---

# PR Review Workflow

A systematic approach to reviewing GitHub pull requests using subagents for different phases. This workflow ensures thorough reviews that catch staleness issues, scope creep, and dependency violations.

---

## ⚠️ COMPLIANCE ENFORCEMENT SYSTEM

**This skill uses deterministic enforcement via hooks.**

A verification hook blocks PR approval if required steps are not completed. This is NOT optional prompting - it is enforced by external code that cannot be bypassed.

### How It Works

1. **You MUST log completion of each step** using the compliance script
2. **The hook checks the log** when you try to approve a PR
3. **If steps are missing, approval is BLOCKED** with exit code 2
4. **You cannot approve until all steps are verified**

### Logging Compliance

After completing each major step, run:

```bash
./scripts/log_compliance.sh <PR_NUMBER> <STEP_MARKER>
```

**Required markers for each phase:**

| Phase | Step | Marker |
|-------|------|--------|
| Phase 1 | Gather PR info | `PHASE1_GATHER_PR_INFO` |
| Phase 1 | Read linked issue | `PHASE1_READ_LINKED_ISSUE` |
| Phase 1 | Prepare local env | `PHASE1_PREPARE_LOCAL_ENV` |
| Phase 1 | Check staleness | `PHASE1_CHECK_STALENESS` |
| Phase 1 | Classify files | `PHASE1_CLASSIFY_FILES` |
| Phase 1 | Scope check | `PHASE1_SCOPE_CHECK` |
| Phase 1 | Complete | `PHASE1_COMPLETE` |
| Phase 2 | Create worktree | `PHASE2_CREATE_WORKTREE` |
| Phase 2 | Check dependencies | `PHASE2_CHECK_DEPENDENCIES` |
| Phase 2 | Load best practices | `PHASE2_LOAD_BEST_PRACTICES` |
| Phase 2 | Review core files | `PHASE2_REVIEW_CORE_FILES` |
| Phase 2 | Run tests | `PHASE2_RUN_TESTS` |
| Phase 2 | Identify issues | `PHASE2_IDENTIFY_ISSUES` |
| Phase 2 | Complete | `PHASE2_COMPLETE` |
| Phase 3 | Determine decision | `PHASE3_DETERMINE_DECISION` |
| Phase 3 | Complete | `PHASE3_COMPLETE` |

### Viewing Progress

Check current compliance status:
```bash
cat /tmp/pr_<PR_NUMBER>_skill_compliance.log
```

### Reset for New Review

If restarting a review:
```bash
rm /tmp/pr_<PR_NUMBER>_skill_compliance.log
```

---

## Core Philosophy

1. **Check staleness FIRST** - Avoid reviewing files already merged to main
2. **Understand context** - Read full issue and dependencies before code
3. **Use subagents** - Delegate phases to specialized agents for focused work
4. **Be systematic** - Follow the workflow phases in order
5. **Document findings** - Provide clear, actionable feedback
6. **Communicate constantly** - Narrate your work and discuss findings before taking action

## Communication Principles

**CRITICAL: Always communicate with the user throughout the review process.**

### Before Running Commands
- **Narrate what you're about to do and why** before executing commands
- Explain the purpose of each phase as you enter it
- Tell the user what you're checking for and what you expect to find

### During the Review
- **Keep the user informed** of your progress through each phase
- Highlight interesting or unexpected findings as you discover them
- Explain what you're looking at and why it matters

### Before Taking Action
- **NEVER draft a review or approval message without discussing findings first**
- Always present your complete findings to the user verbosely
- Ask for the user's feedback and decision before proceeding
- Give the user options rather than making decisions for them

### Decision Points
When you reach a decision point:
1. **Summarize all findings** clearly and completely
2. **Present options** to the user (e.g., "Should I request rebase?" or "Would you like me to fix these issues?")
3. **Wait for explicit direction** before drafting any GitHub content
4. **Never assume** what the user wants - always ask

### Example Communication Flow

**Good:**
```
"I'm starting the Pre-Review Analysis phase. First, I'll gather PR metadata to understand the scope and size of the changes..."

[runs gather_pr_info.sh]

"I found that this PR has 233 additions across 4 files. Let me check the linked issue to understand the requirements..."

[reviews issue]

"The issue asks for email configuration changes. Now I'll check if the branch is stale..."

[runs staleness check]

"Found something important: the branch is 10 commits behind main and is missing 3 dependencies (flower, sqlalchemy, pytz) that were added to main. This is critical because merging without rebasing will DELETE these dependencies.

Here's what I found overall:
[detailed findings]

What would you like me to do? Should I:
1. Request the developer rebase before approval
2. Offer to do the rebase myself
3. Something else?"
```

**Bad:**
```
[silently runs all commands]
[generates review and submits it without discussion]
```

## Workflow Overview

The review process consists of 4 phases, each handled by a specialized subagent:

1. **Pre-Review Analysis** - Gather context, check staleness, identify scope issues
2. **Code Review** - Review actual code quality and Django best practices
3. **Decision & Communication** - Determine conflicts and generate review
4. **Post-Approval** - Handle merge process and dependent PRs

## Prerequisites

### GitHub CLI (gh) Version Requirements

**CRITICAL**: This workflow requires GitHub CLI (`gh`) version **2.82.1 or later** to avoid API deprecation errors when editing PRs.

#### Checking Your Version

```bash
gh --version
```

If you see a version older than 2.82.1 (e.g., `gh version 2.4.0`), you must upgrade before proceeding.

#### Upgrading GitHub CLI on Ubuntu/WSL

**Official Method** (requires sudo - user must run these commands):

```bash
# Add GitHub CLI repository
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Update and install latest gh
sudo apt update
sudo apt install gh -y

# Verify upgrade
gh --version
```

**Expected output after upgrade**: `gh version 2.83.1` or later

#### When gh Commands Fail

If you encounter errors like:
```
GraphQL: Projects (classic) is being deprecated...
```

This indicates an outdated gh version. **DO NOT** try to work around this error. Instead:

1. Check the current gh version: `gh --version`
2. Search online for the latest gh version available
3. If your version is outdated, inform the user they need to upgrade
4. Provide the exact upgrade commands above
5. **Wait for user to run sudo commands** - you cannot run sudo commands yourself
6. Work interactively with the user to complete the upgrade
7. Verify the upgrade succeeded before retrying the original command

**NEVER**:
- Attempt to bypass sudo requirements
- Try to install gh manually to ~/.local/bin (use official method instead)
- Continue with workflow if gh commands are failing due to version issues

## Phase 1: Pre-Review Analysis Agent

**Goal**: Gather all context and identify issues BEFORE touching code.

### Subagent Instructions

You are the Pre-Review Analysis Agent. Your job is to gather comprehensive context and identify potential issues before code review begins.

**Execute these steps in order:**

#### Step 1: Gather PR Information

```bash
# Use the provided script
(All scripts are in their respective skill folder in .claude/skills/)
./scripts/gather_pr_info.sh <PR_NUMBER>

# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_GATHER_PR_INFO
```

**Extract and document**:
- PR size (additions/deletions)
- Number of files changed
- Author and creation date
- PR description and linked issue number
- Base branch (usually `main`)
- Head branch (feature branch)
- Number of commits
- Last updated timestamp

#### Step 2: Review Related Issue(s)

**Fetch the linked issue**:
```bash
gh issue view <ISSUE_NUMBER> --json title,body,labels
```

**Read and understand**:
- Complete requirements and acceptance criteria
- What is explicitly in scope
- What is explicitly out of scope ("Future enhancements", "Next issues")
- Business context and goals

**Check for dependencies**:
If issue mentions dependent issues, fetch those too:
```bash
gh issue view <DEPENDENCY_ISSUE_NUMBER> --json title,body,labels
```

```bash
# Log compliance after reading and understanding the issue
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_READ_LINKED_ISSUE
```

#### Step 3: Prepare Local Environment (CRITICAL)

**Before checking staleness, ensure local main is up to date**:

```bash
# Use the provided script
./scripts/prepare_local_env.sh

# This script:
# - Checkouts main branch
# - Checks for staged/uncommitted changes (stops if found)
# - Pulls latest from origin/main (stops on conflicts)
# - Reports current commit status
```

**STOP and ask the user to resolve if**:
- Staged commits exist in local
- Uncommitted changes exist
- Merge conflicts occur during pull

Only proceed after local main is clean and up to date.

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_PREPARE_LOCAL_ENV
```

#### Step 4: Check Branch Staleness (CRITICAL)

**Problem**: PR may show files as "changed" when already in base branch due to lack of rebase.

```bash
# Use the provided script
./scripts/check_staleness.sh <PR_NUMBER>

# This script:
# - Fetches latest main
# - Checks if PR branch is behind main (commits behind count)
# - Classifies each file as DUPLICATE, MODIFIED, or NEW
# - Saves classification to /tmp/pr_<PR_NUMBER>_file_status.txt
# - Checks for suspicious deletions
```

**Interpret results**:
- If `commits behind > 0`: Branch is STALE
- Focus only on NEW and MODIFIED files for review
- DUPLICATE files are already in main (skip review)
- Verify any deletions are intentional

**Understanding Staleness (IMPORTANT - Read Carefully)**:

Staleness means the PR branch is behind main, but this is NOT automatically critical. Here's how to interpret it:

**What staleness affects:**
- Only files that the PR is ACTUALLY CHANGING matter
- If the PR touches 4 files and none are DUPLICATE, staleness is usually fine
- The staleness check already filters to show you only PR-touched files

**What NOT to do:**
- ❌ Don't manually check files outside the PR's scope (like `git diff origin/main pyproject.toml` if pyproject.toml isn't in the PR)
- ❌ Don't panic about "missing changes" in files the PR doesn't touch
- ❌ Don't treat "X commits behind" as critical by itself

**When staleness IS critical:**
- PR touches the same files that changed in main (HIGH conflict risk)
- 80%+ files are duplicates (dependency violation - PR built on wrong base)
- PR modifies dependency files (pyproject.toml, package.json) that changed in main

**When staleness is NOT critical:**
- PR touches only a few specific files (e.g., 4 files)
- No DUPLICATE files detected (means PR changes are genuine, not already merged)
- Files the PR touches haven't changed in main since branch creation
- Dependencies/configs the PR doesn't touch may differ, but that's fine - rebase will bring them in automatically

**Example - Good scenario:**
```
PR touches: 4 files (3 MODIFIED, 1 NEW)
Branch status: 10 commits behind
Assessment: Fine! The 4 files are the actual changes. Rebase will cleanly bring in the 10 commits.
```

**Example - Bad scenario:**
```
PR touches: 15 files (12 DUPLICATE, 3 NEW)
Branch status: 5 commits behind
Assessment: Critical! 80% duplicates = likely built on wrong base or dependency violation.
```

**Red flags (real concerns)**:
- 80%+ files are duplicates - high probability of dependency violation
- Large deletions (500+ lines) that may not be intentional
- Branch last updated before recent main merges AND modifies same files

```bash
# Log compliance after staleness analysis
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_CHECK_STALENESS
```

#### Step 5: Classify Files (NEW/MODIFIED only)

```bash
# Use the provided script
./scripts/classify_files.sh <PR_NUMBER>

# This script:
# - Uses staleness data if available
# - Classifies files into: docs, infrastructure, tests, migrations, core code
# - Saves categorized lists to /tmp/pr_<PR_NUMBER>_*.txt
# - Provides count summary
```

**Calculate actual review scope**:
```
Real additions = Total additions - Duplicate lines
Core code size = Real additions - (docs + infra + tests + migrations)
```

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_CLASSIFY_FILES
```

#### Step 6: Check for Scope Creep

**Compare NEW/MODIFIED files against issue requirements**.

Load the scope creep guide for reference:
```bash
view references/scope_creep_guide.md
```

**Identify scope additions**:
- **Always acceptable** (do not flag): Extra docs, tests, minor cleanup
- **Question the user about**: Features marked for future, unmentioned functionality, unrelated fixes, breaking changes, major architectural changes, security changes

**Red flags**:
- Issue asks for 800 lines, PR delivers 2,400 lines
- Issue says "Next issue will add X" but PR implements X
- PR modifies files from different features
- MODIFIED files from other merged PRs (UI changes from another PR)

**IMPORTANT**: When scope additions are detected beyond docs/tests:
1. Document what is out of scope
2. Ask the user: "I found scope additions beyond the issue requirements. Should we:
   - Accept them (they look good and save time)
   - Request the developer remove them
   - Request the developer split them into separate PRs
   
   What would you like to do?"
3. Do NOT proceed with a recommendation until user responds

**Note**: Extra documentation and tests are ALWAYS acceptable scope creep. Only flag other additions.

**IMPORTANT - .django-workflow/ Files:**
Files in `.django-workflow/` directories are internal implementation notes generated by Claude sub-agents. These files:
- Should NOT be reviewed for code quality
- Should NOT be counted in scope analysis
- Should NOT be considered scope creep
- Are totally fine to leave as-is in PRs

When calculating PR size and scope, exclude `.django-workflow/` files from your counts and analysis. Focus only on actual code, tests, and migrations.

```bash
# Log compliance after scope analysis
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_SCOPE_CHECK
```

#### Step 7: Check for Dependency Violations

**Pattern to detect**:
- Multiple PRs from same developer open simultaneously
- PRs modifying identical files
- PR B includes commits from unmerged PR A
- High percentage of DUPLICATE files (dependency violation indicator)

**Verify**:
```bash
# Check if other open PRs exist from same author
gh pr list --author <AUTHOR>

# Compare file overlap if suspicious
gh pr view <PR_A> --json files --jq '.files[].path'
gh pr view <PR_B> --json files --jq '.files[].path'
```

#### Output from Pre-Review Agent

Produce a structured summary:

```markdown
# Pre-Review Analysis Summary

## PR Overview
- **PR Number**: #XXX
- **Title**: [title]
- **Author**: [author]
- **Issue**: #XXX
- **Total Additions/Deletions**: X,XXX / XXX
- **Files Changed**: XX

## Branch Status
- **Status**: [UP TO DATE | STALE - X commits behind]
- **Files Classification**:
  - DUPLICATE (already in main): XX files
  - MODIFIED (changed from main): XX files
  - NEW (not in main): XX files

## File Classification (NEW/MODIFIED only)
- Documentation: XX files
- Infrastructure: XX files
- Tests: XX files
- Migrations: XX files
- Core Code: XX files (~X,XXX lines)

## Issue Requirements Summary
[Brief summary of what issue requires]
- In scope: [list]
- Out of scope: [list marked as future]

## Scope Analysis
[Status: ACCEPTABLE | NEEDS USER DECISION]

- Acceptable additions: [docs/tests - list if any]
- Questionable additions: [list if any - WAIT for user decision]
- Problematic additions: [list if any - WAIT for user decision]

## Dependency Check
[No violations found | Potential violation detected]
[Details if violation detected]

## Recommendation
[PROCEED TO CODE REVIEW | NEEDS REBASE | NEEDS USER DECISION ON SCOPE]
[Specific actions needed before code review, if any]
```

**Hand off to Code Review Agent only if**: Recommendation is "PROCEED TO CODE REVIEW"

```bash
# Log Phase 1 completion
./scripts/log_compliance.sh <PR_NUMBER> PHASE1_COMPLETE
```

---

## Phase 2: Code Review Agent

**Goal**: Review the actual code for quality, correctness, and Django best practices.

### Subagent Instructions

You are the Code Review Agent. Your job is to perform detailed code review of NEW and MODIFIED files identified in Pre-Review Analysis.

**Prerequisites**: Pre-Review Analysis must be complete with "PROCEED TO CODE REVIEW" recommendation.

#### Step 1: Set Up Isolated Review Environment (Automatic Worktree)

**This step automatically creates an isolated worktree for the PR review.**

The worktree approach is used transparently - the user doesn't need to do anything. Benefits:
- User's current work in the main repo is completely untouched
- No stashing or committing required
- Clean environment for accurate test results
- Automatic cleanup after review

**Step 1a: Record original directory and create worktree**

```bash
# Record where we started (for returning later)
ORIGINAL_DIR=$(pwd)

# Create worktree for this PR review
.claude/skills/git-worktrees-skill/scripts/create_worktree.sh pr-<PR_NUMBER> --pr <PR_NUMBER>
```

Inform the user:
```
"I'm setting up an isolated environment for this PR review.

Creating worktree at ../talent_ai-pr-<PR_NUMBER>/ - this keeps your current work untouched.
I'll do the entire review there, then return here when done."
```

**Step 1b: Change to worktree directory**

```bash
cd ../talent_ai-pr-<PR_NUMBER>
```

Confirm to user:
```
"Now working in the PR review worktree. Your main repo is unchanged."
```

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_CREATE_WORKTREE
```

**IMPORTANT - Returning After Review:**

At the END of the review (after Phase 3 or 4), always return to the original directory:

```bash
cd $ORIGINAL_DIR
```

And inform the user:
```
"Review complete. Returned to your original working directory.

The worktree at ../talent_ai-pr-<PR_NUMBER>/ still exists.
Would you like me to clean it up? (This only removes the directory, not the branch.)"
```

**Only remove the worktree if user explicitly confirms.**

#### Step 2: Resolve Dependencies (CRITICAL)

**NEVER skip this step. Always install dependencies before running tests.**

Check if PR adds new dependencies:
```bash
# Check for changes to Poetry files
git diff origin/main --name-only | grep -E "(pyproject.toml|poetry.lock)"
```

If dependencies changed, install them:
```bash
poetry install --no-root
```

**Communication Rule**:
- ALWAYS narrate what you're doing: "Installing new dependencies because the PR adds django-health-check to pyproject.toml"
- Explain why: "This is required to run tests that use the new package"
- Show progress and results

**Document**:
- What dependencies were added
- Whether installation succeeded
- Any warnings or version conflicts

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_CHECK_DEPENDENCIES
```

#### Step 3: Review Django Best Practices

Load the Django best practices checklist:
```bash
view references/django_best_practices.md

# Log compliance - YOU MUST ACTUALLY READ THE BEST PRACTICES FILE
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_LOAD_BEST_PRACTICES
```

**Review files by category** (focus on NEW/MODIFIED only):

**Core Code Review**:
```bash
# Get list of core code files
cat /tmp/pr_<PR_NUMBER>_core.txt

# Review each file
view <filepath>
```

**Check**:
- Models: Field definitions, relationships, methods, Meta options
- Views: Query optimization, permission checks, HTTP method handling
- Forms: Validation, ModelForm usage, error handling
- URLs: Reverse references, namespacing, converters
- Templates: Inheritance, static files, CSRF tokens, no business logic
- Security: Input escaping, SQL injection prevention, authentication
- Performance: N+1 queries, select_related/prefetch_related usage
- Code organization: DRY principle, single responsibility

**Infrastructure Review**:
```bash
cat /tmp/pr_<PR_NUMBER>_infra.txt
```
- Check settings changes for security implications
- Review requirements.txt for version pinning
- Verify __init__.py changes don't break imports

**Test Review**:
```bash
cat /tmp/pr_<PR_NUMBER>_tests.txt
```
- Verify tests exist for new functionality
- Check test quality and coverage
- Ensure tests are independent

**Migration Review**:
```bash
cat /tmp/pr_<PR_NUMBER>_migrations.txt
```
- Verify migrations are safe
- Check for data migrations correctness
- Ensure reversibility

**UI/Template Review (Phoenix Theme Compliance)**:

If the PR contains ANY UI changes (template files, CSS, JavaScript, or frontend components), invoke the `phoenix-pattern-validator` sub-agent to check Phoenix theme compliance:

```bash
# Identify UI files in the PR
cat /tmp/pr_<PR_NUMBER>_core.txt | grep -E "(templates/.*\.html|static/.*\.(css|js))"
```

If UI files are found, use the Task tool to launch the `phoenix-pattern-validator` agent with the template paths for validation. The phoenix theme skill and its sub-agents have comprehensive knowledge of Phoenix v1.23.0 patterns, Font Awesome 5 requirements, accessibility standards, and Django/HTMX conventions.

```bash
# Log compliance - only after ACTUALLY reviewing each file against best practices
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_REVIEW_CORE_FILES
```

#### Step 4: Run Migrations

```bash
# Run migrations in development environment
DJANGO_ENVIRONMENT=local python manage.py migrate

# Check for warnings or errors
```

#### Step 5: Run Tests (CRITICAL - NEVER SKIP)

**NEVER suggest skipping test execution. This is NON-NEGOTIABLE.**

```bash
# Run full test suite with proper environment
DJANGO_ENVIRONMENT=local python manage.py test

# Or run specific app tests
DJANGO_ENVIRONMENT=local python manage.py test <app_name>

# Check coverage if available
DJANGO_ENVIRONMENT=local coverage run --source='.' manage.py test
DJANGO_ENVIRONMENT=local coverage report
```

**If tests fail due to missing dependencies or environment issues**:
- Install missing dependencies immediately
- Fix environment configuration
- Re-run tests until they execute (pass or fail)
- NEVER skip to next step until tests actually run

**Document**:
- All tests passing or failing
- New tests added or missing
- Test coverage percentage
- Any failures or warnings
- If tests cannot run, document the specific blocker and work to resolve it

```bash
# Log compliance - tests MUST be run, not skipped
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_RUN_TESTS
```

#### Step 6: Manual Testing (if needed)

For UI changes or complex features:
```bash
# Start development server
python manage.py runserver

# Test key workflows manually
```

**Document** what was tested manually and results.

#### Step 7: Identify Issues

**Categorize findings**:

**Critical (blocks merge)**:
- Security vulnerabilities
- Breaking changes
- Major bugs
- Test failures
- Migration issues

**Non-Critical (nice to have)**:
- Code style improvements
- Performance optimizations
- Additional test coverage
- Documentation improvements

**Minor/Pedantic**:
- Simple few-line changes
- Trivial formatting issues
- Very minor improvements

#### Step 8: Determine Issue Handling Approach

**For Critical Issues**: Always request changes.

**For Minor/Pedantic Issues or Simple Test Failures**:
Ask the user: "I found [number] minor/pedantic issues:
- [list issues with file:line references]

Would you like me to:
1. Try to fix these issues directly (I can make the changes and push to the branch)
2. Request changes from the developer
3. Approve with notes (issues are too minor to block)

What would you like to do?"

Wait for user response before proceeding.

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_IDENTIFY_ISSUES
```

#### Output from Code Review Agent

Produce detailed review findings:

```markdown
# Code Review Findings

## Files Reviewed
- Models: [list files]
- Views: [list files]
- Forms: [list files]
- Tests: [list files]
- Migrations: [list files]

## Django Best Practices Assessment

### Followed
- [Specific practices verified with file/line references]

### Issues Found
[For each issue: severity, file, lines, description, recommendation]

## Testing Results
- **Migration Status**: [success/failure with details]
- **Test Results**: [passing/failing with details]
- **Coverage**: XX%
- **Manual Testing**: [if performed, list what was tested]

## Critical Issues (MUST FIX)
[List with file/line references and explanation]

## Non-Critical Suggestions
[List improvements that would be nice to have]

## Minor/Pedantic Issues
[List simple issues - WAIT for user decision on handling]

## Recommendation
[APPROVE | REQUEST CHANGES | NEEDS USER DECISION ON MINOR ISSUES]
```

**Hand off to Decision Agent** with review findings.

```bash
# Log Phase 2 completion
./scripts/log_compliance.sh <PR_NUMBER> PHASE2_COMPLETE
```

---

## Phase 3: Decision & Communication Agent

**Goal**: Determine final decision and generate review feedback.

### Subagent Instructions

You are the Decision & Communication Agent. Your job is to synthesize findings and generate the final review.

**Prerequisites**: Both Pre-Review Analysis and Code Review must be complete.

#### Step 1: Check for Conflicts

```bash
# Check if PR conflicts with main
git fetch origin main
git merge-base HEAD origin/main
git diff HEAD origin/main --name-only
```

**If conflicts exist**:
- Document what needs to change
- Ask developer if they want help with rebase
- Explain what will happen during rebase
- **Never rebase without explicit permission**

#### Step 2: Determine Final Decision

**Consider**:
- Pre-review findings (scope, staleness, dependencies)
- Code review findings (quality, bugs, best practices)
- Test results
- Conflicts with main

**Decision logic**:

```
IF critical issues exist:
    → REQUEST CHANGES
ELSE IF scope creep needs user decision:
    → Already handled in Pre-Review
ELSE IF minor issues need user decision:
    → Already handled in Code Review
ELSE IF all checks pass:
    → APPROVE
ELSE IF minor issues only and user chose "approve with notes":
    → APPROVE with notes
```

```bash
# Log compliance
./scripts/log_compliance.sh <PR_NUMBER> PHASE3_DETERMINE_DECISION
```

#### Step 3: Generate Review

Use the review template generator:
```bash
# For approval
./scripts/generate_review_template.sh <PR_NUMBER> approval

# For changes
./scripts/generate_review_template.sh <PR_NUMBER> changes

# Edit the generated file at /tmp/pr_<PR_NUMBER>_review_*.md
```

**Fill in the template** with:
- All findings from pre-review and code review
- Specific file/line references
- Clear explanation of issues
- Actionable recommendations

**CRITICAL - GitHub Content Attribution Rules**:

**NEVER include AI attribution in public-facing GitHub content**:
- ❌ PR descriptions (body text)
- ❌ PR titles
- ❌ Commit messages
- ❌ Review comments
- ❌ Issue comments
- ❌ Any content visible on GitHub

**Specifically forbidden**:
- "Generated with Claude Code" or similar phrases
- "Co-Authored-By: Claude <noreply@anthropic.com>"
- "🤖" emojis or "Generated with..." footers

**Why**: These are professional code reviews and commits that represent the team's work, not AI demonstrations.

**Write as a human reviewer**:
- Use first person: "I reviewed...", "I found...", "I tested..."
- Focus on technical findings, not the review process
- Be professional and direct

**Note**: Internal documentation (workflow files, skill references, planning docs) can mention AI tools - this rule applies ONLY to public GitHub content.

**For scope creep**, load the guide:
```bash
view references/scope_creep_guide.md
```

Use the communication patterns from the guide.

#### Step 4: Submit Review

```bash
# Log Phase 3 completion BEFORE submitting review
# This is required - the hook will block approval if not logged
./scripts/log_compliance.sh <PR_NUMBER> PHASE3_COMPLETE
```

```bash
# For approval
gh pr review <PR_NUMBER> --approve --body-file /tmp/pr_<PR_NUMBER>_review_approval.md

# For changes
gh pr review <PR_NUMBER> --request-changes --body-file /tmp/pr_<PR_NUMBER>_review_changes.md

# For comments only (no approval/changes)
gh pr review <PR_NUMBER> --comment --body-file /tmp/pr_<PR_NUMBER>_review_approval.md
```

#### Output from Decision Agent

```markdown
# Review Submitted

**Decision**: [APPROVED | CHANGES REQUESTED | COMMENTED]
**PR Number**: #XXX

## Summary of Review
[Brief summary of what was communicated]

## Next Steps for Developer
[Clear list of what developer should do]

## Handoff to Post-Approval Agent
[If approved, pass control for post-approval steps]
```

---

## Phase 4: Post-Approval Agent

**Goal**: Handle post-approval tasks and dependent PRs.

### Subagent Instructions

You are the Post-Approval Agent. Your job is to handle tasks after PR approval.

**Prerequisites**: PR must be APPROVED.

#### Step 1: Notify Developer

```markdown
PR #XXX has been approved and is ready to merge!

[If any notes or dependencies, mention them]

You can merge when ready using the GitHub interface.
```

#### Step 2: Document if Needed

If review revealed patterns or issues that should be documented:
- Create or update team documentation
- Share learnings with team
- Note for future reviews

#### Step 3: Monitor for Dependent PRs

If there are dependent PRs that need rebasing:

1. Wait for this PR to merge to main
2. Check if dependent PR still needs review
3. **Ask developer** if they want help rebasing
4. If yes, explain what will happen:
   - "PR B currently has X additions"
   - "After rebase, duplicate commits will be dropped"
   - "PR B should shrink to ~Y additions"
   - "I'll need to force-push the rebased branch"
5. Get explicit confirmation
6. Perform rebase if authorized
7. Initiate review of rebased PR

#### Output from Post-Approval Agent

```markdown
# Post-Approval Complete

**Actions Taken**:
- Developer notified of approval
- [✓ | N/A] Documentation updated
- [✓ | N/A] Dependent PRs identified and noted

**Dependent PRs** (if any):
- PR #XXX - [status and next steps]

**Review Complete**
```

#### Final Step: Return to Original Directory and Cleanup

After completing the review (whether approved, changes requested, or commented):

```bash
# Return to original working directory
cd $ORIGINAL_DIR
```

Inform the user:
```
"Review complete. I've returned to your original working directory at $ORIGINAL_DIR.

The PR review worktree still exists at ../talent_ai-pr-<PR_NUMBER>/.
Would you like me to clean it up? (This removes the directory only, not the branch.)"
```

**If user confirms cleanup:**
```bash
.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh pr-<PR_NUMBER>
```

**If user declines:** Leave the worktree for potential future use or manual cleanup.

---

## Using This Skill

### For New Review

```
I need to review PR #XXX. Please follow the systematic pr-review-workflow.
```

The workflow will:
1. Invoke Pre-Review Analysis Agent
2. If proceeding, invoke Code Review Agent
3. Invoke Decision & Communication Agent
4. If approved, invoke Post-Approval Agent

### For Resume After Rebase

```
PR #XXX has been rebased. Please resume the review starting from the Code Review phase.
```

### For Quick Status Check

```
Give me a pre-review analysis for PR #XXX - just the context and scope check, no code review yet.
```

---

## Scripts Reference

All scripts are in `scripts/` directory:

- **prepare_local_env.sh** - Ensures local main is clean and up to date
- **gather_pr_info.sh** - Gets comprehensive PR metadata and saves diff
- **check_staleness.sh** - Checks branch staleness, classifies files as DUPLICATE/MODIFIED/NEW
- **classify_files.sh** - Categorizes files by type (docs/tests/migrations/core)
- **generate_review_template.sh** - Creates approval or change request template

**Usage pattern**:
```bash
# For prepare_local_env (no PR number needed)
./scripts/prepare_local_env.sh

# For other scripts
./scripts/<script_name>.sh <PR_NUMBER>
```

All scripts save output to `/tmp/pr_<PR_NUMBER>_*` for reference.

---

## GitHub CLI Tips

### When Commands Fail - Look It Up Online

**CRITICAL**: When a terminal command fails unexpectedly:

1. **Get the current date first** - Run `date` to know what timeframe is relevant for searches
2. **Search online for the correct syntax** - Use `gh <command> --help` and web search with an appropriate year
3. **Update this skill** with the correct command once you figure it out

```bash
# Check current date before web searches
date
```

### Viewing Diff for Specific Files

The `gh pr diff` command does **NOT** support filtering by filename directly. There is an [open feature request](https://github.com/cli/cli/issues/5398) for this.

**WRONG** (will error):
```bash
gh pr diff 422 -- path/to/file.py  # Error: accepts at most 1 arg
```

**CORRECT** - Checkout PR first, then use git diff:
```bash
# Checkout PR and diff specific file against main
gh pr checkout <PR_NUMBER> && git diff origin/main -- path/to/file.py

# Or for multiple specific files
gh pr checkout <PR_NUMBER> && git diff origin/main -- file1.py file2.py
```

**Alternative** - Pipe through grep/awk (less reliable):
```bash
# Filter diff output with awk (can miss content at file boundaries)
gh pr diff 422 | awk '/^diff --git.*local\.py/,/^diff --git/'
```

---

## References

Detailed guides in `references/` directory - load as needed during review phases.

**Core references**:
- **django_best_practices.md** - Comprehensive Django review checklist
- **scope_creep_guide.md** - How to identify and handle scope creep

**Stack-specific references** (25+ available):
- Django REST Framework, Celery, PostgreSQL, Redis
- Azure services (OpenAI, Storage, AI Search)
- HTMX, Templates, Channels/WebSockets, CDN/SRI
- Document processing, file validation, AI/ML integration
- Custom middleware, audit logging, performance monitoring
- Authentication, authorization, SOC2, security

Load relevant references during Code Review phase based on technologies used in the PR.

---

## Key Principles

1. **Staleness first** - Always check before reviewing
2. **Clean local state** - Ensure local main is up to date before comparing
3. **Systematic approach** - Follow phases in order
4. **Use subagents** - Delegate to specialized agents
5. **Ask the user** - For scope creep beyond docs/tests and minor issues
6. **Document findings** - Be specific and actionable
7. **Ask before rebasing** - Never touch branches without permission
8. **NEVER skip tests** - ALWAYS install dependencies and run tests. NEVER suggest skipping test execution for ANY reason. If tests can't run, fix the blocker first.
9. **Communicate constantly** - Narrate what you're doing and why before running commands. Keep the user informed of your progress and reasoning. ALWAYS discuss findings verbosely with the user and ask for their feedback BEFORE drafting any review or approval message for GitHub.
10. **Resolve dependencies first** - Always check for and install new dependencies before running tests or migrations
11. **Be specific** - List exactly what was checked
12. **Provide options** - Give developer clear next steps
13. **NEVER mention Claude Code** - Do not mention Claude, Claude Code, AI, or assistants in any GitHub content (PRs, reviews, issues, comments). Write as if you personally did the work. No "Generated with Claude Code" footers.
