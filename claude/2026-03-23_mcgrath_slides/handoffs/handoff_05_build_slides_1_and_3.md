# Handoff: Build Slides 1 and 3 (Title + Client Logos)

## Purpose

You are building the first two HTML slides for a McGrath RFP response deck. This is the first build session -- your work sets the tone and establishes patterns for all subsequent slide builders.

**You are building two slides:**
1. **Slide 1: Title + About BayOne** (merged from original slides 01 and 02)
2. **Slide 3: Client Logos**

These are the opening and credibility slides. They need to look polished, professional, and immediately communicate that BayOne is a serious solutions vendor -- not a staffing company.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck as high-fidelity HTML slides. The original PowerPoint (made by a coworker named Amit) is poor quality. Colin (Director of AI) is orchestrating the rebuild across parallel Claude sessions. You are the first builder.

### What Came Before You
Research sessions have already completed:
- Bad slide autopsy (what NOT to do): `claude/2026-03-23_mcgrath_slides/research/05_bad_slide_autopsy.md`
- Ariat crossover comparison (which content to use): `claude/2026-03-23_mcgrath_slides/research/06_ariat_crossover_detailed.md`
- Slide reordering proposal: `claude/2026-03-23_mcgrath_slides/research/07_slide_reordering_proposal.md`
- Full research synthesis: `claude/2026-03-23_mcgrath_slides/planning/03_research_synthesis.md`

### Who You Can Ask
Tell the user if you have questions -- they are the orchestrator and can help.

## Design System

### The Gold Standard (READ THESE FIRST)
These three HTML files represent the target quality. Read all three before you start building. They establish the visual language, component patterns, and level of polish you're aiming for:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_02_enterprise_ai_solutions.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_03_quality_engineering.html`

### Page Layout Templates (9 options)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`

Scan these to find layouts that fit your slides. Key candidates:
- `layout_hero_stat.html` -- Could work for the title slide's stats bar
- `layout_split_screen.html` -- Left panel with text + right panel with image (good for title slide)

### UI Component Library (24+ components)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/ui_catalog/`

Browse for useful components. These are a starting collection, not exhaustive -- you can and should create new patterns when these don't fit.

### Core Design Rules
- **Canvas:** 16:10 aspect ratio, max-width 1100px, white-to-light-purple gradient background, border-radius 12px
- **Colors:** Purple gradient palette: `#2e1065` (darkest) -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` (accent) -> `#e879f9` (glow). Neutrals: `#0f172a` (dark text), `#334155` (body), `#64748b` (secondary), `#e2e8f0` (border)
- **Typography:** Inter font (300-700 weights). Headlines 24-28px bold, Lead 12-15px, Body 11-12px, Labels 10-11px uppercase letter-spaced
- **Icons:** Font Awesome 6.5.1 CDN. Icon boxes 36-48px with gradient backgrounds, border-radius 8-12px
- **Standard structure:** slide-header (logo + context label) / slide-content (main area) / slide-footer (gradient bar + slide number)

## Slide 1: Title + About BayOne

### What You're Building
A single slide that merges the original title slide (McGrath 01) and the About BayOne stats slide (McGrath 02). Use **Ariat slide 01** as the primary source -- it already does this merge beautifully.

### Source Material
**Primary source (Ariat 01):**
- Extract: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_01/`
- Read both `content.md` AND the PNG screenshot

**Secondary sources (original McGrath slides):**
- McGrath 01: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_01/`
- McGrath 02: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_02/`

### Content to Include
From the crossover analysis (research/06):
- **Title:** Reference McGrath specifically (e.g., "McGrath Support Proposal" or "Response to McGrath Support Proposal")
- **Elevator pitch:** "BayOne is a global Talent and Technology Solutions partner headquartered in the San Francisco Bay Area. We solve business problems, bridge talent gaps, and drive innovation for customers."
- **Stats bar:** 100+ customers, **1,000+ projects** (use Ariat's number, not McGrath's 750+), 13 years, Global Presence
- **Branding:** BayOne logo prominent, McGrath logo should appear
- **Layout concept:** Ariat 01 uses left text / right team photo / stats bar at bottom. This pattern works well.
- **#TheFutureWorksHere** tagline

### What NOT to Do
- Don't make it plain white with just logos (that's what McGrath 01 was -- bare minimum)
- Don't create two separate slides -- this is ONE merged slide
- Don't use "750+ projects" -- use "1,000+ projects"

---

## Slide 3: Client Logos

### What You're Building
A logo grid showing BayOne's impressive client roster, with the "90% referral" message. Use **Ariat slide 02** as the primary source.

### Source Material
**Primary source (Ariat 02):**
- Extract: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_02/`
- Read both `content.md` AND the PNG screenshot

**Secondary source (McGrath 03):**
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_03/`

### Content to Include
From the crossover analysis (research/06):
- **Title:** "BayOne helps transform companies"
- **Logo grid:** Use Ariat 02's more current logo set (includes Netflix, GE, Atlassian, Workday, HPE, SoFi, Levi's, etc.)
- **Referral message:** "We follow a customer-centric approach. 90% of all our customers have been through direct referrals!" -- Ariat puts this in a highlighted bar at the bottom, which is more visually distinct

### Design Considerations
- Logo slides are inherently simple -- the design challenge is making a grid of logos feel polished rather than like a generic vendor brochure
- Consider how the gold standard slides handle visual hierarchy -- clean spacing, subtle gradients, professional typography
- The logos themselves will be represented as text names in styled boxes/cards (since we don't have actual logo image files). Make this look intentional and clean, not like a workaround.
- Or, if you can reference logos via a CDN or unicode/font approach, explore that

### What NOT to Do
- Don't make it feel like a staffing company's client list (the autopsy report, research/05, specifically calls this out)
- The framing should be "we transform companies" not "we supply workers to companies"

---

## Output

Write your HTML slides to:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_01_title.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_03_client_logos.html`

Each slide should be a standalone, self-contained HTML file (inline CSS, CDN references for fonts/icons) that can be opened in a browser.

## Rules
1. Read the three gold standard HTML slides FIRST, before anything else
2. Then read the Ariat source slides for your two slides
3. Then read the crossover analysis (research/06) for context on what content to use
4. Skim the anti-patterns summary (research/05) so you know what to avoid
5. Use parallel explore agents to read files efficiently
6. Persist your work -- save HTML files as you go, iterate
7. Use simple `scratchpad.py` scripts if you need Python; never heredocs or `python -c`
8. Do NOT modify any source files
9. Do NOT make content changes without user approval -- if you think the elevator pitch or stats should be different, ask first
10. If you don't like a component from the UI catalog, prototype alternatives as separate HTML files and ask the user
11. Always read PNG screenshots, not just content.md -- the markdown extraction sometimes misses table/grid content
