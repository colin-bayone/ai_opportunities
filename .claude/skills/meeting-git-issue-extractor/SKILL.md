---
name: meeting-git-issue-extractor
description: Extract actionable GitHub issues from meeting transcripts, call notes, images, and PDFs. Use when user mentions meeting notes, transcripts, action items from calls, or wants to create issues from conversation context. Supports async sub-agents for parallel codebase exploration. (project)
---

# Meeting Git Issue Extractor

## Overview

This skill transforms meeting transcripts, call notes, PDFs, images, and conversation context into well-structured GitHub issues. It uses async sub-agents for parallel exploration and integrates with the `github-issue-creator-skill` for issue templating.

## When to Use This Skill

Use proactively when user:
- Mentions "meeting notes", "transcript", "call notes"
- Has a recording transcript to process
- Says "action items" or "issues from our discussion"
- Wants to extract work items from any documented conversation
- Has PDFs or images with requirements to convert to issues

## Hard Rules

1. **Never mention Claude Code, Claude, or AI in any issue content**
2. **Never add Co-Authored-By or attribution to Claude/AI**
3. **Never create GitHub issues without explicit user approval**
4. **Maximum 3 questions per message to user**
5. **One issue at a time during clarification phase**
6. **Always create issues as markdown files first, then create in GitHub**
7. **Never assign time estimates, timelines, or complexity levels** - LLMs have no concept of time; don't guess how long things take
8. **Never assign ownership unless user explicitly states it** - Don't assume who should work on what
9. **Never reference issue numbers that don't exist yet** - We can't know future issue numbers; use descriptive names for dependencies until issues are created
10. **Create issues in dependency order when practical** - If Issue B depends on Issue A, prefer creating Issue A first so we have the real issue number
11. **Post-creation edits are allowed** - After creating issues, go back and update dependency references with actual issue numbers to avoid blocking async workflows
12. **Keep issues focused - no scope creep** - Each issue should be a single logical unit of work. If additional work is identified, create separate issues rather than bundling
13. **Screenshots required for UI changes** - Place in `issues/attachments/<issue-name>/` for manual upload to GitHub

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 1: Session Setup                                                  │
│   - Create session folder (claude/<date>_<topic>/)                      │
│   - Handle input files (move/copy/extract-summarize)                    │
│   - Create orchestration structure                                      │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 2: Document Analysis (document-analyzer agent - opus)             │
│   - Analyze transcripts/PDFs/images                                     │
│   - Extract action items and topics                                     │
│   - Note transcription errors and ambiguities                           │
│   - Output: topic breakdown with priorities                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 3: Workflow Selection                                             │
│   Ask user preference:                                                  │
│   - Option A: Parallel exploration + sequential issues                  │
│   - Option B: Fully parallel (explore + draft all at once)              │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 4: Codebase Exploration (codebase-explorer agents - opus)         │
│   - Investigate current implementation per topic                        │
│   - Can run in parallel if user chose that option                       │
│   - Output: findings documents per topic                                │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 5: User Clarification (main agent)                                │
│   - Ask clarifying questions (max 3 per message)                        │
│   - Handle one topic/issue at a time                                    │
│   - Record decisions in decisions/clarifications.md                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 6: Issue Drafting (issue-drafter agents - opus)                   │
│   - Draft issues using github-issue-creator-skill patterns              │
│   - Respect chronology, priority, dependencies from planning            │
│   - Output: markdown files in issues/ folder                            │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 7: Issue Review (issue-reviewer agent - haiku)                    │
│   - Syntax check each issue                                             │
│   - Rule compliance (no AI attribution, proper format)                  │
│   - Output: reviewed/approved flag                                      │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ Phase 8: GitHub Creation (with user approval)                           │
│   - Fetch available labels via script                                   │
│   - Ask assignee per issue                                              │
│   - Create in GitHub only after explicit approval                       │
└─────────────────────────────────────────────────────────────────────────┘
```

## Phase 1: Session Setup

### Step 1.1: Create Session Folder

Ask user for topic name, then create folder structure:

```
claude/<YYYY-MM-DD>_<topic-slug>/
├── orchestration/
│   ├── 00_master_plan.md           # Overall coordination
│   ├── 01_topic_breakdown.md       # Identified topics and priorities
│   ├── 02_agent_assignments.md     # Which agent handles what
│   └── state.json                  # Resumption state tracking
├── agents/
│   ├── document-analyzer/
│   │   └── analysis_output.md
│   ├── codebase-explorer/
│   │   └── <topic>_findings.md
│   ├── issue-drafter/
│   │   └── drafts/
│   └── issue-reviewer/
│       └── review_results.md
├── research/
│   └── <topic>_investigation.md
├── issues/
│   ├── 01_<issue-name>.md
│   └── attachments/                # Screenshots/images for issues
│       ├── 01_<issue-name>/        # Per-issue attachment folders
│       │   └── screenshot.png
│       └── README.md               # Instructions for attaching to GitHub
├── decisions/
│   └── clarifications.md           # Q&A log with user
└── source/
    └── (original files always here)
