# Existing RFP Questions (Original 20)

**Source:** Initial BayOne draft
**Date:** February 20, 2026

---

## Revisions Summary

| Original # | Status | Change |
|------------|--------|--------|
| Q8 | **REVISED** | Removed specific split example ("Salesforce/CRM... Oracle ERP") that revealed our thinking |
| Q9 | **REMOVED** | Too aggressive — signals "we're the incumbent, favor us" |
| Q18 | **REVISED** | Made neutral — removed specific hybrid model description |
| Q19 | **REVISED** | Made neutral — removed "Year 1 onboarding investment" language |

---

## Category 1: Scope & Transition Planning

### Q1: Ticket Volume Data

| | |
|---|---|
| **RFP Reference** | MGRC Environment / MGRC Overview |
| **Question** | Can MGRC provide a breakdown of current monthly ticket/service request volume by application area (Salesforce, Oracle Fusion, OCI, NexSTAR, integrations, etc.) and by priority level (P1–P4) for the trailing 12 months? |
| **Why We Ask** | Single most important data point for our cost model. Without ticket volume by app and severity, we're guessing on team size. Every other MSP will ask this too — not asking makes us look unsophisticated. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | None |

---

### Q2: Current FTE Count

| | |
|---|---|
| **RFP Reference** | MGRC Environment / MGRC Overview |
| **Question** | What is the current FTE count (internal and external/contractor) supporting each application area today? How many of these resources are expected to transition to the MSP, remain at MGRC, or depart during the onboarding period? |
| **Why We Ask** | Tells us how many people do this work today = how many we likely need. Also reveals whether MGRC expects us to absorb their existing contractors (rebadge) or bring entirely new staff. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | None |

---

### Q3: KT Period Resource Availability

| | |
|---|---|
| **RFP Reference** | Specific Requirements / General / Transition |
| **Question** | For the Knowledge Transfer phase (May 18 – July 6), will MGRC's current support resources remain fully available to shadow and co-work with MSP staff during the entire transition period, or is there an expected ramp-down schedule for current resources? |
| **Why We Ask** | If current staff leave before KT is complete, we have a coverage gap. We need to price for parallel running costs and potentially a longer stabilization period. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | Low |

---

### Q4: Phased Go-Live Approach

| | |
|---|---|
| **RFP Reference** | Specific Requirements / General / Go-Live |
| **Question** | Is MGRC open to a phased go-live approach where application areas are transitioned in priority waves rather than a single go-live date of July 6 for all areas? |
| **Why We Ask** | Phased approach dramatically reduces our delivery risk and lets us demonstrate early wins. Also gives us time to ramp on complex areas like Oracle Fusion full suite. Signals we're thinking pragmatically, not just saying yes to everything. |
| **Strategic Purpose** | Risk mitigation |
| **Sensitivity** | Low |
| **Risk Flag** | Minor — could imply hesitation about going live all at once. However, phased transitions are industry best practice. |

---

### Q5: Integration Stability Status

| | |
|---|---|
| **RFP Reference** | MGRC Environment / Integration Inventory |
| **Question** | Of the 50+ integrations listed, how many are currently in production and stable versus in active development or experiencing recurring issues? Can MGRC provide error/failure rates for the top integrations by volume? |
| **Why We Ask** | A stable integration needs monitoring; one with recurring issues needs engineering. This distinction could mean the difference between 2 integration engineers and 5. Shows we understand the integration complexity deeply. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | Low |

---

### Q6: Annual Hour Estimates

| | |
|---|---|
| **RFP Reference** | Specific Requirements / OCI, Row 48 |
| **Question** | The RFP notes OCI effort is estimated at under 1,000 hours annually. Can MGRC provide similar annual hour estimates for other application areas to help vendors right-size proposals? |
| **Why We Ask** | If they gave us 1,000 hours for OCI, they likely have internal estimates for other areas too. Getting these numbers lets us price far more accurately than competitors who are guessing. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | Low |

---

## Category 2: Evaluation & Selection Criteria

### Q7: Evaluation Criteria Weighting

| | |
|---|---|
| **RFP Reference** | Next Steps / Selection Process |
| **Question** | Can MGRC share the relative weighting or ranking of the evaluation criteria listed (expertise, completeness, customer service, governance, vendor strength, compliance, value/TCO)? |
| **Why We Ask** | If price is 50% of the score we need to be aggressive on cost. If expertise is weighted highest, we lean hard into our institutional knowledge. This shapes everything. |
| **Strategic Purpose** | Evaluation intel |
| **Sensitivity** | None |

