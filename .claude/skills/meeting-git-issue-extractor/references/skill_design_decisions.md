# Meeting Git Issue Extractor - Design Decisions

This document captures the design decisions made during skill creation for reference and future modifications.

## Origin

Created from a real workflow session on December 29-30, 2025 where we:
1. Analyzed a transcript from a call with Pallavi Badiger
2. Created 5 search page issues (#841-845)
3. Created 4 notification system issues (#852-855)
4. Followed a structured Q&A process with max 3 questions per message

The skill captures this workflow for reuse.

## Key Design Decisions

### 1. Sub-Agent Model Selection

| Agent | Model | Rationale |
|-------|-------|-----------|
| document-analyzer | opus | Needs deep understanding of transcripts, nuance in speech-to-text errors |
| codebase-explorer | opus | Context-heavy work, needs comprehensive codebase understanding |
| issue-drafter | opus | Quality issue writing requires sophisticated understanding |
| issue-reviewer | haiku | Simple rule-checking task, fast verification |

**Decision:** User explicitly requested Opus for exploration/drafting agents. Haiku is only appropriate for simple compliance checking.

### 2. Workflow Options

Two modes supported:
- **Parallel explore, sequential issues**: Explore all topics at once, then clarify/draft one topic at a time
- **Fully parallel**: Do everything in parallel, review all at once

**Rationale:** User wanted flexibility. The sequential issues option allows focused attention on one topic at a time, reducing cognitive load.

### 3. Question Limits

- Maximum 3 questions per message
- One issue at a time during clarification phase

**Rationale:** User explicitly stated "don't hit them with ten questions... that's overwhelming"

### 4. File Handling Options

Three options for source files:
1. **Move** - Cut from original location
2. **Copy** - Keep original, copy to session
3. **Extract & summarize** - For PDFs, have agent extract and summarize

**Rationale:** User wanted flexibility, especially for PDFs which may need preprocessing.

### 5. Attribution Rules

**HARD RULE:** Never mention Claude, Claude Code, or AI in any issue content.

This applies to:
- Issue body text
- Co-Authored-By lines
- Generated-by notices
- Any reference to AI assistance

**Rationale:** From project CLAUDE.md - this is a strict requirement.

### 5b. No Time Estimates or Complexity Levels

**HARD RULE:** Never assign time estimates, timelines, or complexity levels to issues.

Forbidden patterns:
- "Estimated Complexity: Low/Medium/High"
- "This will take 2-3 days"
- "~4 hours of work"
- Story points or effort estimates

**Rationale:** LLMs have no concept of time or how long tasks take, especially with AI-assisted coding. These estimates are meaningless guesses that could mislead developers.

### 5c. No Non-Existent Issue References

**HARD RULE:** Never reference issue numbers that don't exist yet.

- WRONG: "Depends on: #999" (when #999 hasn't been created)
- RIGHT: "Depends on: Issue for Notification Types Registry"

**Rationale:** We can't know future issue numbers. Use descriptive names, then update with actual numbers after creation via `gh issue edit`.

**Post-creation updates allowed:** After all issues are created, go back and update dependency references with real issue numbers to avoid blocking async workflows.

### 6. Assignee Handling

Ask per issue, not batch assignment.

**Rationale:** User stated "not every issue will get an assignee at the time of creation"

### 7. GitHub Creation Flow

- Always create markdown files first
- Never create in GitHub without explicit user approval
- Fetch available labels via script to enable proper tagging

**Rationale:** User explicitly stated "You should always make them as Markdown files for me to review"

### 8. Session Resumption

Full resumption support via `orchestration/state.json`.

Tracks:
- Current phase
- Completed phases
- Topics and their status
- Issues created
- Workflow mode selected

**Rationale:** These workflows can take time; interruptions are expected.

### 9. Integration with github-issue-creator-skill

Layered approach:
- meeting-git-issue-extractor handles extraction and coordination
- issue-drafter agents use github-issue-creator-skill patterns

**Rationale:** Separation of concerns; each skill has its purpose.

### 10. Folder Structure

Per-agent folders plus master orchestration:
```
claude/<date>_<topic>/
├── orchestration/     # Master coordination
├── agents/           # Per-agent output folders
├── research/         # Investigation outputs
├── issues/           # Final issue markdowns
├── decisions/        # Q&A log
└── source/           # Original files (always created)
```

**Rationale:** User wanted "each sub-agent to have its own folder, as well as one master planning folder to orchestrate"

## Future Enhancements

Noted but not implemented:
1. Audio file support (transcription)
2. Django 6 upgrade evaluation (separate concern)
3. Additional input format support

## Related Skills

- `github-issue-creator-skill` - Issue templates and patterns
- `phoenix-theme-skill` - UI patterns (referenced in issues)
- `skill-creator` - Used to initialize this skill

## Session That Created This Skill

Original transcript from December 29, 2025 call is in:
`claude/2025-12-29_pallavi_call/`

Issues created during that session:
- Search page: #841-845
- Notifications: #852-855

All assigned to pbadiger1994 (Pallavi Badiger)
