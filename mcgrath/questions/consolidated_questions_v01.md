# McGrath RFP Questions - Consolidated Draft v01

**Date:** February 20, 2026
**Status:** Pending final competitive risk review

---

## Summary

| Source | Count |
|--------|-------|
| Original questions (refined) | 19 |
| New gap questions | 17 |
| **Total** | **36** |

---

## Section 1: Scope & Transition Planning (11 questions)

### Q1: Ticket Volume Data
**Source:** Original
**Question:** Can MGRC provide a breakdown of current monthly ticket/service request volume by application area (Salesforce, Oracle Fusion, OCI, NexSTAR, integrations, etc.) and by priority level (P1–P4) for the trailing 12 months?
**Justification:** Essential for cost model. Every MSP will ask this.

### Q2: Current FTE Count
**Source:** Original
**Question:** What is the current FTE count (internal and external/contractor) supporting each application area today? How many of these resources are expected to transition to the MSP, remain at MGRC, or depart during the onboarding period?
**Justification:** Standard scoping — tells us team size needed.

### Q3: KT Period Resource Availability
**Source:** Original
**Question:** For the Knowledge Transfer phase (May 18 – July 6), will MGRC's current support resources remain fully available to shadow and co-work with MSP staff during the entire transition period, or is there an expected ramp-down schedule for current resources?
**Justification:** Coverage gap risk if staff leave before KT complete.

### Q4: Phased Go-Live Approach
**Source:** Original
**Question:** Is MGRC open to a phased go-live approach where application areas are transitioned in priority waves rather than a single go-live date of July 6 for all areas?
**Justification:** De-risks delivery; shows pragmatic thinking.
**Risk Flag:** Minor — could imply hesitation about going live all at once. However, phased transitions are industry best practice. Positions us as pragmatic, not uncertain. **Recommendation: KEEP**

### Q5: Integration Stability Status
**Source:** Original
**Question:** Of the 50+ integrations listed, how many are currently in production and stable versus in active development or experiencing recurring issues? Can MGRC provide error/failure rates for the top integrations by volume?
**Justification:** Stable vs troubled integrations = different staffing. Shows we understand complexity.

### Q6: Annual Hour Estimates
**Source:** Original
**Question:** The RFP notes OCI effort is estimated at under 1,000 hours annually. Can MGRC provide similar annual hour estimates for other application areas to help vendors right-size proposals?
**Justification:** Smart catch from RFP; helps accurate pricing.

### Q7: FTE Details (Depth Gap - builds on Q2)
**Source:** Gap — Depth
**Question:** What is the current onshore/offshore distribution of support resources, and what is the organizational structure (e.g., dedicated teams per app vs. shared pool)?
**Justification:** Understanding current model helps us staff appropriately.

### Q8: Integration Ownership (Depth Gap - builds on Q5)
**Source:** Gap — Depth
**Question:** As a follow-up on integration stability: when integration issues arise, does MGRC's team typically resolve them in-house, or are they escalated to software vendors like Oracle or MuleSoft, or to the current support provider?
**Justification:** Clarifies accountability model for integrations.

### Q9: July Go-Live Readiness (Risk Gap)
**Source:** Gap — Risk
**Question:** Is the July 6 go-live date firm, or is there potential for schedule adjustment based on current project status? What contingency exists if the Oracle Fusion go-live extends past May 18?
**Justification:** Shows dependency awareness. Colin note: important to understand timeline risk.
**Risk Flag:** Minor — asking if date is "firm" could reveal timeline nervousness. However, this levels the info field — large MSPs know the Oracle Fusion status internally; asking formally gets it on record. **Recommendation: KEEP**

### Q10: Vendor Consolidation Impact (Risk Gap)
**Source:** Gap — Risk
**Question:** As MGRC consolidates vendor relationships, what is the expected timeline for transitioning work from exiting vendors to the selected MSP(s)? Will the MSP be responsible for any transition activities from other vendors?
**Justification:** Hidden scope risk from vendor transitions.

### Q11: Documentation State (Topic Gap)
**Source:** Gap — Topic
**Question:** Can MGRC characterize the current state of operational documentation (runbooks, SOPs, architecture diagrams) for each application area? Which areas are well-documented vs. relying primarily on tribal knowledge?
**Justification:** Poor documentation = longer KT, higher transition risk.
**Risk Flag:** Minor — "tribal knowledge" phrasing could imply KT concerns that large embedded teams wouldn't have. However, documentation quality affects any transition. Standard due diligence; positions us as thorough. **Recommendation: KEEP**

---

## Section 2: Evaluation & Selection Criteria (4 questions)

### Q12: Evaluation Criteria Weighting
**Source:** Original
**Question:** Can MGRC share the relative weighting or ranking of the evaluation criteria listed (expertise, completeness, customer service, governance, vendor strength, compliance, value/TCO)?
**Justification:** Shapes where we emphasize in proposal. Every bidder asks this.