```

### Step 1.2: Handle Input Files

Ask user about their input files using AskUserQuestion:

**Question 1: Input Source**
- Header: "Input"
- Options:
  - "I have files to provide" - User will specify file paths
  - "Use conversation context" - Extract from current conversation
  - "Both" - Files and conversation context

**Question 2: File Handling** (if files provided)
- Header: "File handling"
- Options:
  - "Move files" - Cut from original location to source/
  - "Copy files" - Copy to source/, keep originals
  - "Extract & summarize" - For PDFs: sub-agent extracts and summarizes

### Step 1.3: Initialize State

Create `orchestration/state.json`:

```json
{
  "session_id": "<uuid>",
  "created_at": "<timestamp>",
  "current_phase": "setup",
  "completed_phases": [],
  "topics": [],
  "workflow_mode": null,
  "issues_created": [],
  "pending_approvals": []
}
```

## Phase 2: Document Analysis

Launch `document-analyzer` sub-agent (opus):

**Agent prompt:**
```
Analyze the documents in the source/ folder for this session.

Your task:
1. Read all source documents thoroughly
2. Extract action items, feature requests, bug reports, improvements
3. Identify distinct topics/themes
4. Note any transcription errors or ambiguities
5. Assign preliminary priorities

Output to agents/document-analyzer/analysis_output.md:
- Summary of documents analyzed
- List of topics identified with descriptions
- Action items per topic
- Ambiguities or unclear items that need clarification
- Suggested priority order

Remember: These are likely speech-to-text transcripts with potential transcription errors. Use common sense interpretation.
```

## Phase 3: Workflow Selection

Ask user their preferred workflow:

**Question: Workflow Mode**
- Header: "Workflow"
- Options:
  - "Parallel explore, sequential issues" - Explore all topics at once, then clarify/draft one at a time
  - "Fully parallel" - Explore and draft all in parallel, then review all at once

Update `state.json` with choice.

## Phase 4: Codebase Exploration

For each identified topic, launch `codebase-explorer` sub-agent (opus):

**Agent prompt:**
```
Investigate the current implementation related to: <topic>

Context from document analysis:
<summary from Phase 2>

Your task:
1. Search codebase for relevant files and patterns
2. Understand current architecture
3. Identify what exists vs what needs to be built
4. Note any existing patterns to follow
5. Find related documentation

Output to agents/codebase-explorer/<topic>_findings.md:
- Relevant files discovered
- Current implementation state
- Patterns to follow
- Dependencies and related systems
- Gaps between current state and requirements
```

**If workflow_mode is "Parallel explore, sequential issues":** Launch all explorers in parallel using multiple Task tool calls in a single message.

**If workflow_mode is "Fully parallel":** Launch explorers and issue-drafters together.

## Phase 5: User Clarification

For each topic, engage in clarification Q&A:

**Rules:**
- Maximum 3 questions per message
- One topic/issue at a time
- Use AskUserQuestion tool for structured questions
- Record all Q&A in `decisions/clarifications.md`

**Pattern:**
```markdown
## Topic: <topic name>

### Question 1
**Asked:** <question>
**Options:** A) ... B) ... C) ...
**User chose:** <answer>
**Rationale:** <any explanation user provided>

### Question 2
...
```

## Phase 6: Issue Drafting

Launch `issue-drafter` sub-agent (opus) for each issue:

**Agent prompt:**
```
Draft a GitHub issue for: <issue title>

