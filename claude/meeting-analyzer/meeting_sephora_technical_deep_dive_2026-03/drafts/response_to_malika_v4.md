# Draft Response to Malika's Email - v4

**To:** Malika Seth, Sephora Team
**From:** Colin / BayOne
**Subject:** RE: Demo Scope Clarification

---

Hi Malika,

Thank you for the detailed follow-up. Before we begin demo preparation, I want to make sure we're fully aligned on scope.

From our call on Wednesday, the agreed demo scope was Cognos lift-and-shift: an MCP connector that extracts report metadata and SQL from Cognos programmatically, with agent-based orchestration handling the conversion to Databricks-compatible output and remapping to your target schema. This was always about the agentic workflow and MCP integration, not just SQL conversion. DataStage was discussed as an optional add-on if time allowed. Your team mentioned providing a Cognos report XML from the Finance folder, along with the target Databricks schema.

Your email introduces a different scope: ETL migration using DataStage, stored procedures, and views, with output in your Spark/Scala framework. You've attached DataStage materials to support this, which is helpful.

I want to be clear that these are two completely separate tracks. While they share some architectural patterns, they require distinct implementation work:

**Track A: Cognos MCP Demo**
What we'd need from you: Cognos report XML, target Databricks schema

**Track B: ETL/DataStage Demo**
What we have: DataStage XML, stored procedures, views, examples of your target Scala/YAML framework
What we'd still need: Databricks source table schemas (the tables your Scala apps read from, like edwlib_whintr, smt_location, smt_product). We have the legacy SQL Server DDL, but to generate accurate Databricks code, we need to know what those source tables look like in your Databricks environment.

Given this is a demo, we'd need to align on one of these two tracks. Covering both would extend into paid engagement territory. Could you let us know which track is most important to demonstrate our capabilities for your evaluation? Once confirmed, I'll share a scoping document with everything you can expect.

Looking forward to your thoughts.

Best,
Colin

