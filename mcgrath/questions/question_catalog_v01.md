# McGrath RFP Questions - Catalog v01

**Date:** February 20, 2026
**Cataloged by:** Session B
**Source:** McGrath RFP Questions BayOne_plaintext.txt

## Summary Statistics

- **Total questions:** 20
- **By category:**
  - Scope & Transition Planning: 6
  - Evaluation & Selection Criteria: 3
  - Staffing & Resource Model: 4
  - Technology & Environment Specifics: 3
  - Commercial & Contractual: 4
- **By strategic purpose:**
  - Scope clarity: 11
  - Evaluation intel: 3
  - Pricing protection: 3
  - Competitive signal: 1
  - Risk mitigation: 2
- **Sensitivity distribution:**
  - None: 7
  - Low: 9
  - Medium: 4
  - High: 0

---

## Category 1: Scope & Transition Planning

### Q1: Ticket Volume Data

- **RFP Reference:** MGRC Environment / MGRC Overview
- **Question:** Can MGRC provide a breakdown of current monthly ticket/service request volume by application area (Salesforce, Oracle Fusion, OCI, NexSTAR, integrations, etc.) and by priority level (P1–P4) for the trailing 12 months?
- **Internal Rationale:** This is the single most important data point for our cost model. Without ticket volume by app and severity, we're guessing on team size. Every other MSP will ask this too — not asking it makes us look unsophisticated.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** None — Any MSP would ask this; it's fundamental to pricing.

### Q2: Current FTE Count

- **RFP Reference:** MGRC Environment / MGRC Overview
- **Question:** What is the current FTE count (internal and external/contractor) supporting each application area today? How many of these resources are expected to transition to the MSP, remain at MGRC, or depart during the onboarding period?
- **Internal Rationale:** Tells us how many people do this work today = how many we likely need. Also reveals whether MGRC expects us to absorb their existing contractors (rebadge) or bring entirely new staff.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** None — Standard MSP scoping question.

### Q3: KT Period Resource Availability

- **RFP Reference:** Specific Requirements / General / Transition
- **Question:** For the Knowledge Transfer phase (May 18 – July 6), will MGRC's current support resources remain fully available to shadow and co-work with MSP staff during the entire transition period, or is there an expected ramp-down schedule for current resources?
- **Internal Rationale:** If current staff leave before KT is complete, we have a coverage gap. We need to price for parallel running costs and potentially a longer stabilization period.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** Low — Shows we're thinking about transition risk but reveals no strategic approach.

### Q4: Phased Go-Live Approach

- **RFP Reference:** Specific Requirements / General / Go-Live
- **Question:** Is MGRC open to a phased go-live approach where application areas are transitioned in priority waves (e.g., Salesforce and integrations first, then Oracle Fusion, then BI/data platforms) rather than a single go-live date of July 6 for all areas?
- **Internal Rationale:** Phased approach dramatically reduces our delivery risk and lets us demonstrate early wins. Also gives us time to ramp on complex areas like Oracle Fusion full suite. Signals we're thinking pragmatically, not just saying yes to everything.
- **Strategic Purpose:** Risk mitigation
- **Sensitivity:** Low — Reveals preference for de-risking but this is reasonable MSP thinking.

### Q5: Integration Stability Status

- **RFP Reference:** MGRC Environment / Integration Inventory
- **Question:** Of the 50+ integrations listed, how many are currently in production and stable versus in active development or experiencing recurring issues? Can MGRC provide error/failure rates for the top integrations by volume?
- **Internal Rationale:** A stable integration needs monitoring; one with recurring issues needs engineering. This distinction could mean the difference between 2 integration engineers and 5. Also shows we understand the integration complexity deeply.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** Low — Shows deep understanding of integration complexity but doesn't reveal strategy.

### Q6: Annual Hour Estimates

- **RFP Reference:** Specific Requirements / OCI, Row 48
- **Question:** The RFP notes OCI effort is estimated at under 1,000 hours annually. Can MGRC provide similar annual hour estimates for other application areas to help vendors right-size proposals?
- **Internal Rationale:** If they gave us 1,000 hours for OCI, they likely have internal estimates for other areas too. Getting these numbers would let us price far more accurately than competitors who are guessing.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** Low — Reasonable request that any observant bidder might make.

---

## Category 2: Evaluation & Selection Criteria

### Q7: Evaluation Criteria Weighting

- **RFP Reference:** Next Steps / Selection Process
- **Question:** Can MGRC share the relative weighting or ranking of the evaluation criteria listed (expertise, completeness, customer service, governance, vendor strength, compliance, value/TCO)?
- **Internal Rationale:** If price is 50% of the score we need to be aggressive on cost. If expertise is weighted highest, we lean hard into our institutional knowledge and incumbent team. This shapes everything.
- **Strategic Purpose:** Evaluation intel
- **Sensitivity:** None — Every bidder asks about evaluation weighting.

