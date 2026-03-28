# User Feedback & Guidelines

## Captured from Colin, 2026-03-23

### Orchestrator Role (THIS Session)
- This session is the ORCHESTRATOR -- it does NOT build slides
- We create detailed handoffs and kickoff docs, guide/mentor worker sessions
- We coordinate, review, and assemble -- we do not execute

### Handoff Documents
- Highly detailed, comprehensive documents
- Must include: context, background, purpose, guidelines, and instructions (not exact step-by-step commands)
- Must contain paths to all needed files
- Must explain what other Claude sessions are doing
- Workers should know they can report back / ask questions

### Kickoff Prompts
- Copy-pasteable prompt for a new Claude session
- Points the session to its handoff doc and gets it started
- Simple and direct

### Worker Session Rules
- Use parallel explore agents to read files
- Persist knowledge in files -- never lose work
- Use simple `scratchpad.py` scripts for Python work; NEVER heredocs or `python -c` commands
- Follow instructions in the exact order specified
- Do NOT make decisions unilaterally
- Can prototype new designs as standalone simple HTML files if user doesn't like a component
- NEVER make changes to provided content unless user says it's approved

### Design System
- The UI catalog and page layouts are a STARTING collection, not exhaustive
- Workers will certainly need to add to and expand on them
- They represent things we've liked over time, not limits

### Content Approach
- Each slide has: an image of the original slide + markdown decomposition from PPTX extractor
- We rebuild slide by slide with MUCH better visual flair
- Some slides will be fully removed (triage needed before handoffs)
- The Ariat PPTX (`BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/`) is a better deck with crossover slides -- use as preferred reference where applicable
- The "other slides" referenced in transcripts = Ariat slides

### Pattern Recognition Rule
- If Colin doesn't want something in one slide, CHECK FOR THE SAME PATTERN across all slides
- Don't assume feedback is isolated to a single occurrence
- Apply criticisms broadly as principles, not one-off fixes

### Triage Decisions (2026-03-23)

**"SKIP" means skip for now -- not delete.** No reason to remove anything. We just focus on other slides first. Skipped slides may be revisited later.

**Slides 06, 07, 08** -- Colin: "all suck"
- 06: Location Footprint
- 07: Awards & Recognition
- 08: BayOne Diversity

**Slides 15, 16, 17, 18, 19, 20, 25, 35, 38, 39, 40, 41, 42, 43, 44** -- Colin: "all awful and should be removed"
- 15: Support Process Flow
- 16: Communication Model
- 17: Escalation Matrix
- 18: Governance & Reporting
- 19: Proposed Coverage
- 20: Assumptions
- 25: Metrics & Reporting
- 35: Case Study 4 (C-Worker)
- 38-39: Sample Profiles
- 40: Blank slide
- 41: L&D Platforms
- 42: Service Management
- 43: DEI divider
- 44: Mom Relaunch

**Result:** 30 slides to BUILD, 18 to SKIP

**Colin's note:** The Neha/Colin transcripts specifically discuss why these slides are bad. An early worker session should investigate and document the anti-patterns.

### Slide Ownership & Reorganization Notes (2026-03-23)
- **Slide 24 (AI Enablement, WIP)** -- Colin's slide. He is Director of AI and is the only one qualified to fix this. Someone else wrote it and it needs significant rework. The Ariat version (slide 10 = AI Strategy and Innovation) is dramatically better, plus there's an HTML gold standard.
- **Slide 14 (Transformation Journey)** -- Colin says this "likely should be" his too.
- **Slides 24 + 14** -- Colin says these "can probably be combined." (24 = AI Enablement WIP, 14 = Transformation Journey today-vs-tomorrow)
- The deck flow needs reorganization -- current order is not logical. A session should analyze and propose reordering.

### Pricing / Capacity -- Hands Off
- Colin will NOT touch anything pricing or capacity related. Slide 36 (Managed Service Commercials) and any staffing/pricing content stays as-is. "Whoever made that bed can lay in it."
- Workers should build slide 36 faithfully from the existing content without corrections.

### Early Session Strategy
1. **Bad Slide Autopsy session** -- Investigate the 18 skipped slides, read their extracted content, and document exactly why they're bad. Creates an anti-patterns reference so we know what NOT to do.
2. **Ariat Crossover Comparison session** -- Cross-compare Ariat deck slides against McGrath deck slides to identify where Ariat content is better and should be preferred.
3. **Slide Reordering session** -- Read all 30 BUILD slides and propose a more logical flow/organization. Also flag slides that could be combined (like 24+13).

### Key People
- **Colin** -- Director of AI, technical lead, orchestrating this work
- **Neha** -- Coworker collaborating on the deck rebuild, has criticisms of existing deck
- **Amit** -- Made the original (bad) deck; not adding value per transcripts
