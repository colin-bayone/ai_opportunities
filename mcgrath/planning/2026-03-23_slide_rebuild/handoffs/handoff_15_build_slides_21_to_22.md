# Handoff: Build Slides 21-22 (Commercial + Prerequisites/Assumptions)

## Purpose

You are building two slides covering the commercial terms section plus a content cleanup task.

**Your slides:**
- **Slide 21: Managed Service Commercials** (old slide 36) -- Pricing. HANDS OFF content.
- **Slide 22: Prerequisites + Assumptions** (old slides 47 and 20 combined) -- Engagement conditions

### CRITICAL: Slide 21 Pricing is HANDS OFF
Colin explicitly said: "I will NOT touch anything pricing or capacity related. Whoever made that bed can lay in it." Build slide 21 faithfully from the existing content. Do NOT modify, correct, or comment on pricing numbers, staffing counts, or cost figures.

### CRITICAL: Slide 22 Requires Content Cleanup
Slide 22 is built from TWO source slides:
- **Slide 47 (Prerequisites):** 9 prerequisites for service delivery (access, documentation, SPOCs, etc.)
- **Slide 20 (Assumptions):** Ticket volume baselines, complexity distribution, resource triggers (was SKIP but content is being salvaged)

Both are dense. You need to:
1. Read both slides fully
2. Identify overlap and deduplicate
3. Propose TWO crisp slides (or one combined slide if the content fits) that retain all important content
4. **Present to Colin for approval before finalizing.** He must directly approve any content removals.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. You are one of three parallel sessions in the final build wave.

### Previously Built
Browse `slides_output/` for quality reference. 20+ slides completed.

### Key Rules
1. **Read gold standard slides first**
2. **No em dashes.** No contrastive framing. No colloquial language.
3. **No Playwright unless Colin explicitly asks.**
4. **Always read PNGs AND content.md.** PNGs are source of truth.
5. **Remove WIP markers and internal annotations** (slide 20 has "Neha to pull more assumptions" in red and a WIP tag).
6. **Plan icons up front.**

### Design System
Standard BayOne design system. 16:10 canvas, max-width 1100px, purple gradient palette, Inter font, Font Awesome icons. See gold standards at `claude/2026-03-03_ariat_slides/foundational/`.

---

## Slide 21: Managed Service Commercials (Old Slide 36)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_36/slide_36.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_36/content.md`

### What It Is
Pricing breakdown: Phase 1 $738.4K, Year 1 $4.867M, Year 2 $3.890M (20% savings), Year 3 $2.829M (27% savings). Total 3-year cost: $12.344M. Key callouts about bundled pricing and year-over-year optimization.

### Rules
- **HANDS OFF.** Build the visual design, preserve ALL pricing content exactly.
- Do not modify, round, reformat, or annotate any numbers.
- Do not add commentary about whether pricing is appropriate.
- Design it professionally -- clean table or card layout with the numbers prominent.

**Output:** `slides_output/slide_21_commercials.html` (slide number 21)

---

## Slide 22: Prerequisites + Assumptions (Old Slides 47 + 20)

### Sources

**Slide 47 (Prerequisites):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_47/slide_47.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_47/content.md`

**Slide 20 (Assumptions -- being salvaged from SKIP):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_20/slide_20.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_20/content.md`

### What These Contain

**Slide 47 (Prerequisites, 9 items):** Access provisioning (Salesforce, CPQ, tools), documentation availability, named SPOCs, ticket history, integration documentation, CPQ details, sample datasets, security/compliance guidelines, release/deployment processes.

**Slide 20 (Assumptions, WIP):** Monthly ticket volume ~1,400 L2/L3, complexity distribution (30% simple, 50% medium, 20% complex), resolution efforts, P1/P2 < 10%, resource adjustments for deviations, KT sessions, production replica environment. Also has "Neha to pull more assumptions" in red and a "COLA" bullet with no context.

### Your Job
1. Read BOTH slides thoroughly (PNGs are source of truth)
2. List all content items from both slides
3. Identify overlap (e.g., KT sessions appears in both)
4. Propose a clean organization -- either:
   - **Two slides:** "Prerequisites" (what McGrath must provide) + "Assumptions" (what BayOne is basing estimates on)
   - **One slide:** If dedup makes it fit, combine into "Prerequisites & Assumptions"
5. **Remove:** WIP markers, "Neha to pull more assumptions", "COLA" with no context, any internal annotations
6. **Present original content and proposed reorganization to Colin.** He must approve before you finalize.

### Important
Assumptions protect BayOne contractually. Do not casually remove assumption items without flagging them. If something seems like legal cover (e.g., "resource adjustments if actual volumes deviate"), keep it and let Colin decide.

**Output:** `slides_output/slide_22_prerequisites.html` (and optionally `slide_22b_assumptions.html` if two slides)

---

## Output Files
- `slides_output/slide_21_commercials.html`
- `slides_output/slide_22_prerequisites.html`
- (optionally `slides_output/slide_22b_assumptions.html`)

Write a results handoff at `handoffs/handoff_15_results.md` when done.
