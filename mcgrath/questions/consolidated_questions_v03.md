# McGrath RFP Questions - Consolidated Draft v03

**Date:** February 24, 2026
**Status:** Enhanced with technical depth from CSV/architecture analysis
**Previous Version:** v02 (February 20, 2026) - 36 questions

---

## Summary

| Source | Count |
|--------|-------|
| Carried forward from v02 (unchanged) | 32 |
| Carried forward from v02 (enhanced) | 4 |
| New questions (technical depth) | 24 |
| **Total** | **60** |

---

## What Changed in v03

This version incorporates technical insights from:
- `specific_requirements.csv` (183 rows of solution-specific requirements)
- `general_requirements.csv` (102 rows of capability requirements)
- `sla.csv` and `kpi.csv` (SLA matrix and KPI definitions)
- `architecture.md` (50+ integrations, system inventory)

**New question categories added:**
- Solution-specific technical questions (Salesforce, RecVue, Oracle Fusion, OCI, NexSTAR, Integrations, Data Pipeline, Databases, Customer Hub)
- SLA/KPI measurement methodology questions
- Architecture-driven integration questions

---

## Legend

- **ORIGINAL** = From v02, unchanged
- **ENHANCED** = From v02, expanded with technical detail
- **NEW: Technical** = New question based on CSV/architecture analysis
- **NEW: SLA/KPI** = New question about measurement methodology
- **NEW: Architecture** = New question driven by integration complexity

---

# SECTION 1: Scope & Transition Planning (14 questions)

## Q1: Ticket Volume Data
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Can MGRC provide a breakdown of current monthly ticket/service request volume by application area (Salesforce, Oracle Fusion, OCI, NexSTAR, integrations, etc.) and by priority level (P1–P4) for the trailing 12 months? |
| **Justification** | Essential for cost model. Every MSP will ask this. |

---

## Q2: Current FTE Count
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | What is the current FTE count (internal and external/contractor) supporting each application area today? How many of these resources are expected to transition to the MSP, remain at MGRC, or depart during the onboarding period? |
| **Justification** | Standard scoping — tells us team size needed. |

---

## Q3: KT Period Resource Availability
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For the Knowledge Transfer phase (May 18 – July 6), will MGRC's current support resources remain fully available to shadow and co-work with MSP staff during the entire transition period, or is there an expected ramp-down schedule for current resources? |
| **Justification** | Coverage gap risk if staff leave before KT complete. |

---

## Q4: Phased Go-Live Approach
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Is MGRC open to a phased go-live approach where application areas are transitioned in priority waves rather than a single go-live date of July 6 for all areas? |
| **Justification** | De-risks delivery; shows pragmatic thinking. |

---

## Q5: Integration Stability Status
| | |
|---|---|
| **Type** | ENHANCED |
| **Original** | Of the 50+ integrations listed, how many are currently in production and stable versus in active development or experiencing recurring issues? Can MGRC provide error/failure rates for the top integrations by volume? |
| **Enhanced** | The architecture diagram shows 50+ integrations across Oracle Cloud (SCM, ERP, CX, EPM), Salesforce, RecVue, and external systems. Can MGRC provide: (a) an inventory of integrations with their current stability status (stable/active development/recurring issues), (b) monthly error/failure rates for the top 10 integrations by volume, and (c) identification of which integrations are synchronous vs. asynchronous? |
| **Justification** | Architecture shows majority are synchronous (blue outline) = high uptime requirements. Sync failures cascade immediately. |

---

## Q6: Annual Hour Estimates
| | |
|---|---|
| **Type** | ENHANCED |
| **Original** | The RFP notes OCI effort is estimated at under 1,000 hours annually. Can MGRC provide similar annual hour estimates for other application areas to help vendors right-size proposals? |
| **Enhanced** | The RFP notes OCI effort is estimated at under 1,000 hours annually. However, the Specific Requirements show 15 categories for OCI alone (Administration, Release Management, Security, DR, etc.). Does the 1,000-hour estimate cover all 15 categories, or only the "Operational Day-to-Day" scope? Can MGRC provide similar annual hour estimates for other application areas, particularly Oracle Fusion (which spans Finance, SCM, Procurement, FSM, EPM) and NexSTAR (24x7 custom application)? |
| **Justification** | CSV shows 15 OCI requirement categories across rows 46-60. 1,000 hours seems low if all are in scope. |

