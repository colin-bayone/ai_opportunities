# McGrath RentCorp MSP RFP - General Requirements Clarifying Questions

**Document Purpose:** Identify ambiguities and interpretation gaps in general requirements that could significantly impact staffing, pricing, and accountability models.

**Date:** February 24, 2026

---

## Section 1: Account & Support Management Expectations

### 1.1 Strategic Planning & Budgeting (Requirement 1.3)
**Issue:** The scope of "strategic plans, budgeting, and benchmarks" is undefined.

**Questions:**
1. What level of strategic planning is expected? (e.g., annual technology roadmaps, multi-year transformation planning, quarterly tactical planning?)
2. Does "budgeting" include full IT budget ownership, advisory input, or just MSP-managed services forecasting?
3. What does "identifying and quantifying business risk" entail? Are you expecting formal risk assessments with quantified financial impacts, or advisory observations?

### 1.2 Service Level Agreements (Requirement 1.4)
**Issue:** "Penalties for non-performance" mentioned without defining financial exposure or cap limits.

**Questions:**
1. Are you expecting financial penalties/service credits for SLA misses, or process-based remediation?
2. If financial penalties apply, is there an expected cap (e.g., percentage of monthly fees)?
3. Should the MSP propose specific SLA targets, or will McGrath define these during contracting?

### 1.3 Governance Committees (Requirement 1.9)
**Issue:** "Contribute to governance committees" is vague regarding time commitment and scope.

**Questions:**
1. How many governance committees exist, and what is the expected MSP participation frequency?
2. What level of participation is expected? (observer, contributor, decision-maker, committee chair?)
3. Is this participation included in base pricing or considered additional consulting time?

---

## Section 2: Shared Responsibility ⚠️ CRITICAL

### 2.1 Shared Responsibility Model (Requirement 2.1)
**Issue:** This is the ONLY requirement in this section, but most requirements throughout the RFP are marked as "Shared." This creates significant ambiguity about accountability boundaries.

**CRITICAL QUESTIONS:**
1. **Throughout the requirements, many items are marked as "Shared" responsibility. Can you provide McGrath's current view of the shared responsibility model?** For example:
   - Who has primary accountability vs. secondary support role?
   - What does McGrath expect to retain vs. delegate to the MSP?
   - Which areas require joint execution vs. clear handoffs?

2. **For "Shared" requirements, how should pricing be structured?** Should we assume:
   - MSP provides full capability with McGrath oversight?
   - McGrath provides primary capability with MSP augmentation?
   - True 50/50 co-execution model?

3. **What is the decision-making authority in "Shared" scenarios?** For example:
   - Change approvals for production systems
   - Patch deployment timing
   - Security incident response
   - Vendor selection for tools/technologies

4. **Can you clarify accountability for these specific "Shared" areas:**
   - End-user device management (monitoring, patching, security)
   - Integration ownership between MuleSoft vs. OIC
   - Database administration vs. database development
   - Application administration vs. application development
   - Help desk Tier 1 vs. Tier 2+ support

---

## Section 3: Provider Tools and Technology

### 3.1 Monitoring Agents for End-User Devices (Requirement 3.1)
**Issue:** Scope of "end user devices" and monitoring depth unclear.

**Questions:**
1. How many end-user devices are in scope? (desktops, laptops, mobile devices?)
2. What level of monitoring is expected? (basic uptime, performance metrics, security posture, application health?)
3. Are end-user devices managed by McGrath IT or expected to be MSP-managed?

### 3.2 Help Desk / Ticketing System Integration (Requirement 3.2)
**Issue:** Reference to both "Fresh Service and Service Now" creates confusion about primary system.

**Questions:**
1. Does McGrath currently use both FreshService and ServiceNow, or is this an either/or statement?
2. If both are in use, which is the primary ticketing system for MSP integration?
3. The requirement asks "Will an installation be required?" - can you clarify if you're asking about agent installation on user devices, or system integration/API setup?

### 3.3 MSP-Provided vs. McGrath-Owned Technology (Requirements 3.3, 3.4)
**Issue:** Unclear which infrastructure is MSP-provided vs. McGrath-owned.

