# RFP Question Gap Analysis

**Date:** February 20, 2026
**Analyzed by:** Session C

---

## Executive Summary

Our 20 questions provide solid coverage of scope clarity and pricing protection but leave significant gaps in compliance/audit processes, disaster recovery, vendor management, and testing/QA areas. The biggest gap is **vendor coordination** — strategic intel explicitly identifies third-party vendor management (Atom) as a critical pain point, yet we ask zero questions about it. This is a missed opportunity to surface MGRC's need and position BayOne as the solution.

---

## Gap Categories

### Topic Gaps

Areas in the RFP with zero questions asked.

| RFP Section | Gap Description | Why It Matters | Suggested Question | Risk Level |
|-------------|-----------------|----------------|-------------------|------------|
| Compliance & Security (Section 7) | 8 compliance frameworks listed (NIST, SOC2, HIPAA, PCI, GDPR, CMMC, CPRA, ISO-27001) but only PCI touched via Q16 | We don't know audit frequency, remediation backlog, or which audits MSP must support. Could be significant hidden scope. | "Can MGRC provide a calendar of compliance audits scheduled for the next 12 months and clarify which audits the MSP will be expected to support, lead evidence gathering for, or remediate findings from?" | Low |
| Disaster Recovery (Scope Section 4) | DR/backup listed as service domain but no questions asked | RTO/RPO expectations directly impact staffing and tooling. DR testing could be 50+ hours annually or 500+. | "What are the current RTO/RPO targets for critical systems (Oracle Fusion, NexSTAR, Customer Hub)? How frequently are DR tests conducted, and will the MSP be expected to plan and execute these drills?" | Low |
| Vendor Management | Strategic intel flags Atom as problematic vendor; consolidation from 20 vendors happening | MSP may inherit coordination responsibility for multiple vendors. This is potential high-value scope BayOne could capture. | "Will the MSP be expected to coordinate with or manage relationships with third-party vendors (e.g., Oracle support, MuleSoft support, implementation partners)? If so, can MGRC provide a list of current third-party vendors and their support scope?" | Low |
| Testing & QA | Strategic intel: "100% manual testing — no automation" | If MSP inherits QA responsibility, test automation state affects staffing. Also signals potential value-add opportunity. | "What is the current state of test automation for regression, smoke, and integration testing? Are there existing test scripts or frameworks the MSP should adopt or build upon?" | Low |
| Security Operations | Daily security ops not addressed — only compliance mentioned | Vulnerability scanning, SIEM monitoring, incident response are distinct from compliance. Could be large hidden scope. | "Does MGRC have existing SIEM/SOC capabilities, or will the MSP be expected to provide security monitoring and incident response? What is the current frequency of vulnerability scanning and penetration testing?" | Low |
| Documentation & KM (Scope Section 4) | Listed as service domain but no questions about current state | Poor documentation = longer KT, higher transition risk. Understanding baseline helps price accurately. | "Can MGRC characterize the current state of operational documentation (runbooks, SOPs, architecture diagrams) for each application area? Which areas are well-documented vs. relying primarily on tribal knowledge?" | Low |

### Depth Gaps

Areas touched but not deeply enough.

| Current Question | What's Missing | Suggested Follow-up | Risk Level |
|------------------|----------------|---------------------|------------|
| Q2: Current FTE Count | Asks about headcount but not skills distribution, offshore/onshore mix, or org structure | "What is the current onshore/offshore distribution of support resources, and what is the organizational structure (e.g., dedicated teams per app vs. shared pool)?" | Low |
| Q14: ServiceNow Migration | Asks about timeline but not ITSM process maturity or custom configurations | "Are there existing ITSM workflows, automations, or custom configurations in FreshService that must be migrated to ServiceNow? What is the expected level of MSP involvement in the migration project?" | Low |
| Q5: Integration Stability | Good question on failure rates but doesn't address ownership or documentation | "For the 50+ integrations, is there clear documentation of ownership (MGRC vs. MSP vs. third-party)? Are integration specifications and error handling procedures documented?" | Low |
| Q10: Dedicated vs Pooled Resources | Asks about support model but not skill requirements per tier | "For dedicated resources, what specific skill certifications or experience levels are required (e.g., Oracle Fusion Cloud certified, Salesforce Admin certified)?" | Low |
| Q4: Phased Go-Live | Asks if open to phased approach but not why it might be needed | *Do not ask directly* — asking why implies we're worried. Better to let MGRC confirm preference without probing root cause. | Medium |

### Risk Gaps

Uncertainties or risks in the RFP that we haven't probed.

| Risk Area | Potential Impact | Suggested Question | Risk Level |
|-----------|------------------|-------------------|------------|
| July Go-Live Readiness | Strategic intel mentions SIT2/UAT overlap and resource pressure. If project slips, MSP transition timeline compresses or extends. | "Is the July 6 go-live date firm, or is there potential for schedule adjustment based on current project status? What contingency exists if the Oracle Fusion go-live extends past May 18?" | Medium |
| Subcontractor Approval | If BayOne needs partners for gaps (MuleSoft, OCI depth), approval process matters | "For vendors proposing subcontractors or named partners for specialized service areas, what is MGRC's approval process and timeline? Are there preferred or pre-approved subcontractor relationships?" | Low |
| Scope Change Control | Q20 asks about RACI but not change control process | "For scope changes identified after contract execution (e.g., new integrations, acquisitions, system upgrades), what is MGRC's change request and approval process? Will these be priced separately or absorbed into the base contract?" | Low |
| M&A Activity | RFP mentions M&A onboarding as service domain — could add significant scope | "Are there pending or planned acquisitions that would affect MSP scope within the first 12 months? How have M&A integrations historically been handled from a support perspective?" | Medium |
| Vendor Consolidation Impact | MGRC consolidating 20 vendors to 3-10 — transition complexity | "As MGRC consolidates vendor relationships, what is the expected timeline for transitioning work from exiting vendors to the selected MSP(s)? Will the MSP be responsible for any transition activities from other vendors?" | Low |

