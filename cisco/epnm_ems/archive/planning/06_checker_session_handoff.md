# Checker Session: POC Proposal Quality Review

**Date:** February 21, 2026
**For:** Reviewer Claude session
**Purpose:** Review the POC proposal with extreme prejudice

---

## Your Role

You are a quality gate. A previous session failed badly on this work- wrote generic consultant-speak, ignored explicit feedback, violated formatting rules. A new session has now attempted the proposal. Your job is to tear it apart if it deserves it.

**Do not be nice. Do not give participation trophies. Be ruthless but fair.**

---

## What You're Reviewing

The POC proposal at: `planning/05_poc_proposal_v2.md`

This is a proposal for BayOne Solutions to do a proof-of-concept UI conversion project for Cisco. It needs to:
1. Demonstrate technical expertise
2. Inspire confidence
3. Sound like a Director of AI, not a student
4. Follow all formatting rules
5. Incorporate the strategic concepts from the brainstorm

---

## Required Reading Before Review

1. `/home/cmoore/programming/cisco_projects/cicd/CLAUDE.md` - Formatting rules and style guidelines
2. `planning/04_session_handoff_v2.md` - The instructions given to the writing session
3. `planning/02_poc_brainstorm.md` - The strategic concepts that must be incorporated
4. `planning/99_session_failure_handoff.md` - What went wrong last time (so you know what to watch for)

Optionally, skim the transcripts in `source/` to verify technical accuracy.

---

## Review Checklist

### Formatting (HARD FAIL if violated)

- [ ] Em-dashes: no space before (`system- architecture` not `system - architecture`)
- [ ] Slashes: space after, not before (`interface/ single` not `interface /single`)
- [ ] Compound words unchanged (`end-to-end`, `AI-first`)
- [ ] No emojis
- [ ] Consistent heading structure

### Technical Depth

- [ ] Demonstrates understanding of Dojo→Angular migration
- [ ] Demonstrates understanding of monolith→microservices decomposition
- [ ] Explains how AI-assisted code conversion actually works (not just "AI helps")
- [ ] References specific tooling: Claude Code, LangGraph, Playwright
- [ ] Explains custom agents tuned to this codebase, not generic tools
- [ ] Shows understanding of "vertical" work (UI + backend together)

### Strategic Concepts (Must Include)

- [ ] Two-phase approach (Exploration → Conversion)
- [ ] Flywheel mechanism with concrete breakdown (one-time vs per-screen work)
- [ ] POC vs Paid boundary clearly drawn
- [ ] Timeline: 4 weeks from access, Colin solo
- [ ] Scope: 2-3 screens, Cisco proposes candidates
- [ ] POC as free investment that becomes foundation for paid work

### Tone & Voice

- [ ] Sounds like a Director of AI with deep experience
- [ ] Confident, not hedging or apologetic
- [ ] Direct, not verbose filler
- [ ] Technical without being academic
- [ ] Would inspire confidence if you were Cisco reading this

### Red Flags (Immediate Failure)

- Generic phrases like "leverage synergies" or "best-in-class"
- Vague promises without mechanism ("it gets faster over time")
- Student-level writing that sounds like a first attempt
- Consultant-speak that says nothing
- Any evidence they didn't read the instructions or feedback

---

## How to Report

Provide your review to Colin in this format:

### Verdict: [PASS / FAIL / NEEDS REVISION]

### Formatting Issues
(List any violations with line references if possible)

### Technical Depth Assessment
(Is it expert-level or generic? Specific gaps?)

### Strategic Concept Coverage
(What's missing or weak?)

### Tone Assessment
(Does it sound like Colin or like a student?)

### Red Flags Found
(Any immediate failures?)

### Specific Feedback
(Line-by-line or section-by-section critique)

### Recommendation
(What needs to change, or is it ready?)

---

## Standards

**PASS:** Ready to send to Cisco with minor polish at most.

**NEEDS REVISION:** Core is solid but has specific issues that must be fixed. List them precisely.

**FAIL:** Fundamentally broken. Would embarrass BayOne if sent. Must be rewritten.

Be honest. Colin would rather know it's bad now than send garbage to Cisco.