### Q8: Multi-MSP vs Single Provider

- **RFP Reference:** Next Steps / Selection Process
- **Question:** Is MGRC open to awarding the MSP engagement to more than one provider with complementary specializations (e.g., one MSP for Salesforce/CRM ecosystem and another for Oracle ERP/infrastructure), or is the strong preference for a single provider across all solution areas?
- **Internal Rationale:** THIS IS OUR MOST IMPORTANT STRATEGIC QUESTION. If multi-vendor is acceptable, we can bid confidently on our strongest areas and potentially partner for the rest. If single-vendor only, we need to build a consortium response. The answer fundamentally changes our bid strategy.
- **Strategic Purpose:** Evaluation intel
- **Sensitivity:** Medium — Reveals we may not feel confident covering all areas independently; signals potential consortium approach.

### Q9: Incumbent Advantage Weighting

- **RFP Reference:** Experience & Methodology / MSP Methodology, 1.4
- **Question:** For vendors who currently have resources supporting MGRC operations, how will demonstrated institutional knowledge, existing relationships, and reduced transition risk be weighted in the evaluation?
- **Internal Rationale:** Subtly highlights our incumbent advantage. Forces the evaluation committee to formally acknowledge the value of existing relationships. Also signals to Mae that we already have skin in the game.
- **Strategic Purpose:** Competitive signal
- **Sensitivity:** Medium — Directly reveals incumbent status and attempts to anchor evaluation criteria in our favor.

---

## Category 3: Staffing & Resource Model

### Q10: Dedicated vs Pooled Resources

- **RFP Reference:** General Requirements / Service & Support, 4.1
- **Question:** For US business hours support (5 AM – 5 PM PST), does MGRC require dedicated named resources assigned exclusively to MGRC for each application area, or is a shared/pooled resource model with guaranteed response SLAs acceptable?
- **Internal Rationale:** Named dedicated resources = significantly higher cost (10–15 FTEs minimum). A pooled model with SLA commitments lets us staff more efficiently. This is potentially a $500K+ annual pricing difference.
- **Strategic Purpose:** Pricing protection
- **Sensitivity:** Low — Standard MSP staffing clarification question.

### Q11: After-Hours Monitoring Requirements

- **RFP Reference:** Specific Requirements / Snowflake/Data, Rows 145–147
- **Question:** For after-hours data pipeline monitoring (10 PM – 7 AM PT), what is the typical nightly volume of pipeline runs and average frequency of interventions requiring hands-on remediation versus automated alerting with next-business-day follow-up?
- **Internal Rationale:** If it's mostly passive monitoring with rare interventions, a small offshore NOC team works. If nightly hands-on fixes are common, we need skilled engineers on night shift. Huge cost difference.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** None — Technical scoping question any MSP would ask.

### Q12: Change Management Policies

- **RFP Reference:** General Requirements / Technology Management, 5.2
- **Question:** Does MGRC have existing documented change management policies, CAB processes, and maintenance window schedules that the MSP should adopt? Or is the MSP expected to design and implement these frameworks as part of Phase 1?
- **Internal Rationale:** Adopting existing processes = less Phase 1 effort. Building from scratch = significant Phase 1 scope and cost. Also tells us how mature their operational governance is.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** None — Standard operational governance question.

### Q13: Oracle Fusion Volumes

- **RFP Reference:** Specific Requirements / Oracle Fusion, Row 36
- **Question:** For Oracle Fusion day-to-day operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, PO/invoice processing, and service requests? Are there seasonal peaks (quarter-end, year-end) that require surge staffing?
- **Internal Rationale:** Oracle Fusion ops is the single largest scope item. Volume data lets us staff accurately. The seasonal peak question shows we understand ERP operations — most MSPs won't think to ask this.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** Low — Shows deep ERP ops understanding but doesn't reveal strategy.

---

## Category 4: Technology & Environment Specifics

### Q14: ServiceNow Migration Timeline

- **RFP Reference:** MGRC Environment / IT Service Management
- **Question:** What is the expected timeline for migration from FreshService to ServiceNow (or similar)? Will the MSP be expected to support both platforms during transition, and is the MSP expected to play a role in the ServiceNow implementation itself?
- **Internal Rationale:** Dual-platform support is expensive. If we're also part of the ServiceNow migration, that's a separate workstream. The answer affects our tooling investment and resource skills.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** None — Standard tooling clarification.

### Q15: NexSTAR Technical Details

- **RFP Reference:** Specific Requirements / NexSTAR, Row 79–80
- **Question:** For NexSTAR (custom application), can MGRC provide documentation on the technology stack, codebase language/framework, architecture diagrams, known technical debt, and deployment pipeline? Will the MSP have full source code and development environment access?
- **Internal Rationale:** Custom apps are the highest-risk area. Without knowing the stack, we can't staff appropriately. If it's .NET on Azure that's different from Java or something proprietary. The 24x7 requirement for a custom app makes this even more critical to understand.
- **Strategic Purpose:** Scope clarity
- **Sensitivity:** Low — Responsible technical due diligence for a custom app.

