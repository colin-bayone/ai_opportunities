# McGrath RFP Slide Deck Rebuild -- Methodology

## Overview

We are rebuilding Amit's WIP PowerPoint deck for the McGrath RFP response as high-fidelity HTML slides using BayOne's established design system. This session (the ORCHESTRATOR) coordinates parallel Claude sessions that each handle a chunk of slides.

## Orchestrator Role

**This session does NOT build slides.** This session:
- Triages and plans the work
- Creates detailed handoff documents for worker sessions
- Creates kickoff prompts (copy-pasteable) that tell new Claude sessions about their handoff doc
- Guides, mentors, and coordinates worker sessions
- Reviews and assembles completed work

Worker sessions do the actual slide building. Each worker gets a handoff doc + kickoff prompt.

## Key Terminology

- **Handoff doc:** A highly detailed, comprehensive document providing context, background, purpose, guidelines, and instructions (not exact step-by-step commands) to the next Claude session. Contains paths to needed files and instructions on what other sessions are doing. Rich enough that the worker can operate autonomously.
- **Kickoff prompt:** A copy-pasteable prompt to start a new Claude session, pointing it to the handoff doc and getting it going.

## Important Context

- **Coworker Neha** is collaborating with Colin on this deck rebuild; she has feedback on what to fix
- The existing deck was made by **Amit** and needs significant visual and content improvement
- We previously built exemplary HTML slides for an Ariat engagement -- those are the gold standard
- The design system (layouts, UI catalog) is a **starting collection, not exhaustive** -- workers may need to expand and create new components as needed
- Colin had a call with Neha about criticisms of the existing deck; some slides will be fully removed

## Source Material

### Original PPTX (Extracted)
- **Location:** `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/`
- **Total slides:** 48
- **Per slide:** `slide_NN/content.md`, `slide_NN/layout.md`, `slide_NN/visual_elements.md`, `slide_NN/slide_NN.png`
- **Index:** `index.md` at root of extraction folder

### Design System Reference
- **Foundational slides (exemplary quality):** `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_enterprise_ai_solutions.html`, `slide_03_quality_engineering.html`
- **Page layout templates (9):** `claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`
- **UI component library (24+):** `claude/2026-03-03_ariat_slides/ui_catalog/*_*.html`

### McGrath RFP Context
- **RFP analysis & data:** `mcgrath/rfp_docs/final/` (architecture.md, requirements CSVs, SLA/KPI data)
- **Questions developed:** `mcgrath/questions/`
- **Gap analysis:** `mcgrath/analysis/`

## Workflow

### Phase 1: Triage (This Session)
1. Review all 48 slides
2. Mark each as: KEEP, REMOVE, MERGE, or REWORK
3. Incorporate feedback from Neha call
4. Establish final slide list and groupings for parallel work

### Phase 2: Handoff Creation (This Session)
1. Group slides into parallel chunks (3-5 slides per chunk)
2. Create detailed handoff documents in `handoffs/` with:
   - Full context and purpose
   - Paths to all needed files (source slides, design system, RFP data)
   - Slide-by-slide guidance (what to keep, what to change, layout suggestions)
   - Design system rules and patterns
   - Instructions for the worker session
3. Create kickoff prompts (copy-pasteable) for each handoff

### Phase 3: Parallel Execution (Worker Sessions)
- Each worker session receives a kickoff prompt pointing to its handoff doc
- Workers read the handoff, explore referenced files using parallel agents
- Workers build slides as standalone HTML files in `slides_output/`
- Workers persist knowledge in scratchpad files, never heredocs
- Workers can prototype alternatives as standalone HTML if designs need iteration
- Workers report back to orchestrator with questions
- **Workers never modify source content without explicit approval**

### Phase 4: Assembly & Review (This Session)
- Collect completed slides from all workers
- Review for consistency across chunks
- Final ordering and numbering
- Any cross-slide adjustments

## Design System Rules (For Handoffs)

### Canvas
- Aspect ratio: 16/10 (widescreen)
- Max-width: 1100px
- Background: Linear gradient white to light purple
- Border radius: 12px

### Colors (Purple Gradient Palette)
- `#2e1065` (darkest) -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` (accent) -> `#e879f9` (glow)
- Neutrals: `#0f172a` (dark text), `#334155` (body), `#64748b` (secondary), `#e2e8f0` (border)

### Typography
- Font: Inter (300, 400, 500, 600, 700)
- Headlines: 24-28px bold
- Lead text: 12-15px light gray
- Body: 11-12px
- Labels: 10-11px uppercase letter-spaced

### Standard Slide Structure
```
slide-header (logo + context label)
slide-content (main area)
slide-footer (gradient bar + slide number)
```

### Icons
- Font Awesome 6.5.1 (CDN)
- Icon boxes: 36-48px with gradient backgrounds, border-radius 8-12px

