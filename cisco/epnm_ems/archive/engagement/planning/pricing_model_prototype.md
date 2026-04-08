# Pricing Model Prototype: EPNM-to-EMS UI Conversion

**Date:** 2026-03-26
**Engagement:** Cisco EPNM-to-EMS UI Conversion
**Revenue:** $500,000 (outcome-based, fixed price)
**Scope:** 250+ screens, full-stack (UI + backend), end-to-end

---

## Input Parameters

### Personnel Rates

| Resource | Base Annual/Hourly | Loaded (+ 20%) | Monthly Loaded | Hourly Loaded |
|---|---|---|---|---|
| Colin Moore (Director of AI) | $180,000/yr | $216,000/yr | $18,000/mo | $103.85/hr |
| US Engineer A | $105,000/yr | $126,000/yr | $10,500/mo | $60.58/hr |
| US Engineer B | $160,000/yr | $192,000/yr | $16,000/mo | $92.31/hr |
| Offshore Engineer (low) | $20/hr | $24.00/hr | $4,152/mo | $24.00/hr |
| Offshore Engineer (mid) | $27/hr | $32.40/hr | $5,609/mo | $32.40/hr |
| Offshore Engineer (high) | $35/hr | $42.00/hr | $7,266/mo | $42.00/hr |

*Monthly = loaded hourly x 173.33 hrs/mo (2,080 hrs/yr / 12)*

### Rate Type Column (Added 2026-03-28)

The Personnel Rates table mixes annual salaries (US resources) and hourly rates (offshore). To make the Loaded Monthly calculation self-describing and correct for any resource type, each row should have a **Rate Type** field: `Annual` or `Hourly`.

The Loaded Monthly formula is conditional on Rate Type:
- **Annual:** Loaded Annual / 12
- **Hourly:** Loaded Hourly × 173.33

This ensures the model works correctly when reused as a template for other engagements. A US contractor at $75/hr entered as "Hourly" calculates correctly, as does a salaried offshore lead at $85K/yr entered as "Annual."

| Resource | Rate Type | Base Rate | Loaded Rate | Loaded Monthly |
|---|---|---|---|---|
| Colin Moore | Annual | $180,000 | $216,000 | $216,000 / 12 = $18,000 |
| US Engineer A | Annual | $105,000 | $126,000 | $126,000 / 12 = $10,500 |
| US Engineer B | Annual | $160,000 | $192,000 | $192,000 / 12 = $16,000 |
| Offshore (low) | Hourly | $20.00 | $24.00 | $24.00 × 173.33 = $4,152 |
| Offshore (mid) | Hourly | $27.50 | $33.00 | $33.00 × 173.33 = $5,720 |
| Offshore (high) | Hourly | $35.00 | $42.00 | $42.00 × 173.33 = $7,266 |

### Constants

- Revenue: $500,000
- Screens: 250
- Working hours per month: 173.33
- POC duration: 1 month (April 2026, Colin solo, absorbed cost)
- POC screens: 2-3 (count toward the 250)

### Margin Thresholds

- July scenarios: minimum 40% margin (hard floor, do not budge below this)
- December scenarios: minimum 30% margin (standard target)
- Scenario 3 (discount): push to December only, floor at 30%

---

## Scenario 1: July Delivery (Compressed)

### Timeline
- April: POC (Colin solo, pattern foundation, 2-3 screens)
- May-June: Full team factory mode (2 months)
- July: QA/QE, integration testing, acceptance

### Staffing Plan

| Resource | April (POC) | May | June | July (QA) |
|---|---|---|---|---|
| Colin | 80 hrs (~46%) | 15% | 10% | 10% |
| US Engineer A ($105K) | -- | 100% | 100% | 100% |
| Offshore Eng 1-6 ($24/hr) | -- | 100% | 100% | -- |
| Offshore Eng 1-4 ($24/hr) | -- | -- | -- | 100% |

### Monthly Costs

| Resource | April | May | June | July | Total |
|---|---|---|---|---|---|
| Colin | $8,308 | $2,700 | $1,800 | $1,800 | $14,608 |
| US Engineer A | -- | $10,500 | $10,500 | $10,500 | $31,500 |
| Offshore (6 eng) | -- | $24,912 | $24,912 | -- | $49,824 |
| Offshore (4 eng, QA) | -- | -- | -- | $16,608 | $16,608 |
| **Monthly Total** | **$8,308** | **$38,112** | **$37,212** | **$28,908** | |
| **Cumulative** | $8,308 | $46,420 | $83,632 | $112,540 | **$112,540** |

### Scenario 1 Results