---

### Q8: Multi-MSP vs Single Provider — REVISED

| | |
|---|---|
| **RFP Reference** | Next Steps / Selection Process |
| **Original** | Is MGRC open to awarding the MSP engagement to more than one provider with complementary specializations (e.g., one MSP for Salesforce/CRM ecosystem and another for Oracle ERP/infrastructure), or is the strong preference for a single provider across all solution areas? |
| **Revised** | Does MGRC have a preference between a single MSP provider across all solution areas versus multiple providers with complementary coverage? |
| **Why Revised** | Original revealed exactly which split we're considering. Revision asks same question without telegraphing our thinking. |
| **Why We Ask** | THIS IS OUR MOST IMPORTANT STRATEGIC QUESTION. If multi-vendor is acceptable, we can bid confidently on our strongest areas. If single-vendor only, we need a consortium response. The answer fundamentally changes our bid strategy. |
| **Strategic Purpose** | Evaluation intel |
| **Sensitivity** | Medium |

---

### ~~Q9: Incumbent Advantage Weighting~~ — REMOVED

| | |
|---|---|
| **RFP Reference** | Experience & Methodology / MSP Methodology, 1.4 |
| **Original** | For vendors who currently have resources supporting MGRC operations, how will demonstrated institutional knowledge, existing relationships, and reduced transition risk be weighted in the evaluation? |
| **Why Removed** | Too aggressive. Essentially a neon sign saying "WE ARE THE INCUMBENT, PLEASE WEIGH THIS IN OUR FAVOR." Will hurt us more than help. |

---

## Category 3: Staffing & Resource Model

### Q10: Dedicated vs Pooled Resources

| | |
|---|---|
| **RFP Reference** | General Requirements / Service & Support, 4.1 |
| **Question** | For US business hours support (5 AM – 5 PM PST), does MGRC require dedicated named resources assigned exclusively to MGRC for each application area, or is a shared/pooled resource model with guaranteed response SLAs acceptable? |
| **Why We Ask** | Named dedicated resources = significantly higher cost (10–15 FTEs minimum). A pooled model with SLA commitments lets us staff more efficiently. This is potentially a $500K+ annual pricing difference. |
| **Strategic Purpose** | Pricing protection |
| **Sensitivity** | Low |

---

### Q11: After-Hours Monitoring Requirements

| | |
|---|---|
| **RFP Reference** | Specific Requirements / Snowflake/Data, Rows 145–147 |
| **Question** | For after-hours data pipeline monitoring (10 PM – 7 AM PT), what is the typical nightly volume of pipeline runs and average frequency of interventions requiring hands-on remediation versus automated alerting with next-business-day follow-up? |
| **Why We Ask** | If it's mostly passive monitoring with rare interventions, a small offshore NOC team works. If nightly hands-on fixes are common, we need skilled engineers on night shift. Huge cost difference. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | None |

---

### Q12: Change Management Policies

| | |
|---|---|
| **RFP Reference** | General Requirements / Technology Management, 5.2 |
| **Question** | Does MGRC have existing change management policies and maintenance schedules for the MSP to adopt, or should we propose a governance framework during Phase 1? |
| **Why We Ask** | Adopting existing processes = less Phase 1 effort. Building from scratch = significant Phase 1 scope and cost. Also tells us how mature their operational governance is. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | None |

---

### Q13: Oracle Fusion Volumes

| | |
|---|---|
| **RFP Reference** | Specific Requirements / Oracle Fusion, Row 36 |
| **Question** | For Oracle Fusion day-to-day operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, PO/invoice processing, and service requests? Are there seasonal peaks (quarter-end, year-end) that require surge staffing? |
| **Why We Ask** | Oracle Fusion ops is the single largest scope item. Volume data lets us staff accurately. The seasonal peak question shows we understand ERP operations — most MSPs won't think to ask this. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | Low |

---

## Category 4: Technology & Environment Specifics

### Q14: ServiceNow Migration Timeline

| | |
|---|---|
| **RFP Reference** | MGRC Environment / IT Service Management |
| **Question** | What is the expected timeline for migration from FreshService to ServiceNow (or similar)? Will the MSP be expected to support both platforms during transition, and is the MSP expected to play a role in the ServiceNow implementation itself? |
| **Why We Ask** | Dual-platform support is expensive. If we're also part of the ServiceNow migration, that's a separate workstream. The answer affects our tooling investment and resource skills. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | None |

