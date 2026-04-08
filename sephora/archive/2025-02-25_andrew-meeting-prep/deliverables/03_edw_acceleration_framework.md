# EDW Modernization
## AI Acceleration Framework
### February 25, 2026

---

## Our Understanding

Sephora is in year one of a three-year EDW re-engineering program, moving from SQL Server, Cognos, and DataStage to Databricks while retaining the Cognos front-end to minimize change management disruption.

The Finance track is near completion and has established the architectural patterns and methodology that will carry forward into Merchandising, Supply Chain, and other domains.

### Scale

| Asset | Volume |
|-------|--------|
| Cognos Reports | 6,000+ |
| SSAS Cubes | 8 |
| KPIs | 800+ |
| Dimensions | 300 |
| Source Systems | 20+ |

### The Core Constraint

The same SMEs needed to keep production running are also needed to validate the re-engineering work. This creates a bandwidth ceiling that determines how fast the program can move. AI acceleration is valuable to the extent that it reduces the burden on these constrained resources.

### Current AI Tooling

The team is actively using Lutra and Flow, evaluating Databricks AI capabilities, and has assessed various partner accelerators. Any additional tooling should complement what exists rather than add fragmentation.

---

## AI Acceleration Ideas

### Report Similarity Clustering

Analyze Cognos report metadata including columns, joins, filters, and output structures to group reports by structural similarity. Reports that share the same underlying data sources and similar query patterns can be re-engineered together as a batch rather than handled individually. This directly supports the goal of processing multiple reports in a single pass.

### Business Logic Extraction

Parse Cognos report definitions and embedded SQL to extract calculations, filters, and business rules into a readable catalog. Twenty years of accumulated logic is sitting inside these reports, implemented by developers who are no longer with the organization. Making this logic visible and documented accelerates SME review and reduces the risk of losing critical business rules during re-engineering.

### Dependency Mapping

Trace the relationships between tables, views, reports, and cubes to create a complete dependency graph. Before touching any source table or deprecating any cube, the team can see exactly what downstream assets are affected. This prevents the surprises that slow down re-engineering efforts when unexpected dependencies surface mid-project.

### Schema Mapping Validation

Automate source-to-target column mapping with confidence scoring. High-confidence mappings proceed without manual review. Low-confidence mappings are flagged for SME attention. This focuses human effort on the cases that actually need human judgment rather than requiring review of every single mapping.

### KPI Lineage Tracing

Map the 800+ KPIs back to their source calculations across reports, cubes, and pipelines. Identify cases where the same KPI is calculated differently in different places, which creates data quality issues and confusion for business users. Standardizing KPI definitions is a prerequisite for a clean semantic layer.

### Change Impact Analysis

Before making any change to source systems, tables, or transformation logic, simulate the downstream impact across the entire reporting portfolio. This allows the team to make changes with confidence rather than discovering broken reports after the fact.

### Documentation Generation

Generate documentation for undocumented stored procedures, DataStage jobs, and Cognos report logic. The institutional knowledge that exists only in code becomes explicit and reviewable. This is particularly valuable for onboarding new team members and for SME validation of extracted business logic.

### Consolidation Detection

Identify reports that perform nearly identical functions with minor variations. Organizations accumulate redundant reports over time as different teams request similar outputs. Surfacing these consolidation opportunities reduces the total volume of assets that need to be re-engineered and simplifies the target state.

---

*Prepared for Andrew Ho & Grishi Chakraborty*
*BayOne Solutions*
