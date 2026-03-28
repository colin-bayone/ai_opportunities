# V3 Deck Integration Decisions

## Date: 2026-03-23

### Integration Count: 70+
Colin approved moving to "70+" across the entire deck. Previously we used "43+" (the RFP number) per the strategy of not exposing insider info. The v3 deck uses 70+ openly, so this is now the standard.

**Slides that need 43+ updated to 70+:** Any previously built slide referencing "43+ integrations" should be updated. This includes at minimum:
- Slide 2 (Exec Summary versions A/B)
- Slide 5 (Scope Summary)
- Slide 6a (Transformation Journey)
- Slide 6b (AI Strategy)

### Content Update Approach
- Do NOT automatically replace existing HTML with v3 content
- Present v3 content alongside existing content and let Colin decide what stays/goes
- The builder should be in the loop with Colin for every content change
- Some existing slides may get v3 content additions; some may be replaced entirely; some may stay as-is

### Section Dividers: DROPPED
Colin decided to not include any section dividers in the HTML deck. If needed, they'll be added in PowerPoint during assembly. This means: `slide_04_section_divider.html`, `slide_new_our_understanding_divider.html`, and `slide_new_proposed_solution_divider.html` are all excluded from the final deck.

### Final Ordering: DEFERRED
The final slide order will be determined during PowerPoint assembly, not in the `final_deck/` folder. The narrative order doc (`planning/06_final_narrative_order.md`) and reconciliation (`planning/07_order_reconciliation.md`) serve as reference guides, not prescriptive. Colin will arrange slides when assembling.

### What the V3 Session Should Do
1. Build the 4 genuinely new slides (architecture, 13 towers, 2 dividers)
2. For the 6 overlapping slides: present v3 content vs existing content side-by-side and get Colin's direction on each
3. Update the 43+ -> 70+ across all previously built slides
4. All changes require Colin's explicit approval before finalizing
