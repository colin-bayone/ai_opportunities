# Handoff: Bad Slide Autopsy

## Purpose

You are a research analyst investigating 18 slides that have been flagged for removal from a McGrath RFP response deck. Your job is to read each flagged slide's extracted content, look at its screenshot, and document exactly WHY it's bad. The goal is to produce a detailed anti-patterns reference that future slide-building sessions can use to understand what NOT to do.

This is a research and documentation task. You are NOT building or fixing slides.

## Context

### The Project
BayOne Solutions is responding to an RFP from McGrath RentCorp for managed services support. A coworker named Amit created a WIP PowerPoint deck that is, frankly, bad. Colin (Director of AI) and Neha (collaborator) are rebuilding the deck as high-fidelity HTML slides. They've flagged 18 of 48 slides to skip.

### Why This Matters
Colin specifically noted that the Neha/Colin call transcripts discuss why these slides are bad. The anti-patterns you document will be used as a "what not to do" guide for the sessions that build the replacement slides. Think of this as a design review postmortem.

### Who You Can Ask
If you have questions or need clarification, tell the user -- they are the orchestrator coordinating this project and can help.

## Source Material

### Extracted PPTX (The Bad Deck)
**Base path:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/`

Each slide folder contains:
- `content.md` -- Extracted text content
- `layout.md` -- Layout description
- `visual_elements.md` -- Visual element descriptions
- `slide_NN.png` -- Screenshot of the original slide

### Transcript Notes (Why These Slides Are Bad)
These files contain detailed notes from Colin/Neha calls that discuss slide quality issues:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/02_transcript1_detailed_notes.md`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/03_transcript2_detailed_notes.md`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/04_combined_transcript_analysis.md`

### Master Tracker (For Context on What's Being Built vs Skipped)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/planning/02_master_slide_tracker.md`

## The 18 Flagged Slides

### Group 1: "All Suck" (Colin's words)
| Slide | Title |
|-------|-------|
| 06 | Location Footprint (global map) |
| 07 | Awards & Recognition |
| 08 | BayOne Diversity (46% women, 11% POC, 2% veterans) |

### Group 2: "All Awful" (Colin's words)
| Slide | Title |
|-------|-------|
| 15 | High Level Support Process Flow (L0-L3) |
| 16 | Communication Model (WIP) |
| 17 | BayOne Escalation Matrix (4 levels) |
| 18 | Managed Service Governance & Reporting |
| 19 | Proposed Coverage (PST time-based matrix) |
| 20 | Assumptions (WIP) |
| 25 | Metrics & Reporting (KPIs) |
| 35 | Case Study 4 -- C-Worker Transformation |
| 38 | Sample Profiles -- Team Lead/L1 |
| 39 | Sample Profiles -- L1 Support Engineers |
| 40 | Blank |
| 41 | Learning & Development Platforms |
| 42 | Better Service Management (360-degree engagement) |
| 43 | Commitment to DEI (title only) |
| 44 | Mom Relaunch Program |

## Instructions (Follow This Order)

### Step 1: Read Transcript Notes
Use parallel explore agents to read all three transcript research files listed above. Understand the context of WHY these slides are being cut. Look for specific mentions of:
- Suva and the L&D platform ($30K unused platform, SharePoint with 2 logins)
- "Boys' club" content that doesn't add value
- WIP placeholders with no real substance
- Content that makes BayOne look like a staffing company rather than a solutions vendor
- Slides that are generic filler rather than McGrath-specific
- The Sarang lesson: don't make indefensible claims

### Step 2: Examine Each Flagged Slide
For each of the 18 slides, read ALL four files in its folder (content.md, layout.md, visual_elements.md, and the PNG screenshot). Use parallel agents where possible to speed this up.

### Step 3: Write the Autopsy Report
Create a detailed report at:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/05_bad_slide_autopsy.md`

For each slide, document:
1. **What it shows** -- Brief description of the slide content
2. **What's wrong with it** -- Be specific and brutal. Categories to consider:
   - Is it generic filler? (Could apply to any company, says nothing about McGrath)
   - Is it WIP/incomplete? (Placeholder content, TODO items)
   - Is it visually bad? (Cluttered, poor layout, ugly)
   - Is it strategically misguided? (Positions BayOne as staffing company, makes weak claims)
   - Is it irrelevant? (Doesn't belong in an RFP response)
   - Is it connected to internal dysfunction? (Suva's L&D, etc.)
   - Is it duplicative? (Says the same thing as another slide)
3. **Anti-pattern extracted** -- A generalizable principle (e.g., "Don't include slides that are obviously WIP with TODO lists" or "Don't pad the deck with generic corporate culture slides that aren't tailored to the client")

### Step 4: Write the Anti-Patterns Summary
At the end of the report, create a consolidated list of all anti-patterns found, organized by category. This becomes the "DON'T DO THIS" reference for building sessions.

## Rules
- Use parallel explore agents to read files efficiently
- Persist your work to files as you go -- don't wait until the end
- Use simple `scratchpad.py` scripts if you need Python for anything; never heredocs or `python -c`
- Do not make changes to any source files
- Be thorough but also direct -- don't pull punches in your analysis
- If you see patterns that apply to slides BEYOND the 18 flagged ones, note them