**Questions:**
1. Does McGrath expect the MSP to provide managed firewalls, or manage McGrath's existing firewalls?
2. For SIEM/security monitoring (3.4), should the MSP bring their own SIEM platform, or integrate with McGrath's existing security tools?
3. What percentage of the infrastructure is expected to be MSP-provided vs. MSP-managed on McGrath's behalf?

---

## Section 4: Service & Support Management ⚠️ CRITICAL

### 4.1 Support Hours and Coverage (Requirements 4.1, 4.4, 4.5)
**Issue:** Conflicting or unclear coverage expectations.

**CRITICAL QUESTIONS:**
1. **Requirement 4.1 specifies "U.S. hours of 5:00am PST to 5:00pm PST" for end-user support, but Requirement 4.5 requires "24/7 monitoring and alerting" with "on-call support for incident resolution."** Please clarify:
   - Is 5am-5pm PST for Tier 2+ desk-side/user-interactive support only?
   - Is 24/7 coverage only for infrastructure monitoring and critical outages?
   - What constitutes a "critical outage" that triggers after-hours response?

2. **What is the expected response time for after-hours critical incidents?** (e.g., 15 minutes, 30 minutes, 1 hour?)

3. **What SLA response/resolution times are expected for different priority levels?** Can you provide your priority matrix (P1/P2/P3/P4 definitions)?

### 4.2 Tier 1 vs. Tier 2+ Support Boundary (Requirements 4.1, 4.3)
**Issue:** Requirements state "beyond Tier 1" multiple times but don't define where Tier 1 ends.

**CRITICAL QUESTIONS:**
1. **Where does McGrath draw the line between Tier 1 and Tier 2 support?** For example:
   - Password resets, account unlocks = Tier 1?
   - Application functional issues = Tier 2?
   - Infrastructure/system issues = Tier 2?

2. **Does McGrath have an existing Tier 1 team that will remain in place?** If so:
   - What is the expected escalation volume from Tier 1 to MSP?
   - Will the MSP have access to Tier 1 ticket history and knowledge base?

3. **For requirements 4.1 and 4.3 stating MSP provides support "beyond Tier 1," should we assume:**
   - McGrath retains Tier 1, MSP provides Tier 2+?
   - MSP provides Tier 2-3, McGrath retains Tier 4/SME resources?
   - MSP provides all tiers with pricing differentiation?

### 4.3 Help Desk Integration (Requirement 4.2)
**Issue:** "Manage integration of help desk support available through Fresh Service and Service Now from MGRC to provider, if needed."

**Questions:**
1. Does "if needed" mean this integration is optional or TBD?
2. What does "manage integration" mean? (API integration, workflow automation, ticket routing rules?)
3. If McGrath has existing Tier 1 using FreshService/ServiceNow, how should escalations to MSP be handled? (email, API, phone call?)

---

## Section 5: Technology Management

### 5.1 Software License Management (Requirement 5.1)
**Issue:** Scope of "business systems and tools" is undefined.

**Questions:**
1. What systems are in scope for license management? (SaaS applications, Microsoft 365, Oracle, Salesforce, all enterprise software?)
2. Does "manage" include procurement, renewal negotiations, and vendor relationship management, or just tracking/optimization?
3. Should MSP provide license harvesting, usage analytics, and optimization recommendations?

### 5.2 Patch Management Process (Requirement 5.2)
**Issue:** Multiple processes mentioned (change, escalation, maintenance windows) without clear ownership.

**Questions:**
1. Does McGrath have an established Change Advisory Board (CAB) that the MSP must integrate with, or should MSP define the change process?
2. For "zero-day" vulnerabilities, what is the expected response time? (immediate deployment, 24 hours, risk-based assessment?)
3. Who defines and approves maintenance windows? (McGrath business owners, MSP recommendation, joint decision?)

---

## Section 6: Managed Data & Database Services

### 6.1 Database Administration Scope (Requirements 6.1, 6.2)
**Issue:** Unclear boundary between database administration and database development.

**Questions:**
1. What database platforms are in scope? (Oracle, SQL Server, MySQL, PostgreSQL, cloud databases?)
2. Does "setup, configure and maintain" include database schema design and application-level optimization, or infrastructure-level DBA work only?
3. Who owns application query optimization? (MSP database team, application development team, joint responsibility?)

