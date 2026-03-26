# Extract GitHub Issues from Meeting Content

Extract actionable GitHub issues from meeting transcripts, call notes, PDFs, images, or conversation context.

## Instructions

Use the `meeting-git-issue-extractor` skill to process the user's input and create well-structured GitHub issues.

### Initial Questions

1. Check if there are any incomplete sessions in `claude/` folder using state_manager.py
2. If incomplete session found, ask user if they want to resume
3. If starting fresh, ask:
   - What topic/meeting is this for? (to name the session folder)
   - Does the user have files to provide, or should we use conversation context?
   - If files: move, copy, or extract/summarize?

### Workflow

Follow the phases defined in the meeting-git-issue-extractor SKILL.md:

1. **Session Setup** - Create folder structure, handle input files
2. **Document Analysis** - Launch document-analyzer agent to extract topics
3. **Workflow Selection** - Ask user preference (parallel explore + sequential issues OR fully parallel)
4. **Codebase Exploration** - Launch codebase-explorer agents per topic
5. **User Clarification** - Ask questions (max 3 per message, one issue at a time)
6. **Issue Drafting** - Launch issue-drafter agents using github-issue-creator-skill patterns
7. **Issue Review** - Launch issue-reviewer agent to check compliance
8. **GitHub Creation** - With user approval only, create issues using gh CLI

### Hard Rules

1. **Never mention Claude, Claude Code, or AI in any issue**
2. **Never add Co-Authored-By or AI attribution**
3. **Maximum 3 questions per message**
4. **One issue at a time during clarification**
5. **Always create markdown files first, then create in GitHub**
6. **Never create GitHub issues without explicit user approval**
7. **Ask assignee per issue (not every issue needs one)**

### Integration

- Use `github-issue-creator-skill` patterns for issue templates
- Reference `phoenix-theme-skill` in UI-related issues
- Reference PR #817 for Playwright testing capabilities

### Arguments

$ARGUMENTS - Optional: path to transcript file or topic description

### Example Invocations

- `/extract-issues` - Start fresh, will ask questions
- `/extract-issues ~/transcript.txt` - Start with specific file
- `/extract-issues "call with Pallavi about notifications"` - Start with topic description