---

## Q7: FTE Details
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | What is the current onshore/offshore distribution of support resources, and what is the organizational structure (e.g., dedicated teams per app vs. shared pool)? |
| **Justification** | Understanding current model helps us staff appropriately. |

---

## Q8: Integration Ownership
| | |
|---|---|
| **Type** | ENHANCED |
| **Original** | As a follow-up on integration stability: when integration issues arise, does MGRC's team typically resolve them in-house, or are they escalated to software vendors like Oracle or MuleSoft, or to the current support provider? |
| **Enhanced** | The Specific Requirements show "Shared=Yes" for most Integration & Connectivity Support categories, and the architecture shows dual middleware platforms (OIC and MuleSoft). When integration issues arise: (a) who owns first-level triage (MSP or MGRC), (b) at what point does ownership transfer to the middleware team, and (c) who coordinates with external system vendors (Avalara, Zilliant, DocuSign, banks) when the issue is on their end? |
| **Justification** | Row 94 (OIC Incident Management) shows NO ownership assignment - appears to be a gap. Need clarity. |

---

## Q9: July Go-Live Readiness
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Is the July 6 go-live date firm, or is there potential for schedule adjustment based on current project status? What contingency exists if the Oracle Fusion go-live extends past May 18? |
| **Justification** | Shows dependency awareness. |

---

## Q10: Vendor Consolidation Impact
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | As MGRC consolidates vendor relationships, what is the expected timeline for transitioning work from exiting vendors to the selected MSP(s)? Will the MSP be responsible for any transition activities from other vendors? |
| **Justification** | Hidden scope risk from vendor transitions. |

---

## Q11: Documentation State
| | |
|---|---|
| **Type** | ENHANCED |
| **Original** | Can MGRC characterize the current state of operational documentation (runbooks, SOPs, architecture diagrams) for each application area? Which areas are well-documented vs. relying primarily on tribal knowledge? |
| **Enhanced** | Can MGRC characterize the current state of operational documentation for each application area? Specifically: (a) for NexSTAR (custom application with 24x7 requirement), what documentation exists for the technology stack, codebase, and deployment procedures? (b) for the Material Voucher Java application shown in the architecture, is there documentation on hosting, ownership, and integration patterns? (c) for RecVue (which sits between Salesforce and Oracle ERP), are billing rules and revenue recognition logic documented? |
| **Justification** | Custom apps (NexSTAR, Material Voucher) and specialized billing (RecVue) are highest KT risk. |

---

## Q12: OIC vs. MuleSoft Platform Split
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | The Specific Requirements include separate sections for OIC (rows 91-103) and MuleSoft (rows 104-115) integration platforms. Can MGRC clarify: (a) the strategic division of workloads between OIC and MuleSoft (e.g., "OIC for Oracle-native, MuleSoft for SaaS"), (b) the expected ratio of MSP effort between the two platforms, and (c) whether there are plans to consolidate to a single platform during the contract term? |
| **Justification** | Dual platforms = dual skill sets = higher staffing cost. Need to understand if this is transitional or permanent. |

---

## Q13: Named Resources Requirement
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | Several Specific Requirements mandate "named MSP resources" due to "data and domain knowledge required" (Oracle BI Tools rows 116-117, Snowflake/Pipeline rows 142-145). Can MGRC clarify: (a) which roles require dedicated named resources vs. pooled support, (b) the expected FTE allocation for named resource areas, and (c) whether named resources must be onshore or can include offshore team members? |
| **Justification** | Named resources = dedicated staffing (higher cost) vs. pooled support (lower cost). $100K+ annual pricing difference. |

---

