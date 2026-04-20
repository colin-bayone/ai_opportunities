# 06 - Research: Cisco EPNM/EMS Pricing Reference

**Source:** /cisco/epnm_ems/pricing/ and /cisco/epnm_ems/deliverables/
**Source Date:** 2026-04-09 (Reference research for Lam POC pricing)
**Document Set:** 06 (Internal Pricing Call)
**Pass:** Research exploration of Cisco engagement pricing as reference for Lam POC

---

## 1. Cisco Pricing Methodology Overview

### Engagement Parameters

The Cisco EPNM-to-EMS UI Conversion was a $500,000 fixed-price, outcome-based engagement to convert approximately 250 screens from a legacy Dojo/JavaScript monolith to a modern Angular microservices platform. The pricing model was built from the inside out: start with real personnel costs, apply load factors and risk reserves, then validate that the target revenue produces acceptable margins across multiple delivery timeline scenarios.

### Core Pricing Philosophy

The AI practice's pricing methodology separates what the client sees from how the price is calculated:

- **Internal model:** Bottom-up cost estimation based on personnel rates, team composition, duration, load factors, risk reserves, and margin targets. Every number traces back to a real cost.
- **Client-facing presentation:** Outcome-based, milestone-driven pricing with no headcount or rate exposure. The client sees deliverables and dollar amounts per phase, not people or hours.

This separation is critical. The client never sees the team composition, never sees hourly rates, never sees the margin. They see phases, deliverables, and prices that total to the SOW amount.

### Personnel Cost Structure

All costs begin with base rates and flow through a standard transformation:

1. **Base Rate** -- either annual salary (US resources) or hourly rate (offshore resources)
2. **Load Factor** -- 20% markup applied uniformly (covers benefits, overhead, administrative costs). Base Rate x 1.20 = Loaded Rate
3. **Loaded Monthly** -- derived differently by rate type:
   - Annual resources: Loaded Annual / 12
   - Hourly resources: Loaded Hourly x 173.33 (working hours per month, based on 2,080 hours/year / 12)
4. **Allocation %** -- per-resource utilization percentage (e.g., Colin at 30%, offshore engineers at 100%)
5. **Effective Monthly** -- Loaded Monthly x Allocation %. This is the actual cost per resource per month.

### Specific Rates Used (Cisco Engagement)

| Resource | Rate Type | Base Rate | Loaded Monthly | Notes |
|---|---|---|---|---|
| Colin Moore (Director of AI) | Annual | $180,000 | $18,000 | Typically allocated at 30% ($5,400 effective) |
| US Engineer A | Annual | $105,000 | $10,500 | Full allocation |
| US Engineer B | Annual | $160,000 | $16,000 | Not used in primary scenarios |
| Offshore Engineer (low) | Hourly | $20.00 | $4,152 | Entry-level |
| Offshore Engineer (mid) | Hourly | $27.50 | $5,720 | Default for modeling |
| Offshore Engineer (high) | Hourly | $35.00 | $7,266 | Senior offshore |

### Cost Layers

The model builds cost in layers, each with a distinct purpose:

1. **Personnel Cost** -- sum of all Effective Monthly costs across all resources across all months of the engagement
2. **Travel & Expenses** -- per-trip cost ($2,750 to San Jose) multiplied by number of trips per scenario (2 for July compressed timeline, 4 for December comfortable timeline)
3. **Hardware & Consumables** -- placeholder at $0 for Cisco (they provide hardware and AI tool licenses), but the line item exists for engagements where BayOne must provision tooling
4. **Base Cost** -- Personnel + Travel + Hardware
5. **Risk Reserve** -- 25% of Base Cost. This is a buffer for scope creep, complex screens, coordination overhead, and unknowns
6. **Loaded Cost** -- Base Cost + Risk Reserve. This is the "true" cost floor; margin is calculated against this

### Margin Calculation

Two margin figures are tracked:

- **Margin on Loaded Cost** = (Revenue - Loaded Cost) / Revenue. This is the conservative, risk-adjusted margin.
- **Margin on Base Cost** = (Revenue - Base Cost) / Revenue. This is the optimistic margin if risk reserve is not consumed.

