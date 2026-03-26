# Handoff: Combined Capacity Distribution Slide (Medium + High)

## Purpose

Combine two capacity distribution slides (Medium and High scenarios) into ONE beautiful, theme-compliant slide. This replaces the existing `slide_10_operational_maturity.html` in the deck (final position #16).

The two source slides have identical structure and key callouts, just different numbers. The design challenge is showing both scenarios clearly on one slide without it feeling cramped.

## Source Material

**Slide 21 (Medium scenario):**
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_21/content.md`
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_21/slide_21.png`

**Slide 22 (High scenario):**
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_22/content.md`
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_22/slide_22.png`

**Existing slide being replaced:**
- `claude/2026-03-23_mcgrath_slides/slides_output/slide_10_operational_maturity.html`

## Content: The Two Scenarios

### Shared Structure (4 phases)

| | Phase 1 (Q1) | Y1 Q1-Q4 | Y2 Q1-Q4 | Y3 Q1-Q4 |
|---|---|---|---|---|
| **Purpose** | Transition: onboarding, KT | Operate + Support | Optimize | Steady State |
| **Support vs Enhancement** | -- | 10% / 90% | 15% / 85% | 30% / 70% |

### Medium Scenario

| | Phase 1 (Q1) | Y1 Q1-Q4 | Y2 Q1-Q4 | Y3 Q1-Q4 |
|---|---|---|---|---|
| **Onsite** | 9 | 9 | 6 | 3 |
| **Offshore** | 3 | 22 | 20 | 18 |
| **Total** | 12 | 31 | 26 | 21 |
| **Tickets/qtr** | -- | ~3,300 | ~2,500 | ~1,800 |
| **Enh hours/qtr** | -- | 1,500 | 2,000 | 3,000 |

### High Scenario

| | Phase 1 (Q1) | Y1 Q1-Q4 | Y2 Q1-Q4 | Y3 Q1-Q4 |
|---|---|---|---|---|
| **Onsite** | 11 | 11 | 7 | 4 |
| **Offshore** | 12 | 26 | 24 | 18 |
| **Total** | 23 | 37 | 31 | 22 |
| **Tickets/qtr** | -- | ~3,900 | ~3,000 | ~1,800 |
| **Enh hours/qtr** | -- | 2,000 | 2,500 | 3,500 |

### Shared Key Callouts
- BayOne team will handle +/- 5% spikes (seasonal, month end, qtr end)
- Automation and process optimization to reduce operational case volume, enabling a shift toward enhancements and innovation
- One integrated team for all support services
- Resource count is indicative; excludes PMO and automation office
- Burst capacity (variable workforce) available for unexpected/unplanned spikes

### Legend
- Support (light/teal)
- Enhancement (dark blue)
- Burst Capacity (pink)

## Design Approach

This is a data-dense slide. The key visual story:
- **Both scenarios show the same trend:** onsite shrinks, offshore adjusts, tickets decrease, enhancement hours increase, support ratio shifts from 90% to 70%.
- **The difference is scale:** High starts with more people and more tickets.

Design directions to consider (present options to Colin):

1. **Two-row layout:** Medium scenario on top, High on bottom. Shared phase headers across the top. Compact cards or cells per phase. The shared callouts go in a footer bar.

2. **Side-by-side timelines:** Two horizontal timelines stacked, with phase columns aligned. Medium on top, High below, with a visual separator. Numbers in each cell.

3. **Tabular with visual bars:** One clean table with two rows per phase (Medium / High), with small stacked bar charts showing support vs enhancement ratios per phase.

4. **Phase cards with scenario tabs:** 4 phase cards across. Each card shows both Medium and High numbers with visual differentiation (e.g., Medium in purple, High in darker purple).

**The anti-patterns from the originals:** The PPTX versions use tiny person icons to represent headcount. This is cute but doesn't translate well to HTML and wastes space. Use numbers, not icons. The stacked bar charts showing support/enhancement split are a good concept but cramped in the original. Give them room.

**Present your concept to Colin before building.** This is a complex data slide.

## Context

### Previously Built
- Read existing `slide_10_operational_maturity.html` to understand what was built before
- Read other approved slides in `slides_output/` for design consistency
- Read gold standard slides at `claude/2026-03-03_ariat_slides/foundational/`

### Key Rules
1. Read gold standard slides first
2. No em dashes, no contrastive framing, no colloquial language
3. No Playwright unless Colin explicitly asks
4. Change ONLY what is approved -- present concept first
5. Read PNGs as source of truth
6. Plan icons up front
7. This is capacity/staffing data -- build faithfully, do not modify the numbers

### Design System
Standard BayOne: 16:10 canvas, max-width 1100px, purple gradient palette, Inter font, Font Awesome 6.5.1.

## Output
`slides_output/slide_16_capacity_distribution.html`

This replaces `slide_10_operational_maturity.html` in the final deck at position 16.

Also update the final deck copy:
`final_deck/16_operational_maturity.html` should be replaced with the new file.

## Write results handoff at `handoffs/handoff_20_results.md` when done.
