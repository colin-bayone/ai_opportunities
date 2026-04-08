# 04 - Discussion: Pricing Strategy

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-26
**Document Set:** 04 (Pricing Strategy Discussion)
**Context:** Post-Set 03 (March 25 meeting with Guhan and Selva), informed by the scope reframe to classic view toggle and web research on modernization pricing benchmarks

---

## Key Decisions Made

### 1. Outcome-Based Pricing, Not Headcount
Colin explicitly rejected headcount-based pricing. The price to Cisco is for a deliverable (250+ screens converted, full-stack, end-to-end), not for people-hours. Internal costing is for BayOne's margin analysis only.

### 2. Revenue: $500,000
This number was discussed with Cisco and accepted in principle. The pricing model validates whether this number works at target margins.

### 3. Margin Targets
- **July delivery: 40% floor (non-negotiable).** If Cisco wants speed, they pay full price.
- **December delivery: 30% floor (minimum acceptable).** 40% is ideal.
- **Never discount July.** Compressed timeline IS the premium.

### 4. Team Structure
- Colin at 30% allocation (oversight, architecture, review)
- 1 US engineer at $105K/yr (onshore lead)
- Offshore engineers at $20-35/hr range (mid-range $27.50 used for modeling)
- Offshore count varies by scenario (8 for July, 3 for December)

### 5. Risk Reserve: 25%
Applied on top of base cost to account for technical complexity, scope drift, and unknown backend depth. This is not a guaranteed spend; it is a contingency buffer that sits inside the gross margin.

### 6. AI Per-Screen Effort: 8 Hours (Conservative)
Colin set 8 hours per screen as the conservative AI-assisted estimate. This covers the full vertical slice (UI + backend). The POC will calibrate this with real data.

### 7. Three Scenarios Modeled
- **July:** Heavy parallelization, 8 offshore, 4 months total. Margin 51.7% (loaded).
- **December:** Comfortable pace, 3 offshore, 9 months total. Margin 34.4% (loaded).
- **Discount:** December timeline only. Max discount ~6% on loaded cost to hold 30% margin.

### 8. POC Is Part of the Project
The 80-hour POC (Colin solo, April) counts toward the 250 screens. It is not a separate phase. The cost is absorbed by BayOne but the work (2-3 screens + pattern foundation) is the start of the engagement.

## Key Insight: Why July Is More Profitable
Same total offshore effort (24 engineer-months) in both scenarios. But July runs for 3 months post-POC vs. 8 months for December. Colin and the US engineer are paid for 5 fewer months in the July scenario, saving ~$69K in onshore overhead. Offshore cost is identical.

## Negotiation Framework
- Cisco wants July: $500K, no discount
- Cisco wants December: $500K ideal, floor $468K (6% off)
- Cisco wants both speed AND discount: not possible, push to December
- Cisco pushes hard on price: reduce scope (150 screens) at discounted price, or maintain price with added value

## Deliverables
- Full pricing prototype saved to `pricing/pricing_model_prototype.md`
- Detailed Excel spec saved to `pricing/excel_pricing_spec.md`
- Excel spec designed for handoff to Claude in Excel for workbook generation

## Open Items
- POC will calibrate the 8 hrs/screen estimate with real data
- Need to confirm engagement start date once hardware arrives
- Need Cisco's actual July interest specifics (specific date and customer expectation)
- Which US engineer ($105K vs $160K) is TBD

## Note on Scope Context
This pricing discussion occurred one day after the Set 03 scope reframe (classic view toggle, not full-stack conversion). The pricing references "250+ screens converted, full-stack, end-to-end" and "8 hours per screen covering the full vertical slice (UI + backend)." Given the Set 03 reframe, the per-screen effort estimate and the nature of the work may need recalibration. The toggle/overlay approach is likely less effort per screen than full-stack vertical conversion, which could improve margins or reduce the total price. This is flagged for resolution in subsequent discussions.