Context:
- Document analysis: <relevant excerpts>
- Codebase findings: <relevant excerpts>
- User decisions: <clarifications>
- Dependencies: <any prerequisite issues>
- Priority: <priority level>

Use the github-issue-creator-skill patterns from:
.claude/skills/github-issue-creator-skill/templates/

Include:
- Clear description (What/Why/How)
- Technical approach
- Specific tasks with file paths
- Testing requirements
- Acceptance criteria
- Notes for implementation

HARD RULES:
- NO mention of Claude, Claude Code, or AI
- NO Co-Authored-By lines
- Use Phoenix theme skill reference where UI is involved
- Reference PR #817 for Playwright testing where applicable

Output to: issues/<nn>_<issue-slug>.md
```

## Phase 7: Issue Review

Launch `issue-reviewer` sub-agent (haiku) for each drafted issue:

**Agent prompt:**
```
Review this issue for compliance:

Issue file: <path>

Check:
1. No Claude/AI attribution or mentions
2. Proper markdown formatting
3. All required sections present (Description, Tasks, Testing, Acceptance Criteria)
4. File paths are specific and accurate
5. Dependencies correctly noted
6. No magic numbers (use CSS variables, constants)

Output to agents/issue-reviewer/review_results.md:
- Issue: <filename>
- Status: PASS / NEEDS_FIXES
- Issues found: <list if any>
- Suggested fixes: <if needed>
```

## Phase 8: GitHub Creation

### Step 8.1: Fetch Labels

Run script to get available labels:

```bash
python .claude/skills/meeting-git-issue-extractor/scripts/fetch_labels.py
```

This outputs available labels for tagging issues.

### Step 8.2: Per-Issue Approval and Creation

For each reviewed issue:

1. **Present issue summary to user**
2. **Ask for assignee:**
   - Header: "Assignee"
   - Options: List known team members + "None" + "Other"
3. **Ask for labels:**
   - Based on fetched labels
   - Can select multiple
4. **Confirm creation:**
   - "Create this issue in GitHub now?"
   - Options: "Yes, create" / "Skip for now" / "Edit first"

5. **Create with gh CLI:**
```bash
# Basic creation
gh issue create --title "Issue Title" --body-file issues/01_issue-name.md

# With assignee and labels
gh issue create --title "Issue Title" --body-file issues/01_issue-name.md --assignee "username" --label "enhancement,ui"

# If issue has attachments, open in browser for manual upload
gh issue create --title "Issue Title" --body-file issues/01_issue-name.md --web
```

6. **Update state.json** with created issue number and URL

### Step 8.3: Post-Creation Dependency Updates

After all issues are created, update any dependency references:

```bash
# Edit issue body to add real issue numbers
gh issue edit <number> --body-file issues/01_issue-name-updated.md

# Or just add a comment with the dependency link
gh issue comment <number> --body "Depends on #<dependency-number>"
```

### Step 8.4: Handle Attachments

**Important:** The gh CLI does not support uploading attachments. For issues with screenshots/images:

#### Capturing Screenshots Locally (Playwright)

Use the Phoenix Theme skill's Playwright integration for automated screenshots:

```bash
# Ensure dev server is running and DEV_AUTH_ENABLED=True in .env.local

# Take authenticated screenshot of any page
poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py \
    --url http://localhost:8000/candidates/search/ \
    --email user@bayone.com \
    --output issues/attachments/01_issue-name/screenshot.png
