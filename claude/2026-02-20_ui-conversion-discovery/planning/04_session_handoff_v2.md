# Session Handoff v2: UI Conversion POC Proposal

**Date:** February 21, 2026
**For:** Next Claude session
**From:** Colin Moore (via previous session)
**Status:** Previous session failed. This is a fresh start with better direction.

---

## STOP - Read This First

A previous session attempted this work and failed badly. The failure is documented in `99_session_failure_handoff.md`. You don't need to read every detail, but understand the core mistake: **the session didn't listen**. Colin said "it's not verbose, it's just sounding like total BS" and the session responded by cutting the proposal in half. That's not a misunderstanding- that's not reading.

Your job is to actually listen, demonstrate technical expertise, and produce work that sounds like it comes from a Director of AI who has done this before- not a junior consultant trying to sound smart.

---

## Your Task

**Goal:** Create a compelling, technically detailed POC proposal for the EPNM→EMS UI conversion project.

**Approach:**
1. Read the required materials (listed below) to build your own understanding
2. Review the existing good work (meeting breakdown, brainstorm notes)
3. Write a new POC proposal from scratch that demonstrates expertise
4. Collaborate with Colin throughout- he'll be actively involved

---

## Required Reading

Read these in order:

### 1. Project Context
- `/home/cmoore/programming/cisco_projects/cicd/CLAUDE.md` - Formatting rules, project overview, style guidelines. **Read this carefully- previous session violated every style rule.**

### 2. Meeting Transcripts
- `source/guhan_selva-2-9-2026.txt` - First meeting (background context)
- `source/guhan_selva-2-20-2026.txt` - Discovery call (primary source)

Note: These are speech-to-text transcripts with errors. Use common sense- names may be garbled, technical terms misspelled.

### 3. Existing Work (Reference, Don't Copy)
- `planning/01_meeting_breakdown.md` - Structured decomposition of the discovery call. This is good work- use it to verify your understanding, but form your own view from the transcripts.
- `planning/02_poc_brainstorm.md` - Strategic brainstorm with Colin's feedback. Contains key concepts you must incorporate (two-phase approach, flywheel mechanism, etc.)

### 4. Failure Documentation
- `planning/99_session_failure_handoff.md` - Skim this to understand what went wrong. Don't repeat those mistakes.

---

## Technical Context You Must Understand

This isn't generic "UI modernization." You need to understand the specific technical challenge:

**EPNM (Legacy System):**
- Monolithic Java backend
- Dojo + JavaScript frontend with some Angular mixed in
- 70-100 UI screens
- Tightly coupled architecture
- Customers have used this for 15+ years
- Limited documentation ("trying to find the way around the code")

**EMS (Modern System):**
- Microservices Java backend
- Angular frontend
- New UX design (customers hate it)
- Some EPNM functionality not yet ported

**The Conversion Challenge:**
- **Vertical work**- if the UI doesn't exist in EMS, the backend doesn't either. This is NOT just skinning.
- Architectures are fundamentally different (monolith vs microservices)
- Can't copy code- "surgery" was done on the old core
- Backend logic must be extracted and re-implemented alongside UI

**BayOne's Technical Approach (as discussed with Cisco):**
- Claude Code for codebase exploration and initial analysis
- LangGraph agent swarm (architect, engineer, foreman, judge agents) for systematic conversion
- Playwright for automated visual testing and validation
- Custom agents tuned specifically to this codebase- not generic tools
- Knowledge graph / pattern library that builds over time

You should be able to speak to Dojo→Angular migration patterns, monolith→microservices decomposition, and how AI-assisted code conversion actually works. If you can't, you're not ready to write this proposal.

---

## Key Strategic Concepts (From Brainstorm)

These came from Colin's feedback and must be incorporated:

### Two-Phase POC Approach
- **Phase 1 (Exploration):** Analyze codebase, categorize screens by complexity, identify 2-3 good POC candidates collaboratively with Cisco SMEs
- **Phase 2 (Conversion):** Convert selected screens end-to-end, test, document patterns

This protects us from picking bad screens blind and makes Cisco a partner in scope decisions.

### The Flywheel Mechanism
Don't just say "it gets faster"- that sounds like a pipe dream. Explain the concrete mechanism:

| Phase | Work | One-time? |
|-------|------|-----------|
| Codebase exploration | Map architecture, relationships, patterns | Yes |
| Agent development | Build custom tooling for THIS codebase | Yes |
| Workflow design | Establish conversion process | Yes |
| Screen conversion | Apply patterns, run agents | Per screen |
| Testing/validation | Gap analysis, fixes | Per screen |

The POC front-loads all the one-time work. Screens 1-3 carry that weight. Screen 50 is just conversion + validation.

### POC vs Paid Boundary
- **POC (Free):** Colin solo, sequential work, 2-3 screens, 4 weeks from access. This is the slowest we can go.
- **Paid Engagement:** Team scale, parallel streams, established patterns. Multiplicative speedup.
- The POC investment (codebase analysis, custom agents, patterns) becomes the foundation for paid work.

### Timeline
- 4 weeks total, timer starts when we have repo access
- Cisco can provide screen examples and context before access
- Phase 1 can partially overlap with waiting for laptop

### Scope
- 2-3 representative screens (Cisco suggested 10- that's too much for free)
- Cisco proposes candidates, we verify feasibility during exploration
- Concerned about "backend isn't set up yet" screens- could explode scope

---

## Formatting Rules (HARD REQUIREMENTS)

Previous session violated all of these. Do not repeat.

### Em-dashes as separators
- **Wrong:** `the system - architecture` (space before)
- **Right:** `the system- architecture` (no space before, space after OK)

### Compound words stay normal
- `end-to-end`, `cloud-native`, `AI-first`- these are hyphenated words, not em-dashes

### Slashes
- **Wrong:** `interface /single pane`
- **Right:** `interface/ single pane` (space after, not before)

### General
- No emojis unless explicitly requested
- Be concise but NOT at the expense of technical depth
- Read CLAUDE.md for additional formatting preferences

---

## File Naming Rules

**Check what exists before creating files.** The previous session created duplicate `01_` files.

Current state of `planning/`:
```
00_session_handoff.md       (original handoff - superseded)
01_session_understanding.md (duplicate - shouldn't exist)
01_meeting_breakdown.md     (good work)
02_poc_brainstorm.md        (good work)
03_poc_proposal_draft.md    (garbage - rewrite from scratch)
04_session_handoff_v2.md    (this file)
99_session_failure_handoff.md (failure documentation)
```

Your new proposal should be `05_poc_proposal_v2.md`. If you create additional files, continue the sequence: `06_`, `07_`, etc.

**Always use two-digit prefixes.** Always check existing files first.

---

## What the Proposal Must Accomplish

1. **Demonstrate technical expertise.** Show you understand Dojo→Angular conversion, monolith→microservices patterns, how AI-assisted code conversion works. Sound like someone who has done similar work (C# to Rust, Spring to Go, thick client to web).

2. **Inspire confidence.** Cisco should read this and think "these people know what they're doing."

3. **Explain the methodology concretely.** Not just phases- actual technical approach. Codebase knowledge graph, pattern identification, custom agent development, LangGraph architecture.

4. **Show the flywheel mechanism.** Why it accelerates, with specifics. Not "it gets faster"- show the one-time vs per-screen breakdown.

5. **Frame the investment correctly.** The POC is heavy lifting we're doing for free that becomes the foundation for paid work.

6. **Be appropriately scoped.** 2-3 screens, 4 weeks from access, Colin solo. Clear boundary between POC and paid.

7. **Sound like Colin.** Director of AI with deep experience. Confident, direct, technically grounded. Not consultant-speak, not student work.

---

## Working Style

**Be a collaborative partner:**
- Bring ideas and perspectives proactively
- Help Colin think through options
- Don't just ask for input constantly

**But stay grounded:**
- Don't go beyond what Colin says or approves
- Don't make independent assumptions about scope or commitments
- Colin will be actively involved- work with him, not ahead of him

**Listen carefully:**
- When Colin gives feedback, read it. Actually read it.
- Don't pattern-match to generic expectations
- If he says "it's not verbose, it's BS"- that means add depth, not cut length

---

## Getting Started

1. Read CLAUDE.md first
2. Read both transcripts to build your own understanding
3. Review the meeting breakdown and brainstorm docs
4. Skim the failure handoff to understand what went wrong
5. Check in with Colin before starting the proposal- verify you understand
6. Write the proposal collaboratively, checking in as you go

**Do not start writing until you've confirmed your understanding with Colin.**
