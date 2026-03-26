# Handoff: Ariat Crossover Comparison

## Purpose

You are a research analyst comparing two extracted PowerPoint decks to identify where the Ariat deck has better content than the McGrath deck for overlapping slides. Your output will guide future slide-building sessions on which source to prefer for each slide.

This is a research and documentation task. You are NOT building or fixing slides.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RFP response deck as HTML slides. The original McGrath deck (made by Amit) is poor quality. There is a separate, better deck that was created for an Ariat engagement (edited by Colin, Director of AI). Several slides overlap in topic between the two decks. Where overlap exists, the Ariat version is generally better and should be the preferred content reference.

Additionally, three Ariat slides were already rebuilt as exemplary HTML -- these represent the absolute gold standard of what the final slides should look like.

### Who You Can Ask
If you have questions, tell the user -- they are the orchestrator for this project.

## Source Material

### McGrath Deck (The Bad One)
**Base path:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/`

Each slide: `slide_NN/content.md`, `slide_NN/layout.md`, `slide_NN/visual_elements.md`, `slide_NN/slide_NN.png`

### Ariat Deck (The Better One)
**Base path:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/`

Same structure: `slide_NN/content.md`, `slide_NN/layout.md`, `slide_NN/visual_elements.md`, `slide_NN/slide_NN.png`

### HTML Gold Standards (Best of the Best)
These are completed HTML slides that represent the target quality:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_02_enterprise_ai_solutions.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_03_quality_engineering.html`

These map to Ariat slides 10, 11, 12 respectively.

### Existing Crossover Mapping (Starting Point)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/01_ariat_crossover_mapping.md`

This was created by the orchestrator based on high-level summaries. Your job is to validate and deepen this with actual side-by-side content comparison.

### Master Tracker
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/planning/02_master_slide_tracker.md`

Only slides marked BUILD matter. Skip anything marked SKIP.

## Known Crossover Pairs (To Validate and Expand)

| McGrath | McGrath Title | Ariat | Ariat Title |
|---------|---------------|-------|-------------|
| 01 | Title Slide | 01 | #TheFutureWorksHere |
| 02 | About BayOne (stats) | 01 | Intro (has stats) |
| 03 | Client Logos | 02 | BayOne helps transform companies |
| 04 | Technology Stack | 03 | Technology Stack |
| 05 | Service Offerings (6 lines) | 04 | Services (8 lines) |
| 09 | Make Tech Purple | 09 | Make Tech Purple |
| 24 | AI Enablement (WIP) | 10 | AI Strategy and Innovation |
| 37 | BayOne's Advantage (7 items) | 06 | Why BayOne? (6 items) |
| 45 | Closing | 19 | Closing |

There may also be Ariat slides with NO McGrath equivalent that could be added:
- Ariat 05: Partnership Models
- Ariat 07: Key Differentiators
- Ariat 11: Enterprise AI Solutions
- Ariat 12: Quality Engineering

## Instructions (Follow This Order)

### Step 1: Read Both Decks
Use parallel explore agents to read the content of all crossover slides from BOTH decks. For each pair, read content.md and look at the PNG screenshot from both decks. Also read the three HTML gold standard files.

### Step 2: Read the Existing Mapping
Read `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/01_ariat_crossover_mapping.md` to understand what the orchestrator already identified.

### Step 3: Side-by-Side Comparison
For each crossover pair, create a detailed comparison. Write your findings to:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/06_ariat_crossover_detailed.md`

For each pair, document:
1. **Content comparison** -- What does each version say? What's different?
2. **Quality comparison** -- Which is more detailed, more professional, more persuasive?
3. **Recommendation** -- Which version should be the primary source? Or should they be merged?
4. **Specific content to pull** -- If the Ariat version is better, what specific text/data should the builder use?
5. **McGrath-specific adaptations needed** -- Even if Ariat content is better, what needs to change to make it McGrath-specific?

### Step 4: Identify Ariat Additions
Look at Ariat slides that have NO McGrath equivalent (especially 05, 07, 11, 12). Assess whether any of these should be ADDED to the McGrath deck. Document your reasoning.

### Step 5: Updated Crossover Map
At the end of your report, provide an updated and validated crossover map with clear recommendations.

## Rules
- Use parallel explore agents to read files efficiently
- Persist your work to files as you go
- Use simple `scratchpad.py` scripts if needed; never heredocs or `python -c`
- Do not modify any source files
- Be specific in your comparisons -- don't just say "Ariat is better," explain exactly what's better and what the builder should use
- Remember: the HTML gold standards are the target quality level. Reference them as the benchmark.