Both are monitored because the negotiation strategy depends on which one is referenced. When the risk reserve is not consumed, the effective margin is higher than the loaded calculation shows.

---

## 2. Scenario-Based Pricing Structure

The Cisco model was built around three scenarios to support negotiation flexibility. Each scenario answers a different business question.

### Scenario 1: July Delivery (Compressed, 4 months)

**Question:** What does it cost if Cisco wants speed?

- April: POC (Colin solo, absorbed cost)
- May-June: Full team factory mode (6-8 offshore + 1 US engineer)
- July: Stabilization & Acceptance (4-8 offshore)

| Metric | Value |
|---|---|
| Revenue | $500,000 |
| Base Cost | $198,788 (with travel) |
| Loaded Cost | $248,485 |
| Margin (loaded) | 50.3% |
| Margin (base) | 60.2% |
| Peak Headcount | 8-12 |
| Peak Monthly Burn | ~$38,000 |

**Key insight:** July is the most profitable scenario despite needing more parallel engineers, because the team is paid for 3 months post-POC instead of 8. The margin is extremely high (50%+ loaded), providing significant room for team expansion to ensure delivery confidence.

### Scenario 2: December Delivery (Comfortable, 9 months)

**Question:** What does it cost at a comfortable pace?

- April: POC (Colin solo)
- May-October: Development with ramp from 3 to 6 offshore engineers
- November-December: Stabilization & Acceptance

| Metric | Value |
|---|---|
| Revenue | $500,000 |
| Base Cost | $273,288 (with travel) |
| Loaded Cost | $341,610 |
| Margin (loaded) | 31.7% |
| Margin (base) | 45.3% |
| Peak Headcount | 8 |
| Peak Monthly Burn | ~$37,000 |

**Key insight:** December carries roughly $75K more in onshore cost (Colin and US engineer paid for 5 additional months). The loaded margin at 31.7% is above the 30% floor but leaves limited room for discounting.

### Scenario 3: Discount Analysis (December timeline with price sensitivity)

**Question:** How far can we discount if Cisco pushes back?

Uses December cost basis. A full discount sensitivity table was built:

| Price | Discount | Margin (loaded) | Viable? |
|---|---|---|---|
| $500,000 | 0% | 31.7% | Yes |
| $488,000 | 2.4% | 30.0% | Floor (loaded) |
| $475,000 | 5% | 28.1% | Below floor on loaded |
| $450,000 | 10% | 24.1% | No |
| $400,000 | 20% | 14.6% | No |

**Key insight:** With travel costs included in the December model, the maximum discount on loaded cost is approximately 2.4% (floor price ~$488K). On base cost the floor is $375K (25% discount). The negotiation strategy depends on whether risk reserve is treated as a hard cost or a buffer within margin.

### Margin Thresholds (Negotiation Rules)

| Timeline | Target | Floor | Rationale |
|---|---|---|---|
| July | 40%+ | 40% hard floor | Compressed timeline IS the premium. Speed costs. Never discount July. |
| December | 40% target | 30% minimum | Standard margin target with flexibility for negotiation |

Specific negotiation rules documented in the model:

1. July delivery at any discount: NO. Speed and discount are mutually exclusive.
2. December at up to ~6% discount: safe on loaded cost margin.
3. December at 6-25% discount: viable only if risk reserve is treated as buffer inside margin (i.e., measuring against base cost, not loaded).
4. Below $375K: walk away or reduce scope.
5. Counter-offer if they push hard: reduce scope (150 screens instead of 250) at the discounted price, or add value (documentation, training, maintenance period) to justify full price.

---

## 3. POC-Specific Pricing Structure

### POC as Absorbed Investment

The Cisco POC was provided at zero cost to the client. The internal cost was absorbed by BayOne:

