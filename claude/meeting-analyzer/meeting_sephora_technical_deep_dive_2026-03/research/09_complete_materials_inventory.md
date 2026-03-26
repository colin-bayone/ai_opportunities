# Complete Materials Inventory - Sephora ETL Migration

**Last Updated:** March 2026
**Status:** All materials received

---

## Location

All files in: `sephora/context/ETL_use_case/ETL_use_case/`

---

## 1. Source Materials (Legacy System)

### DataStage Job XML Files

| File | Size | Purpose |
|------|------|---------|
| DS_Jobs_inventory.xml | 39 KB | Daily inventory periodic load job |
| DS_Jobs_lod_F_Purchase_Order.xml | 565 KB | Purchase order load with lookups |
| DS_Jobs_sqr_DF_Punch_Daily.xml | 1.4 MB | Daily punch/timesheet data |

### SQL Server DDL Files

| File | Table | Columns |
|------|-------|---------|
| DDL_INVENTORY_PERIODIC_DAILY_GT_042015.txt | INVENTORY_PERIODIC_DAILY_GT_042015 | 36 |
| DDL_INVENTORY_PERIODIC_WEEKLY_GT_042015.txt | INVENTORY_PERIODIC_WEEKLY_GT_042015 | 32 |
| DDL_STOCK_CONTINUITY_ALL_SKU.txt | STOCK_CONTINUITY_ALL_SKU | 12 |

### Stored Procedures

| File | Procedure | Purpose |
|------|-----------|---------|
| SP_usp_Update_Inv_Periodic.txt | usp_Update_Inv_Periodic | Update inventory flags (daily/weekly/monthly) |
| SP_usp_Populate_Stock_Continuity.txt | usp_Populate_Stock_Continuity | Populate stock continuity snapshot |

### Views

| File | View | Source |
|------|------|--------|
| view_INVENTORY_PERIODIC.txt | INVENTORY_PERIODIC | INVENTORY_PERIODIC_DAILY with LOC_PROD join |
| view_INVENTORY_PERIODIC_WEEKLY.txt | INVENTORY_PERIODIC_WEEKLY | Weekly aggregation pass-through |

### Documentation

| File | Contents |
|------|----------|
| ETL Migration Use Cases_description.docx | Business context and use case descriptions |

---

## 2. Target Materials (Databricks Framework)

Location: `target/`

### Scala Applications

| File | Class | Sources | Output |
|------|-------|---------|--------|
| InventoryPeriodicDailyAggApplication.scala | InventoryPeriodicDailyAggApp | 11 source tables | 33+ column inventory snapshot |
| StockContinuityAllSkuApplication.scala | StockContinuityAllSkuApp | 5 source tables | 9 column stock continuity |

### YAML Configuration Files

| File | Purpose |
|------|---------|
| inventory_periodic_daily/inventory-periodic-daily-with-flags-agg.yaml | Job config (sources, output, partitioning) |
| inventory_periodic_daily/inventory-periodic-daily-with-flags-agg.deployment.yaml | Databricks deployment (cluster, secrets, notifications) |
| stock_continuity_all_sku/stock-continuity-all-sku-agg.yaml | Job config |
| stock_continuity_all_sku/stock-continuity-all-sku-agg.deployment.yaml | Deployment config |

### HQL Create Scripts

| File | Table | Format |
|------|-------|--------|
| inventory_periodic_daily/create.hql | inventory_periodic_daily | Delta, partitioned by Business_Date |
| stock_continuity_all_sku/create.hql | stock_continuity_all_sku | Delta, partitioned by Processing_Date |

---

## 3. Databricks Source Schemas (New)

Location: `new/`

| File | Table | Columns | Format |
|------|-------|---------|--------|
| edwlib_whintr.txt | edwlib_whintr | 19 | DDL (Parquet) |
| retfl030_skuloc.txt | retfl030_skuloc | 19 | DDL (Parquet) |
| smt_location.xlsx | smt_location | 47 | Excel schema export |
| smt_product.xlsx | smt_product | 151 | Excel schema export |

### Key Tables

**edwlib_whintr** - Warehouse inventory transactions
- Key columns: WZSKU (SKU), WZSTRE (store), WZPO (PO), quantities, costs, dates

**retfl030_skuloc** - SKU location inventory
- Key columns: SSSKU (SKU), SSSTRE (store), on-hand units, costs, damaged/lost

**smt_location** - Location master (47 columns)
- Hierarchical: region, district, store
- Includes addresses, managers, dates, E3 integration

**smt_product** - Product master (151 columns)
- Classification: class, subclass, department, brand
- Pricing: retail, cost, vendor pricing
- Attributes: 32 dynamic attribute columns

---

## 4. Data Relationships

```
Transaction Tables              Dimension Tables
─────────────────              ────────────────
edwlib_whintr.WZSKU    ───────► smt_product.sku_number
retfl030_skuloc.SSSKU  ───────► smt_product.sku_number

edwlib_whintr.WZSTRE   ───────► smt_location.location_number
retfl030_skuloc.SSSTRE ───────► smt_location.location_number
```

---

## 5. Output Requirements

Based on Malika's clarification, the demo must produce:

### Spark SQL Transformations
- Core business logic extracted from DataStage jobs and stored procedures
- Flag calculations (store_with_inv_flag, store_with_sales_flag, etc.)
- Joins across source tables
- Aggregations and groupings

### YAML Configuration Files
- Job configuration (sources, output paths, partitioning)
- Deployment configuration (cluster settings, secrets, notifications)
- Must match the pattern in the target examples

### Both Are Required
Their framework: business logic in Spark SQL, pipeline config in YAML. A migrated pipeline needs both to be executable.

---

## Summary

| Category | Count | Status |
|----------|-------|--------|
| DataStage XML jobs | 3 | Have |
| SQL Server DDL | 3 | Have |
| Stored procedures | 2 | Have |
| Views | 2 | Have |
| Target Scala apps | 2 | Have |
| Target YAML configs | 4 | Have |
| Target HQL scripts | 2 | Have |
| Databricks source schemas | 4 | Have (new) |

**All materials received. Ready to build the demo.**