| Metric | Value |
|---|---|
| Total Cost | $112,540 |
| Revenue | $500,000 |
| Gross Margin | $387,460 |
| **Margin %** | **77.5%** |
| Cost per Screen | $450 |
| Peak Headcount | 8 (Colin + US + 6 offshore) |
| Peak Monthly Burn | $38,112 |

**Analysis:** Margin is extremely high at 77.5%. This means either:
1. We can afford MORE offshore engineers for delivery confidence
2. The price is generous for this timeline
3. There is room to negotiate if needed while staying above 40%

### Scenario 1a: July with Heavier Staffing (10 offshore peak)

| Resource | April | May | June | July (QA) | Total |
|---|---|---|---|---|---|
| Colin | $8,308 | $2,700 | $1,800 | $1,800 | $14,608 |
| US Engineer A | -- | $10,500 | $10,500 | $10,500 | $31,500 |
| Offshore (10 eng) | -- | $41,520 | $41,520 | -- | $83,040 |
| Offshore (6 eng, QA) | -- | -- | -- | $24,912 | $24,912 |
| **Total** | | | | | **$154,060** |

| Metric | Value |
|---|---|
| Total Cost | $154,060 |
| Margin | $345,940 |
| **Margin %** | **69.2%** |
| Peak Headcount | 12 |

Still well above 40%. Could even go to 15 offshore and still be at 40%+.

### Scenario 1b: July -- What is the max team at 40% margin floor?

Cost budget at 40%: $500K x 0.60 = $300,000
Fixed costs (Colin + US, 4 months): $46,108
Remaining for offshore: $253,892
Over 3 months (May-Jul): $84,631/mo
At $4,152/mo per engineer: **20 offshore engineers**

That is the theoretical max team for July at 40% margin. Obviously you would never need 20 engineers for 250 screens in 3 months -- the coordination overhead would eat the gains. But it shows how much room there is.

**Practical max for July: 8-12 offshore engineers.** Beyond that, coordination costs outweigh parallelization gains.

---

## Scenario 2: December Delivery (Comfortable)

### Timeline
- April: POC (Colin solo)
- May-July: Foundation + scale (3 months)
- August-October: Peak factory (3 months)
- November-December: QA/QE, integration, acceptance (2 months)

### Staffing Plan (Flex Ramp: 3 → 5 → 6 → 4)

| Resource | April | May-Jun | Jul-Aug | Sep-Oct | Nov-Dec |
|---|---|---|---|---|---|
| Colin | 46% | 20% | 15% | 10% | 10% |
| US Engineer A ($105K) | -- | 100% | 100% | 100% | 50% |
| Offshore ($24/hr) | -- | 3 eng | 5 eng | 6 eng | 4 eng |

### Monthly Costs

| Resource | April | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Colin | $8,308 | $3,600 | $3,600 | $2,700 | $2,700 | $1,800 | $1,800 | $1,800 | $1,800 | $28,108 |
| US Eng A | -- | $10,500 | $10,500 | $10,500 | $10,500 | $10,500 | $10,500 | $5,250 | $5,250 | $73,500 |
| Offshore | -- | $12,456 | $12,456 | $20,760 | $20,760 | $24,912 | $24,912 | $16,608 | $16,608 | $149,472 |
| **Monthly** | **$8,308** | **$26,556** | **$26,556** | **$33,960** | **$33,960** | **$37,212** | **$37,212** | **$23,658** | **$23,658** | |
| **Total** | | | | | | | | | | **$251,080** |

### Scenario 2 Results

| Metric | Value |
|---|---|
| Total Cost | $251,080 |
| Revenue | $500,000 |
| Gross Margin | $248,920 |
| **Margin %** | **49.8%** |
| Cost per Screen | $1,004 |
| Peak Headcount | 8 (Colin + US + 6 offshore) |
| Peak Monthly Burn | $37,212 |
| Avg Monthly Burn | $27,898 |

---

## Scenario 3: December Delivery -- Discounted Price

**Premise:** Cisco asks for a discount. We push the timeline to December (no July option at discount). Floor is 30% margin.

### What Discount Can We Offer?

Using the December cost basis of $251,080:

| Discounted Price | Margin $ | Margin % | Viable? |
|---|---|---|---|
| $500,000 (full price) | $248,920 | 49.8% | Yes |
| $475,000 (5% off) | $223,920 | 47.1% | Yes |
| $450,000 (10% off) | $198,920 | 44.2% | Yes |
| $425,000 (15% off) | $173,920 | 40.9% | Yes |
| $400,000 (20% off) | $148,920 | 37.2% | Yes |
| $375,000 (25% off) | $123,920 | 33.0% | Yes (barely) |
| $358,686 (floor) | $107,606 | 30.0% | Floor |
| $350,000 (30% off) | $98,920 | 28.3% | **No -- below 30%** |

