# ETL_use_case Folder Analysis

**Created:** March 9, 2026
**Purpose:** Document what Sephora provided vs. what was discussed in Meeting 4 and requested in Malika's email

---

## File Inventory (19 files total)

### Legacy Source Materials (10 files)
- 3 DDL files (SQL Server table definitions)
- 2 Stored procedures
- 2 Views
- 3 DataStage XML job definitions
- 1 Documentation file (.docx)

### Target Materials (8 files)
- 2 Scala applications
- 2 Hive DDL files (create.hql)
- 4 YAML config files (aggregation + deployment)

---

## Wave 1: DDL Files (SQL Server Table Definitions)

### DDL_INVENTORY_PERIODIC_DAILY_GT_042015.txt
- **Database:** Sephora_EDW
- **Table:** INVENTORY_PERIODIC_DAILY_GT_042015
- **Columns:** 35 columns
- **Primary Key:** Date_SK, Location_SK, Product_SK (composite)
- **Key Fields:** Inventory metrics (ending/beginning costs, units, retail), flags (Active_Store_Flag, Store_With_Inv_Flag, Store_With_Sales_Flag), behavior codes
- **Data Types:** Mix of int, decimal (various precisions), char, datetime
- **Key Observation:** Uses surrogate keys (Date_SK, Location_SK, Product_SK) not business keys

### DDL_INVENTORY_PERIODIC_WEEKLY_GT_042015.txt
- **Database:** Sephora_EDW
- **Table:** INVENTORY_PERIODIC_WEEKLY_GT_042015
- **Columns:** 33 columns (fewer than daily - missing SKU_Behavior_Code, DC_SKU_Behavior_Code, E3_Source_Code)
- **Primary Key:** Same composite key
- **Structure:** Weekly aggregation of daily inventory data

### DDL_STOCK_CONTINUITY_ALL_SKU.txt
- **Database:** Sephora_EDW
- **Table:** STOCK_CONTINUITY_ALL_SKU
- **Columns:** 12 columns (simpler than inventory tables)
- **Primary Key:** Same Date_SK, Location_SK, Product_SK pattern
- **Purpose:** Track SKU availability and status flags

---

## Wave 2: Stored Procedures

### SP_usp_Update_Inv_Periodic.txt (~304 lines)
- **Purpose:** Update inventory flag calculations for Daily, Weekly, and Monthly tables
- **Business Logic:**
  - Calculates `Active_Store_Flag`, `Store_With_Inv_Flag`, `Store_With_Sales_Flag`
  - Flag logic based on Available_Sales_Units thresholds (>=2 for most, >=1 for SKU_Behavior_Code '9')
  - Special handling for dotcom locations (Is_Dotcom='Y')
  - Joins with: DATE, mini_raq2, VW_ACTIVE_STORE_PRODUCT_LOCATION, SALES_TY, Location_DC
  - Propagates daily flags to weekly/monthly tables
- **Complexity:** High - multiple temp tables, conditional updates, cross-table propagation
- **Dependencies:** References tables not in the provided materials (SALES_TY, mini_raq2, VW_ACTIVE_STORE_PRODUCT_LOCATION)

### SP_usp_Populate_Stock_Continuity.txt (~96 lines)
- **Purpose:** Populate STOCK_CONTINUITY table from INVENTORY_PERIODIC
- **Business Logic:**
  - Filters active inventory (Active_Store_Flag = 1)
  - Joins LOCATION_PRODUCT, LOCATION, PRODUCT, INVENTORY_PERIODIC
  - Buyer_Class IN ('R', 'W'), Status_Flag = 'A', Department < 60, SKU_Type = '1'
  - Handles 21-day start date delay
  - Sunday data goes to STOCK_CONTINUITY_WEEKLY
  - Calls additional procedures: usp_Populate_Stock_Continuity_All_SKU, etc.
- **Complexity:** Medium - straightforward ETL pattern
- **Dependencies:** References tables not provided (LOCATION_PRODUCT, LOCATION, PRODUCT)

---

## Wave 3: Views