## Q14: Database Actual Counts
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | The Specific Requirements specify "up to 5 SQL Servers" and "up to 7 ATP Databases" (rows 148-160). Can MGRC provide: (a) the actual current count of each database type in production, (b) for SQL Servers, the configuration (standalone, Always On, Failover Cluster), and (c) for ATP databases, the current OCPU/storage allocations? |
| **Justification** | "Up to" language creates scope ambiguity. Actual counts drive licensing and staffing. |

---

# SECTION 2: Evaluation & Selection Criteria (4 questions)

## Q15: Evaluation Criteria Weighting
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Can MGRC share the relative weighting or ranking of the evaluation criteria listed (expertise, completeness, customer service, governance, vendor strength, compliance, value/TCO)? |
| **Justification** | Shapes where we emphasize in proposal. Every bidder asks this. |

---

## Q16: Multi-MSP vs Single Provider
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Does MGRC have a preference between a single MSP provider across all solution areas versus multiple providers with complementary coverage? |
| **Justification** | Critical strategic question. |

---

## Q17: Evaluation Committee Composition
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Can MGRC share who will be participating in the evaluation process (e.g., IT, Finance, Procurement, Business Units)? |
| **Justification** | Helps tailor messaging to evaluators. |

---

## Q18: AI/Automation Priorities
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | What role does MGRC envision AI and automation playing in managed services over the next 2-3 years? Are there specific areas where automation is a priority? |
| **Justification** | Levels the field on AI positioning. |

---

# SECTION 3: Staffing & Resource Model (8 questions)

## Q19: Dedicated vs Pooled Resources
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For US business hours support (5 AM – 5 PM PST), does MGRC require dedicated named resources assigned exclusively to MGRC for each application area, or is a shared/pooled resource model with guaranteed response SLAs acceptable? |
| **Justification** | $500K+ annual pricing difference based on answer. |

---

## Q20: After-Hours Monitoring Requirements
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For after-hours data pipeline monitoring (10 PM – 7 AM PT), what is the typical nightly volume of pipeline runs and average frequency of interventions requiring hands-on remediation versus automated alerting with next-business-day follow-up? |
| **Justification** | Passive monitoring vs active engineering = huge cost difference. |

---

## Q21: Change Management Policies
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Does MGRC have existing change management policies and maintenance schedules for the MSP to adopt, or should we propose a governance framework during Phase 1? |
| **Justification** | Adopting existing vs building from scratch = different Phase 1 scope. |

---

## Q22: Oracle Fusion Volumes
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For Oracle Fusion day-to-day operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, PO/invoice processing, and service requests? Are there seasonal peaks (quarter-end, year-end) that require surge staffing? |
| **Justification** | Largest scope item. Seasonal peak question shows ERP ops maturity. |

---

## Q23: Skill Requirements
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For dedicated resources, are there specific skill certifications or experience requirements that MGRC considers mandatory vs. preferred? |
| **Justification** | Staffing accuracy; distinguishes required vs nice-to-have. |

---

## Q24: Vendor Management
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Will the MSP be expected to coordinate with or manage relationships with third-party vendors (e.g., Oracle support, MuleSoft support, implementation partners)? If so, can MGRC provide a list of current third-party vendors and their support scope? |
| **Justification** | Potential high-value scope for BayOne. |

---

## Q25: After-Hours Coverage Model
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | The Specific Requirements specify after-hours monitoring (10pm-7am PT) for data pipelines (Rivery, SplashBI, Tableau) and 24x7 support for NexSTAR. Can MGRC clarify: (a) is after-hours coverage required 7 days/week including weekends/holidays, or business days only, (b) what is the historical frequency of incidents requiring intervention during these windows, and (c) is the expectation for active monitoring (dedicated overnight shift) or on-call response? |
| **Justification** | Dedicated overnight shift (7x9 hours) = 1.5-2 FTE. On-call rotation = 0.25-0.5 FTE. Major pricing difference. |

---