| Metric | Value |
|---|---|
| Duration | 4 weeks (1 month) |
| Staffing | Colin Moore solo |
| Hours | 80 (approximately 46% allocation) |
| Cost to BayOne | $8,308 (loaded) |
| Screens Delivered | 2-3 (counted toward the 250 total) |
| Cost as % of Revenue | 1.7% of the $500K engagement |

### POC Strategic Purpose

The POC was explicitly designed as the investment that unlocks the paid engagement:

- Builds the pattern library and knowledge base that makes factory mode possible
- Establishes conversion velocity data for credible estimation
- Demonstrates capability against the actual codebase (not a toy example)
- Creates switching costs -- the infrastructure developed during POC transfers to the paid engagement
- Allows Cisco to evaluate BayOne's capability before committing to $500K

### POC Deliverables (Client-Facing)

The POC proposal presented to Cisco was structured as a two-phase, four-week engagement:

**Phase 1 (Weeks 1-2): Exploration and Onboarding**
- Codebase analysis using AI-assisted exploration
- Screen inventory with complexity classification
- Dependency graphs and pattern identification
- Collaborative screen selection with Cisco SMEs

**Phase 2 (Weeks 3-4): Conversion, Testing, and Acceptance**
- Convert 2-3 selected screens end-to-end (frontend and backend)
- Automated visual validation using Playwright
- Pattern library development
- Gap documentation for missing EMS services
- Estimation model for remaining screens

### POC-to-Paid Engagement Bridge

The POC proposal explicitly positioned the transition:

- POC infrastructure (agents, patterns, knowledge base) transfers directly to paid engagement
- POC velocity is the conservative floor (single resource, sequential, infrastructure still being built)
- Paid engagement adds team scale and parallel execution via LangGraph multi-agent architecture
- The acceleration argument: first screen carries full infrastructure weight, second benefits from all prior work, third follows established patterns

---

## 4. Client-Facing vs. Internal Presentation

### What the Client Sees (Pricing Breakdown HTML)

The client-facing pricing breakdown presents the $500K as four outcome-based phases:

| Phase | Amount | % of Total |
|---|---|---|
| Discovery and Codebase Analysis | $50,000 | 10% |
| AI Tooling and Agent Development | $100,000 | 20% |
| Screen Conversion and Integration | $275,000 | 55% |
| Quality Engineering and Validation | $75,000 | 15% |
| **Total (Not-to-Exceed)** | **$500,000** | **100%** |

Each phase includes 6-9 specific deliverable line items, all marked "Included" (no per-item pricing). The total is presented as "Not-to-Exceed" -- outcome-based, not time-and-materials.

**What is deliberately absent from the client-facing document:**
- No headcount or team composition
- No hourly rates or salaries
- No margin percentages
- No duration per phase (just deliverables)
- No mention of offshore resources
- No internal cost structure
- No risk reserve

The pricing basis section states scope is "approximately 240 to 260 screens" with language that reasonable variance will be accommodated within the engagement, and significant changes would follow a change request process.

### What Colin Sees (Internal Pricing Model)

The internal model contains everything the client document does not:

- Full personnel rate table with base rates, load factors, loaded rates, and allocations
- Month-by-month cost breakdown per resource per scenario
- Margin calculations at both base and loaded cost
- Risk reserve calculations
- Discount sensitivity analysis with floor prices
- Throughput/capacity projections per scenario
- Travel and expense line items
- Negotiation rules and walk-away points

### Dual-Version Proposal Strategy

Two versions of the POC proposal were created:

**Client-facing version (poc_proposal_v5):** 8 sections, clean and focused. Omits technical depth on AI tooling, acceleration mechanisms, and internal execution details. Investment model section simply states "Cost to Cisco: None" for POC and "Outcome-based engagement" for paid.

**Detailed internal-facing version (poc_proposal_v5_detailed):** 10 sections. Adds:
- Section 05: Acceleration Mechanism -- detailed explanation of one-time infrastructure investment vs. per-screen marginal cost, velocity improvement projections, knowledge base compound growth
- Section 06: Technical Context -- detailed EPNM and EMS architecture analysis, vertical integration requirements, Dojo-to-Angular translation challenges
- More granular AI tooling section with LangGraph multi-agent architecture details

