# Results: Build Slides 21-22

## Status: COMPLETE

All three slides built and output to `slides_output/`.

---

## Slide 21: Managed Service Commercials
**File:** `slides_output/slide_21_commercials.html`
**Slide number:** 21

### Design
- Purple gradient table header with white text
- Clean data row with all five columns: Phase 1, Year 1, Year 2, Year 3, Total Cost
- Total Cost cell has subtle purple background highlight
- Savings row uses pill badges with down-arrow icons for Year 2 (20%) and Year 3 (27%)
- Key Callouts section below with icon header and three bullet items

### Content
ALL pricing numbers preserved exactly from source (slide 36 PNG):
- Phase 1: $ 738,400
- Year 1: $ 4,867,200
- Year 2: $ 3,889,600
- Year 3: $ 2,828,800
- Total Cost: $ 12,344,800
- Year 2 savings 20%, Year 3 savings 27%
- Three Key Callouts reproduced verbatim

**No modifications made to any numbers or callout text.**

---

## Slide 22: Prerequisites
**File:** `slides_output/slide_22_prerequisites.html`
**Slide number:** 22

### Design
- Uses category-row pattern from slide 12 (KPI Metrics)
- Three grouped rows with icon + label on left, 2-column item grid on right
- Categories: System Access & Environments (4 items), Documentation & Data (3 items), People, Process & Governance (5 items)

### Content (12 items total)
Consolidated from slide 47 (9 original prerequisites) plus 3 items absorbed from slide 20 (assumptions) that were prerequisite-like in nature:
- Slide 47 #1 merged with slide 20 #11 (tool access consolidated)
- Slide 20 #8 (production replica), #9 (vendor coordination), #10 (knowledge transfer) moved here

### Removals
- "WIP" marker removed

---

## Slide 22b: Assumptions
**File:** `slides_output/slide_22b_assumptions.html`
**Slide number:** 22 (second assumptions slide, numbering TBD by orchestrator)

### Design
- Top section: "Volume and Complexity Baseline" card with 4-metric grid showing key numbers prominently
- Bottom section: Three condition cards in a 3-column grid (Discovery & Baselining, Resource Adjustments, Stakeholder Participation)

### Content (7 items)
Volume baseline metrics displayed as headline numbers:
- ~1,400 monthly L2/L3 tickets
- 30/50/20 complexity ratio (simple/medium/complex)
- 1/3/8 resolution hours
- < 10% P1/P2 volume

Engagement conditions:
- Discovery phase baselining with change request clause
- Resource count revision triggers (ticket deviation, integration count, Mulesoft/OIC migration)
- Stakeholder participation requirement

### Removals (approved by Colin)
- "COLA" (no context)
- "Neha to pull more assumptions" (internal annotation)
- "WIP" markers

---

## Decisions Made
- **Two slides** for prerequisites/assumptions (Colin approved the split)
- Three prerequisite-like items from slide 20 moved to slide 22 (Prerequisites)
- Overlap between slide 47 #1 and slide 20 #11 consolidated into single item
- All contractual protection language preserved (change request clause, resource revision triggers)
- "Most of the Mulesoft integration will migrate to OIC" kept per handoff guidance (flagged but retained)
