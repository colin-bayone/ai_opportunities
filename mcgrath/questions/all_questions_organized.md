# McGrath RFP Questions — Complete Organized View

**Date:** February 20, 2026
**Total:** 36 questions (19 original + 17 new)

---

## At a Glance

| Section | Original | New | Total |
|---------|----------|-----|-------|
| Scope & Transition | 6 | 5 | 11 |
| Evaluation & Selection | 2 | 2 | 4 |
| Staffing & Resources | 4 | 2 | 6 |
| Technology & Environment | 3 | 4 | 7 |
| Compliance & Audit | 0 | 1 | 1 |
| Commercial & Contractual | 4 | 3 | 7 |
| **Total** | **19** | **17** | **36** |

---

# Section 1: Scope & Transition Planning

*11 questions — understanding what we're signing up for*

## Operational Volumes

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 1 | Can MGRC provide a breakdown of current monthly ticket/service request volume by application area and by priority level (P1–P4) for the trailing 12 months? | Original | MGRC Environment / MGRC Overview |
| 2 | What is the current FTE count (internal and contractor) supporting each application area? How many are expected to transition to the MSP, remain at MGRC, or depart? | Original | MGRC Environment / MGRC Overview |
| 3 | What is the current onshore/offshore distribution of support resources, and what is the organizational structure (dedicated teams per app vs. shared pool)? | NEW | MGRC Environment |
| 4 | The RFP notes OCI effort is estimated at under 1,000 hours annually. Can MGRC provide similar annual hour estimates for other application areas? | Original | Specific Requirements / OCI, Row 48 |

## Transition Planning

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 5 | For the Knowledge Transfer phase (May 18 – July 6), will current support resources remain available during the entire transition, or is there a ramp-down schedule? | Original | Specific Requirements / General / Transition |
| 6 | Is MGRC open to a phased go-live approach where application areas transition in priority waves rather than a single July 6 go-live? | Original | Specific Requirements / General / Go-Live |
| 7 | Is the July 6 go-live date firm, or is there potential for schedule adjustment? What contingency exists if the Oracle Fusion go-live extends past May 18? | NEW | Timeline |
| 8 | Can MGRC characterize the current state of operational documentation (runbooks, SOPs, architecture diagrams) for each application area? Which areas rely on tribal knowledge? | NEW | Scope Section 4 — Documentation & KM |

## Integrations

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 9 | Of the 50+ integrations listed, how many are in production and stable vs. in active development or experiencing recurring issues? Can MGRC provide error rates for top integrations? | Original | MGRC Environment / Integration Inventory |
| 10 | When integration issues arise, does MGRC's team typically resolve them in-house, or are they escalated to software vendors like Oracle or MuleSoft? | NEW | MGRC Environment / Integration Inventory |

## Vendor Transitions

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 11 | As MGRC consolidates vendor relationships, what is the timeline for transitioning work from exiting vendors to the selected MSP(s)? Will the MSP be responsible for transition activities? | NEW | Strategic intel |

---

# Section 2: Evaluation & Selection Criteria

*4 questions — understanding how we'll be judged*

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 12 | Can MGRC share the relative weighting or ranking of the evaluation criteria (expertise, completeness, customer service, governance, vendor strength, compliance, value/TCO)? | Original | Next Steps / Selection Process |
| 13 | Does MGRC have a preference between a single MSP provider across all solution areas versus multiple providers with complementary coverage? | Original (REVISED) | Next Steps / Selection Process |
| 14 | Can MGRC share who will be participating in the evaluation process (IT, Finance, Procurement, Business Units)? | NEW | Next Steps / Selection Process |
| 15 | What role does MGRC envision AI and automation playing in managed services over the next 2-3 years? Are there specific areas where automation is a priority? | NEW | Strategic intel / Mae Roberts |

---

# Section 3: Staffing & Resource Model

*6 questions — understanding how to staff this*

## Support Model

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 16 | For US business hours support, does MGRC require dedicated named resources for each application area, or is a pooled model with SLA commitments acceptable? | Original | General Requirements / Service & Support, 4.1 |
| 17 | For dedicated resources, are there specific skill certifications or experience requirements that MGRC considers mandatory vs. preferred? | NEW | General Requirements / Service & Support |
| 18 | For after-hours data pipeline monitoring (10 PM – 7 AM PT), what is the typical nightly volume and frequency of hands-on interventions vs. next-business-day follow-up? | Original | Specific Requirements / Snowflake/Data, Rows 145–147 |