The detailed version serves two purposes: (1) internal reference for BayOne team members who need technical depth, and (2) available if Cisco stakeholders request deeper technical justification.

---

## 5. Excel Template Structure and Iteration Pattern

### Excel Workbook Structure (6 Tabs)

The pricing model was designed as a reusable Excel template with six tabs:

1. **Inputs** -- Single source of truth for all configurable parameters
   - Personnel Rates table (Resource, Rate Type, Base Rate, Load Factor, Loaded Rate, Loaded Monthly, Allocation %, Effective Monthly)
   - Engagement Parameters (Revenue, Total Screens, Hours per Screen, Risk Reserve %, POC Hours)
   - Margin Thresholds (July floor 40%, December floor 30%)
   - Scenario Parameters (offshore engineer counts, dev months, stabilization months per scenario)
   - Travel & Expenses (cost per trip, trips per scenario)
   - Hardware & Consumables (placeholder)
   - Working Hours per Month (173.33, editable)

2. **July Delivery** -- Monthly cost breakdown, financial summary, per-screen economics, staffing summary

3. **December Delivery** -- Same structure as July but with 9-month timeline and ramping team

4. **Discount Analysis** -- Sensitivity table testing prices from $500K down to $350K, floor price calculations, negotiation rules

5. **Comparison** -- Side-by-side dashboard of all three scenarios (revenue, costs, margins, headcount, per-screen economics)

6. **Throughput** -- Screen conversion capacity model by month, utilization analysis

### Key Design Principles

