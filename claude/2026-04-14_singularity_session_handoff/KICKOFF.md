# Kickoff Prompt

**Paste this into the new Claude session:**

---

I need you to pick up where a previous Claude session left off on a major Singularity skill extension project. Before doing ANY work, you need to get oriented.

## Step 1: Read the handoff

Read these files in this order:

1. `claude/2026-04-14_singularity_session_handoff/HANDOFF.md` — Start here. Orientation, priorities, behavioral context.
2. `claude/2026-04-14_singularity_session_handoff/00_session_overview.md` — Full picture of what was done across 4 days.
3. `claude/2026-04-14_singularity_session_handoff/references/03_unresolved_and_remaining.md` — What needs to happen next, including the folder restructure problem and the full current file list.
4. `claude/2026-04-14_singularity_session_handoff/references/02_feedback_violations_and_lessons.md` — Behavioral corrections and lessons. Read this carefully. The previous session had significant issues with inventing rules and thresholds that I did not give.

The other reference files are available when you need specific context:
- `references/01_all_changes_by_phase.md` — Every file changed, organized by phase
- `references/04_hooks_and_enforcement.md` — Enforcement architecture, stop hook, hard rules
- `references/05_presentations_and_mermaid.md` — Presentation system and mermaid capabilities

## Step 2: Read the hard rules

Read `.claude/skills/singularity/references/hard_rules.md`. These are 16 behavioral rules (B1-B16) that exist because the previous session violated each one at least once. They are not suggestions.

## Step 3: Understand the immediate priority

The Singularity skill's folder structure needs to be redesigned. It is currently a mess with 7 levels of nesting, duplicate folder names, scattered gold standards, and an out-of-date structure doc. Do NOT start reorganizing without discussing the target structure with me first.

## Step 4: Create a session folder and to-do list

Create `claude/2026-04-14_singularity_restructure/` (or whatever date is current) with a to-do list in markdown. Capture any feedback I give you in this folder immediately — do not wait.

## Ground rules

- One question at a time in discussion (B1)
- Do not invent thresholds, absolute bans, or universal rules from my feedback (B2)
- Read files before describing or making claims about them (B4)
- Propose structure before producing documents (B7)
- If I correct you multiple times, confirm the agreed approach before executing (B16)
- Use to-do lists in markdown files on disk, not just in conversation
- The full transcript from the previous session is at `2026-04-14-170841-look-at-ciscocicd-we-have-used-the-singularity_508PM_MASTER.txt` if you need to look up specific context (11,000+ lines)

Let me know when you have read the handoff documents and are ready to proceed.
