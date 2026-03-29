# Demo Feasibility Analysis: What We Have vs. What We Need

**Created:** March 9, 2026
**Purpose:** Clear accounting of materials provided, materials missing, and whether each demo track is actually feasible

---

## The Two Demo Tracks

### Track A: Cognos MCP Demo (Original Scope from Wednesday)
**What it would show:** MCP server connects to Cognos → extracts report metadata/SQL → agent orchestration → converts to Databricks SQL → remaps to target schema

### Track B: ETL/DataStage Demo (Added in Malika's Email)
**What it would show:** Agent parses DataStage XML → extracts transformation logic → generates Databricks-compatible Scala/YAML matching their framework

---

## Track A: Cognos MCP Demo

### What We Need
1. Cognos report XML (to parse and convert)
2. Target Databricks schema (to remap the queries to)
3. Cognos environment access OR detailed API docs (to build MCP server)

### What They Provided
Nothing.

### What They Promised on Wednesday's Call
- Gariashi said Vlad would pull a Finance report XML from Report Studio
- They would provide target Databricks schema (catalog + table structure)

### Status: NOT FEASIBLE
We cannot demo this track without materials. Zero of the required inputs have been provided.

---

## Track B: ETL/DataStage Demo

### What the Demo Would Actually Produce

Looking at their target folder, the output would be:
1. **Scala application** (like `InventoryPeriodicDailyAggApplication.scala`) - Spark code that reads source tables, applies transformations, writes to target
2. **YAML config** (like `inventory-periodic-daily-with-flags-agg.yaml`) - Defines source file paths, output path, partition column
3. **Deployment YAML** (like `inventory-periodic-daily-with-flags-agg.deployment.yaml`) - Databricks cluster config, job settings
4. **Hive DDL** (like `create.hql`) - Target table definition

### What We Need to Generate That Output

To generate a Scala app, we need to know:
- What source tables to read from (their names and paths in Databricks)
- What columns exist in those source tables (schema)
- What transformations to apply (this comes from parsing the legacy job)
- What target table to write to (schema)

To generate a YAML config, we need to know:
- Source file paths in Databricks (e.g., `#{mcs_db_dbfs_path}#/edwlib_whintr`)
- Target output path
- Their parameterization scheme

### What They Provided

| Material | What It Tells Us |
|----------|------------------|
| DataStage XML (3 files) | Legacy job structure, embedded SQL, transformation logic |
| Stored procedures (2 files) | Additional legacy business logic |
| Views (2 files) | Legacy data access patterns |
| SQL Server DDL (3 files) | Legacy SOURCE table schemas (old system) |
| Target Scala apps (2 files) | Pattern to match for output |
| Target YAML configs (4 files) | Framework structure to match |
| Target create.hql (2 files) | TARGET OUTPUT table schemas only |

### What's Missing

**Critical Gap: Databricks Source Table Schemas**

The Scala apps read from tables like:
- `edwlib_whintr`
- `retfl030_skuloc`
- `retfl030_whctl`
- `smt_location`
- `smt_product`
- `e3_raq`
- `location_dc`

These are parquet files in their Databricks environment. The YAML configs reference them with parameterized paths:
```yaml
sourceFiles:
  - name: "edwlib_whintr"
    path: "#{mcs_db_dbfs_path}#/edwlib_whintr.snappy.parquet"
    format: "parquet"
```

**We do NOT know:**
- What columns exist in these Databricks source tables
- What data types they have
- Whether they match the legacy SQL Server schemas or have been transformed

**We only have:**
- Legacy SQL Server DDL (the OLD system, not Databricks)
- Target OUTPUT table DDL (inventory_periodic_daily, stock_continuity_all_sku)

**The problem:** We can parse the DataStage job and understand what it DOES. But to generate Scala code that reads from their Databricks sources, we need to know what those sources look like. We don't.

### What They Promised on Wednesday's Call
- Target Databricks schema (catalog + table structure) - Sergey was point person
- Sample YAML config (they did provide examples in target folder)

### Status: PARTIALLY FEASIBLE

We could demonstrate:
- Parsing the DataStage XML
- Extracting the embedded SQL and transformation logic
- Showing agent orchestration during parsing

We cannot accurately produce:
- Working Scala code that reads from their actual Databricks sources
- YAML configs with correct source table references

**We could fake it** by assuming the Databricks tables have similar schemas to the legacy SQL Server tables. But that's an assumption, not knowledge. The output would be a pattern demonstration, not production-ready code.

---

## Summary Table

| Track | Materials Provided | Materials Missing | Feasibility |
|-------|-------------------|-------------------|-------------|
| Cognos MCP | None | Everything (report XML, Databricks schema, access) | NOT FEASIBLE |
| ETL/DataStage | Legacy artifacts + target OUTPUT examples | Databricks SOURCE table schemas | PARTIALLY FEASIBLE (demo only, not working code) |

---

## What We Should Ask For

### If They Want Cognos Demo:
1. Cognos report XML from Finance folder (Vlad was supposed to provide)
2. Target Databricks schema (catalog + table structure)

### If They Want ETL Demo:
1. Databricks source table schemas (DDL or schema exports for edwlib_whintr, retfl030_skuloc, smt_location, smt_product, etc.)
2. Clarification: Do the Databricks sources mirror the legacy SQL Server structure, or have they been transformed?

### Either Way:
They need to provide the Databricks schema information. Without knowing what their Databricks environment looks like, we cannot generate code that targets it.

---

## The Fundamental Question

On Wednesday's call, they agreed to provide:
- Cognos report XML
- Target Databricks schema
- Sample YAML config

They provided:
- Sample YAML configs (in target folder) ✓
- DataStage materials (not originally in scope, added by Malika's email)

They did NOT provide:
- Cognos report XML
- Target Databricks schema (for either source or target tables beyond the two OUTPUT tables)

**Without the Databricks schema, neither demo track produces working output.**