### 6.2 Backup and Recovery Strategy Ownership (Requirements 6.3, 6.4)
**Issue:** Two similar requirements about backup strategy with unclear differentiation.

**Questions:**
1. Does McGrath have an existing backup/recovery strategy that needs execution support, or should MSP design from scratch?
2. What is the difference between "implement data backup and recovery strategies" (6.3) vs. "develop and manage a data backup & migration strategy" (6.4)?
3. What RPO/RTO targets should the MSP design for? (varies by system tier, or enterprise standard?)

### 6.3 Data Quality and ETL Support (Requirements 6.7, 6.8)
**Issue:** Unclear boundary between data operations and data engineering.

**Questions:**
1. Who develops ETL jobs and data integration pipelines? (MSP, McGrath team, integration vendor?)
2. For "data cleaning and checking efforts" (6.8), is this ongoing operational support or project-based data quality initiatives?
3. What tools/platforms are used for ETL? (Oracle GoldenGate, Informatica, custom scripts, MuleSoft?)

---

## Section 7: Integration Management ⚠️ CRITICAL

### 7.1 MuleSoft vs. OIC Ownership Split (Requirements 7.1-7.6)
**Issue:** All integration requirements reference both MuleSoft and OIC without clarifying ownership boundaries.

**CRITICAL QUESTIONS:**
1. **Does McGrath use both MuleSoft and Oracle Integration Cloud (OIC) in production today?** If so:
   - Which platform is primary vs. secondary?
   - Are different integration types assigned to different platforms? (e.g., Oracle-to-Oracle via OIC, third-party via MuleSoft?)
   - How many integrations exist on each platform?

2. **What is the expected MSP role for each platform?**
   - Full ownership of development, deployment, and support for both?
   - Support/operations only with development handled by another team/vendor?
   - Different levels of support for each platform?

3. **Who owns integration development vs. operations?**
   - New integration builds
   - Existing integration enhancements
   - Production monitoring and incident response
   - Platform upgrades and version management

### 7.2 Integration with Third-Party Systems (Requirement 7.1)
**Issue:** Multiple third-party systems listed without context on complexity or ownership.

**Questions:**
1. How many integrations exist with each listed system? (Oracle Fusion, RecVue, ADP, banks)
2. Who owns the technical relationship with these third-party vendors? (McGrath, MSP, or joint?)
3. For bank integrations specifically, what security/compliance requirements apply? (PCI-DSS, SOC2, specific bank certification programs?)

### 7.3 Quarterly Oracle Fusion Updates (Requirement 7.3)
**Issue:** Oracle Fusion releases quarterly updates that can break integrations.

**Questions:**
1. Does McGrath expect the MSP to perform pre-release testing in a sandbox environment before each quarterly Oracle update?
2. What is the expected timeline for integration regression testing and remediation after Oracle releases updates?
3. Who owns the cost of integration fixes required due to Oracle's breaking changes? (included in base MSP pricing, time & materials, Oracle's responsibility?)

---

## Section 8: Technical Architecture

### 8.1 Architecture Role Definition (Requirements 8.1-8.6)
**Issue:** Architecture activities span strategic guidance to tactical observation, creating role ambiguity.

**Questions:**
1. Is McGrath expecting the MSP to provide a dedicated Enterprise Architect role, or architectural guidance as part of technical leads' responsibilities?
2. What percentage of MSP time should be allocated to architecture activities vs. hands-on implementation/support?
3. Does McGrath have an internal architecture team that MSP must align with, or is MSP expected to lead architecture definition?

### 8.2 Cross-Functional Architecture Governance (Requirements 8.7, 8.8)
**Issue:** These requirements suggest multi-vendor/multi-team coordination complexity.

**Questions:**
1. How many other vendors/partners does the MSP need to coordinate with for architecture decisions? (names/roles would be helpful)
2. What governance bodies exist for architecture decisions? (Architecture Review Board, Change Advisory Board, steering committees?)
3. Who has final decision-making authority when architecture opinions differ between MSP, internal teams, and other vendors?

---

## Section 9: Technical Services

### 9.1 Application Development Scope (Requirements 9.1, 9.2)
**Issue:** "On request" suggests project-based work, but scope and pricing model unclear.

