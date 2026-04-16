# Session Continuity

## The Problem

Claude Code sessions have finite context. An engagement may span weeks or months. Multiple sessions will work on the same engagement. Each new session starts with zero context about the engagement.

The blockchain methodology solves this by making the document system self-describing. But the skill also needs operational continuity: how does a new session know where the previous one left off, what was completed, and what still needs to be done?

## Session Handoff Documents

When a session ends with incomplete work, create a handoff document:

```
/<client_name>/<opportunity_name>/planning/session_handoff_<date>.md
```

### What a Handoff Document Contains

1. **What was completed this session.** Which document sets were fully processed, which files were written.

2. **What is partially completed.** Which files exist, which are still needed. Include the exact file names that were planned but not written.

3. **What needs to happen next.** Specific, actionable next steps with enough context that a new session can pick up without re-reading everything.

4. **Known issues or blockers.** Anything that went wrong, workarounds that were applied, things to avoid.

5. **User preferences learned.** Any guidance the user gave that is not captured in the methodology or skill notes. (Though ideally this should go in skill notes.)

6. **File inventory.** A tree listing of all files in the engagement folder (`/<client_name>/<opportunity_name>/`) with their status (DONE, IN PROGRESS, NOT STARTED, DELETE).

### Example Handoff

```markdown
# Session Handoff: 2026-03-20

## Completed
- Document Set 01 (Call Prep): 5 files + summary
- Document Set 02 (Meeting): People file and topic map

## Partially Completed
- Document Set 02: 5 deep dive files NOT WRITTEN
  - 02_meeting_technical_use_cases_2026-03-12.md
  - 02_meeting_what_was_tried_2026-03-12.md
  - (etc.)

## What Needs to Happen Next
Re-run the 5 parallel agents for the deep dives.
Each agent reads the transcript with ONE topic focus.

## Known Issues
Agent permissions: mode "bypassPermissions" works with
Write permission in settings.local.json.

## User Preferences
- Do NOT suggest doing deep dives sequentially
- Agents must do the analysis work
- Capture skill notes immediately when user gives guidance
```

## Reading Order for a New Session

When a new session begins on an existing engagement:

1. **Read the handoff document** (if one exists) to understand where things left off.
2. **Read the methodology document** (`/<client_name>/<opportunity_name>/research/00_methodology_<date>.md`) to understand the system.
3. **Read the skill notes** (`/<client_name>/<opportunity_name>/planning/skill_notes.md`, if it exists) to understand accumulated do's and don'ts.
4. **Read the summary documents** in `/<client_name>/<opportunity_name>/research/` in order to reconstruct the engagement state.
5. **Read the org chart** (`/<client_name>/<opportunity_name>/org_chart.md`) for people context.
6. **Read any incomplete work** that needs to be resumed.

## The Methodology Document as Anchor

The `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` file is the first document any session reads. It explains:

- What blockchain style means and why it is used
- The numbering convention
- The rules (never edit old docs, etc.)
- Summary documents, bridge documents, people tracking
- Processing order for new sets

This file CAN be updated (it is the exception to append-only) because it describes the system itself. If the methodology evolves, update the methodology document.

## Skill Notes as Accumulated Wisdom

The `/<client_name>/<opportunity_name>/planning/skill_notes.md` file accumulates do's, don'ts, and wisdom across sessions. It is organized by topic:

- Structure and organization
- Philosophy
- Numbering conventions
- Source material quality (speech-to-text handling)
- Transcript processing (standard files, variable files, multi-pass, agent architecture)
- Discussion capture
- Research agents
- Question batching

When the user gives guidance during a session ("don't fixate on timeline claims," "max 5 questions per batch"), it should be captured in skill notes immediately, not at the end of the session.

## Memory Integration

Some engagement-level patterns may warrant saving to Claude's persistent memory system (if available). Candidates:

- User preferences about communication style
- Feedback about approaches that worked or didn't
- Project-level context that transcends the session

Most information should stay in the engagement's skill notes (`/<client_name>/<opportunity_name>/planning/skill_notes.md`) rather than memory, because it is engagement-specific. Memory is for cross-engagement preferences.
