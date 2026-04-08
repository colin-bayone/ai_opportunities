# Draft Response to Malika's Email - v7

**To:** Malika Seth, Sephora Team
**From:** Colin / BayOne
**Subject:** RE: Demo Scope Clarification

---

Hi Malika,

Thank you for the detailed follow-up. Before we begin demo preparation, I want to make sure we're fully aligned on scope.

From our call on Wednesday, the agreed demo scope was Cognos lift-and-shift with agent-based orchestration and MCP integration, not just SQL conversion. DataStage was mentioned towards the end of the meeting as an additional interesting area, but wasn't the explicit focus. Your team mentioned providing a Cognos report XML from the Finance folder, along with the target Databricks schema.

It sounds like your team has been thinking more about this and is now leaning towards ETL migration as the primary use case. Thank you for attaching the DataStage materials.

Both tracks are extensions of the same underlying system and share the same architecture. For a demo, we'd need to pick one to build out and demonstrate the capability, as covering both would extend into paid engagement territory. If you'd like to move forward after seeing the capability, the scope of that engagement would be yours to define.

**Track A: Cognos MCP Demo**

What we would deliver:
- MCP connector for Cognos that extracts report metadata and SQL programmatically
- Agent-based conversion with orchestration from Cognos/SQL Server to Databricks-compatible output
- Remapping to your target schema

What we'd need from you:
- Cognos report XML
- Target Databricks schema

**Track B: ETL/DataStage Demo**

What we would deliver:
- Parsing DataStage job XML and extracting transformation logic
- Interpreting SQL Server stored procedures and views
- Agent orchestration across the parsing, interpretation, and generation steps
- Generating Databricks-compatible output matching your YAML config and Scala framework

What we have:
- DataStage XML files
- Stored procedures and views
- Examples of your target Scala/YAML framework

What we'd still need:
- Databricks source table schemas (the tables your Scala apps read from, like edwlib_whintr, smt_location, smt_product)
- We have the legacy SQL Server DDL, but to generate accurate Databricks code, we need to know what those source tables look like in your Databricks environment

One clarification on Track B: On the call, Sergey indicated the agent should generate YAML configuration files for your existing framework, not new Scala code. Your email mentions "Spark SQL / Scala" as the expected output. Could you confirm which is correct?

Could you let us know which track is most important to demonstrate our capabilities for your evaluation? Once confirmed, I'll share a scoping document with everything you can expect.

Looking forward to your thoughts.

Best,
Colin