```

See `docs/playwright-testing-guide.md` and PR #820 for full details.

#### Uploading to GitHub Issues

1. **Option A - Web Upload (Recommended for few attachments):**
   ```bash
   # Open issue in browser for manual attachment
   gh issue view <number> --web
   ```
   Then drag/drop images from `issues/attachments/<issue-name>/` into the comment box.

2. **Option B - Create with --web flag:**
   ```bash
   gh issue create --title "..." --body-file ... --web
   ```
   This opens the browser where you can drag/drop attachments before submitting.

3. **Option C - Add attachments via comment:**
   - Create the issue first via CLI
   - Open in browser: `gh issue view <number> --web`
   - Add a comment with the attached images

**Private Repository Security:** Attachments in private repos are secure:
- Stored on GitHub's CDN with token-expiring links
- Only users with repository access can view them
- Links stop working after token expiration

## Resumption Support

### Saving State

After each phase completion, update `orchestration/state.json`:

```json
{
  "current_phase": "exploration",
  "completed_phases": ["setup", "analysis"],
  "topics": [
    {"name": "search-page", "status": "explored"},
    {"name": "notifications", "status": "pending"}
  ],
  "last_activity": "<timestamp>"
}
```

### Resuming Session

When user returns and invokes skill:

1. Check for existing session folders in `claude/`
2. If found with incomplete state, ask: "Resume session from <folder>?"
3. Load `state.json` and continue from `current_phase`

## Sub-Agent Definitions

### document-analyzer

| Property | Value |
|----------|-------|
| Model | opus |
| Async | No (needs immediate output for planning) |
| Tools | Read, Glob, Write |
| Purpose | Analyze source documents, extract topics and action items |

### codebase-explorer

| Property | Value |
|----------|-------|
| Model | opus |
| Async | Yes (can run in parallel) |
| Tools | Read, Glob, Grep, Task (for deeper exploration) |
| Purpose | Investigate current implementation per topic |

### issue-drafter

| Property | Value |
|----------|-------|
| Model | opus |
| Async | Yes (can draft in parallel) |
| Tools | Read, Write, Glob |
| Purpose | Draft issue markdown using github-issue-creator-skill patterns |

### issue-reviewer

| Property | Value |
|----------|-------|
| Model | haiku |
| Async | No (quick review) |
| Tools | Read, Write |
| Purpose | Syntax check and rule compliance verification |

## Scripts

### scripts/init_session.py

Creates session folder structure with proper permissions and initial files.

### scripts/fetch_labels.py

Fetches available GitHub labels for the repository:
```python
# Uses: gh label list --json name,description
```

### scripts/state_manager.py

Utilities for reading/writing session state:
- `load_state(session_path)` - Load state.json
- `save_state(session_path, state)` - Save state.json
- `get_current_phase(session_path)` - Get current phase
- `advance_phase(session_path, new_phase)` - Move to next phase

## Example Session

```
User: I have a transcript from my call with Pallavi about UI improvements

Claude: I'll help you extract GitHub issues from that transcript. Let me set up a session folder.

[Creates claude/2025-12-30_pallavi-ui-call/]

What would you like to do with the transcript file?
1. Move it to the session folder
2. Copy it to the session folder
3. Extract and summarize (for PDFs)

User: Copy it

Claude: [Copies file to source/]

Now I'll analyze the transcript to identify topics and action items.

[Launches document-analyzer agent]

I found 3 main topics:
1. Search page collapsible sections
2. Skills terminology standardization
3. Notification system improvements

How would you like to proceed?
1. Parallel exploration + sequential issues
2. Fully parallel

User: Option 1

Claude: [Launches 3 codebase-explorer agents in parallel]

Let's start with the search page topic. I have some clarifying questions:

1. For the collapsible sections, should they use Bootstrap collapse or custom JS?
   A) Bootstrap collapse (recommended)
   B) Custom JavaScript
   C) Other

2. Which sections should be collapsible?
   A) All sections except title
   B) Only Ideal Candidate and Key Skills
   C) Let me specify

[Max 3 questions per message, continues through clarification...]
```

## Related Skills and References

- `github-issue-creator-skill` - Issue templates and patterns
- `phoenix-theme-skill` - UI component patterns, Playwright screenshot capabilities (PR #820)
- `docs/git-workflow-requirements.md` - Team workflow requirements (issues completed in order, no scope creep, acceptance criteria)
- `docs/playwright-testing-guide.md` - Authenticated screenshot capture for UI issues

## gh CLI Quick Reference

```bash
# Create issue
gh issue create --title "Title" --body-file issues/01_name.md
gh issue create --title "Title" --body-file issues/01_name.md --assignee "user" --label "label1,label2"
gh issue create --title "Title" --body-file issues/01_name.md --web  # Opens browser for attachments

# Edit issue (for dependency updates)
gh issue edit <number> --body-file issues/01_name-updated.md
gh issue edit <number> --add-label "label"

# Add comment
gh issue comment <number> --body "Depends on #<other-number>"

# View issue
gh issue view <number>
gh issue view <number> --web  # Opens in browser

# List labels
gh label list --json name,description
```

## Slash Command

Also invocable via: `/extract-issues`