### Q13: Multi-MSP vs Single Provider (REVISED)
**Source:** Original — Refined
**Original:** Is MGRC open to awarding the MSP engagement to more than one provider with complementary specializations (e.g., one MSP for Salesforce/CRM ecosystem and another for Oracle ERP/infrastructure), or is the strong preference for a single provider across all solution areas?
**Revised Question:** Does MGRC have a preference between a single MSP provider across all solution areas versus multiple providers with complementary coverage?
**Justification:** Critical strategic question. Revision removes specific split example that revealed our thinking.

### Q14: Evaluation Committee Composition (Competitive Intel Gap)
**Source:** Gap — Competitive Intel
**Question:** Can MGRC share who will be participating in the evaluation process (e.g., IT, Finance, Procurement, Business Units)?
**Justification:** Helps tailor messaging to evaluators. Standard process question.

### Q15: AI/Automation Priorities (Competitive Intel Gap)
**Source:** Gap — Competitive Intel
**Question:** What role does MGRC envision AI and automation playing in managed services over the next 2-3 years? Are there specific areas where automation is a priority?
**Justification:** Mae flagged AI as differentiator. Colin note: Everyone else positions around AI too — levels the field.

---

## Section 3: Staffing & Resource Model (6 questions)

### Q16: Dedicated vs Pooled Resources
**Source:** Original
**Question:** For US business hours support (5 AM – 5 PM PST), does MGRC require dedicated named resources assigned exclusively to MGRC for each application area, or is a shared/pooled resource model with guaranteed response SLAs acceptable?
**Justification:** $500K+ annual pricing difference based on answer.

### Q17: After-Hours Monitoring Requirements
**Source:** Original
**Question:** For after-hours data pipeline monitoring (10 PM – 7 AM PT), what is the typical nightly volume of pipeline runs and average frequency of interventions requiring hands-on remediation versus automated alerting with next-business-day follow-up?
**Justification:** Passive monitoring vs active engineering = huge cost difference.

### Q18: Change Management Policies
**Source:** Original
**Question:** Does MGRC have existing documented change management policies, CAB processes, and maintenance window schedules that the MSP should adopt? Or is the MSP expected to design and implement these frameworks as part of Phase 1?
**Justification:** Adopting existing vs building from scratch = different Phase 1 scope.

### Q19: Oracle Fusion Volumes
**Source:** Original
**Question:** For Oracle Fusion day-to-day operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, PO/invoice processing, and service requests? Are there seasonal peaks (quarter-end, year-end) that require surge staffing?
**Justification:** Largest scope item. Seasonal peak question shows ERP ops maturity.

### Q20: Skill Requirements (Depth Gap - builds on Q16)
**Source:** Gap — Depth
**Question:** For dedicated resources, what skill certifications or experience levels are required (e.g., Oracle Fusion Cloud certified, Salesforce Admin certified)? Are there any that aren't required but would be preferred?
**Justification:** Staffing accuracy; distinguishes required vs nice-to-have.

### Q21: Vendor Management (Topic Gap)
**Source:** Gap — Topic
**Question:** Will the MSP be expected to coordinate with or manage relationships with third-party vendors (e.g., Oracle support, MuleSoft support, implementation partners)? If so, can MGRC provide a list of current third-party vendors and their support scope?
**Justification:** Strategic intel flagged Atom as pain point. This is potential high-value scope for BayOne.

---

## Section 4: Technology & Environment (7 questions)

### Q22: ServiceNow Migration Timeline
**Source:** Original
**Question:** What is the expected timeline for migration from FreshService to ServiceNow (or similar)? Will the MSP be expected to support both platforms during transition, and is the MSP expected to play a role in the ServiceNow implementation itself?
**Justification:** Dual-platform support and migration involvement = different scope.

### Q23: NexSTAR Technical Details
**Source:** Original
**Question:** For NexSTAR (custom application), can MGRC provide documentation on the technology stack, codebase language/framework, architecture diagrams, known technical debt, and deployment pipeline? Will the MSP have full source code and development environment access?
**Justification:** Custom apps are highest risk. 24x7 requirement makes this critical.

### Q24: PCI Compliance Scope
**Source:** Original
**Question:** For the Customer Hub (nopCommerce), can MGRC confirm the current PCI compliance scope (SAQ type), frequency of penetration testing, and whether the MSP will be expected to maintain PCI certification on behalf of MGRC or support MGRC's own PCI audit process?
**Justification:** PCI accountability significantly affects security costs and insurance.

### Q25: ServiceNow Migration Details (Depth Gap - builds on Q22)
**Source:** Gap — Depth
**Question:** Are there existing ITSM workflows, automations, or custom configurations in FreshService that must be migrated to ServiceNow? What is the expected level of MSP involvement in the migration project?
**Justification:** Migration complexity affects Phase 1 scope.

