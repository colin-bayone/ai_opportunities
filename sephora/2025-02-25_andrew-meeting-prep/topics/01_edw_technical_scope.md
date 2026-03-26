# EDW Technical Scope - Comprehensive Detail

## Project Overview

| Attribute | Value | Source |
|-----------|-------|--------|
| **Project Name** | EDW Modernization | Mani, Meeting 1 |
| **Project Type** | Re-engineering (NOT migration) | Mani, Meeting 2 - explicit correction |
| **Duration** | 3 years (2026-2028) | Mani, Meeting 1 |
| **Acceleration Target** | Complete by 2027 or early 2028 | Mani, Meeting 1 |
| **Start Date** | Already started (as of late 2025) | Mani, Meeting 1 |

---

## Source Environment (Legacy)

### Database Layer
| Component | Details | Source |
|-----------|---------|--------|
| **Primary Database** | SQL Server | Mani, Meeting 1 |
| **Age** | 15-20 years of accumulated work | Mani, Meeting 1 |
| **Data Warehouse** | Enterprise Data Warehouse (EDW) | Mani, Meeting 1 |

### Reporting Layer
| Component | Details | Source |
|-----------|---------|--------|
| **Primary BI Tool** | IBM Cognos | Mani, Meeting 1 |
| **OLAP Layer** | SSAS Cubes (8 cubes identified elsewhere) | Colin context, Meeting 2 |
| **Report Count** | "Thousands" (exact count unknown) | Mani, Meeting 1 |
| **Report Age** | 15-20 years of accumulated reports | Mani, Meeting 1 |

### ETL/Pipeline Layer
| Component | Details | Source |
|-----------|---------|--------|
| **ETL Tool** | IBM DataStage | Colin summary, Meeting 2 |
| **Pipeline Count** | "Thousands" (exact count unknown) | Implied from report count |

### Known Complexity Factors
- Embedded SQL in Cognos reports
- Business logic buried in code
- 15-20 years of tribal knowledge
- Dependencies not fully documented
- Queries "very deep inside the code"

---

## Target Environment (Modern)

### Data Platform
| Component | Details | Source |
|-----------|---------|--------|
| **Target Platform** | Databricks | Mani, Meeting 1 & 2 |
| **Architecture** | Lakehouse (implied) | Industry standard for Databricks |
| **Cloud Provider** | Microsoft Azure (Microsoft at governance table) | Mani, Meeting 2 |

### Reporting Layer (Planned)
| Component | Details | Status | Source |
|-----------|---------|--------|--------|
| **ThoughtSpot** | Under consideration | Future, not priority | Mani, Meeting 2 |
| **Tableau** | Under consideration | Future, not priority | Mani, Meeting 2 |
| **Cognos** | Retained during transition | Current strategy | Mani, Meeting 2 |

### Critical Clarification on Reporting
> "There is a desire to move to ThoughtSpot or Tableau, but that's not something that we are pursuing right now. The change management is not... it's not so resistant. That's why we're keeping this."
> — Mani, Meeting 2

**Translation:** Front-end (Cognos) stays; back-end (data) moves to Databricks.

---

## Semantic Layer

| Aspect | Details | Source |
|--------|---------|--------|
| **Status** | Being formed, ongoing effort | Mani, Meeting 2 |
| **Priority** | Secondary to progress | Mani, Meeting 2 |
| **Owners** | Andrew Ho and Terti | Mani, Meeting 2 |
| **Philosophy** | "If semantic layer slows us down, we just go ahead" | Mani, Meeting 2 |

---

## Track-Based Approach

### Track Sequencing
| Track | Status | Timeline | Notes |
|-------|--------|----------|-------|
| **Finance** | In progress, nearly complete | ~20-24 days remaining | First track, patterns established |
| **Finance - Business Planning** | First sub-track | Almost done | Subdivision approach |
| **Finance - Accounting** | Queued | After Business Planning | Later priority |
| **Supply Chain** | Not started | Future | Potential pilot for BayOne |
| **Merchandising** | Not started | Future | Potential pilot for BayOne |
| **Stores** | Not started | Future | Under David's team |
| **E-commerce/Omni** | Not started | Future | Under Rajesh |

### Pattern Established from Finance Track
- Architectural patterns defined
- Accelerator tools evaluated and selected
- Roadmap sequencing methodology proven
- Can be applied to subsequent tracks

