# MGRC v3 Deck Mapping

## Source
`claude/2026-03-19_pptx_extractor_skill/source/MGRC Managed Services Proposal v3 2/`

Colin wants to add slides 2, 4, 5, 6, 7, 8, 9, 20, 21, 22 from this deck.

## Mapping Against Our Existing Deck

### REPLACES OR UPDATES Existing Slides

| v3 Slide | v3 Content | Our Slide | Impact |
|----------|-----------|-----------|--------|
| **2** | Exec Summary (5 embedded resources, 4 value pillars, $300-500K KT savings, 3yr cost optimization) | Slide 2 (Exec Summary versions A/B) | **MUCH more specific.** Has concrete differentiators (embedded team, zero KT risk) vs our narrative versions. Recommend replacing or creating a 4th version. |
| **7** | RFP Scope Summary (70+ integrations, FreshService, expanded out-of-scope) | Slide 5 (Scope Summary) | **Better content.** Mentions 70+ integrations (vs our 50+), adds FreshService, adds infra/L0-L1 out-of-scope items. Could update existing slide 5 or replace. |
| **9** | Transformation Journey (adds manual patch testing/automated patch testing) | Slide 6a (Transformation) | **Adds items.** Two new Today/Tomorrow pairs. Could update 6a content. |
| **20** | Metrics & Reporting (Cost/Quality/Time KPIs + phased timeline) | Slide 12 (KPI Metrics) | **Slightly different KPIs.** Adds enhancement defect leakage, schedule variance. Has phased timeline. Could update slide 12. |
| **21** | Key Assumptions (10 crisp points) | Slide 22 (Prerequisites+Assumptions cleanup) | **SOLVES our cleanup problem.** This is the clean, final version of assumptions. Replaces the messy slide 20 salvage work. |
| **22** | Risks & Mitigation (7 consolidated rows) | Slides 18+19 (Risks Part 1+2) | **Consolidated.** 7 risks in one slide vs our 8 across two. References embedded team and rebadging. Could replace both. |

### GENUINELY NEW Slides (No Existing Equivalent)

| v3 Slide | Content | Where It Fits |
|----------|---------|--------------|
| **4** | "Our Understanding" section divider | Before the scope/architecture slides. Different framing from our "Our Solution" divider. |
| **5** | NextGen Ecosystem Architecture (12-13 systems, 70+ integrations, full diagram) | Section 2 after the "understanding" divider. This is HUGE -- shows we understand their entire technical landscape. |
| **6** | 13 Solution Towers (full scope table with all 13 systems + Bid/Bid* status) | Section 2 after architecture. More granular than our 6-card scope summary. |
| **8** | "Proposed Solution" section divider | Between the understanding section and the solution/transformation slides. |

## Proposed Integration Plan

### Section 2 Restructured:

**Understanding Block (NEW from v3):**
- Slide 4 (v3): "Our Understanding" section divider -- NEW
- Slide 5 (v3): Architecture diagram -- NEW
- Slide 6 (v3): 13 Solution Towers -- NEW
- Slide 7 (v3): RFP Scope Summary -- REPLACES our slide 5

**Solution Block:**
- Slide 8 (v3): "Proposed Solution" section divider -- NEW (or merge with existing slide 4)
- Slide 6a: Transformation Journey -- UPDATE content with v3 slide 9 additions
- Slide 6b: AI Strategy -- KEEP as-is
- Slide 7: Solution Summary -- KEEP as-is
- Slide 8: Operations Snapshot -- KEEP as-is

### Exec Summary Decision:
v3 Slide 2 has very specific content (5 embedded resources, zero-risk transition, $300-500K KT savings, 4 value pillars). Our versions A/B are more narrative. Colin should decide:
- Replace with v3 content entirely?
- Create a hybrid (v3's specific claims + our narrative framing)?
- Keep both and choose later?

### Risks/Assumptions Simplification:
- v3 Slide 22 (consolidated 7 risks) could replace our slides 18+19 (saving a slide)
- v3 Slide 21 (10 assumptions) solves the prerequisites/assumptions cleanup entirely
- The dedup work between Key Asks and Risks may be simplified since v3 Slide 22 is already consolidated

## Important Content Notes

### 70+ Integrations
The v3 deck uses "70+" integrations throughout (slides 5, 6, 7). Our deck uses "43+" (the RFP number) per Colin's strategy of not exposing insider information. **Colin needs to decide: does the v3 deck's use of 70+ change our approach?** This is a strategic question.

### 5 Embedded Resources
v3 Slide 2 leads with "5 resources already embedded at MGRC." This is a powerful differentiator but may require validation that this can be stated in the RFP response.

### FreshService
v3 mentions FreshService as the ticketing tool. Not in our current slides. Should be added where relevant.

### MuleSoft to OIC Migration
v3 Slide 21 assumption #6: "Most MuleSoft integrations migrating to OIC; pricing reflects post-migration." This is new intel not in our existing content.