### Q26: Testing & QA State (Topic Gap)
**Source:** Gap — Topic
**Question:** What is the current state of test automation for regression, smoke, and integration testing? Would MGRC be interested in the MSP introducing automation capabilities as part of the engagement?
**Justification:** Strategic intel: 100% manual testing. Probes automation appetite without revealing our approach.
**Risk Flag:** Minor — proactively offering automation in the question tips our hand slightly (pitching before the proposal). However, large MSPs also position automation as a differentiator. **Recommendation: KEEP** | Optional softer version: "What is the current state of test automation for regression, smoke, and integration testing? Are there specific QA areas where improvements are desired?"

### Q27: Security Operations (Topic Gap)
**Source:** Gap — Topic
**Question:** Does MGRC have existing SIEM/SOC capabilities, or will the MSP be expected to provide security monitoring and incident response? What is the current frequency of vulnerability scanning and penetration testing?
**Justification:** Security ops distinct from compliance — could be large hidden scope.

### Q28: Disaster Recovery (Topic Gap)
**Source:** Gap — Topic
**Question:** For critical systems like Oracle Fusion, NexSTAR, and Customer Hub — what are the recovery targets if there's an outage? How often are disaster recovery tests conducted, and will the MSP be expected to plan and run those drills?
**Justification:** DR testing effort ranges widely. Modified to remove jargon.

---

## Section 5: Compliance & Audit (1 question)

### Q29: Compliance Audit Calendar (Topic Gap)
**Source:** Gap — Topic
**Question:** Can MGRC provide a calendar of compliance audits scheduled for the next 12 months and clarify which audits the MSP will be expected to support, lead evidence gathering for, or remediate findings from?
**Justification:** 8 compliance frameworks listed. Unknown effort implications — potential hidden scope.

---

## Section 6: Commercial & Contractual (7 questions)

### Q30: Budget Range
**Source:** Original
**Question:** Does MGRC have a target budget range or not-to-exceed threshold for the MSP engagement that vendors should be aware of when structuring proposals?
**Justification:** Rarely answered directly but worth asking. Prevents wasted effort.

### Q31: Hybrid Pricing Model (REVISED)
**Source:** Original — Refined
**Original:** For pricing flexibility, is MGRC open to a hybrid model combining a fixed monthly retainer for core operational support with a flexible/variable pool of hours for enhancement, transformation, and project work? Or does MGRC prefer fully fixed pricing?
**Revised Question:** Is MGRC open to pricing models that combine fixed operational support with variable capacity for enhancement and project work?
**Justification:** Gets same intel without revealing our commercial preference.

### Q32: Multi-Year Pricing Model (REVISED)
**Source:** Original — Refined
**Original:** For the multi-year pricing (Years 1–3), does MGRC expect flat pricing across all years, or is a ramp model acceptable where Year 1 pricing reflects onboarding investment with normalized pricing in Years 2–3?
**Revised Question:** For multi-year pricing, does MGRC expect flat pricing across Years 1–3, or is there flexibility in how pricing is structured year-over-year?
**Justification:** Gets same intel without describing our exact strategy.

### Q33: RACI Finalization Timing
**Source:** Original
**Question:** For items designated as 'Shared Responsibility,' will the RACI and responsibility splits be finalized before contract execution, or will they be defined during the Phase 1 onboarding period? How will scope disputes in shared areas be resolved?
**Justification:** Most of RFP is Shared Responsibility. Protects against undefined scope.

### Q34: Scope Change Control (Risk Gap)
**Source:** Gap — Risk
**Question:** For scope changes identified after contract execution (e.g., new integrations, acquisitions, system upgrades), what is MGRC's change request and approval process? Will these be priced separately or absorbed into the base contract?
**Justification:** Protects against post-contract scope creep.

### Q35: M&A Activity — Pending Acquisitions (Risk Gap)
**Source:** Gap — Risk
**Question:** Are there pending or planned acquisitions that would affect MSP scope within the first 12 months? If so, how many and what is their general scope?
**Justification:** M&A onboarding listed as service domain. Could add significant scope.

### Q36: M&A Activity — Historical Handling (Risk Gap)
**Source:** Gap — Risk
**Question:** How have M&A integrations historically been handled from a support perspective?
**Justification:** Understanding past approach helps us plan for future acquisitions.

---

## Removed Questions

### Original Q9: Incumbent Advantage Weighting
**Original:** For vendors who currently have resources supporting MGRC operations, how will demonstrated institutional knowledge, existing relationships, and reduced transition risk be weighted in the evaluation?
**Decision:** Remove entirely
**Reason:** Will hurt us. Too aggressive; signals "we're the incumbent, favor us."

---

## Pending: Final Competitive Risk Review

This draft will undergo one more review focused on:
- Questions that reveal too much given competitive landscape
- Questions where larger MSPs (100-200 embedded) already have answers via internal channels
- Balance: enlightening to us without advantaging competitors
