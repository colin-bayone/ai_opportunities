# Sephora EDW Modernization - Key Terms and Definitions

*Last updated: February 12, 2026*

---

## Core Technologies

### EDW (Enterprise Data Warehouse)

**What it is:** A centralized repository that integrates structured data from across an organization's multiple systems, optimized for query and analysis rather than transaction processing. Traditional EDWs run on platforms like Teradata, Oracle, or SQL Server with separate storage and compute layers.

**In Sephora's context:** The legacy EDW is ~20 years old, massive, and hard to scale. It's the source system being migrated away from. Contains data from 20+ source systems with decades of accumulated business logic.

**Why it matters:** This is the core infrastructure being modernized. Legacy EDWs face challenges with cost (expensive hardware/licensing), scalability (can't handle modern data volumes), and rigidity (batch-only, can't support real-time or AI workloads).

---

### SSAS (SQL Server Analysis Services) / SSAS Cubes

**What it is:** Microsoft's enterprise OLAP (Online Analytical Processing) tool that creates multidimensional data structures called "cubes." These cubes organize data into dimensions (time, geography, products) and measures (sales, revenue) for near-instantaneous analysis without requiring complex SQL queries.

**In Sephora's context:** Sephora has **8 SSAS cubes** sitting on top of the legacy EDW. Business users interact with these via Excel-based interfaces for drag-and-drop analysis. This is a **major migration blocker** because:
- There's no native connector between SSAS cubes and Databricks
- Business users are deeply attached to the Excel-based cube experience
- Forcing a tool change would cause massive change management issues

**Why it matters:** The "connector problem" that Sephora has identified is actually a change management problem, not a technical one. Databricks has mature connectivity (ODBC/JDBC), but users want to preserve the legacy cube experience. This creates long-term maintenance headaches if they try to build compatibility shims.

---

### IBM Cognos Analytics

**What it is:** IBM's enterprise BI and reporting platform that provides interactive reports, dashboards, and AI-assisted analytics with strong governance features. Typically deployed on-premises or in private clouds.

**In Sephora's context:** The **primary legacy reporting platform** being migrated away from. Houses ~6,000 reports. Some Cognos reports contain **embedded SQL** that may break when data moves to Databricks.

**Why it matters:** Cognos represents the "source" in this migration. Organizations typically move away from Cognos due to higher costs, complex deployment, and limited cloud-native capabilities. The embedded SQL within Cognos reports needs to be detected, analyzed, and potentially rewritten.

---

### IBM DataStage

**What it is:** IBM's industry-leading ETL (Extract, Transform, Load) tool that connects disparate data sources, transforms large volumes of complex data, and delivers data across hybrid cloud environments.

**In Sephora's context:** Sephora has **thousands of DataStage ETL jobs** that need to be migrated. Each job requires:
- Extracting business logic
- Re-architecting for Databricks
- Rebuilding transformations
- Handling non-1:1 mappings (e.g., one EDW table may become 5 Databricks tables)

**Why it matters:** DataStage jobs often contain decades of business rules. Incorrect translation can cause data quality issues. This is one of the biggest bottlenecks in the migration.

---

### Databricks

**What it is:** A unified "lakehouse" platform that combines the best elements of data lakes (low-cost object storage) and data warehouses (structured query performance). Built on Apache Spark. Handles structured, semi-structured, and unstructured data in one place with integrated AI/ML capabilities.

**In Sephora's context:** The **target platform** for the modernization. Data is being migrated into Databricks, with reporting shifting to Tableau/ThoughtSpot on top.

**Why it matters:** Offers potential for 5-10x performance improvements, lower costs, and native support for both SQL analytics and AI workloads. However, the value proposition is undermined if Sephora tries to preserve legacy patterns (like SSAS cubes) rather than modernizing fully.

---

### Tableau

**What it is:** Salesforce's visual analytics and BI platform known for advanced data visualization, drag-and-drop interface, and deep enterprise integrations.

**In Sephora's context:** One of the **target BI tools** for the migration (alongside ThoughtSpot). Dashboards will be rebuilt in Tableau from Cognos.

**Why it matters:** Requires careful planning around semantic layer migration and dashboard conversion from Cognos.

---

### ThoughtSpot (possibly "Hotspot")

**What it is:** An AI-powered, search-driven BI platform that emphasizes self-service analytics through natural language queries. Users can explore data without writing SQL.

**In Sephora's context:** One of the **target BI tools**. The term "Hotspot" in internal communications likely refers to ThoughtSpot.

**Why it matters:** Integrates natively with Databricks. Good for self-service analytics use cases where business users need to explore data independently.

---

### Semantic Layer

**What it is:** A business-friendly abstraction layer between raw data and analytics tools. Defines business terms, metrics, and relationships in one centralized place. Ensures that terms like "revenue," "customer," or "conversion rate" mean the same thing across all BI tools and reports.

**In Sephora's context:** The SSAS cubes and Cognos reports contain years of embedded business logic that serves as a de facto semantic layer. This must be reconstructed in the new environment.

**Why it matters:** One of the most critical (and often underestimated) migration components. If the semantic layer isn't properly migrated, different reports may show conflicting numbers, eroding trust in the new platform.

---

## Technical Processes

### ETL (Extract, Transform, Load)

**What it is:** The process of extracting data from source systems, transforming it to fit business needs, and loading it into a target system (like a data warehouse).

**In Sephora's context:** Thousands of DataStage ETL pipelines need to be re-engineered for Databricks.

---

### Data Mapping

**What it is:** The process of defining how data elements from source systems correspond to elements in the target system.

**In Sephora's context:** Currently one of the **slowest phases** of their migration. Even with AI assistance, engineers still manually validate mappings. AI can help with:
- Automated mapping suggestions
- Lineage discovery
- Pattern detection
- Redundancy identification

---

### Data Lineage

**What it is:** The full lifecycle of data - where it comes from, how it moves, and what transformations it undergoes.

**In Sephora's context:** AI-assisted lineage discovery is one of the areas where Sephora wants help. Understanding lineage is critical for:
- Impact analysis when making changes
- Debugging data quality issues
- Compliance and audit requirements

---

## Sephora-Specific Terms

### Report Rationalization

**What it is:** The process of analyzing existing reports to identify which are actually used vs. outdated/redundant.

**In Sephora's context:** They've completed Phase 1 rationalization. This helps prioritize what to migrate vs. what to retire.

---

### Migration Tracks

**What it is:** Parallel workstreams for migrating different business areas.

**In Sephora's context:** Includes Finance, Digital/e-comm, and others. Each track is at different phases of the migration.

---

### Complexity Scoring

**What it is:** A method of rating reports or pipelines by difficulty to migrate.

**In Sephora's context:** Sephora wants AI-assisted tooling to help score complexity and prioritize migration work.

---

## Related Documents

- [Project Overview](./00_project_overview.md)
- [Pain Points and Opportunities](./02_pain_points.md)
