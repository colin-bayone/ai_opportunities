# Handoff: Build Slides 7-10 (Solution Completion + Delivery Start)

## Purpose

You are building four slides that complete the Solution section and begin the Delivery Approach section of the McGrath RFP response deck.

**Your slides:**
- **Slide 7: Solution Summary** (old slide 12) -- Outcomes table
- **Slide 8: BayOne Operations Snapshot** (old slide 48) -- Operational proof metrics
- **Slide 9: Phase 1 Discovery & Transition** (old slide 21) -- 4 phases with responsibilities
- **Slide 10: Operational Maturity & Value Transformation** (old slide 22) -- 4-phase roadmap with team sizing

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck as HTML slides. You are one of three parallel build sessions. The other two are building slides 11-17 (quality/KPIs/case studies) and slides 23-28 (closing section).

### Previously Built (Read for Quality Reference)
- `slides_output/slide_01_title.html` -- Title slide
- `slides_output/slide_04_section_divider.html` -- Dark gradient section divider
- `slides_output/slide_05_scope_summary.html` -- Card-based scope table (good density reference)
- `slides_output/slide_06a_transformation.html` -- Transformation journey
- `slides_output/slide_06b_ai_strategy.html` -- AI strategy cards

### Build Lessons (READ THESE)
- `planning/04_slide_build_feedback.md` -- Sessions 1-2 lessons
- `handoffs/handoff_07_results.md` -- Session 2 workflow lessons
- `planning/05_exec_summary_build_report.md` -- Session 3 lessons

### Key Rules (Distilled from Previous Sessions)
1. **Read gold standard slides first:** `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_*.html`, `slide_03_*.html`
2. **Proactively search `mcgrath/rfp_docs/`** for supporting detail. Don't wait to be told.
3. **Compare your output to gold standard before presenting.** If yours looks sparse, fix it first.
4. **No em dashes in regular prose.** Use commas, colons, periods, parentheses.
5. **No contrastive framing** ("not X", "not an afterthought"). Write direct positive statements.
6. **No Playwright unless Colin explicitly asks.**
7. **Change ONLY what is requested.** Don't overshoot.
8. **Plan icons up front** in a table before coding. No duplicates.
9. **Always read PNGs AND content.md.** The markdown extraction sometimes misses content. PNGs are source of truth.
10. **Remove WIP markers, internal annotations, and boilerplate** without being asked.

### Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700). Headlines 24-28px, Body 11-12px, Labels 10-11px
- **Icons:** Font Awesome 6.5.1 CDN
- **Structure:** slide-header / slide-content / slide-footer (gradient bar + number)
- **Layouts:** `claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`
- **Components:** `claude/2026-03-03_ariat_slides/ui_catalog/`

---

## Slide 7: Solution Summary (Old Slide 12)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_12/slide_12.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_12/content.md`

### What It Is
WIP outcomes table with two sections: "Expected Outcome & Metrics" (Business, Efficiency, Transformation rows) and "Key Enablers" (Industry Leadership, Process & Framework, Governance & People). Currently a basic table layout marked WIP.

### Design Approach
This is a structured data slide. Consider card-based layout or styled table. The content describes WHAT McGrath gets from the engagement. It follows the AI strategy slides, so it should feel like: "Here's what all that capability delivers in practice."

**Remove:** WIP marker. Enrich content from `mcgrath/rfp_docs/` if the existing bullets feel thin.

**Output:** `slides_output/slide_07_solution_summary.html` (slide number 07)

---

## Slide 8: BayOne Operations Snapshot (Old Slide 48)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_48/slide_48.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_48/content.md`

### What It Is
WIP operating metrics overview. Key stats: 100+ applications managed, 50+ P1/P2 apps, >5K tickets/quarter, >95% SLA adherence, >4.4 CSAT. Also covers operating model (100+ resources, 24x7, 90% offshore) and services/tech stack.

### Design Approach
This slide proves BayOne has operational muscle. Consider a stat-heavy layout: `layout_hero_stat.html` or `layout_proof_point.html` as starting points. Big numbers with supporting context. This closes Section 2 (The Solution) with credibility.

**Remove:** WIP marker. This is McGrath-agnostic proof of BayOne's operational capacity.

**Output:** `slides_output/slide_08_operations_snapshot.html` (slide number 08)

---

## Slide 9: Phase 1 Discovery & Transition (Old Slide 21)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_21/slide_21.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_21/content.md`

### CRITICAL: The content.md was re-extracted but still may not capture everything. The PNG is the source of truth.
The PNG shows 4 detailed phases: Preliminary, Knowledge Acquisition, Shadow Support, Reverse Shadow & Ownership. Each has responsibilities, timelines, and bullet points.

### Design Approach
This opens Section 3 (Delivery Approach). It's a phased timeline. Consider `layout_timeline_journey.html` or a custom 4-column/4-row layout. The chevron flow bar from the gold standard `slide_03_quality_engineering.html` could work well for the 4 phases.

**This is dense content.** The original has detailed responsibilities per phase. Preserve the detail, don't simplify it away.

**Output:** `slides_output/slide_09_phase1_discovery.html` (slide number 09)

---

## Slide 10: Operational Maturity & Value Transformation (Old Slide 22)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_22/slide_22.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_22/content.md`

### What It Is
4-phase roadmap: On-board (Q1), Stabilize (Y1), Optimize (Y2), Steady State (Y3). Shows team sizing progression (Onsite 9->9->6->3, Offshore 3->22->20->20) and workload distribution shifting from support-heavy to enhancement-focused. Automation reduces operational cases over time.

### Design Approach
Timeline or phased journey layout. The team sizing data and workload shift are the key visuals. Consider how to show the progression (numbers getting smaller onsite, bigger offshore, support shrinking, enhancements growing). This could use a timeline with stat callouts per phase.

**Pricing/capacity note:** This slide shows team sizing (headcount numbers). These are NOT pricing -- they are staffing model data from Amit's plan. Build them faithfully, do not modify.

**Output:** `slides_output/slide_10_operational_maturity.html` (slide number 10)

---

## Output Files
- `slides_output/slide_07_solution_summary.html`
- `slides_output/slide_08_operations_snapshot.html`
- `slides_output/slide_09_phase1_discovery.html`
- `slides_output/slide_10_operational_maturity.html`

## Rules
All standard rules from Key Rules section above. Additionally:
- You are one of three parallel sessions. Focus on YOUR slides.
- Write a results handoff when done at `handoffs/handoff_11_results.md` documenting what you built, design choices, and any issues.