### Competitive Intelligence Gaps

Information that would help us win but we're not asking for.

| Information Need | How It Helps Us | Possible Question | Risk of Asking |
|------------------|-----------------|-------------------|----------------|
| Number of bidders | Helps calibrate pricing aggressiveness and likelihood of multi-vendor award | "How many vendors is MGRC evaluating for this engagement?" | Low — standard question, though rarely answered directly |
| Previous MSP experience | Understanding past failures helps us avoid those pitfalls and position against them | "Has MGRC engaged MSPs for similar scope previously? If so, what lessons learned should vendors incorporate into their proposals?" | Low — frames us as learning-oriented |
| AI/Automation priorities | Mae flagged AI as differentiator; knowing priorities helps us emphasize right capabilities | "What role does MGRC envision AI and automation playing in managed services over the next 2-3 years? Are there specific areas where automation is a priority?" | Medium — reveals we're positioning around AI |
| Evaluation committee composition | Knowing who evaluates helps tailor messaging | "Can MGRC share who will be participating in the evaluation process (e.g., IT, Finance, Procurement, Business Units)?" | Low — reasonable process question |
| Pain points with current model | Understanding what's broken helps us position as the fix | *Do not ask directly* — could seem like we're fishing for ammunition. Better to infer from RFP structure. | High |
| Incumbent performance concerns | Could help us differentiate | *Do not ask* — we ARE an incumbent; asking could backfire | High |

---

## Priority Recommendations

Top 5 gaps to address, ranked by importance:

1. **Vendor Management / Third-Party Coordination (Topic Gap)**
   - Strategic intel explicitly identifies Atom as a pain point
   - Asking positions BayOne to capture this scope
   - Low risk — any MSP should ask about vendor landscape
   - **Suggested question:** "Will the MSP be expected to coordinate with or manage relationships with third-party vendors? Can MGRC provide a list of current third-party vendors and their support scope?"

2. **Compliance Audit Calendar (Topic Gap)**
   - 8 compliance frameworks with unknown effort implications
   - Hidden scope risk if audit support is extensive
   - **Suggested question:** "Can MGRC provide a calendar of compliance audits and clarify which audits the MSP will support?"

3. **Documentation State (Topic Gap)**
   - Directly impacts KT risk and Phase 1 pricing
   - Poor documentation = longer, costlier transition
   - **Suggested question:** "Can MGRC characterize the current state of operational documentation for each application area?"

4. **Subcontractor Approval Process (Risk Gap)**
   - Critical if BayOne partners for MuleSoft, OCI, or other gaps
   - Need to know timeline and constraints before proposal
   - **Suggested question:** "For vendors proposing subcontractors, what is MGRC's approval process and timeline?"

5. **Scope Change Control (Risk Gap)**
   - Protects against scope creep beyond RACI question
   - M&A, new integrations, upgrades could expand scope
   - **Suggested question:** "What is MGRC's change request and approval process for post-contract scope changes?"

---

## Gaps We Should NOT Fill

Questions we considered but rejected because they reveal too much.

| Considered Question | Why It's Risky | Recommendation |
|---------------------|----------------|----------------|
| "Is offshore staffing acceptable for 24/7 monitoring?" | Reveals we're planning offshore model for cost efficiency; competitors could note this | Do not ask — assume offshore is acceptable per industry norms; confirm informally if needed |
| "What is the minimum required margin or expected cost per FTE?" | Directly reveals pricing strategy concerns | Do not ask — use industry benchmarks |
| "Does MGRC require deep MuleSoft development expertise in-house?" | Reveals potential capability gap | Do not ask — address through subcontractor question instead |
| "What caused issues with current vendors that led to this RFP?" | Fishing for competitor intelligence; could seem adversarial | Do not ask — infer from RFP structure and contractor intel |
| "Why are you consolidating from 20 vendors?" | Could seem like we're questioning their decision | Do not ask — accept the strategy and position as a consolidation partner |
| "What is MGRC's appetite for Year 1 discount in exchange for longer commitment?" | Reveals aggressive pricing strategy | Do not ask — propose this in the pricing narrative instead |

---

## Coverage Assessment by RFP Section

| RFP Section | Questions Asked | Coverage Level | Notes |
|-------------|-----------------|----------------|-------|
| Scope & Environment | 6 (Q1-Q6) | Good | Strong on volumes, transitions, integrations |
| Evaluation Criteria | 3 (Q7-Q9) | Adequate | Key strategic questions covered |
| Staffing Model | 4 (Q10-Q13) | Good | Support model, volumes, change mgmt |
| Technology Specifics | 3 (Q14-Q16) | Partial | ServiceNow, NexSTAR, PCI covered; DR, security ops missing |
| Commercial Terms | 4 (Q17-Q20) | Good | Budget, pricing models, RACI addressed |
| Compliance & Security | 1 (partial via Q16) | Weak | 8 frameworks, minimal questions |
| Disaster Recovery | 0 | None | Significant gap |
| Vendor Management | 0 | None | Critical gap given intel |
| Testing & QA | 0 | None | Gap, especially given manual testing intel |
| Documentation/KM | 0 | None | Transition risk implication |

---

## Summary Statistics

- **Total gaps identified:** 20
  - Topic gaps: 6
  - Depth gaps: 5
  - Risk gaps: 5
  - Competitive intel gaps: 4 (2 actionable, 2 too risky)
- **Recommended new questions:** 11-13 (depending on risk tolerance)
- **Questions to avoid:** 6 (too revealing)
