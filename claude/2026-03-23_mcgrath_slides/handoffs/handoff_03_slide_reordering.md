# Handoff: Slide Reordering & Flow Analysis

## Purpose

You are an information architecture analyst reviewing the 30 slides marked for BUILD in a McGrath RFP response deck. Your job is to read every slide's content, understand the narrative arc of the deck, and propose a better ordering that tells a more logical and compelling story. You should also identify slides that could be combined.

This is a research and documentation task. You are NOT building or fixing slides.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RFP response deck. The original was created by Amit and has poor organization. Colin (Director of AI) has already noted that the flow is illogical and that some slides should be combined (specifically slides 14 + 24). 18 slides have been flagged to skip, leaving 30 to build. The remaining 30 need a better narrative structure.

### Key Insight from Colin
- **Slides 14 (Transformation Journey) and 24 (AI Enablement)** should probably be combined. Slide 14 is "today vs tomorrow" and slide 24 is AI strategy -- the transformation narrative and AI story naturally go together.
- **Slide 24 is Colin's slide** -- he's Director of AI and is the only one qualified to own the AI content. It currently has WIP placeholder content from someone else.
- The deck should position BayOne as a **niche AI-enabled solutions vendor**, NOT a staffing company.
- The AI story is THE key differentiator for this proposal.

### Who You Can Ask
If you have questions, tell the user -- they are the orchestrator.

## Source Material

### Extracted PPTX
**Base path:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/`

Each slide: `slide_NN/content.md`, `slide_NN/layout.md`, `slide_NN/visual_elements.md`, `slide_NN/slide_NN.png`

### Master Tracker (Which Slides to Analyze)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/planning/02_master_slide_tracker.md`

### Transcript Analysis (Strategic Context)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/04_combined_transcript_analysis.md`

### User Feedback & Guidelines
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/decisions/00_user_feedback_and_guidelines.md`

## The 30 BUILD Slides (Current Order)

| Current # | Title | Section |
|-----------|-------|---------|
| 01 | Title Slide -- Response to McGrath | Intro |
| 02 | About BayOne (stats) | Intro |
| 03 | Client Logos | Intro |
| 04 | Technology Stack | Intro |
| 05 | Service Offerings (6 lines) | Intro |
| 09 | Make Tech Purple | Intro |
| 10 | Support Proposal Solution (divider) | Solution |
| 11 | Exec Summary (WIP) | Solution |
| 12 | Solution Summary (WIP) | Solution |
| 13 | RFP Scope Summary | Solution |
| 14 | Transformation Journey | Solution |
| 21 | Phase 1 Discovery (divider) | Delivery |
| 22 | Operational Maturity (4 phases) | Delivery |
| 23 | Service Quality Audit Process | Delivery |
| 24 | AI Enablement (WIP) | Delivery |
| 26 | Risks & Mitigation Part 1 | Delivery |
| 27 | Risks & Mitigation Part 2 | Delivery |
| 28 | Key Asks (4 from McGrath) | Delivery |
| 29 | Summary (3 pillars) | Delivery |
| 30 | Why BayOne? (divider) | Proof |
| 31 | Case Study Title -- Oracle HCM | Proof |
| 32 | Case Study 1 -- Oracle Fusion HCM | Proof |
| 33 | Case Study 2 -- Oracle ERP Reporting | Proof |
| 34 | Case Study 3 -- Oracle EBS Support | Proof |
| 36 | Managed Service Commercials (pricing) | Commercial |
| 37 | BayOne's Advantage (7 items) | Commercial |
| 45 | Closing / Call to Action | Closing |
| 46 | Measurement By Metrics (10 KPIs) | Operations |
| 47 | Prerequisites (WIP) | Operations |
| 48 | BayOne Operations Snapshot (WIP) | Operations |

## Instructions (Follow This Order)

### Step 1: Read Context Documents
Use parallel explore agents to read:
- The master tracker
- The combined transcript analysis
- The user feedback and guidelines doc

Understand the strategic context: what story is BayOne trying to tell? What matters most to McGrath?

### Step 2: Read Every BUILD Slide
Read the content.md and look at the screenshot (PNG) for ALL 30 BUILD slides. Use parallel agents to do this efficiently. You need to understand what each slide actually contains to propose a better flow.

### Step 3: Analyze the Current Flow
Document your analysis of the current ordering. What works? What doesn't? Where are the narrative breaks?

Consider:
- Does the deck open strong? Does it hook McGrath quickly?
- Is the "who we are" section too long before getting to "what we'll do for you"?
- Is the AI story (BayOne's key differentiator) buried too deep?
- Do the case studies appear at the right moment?
- Are the section divider slides (10, 21, 30) placed well?
- Does the deck build toward a natural close?
- Are there slides that feel out of place in their current position?
- The operations slides (46, 47, 48) are at the very end -- should they be?

### Step 4: Propose New Ordering
Write your full analysis and proposal to:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/07_slide_reordering_proposal.md`

Your proposal should include:
1. **Current flow analysis** -- What's wrong with the current order
2. **Proposed new flow** -- A renumbered sequence with section groupings and rationale for each move
3. **Combination candidates** -- Slides that should be merged (14+24 is already flagged; are there others?)
4. **Narrative arc** -- A 2-3 sentence description of the story the deck should tell
5. **Section structure** -- Proposed sections with clear names and purposes
6. **Slides that might be missing** -- Based on the Ariat crossover mapping (`research/01_ariat_crossover_mapping.md`), are there Ariat-only slides that should be added to strengthen the flow?

### Step 5: Impact on Skipped Slides
Briefly note whether ANY of the 18 skipped slides contain content that actually should be part of the flow (just in a better form). Don't second-guess the skip decisions, but flag if reordering reveals a gap.

## Rules
- Use parallel explore agents to read files efficiently
- Persist your work to files as you go
- Use simple `scratchpad.py` scripts if needed; never heredocs or `python -c`
- Do not modify any source files
- Think like a presentation strategist, not just an organizer -- the ORDER tells a story
- The AI story should be prominent, not buried
- Remember: slide 36 (pricing) content is hands-off -- don't suggest changes to pricing/capacity content
- Do NOT make final decisions -- propose and explain. The orchestrator and Colin will decide.