## Operational Governance

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 19 | Does MGRC have existing change management policies and maintenance schedules for the MSP to adopt, or should we propose a governance framework during Phase 1? | Original | General Requirements / Technology Management, 5.2 |
| 20 | For Oracle Fusion operations, can MGRC provide monthly volumes for period-close, journal entries, PO/invoice processing? Are there seasonal peaks requiring surge staffing? | Original | Specific Requirements / Oracle Fusion, Row 36 |

## Third-Party Coordination

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 21 | Will the MSP be expected to coordinate with third-party vendors (Oracle support, MuleSoft support, implementation partners)? Can MGRC provide a list of current vendors? | NEW | Strategic intel / Atom pain point |

---

# Section 4: Technology & Environment

*7 questions — understanding the technical landscape*

## ITSM & Tooling

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 22 | What is the expected timeline for migration from FreshService to ServiceNow? Will the MSP support both platforms during transition and play a role in the implementation? | Original | MGRC Environment / IT Service Management |
| 23 | Are there existing ITSM workflows, automations, or custom configurations in FreshService that must be migrated to ServiceNow? What is the expected MSP involvement? | NEW | MGRC Environment / IT Service Management |

## Custom Applications

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 24 | For NexSTAR (custom application), can MGRC provide documentation on the technology stack, architecture, known technical debt, and deployment pipeline? Full source code access? | Original | Specific Requirements / NexSTAR, Row 79–80 |

## Testing & QA

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 25 | What is the current state of test automation for regression, smoke, and integration testing? Would MGRC be interested in the MSP introducing automation capabilities? | NEW | Strategic intel / 100% manual testing |

## Security & Compliance

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 26 | For the Customer Hub (nopCommerce), can MGRC clarify the PCI compliance scope and whether the MSP is expected to maintain PCI certification or support MGRC's existing audit process? | Original | Specific Requirements / Customer Hub, Row 164–165 |
| 27 | Does MGRC have existing SIEM/SOC capabilities, or will the MSP be expected to provide security monitoring and incident response? | NEW | Compliance & Security Requirements |

## Disaster Recovery

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 28 | For critical systems (Oracle Fusion, NexSTAR, Customer Hub) — what are the recovery targets if there's an outage? How often are DR tests conducted, and will the MSP run those drills? | NEW | Scope Section 4 — Disaster Recovery & Backup |

---

# Section 5: Compliance & Audit

*1 question — understanding compliance burden*

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 29 | Can MGRC provide a calendar of compliance audits scheduled for the next 12 months and clarify which audits the MSP will support, lead evidence gathering for, or remediate? | NEW | Compliance & Security (Section 7) |

---

# Section 6: Commercial & Contractual

*7 questions — protecting our commercial interests*

## Pricing

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 30 | Does MGRC have a target budget range or not-to-exceed threshold that vendors should be aware of? | Original | Pricing Here / General |
| 31 | Is MGRC open to pricing models that combine fixed operational support with variable capacity for enhancement and project work? | Original (REVISED) | Pricing Here / General |
| 32 | For multi-year pricing, does MGRC expect flat pricing across Years 1–3, or is there flexibility in how pricing is structured year-over-year? | Original (REVISED) | Pricing Here / Phase 1 & 2 |

## Scope Protection

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 33 | For items designated 'Shared Responsibility,' will the RACI be finalized before contract execution or during Phase 1? How will scope disputes be resolved? | Original | General Requirements / Shared Responsibility, 2.1 |
| 34 | For scope changes after contract execution (new integrations, acquisitions, upgrades), what is MGRC's change request process? Will these be priced separately or absorbed? | NEW | General Requirements |

## M&A Impact

| # | Question | Type | RFP Ref |
|---|----------|------|---------|
| 35 | Are there pending or planned acquisitions that would affect MSP scope within the first 12 months? If so, how many and what is their general scope? | NEW | Scope — Data Management (M&A onboarding) |
| 36 | How have M&A integrations historically been handled from a support perspective? | NEW | Scope — Data Management |

---

# Summary

## By Type
- **Original (unchanged):** 16
- **Original (revised):** 3 — Q13, Q31, Q32
- **New (gap analysis):** 17

## By Purpose
- **Scope clarity:** 18 questions
- **Risk mitigation:** 8 questions
- **Pricing protection:** 4 questions
- **Evaluation intel:** 4 questions
- **Competitive intel:** 2 questions

## Removed
- Original Q9 (Incumbent Advantage) — too aggressive

## Risk Flags (Minor)
- Q6 (Phased go-live) — could imply hesitation
- Q7 (July readiness) — could reveal nervousness
- Q8 (Documentation) — "tribal knowledge" phrasing
- Q25 (Testing/QA) — proactively offers automation