### Key Patterns
- Gradient text on large headlines
- Accent bars (top or left, 3-4px) on cards
- CSS Grid for multi-item layouts, Flexbox for alignment
- Box shadows: subtle (0 2px 8px rgba(0,0,0,0.06))

## CRITICAL: PPTX Extraction Limitation

The PPTX extractor's markdown files (content.md) sometimes FAIL to capture table/grid content. They may show only a slide title when the actual slide has dense content (tables, multi-column layouts, etc.). **The PNG screenshots are the source of truth.** Workers MUST always read the PNG images, not rely solely on content.md.

### Previously Bad Extractions (RE-EXTRACTED, now fixed)
- **Slide 21** -- Was missing 4 detailed phases with responsibilities/timelines. Re-extracted by pptx-extractor session.
- **Slide 30** -- Was missing expertise columns + execution readiness. Re-extracted.
- **Slide 31** -- Was missing full case study content. Re-extracted.

### Verified Accurate Extractions
Slides 10, 11, 12, 22, 32, 33, 34, 36, 37 all have accurate markdown matching their PNGs.

## Worker Session Rules

1. Follow instructions in the exact order specified in the handoff
2. Use parallel explore agents to read referenced files
3. Persist knowledge in files (never heredocs or python -c)
4. Use simple `scratchpad.py` scripts when Python work is needed
5. Never make unilateral decisions -- ask the user or report back
6. Never modify provided content unless user approves
7. Can prototype alternative designs as standalone HTML files
8. Output slides to `claude/2026-03-23_mcgrath_slides/slides_output/`
9. Workers know they can report back to the orchestrator / ask questions
10. The UI catalog and page layouts are a starting collection, not exhaustive -- workers can and should create new components/layouts when the existing ones don't fit
11. **Always read the PNG screenshot of the source slide** -- content.md is sometimes incomplete (see PPTX Extraction Limitation above)
12. **Visually inspect your output before declaring done.** Run a Playwright screenshot and compare to the source. If the source has visual richness and yours has uniform rectangles, something is wrong.
13. **Flag image-dependent slides upfront.** If a slide's value comes from images/logos/photos that can't be reproduced in HTML, tell the user immediately rather than building a bad substitute. Some slides should use the PPTX directly.

## Lessons from First Build Session (planning/04_slide_build_feedback.md)

### What Works in HTML
- Split-screen layouts with purple gradient panels
- Stats bars with gradient text numbers
- Frosted-glass icon grids as visual panel substitutes for photos
- Pill badges with gradient backgrounds
- Hero-style brand rows (no standard header for title slides)

### What Does NOT Work in HTML
- **Logo slides.** Text names in boxes are not logos. The entire point is brand recognition at a glance. Use PPTX directly or source actual logo images.
- Subtle CSS differences (1px font weight, 1px size) for hierarchy -- invisible at presentation scale
- Uniform identical containers for varied content -- looks like a spreadsheet
- Empty grid cells -- draw attention to incompleteness

## Lessons from Second Build Session (handoffs/handoff_07_results.md)

### Workflow That Works
- **Build, screenshot, compare to gold standard, iterate.** Catch sparseness and formatting issues BEFORE presenting to user.
- **Parallel explore agents for content enrichment.** 3 agents searching different doc locations simultaneously returned comprehensive RFP detail in ~90 seconds. Builders should proactively search `mcgrath/` for supporting content.
- **Icon planning up front.** Map all icons in a table before writing HTML -- eliminates duplicate-icon bugs.
- **Asymmetric grid rows** (`grid-template-rows: 3fr 4fr`) solve uneven content density across cards.

### Mistakes to Avoid
- **Check CLAUDE.md formatting rules** before outputting text (em dashes caught in slide 04).
- **Don't present sparse first drafts.** If gold standard cards have 3-4 items and yours has 1, fix it before showing user.
- **Proactively search project docs** for supporting content -- don't wait to be told.
- **Remove internal boilerplate** (footnotes, WIP markers, annotations) without being asked.

## Lessons from Third Build Session (planning/05_exec_summary_build_report.md)

### Content Quality
- **No em dashes.** Handoff content may contain them -- rewrite with commas, colons, periods, or parentheses before building.
- **No contrastive rhetorical framing.** Remove "not X" patterns ("not bolted on", "not an afterthought"). Rewrite as direct positive statements.
- **No colloquial language.** Remove: "bolted on", "keeping the lights on", "call it a solution", "slide-deck promises."
- **No zero-value badges/labels.** Remove: "Looking ahead:", "Our commitment:", "In Practice" badges. Don't label what is obvious.

### Workflow
- **Do NOT run Playwright unless Colin explicitly asks.** This was repeated three times in session 3.
- **Change ONLY what is requested.** If asked to move one element, do not also change backgrounds, headers, or other sections. If a related change seems necessary, ask first.
- **Don't play gradient whack-a-mole.** When the simple answer is "gray on one section, white everywhere else," don't iterate through four complex alternatives. Ask for clarification before iterating.