### Q16: PCI Compliance Scope

- **RFP Reference:** Specific Requirements / Customer Hub, Row 164–165
- **Question:** For the Customer Hub (nopCommerce), can MGRC confirm the current PCI compliance scope (SAQ type), frequency of penetration testing, and whether the MSP will be expected to maintain PCI certification on behalf of MGRC or support MGRC's own PCI audit process?
- **Internal Rationale:** PCI responsibility for a customer-facing payment portal is a significant compliance obligation. If we're the ones holding PCI accountability, our security costs and insurance requirements increase substantially.
- **Strategic Purpose:** Risk mitigation
- **Sensitivity:** Low — Responsible compliance clarification for payment processing.

---

## Category 5: Commercial & Contractual

### Q17: Budget Range

- **RFP Reference:** Pricing Here / General
- **Question:** Does MGRC have a target budget range or not-to-exceed threshold for the MSP engagement that vendors should be aware of when structuring proposals?
- **Internal Rationale:** Saves everyone time. If their budget is $2M/year and we price at $4M, we're wasting effort. Most companies won't share exact numbers, but sometimes they'll give a range or confirm 'you're in the ballpark' during Q&A sessions.
- **Strategic Purpose:** Evaluation intel
- **Sensitivity:** None — Every vendor asks about budget.

### Q18: Hybrid Pricing Model

- **RFP Reference:** Pricing Here / General
- **Question:** For pricing flexibility, is MGRC open to a hybrid model combining a fixed monthly retainer for core operational support with a flexible/variable pool of hours for enhancement, transformation, and project work? Or does MGRC prefer fully fixed pricing?
- **Internal Rationale:** A hybrid model plays to our strength — it lets us commit to a competitive fixed price for the base while offering flexibility that MGRC has said they value. It also protects us from scope creep on transformation work.
- **Strategic Purpose:** Pricing protection
- **Sensitivity:** Medium — Reveals our preferred commercial structure and concern about scope creep.

### Q19: Multi-Year Pricing Model

- **RFP Reference:** Pricing Here / Phase 1 & 2
- **Question:** For the multi-year pricing (Years 1–3), does MGRC expect flat pricing across all years, or is a ramp model acceptable where Year 1 pricing reflects onboarding investment with normalized pricing in Years 2–3?
- **Internal Rationale:** We may want to price Year 1 aggressively (even at lower margin) to win, then normalize in Years 2–3. Understanding their expectations prevents us from pricing ourselves out or leaving money on the table.
- **Strategic Purpose:** Pricing protection
- **Sensitivity:** Medium — Reveals potential Year 1 aggressive pricing strategy.

### Q20: RACI Finalization Timing

- **RFP Reference:** General Requirements / Shared Responsibility, 2.1
- **Question:** For items designated as 'Shared Responsibility,' will the RACI and responsibility splits be finalized before contract execution, or will they be defined during the Phase 1 onboarding period? How will scope disputes in shared areas be resolved?
- **Internal Rationale:** Most of the RFP is Shared Responsibility, but the splits aren't defined yet. If we sign a fixed-price contract without clear RACI, we risk absorbing more scope than priced. This protects us contractually.
- **Strategic Purpose:** Risk mitigation
- **Sensitivity:** Low — Responsible contractual clarification.

---

## Observations

**Category Distribution:**
- Scope & Transition Planning has the most questions (6), reflecting the significant pricing risk from undefined volumes and transition logistics.
- Evaluation & Selection Criteria has only 3 questions but includes the "most important strategic question" (Q8 on multi-MSP).
- Commercial & Contractual questions (4) focus heavily on pricing flexibility and contractual protection.

**Strategic Purpose Patterns:**
- The majority (11/20) focus on scope clarity, indicating the RFP leaves significant ambiguity in operational volumes.
- Only 1 question is explicitly designed as a competitive signal (Q9 on incumbent advantage).
- Risk mitigation questions (Q4, Q16, Q20) address transition risk, compliance, and contractual exposure.

**Sensitivity Distribution:**
- No high-sensitivity questions — the drafters avoided overtly revealing strategic weaknesses.
- 4 medium-sensitivity questions (Q8, Q9, Q18, Q19) reveal either incumbent status, pricing approach preferences, or consortium considerations.
- The remaining 16 questions are low or no sensitivity, meaning competitors would gain minimal strategic advantage from seeing them.

**Notable Observations:**
- Q8 is flagged internally as "MOST IMPORTANT STRATEGIC QUESTION" — answer fundamentally changes bid approach.
- Q9 directly highlights incumbent status; this is an aggressive competitive move.
- Q10 could represent $500K+ annual pricing difference based on answer.
- Q17 (budget question) rarely gets a direct answer but is worth asking.
- Categories 1 and 3 are most data-driven; answers here have direct cost model implications.