**Questions:**
1. Should application development services (customizations, extensions, reports) be priced as:
   - Included capacity within base MSP pricing (e.g., X hours/month)?
   - Time & materials for discrete projects?
   - Fixed-price project engagements?

2. What volume of customization/development work does McGrath anticipate annually? (hours, number of projects, or percentage of MSP team capacity?)

3. For Oracle Visual Builder, APEX, OIC development specifically - does McGrath have existing citizen developers or internal teams doing this work today, or would MSP own all development?

### 9.2 Multi-System Integration Support (Requirement 9.4)
**Issue:** Complex environment with integrations "owned or managed by different internal teams or vendors."

**Questions:**
1. Can you provide a breakdown of which integrations are owned by which teams/vendors? (e.g., Salesforce CPQ managed by Salesforce partner, Oracle Fusion integrations by MSP, etc.)
2. When integration issues span multiple systems owned by different parties, who coordinates troubleshooting and resolution?
3. What is the expected MSP responsibility for integrations owned by other vendors? (troubleshooting assistance, full support if other vendor fails to respond, advisory only?)

### 9.3 Salesforce Seasonal Releases (Requirement 9.5)
**Issue:** Salesforce releases 3 times per year with potential breaking changes.

**Questions:**
1. Does McGrath expect the MSP to perform regression testing before each Salesforce release (Winter, Spring, Summer)?
2. What is the expected timeline for testing and remediation after Salesforce releases updates in preview sandboxes?
3. Are Salesforce release readiness activities included in base pricing or scoped as project work?

---

## Section 10: Application Administration

### 10.1 User & Role Management (Requirement 10.1)
**Issue:** Security role management across multiple systems with SOD requirements.

**Questions:**
1. What systems are in scope for user/role administration? (Oracle, Salesforce, MuleSoft, custom applications?)
2. Does McGrath have an Identity and Access Management (IAM) system that MSP must integrate with, or will MSP manage access directly in each system?
3. For "periodic security roles" review - what frequency is expected? (monthly, quarterly, annually?)

### 10.2 Configuration Management (Requirement 10.2)
**Issue:** "Functional setups across supported modules and systems" is extremely broad.

**Questions:**
1. What is the boundary between application configuration (expected of MSP) vs. business process configuration (McGrath business owners)?
2. For Oracle Fusion and Salesforce specifically, how many modules/clouds are in scope? (e.g., Oracle Financials, HCM, SCM, CX / Salesforce Sales Cloud, Service Cloud, CPQ, etc.)
3. Should MSP provide configuration documentation and change logs for all configuration changes, or only major changes?

### 10.3 Patch and Update Management (Requirement 10.3)
**Issue:** Overlaps with Section 5.2 but adds regression testing and rollback requirements.

**Questions:**
1. Is this requirement specific to application-layer updates (Oracle Fusion, Salesforce, SaaS apps) while 5.2 covers infrastructure patching?
2. What constitutes "regression testing" for application updates? (full UAT, smoke testing, automated test suite execution?)
3. For SaaS applications with forced updates (Salesforce, Oracle Cloud), how should MSP handle rollback if it's not possible?

### 10.4 License Optimization (Requirement 10.4)
**Issue:** "Periodic licensing review" without defined frequency or scope.

**Questions:**
1. How often should license optimization reviews occur? (quarterly, annually, or ad-hoc?)
2. Should MSP track license utilization continuously and alert when waste is detected, or perform point-in-time assessments?
3. Does this include negotiating with vendors for better pricing, or just providing optimization recommendations to McGrath?

---

## Section 11: Compliance and Security ⚠️ CRITICAL

### 11.1 Compliance Frameworks (Requirement 11.1)
**Issue:** Multiple frameworks listed (NIST, SOC2 Type 2, HIPAA, PCI, GDPR, CMMC) with varying applicability.

**CRITICAL QUESTIONS:**
1. **Which compliance frameworks are mandatory vs. aspirational for this engagement?**
   - HIPAA: Does McGrath handle Protected Health Information (PHI)?
   - PCI: Does McGrath process credit card data in systems managed by MSP?
   - GDPR: What European operations exist that trigger GDPR requirements?
   - CMMC: Does McGrath have Department of Defense contracts requiring CMMC certification?