### Scenario 3: Maximum Discount (30% margin floor)

**Floor price at December timeline: $358,686 (~$359K)**

That is a **28.2% discount** from $500K. Below that, walk away or reduce scope.

### Scenario 3 Results (at $400K, a round-number discount)

| Metric | Value |
|---|---|
| Revenue | $400,000 |
| Total Cost | $251,080 |
| Gross Margin | $148,920 |
| **Margin %** | **37.2%** |
| Discount from $500K | 20% |
| Cost per Screen | $1,004 |
| Revenue per Screen | $1,600 |

### Key Negotiation Points

- **July delivery at any discount: NO.** July already compresses the timeline and increases risk. If they want speed AND a discount, that is unreasonable.
- **December at up to 20% discount: viable.** $400K is a clean round number, 37.2% margin, still healthy.
- **December at 25%+ discount: dangerous.** Below $375K, margin drops into the low 30s. No buffer for scope creep, complex screens, or coordination overhead.
- **Counter-offer if they push hard:** Reduce scope (150 screens instead of 250) at the discounted price, or maintain price with added value (documentation, training, maintenance period).

---

## Cross-Scenario Comparison

| Metric | Scenario 1 (July) | Scenario 2 (Dec) | Scenario 3 (Discount) |
|---|---|---|---|
| Revenue | $500,000 | $500,000 | $400,000 |
| Total Cost | $112,540 | $251,080 | $251,080 |
| Margin $ | $387,460 | $248,920 | $148,920 |
| **Margin %** | **77.5%** | **49.8%** | **37.2%** |
| Duration | 4 months | 9 months | 9 months |
| Peak Offshore | 6 | 6 | 6 |
| Peak Headcount | 8 | 8 | 8 |
| Cost/Screen | $450 | $1,004 | $1,004 |
| Monthly Burn (avg) | $28,135 | $27,898 | $27,898 |

### Key Insight

The July scenario has dramatically higher margin because you're paying the team for 3 months instead of 8. The total work output is the same (250 screens), but the calendar cost is much lower. This means:

1. **July is actually the most profitable scenario** despite needing more parallel engineers
2. **The December margin is still excellent** at nearly 50%
3. **Even a 20% discount on December** leaves a healthy 37% margin
4. **Never discount July.** The compressed timeline IS the premium. If they want it fast, they pay full price. 40% is the floor and you're well above it.

---

## POC Economics (Absorbed)

| Metric | Value |
|---|---|
| Colin's time | 80 hours |
| Colin's loaded cost | $103.85/hr |
| POC cost to BayOne | $8,308 |
| Screens delivered | 2-3 |
| Patterns/knowledge base | Foundation for factory mode |

This is the investment that unlocks the $500K engagement. The POC cost represents 1.7% of revenue. The knowledge base and patterns built during POC accelerate everything that follows.

---

## Throughput Assumptions (To Be Calibrated by POC)

These are estimates. The POC will provide real data.

| Phase | Screens/Engineer/Week | Rationale |
|---|---|---|
| POC (month 1) | 0.5-0.75 | Building patterns, learning codebase, heavy discovery |
| Foundation (months 2-3) | 3-5 | Patterns emerging, agents being tuned |
| Factory (months 4+) | 8-15 | Patterns established, agents trained, review-only cycle |
| QA/Integration | N/A | Fixing, testing, not converting new screens |

### Capacity Check: July Scenario

- May: 6 engineers x 5 screens/eng/week (still ramping) x 4.3 weeks = 129 screens
- June: 6 engineers x 10 screens/eng/week (factory) x 4.3 weeks = 258 screens
- Capacity: 387 screens in 2 months

250 screens is **64% of capacity.** Comfortable even with ramp overhead.

### Capacity Check: December Scenario

- May-Jun: 3 eng x 4 avg x 8.7 weeks = 104
- Jul-Aug: 5 eng x 8 avg x 8.7 weeks = 348
- Sep-Oct: 6 eng x 12 avg x 8.7 weeks = 626
- Capacity: 1,078 screens in 6 dev months

250 screens is **23% of capacity.** Extremely comfortable. Could reduce team or shorten timeline.

---

## Travel & Expenses

**Added 2026-03-28 based on CEO feedback.**

