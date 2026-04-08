# Track A: Cognos MCP Demo

**Prepared for:** Sephora
**Date:** March 2026

---

## Overview

This demo will demonstrate agent-based orchestration for Cognos report migration. The focus is not on code conversion alone, but on how agents coordinate across systems to automate the end-to-end migration workflow.

---

## Demo Approach

### Working with Exported XML

For this demo, we will work with an exported Cognos report XML that you provide. The agents will:

1. Parse the report definition and extract embedded SQL
2. Interpret the report structure, data sources, joins, and calculations
3. Convert SQL Server syntax to Databricks-compatible SQL
4. Remap table references to your target Databricks schema
5. Generate output ready for validation

This approach aligns with what was discussed on the call: you provide the report XML, we produce converted output, and your team validates by pointing it to Databricks.

### About MCP Connectivity

We can build the MCP connector for Cognos, but demonstrating live MCP connectivity requires access to a running Cognos environment. Since Cognos is a proprietary IBM product with no freely available Docker image or trial server we can spin up, we cannot test or demonstrate the MCP connector without environment access.

**If you would like to see MCP working in the demo:**
- We would need access to your Cognos environment (API/SDK level)
- Based on the call discussion, this may not be feasible given security constraints

**Without environment access:**
- We demonstrate the agent orchestration and conversion workflow using exported XML
- The MCP connector architecture can be shown and explained, but not executed live
- In production, the MCP connector would replace the manual XML export step

---

## What We Would Deliver

### Agent Orchestration
- Multiple specialized agents working together:
  - **Cognos Extractor** - Pulls report definition from Cognos or provided XML
  - **Report Interpreter** - Interprets report structure, embedded SQL, and business logic
  - **SQL Translator** - Translates SQL Server syntax to Databricks-compatible SQL
  - **Schema Mapper** - Maps source tables to target Databricks schema
  - **Output Generator** - Produces final Databricks-compatible output
- **Pipeline Orchestrator** coordinating handoffs between agents
- Visible task sequencing and dependency handling

### End-to-End Workflow
```
Cognos Report → MCP Extraction → Parse Structure → Interpret SQL →
Convert Syntax → Remap to Target Schema → Generate Output → Validation
```

### MCP Connector for Cognos (Architecture)
- Programmatic connection to Cognos via SDK (Java/.NET)
- Automated extraction of report metadata and SQL from Cognos Content Store
- Would eliminate manual XML exports from Report Studio in production
- Can be built and demonstrated if environment access is provided

### Output
- Databricks-compatible SQL queries
- Remapped to your target catalog and table structure
- Ready for validation against original report

---

## What We Need From You

| Item | Description | Who |
|------|-------------|-----|
| Cognos report XML | Full export from Report Studio | Gariashi |
| Target Databricks schema | Catalog and table structure for remapping (what the Cognos report should point to after migration) | Sergey |

**Optional (for live MCP demonstration):**

| Item | Description |
|------|-------------|
| Cognos environment access | API/SDK access to demonstrate live MCP connectivity |

---

## Demo Workflow

1. **Input** - Exported Cognos report XML (provided by your team)
2. **Report Interpreter** - Dissects the report structure, identifies embedded SQL, data sources, joins, calculations
3. **SQL Translator** - Transforms SQL Server syntax to Databricks SQL (handling differences like identity columns, T-SQL functions, etc.)
4. **Schema Mapper** - Maps old table references to new Databricks schema
5. **Pipeline Orchestrator** - Coordinates handoffs, manages task sequencing, handles dependencies
6. **Output** - Databricks-compatible report definition ready for validation

Throughout: You'll see agents communicating, handing off work, and the orchestration layer managing the flow.

---

## Success Criteria

The demo will be considered successful if:

1. Agents successfully parse and interpret the Cognos report XML
2. Agent orchestration is visible - you can see agents handing off tasks, coordinating, and sequencing work
3. SQL conversion handles syntax differences between SQL Server and Databricks correctly
4. Output is remapped to your target Databricks schema
5. The workflow demonstrates automation of what is currently a manual, multi-step process

---

## Scope

**In Scope:**
- Single Cognos report conversion
- Multi-agent orchestration demonstration
- SQL Server to Databricks SQL conversion
- Schema remapping to target Databricks environment
- Databricks-compatible output generation
- MCP connector architecture (demonstration requires environment access)

**Out of Scope:**
- Multiple reports
- DataStage/ETL conversion
- Framework Manager model migration
- Content Store migration
- Production deployment
- Validation against live Databricks (unless access provided)
- Ongoing maintenance

---

## What This Demonstrates

This demo shows our capability to build system integrations that automate legacy report migration through agent orchestration.

The key differentiator is not code conversion, but how agents coordinate across multiple tools (Cognos, SQL parsing, Databricks) to automate the entire workflow without manual intervention at each step.

The MCP connector and agent orchestration patterns established here would extend to additional reports and use cases in a paid engagement. With environment access, the MCP connector would complete the automation by eliminating manual XML exports entirely.