- **Every scenario tab references the Inputs tab.** No hardcoded numbers in scenario calculations. Change a rate on Inputs, all scenarios update automatically.
- **Named ranges for all inputs** to make formulas readable (e.g., `ColinMonthly`, `OffshoreMonthly`, `RiskReserve`, `JulyFloor`).
- **Conditional formatting** throughout: green for margins above target, amber for margins in caution zone (30-40%), red for margins below floor.
- **BayOne brand palette** in formatting: deep violet headers (#2e1065), purple section headers (#5b21b6), light purple accent rows (#ede9fe).

### Iteration Pattern (Three Correction Rounds)

The pricing model went through three rounds of corrections after initial build. This reveals what the AI practice considers important and what typical first-draft mistakes look like:

**Correction v1 (5 changes):**
1. Added Travel & Expenses section (missed initially; CEO feedback prompted this)
2. Added Hardware & Consumables placeholder (CEO feedback)
3. Replaced single "Colin Allocation %" with per-resource Allocation % column (generalization for reuse)
4. Reframed "QA Months" as "Stabilization & Acceptance" (framing matters; testing happens throughout, the final phase is about stakeholder trust and integration validation)
5. Made Working Hours per Month editable (was hardcoded; needs to be adjustable for different availability assumptions)

**Correction v2 (1 change):**
6. Added Rate Type column (Annual vs. Hourly) to Personnel Rates table. The existing table mixed annual salaries and hourly rates in the same column without indicating which formula applied. Adding a dropdown-driven Rate Type makes the Loaded Monthly formula self-describing and correct for any resource type.

**Correction v3 (1 change):**
7. Confirmed Working Hours per Month cell is truly editable with proper formatting, cell comments, and validation that changing it flows through to all hourly resource costs without affecting annual resource costs.

**Pattern from corrections:**
- First-draft models miss non-personnel costs (travel, hardware) and operational details
- Reusability concerns dominate corrections: Rate Type, per-resource allocation, editable constants
- Framing and labeling matter ("Stabilization & Acceptance" vs. "QA" changes how the client perceives the phase)
- CEO-level feedback focuses on completeness (travel, hardware) and operational realism

---

## 6. Applicability to Lam Research POC Pricing

### What Transfers Directly

**The cost structure methodology transfers intact.** The same layered approach applies:
- Base personnel rates with load factor (1.20x)
- Rate Type distinction (Annual vs. Hourly)
- Per-resource allocation percentages
- Travel & Expenses as configurable line items
- Risk reserve as a percentage of base cost
- Margin thresholds with separate floors for compressed vs. comfortable timelines

**The Excel template structure transfers as a reusable template.** Swap out the engagement-specific parameters (revenue, scope unit, team composition) and the same 6-tab structure works.

**The dual-document strategy transfers.** Internal pricing model with full cost transparency, client-facing deliverable with outcome-based phases and no rate exposure.

### What Needs Adaptation

**Scope unit changes.** Cisco used "screens" as the atomic scope unit (250 screens, cost per screen, screens per engineer per week). Lam Research uses different scope units depending on what the POC is proving: documents processed, entity types detected, redaction accuracy percentage, or pipeline throughput. The pricing model needs a scope unit that maps to effort, similar to how "screens" mapped to conversion hours.

**Team composition changes.** Cisco was a large-team engagement (up to 8+ resources over 4-9 months). Lam is likely a smaller, more specialized team. The NER/redaction work is more ML-heavy and less "factory mode" than screen conversion. The resource mix will lean toward fewer, more senior resources rather than many offshore engineers in parallel.

**POC economics may differ.** Cisco POC was zero-cost, 4 weeks, Colin solo, with the explicit goal of unlocking a $500K paid engagement. The Lam POC structure needs to reflect:
- Whether the POC is zero-cost or paid
- What the POC needs to prove (accuracy? throughput? integration feasibility?)
- What the follow-on engagement looks like (ongoing service? one-time implementation? licensed solution?)

**Margin targets may differ.** The Cisco 40%/30% floors were set for a large fixed-price engagement. A smaller Lam POC may have different margin dynamics, especially if the POC is paid and the follow-on is a different commercial model.

**Risk reserve calibration.** Cisco used 25% risk reserve. NER/redaction work has different risk factors: model accuracy uncertainty, data quality issues, regulatory requirements, integration complexity with Lam's existing systems. The risk reserve percentage may need to be higher or lower depending on how well-defined the POC scope is.

### Specific Lessons for Lam Pricing

1. **Build the internal model first, then derive the client presentation.** Never start with what the client sees. The internal model with real costs and margins is the source of truth.

2. **Multiple scenarios support negotiation.** Having July/December/Discount equivalents for Lam means Colin enters any pricing conversation with pre-calculated responses to "can you do it faster?" and "can you do it cheaper?"

3. **Never expose headcount or rates.** Present deliverables and outcomes. Lam should see phases with deliverables and prices, not people and hours.

4. **The POC investment math matters.** Cisco POC cost BayOne $8,308 (1.7% of revenue). Calculate the Lam POC cost as a percentage of the expected follow-on revenue to evaluate whether the investment is justified.

5. **Travel costs shift discount floors more than expected.** Adding $11K in travel to the December scenario dropped the maximum discount from ~28% to ~2.4% on loaded cost. For Lam (also likely requiring travel), model travel early.

6. **"Stabilization & Acceptance" framing applies universally.** Do not label any final phase as "QA." It signals a waterfall mindset. The final phase is about integration validation and stakeholder trust-building.

7. **Per-screen (per-unit) economics provide negotiation ammunition.** Cisco's $2,000/screen revenue was a clean number for quick mental math. Establish an equivalent per-unit metric for Lam (cost per document type? cost per entity class? cost per pipeline stage?) that simplifies the value conversation.

8. **The discount sensitivity table is a negotiation weapon.** Pre-calculating exact margins at every discount level means Colin never has to guess during a negotiation call. Build this for Lam before any pricing conversation.

9. **Risk reserve is the hidden negotiation lever.** At 25% risk reserve, the gap between base cost margin and loaded cost margin is significant. This gives room to present the loaded-cost margin as the "real" number while knowing the base-cost margin provides additional buffer if risk does not materialize.

10. **Throughput projections need POC calibration.** The Cisco model included detailed capacity checks (screens per engineer per week) that were explicitly labeled as assumptions to be validated by the POC. Lam pricing should include similar projections with the same caveat: these are estimates that the POC will calibrate.