---

### Q15: NexSTAR Technical Details

| | |
|---|---|
| **RFP Reference** | Specific Requirements / NexSTAR, Row 79–80 |
| **Question** | For NexSTAR (custom application), can MGRC provide documentation on the technology stack, codebase language/framework, architecture diagrams, known technical debt, and deployment pipeline? Will the MSP have full source code and development environment access? |
| **Why We Ask** | Custom apps are the highest-risk area. Without knowing the stack, we can't staff appropriately. If it's .NET on Azure that's different from Java or something proprietary. The 24x7 requirement for a custom app makes this even more critical to understand. |
| **Strategic Purpose** | Scope clarity |
| **Sensitivity** | Low |

---

### Q16: PCI Compliance Scope

| | |
|---|---|
| **RFP Reference** | Specific Requirements / Customer Hub, Row 164–165 |
| **Question** | For the Customer Hub (nopCommerce), can MGRC clarify the PCI compliance scope and whether the MSP is expected to maintain PCI certification or support MGRC's existing audit process? |
| **Why We Ask** | PCI responsibility for a customer-facing payment portal is a significant compliance obligation. If we're the ones holding PCI accountability, our security costs and insurance requirements increase substantially. |
| **Strategic Purpose** | Risk mitigation |
| **Sensitivity** | Low |

---

## Category 5: Commercial & Contractual

### Q17: Budget Range

| | |
|---|---|
| **RFP Reference** | Pricing Here / General |
| **Question** | Does MGRC have a target budget range or not-to-exceed threshold for the MSP engagement that vendors should be aware of when structuring proposals? |
| **Why We Ask** | Saves everyone time. If their budget is $2M/year and we price at $4M, we're wasting effort. Most companies won't share exact numbers, but sometimes they'll give a range or confirm "you're in the ballpark" during Q&A sessions. |
| **Strategic Purpose** | Evaluation intel |
| **Sensitivity** | None |

---

### Q18: Hybrid Pricing Model — REVISED

| | |
|---|---|
| **RFP Reference** | Pricing Here / General |
| **Original** | For pricing flexibility, is MGRC open to a hybrid model combining a fixed monthly retainer for core operational support with a flexible/variable pool of hours for enhancement, transformation, and project work? Or does MGRC prefer fully fixed pricing? |
| **Revised** | Is MGRC open to pricing models that combine fixed operational support with variable capacity for enhancement and project work? |
| **Why Revised** | Original revealed our preferred commercial structure and concern about scope creep. Revision gets same intel without telegraphing. |
| **Strategic Purpose** | Pricing protection |
| **Sensitivity** | Medium (original) → Low (revised) |

---

### Q19: Multi-Year Pricing Model — REVISED

| | |
|---|---|
| **RFP Reference** | Pricing Here / Phase 1 & 2 |
| **Original** | For the multi-year pricing (Years 1–3), does MGRC expect flat pricing across all years, or is a ramp model acceptable where Year 1 pricing reflects onboarding investment with normalized pricing in Years 2–3? |
| **Revised** | For multi-year pricing, does MGRC expect flat pricing across Years 1–3, or is there flexibility in how pricing is structured year-over-year? |
| **Why Revised** | Original explicitly described our strategy (aggressive Year 1, normalize later). Revision asks about flexibility without revealing our approach. |
| **Strategic Purpose** | Pricing protection |
| **Sensitivity** | Medium (original) → Low (revised) |

---

### Q20: RACI Finalization Timing

| | |
|---|---|
| **RFP Reference** | General Requirements / Shared Responsibility, 2.1 |
| **Question** | For items designated as 'Shared Responsibility,' will the RACI and responsibility splits be finalized before contract execution, or will they be defined during the Phase 1 onboarding period? How will scope disputes in shared areas be resolved? |
| **Why We Ask** | Most of the RFP is Shared Responsibility, but the splits aren't defined yet. If we sign a fixed-price contract without clear RACI, we risk absorbing more scope than priced. This protects us contractually. |
| **Strategic Purpose** | Risk mitigation |
| **Sensitivity** | Low |

---

## Summary

| Category | Original Count | After Revisions |
|----------|---------------|-----------------|
| Scope & Transition Planning | 6 | 6 |
| Evaluation & Selection Criteria | 3 | 2 (Q9 removed) |
| Staffing & Resource Model | 4 | 4 |
| Technology & Environment | 3 | 3 |
| Commercial & Contractual | 4 | 4 |
| **Total** | **20** | **19** |