## Q26: Period-Close Support Model
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | For Oracle Fusion "period-close activities for GL, AP, AR, Inventory, Costing, and related modules" (row 34, Shared), what is the expected MSP role? Specifically: (a) is MSP responsible for executing close processes (running jobs, journal validation, reconciliation) or providing on-call support, (b) what is the close timeline (e.g., 5-day window), and (c) are after-hours or weekend close activities expected? |
| **Justification** | Close execution requires dedicated resources with deep GL/subledger knowledge. "Support" is much lower effort than "execute." |

---

# SECTION 4: Technology & Environment (12 questions)

## Q27: ServiceNow Migration Timeline
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | What is the expected timeline for migration from FreshService to ServiceNow (or similar)? Will the MSP be expected to support both platforms during transition, and is the MSP expected to play a role in the ServiceNow implementation itself? |
| **Justification** | Dual-platform support and migration involvement = different scope. |

---

## Q28: NexSTAR Technical Details
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For NexSTAR (custom application), can MGRC provide documentation on the technology stack, codebase language/framework, architecture diagrams, known technical debt, and deployment pipeline? Will the MSP have full source code and development environment access? |
| **Justification** | Custom apps are highest risk. 24x7 requirement makes this critical. |

---

## Q29: PCI Compliance Scope
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For the Customer Hub (nopCommerce), can MGRC clarify the PCI compliance scope and whether the MSP is expected to maintain PCI certification or support MGRC's existing audit process? |
| **Justification** | PCI accountability significantly affects security costs and insurance. |

---

## Q30: ServiceNow Migration Details
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Are there existing ITSM workflows, automations, or custom configurations in FreshService that must be migrated to ServiceNow? What is the expected level of MSP involvement in the migration project? |
| **Justification** | Migration complexity affects Phase 1 scope. |

---

## Q31: Testing & QA State
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | What is the current state of test automation for regression, smoke, and integration testing? Would MGRC be interested in the MSP introducing automation capabilities as part of the engagement? |
| **Justification** | Probes automation appetite. |

---

## Q32: Security Operations
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Does MGRC have existing SIEM/SOC capabilities, or will the MSP be expected to provide security monitoring and incident response? |
| **Justification** | Security ops distinct from compliance — could be large hidden scope. |

---

## Q33: Disaster Recovery
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For critical systems like Oracle Fusion, NexSTAR, and Customer Hub — what are the recovery targets if there's an outage? How often are disaster recovery tests conducted, and will the MSP be expected to plan and run those drills? |
| **Justification** | DR testing effort ranges widely. |

---

## Q34: RecVue Billing Complexity
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | RecVue sits between Salesforce and Oracle ERP as a critical billing hub (per the architecture diagram). Can MGRC provide: (a) monthly billing cycle volume (number of invoices generated), (b) typical exception rate requiring manual intervention, (c) complexity of revenue recognition rules (standard vs. custom), and (d) current FTE hours dedicated to billing cycle execution and exception handling? |
| **Justification** | Row 17 marks RecVue Day-to-Day Operations as "MSP Owned" - understanding volume drives staffing for dedicated billing analyst. |

---

## Q35: RecVue Hosting and DR
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | Row 28 marks RecVue Disaster Recovery as "MSP Owned." Is RecVue hosted on-premises, in MGRC's cloud tenancy, or in RecVue's SaaS environment? If SaaS, what is the MSP's DR responsibility (application config backup vs. infrastructure DR)? |
| **Justification** | SaaS = vendor-managed DR. Self-hosted = MSP infrastructure responsibility. Major scope difference. |

---

## Q36: Customer Hub Architecture
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | For Customer Hub (nopCommerce), the Specific Requirements reference "PCI-scoped platform" with MSP responsible for "security hardening, vulnerability scanning, patching." Can MGRC clarify: (a) does Customer Hub process and store credit card data directly, or does it redirect to a third-party payment processor, (b) what tokenization/encryption controls are in place, and (c) what is the expected vulnerability scanning cadence (quarterly external, annual internal per PCI DSS)? |
| **Justification** | Cardholder data in scope = SAQ-D compliance. Payment processor redirect = SAQ-A. Massive difference in PCI audit effort. |

