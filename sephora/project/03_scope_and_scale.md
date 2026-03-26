# Sephora EDW Modernization - Scope and Scale

*Last updated: February 12, 2026*

---

## Quantified Scope

These numbers were provided by Gariashi and represent the scale of the migration challenge:

| Asset Type | Count | Notes |
|------------|-------|-------|
| **Reports** | ~6,000 | Across Cognos, varying complexity |
| **SSAS Cubes** | 8 | Major migration blocker |
| **KPIs** | 800+ | Business-critical metrics |
| **Dimensions** | 300 | Reference data structures |
| **Source Systems** | 20+ | Feed into the EDW |
| **ETL Pipelines** | Thousands | DataStage jobs |

---

## Report Complexity Spectrum

"Reports" can mean very different things. Understanding the distribution is critical:

| Type | Description | Migration Complexity |
|------|-------------|---------------------|
| **Tabular/Static** | Excel-like data tables, canned outputs | Low |
| **Filtering-based** | User-defined parameter reports | Low-Medium |
| **Email reports** | Scheduled distribution | Medium (need automation rebuild) |
| **Excel pivot/analysis** | Via SSAS cubes | HIGH (cube dependency) |
| **Interactive dashboards** | Drill-down, executive-level | Medium-High |
| **Specialized/Engineering** | Deep technical reports | Variable |

**Key question to answer:** What is the distribution across these types? This determines where AI can help most.

---

## EDW Characteristics

| Attribute | Value |
|-----------|-------|
| **Age** | ~20 years |
| **Size** | "Massive" (specific metrics unknown) |
| **Processing** | Batch only (no real-time) |
| **Scalability** | Limited / hard to scale |
| **Platform** | SQL Server |

---

## Timeline

| Milestone | Target |
|-----------|--------|
| Program start | 2026 |
| Program end | 2028 |
| Total duration | 3 years |

**Key observation:** This appears to be a goal, not a detailed plan. The breakdown of where time is consumed (analysis vs. rebuild vs. validation/sign-off) is unclear.

---

## Migration Tracks (Parallel Workstreams)

| Track | Status |
|-------|--------|
| Finance | In progress |
| Digital / E-commerce | In progress |
| Other tracks | Various phases |

All tracks follow the same general phases:
1. Rationalization / analysis
2. Data migration to Databricks
3. Pipeline re-engineering
4. Report conversion
5. Validation and sign-off

---

## Current Tools Inventory

### Source Stack (Being Migrated From)
- SQL Server (EDW storage)
- SSAS Cubes (analytical layer)
- IBM Cognos (reporting)
- IBM DataStage (ETL)

### Target Stack (Being Migrated To)
- Databricks (lakehouse platform)
- Tableau (BI/visualization)
- ThoughtSpot (self-service analytics)

### In Flux
- Semantic layer approach (TBD)
- SSAS cube replacement strategy (major open question)

---

## Data Considerations

| Category | Status |
|----------|--------|
| **Security/Access** | No major blockers expected |
| **PII** | Exists but nothing unusual |
| **Compliance** | Standard retail data considerations |

---

## What's Already Completed

| Phase | Status |
|-------|--------|
| Report rationalization (Phase 1) | Done |
| Some data migration to Databricks | Done |
| Pipeline re-engineering (select tracks) | In progress |
| AI mapping tool POCs | Done (validated AI helps, but manual validation still required) |

---

## Scale Implications for AI Opportunity

Given the scale, even small per-unit improvements have large aggregate impact:

| If AI saves... | Across 6,000 reports... | Total savings |
|----------------|------------------------|---------------|
| 30 min per report | 6,000 reports | 3,000 hours |
| 1 hour per pipeline | 2,000 pipelines | 2,000 hours |
| 50% mapping time | All tracks | Significant |

This is a **volume play** where AI acceleration tools could deliver substantial ROI.

---

## Key Unknowns (Scope Gaps)

- [ ] Exact number of DataStage pipelines
- [ ] Distribution of report complexity types
- [ ] Specific data volume metrics (TB/PB)
- [ ] Breakdown of 3-year timeline by phase
- [ ] Number of users impacted by SSAS cube changes
- [ ] Budget for the modernization program

---

## Related Documents

- [Project Overview](./00_project_overview.md)
- [Pain Points and Opportunities](./02_pain_points.md)