---

## Scale Metrics

### Quantified
| Metric | Value | Confidence | Source |
|--------|-------|------------|--------|
| Reports | "Thousands" | Medium | Mani, Meeting 1 |
| SSAS Cubes | 8 | High | Context documents |
| KPIs | 800+ | Medium | Context documents |
| Dimensions | 300 | Medium | Context documents |
| Source Systems | 20+ | Medium | Context documents |
| DataStage Pipelines | "Thousands" | Low | Implied |
| Project Duration | 3 years | High | Mani, Meeting 1 |

### Unquantified (Gaps)
- Exact report count
- Exact pipeline count
- Data volume (TB/PB)
- User count
- Report complexity distribution
- Daily query volume

---

## Technical Challenges Identified

### 1. Codebase Complexity
> "Cognos, there are actually like 15, 20 years back, something might have been implemented. So the queries are actually like very deep inside the code. We can't... if we have manually, if somebody has to go through that, it will take years for us to even finish this."
> — Mani, Meeting 1

**Challenge:** Buried business logic, embedded SQL, undocumented dependencies

### 2. Scale of Re-engineering
> "If we go report by report, it will take a long time for us."
> — Mani, Meeting 1

**Challenge:** Volume prohibits manual approach; need batch/pattern-based methods

### 3. Knowledge Preservation
**Challenge:** Tribal knowledge in legacy systems must be preserved during re-engineering

### 4. Change Management
> "The change management is not... it's not so resistant. That's why we're keeping this [Cognos]."
> — Mani, Meeting 2

**Challenge:** Business users attached to existing interfaces

### 5. SSAS Cube Transition
**Challenge:** Excel-based cube interfaces relied upon by business users; no direct "connector" to Databricks (change management issue, not technical)

### 6. Validation Requirements
**Challenge:** Even with AI assistance, human validation required for parity checks

---

## Governance Structure

### Core Governance Table
| Stakeholder | Role | Source |
|-------------|------|--------|
| Databricks | Platform partner, accelerator provider | Mani, Meeting 2 |
| Microsoft | Cloud platform (Azure) | Mani, Meeting 2 |
| Data Platform Team | Internal data architecture | Mani, Meeting 2 |
| Store Engineering | Domain representation | Mani, Meeting 2 |
| BI SMEs | Report expertise | Mani, Meeting 2 |

### Decision Authority
> "This team together, regardless where they come from, doesn't matter. But this is the core team. This team establishes what's right to do, how to do it."
> — Mani, Meeting 2

---

## Tools & Accelerators in Use/Evaluation

| Tool | Type | Status | Source |
|------|------|--------|--------|
| Databricks native tools | Platform | In use | Mani, Meeting 2 |
| Databricks partner accelerators | Migration | Evaluated | Mani, Meeting 2 |
| Lutra | AI/Automation | In use | Mani, Meeting 2 |
| Flow | AI/Automation | In use | Mani, Meeting 2 |
| Various code analysis tools | Code extraction | Evaluated | Mani, Meeting 2 |

> "Each tool has its own strength. Now, the team is assessing... which particular tool is good and for what."
> — Mani, Meeting 2

---

## What "Re-engineering" Means (Not Migration)

### Migration (What They're NOT Doing)
- Lift and shift
- Moving data from here to there
- Keeping same logic/structure
- 1:1 mapping

### Re-engineering (What They ARE Doing)
- Rewiring and rebuilding
- Re-architecting for modern platform
- Potentially consolidating reports
- Potentially eliminating redundancy
- New patterns for Databricks optimization

> "It's not just migration. We have to re-engineer that. We have to re-engineer and rewire those things."
> — Mani, Meeting 2

---

## Impact on BayOne Engagement

### What This Means for Proposal
1. Don't call it "migration" - always "modernization" or "re-engineering"
2. Pattern-based approaches align with their philosophy
3. Code analysis for hidden logic is high value
4. Batch processing (not report-by-report) is the ask
5. Front-end changes are out of scope for now
6. Back-end (data platform) work is in scope

### Technical Credibility Points
- Colin's Snowflake experience directly relevant
- BI/AI same-roof experience valuable
- Understanding of SSAS/SSRS demonstrates depth
- Recognition of change management challenges builds trust