2. **What is McGrath's current compliance posture?**
   - Which certifications/attestations does McGrath hold today?
   - Which frameworks require MSP to maintain their own certification vs. operate within McGrath's compliance program?

3. **What does "McGrath RentCorp's IT Security Compliance Policy Manual" contain, and can it be shared with bidders?** This could significantly impact MSP staffing and processes.

### 11.2 Cybersecurity Controls (Requirement 11.2)
**Issue:** "Robust cybersecurity strategies, policies, procedures, and controls" is vague.

**Questions:**
1. Should the MSP propose their own cybersecurity framework, or adopt McGrath's existing policies and standards?
2. Are there specific security controls McGrath requires? (MFA, encryption standards, network segmentation, SIEM, EDR, etc.)
3. What security tools/platforms does McGrath already have in place that MSP must integrate with?

### 11.3 Penetration Testing and Incident Response (Requirements 11.3, 11.4)
**Issue:** Overlap between threat monitoring, pen testing, and incident response without clear ownership.

**Questions:**
1. Does McGrath expect the MSP to conduct penetration testing, or contract with a third-party pen test provider and remediate findings?
2. For security incident response, what is the MSP's role vs. McGrath's internal security team? (full incident response ownership, technical remediation only, advisory/consulting?)
3. What constitutes a security incident that triggers incident response processes? (any malware detection, confirmed data breach, suspected unauthorized access?)

### 11.4 Audit Support (Requirement 11.8)
**Issue:** "Timely manner" is undefined for audit evidence requests.

**Questions:**
1. What types of audits should MSP expect? (financial audits, SOX compliance, security audits, vendor audits?)
2. What is the expected turnaround time for audit evidence requests? (24 hours, 3 business days, 1 week?)
3. Should MSP maintain audit-ready documentation continuously, or compile evidence when audit requests are received?

---

## Section 12: Governance and Documentation

### 12.1 Documentation Standards (Requirement 12.1)
**Issue:** "Publish regularly" without defining frequency or format.

**Questions:**
1. What documentation format does McGrath prefer? (Confluence, SharePoint, Word/PDF, markdown in Git?)
2. What does "regularly" mean for documentation updates? (real-time, weekly, after each change, quarterly reviews?)
3. Should documentation include runbooks, architecture diagrams, process flows, change logs, and knowledge base articles - or specific subset?

### 12.2 Knowledge Transfer (Requirement 12.2)
**Issue:** "As needed" suggests undefined frequency and scope.

**Questions:**
1. What scenarios trigger knowledge transfer requirements? (new McGrath hires, system changes, quarterly reviews, end of contract?)
2. What format should knowledge transfer take? (formal training sessions, documentation handoff, shadowing/working sessions?)
3. If MSP resources transition, is there an expectation for overlap/cross-training periods?

---

## Section 13: Backup and Disaster Recovery

### 13.1 Backup Strategy Ownership (Requirement 13.1)
**Issue:** "Design methodology and gain approval for, OR review and offer feedback on existing methodology" - unclear which scenario applies.

**Questions:**
1. Does McGrath have an existing backup/DR strategy that MSP should execute against, or is MSP expected to design from scratch?
2. What systems are in scope for MSP-managed backups vs. vendor-managed backups (e.g., Oracle Cloud, Salesforce, AWS)?
3. For SaaS applications, does McGrath expect third-party backup solutions (e.g., Veeam for Salesforce, Odaseva), or rely on vendor-native backup?

### 13.2 DR Testing Frequency (Requirements 13.2, 13.5)
**Issue:** "How often" is asked but not defined.

**Questions:**
1. What is McGrath's expectation for DR testing frequency? (quarterly, semi-annually, annually?)
2. Should DR tests be full failover tests or tabletop exercises?
3. What systems are considered critical for DR testing vs. lower priority for recovery?

### 13.3 Disaster Recovery Scope (Requirements 13.3, 13.4)
**Issue:** Overlap between developing DR plans and providing recovery support.

**Questions:**
1. Does McGrath have existing DR plans that need testing/updates, or should MSP develop new DR plans?
2. For "recovery support in case of system failure" (13.4), what is expected response time for DR activation?
3. Are there specific RTO/RPO requirements for different system tiers? (e.g., Tier 1 = 4hr RTO/1hr RPO, Tier 2 = 24hr RTO/8hr RPO?)