---

## Q37: Material Voucher Application
| | |
|---|---|
| **Type** | NEW: Architecture |
| **Question** | The architecture diagram shows a "Material Voucher (Java Application)" connected to Oracle SCM Inventory. Can MGRC clarify: (a) where is this application hosted (on-premises, OCI, Azure), (b) who owns the source code and documentation, (c) is the MSP expected to support application code or only the integration to Oracle, and (d) is this application in scope for MSP support or retained by MGRC? |
| **Justification** | Custom Java app is unknown quantity. If in scope, need Java developers. If out of scope, need clear boundary. |

---

## Q38: Multi-CRM Strategy
| | |
|---|---|
| **Type** | NEW: Architecture |
| **Question** | The architecture shows three CRM-related systems: Salesforce (primary), Oracle CRM on Demand, and Nextstar. Are Oracle CRM on Demand and Nextstar being retired as part of the Salesforce consolidation, or will the MSP need to support all three platforms? If being retired, what is the timeline? |
| **Justification** | Three CRM platforms = 3x support complexity. Retirement timeline affects staffing model. |

---

# SECTION 5: SLA & KPI (8 questions)

## Q39: Response vs Resolution SLAs
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | The SLA document defines response time targets (15 min for P1, 60-120 min for P2, etc.) but also references "timeline for the solution and fixes." Can MGRC clarify: (a) are there defined resolution time SLAs in addition to response time SLAs, (b) if yes, what are the target resolution times for each priority level, and (c) are response and resolution measured separately in the SLO calculations? |
| **Justification** | Response time is achievable with process. Resolution time depends on issue complexity and may not be controllable. |

---

## Q40: P2 Response Time Clarification
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | For P2 (High) priority incidents, the SLA states "60-120 minutes" response time. For SLA compliance measurement, is the target 60 minutes (aspirational) or 120 minutes (acceptable)? Will a response at 90 minutes count as SLA-compliant? |
| **Justification** | 2x difference affects staffing and escalation procedures. |

---

## Q41: Priority Assignment Authority
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | Who has authority to assign priority levels (P1-P4) to incoming tickets? Does MGRC's reporting user assign priority, or does the MSP assess and classify? If the MSP classifies, what is the appeal process if MGRC disagrees with the assignment? |
| **Justification** | Prevents SLA disputes over priority classification after incidents. |

---

## Q42: SLA Exclusion Windows
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | The SLA document doesn't specify exclusion windows. Can MGRC clarify: (a) are P1/P2 response SLAs expected 24/7/365 or only during business hours, (b) are there exclusion windows for scheduled maintenance, (c) are SLAs suspended during force majeure events, and (d) what is the documentation process for exclusions? |
| **Justification** | Defines realistic on-call staffing and protects against penalization for circumstances outside MSP control. |

---

## Q43: SLA Non-Compliance Consequences
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | What are the consequences when monthly/quarterly SLA compliance falls below the defined objectives (95% for P1, 90% for P2-P4)? Specifically: (a) are there service credits or penalty clauses, (b) what is the remediation process if SLA compliance drops below minimum thresholds, and (c) is there a grace period during the first 90 days of engagement? |
| **Justification** | Determines financial risk exposure. Grace period allows baseline establishment before penalties. |

---

## Q44: KPI Tracking Granularity
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | Should KPIs be measured and reported: (a) globally across all MGRC systems, (b) per business unit/division (modular, test equipment, containment, HVAC), (c) per system/application, or (d) hybrid approach with global rollups and system-specific breakdowns? |
| **Justification** | Affects ticketing system configuration and reporting infrastructure. |

---

## Q45: Historical Performance Baseline
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | To set realistic targets, can MGRC provide historical performance data for the past 6-12 months, including: Average Resolution Time, First Contact Resolution Rate, MTTR, and SLA Compliance Rate? Are there known seasonal variations (higher volumes during tax season, quarter-end)? |
| **Justification** | Prevents committing to unachievable targets without understanding current state. |

---

