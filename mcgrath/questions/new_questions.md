# New RFP Questions (Added via Gap Analysis)

**Source:** Gap analysis review with Colin Moore
**Date:** February 20, 2026
**Total:** 17 new questions

---

## Topic Gaps (6 questions)

These fill areas where we had ZERO questions.

---

### Compliance Audit Calendar

| | |
|---|---|
| **Gap Filled** | Compliance & Security (Section 7) — 8 frameworks listed, only PCI touched |
| **RFP Reference** | Compliance & Security Requirements |
| **Question** | Can MGRC provide a calendar of compliance audits scheduled for the next 12 months and clarify which audits the MSP will be expected to support, lead evidence gathering for, or remediate findings from? |
| **Why We Ask** | We don't know audit frequency, remediation backlog, or which audits MSP must support. Could be significant hidden scope — audits could be 50+ hours or 500+ annually. |
| **Risk Level** | Low |

---

### Disaster Recovery

| | |
|---|---|
| **Gap Filled** | DR/backup listed as service domain but no questions asked |
| **RFP Reference** | Scope of Services (Section 4) — Disaster Recovery & Backup |
| **Question** | For critical systems like Oracle Fusion, NexSTAR, and Customer Hub — what are the recovery targets if there's an outage? How often are disaster recovery tests conducted, and will the MSP be expected to plan and run those drills? |
| **Why We Ask** | RTO/RPO expectations directly impact staffing and tooling. DR testing could range widely in effort. |
| **Note** | Modified from original to remove jargon (RTO/RPO) |
| **Risk Level** | Low |

---

### Vendor Management

| | |
|---|---|
| **Gap Filled** | Strategic intel flags Atom as problematic; consolidation from 20 vendors happening |
| **RFP Reference** | Scope of Services — Integration & Connectivity; Strategic intel from contractor calls |
| **Question** | Will the MSP be expected to coordinate with or manage relationships with third-party vendors (e.g., Oracle support, MuleSoft support, implementation partners)? If so, can MGRC provide a list of current third-party vendors and their support scope? |
| **Why We Ask** | MSP may inherit coordination responsibility for multiple vendors. This is potential high-value scope BayOne could capture. Atom was explicitly flagged as a pain point. |
| **Risk Level** | Low |

---

### Testing & QA State

| | |
|---|---|
| **Gap Filled** | Strategic intel: "100% manual testing — no automation" |
| **RFP Reference** | Strategic intel from Reena (QA Coordinator) |
| **Question** | What is the current state of test automation for regression, smoke, and integration testing? Would MGRC be interested in the MSP introducing automation capabilities as part of the engagement? |
| **Why We Ask** | If MSP inherits QA responsibility, automation state affects staffing. Also signals potential value-add opportunity. |
| **Note** | Modified to probe automation appetite without revealing we see this as an upsell |
| **Risk Flag** | Minor — proactively offering automation tips our hand slightly |
| **Risk Level** | Low |

---

### Security Operations

| | |
|---|---|
| **Gap Filled** | Daily security ops not addressed — only compliance mentioned |
| **RFP Reference** | Compliance & Security Requirements; Scope of Services — Security & Compliance |
| **Question** | Does MGRC have existing SIEM/SOC capabilities, or will the MSP be expected to provide security monitoring and incident response? |
| **Why We Ask** | SIEM monitoring and incident response are distinct from compliance. Could be large hidden scope. |
| **Note** | Simplified — removed vulnerability scanning/pen testing frequency (audit-level detail) |
| **Risk Level** | Low |

---

### Documentation & Knowledge Management

| | |
|---|---|
| **Gap Filled** | Listed as service domain but no questions about current state |
| **RFP Reference** | Scope of Services (Section 4) — Documentation & KM |
| **Question** | Can MGRC characterize the current state of operational documentation (runbooks, SOPs, architecture diagrams) for each application area? Which areas are well-documented vs. relying primarily on tribal knowledge? |
| **Why We Ask** | Poor documentation = longer KT, higher transition risk. Understanding baseline helps price accurately. |
| **Risk Flag** | Minor — "tribal knowledge" phrasing could imply KT concerns |
| **Risk Level** | Low |

---

## Depth Gaps (4 questions)

These add depth to existing questions.

---

### FTE Details

| | |
|---|---|
| **Builds On** | Q2 (Current FTE Count) — asks headcount but not structure |
| **RFP Reference** | MGRC Environment / MGRC Overview |
| **Question** | What is the current onshore/offshore distribution of support resources, and what is the organizational structure (e.g., dedicated teams per app vs. shared pool)? |
| **Why We Ask** | Understanding current model helps us staff appropriately and match their existing structure. |
| **Risk Level** | Low |

---

### ServiceNow Migration Details

| | |
|---|---|
| **Builds On** | Q14 (ServiceNow Migration Timeline) — asks timeline but not complexity |
| **RFP Reference** | MGRC Environment / IT Service Management |
| **Question** | Are there existing ITSM workflows, automations, or custom configurations in FreshService that must be migrated to ServiceNow? What is the expected level of MSP involvement in the migration project? |
| **Why We Ask** | Migration complexity affects Phase 1 scope. Custom configurations could significantly increase effort. |
| **Risk Level** | Low |

---

### Integration Ownership

| | |
|---|---|
| **Builds On** | Q5 (Integration Stability) — asks about failure rates but not accountability |
| **RFP Reference** | MGRC Environment / Integration Inventory |
| **Question** | As a follow-up on integration stability: when integration issues arise, does MGRC's team typically resolve them in-house, or are they escalated to software vendors like Oracle or MuleSoft, or to the current support provider? |
| **Why We Ask** | Clarifies accountability model for integrations. Affects how we staff and what expertise we need. |
| **Note** | Modified for clearer escalation framing |
| **Risk Level** | Low |