### view_INVENTORY_PERIODIC.txt
- **Purpose:** Daily inventory view joining with location-product mappings
- **Base Table:** INVENTORY_PERIODIC_DAILY (with NOLOCK hint)
- **Joins:** LEFT OUTER JOIN to VW_LOC_PROD for SKU behavior codes
- **Output:** 28 columns including computed LOC_PROD_SK (concatenated key)
- **Note:** Comment shows it was previously using INVENTORY_PERIODIC_DAILY_GT_042015

### view_INVENTORY_PERIODIC_WEEKLY.txt
- **Purpose:** Simple passthrough view over weekly table
- **Base Table:** INVENTORY_PERIODIC_WEEKLY_GT_042015
- **Joins:** None - simple SELECT from underlying table
- **Output:** 30 columns (all from base table)

---

## Wave 4: DataStage XML Job Definitions

### DS_Jobs_inventory.xml (39 KB)
- **Contains:** 2 jobs in one file
  1. `lod_F_Inventory_Periodic_Daily_opt_poc` - Daily inventory load
  2. `lod_F_Inventory_Periodic_Weekly_opt` - Weekly inventory load
- **Tool:** IBM InfoSphere DataStage 11.7
- **Category:** \Jobs\EDW\Sephora_EDW\Fact_Tables
- **Parameters:** $EDW_TARGET, $EDW_USERNAME, $EDW_PASSWORD, pDate
- **Structure:** ODBC stage → Transformer stage → Output
- **Embedded SQL:** ~125 lines of complex INSERT/UPDATE including:
  - Truncate and insert into STG_INVENTORY_PERIODIC_DAILY
  - Multiple JOINs across replication tables (SKULOC, WHINTR, WHDET, etc.)
  - Dotcom location handling (dual inventory logic)
  - Begin inventory from previous day
  - SKU behavior code updates
  - Calls stored procs: usp_Update_Inv_Periodic, usp_Populate_Stock_Continuity
- **This is the key job for the demo** - shows full ETL flow

### DS_Jobs_lod_F_Purchase_Order.xml (565 KB - large)
- **Job:** `lod_F_Purchase_Order`
- **Category:** \Jobs\EDW\Sephora_EDW\Fact_Tables
- **Parameters:** $EDW_SERVER, $EDW_REPLICATION_MERCH, $EDW_TARGET, etc.
- **Stages:** DRSConnector (source), Transformer, HashFile lookups, ODBCConnector (target)
- **Purpose:** Load purchase order facts with dimension lookups
- **Complexity:** Multiple lookup stages for Product, Location, Buyer, Vendor, etc.

### DS_Jobs_sqr_DF_Punch_Daily.xml (1.4 MB - very large)
- **Job:** `jbp_DF_Punch_report`
- **Description:** Load Punch data from DF (DayForce)
- **Author:** Sergey Shtypuliak (multiple versions 2020-2022)
- **Category:** \Jobs\EDW\DF
- **Complexity:** Extremely complex - 45+ stages including:
  - REST API calls (XMLStagePX)
  - Multiple transformers, aggregators, funnels
  - Lookups for location, HR, CEL activity
  - Pagination handling (Page1, Page2, etc.)
- **Note:** This is NOT inventory-related - it's workforce management/timekeeping

---

## Wave 5: Target Scala Applications

### InventoryPeriodicDailyAggApplication.scala (397 lines)
- **Package:** com.sephora.dataplatform.aggregation
- **Extends:** AggregationApplication framework
- **Complexity:** HIGH - multi-stage aggregation with complex joins
- **Key Operations:**
  - Joins 11 source datasets (edwlib_whintr, retfl030_skuloc, retfl030_whctl, etc.)
  - Calculates Available_Sales_Units, Ending_Inventory metrics
  - Handles dotcom dual-inventory logic
  - Updates begin inventory from previous day
  - Propagates flags to weekly/monthly
- **Output:** Delta table partitioned by Business_Date

### StockContinuityAllSkuApplication.scala (111 lines)
- **Package:** com.sephora.dataplatform.aggregation
- **Extends:** AggregationApplication framework
- **Complexity:** MEDIUM - straightforward join pattern
- **Key Operations:**
  - Filters inventory_periodic_daily for Active_Store_Flag=1
  - Joins with e3_raq, smt_location, smt_product, location_dc
  - US dotcom mapping logic
  - Filters by Buyer_Class, Territory_Status, Department, SKU_Type
- **Output:** Delta table partitioned by Processing_Date

