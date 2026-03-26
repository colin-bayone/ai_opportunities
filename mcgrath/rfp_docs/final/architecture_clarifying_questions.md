# McGrath RentCorp RFP - Architecture Clarifying Questions

**Purpose:** Scope MSP support requirements based on future state architecture analysis
**Generated:** February 24, 2026
**Source Document:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/architecture.md`

---

## Executive Summary

The future state architecture reveals **50+ integration points** across Oracle Cloud, Salesforce, and external systems with a **synchronous-heavy integration pattern** that creates high uptime dependencies. Critical questions below focus on ownership boundaries, failure scenarios, and operational complexity that will directly impact MSP scope and pricing.

**Key Risk Areas:**
- RecVue as single point of failure for billing/revenue
- Majority synchronous integrations (immediate SLA impact from partner downtime)
- Custom/legacy applications with unclear ownership
- Multi-CRM environment suggesting incomplete migration
- Dense integration cluster between Salesforce and Oracle

---

## 1. Integration Stability & Ownership

### Q1.1: Integration Maturity Classification
**Context:** Architecture shows 50+ integration points across Oracle Cloud, Salesforce, RecVue, and external systems.

**Question:** Please classify each integration into one of three categories:
- **Stable/Production:** Live, fully tested, minimal expected changes
- **In Active Development:** Currently being built or enhanced
- **Future/Planned:** Not yet implemented but shown in future state diagram

**Why it matters:** MSP support model differs drastically between stable integrations (monitoring/troubleshooting) vs active development (testing, deployment, rollback planning). This affects staffing, escalation paths, and pricing.

---

### Q1.2: Integration Failure Triage Ownership
**Context:** Synchronous integrations (blue lines) create immediate failure visibility when partner systems have issues.

**Question:** When an integration fails, who performs initial triage to determine root cause:
- **Scenario A:** Salesforce → RecVue integration fails during quote submission
- **Scenario B:** Oracle SCM → Intellinum integration fails during PO scan/label
- **Scenario C:** Bank BAI2 statement feed fails to load into Oracle Cash Management

Is the MSP expected to:
1. Monitor all integration endpoints (both sides)?
2. Diagnose failures in external vendor systems (RecVue, Intellinum, Bank)?
3. Engage vendor support on McGrath's behalf, or escalate internally?

**Why it matters:** Defines MSP scope boundary. If MSP must troubleshoot RecVue billing logic or Intellinum label format issues, this requires specialist knowledge beyond standard Oracle/Salesforce administration.

---

### Q1.3: Middleware/iPaaS Platform
**Context:** Architecture diagram shows direct connections between systems but doesn't specify integration technology.

**Question:**
- Is there a middleware/iPaaS layer (Oracle Integration Cloud, MuleSoft, Boomi, Dell Boomi, Informatica)?
- If yes, who currently manages it? Is it in scope for MSP?
- If no middleware exists, are integrations point-to-point API calls, scheduled batch jobs, or file transfers?
- Does McGrath have integration monitoring/observability tools (e.g., OIC monitoring, Splunk, Datadog)?

**Why it matters:** Middleware platforms require specialized expertise. Point-to-point integrations may lack centralized monitoring, increasing MTTR. Existing observability tools reduce MSP onboarding complexity.

---

## 2. RecVue as Critical Billing Hub

### Q2.1: RecVue Criticality & Recovery Time Objective
**Context:** RecVue sits between Salesforce (quotes/contracts) and Oracle ERP (receivables/billing), processing revenue recognition and subscription billing.

**Question:**
- What is RecVue's current uptime SLA with its vendor?
- If RecVue experiences an outage, what is the business impact timeline:
  - Hour 1: Can sales still quote? Can customers receive invoices?
  - Hour 4: Revenue recognition batch jobs missed?
  - Day 1: Revenue reporting impact?
- Does McGrath have a documented RecVue disaster recovery plan?
- Is RecVue SaaS (vendor-managed) or self-hosted?

**Why it matters:** RecVue appears to be a single point of failure for the entire quote-to-cash process. MSP needs to understand acceptable downtime, escalation procedures, and whether RecVue vendor relationship management is in scope.

---

### Q2.2: RecVue Billing Logic Complexity
**Context:** RecVue handles complex revenue recognition and subscription billing between Salesforce and Oracle ERP.

**Question:**
- How complex are RecVue's billing rules? (e.g., usage-based billing, multi-element arrangements, ASC 606 revenue recognition)
- Are billing rules configured by McGrath staff, or does RecVue vendor assist?
- When billing errors occur (incorrect revenue allocation, failed invoice generation), who investigates:
  - Finance team interprets business rules?
  - IT/MSP troubleshoots technical integration?
  - RecVue vendor support assists?

**Why it matters:** If MSP is expected to troubleshoot billing logic errors, this requires finance domain knowledge beyond typical IT support. Defines need for specialized billing integration SME on MSP team.

---

## 3. Custom & Legacy Applications

### Q3.1: Material Voucher Java Application
**Context:** Architecture shows "Material Voucher" as a custom Java application connecting to Oracle SCM Inventory—flagged as potential legacy risk.

**Question:**
- **Hosting:** Where is Material Voucher hosted? (on-premises, cloud VM, managed hosting)
- **Ownership:** Who developed it? Is source code available to MSP?
- **Current Support:** Who currently supports it? (internal dev team, offshore vendor, no one)
- **Scope:** Is Material Voucher application support in scope for MSP, or only the integration connection point to Oracle Inventory?
- **Replacement Plans:** Is this application being retired/replaced in the NextGen roadmap?

**Why it matters:** Custom Java app support requires software development skills, not just Oracle admin. If no documentation/source code exists, this is a high-risk support area. Clarifies whether MSP needs a Java developer on staff.

---

### Q3.2: Multi-CRM Strategy (Oracle CRM on Demand + Nextstar + Salesforce)
**Context:** Architecture shows three CRM systems: Oracle CRM on Demand (legacy), Nextstar (adjacent system), and Salesforce (current).

**Question:**
- **Oracle CRM on Demand:** Is this being actively retired? If yes, what's the decommission timeline?
- **Nextstar:** What is this system? (Azure-hosted per notes) What business function does it serve?
- **Integration:** Do Oracle CRM on Demand and Nextstar integrate with Salesforce, or are they isolated?
- **MSP Scope:** Is MSP expected to support all three CRM platforms, or only Salesforce?

**Why it matters:** Supporting three CRM platforms triples complexity vs single Salesforce environment. If Oracle CRM on Demand is being retired in 6 months, MSP staffing/training priorities shift. Nextstar as unknown Azure system may require .NET/Azure DevOps skills.

---

## 4. Synchronous Integration SLA Impact

### Q4.1: Partner System Downtime Handling
**Context:** Majority of integrations are synchronous (blue lines)—user-facing transactions wait for partner system responses.

**Question:**
- When a synchronous partner system is down (e.g., DocuSign, Dun & Bradstreet, Avalara), what is the user experience?
  - Hard error (transaction fails)?
  - Graceful degradation (transaction queued for retry)?
  - Manual workaround process?
- Does McGrath have SLAs with these vendors? What are typical response times?
- Is MSP responsible for engaging vendor support during their outages, or does McGrath handle vendor relationships?

**Why it matters:** Synchronous integrations mean MSP is on the hook for incidents caused by partner downtime, even if root cause is external. Defines escalation procedures and whether MSP needs 24/7 vendor liaison capability.

---

### Q4.2: Integration Circuit Breaker & Retry Logic
**Context:** Synchronous integrations can cascade failures if partner systems slow down or timeout.

**Question:**
- Do integrations have circuit breaker patterns (auto-disable after N failures)?
- Are there retry policies for transient failures?
- Can integrations be manually disabled without code deployment (e.g., feature flags, admin panel)?
- Who is authorized to disable a failing integration during an incident (MSP, McGrath IT leadership, both)?

**Why it matters:** Without circuit breakers, a single slow integration can bring down the entire platform. MSP needs incident response procedures for quickly isolating failing integrations. Manual disable capability is critical for L1/L2 support.

---

## 5. Data Pipeline Operations

### Q5.1: Snowflake Extract Schedule & Dependencies
**Context:** Architecture shows Snowflake as data warehouse extracting from Oracle Cloud, feeding Tableau and SplashBI.

**Question:**
- **Extract Timing:** When does the Snowflake extract run? (nightly, hourly, real-time CDC)
- **Extract Technology:** Is this Oracle Data Integrator, OCI Data Integration, custom scripts, or Rivery?
- **Failure Impact:** If Snowflake extract fails, who is impacted? (executive dashboards, operational reports, customer-facing analytics)
- **Recovery Time:** What's the acceptable delay for data in Tableau/SplashBI? (same-day, next-day, weekly)

**Why it matters:** Data pipeline failures often have delayed visibility ("reports look wrong 2 days later"). Defines monitoring requirements and whether MSP needs a dedicated data engineer vs general Oracle admin.

---

### Q5.2: Rivery & SplashBI Ownership
**Context:** Architecture shows Rivery (ETL tool) and SplashBI (BI platform) in data pipeline.

**Question:**
- **Rivery:** Who currently manages Rivery? Is it SaaS or self-hosted? Is it in scope for MSP?
- **SplashBI:** What is SplashBI's relationship to Tableau? (replacement, complementary, different audience)
- **Support Boundaries:** For a "data looks wrong" incident in Tableau:
  - Does MSP troubleshoot Snowflake data quality?
  - Does MSP troubleshoot Rivery ETL logic?
  - Does MSP troubleshoot Tableau dashboard logic, or only infrastructure/access issues?

**Why it matters:** ETL/BI support is a specialized skill set (SQL, data modeling, dashboard design). Clarifies whether MSP needs a BI/analytics SME or if this is escalated to a separate team.

---

## 6. Banking & Payment Integrations

### Q6.1: Bank Connection Architecture
**Context:** Architecture shows synchronous integrations with Bank (BAI2 statements, APO), SnapPay (payments), XE (currency rates).

**Question:**
- **Bank Integration:** Is bank connection direct API, SFTP file transfer, or through a treasury management system (e.g., Kyriba, GTreasury)?
- **APO Context:** What does "APO" refer to? (Accounts Payable Outsourcing, Automatic Payment Order, other)
- **Failure Scenarios:** If BAI2 statement feed fails:
  - Who contacts the bank (MSP, McGrath treasury team)?
  - How quickly must it be resolved (same-day cash visibility, next-day acceptable)?

**Why it matters:** Banking integrations often involve security protocols (IP whitelisting, VPN tunnels) and bank-specific change control processes. MSP needs to understand escalation paths and whether 24/7 bank liaison is required.

---

## 7. Oracle Fusion Internal Integrations

### Q7.1: Inter-Module Integration Support Boundaries
**Context:** Architecture shows "Automated PO Creation" between Order Management and Procurement within Oracle SCM—a cross-module integration within the same cloud.

**Question:**
- Are Oracle Fusion internal integrations (SCM to ERP, ERP to EPM) considered "integrations" requiring MSP support, or "application configuration" managed by Oracle admins?
- If an automated process fails (e.g., sales order doesn't create purchase order), who investigates:
  - MSP integration team?
  - MSP Oracle SCM functional expert?
  - McGrath business analyst?

**Why it matters:** Defines whether MSP needs deep Oracle Fusion functional expertise across all four clouds (SCM, ERP, CX, EPM) or if internal Oracle integrations are handled by a separate Oracle Center of Excellence.

---

## 8. Change Management & Testing

### Q8.1: Integration Testing After Oracle Cloud Updates
**Context:** Oracle Cloud delivers quarterly feature updates that can break integrations.

**Question:**
- Does McGrath have a sandbox/test environment that mirrors production integrations?
- After Oracle quarterly updates, who performs integration regression testing:
  - MSP runs test scripts?
  - McGrath QA team?
  - Vendor partners (RecVue, Salesforce)?
- If an Oracle update breaks an integration, what's the rollback process? (Oracle doesn't allow rollback—is there a workaround process?)

**Why it matters:** Integration testing is time-intensive. If MSP must test 50+ integrations quarterly, this is significant recurring effort. Defines whether MSP needs dedicated QA resources vs ad-hoc testing by admins.

---

## 9. High-Level Scoping Questions

### Q9.1: Integration Monitoring Baseline
**Question:** What percentage of the 50+ integrations currently have automated monitoring (success/failure alerts)?

**Why it matters:** If 0% have monitoring, MSP must build from scratch. If 100% have monitoring, MSP inherits existing alerting and focuses on response/remediation.

---

### Q9.2: Current Integration Team Size
**Question:** How many FTEs currently support these integrations at McGrath? What are their skill sets (Oracle, Salesforce, middleware, data engineering)?

**Why it matters:** Establishes baseline for MSP staffing proposal. If McGrath currently has 2 FTEs struggling, MSP may propose 3-4. If they have 8 FTEs, there may be inefficiencies to address.

---

## Appendix: Integration Count by Type

Based on architecture analysis:

| Integration Type | Count (Approx) | Notes |
|------------------|----------------|-------|
| **Synchronous** | 35+ | Majority—high uptime requirement |
| **Asynchronous** | 8+ | ADP, Xactly, Zilliant, Oracle Aconex |
| **Data Extract/Load** | 5+ | Snowflake, Tableau, Rivery, SplashBI |
| **Identity/HR** | 2 | AD, ADP |
| **Custom Apps** | 2+ | Material Voucher, Nextstar |
| **Legacy/Unknown** | 2 | Oracle CRM on Demand, Nextstar |

**Total visible integration points:** 50+
**High complexity hubs:** Salesforce, RecVue, Oracle ERP, Snowflake

---

## Recommended Next Steps

1. **Prioritize Q1.2, Q2.1, Q3.1:** These define fundamental MSP scope boundaries
2. **Request Integration Inventory:** Ask McGrath for spreadsheet listing all integrations with ownership, monitoring status, and criticality rating
3. **Schedule Architecture Deep-Dive:** 2-hour session with McGrath integration team to walk through 5-10 most critical integration flows
4. **Assess Monitoring Gaps:** Review current monitoring tools and identify blind spots

---

**Document Status:** Draft for internal review
**Next Action:** Share with McGrath during RFP Q&A phase
