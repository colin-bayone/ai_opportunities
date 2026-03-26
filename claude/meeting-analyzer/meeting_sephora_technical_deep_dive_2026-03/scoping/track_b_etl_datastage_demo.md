# Track B: ETL/DataStage Demo

**Prepared for:** Sephora
**Date:** March 2026

---

## Overview

This demo will demonstrate agent-based orchestration for ETL migration, including parsing DataStage job XML, interpreting SQL Server stored procedures and views, and generating YAML configuration files that work with your existing Databricks framework.

---

## Demo Approach

### Working with Provided Materials

For this demo, we will work with the DataStage XML files, stored procedures, views, and target framework examples you have provided. The agents will:

1. Parse DataStage job definitions and extract embedded SQL
2. Interpret stored procedure logic and business rules
3. Map transformation patterns to your existing Databricks framework
4. Generate YAML configuration files matching your deployment structure
5. Produce output ready for validation against your existing pipelines

Based on the call discussion, your team already has an AggregationApplication framework in Databricks. The agent output will be YAML configs that work with this existing framework, not new Scala code.

### About Source Table Schemas

We have the legacy SQL Server DDL, but your Scala applications read from Databricks source tables (edwlib_whintr, smt_location, smt_product, retfl030_skuloc, etc.). To generate accurate YAML configs, we need to know what these source tables look like in your Databricks environment.

**If you can provide Databricks source table schemas:**
- We generate YAML configs with correct column references and data types
- Output can be validated directly against your existing framework

**Without source table schemas:**
- We demonstrate the agent orchestration and parsing workflow
- YAML configs will reference the source tables by name, but column mappings may need adjustment

---

## What We Would Deliver

### Agent Orchestration
- Multiple specialized agents working together:
  - **DataStage Parser** - Extracts job structure, embedded SQL, and transformation logic from XML
  - **SQL Interpreter** - Analyzes stored procedures, views, and business logic
  - **Pattern Mapper** - Maps legacy transformation patterns to your Databricks framework
  - **Config Generator** - Produces YAML configuration files matching your deployment structure
  - **Schema Validator** - Verifies output compatibility with target environment
- **Pipeline Orchestrator** coordinating handoffs between agents
- Visible task sequencing and dependency handling

### End-to-End Workflow
```
DataStage XML → Parse Job Structure → Interpret SQL Logic →
Map to Framework Patterns → Generate YAML Configs → Validation
```

### Output
- YAML configuration files matching your existing framework pattern
- Deployment YAML files for cluster and Spark configuration
- Documentation of transformation logic extracted from source

---

## What We Have

| Material | Description |
|----------|-------------|
| DataStage XML files | 3 job definitions (inventory, purchase order, punch daily) |
| DDL files | 3 SQL Server table definitions |
| Stored procedures | 2 files (usp_Update_Inv_Periodic, usp_Populate_Stock_Continuity) |
| Views | 2 files (INVENTORY_PERIODIC, INVENTORY_PERIODIC_WEEKLY) |
| Target Scala apps | 2 examples showing your AggregationApplication framework pattern |
| Target YAML configs | 4 files showing your configuration and deployment structure |
| Target Hive DDL | 2 create.hql files showing target table structure |

---

## What We Need From You

| Item | Description | Why It's Needed |
|------|-------------|-----------------|
| Databricks source table schemas | Column definitions for tables like edwlib_whintr, smt_location, smt_product, retfl030_skuloc, etc. | Your Scala apps read from these tables. We have the legacy SQL Server DDL, but to generate accurate YAML configs, we need to know what these source tables look like in your Databricks environment. |

**Please Confirm - Output Format:**

We received different guidance on the expected output format:

- **Sergey (call):** YAML configuration files that work with your existing AggregationApplication framework, not new Scala code
- **Malika (email):** "Spark SQL / Scala" along with deployment artifacts

Please confirm which output format is correct for the demo.

---

## Demo Workflow

1. **Input** - DataStage XML, stored procedures, views (provided in ETL_use_case folder)
2. **DataStage Parser** - Extracts job structure, embedded SQL, transformation stages
3. **SQL Interpreter** - Analyzes stored procedure logic, business rules, flag calculations
4. **Pattern Mapper** - Maps legacy patterns to your AggregationApplication framework
5. **Config Generator** - Produces YAML files matching your configuration structure
6. **Pipeline Orchestrator** - Coordinates handoffs, manages task sequencing, handles dependencies
7. **Output** - YAML configuration files ready for validation

Throughout: You'll see agents communicating, handing off work, and the orchestration layer managing the flow.

---

## Success Criteria

The demo will be considered successful if:

1. Agents successfully parse DataStage XML and extract embedded SQL and job structure
2. Stored procedure logic is interpreted and business rules are identified
3. Agent orchestration is visible across parsing, interpretation, and generation steps
4. Output YAML configs follow your existing framework pattern
5. The workflow demonstrates automation of what is currently a manual analysis process

---

## Scope

**In Scope:**
- Single DataStage job conversion (inventory pipeline)
- Associated stored procedure and view interpretation
- Agent orchestration demonstration
- YAML configuration file generation
- Framework pattern matching

**Out of Scope:**
- Multiple pipelines
- Cognos report conversion
- New Scala code generation (output is YAML configs for existing framework)
- Production deployment
- Ongoing maintenance

---

## What This Demonstrates

This demo shows our capability to automate legacy ETL migration using agent orchestration. The focus is on parsing complex DataStage jobs, interpreting SQL Server logic, and generating configuration files that work with your existing Databricks framework.

The key differentiator is not code generation, but how agents coordinate to understand legacy ETL logic and produce output that integrates with your established patterns without introducing new frameworks.

The parsing and generation patterns established here would extend to additional pipelines and use cases in a paid engagement.