## Q46: Measurement Tooling
| | |
|---|---|
| **Type** | NEW: SLA/KPI |
| **Question** | Regarding measurement tooling: (a) does MGRC provide the ticketing system, or should the MSP propose one, (b) who provides infrastructure monitoring and alerting tools, (c) will the MSP have API/database access to pull raw data for independent SLA validation, and (d) is there a neutral third-party system that timestamps ticket events to prevent disputes? |
| **Justification** | Determines infrastructure costs and data integrity for SLA verification. |

---

# SECTION 6: Compliance & Audit (2 questions)

## Q47: Compliance Audit Calendar
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Can MGRC provide a calendar of compliance audits scheduled for the next 12 months and clarify which audits the MSP will be expected to support, lead evidence gathering for, or remediate findings from? |
| **Justification** | 8 compliance frameworks listed. Unknown effort implications. |

---

## Q48: Compliance Framework Prioritization
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | The General Requirements reference multiple compliance frameworks (NIST, SOC2, HIPAA, PCI, GDPR, CMMC). Can MGRC clarify which frameworks are: (a) mandatory/certified today, (b) in active pursuit, and (c) aspirational/future? Specifically, does MGRC process HIPAA-protected health information, and does MGRC have or require CMMC certification? |
| **Justification** | HIPAA/CMMC have major staffing and process implications. Need to know if these are active requirements or future considerations. |

---

# SECTION 7: Commercial & Contractual (7 questions)

## Q49: Budget Range
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Does MGRC have a target budget range or not-to-exceed threshold for the MSP engagement that vendors should be aware of when structuring proposals? |
| **Justification** | Rarely answered directly but worth asking. |

---

## Q50: Hybrid Pricing Model
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Is MGRC open to pricing models that combine fixed operational support with variable capacity for enhancement and project work? |
| **Justification** | Gets intel on commercial flexibility. |

---

## Q51: Multi-Year Pricing Model
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For multi-year pricing, does MGRC expect flat pricing across Years 1–3, or is there flexibility in how pricing is structured year-over-year? |
| **Justification** | Gets intel without describing our exact strategy. |

---

## Q52: RACI Finalization Timing
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For items designated as 'Shared Responsibility,' will the RACI and responsibility splits be finalized before contract execution, or will they be defined during the Phase 1 onboarding period? How will scope disputes in shared areas be resolved? |
| **Justification** | Most of RFP is Shared Responsibility. Protects against undefined scope. |

---

## Q53: Scope Change Control
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | For scope changes identified after contract execution (e.g., new integrations, acquisitions, system upgrades), what is MGRC's change request and approval process? Will these be priced separately or absorbed into the base contract? |
| **Justification** | Protects against post-contract scope creep. |

---

## Q54: M&A Activity — Pending Acquisitions
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | Are there pending or planned acquisitions that would affect MSP scope within the first 12 months? If so, how many and what is their general scope? |
| **Justification** | M&A onboarding listed as service domain. |

---

## Q55: M&A Activity — Historical Handling
| | |
|---|---|
| **Type** | ORIGINAL |
| **Question** | How have M&A integrations historically been handled from a support perspective? |
| **Justification** | Understanding past approach helps plan for future. |

---

# SECTION 8: Shared Responsibility Clarification (5 questions)

## Q56: Shared Responsibility Definition
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | The Specific Requirements show most categories as "Shared=Yes" between MSP and MGRC. Can MGRC provide: (a) a definition of what "Shared" means operationally (e.g., who initiates, who executes, who approves), (b) examples of how shared work would be divided in practice, and (c) the decision-making authority and escalation path for shared activities? |
| **Justification** | 150+ of 183 requirements are "Shared." Without clear RACI, scope disputes are inevitable. |

---

## Q57: Development vs Configuration Boundary
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | For "Development, Enhancement & Optimization" categories marked "Shared" (Salesforce row 12, Oracle Fusion row 43, etc.), what is the expected split between MSP-led development and MGRC-led development? Specifically, will MSP be responsible for custom code (Apex, Java, PL/SQL) or limited to declarative configuration (flows, validation rules, Fast Formulas)? |
| **Justification** | Senior developers cost 40-60% more than administrators. Custom code vs. configuration is major pricing distinction. |

