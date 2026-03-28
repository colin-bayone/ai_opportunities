# Handoff: Build Slides 4 and 5 (Section Divider + RFP Scope Summary)

## Purpose

You are building two HTML slides for a McGrath RFP response deck. These open Section 2: "The Solution" -- the transition from "who we are" to "what we'll do for you."

**You are building:**
1. **Slide 4: "Support Proposal Solution"** (section divider, originally slide 10)
2. **Slide 5: "RFP Scope Summary"** (originally slide 13)

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck as high-fidelity HTML slides. The original PowerPoint was poor quality. This is the second build session. The first session successfully built slide 01 (title) and learned important lessons documented below.

### What Came Before
- **Slide 01 (title)** is done: `slides_output/slide_01_title.html` -- APPROVED
- **Slide 03 (client logos)** will use the Ariat PPTX directly (logos can't be reproduced in HTML without image files)
- **Slide 02 (exec summary)** content is being drafted in a parallel session
- **Build feedback from session 1:** `claude/2026-03-23_mcgrath_slides/planning/04_slide_build_feedback.md` -- READ THIS. Contains critical lessons about what works and what doesn't in HTML slides.

### Who You Can Ask
Tell the user if you have questions -- they are the orchestrator.

## Design System

### The Gold Standard (READ FIRST)
These three HTML files set the quality bar. Read all three before building:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_02_enterprise_ai_solutions.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_03_quality_engineering.html`

### Also Read Slide 01 (Already Built)
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_01_title.html`

This was approved by Colin. Match its quality and visual language.

### Page Layout Templates
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`

For the scope summary slide, consider:
- `layout_two_column_detail_rows.html` -- Horizontal rows with left label + right content grid. Good for the in-scope services table.
- `layout_problem_solution.html` -- Could work with "In Scope" as the main section and "Out of Scope" / "Coverage" as secondary.

### UI Component Library
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/ui_catalog/`

### Core Design Rules
- **Canvas:** 16:10 aspect ratio, max-width 1100px, white-to-light-purple gradient background, border-radius 12px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`. Neutrals: `#0f172a`, `#334155`, `#64748b`, `#e2e8f0`
- **Typography:** Inter (300-700). Headlines 24-28px, Lead 12-15px, Body 11-12px, Labels 10-11px uppercase
- **Icons:** Font Awesome 6.5.1 CDN. Icon boxes 36-48px with gradient backgrounds
- **Standard structure:** slide-header (logo + context label) / slide-content / slide-footer (gradient bar + slide number)

---

## Slide 4: Section Divider -- "Support Proposal Solution"

### Source
- PNG: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_10/slide_10.png`

### What It Is
A section divider marking the start of "The Solution." The original is just centered text on a white background with the purple wave footer. It's bland.

### What to Build
A visually striking section divider that signals a shift from "here's who we are" to "here's what we'll do for McGrath." This should feel like a chapter break.

Design ideas (not prescriptive -- use your judgment):
- Large gradient text title centered
- Subtle background pattern or gradient to differentiate from content slides
- Could include a brief subtitle like "Our approach to McGrath's NextGen managed services" to bridge the narrative
- Keep it clean and purposeful -- section dividers should provide visual breathing room

### Content
- Title: "Support Proposal Solution" (or refine if you think a better title serves the narrative -- flag for user approval)
- Slide number: 04

---

## Slide 5: RFP Scope Summary

### Source
- PNG: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_13/slide_13.png`
- Content MD: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_13/content.md`

### What It Is
A scope summary showing what's in-scope and out-of-scope for the managed services engagement. Currently a purple-bordered table with 6 service rows, plus Coverage & SLAs and Out of Scope sections. Has a WIP marker and a red internal annotation.

### Content to Include (From the Original)

**Title:** "RFP Scope Summary -- Our Understanding"

**In Scope (6 services):**

| Service | Description |
|---------|-------------|
| Operational Support | Monitoring systems, managing integrations, restarting stuck workflows, ticket management |
| Enhancements | MVP backlog, Configuration improvements, changes with <40 hrs per unit efforts |
| Bug Fixes | Post go-live / implementation defects |
| Quarterly Releases & Testing | Oracle Fusion quarterly patches, regression testing, production validation |
| Integration Troubleshooting | Monitoring 50+ integrations, root cause analysis on failures, restarting stuck processes across the MuleSoft/OIC layer |
| Value Added Services | Automation & AI usage to create support efficiencies to reduce support effort |

**Coverage & SLAs:**
- 5 am -- 5 pm PST coverage
- 24 hrs P1 Support

**Out of Scope:**
- Engineering development (separate SOW)

**Footnote:** * As per the Specific Requirements worksheet in the RFP

### What to REMOVE
- **"WIP" marker** -- must not appear on the final slide
- **Red annotation text** ("Add SLA driven, App support, timeline, model, key applications") -- this is an internal instruction from Amit, not client-facing content

### What NOT to Change
- Do NOT modify the service descriptions or scope items. This is RFP-sourced content that Colin must approve changes to.
- Do NOT add pricing or capacity numbers.

### Design Approach
This is a table-heavy slide. The challenge is making a data table look polished and not like a spreadsheet. Consider:
- Card-based layout where each service gets its own card with an icon, bold service name, and description
- Or a clean table with accent bars/color coding per row
- Coverage & SLAs could be a highlighted callout bar at the bottom
- Out of Scope should be visually distinct (muted, separated) so it's clear what's excluded
- The "our understanding" subtitle signals this is based on current RFP info and subject to discovery refinement

### Slide Number
05

---

## Output

Write your HTML slides to:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_04_section_divider.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_05_scope_summary.html`

Each slide: standalone, self-contained HTML (inline CSS, CDN fonts/icons), opens in a browser.

## Rules
1. Read the three gold standard HTML slides and slide_01_title.html FIRST
2. Read the build feedback doc (`planning/04_slide_build_feedback.md`) for lessons from session 1
3. Read the source PNGs AND content.md for both slides
4. Browse layout templates and UI components for inspiration
5. Use parallel explore agents to read files efficiently
6. **Visually inspect your output** -- take a Playwright screenshot and compare to what a polished slide should look like
7. Use simple `scratchpad.py` scripts if needed; never heredocs or `python -c`
8. Do NOT modify source files
9. Do NOT change content without user approval
10. If you want to suggest a better title for the section divider, present it as an option for the user to approve
