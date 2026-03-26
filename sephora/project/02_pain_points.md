# Sephora EDW Modernization - Pain Points and Opportunities

*Last updated: February 12, 2026*

---

## Critical Blockers

### A. SSAS Cubes Migration Blocker (HIGHEST PRIORITY)

**The stated problem:** SSAS Cubes sit on top of the legacy EDW. To move them to Databricks, they need a "connector" which currently doesn't exist.

**The actual problem (Colin's analysis):** This isn't really a connector problem. Databricks has mature connectivity (ODBC/JDBC) - you can already natively connect Excel, Tableau, Power BI today.

What they're really saying is: *"Business users are used to SSAS cubes and we don't want to change their experience."*

**Why this matters:**
- This is a **change management problem**, not a technical one
- Trying to preserve the legacy cube experience while moving to Databricks will create long-term maintenance headaches
- If they're investing in a 3-year modernization, they should modernize the semantic layer too - not build compatibility shims to keep 20-year-old services alive

**Business impact:**
- Users currently rely on Excel-based cube interfaces
- Canned reports depend on cubes
- Ad-hoc drag-and-drop dashboards depend on cubes
- Switching tools completely would cause massive change management

**What Sephora wants:** Help figuring out a way to keep the same interface/experience while pulling data from Databricks underneath.

**Colin's concern:** A "half-in, half-out" approach rarely works successfully. It requires a strong internal leader at Sephora with real power to enact and force change. If that person doesn't exist or is a "yes-man" to business users, there will be constant churn.

**Opportunity:** This is one of the biggest AI-assisted opportunity areas if the organizational dynamics can be navigated.

---

### B. Re-engineering Thousands of ETL Pipelines

**The problem:** There are thousands of DataStage ETL jobs that must be migrated. Each requires:
- Extracting logic
- Re-architecting for Databricks
- Rebuilding transformations across many tables
- Old EDW → Databricks mapping is **not 1:1** (one EDW table may become 5 Databricks tables)

**AI opportunity:** Tooling that helps:
- Extract SQL logic automatically
- Identify tables and dependencies
- Discover lineage
- Generate Databricks-compatible code

**Scale:** Thousands of pipelines - this is a volume problem where AI acceleration could have massive impact.

---

### C. Embedded SQL Inside Cognos Reports

**The problem:** Some Cognos reports contain embedded SQL that may break when moving to Databricks due to:
- Syntax differences
- Table/column name changes
- Databricks-specific optimization requirements

**What's needed:**
- Detection of embedded SQL
- Identification of break points
- SQL rewriting for Databricks compatibility
- Performance optimization

**AI opportunity:** Automated SQL analysis and conversion suggestions.

---

### D. Data Mapping - Slowest Phase

**The problem:** Data mapping (source-to-target) is currently one of the **slowest phases** of the migration. Even with AI tools:
- Engineers still manually validate every mapping
- This slows down each migration track
- High manual effort per pipeline

**What's being done:** They've used AI tools for mapping POCs and validated that AI helps, but manual validation is still required.

**AI opportunity:** Streamline mapping validation, not just mapping suggestions. Reduce the "last mile" manual effort.

---

### E. Report-by-Report Migration Too Slow

**The problem (per Mani):** Migrating reports one-by-one is too slow given the scale (6,000 reports, 15-20 years of legacy).

**What they're exploring:**
- Can multiple reports be migrated at once?
- Can something auto-detect common structures?
- Can tooling reduce manual review?

**This is a HUGE opportunity for AI:**
- Pattern detection across reports
- Report clustering by similarity
- Batch migration of similar reports
- Automated structure detection

---

## Specific AI Opportunities (Mani's Explicit Ask)

These were explicitly mentioned by Mani as areas where AI could help:

| Capability | Description | Impact |
|------------|-------------|--------|
| **Codebase analysis** | AI to scan legacy Cognos/SQL code | HIGH |
| **Pattern detection** | Identify common structures across reports | HIGH |
| **Report clustering** | Group similar reports for batch migration | HIGH |
| **Schema dependency mapping** | Surface buried dependencies | HIGH |
| **Automated rewrite suggestions** | Generate Databricks-compatible code | MEDIUM-HIGH |
| **Query optimization suggestions** | Improve performance post-migration | MEDIUM |
| **Impact analysis** | Understand downstream effects of changes | MEDIUM |
| **Hidden logic identification** | Find business rules buried in code | HIGH |
| **Risk highlighting** | Flag potential migration issues | MEDIUM |

**Key Quote:** *"If someone comes with groundwork done and a proposal — that would be very productive."*

---

## Operational Pain Points

### Manual Review Bottleneck

**The problem:** Manual review of each report/pipeline is creating a years-long timeline.

**What's needed:** AI-assisted tooling to:
- Reduce manual review burden
- Automate validation where possible
- Flag only high-risk items for human review

---

### Organizational Complexity (Decentralization)

**New in 2026:** Reporting is being decentralized into domain teams (Stores, E-commerce, Supply Chain).

**Implications:**
- Multiple stakeholders across different orgs
- Different teams at different maturity levels
- Model 3 (Supply Chain/Merchandising) has legacy tech preventing immediate decentralization
- Coordination complexity increases

**Opportunity:** BayOne could help with standardization and framework development as Mani's team transitions to governance role.

---

### Databricks Direction Not Yet Locked

**Status:** Sephora is speaking with Databricks about their AI tools but is **still experimenting**.

**Implication:** They are **not locked into a direction yet**. This creates opportunity for BayOne to:
- Influence the approach
- Propose alternative or complementary tools
- Position as the acceleration strategy partner

---

## Opportunity Summary

| Area | Type | Potential Impact | Status |
|------|------|------------------|--------|
| Multi-report batch migration | AI Tooling | **VERY HIGH** | Explicitly requested |
| Codebase analysis / scanning | AI Tooling | **HIGH** | Explicitly requested |
| Pattern detection / clustering | AI Tooling | **HIGH** | Explicitly requested |
| Schema dependency mapping | AI Tooling | **HIGH** | Explicitly requested |
| SSAS Cube experience preservation | Strategy + Change Management | HIGH (but risky) | Needs careful navigation |
| ETL pipeline conversion | AI Tooling | HIGH (volume play) | Known need |
| Embedded SQL detection/rewriting | AI Tooling | MEDIUM-HIGH | Known need |
| Data mapping automation | AI Tooling | MEDIUM-HIGH | POC done, more needed |
| Governance framework (decentralization) | Advisory | MEDIUM | New opportunity |

---

## Colin's Past Experience

Colin led BI reporting and migration at Coherent (BI fell naturally under AI because of the deep ties with Data). This gives BayOne:
- Real experience doing exactly what Mani wants
- Credibility to speak to both technical and strategic aspects
- Understanding of what works and what doesn't in these migrations

---

## Suggested Pilot Area

**Finance - Business Planning reports** mentioned as potential pilot area for AI-assisted migration approach.

---

## Preparation Recommendations (Per Zahra)

Before meeting Mani, Colin should review:
- Cognos-to-Databricks migration frameworks
- AI-assisted SQL transformation
- LLM-based codebase scanning tools
- Automated schema lineage tools
- Semantic layer reconstruction approaches

And prepare:
- **1-page POV:** AI-Assisted EDW Modernization Framework
- Example architecture flow
- Suggested phased approach
- Potential pilot area (Finance - Business Planning reports)

**Come with:** Structured proposal, not "what are your pain points" but "Here's how we would accelerate your migration."

---

## Related Documents

- [Project Overview](./00_project_overview.md)
- [Key Terms and Definitions](./01_glossary.md)
- [Scope and Scale](./03_scope_and_scale.md)