---

### Skill Requirements

| | |
|---|---|
| **Builds On** | Q10 (Dedicated vs Pooled Resources) — asks about model but not skill requirements |
| **RFP Reference** | General Requirements / Service & Support, 4.1 |
| **Question** | For dedicated resources, are there specific skill certifications or experience requirements that MGRC considers mandatory vs. preferred? |
| **Why We Ask** | Staffing accuracy — distinguishes required vs nice-to-have certifications. Affects recruiting and pricing. |
| **Note** | Simplified to remove example certifications (avoid looking like we're checking boxes) |
| **Risk Level** | Low |

---

## Risk Gaps (5 questions)

These probe uncertainties and risks in the RFP.

---

### July Go-Live Readiness

| | |
|---|---|
| **Risk Area** | Strategic intel mentions SIT2/UAT overlap and resource pressure |
| **RFP Reference** | Specific Requirements / General / Go-Live; Timeline |
| **Question** | Is the July 6 go-live date firm, or is there potential for schedule adjustment based on current project status? What contingency exists if the Oracle Fusion go-live extends past May 18? |
| **Why We Ask** | If project slips, MSP transition timeline compresses or extends. Shows dependency awareness. |
| **Colin Note** | Important to understand timeline risk |
| **Risk Flag** | Minor — asking if date is "firm" could reveal nervousness. However, levels the info field. |
| **Risk Level** | Medium |

---

### Scope Change Control

| | |
|---|---|
| **Risk Area** | Q20 asks about RACI but not change control process |
| **RFP Reference** | General Requirements / Shared Responsibility |
| **Question** | For scope changes identified after contract execution (e.g., new integrations, acquisitions, system upgrades), what is MGRC's change request and approval process? Will these be priced separately or absorbed into the base contract? |
| **Why We Ask** | Protects against post-contract scope creep. M&A, new integrations, upgrades could expand scope. |
| **Risk Level** | Low |

---

### M&A Activity — Pending Acquisitions

| | |
|---|---|
| **Risk Area** | RFP mentions M&A onboarding as service domain — could add significant scope |
| **RFP Reference** | Scope of Services — Data Management (M&A onboarding) |
| **Question** | Are there pending or planned acquisitions that would affect MSP scope within the first 12 months? If so, how many and what is their general scope? |
| **Why We Ask** | M&A onboarding listed as service domain. Need to understand if this is theoretical or imminent. |
| **Note** | Split from original into two questions — this covers future |
| **Risk Level** | Medium |

---

### M&A Activity — Historical Handling

| | |
|---|---|
| **Risk Area** | Understanding past approach helps us plan |
| **RFP Reference** | Scope of Services — Data Management (M&A onboarding) |
| **Question** | How have M&A integrations historically been handled from a support perspective? |
| **Why We Ask** | Past approach informs expectations. If M&A has been chaotic, we need to price for that. |
| **Note** | Split from original — this covers historical |
| **Risk Level** | Low |

---

### Vendor Consolidation Impact

| | |
|---|---|
| **Risk Area** | MGRC consolidating 20 vendors to 3-10 — transition complexity |
| **RFP Reference** | Strategic intel; Timeline |
| **Question** | As MGRC consolidates vendor relationships, what is the expected timeline for transitioning work from exiting vendors to the selected MSP(s)? Will the MSP be responsible for any transition activities from other vendors? |
| **Why We Ask** | Hidden scope risk. We may inherit work from exiting vendors, which affects Phase 1 effort. |
| **Risk Level** | Low |

---

## Competitive Intel Gaps (2 questions)

These help us understand the evaluation landscape.

---

### AI/Automation Priorities

| | |
|---|---|
| **Intel Need** | Mae flagged AI as differentiator |
| **RFP Reference** | Strategic intel from Mae Roberts; Win Strategy 4 (AI & Automation Capabilities) |
| **Question** | What role does MGRC envision AI and automation playing in managed services over the next 2-3 years? Are there specific areas where automation is a priority? |
| **Why We Ask** | Helps us emphasize right capabilities. Positions BayOne's automation roadmap. |
| **Colin Note** | Everyone else would be positioning around AI too — asking this levels the field |
| **Risk Level** | Medium |

---

### Evaluation Committee Composition

| | |
|---|---|
| **Intel Need** | Knowing who evaluates helps tailor messaging |
| **RFP Reference** | Next Steps / Selection Process |
| **Question** | Can MGRC share who will be participating in the evaluation process (e.g., IT, Finance, Procurement, Business Units)? |
| **Why We Ask** | Helps tailor proposal messaging to actual evaluators. Standard process question. |
| **Risk Level** | Low |

---

## Skipped Gaps (4 questions)

These were considered but rejected.

| Gap | Why Skipped |
|-----|-------------|
| Phased Go-Live depth (why needed?) | Asking "why" implies we're worried about timeline |
| Subcontractor Approval | Tips our hand that we might have capability gaps |
| Number of Bidders | Rarely answered; limited value |
| Previous MSP Experience | Obviously they haven't done similar scope before |

---

## Summary

| Type | Count |
|------|-------|
| Topic Gaps | 6 |
| Depth Gaps | 4 |
| Risk Gaps | 5 |
| Competitive Intel | 2 |
| **Total Added** | **17** |
| Skipped | 4 |
