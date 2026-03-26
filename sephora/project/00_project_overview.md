# Sephora EDW Modernization - Project Overview

*Last updated: February 12, 2026*

---

## Executive Summary

Sephora is undertaking a **3-year enterprise data warehouse (EDW) modernization program** to migrate from their legacy SQL/Cognos environment to Databricks. The program involves re-engineering thousands of reports, ETL pipelines, and data models across multiple business tracks.

**Timeline:** 2026-2028 (possibly complete by early 2028 or even 2027 if AI-accelerated)

**Core Migration Path:**
```
Legacy Stack                    Target Stack
─────────────                   ────────────
SQL Server (EDW)        ───►    Databricks (Lakehouse)
SSAS Cubes              ───►    (TBD - major blocker)
Cognos Reports          ───►    Tableau / ThoughtSpot
DataStage ETL           ───►    Databricks pipelines
                                Some Cognos retained (data layer modernized)
```

---

## Major Organizational Shift: Democratization Model (2026)

**This is a significant strategic change.** Starting 2026, reporting is being **decentralized** from Mani's centralized team into domain engineering teams.

### Current State (Pre-2026)
- Centralized reporting team under Mani
- Single team handles all reporting across domains

### Future State (2026 Onward)
- Reporting becomes **embedded within domain engineering teams** (Stores, E-commerce, Supply Chain, etc.)
- Mani's team transitions to:
  - Lean governance
  - Framework + tool standardization
  - SME advisory support
  - Data validation + architectural oversight

### Three Operating Models Being Tested

| Model | Domain | Status | Timeline |
|-------|--------|--------|----------|
| **Model 1** | Stores (David/Natalia) | Delivery owned by Stores, Mani provides SME oversight | ~1 year to stabilize |
| **Model 2** | E-commerce (Rajesh, starting with Omni) | Hiring through Grishi, engineers execute in Rajesh's org | May fully transition by June/July 2026 |
| **Model 3** | Supply Chain / Merchandising | Still centralized under Grishi | Transitions later (legacy tech prevents immediate decentralization) |

**Implication for BayOne:** This decentralization creates multiple entry points and hiring opportunities across different domain teams, not just Mani's central org.

---

## Program Context

### What's Being Migrated

| Component | Scale | Complexity |
|-----------|-------|------------|
| Reports | ~6,000 | 15-20 years of legacy, high variability |
| SSAS Cubes | 8 | Contains pre-aggregated business logic |
| KPIs | 800+ | Business-critical metrics |
| Dimensions | 300 | Reference data structures |
| Source Systems | 20+ | Feed into the EDW |
| ETL Pipelines | Thousands | DataStage jobs with embedded business rules |

### The Legacy EDW
- ~20 years old
- Massive and hard to scale
- Batch processing only (no real-time capability)
- Contains decades of accumulated business logic
- Queries buried in old Cognos reports

### Core Challenges (Per Mani)
- Deep legacy codebase
- Queries buried in old Cognos reports
- Manual review = years of effort
- Migration report-by-report is too slow

---

## Where They Want AI Help (Explicitly Stated)

Mani explicitly mentioned these AI acceleration opportunities:

### 1. Acceleration of Report Migration
- Can multiple reports be migrated at once?
- Can something auto-detect common structures?
- Can tooling reduce manual review?

### 2. AI-Based Codebase Analysis
They want AI to:
- Scan legacy Cognos/SQL code
- Identify hidden logic
- Highlight risks
- Recommend migration approach
- Surface buried dependencies

### 3. Databricks AI Tools Exploration
- Already speaking with Databricks
- Still experimenting - **not locked into a direction yet**
- Looking for acceleration strategy

**Key Quote:** *"If someone comes with groundwork done and a proposal — that would be very productive."*

---

## Current Reporting Landscape

### Tools in Use

| Tool | Purpose |
|------|---------|
| **Cognos** | Primary legacy reporting (being deprecated, some retained with modernized data layer) |
| **Tableau** | Target BI tool |
| **ThoughtSpot** | Target BI tool |
| **SSAS Cubes** | Excel-based analytical interface (major migration blocker) |
| **DataStage** | Legacy ETL tool (IBM) |
| **Databricks** | Target lakehouse platform |
| **SQL Server** | Legacy EDW storage |

### Report Types
- Canned / static reports
- Filtering-based custom reports
- Excel-based pivot/analysis tools (via SSAS cubes)
- Email reports
- Interactive dashboards

---

## Two Parallel Opportunities

Sephora's engagement with BayOne has **two distinct tracks**:

### 1. Staffing Track
- Multiple hiring managers: Ram, Andrew, Grishi, Rizwan (late Q1)
- Rate strategy: $105-115/hr ($120+ only if on-site)
- Preference: Nearshore US talent
- Skills sought: Full stack, Full stack + AI, AI-enabled data processing, Agentic AI

### 2. Solutions / Strategic Partnership Track
- AI-assisted tooling and recommendations
- This is a **3-year modernization program, not a small POC**
- They are **explicitly looking for AI acceleration**
- They want **proposal-led conversation**, not discovery-only

**Key insight:** They're not locked into Databricks AI tools yet - still experimenting. This creates opportunity for BayOne to influence direction.

---

## 2026 Major Focus Areas

Beyond EDW modernization, Mani's org is focused on:
- Marketing AI task force
- Journey orchestration
- CRM personalization
- Influencer marketing expansion

---

## Suggested Pilot Area

**Finance - Business Planning reports** mentioned as potential pilot area for AI-assisted migration.

---

## Data Landscape Quick Facts

- **Source systems:** ~20 feed into the EDW
- **Security/Access:** No major blockers expected
- **PII:** Exists but nothing unusual
- **Compliance:** Standard retail data considerations

---

## Related Documents

- [People Directory](../stakeholders/00_people_directory.md)
- [Key Terms and Definitions](./01_glossary.md)
- [Pain Points and Opportunities](./02_pain_points.md)
- [Scope and Scale](./03_scope_and_scale.md)