---

## Section 14: Continuous Improvement

### 14.1 Agile Sprint Methodology (Requirement 14.8)
**Issue:** "Fluid use of resources to support McGrath's continuous improvement efforts as part of an agile sprint methodology."

**CRITICAL QUESTIONS:**
1. Does McGrath operate on an agile sprint cadence today? If so, what is the sprint length? (1 week, 2 weeks, 3 weeks?)
2. What does "fluid use of resources" mean? (MSP team participates in McGrath sprints, MSP runs parallel sprints, ad-hoc resource allocation?)
3. How should MSP balance agile project work vs. ongoing operational support/tickets?

### 14.2 Development vs. Administration (Requirements 14.2, 14.3)
**Issue:** References to "App Dev Support" and "Script/code development" overlap with Section 9 Technical Services.

**Questions:**
1. What is the difference between Section 9 Technical Services (application development) and Section 14 Continuous Improvement development support?
2. Is Section 14 focused on smaller enhancements, automation scripts, and technical debt reduction while Section 9 is new features/projects?
3. Should these development activities be priced separately or as combined capacity?

### 14.3 Quarterly Release Management (Requirement 14.9)
**Issue:** Overlaps with earlier requirements about Oracle/Salesforce updates but adds "sandbox testing."

**Questions:**
1. How many sandbox/non-production environments exist that require testing before production updates?
2. Who owns test case development and UAT execution? (McGrath business users, MSP, or joint?)
3. What is the expected timeline for testing and deployment after a mandatory update is released by the vendor?

---

## Section 15: Project Management

### 15.1 Project vs. Operational Work Mix (Requirement 15.1)
**Issue:** Unclear how project management fits with ongoing MSP operations.

**Questions:**
1. Should project management be a dedicated role within the MSP team, or do technical leads manage projects as part of their broader responsibilities?
2. What percentage of MSP capacity should be allocated to project work vs. operational support?
3. What project management methodology does McGrath prefer? (Agile, Waterfall, Hybrid, PMI/PMP standards?)

### 15.2 Documentation Review and Approval (Requirement 15.2)
**Issue:** MSP reviewing and approving specifications suggests oversight role, which conflicts with MSP doing the implementation work.

**Questions:**
1. Is McGrath expecting the MSP to review documentation created by other vendors/internal teams, or review their own deliverables before client acceptance?
2. Who creates Functional and Technical specification documents? (McGrath business analysts, MSP, third-party partners?)
3. What approval authority does the MSP have vs. advisory role in reviewing specifications?

---

## Summary of Highest-Priority Questions

### Tier 1 Priority (Deal-Breakers):
1. **Section 2 (Shared Responsibility):** Define accountability boundaries for all "Shared" requirements
2. **Section 4 (Support Hours):** Clarify 5am-5pm PST vs. 24/7 coverage and Tier 1 vs. Tier 2+ boundaries
3. **Section 7 (Integration Management):** Define MuleSoft vs. OIC ownership and integration development vs. operations split
4. **Section 11 (Compliance):** Identify which compliance frameworks are mandatory (HIPAA, PCI, GDPR, CMMC applicability)

### Tier 2 Priority (Significant Pricing Impact):
1. **Section 9 (Technical Services):** Clarify application development pricing model (included capacity vs. T&M vs. fixed-price)
2. **Section 14 (Continuous Improvement):** Define agile sprint participation model and project vs. operational work balance
3. **Section 6 (Database Services):** Clarify DBA vs. database development boundary
4. **Section 8 (Technical Architecture):** Define architecture role expectations (dedicated architect vs. guidance from leads)

### Tier 3 Priority (Operational Clarity):
1. **Section 13 (DR/Backup):** Define testing frequency and RTO/RPO targets
2. **Section 10 (Application Admin):** Clarify scope of "supported modules and systems"
3. **Section 12 (Documentation):** Define documentation standards and knowledge transfer expectations

---

**Next Steps:**
1. Submit this clarifying questions document to McGrath procurement
2. Request bidder Q&A session or written response deadline
3. Based on answers, refine staffing model and pricing assumptions
4. Update shared responsibility RACI matrix for proposal
