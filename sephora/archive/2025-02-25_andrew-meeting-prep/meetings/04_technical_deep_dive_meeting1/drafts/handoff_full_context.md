# Full Context Handoff: Sephora Demo Scoping

This document provides complete context for another Claude session working on the email response to Malika. Read the entire thing before making changes to the email.

---

## Background: What Happened

### Meeting 4 (Wednesday, March 2026)

BayOne had a technical deep dive call with Sephora. The attendees included Colin (BayOne), Malika, Sergey, Gariashi, and others from Sephora.

**What was agreed on the call:**
- The demo would focus on Cognos lift-and-shift with agent-based orchestration and MCP integration
- This was NOT just SQL conversion (Malika explicitly said code conversion alone isn't valuable because they do that internally)
- The value proposition was agent orchestration across systems, automating what is currently a manual multi-step process
- DataStage/ETL was mentioned towards the end of the meeting as an additional interesting area, but it was secondary to Cognos

**What Sephora said they would provide:**
- Cognos report XML from the Finance folder (Gariashi said Vlad would pull it)
- Target Databricks schema (Sergey was point person)
- Sample YAML config showing their existing framework

**What Sergey specifically said about ETL output:**
- "Our goal is to migrate DataStage jobs to existing framework"
- "You don't need to do Python development or something. You just need to do configuration"
- "No need to write Scala code at all... just create config file"
- "How to teach these agents to understand that we need to create three YAML files with some configuration inside"

This is important: Sergey explicitly said the output should be YAML configuration files for their existing AggregationApplication framework, not new Scala code.

### Malika's Email (March 6, 2026)

After the call, Malika sent a follow-up email that shifted the scope:

**What her email said:**
- Elevated ETL/DataStage from secondary to primary interest
- Asked for "Spark SQL / Scala" output along with deployment artifacts (contradicting what Sergey said on the call about YAML configs)
- Still mentioned Cognos MCP but provided zero Cognos materials
- Attached an ETL_use_case folder with DataStage files only

**What she attached:**
- 3 DataStage XML files (job definitions for inventory, purchase order, punch daily)
- 3 DDL files (SQL Server table definitions)
- 2 stored procedures (usp_Update_Inv_Periodic, usp_Populate_Stock_Continuity)
- 2 views (INVENTORY_PERIODIC, INVENTORY_PERIODIC_WEEKLY)
- 2 target Scala apps (examples of their AggregationApplication framework)
- 4 target YAML configs (showing their configuration and deployment structure)
- 2 target Hive DDL files (create.hql showing target table structure)

**What she did NOT attach:**
- Any Cognos report XML
- Any target Databricks schema
- Databricks source table schemas (the tables their Scala apps read from)

---

## The Two Tracks

### Track A: Cognos MCP Demo

**What it is:**
An MCP connector for Cognos that extracts report metadata and SQL programmatically, with agent-based conversion from Cognos/SQL Server to Databricks-compatible output, remapped to their target schema.

**The agents involved:**
- Cognos Extractor: Parse report XML and extract embedded queries
- Report Interpreter: Analyze SQL structure, joins, and calculations
- SQL Translator: Convert SQL Server syntax to Databricks SQL
- Schema Mapper: Remap table references to target schema
- Output Generator: Produce validated Databricks SQL
- Pipeline Orchestrator: Coordinates handoffs, validates outputs, manages sequence

**What we need from Sephora:**
- Cognos report XML (from Finance folder)
- Target Databricks schema (what the report should point to after migration)

**THE MCP CAVEAT:**

This is critical. We researched whether we could spin up our own Cognos environment to demonstrate live MCP connectivity. The answer is no.

- Cognos is a proprietary IBM product
- There is no freely available Docker image
- Community Docker setups require IBM licensed products from Passport Advantage (paywall)
- Free trial options are cloud-hosted, not self-hosted
- We cannot spin up a Cognos server without their environment access

**What this means for the demo:**

We CAN build the MCP connector. We CANNOT demonstrate or test it without access to their Cognos environment.

For the demo, we would work with exported Cognos report XML that they provide. The agents would parse and convert that XML. The MCP connector architecture can be shown and explained, but it cannot be executed live.

If Sephora wants to see MCP working in the demo, they would need to provide API/SDK level access to their Cognos environment. Based on the call discussion, their security posture may not allow this.

**How to frame this:**
- We can build the MCP connector
- Live demonstration requires environment access from Sephora
- Without that access, we demonstrate the workflow using exported XML
- In production, the MCP connector would replace manual XML exports

This is not a limitation on our side. It's a constraint of the technology. We're putting the ball in their court: if they want live MCP, they provide access. If not, we work with exported XML.

### Track B: ETL/DataStage Demo

**What it is:**
Parsing DataStage job XML, interpreting SQL Server stored procedures and views, and generating output that works with their existing Databricks framework.

**The agents involved:**
- DataStage Parser: Extract job structure, embedded SQL, and transformations
- SQL Interpreter: Analyze stored procedures, views, and business logic
- Pattern Mapper: Map legacy patterns to Databricks framework
- Config Generator: Produce YAML configuration files
- Schema Validator: Verify output compatibility
- Pipeline Orchestrator: Coordinates handoffs, validates outputs, manages sequence

**What we already have:**
- DataStage XML files (3 job definitions)
- DDL files (3 SQL Server table definitions)
- Stored procedures (2 files)
- Views (2 files)
- Target Scala apps (2 examples showing AggregationApplication framework)
- Target YAML configs (4 files)
- Target Hive DDL (2 files)

**What we still need:**
- Databricks source table schemas (column definitions for tables like edwlib_whintr, smt_location, smt_product, retfl030_skuloc)

We have the legacy SQL Server DDL, but their Scala applications read from Databricks source tables. To generate accurate output, we need to know what those source tables look like in their Databricks environment.

**THE OUTPUT FORMAT DISCREPANCY:**

There is a conflict between what was said on the call and what Malika wrote in her email:

- **Sergey (on the call):** YAML configuration files that work with their existing AggregationApplication framework. Not new Scala code. Just config files.
- **Malika (in her email):** "Spark SQL / Scala" along with deployment artifacts.

These are fundamentally different deliverables. YAML configs means we're generating configuration files that plug into their existing framework. Scala code means we're writing new application code.

The email needs to ask them to clarify which output format is correct.

---

## What We Built

We created detailed scoping documents for both tracks:

**Track A: track_a_cognos_mcp_demo.html**
- Full breakdown of the demo approach
- Section on MCP Connectivity Requirements explaining what happens with vs without environment access
- Agent orchestration diagram showing Pipeline Orchestrator above the agents
- Prerequisites table listing what we need
- Success criteria
- Scope (in/out)

**Track B: track_b_etl_datastage_demo.html**
- Full breakdown of the demo approach
- Section on Source Schema Requirements
- Agent orchestration diagram
- Table of materials we already have
- Prerequisites table listing what we still need
- Confirmation box explicitly calling out the Sergey vs Malika output format discrepancy
- Success criteria
- Scope (in/out)

Both documents use professional formatting with the BayOne design system. Both have the agentic workflow diagram showing the Pipeline Orchestrator at the top coordinating the agents below.

---

## What the Email Needs to Do

1. **Acknowledge the scope shift:** The call focused on Cognos, but Malika's email and attachments lean towards ETL. That's fine, but we need to pick one for the demo.

2. **Explain that both tracks use the same underlying architecture:** This is extensions of the same system, not two separate implementations.

3. **Be clear that covering both would be paid engagement territory:** The demo shows capability on one track. If they want both, that's a scope discussion.

4. **For Track A, include the MCP caveat:** We can build it, we cannot demonstrate it without their environment access. Frame it as putting the ball in their court.

5. **For Track B, ask about the output format:** Sergey said YAML, Malika said Scala. Which is it?

6. **Note that both scoping documents are attached:** They can read the full details for each track. The email is the summary, the scoping docs are the substance.

7. **Ask which track matters most for their evaluation:** Once they pick, we build it out.

---

## Key Files

All in `claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/`:

- `scoping/track_a_cognos_mcp_demo.html` - Track A scoping doc (attach to email)
- `scoping/track_b_etl_datastage_demo.html` - Track B scoping doc (attach to email)
- `scoping/track_a_cognos_mcp_demo.md` - Track A markdown version
- `scoping/track_b_etl_datastage_demo.md` - Track B markdown version
- `research/05_etl_use_case_analysis.md` - Inventory of what Malika attached
- `research/06_malika_email_breakdown.md` - Analysis of her email
- `research/07_demo_feasibility_analysis.md` - What we have vs what's missing

---

## Summary

The original call agreed on Cognos with MCP. Malika's email shifted towards ETL. Both are viable but we pick one for the demo. Track A has an MCP constraint (can build, can't demo without their environment). Track B has an output format question (YAML vs Scala). Both scoping docs are attached to the email. They pick a track, we build it.