| Item | Cost | Notes |
|---|---|---|
| Cost per trip | $2,750 | Flights, hotel, meals, ground transport to San Jose |
| July scenario trips | 2 | Kickoff + final demo/acceptance |
| December scenario trips | 4 | Kickoff + 2 checkpoints + final demo/acceptance |

### Impact on Scenarios

| Scenario | Travel Cost | Revised Base Cost | Revised Loaded Cost | Revised Margin (loaded) |
|---|---|---|---|---|
| July | $5,500 | $198,788 | $248,485 | 50.3% |
| December | $11,000 | $273,288 | $341,610 | 31.7% |
| Discount ($468K) | $11,000 | $273,288 | $341,610 | 27.0% |

Travel cost is modest but shifts the December discount floor. At 30% margin on loaded cost, the new floor price is approximately $488K (2.4% discount max) with travel included.

---

## Hardware & Consumables (Placeholder)

**Added 2026-03-28 based on CEO feedback.**

Cisco provides the laptop, development environment, and AI tool licenses. BayOne-side hardware and consumable costs are currently zero but the line item exists for completeness.

| Item | Monthly | One-Time | Default |
|---|---|---|---|
| Tools & Subscriptions | $0/mo | -- | Placeholder |
| Equipment | -- | $0 | Placeholder |

These should be configurable on the Inputs tab. If BayOne needs to provision any tooling outside Cisco's infrastructure (e.g., LangGraph hosting, testing tools), the costs go here.

---

## Per-Resource Utilization

**Added 2026-03-28 based on CEO feedback.**

The original model only had Colin's allocation as a configurable parameter. All resources should have a settable utilization/allocation percentage.

| Resource | Default Allocation | Effective Monthly |
|---|---|---|
| Colin Moore | 30% | $18,000 × 0.30 = $5,400 |
| US Engineer A ($105K) | 100% | $10,500 × 1.00 = $10,500 |
| US Engineer B ($160K) | 100% | $16,000 × 1.00 = $16,000 |
| Offshore Engineer (mid) | 100% | $5,720 × 1.00 = $5,720 |

Making this per-resource means:
- A US engineer at 80% allocation reduces their monthly cost to $8,400
- An offshore engineer at 90% drops to $5,148/mo
- These flow through to all scenario calculations automatically
- Useful for modeling shared resources or partial allocations

---

## Phase Naming: "Stabilization & Acceptance" (Replaces "QA")

**Added 2026-03-28 based on CEO feedback and discussion.**

The original model labeled the final phase "QA months." This is misleading because:
- Development follows an agile cycle where testing happens continuously throughout
- The final phase is not a distinct QA effort; it is a stabilization period
- Its purpose is production-level validation after Cisco integrates the converted screens
- It is the period where stakeholders build trust in the deliverables
- It includes bug fixes, refinements, and final acceptance

**New label: "Stabilization & Acceptance"**

This phase covers:
1. Production-level testing in Cisco's environment after integration
2. Bug fixes and refinements based on integration findings
3. Stakeholder demos and confidence-building
4. Final acceptance criteria verification
5. Handoff and documentation

All references to "QA months" in the model should read "Stabilization & Acceptance months." The duration and cost remain the same; only the framing changes.

---

## Revised Cross-Scenario Comparison (With Travel)

| | July (Sc. 1) | December (Sc. 2) | Discount (Sc. 3) |
|---|---|---|---|
| Revenue | $500K | $500K | $488K (floor) |
| Personnel Cost | $193,288 | $262,288 | $262,288 |
| Travel & Expenses | $5,500 | $11,000 | $11,000 |
| Hardware & Consumables | $0 | $0 | $0 |
| **Base Cost** | **$198,788** | **$273,288** | **$273,288** |
| Risk Reserve (25%) | $49,697 | $68,322 | $68,322 |
| **Loaded Cost** | **$248,485** | **$341,610** | **$341,610** |
| **Margin % (loaded)** | **50.3%** | **31.7%** | **30.0%** |
| **Margin % (base)** | **60.2%** | **45.3%** | **44.0%** |

---

## Notes for Excel Spec

This prototype confirms the model works. The Excel workbook should include:
1. An inputs sheet where all rates, allocations, and assumptions can be changed
2. Month-by-month cost breakdown for each scenario
3. Margin calculations that update automatically
4. A comparison dashboard
5. Discount sensitivity table for Scenario 3
6. Throughput projections (to be updated after POC)
7. Travel & Expenses as a configurable line item per scenario
8. Hardware & Consumables as a placeholder line item
9. Per-resource utilization/allocation percentages on the Inputs tab
10. "Stabilization & Acceptance" labeling (not "QA")
