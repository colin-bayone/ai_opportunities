# Draft Response to Malika's Email - v3

**To:** Malika Seth, Sephora Team
**From:** Colin / BayOne
**Subject:** RE: Demo Scope Clarification

---

Hi Malika,

Thank you for the detailed follow-up. Before we begin demo preparation, I want to make sure we're fully aligned on scope.

**What was agreed on Wednesday's call:**

The demo would focus on Cognos lift-and-shift: an MCP connector that extracts report metadata and SQL from Cognos programmatically, with agent-based orchestration handling the conversion to Databricks-compatible output and remapping to your target schema. This was always about the agentic workflow and MCP integration, not just SQL conversion. DataStage was discussed as an optional add-on if time allowed.

To support this, your team mentioned providing:
- A Cognos report XML from the Finance folder (Gariashi mentioned Vlad could help)
- Target Databricks schema (catalog and table structure)
- A sample YAML config from your existing framework (Sergey)

**What your email now describes:**

Your email shifts the emphasis to the ETL migration use case and asks us to demonstrate agent orchestration across DataStage, stored procedures, and views. You've attached DataStage materials to support this track. You've also clarified that code translation alone isn't the focus since your team handles that internally, which aligns with our understanding: the demo was always about orchestration, not isolated conversion.

**Clarification needed:**

These are two separate tracks that share architectural patterns but require distinct implementation work:

**Track A: Cognos MCP Demo** (original scope)
- What we have: Nothing yet
- What we would need: Cognos report XML, target Databricks schema

**Track B: ETL/DataStage Demo** (newly emphasized)
- What we have: DataStage XML files, stored procedures, views, and examples of your target Scala/YAML framework
- What we would still need: Databricks source table schemas (the tables your Scala apps read from, such as edwlib_whintr, smt_location, smt_product, etc.). We have the legacy SQL Server DDL, but to generate accurate Databricks code, we'd need to know what those source tables look like in your Databricks environment.

For the demo, we'd want to focus on one track to ensure we deliver something valuable rather than spreading thin across both. Could you confirm which track you'd like us to prioritize? Once we know, I'll put together a scoping document with exactly what you can expect.

Looking forward to your thoughts.

Best,
Colin