---

## Wave 6: Target YAML Configuration Files

### inventory-periodic-daily-with-flags-agg.yaml
- **Job Name:** inventory_periodic_daily_wf_job_name (parameterized)
- **Source Files:** 11 datasets from various paths (mcs_db, hdp_db, analytics_db, sdpdb_db)
- **Output:** Delta format to analytics_db_dbfs_path/inventory_periodic_daily
- **Mode:** incremental-partition-overwrite by Business_Date

### inventory-periodic-daily-with-flags-agg.deployment.yaml
- **Cluster:** Standard_DS3_v2, 1 worker, autotermination 10 min
- **Spark Version:** Parameterized (analytics_spark_version)
- **Init Scripts:** external-metastore.sh, set_spark_params.sh, setup_log4j.sh
- **Key Config:** Delta preview enabled, broadcast join disabled, hive metastore integration

### stock-continuity-all-sku-agg.yaml
- **Source Files:** 5 datasets (inventory_periodic_daily, e3_raq, smt_location, smt_product, location_dc)
- **Output:** Delta format to golden_book_analytics_db_dbfs_path/stock_continuity_all_sku
- **Mode:** incremental-partition-overwrite by Processing_Date

### stock-continuity-all-sku-agg.deployment.yaml
- **Identical cluster config** to inventory daily deployment
- **Same init scripts and Spark configuration**

---

## Wave 7: Target Hive DDL (create.hql files)

### inventory_periodic_daily/create.hql
- Creates Delta table with 32 columns
- Key columns: Business_Date (partition), Location_Number, Sku_Number
- Inventory metrics, flags, behavior codes
- Uses parameterized ${db}, ${table}, ${format}, ${path}

### stock_continuity_all_sku/create.hql
- Creates Delta table with 10 columns
- Key columns: Processing_Date (partition), Location_Number, Sku_Number
- Simpler structure than inventory tables

---

# CRITICAL ANALYSIS

## What Was Discussed in Meeting 4 vs. What Email Requested

| Topic | Meeting 4 (Sergey's Input) | Malika's Email |
|-------|---------------------------|----------------|
| **Demo Focus** | Cognos lift-and-shift | MCP server for Cognos + ETL migration |
| **Output Format** | "YAML configs, not code" | "Spark SQL / Scala" + deployment artifacts |
| **Code Translation** | Not discussed as primary | "Would NOT be primary" - they do this internally |
| **What They Want to See** | Agent parsing + conversion | Automated extraction, orchestration, end-to-end |

## Is What They Provided Sufficient?

### FOR ETL DEMO: YES (mostly)
- ✅ Complete source-to-target mapping example
- ✅ DataStage XML with embedded SQL
- ✅ Target Scala applications showing Databricks output
- ✅ YAML configs showing their framework pattern
- ✅ Hive DDL for target schema
- ⚠️ Missing: Some referenced tables not included (SALES_TY, mini_raq2, etc.)

### FOR COGNOS DEMO: **NO - NOTHING PROVIDED**
- ❌ No Cognos report XML
- ❌ No Framework Manager model
- ❌ No target Databricks schema for remapping
- The email mentions Cognos but provided only ETL materials

## Key Gap: COGNOS MATERIALS STILL NEEDED

They said in Meeting 4 they'd provide:
1. Cognos report XML from Finance folder
2. Target Databricks schema

**They have NOT provided these.** The ETL_use_case folder is DataStage/inventory only.

## What's Different From Meeting 4

1. **Scope Expanded:** Email adds ETL migration explicitly (we were treating it as optional)
2. **Value Prop Shifted:** They already do code translation internally, want orchestration/automation
3. **New Person:** Malika Seth wrote the email - wasn't in Meeting 4
4. **Output Confusion:** Sergey said YAML, email says Spark SQL/Scala (their target shows BOTH)

## Recommendation for Response

Ask for:
1. **The Cognos report XML** - still the primary demo deliverable
2. **Target Databricks schema** - needed for remapping
3. **Clarification on output format** - YAML configs (Sergey) vs Spark SQL/Scala (email)?

Tell them:
- ETL materials look sufficient for a DataStage conversion demo
- We can show both YAML config generation AND the Scala code pattern
- Still need Cognos materials for the primary demo track