---

## Q58: Integration Development vs Operations
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | For Integration Platform "Development, Enhancement & Optimization" (OIC row 101, MuleSoft row 113), what is the expected balance between: (a) maintaining existing integrations, (b) modifying integrations for business changes, and (c) developing net-new integrations? Is there an existing backlog of integration development requests? |
| **Justification** | Row 113 (MuleSoft) is marked "MSP Augmented" suggesting MGRC has internal developers. Need clarity on staffing model. |

---

## Q59: BRD/FSD Documentation Expectations
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | Row 34 (Oracle Fusion Operational Day-to-Day) references "Documentation: BRDs, FSDs, test scripts, SOPs, and knowledge articles." What is the expected volume of enhancements requiring formal BRDs/FSDs, and who is responsible for initial requirements gathering and business analysis? |
| **Justification** | Creating BRDs/FSDs is business analyst work, not functional support. Significantly different skill level and cost. |

---

## Q60: Security & Compliance SoD Reviews
| | |
|---|---|
| **Type** | NEW: Technical |
| **Question** | For Security & Compliance requirements marked "Shared" across multiple solutions, what is the expected frequency of segregation-of-duties reviews? Does MGRC use SoD tooling (Appsian, Soterion, Oracle AACG), or are reviews performed manually? How many user accounts and roles are in scope? |
| **Justification** | Manual SoD reviews in large Oracle/Salesforce environments can consume 40-80 hours per quarter. Tooling reduces effort significantly. |

---

# Removed Questions

## Original Q9: Incumbent Advantage Weighting
| | |
|---|---|
| **Type** | REMOVED in v02 |
| **Reason** | Will hurt us. Too aggressive; signals "we're the incumbent, favor us." |

---

# Question Cross-Reference

## Questions Enhanced from v02
| v03 # | v02 # | Enhancement Summary |
|-------|-------|---------------------|
| Q5 | Q5 | Added sync/async classification request from architecture |
| Q6 | Q6 | Added OCI category count (15) and NexSTAR/Oracle scope |
| Q8 | Q8 | Added OIC row 94 gap, dual-platform context |
| Q11 | Q11 | Added NexSTAR, Material Voucher, RecVue specifics |

## New Questions by Source
| Source | Questions |
|--------|-----------|
| specific_requirements.csv | Q12-14, Q25-26, Q34-36, Q48, Q56-60 |
| general_requirements.csv | Q48, Q56-60 |
| sla.csv / kpi.csv | Q39-46 |
| architecture.md | Q37-38 |

---

# Priority Submission Recommendations

## Must-Ask Before Pricing (10 questions)
1. **Q56** - Shared Responsibility Definition (affects 150+ requirements)
2. **Q25** - After-Hours Coverage Model (dedicated shift vs. on-call = 1.5 FTE difference)
3. **Q6** - OCI 1,000 Hour Estimate Validation (scope could be 2-3x higher)
4. **Q13** - Named Resources Requirement (dedicated vs. pooled = $500K+ difference)
5. **Q28** - NexSTAR Technical Details (custom app with 24x7 = highest risk)
6. **Q12** - OIC vs MuleSoft Split (dual platforms = dual skill sets)
7. **Q43** - SLA Non-Compliance Consequences (financial risk exposure)
8. **Q34** - RecVue Billing Complexity (MSP Owned billing operations)
9. **Q14** - Database Actual Counts ("up to" vs. actual)
10. **Q26** - Period-Close Support Model (execute vs. support = major difference)

## High Priority (8 questions)
Q5, Q8, Q11, Q37, Q38, Q39, Q45, Q57

## Standard Priority (remaining 42 questions)
All others - important for complete scoping but less likely to swing pricing dramatically.

---

**Document Version:** v03
**Date:** February 24, 2026
**Total Questions:** 60
**Next Action:** Review with Colin, prioritize for submission by 4pm PT deadline
