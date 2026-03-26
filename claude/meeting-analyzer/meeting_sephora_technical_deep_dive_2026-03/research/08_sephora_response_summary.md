# Sephora Response Summary (Email 3)

**Date:** March 2026
**From:** Malika

---

## Key Decisions

### 1. Track Selected: Track B (ETL/DataStage Demo)

They chose Track B. Cognos is off the table for the demo.

### 2. Output Format Clarified

This is important. The output needs BOTH components:

- **Spark SQL transformations:** Core transformation logic lives here
- **YAML configuration and deployment artifacts:** Pipeline config and deployment setup

Their framework architecture:
- Business logic sits in the Spark SQL layer
- Pipeline configuration and deployment managed through YAML files
- Both pieces are required for a migrated pipeline to be executable

This resolves the Sergey vs Malika discrepancy. It was not either/or. It was both.

### 3. Missing Materials Provided

They sent the Databricks source table schemas we asked for:
- `edwlib_whintr.txt` - Warehouse inventory transactions (19 columns)
- `retfl030_skuloc.txt` - SKU location data (19 columns)
- `smt_location.xlsx` - Location master data (47 columns)
- `smt_product.xlsx` - Product master data (151 columns)

These are in: `sephora/context/ETL_use_case/ETL_use_case/new/`

---

## What We Have Now

### Original Materials (from Malika's first email)
- 3 DataStage XML job definitions
- 3 DDL files (SQL Server table definitions)
- 2 stored procedures
- 2 views
- ETL Migration Use Cases description document

### Target Examples (what the output should look like)
- 2 Scala applications (InventoryPeriodicDailyAggApplication, StockContinuityAllSkuApplication)
- 4 YAML config files (2 job configs, 2 deployment configs)
- 2 HQL create scripts

### New Materials (from this email)
- 4 Databricks source table schemas

---

## What This Means for the Demo

We have everything we need:

1. **Source:** DataStage XML, stored procedures, views showing the legacy ETL logic
2. **Target pattern:** Scala apps and YAML configs showing exactly what output should look like
3. **Schema context:** Databricks source table schemas so we can generate accurate column references

The demo should produce:
- Spark SQL with the transformation logic (extracted from DataStage/stored procs)
- YAML configs that match their existing deployment pattern

---

## Next Steps

1. Confirm we have what we need (we do)
2. Build the demo for Track B
3. Respond to Malika confirming we're moving forward

---

## Full Email Thread

Colin's email asked them to:
- Choose a track (they chose B)
- Clarify YAML vs Scala (they said both)
- Provide Databricks schemas (they did)

All questions answered. All materials provided. Ready to build.
