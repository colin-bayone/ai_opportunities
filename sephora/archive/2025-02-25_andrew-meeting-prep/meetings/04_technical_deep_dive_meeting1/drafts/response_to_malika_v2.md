# Draft Response to Malika's Email - v2

**To:** Malika Seth, Sephora Team
**From:** Colin / BayOne
**Subject:** RE: Demo Scope Clarification

---

Hi Malika,

Thank you for the detailed follow-up. I want to make sure we're aligned on scope before we proceed with demo preparation.

From our call on Wednesday, the agreed demo scope was:
- MCP connector for Cognos that extracts report metadata and SQL programmatically
- Agent-based conversion with orchestration from Cognos/SQL Server to Databricks-compatible output
- If time allowed, DataStage job conversion generating YAML configs for your existing Databricks framework

Your email adds clarity on a few points. First, that code translation on its own is not the focus since your team is already doing that internally. That aligns with what we discussed: the demo was always about the MCP integration and agent orchestration, not just the conversion output. Second, you've elevated the ETL migration use case from optional to explicitly requested, which works well since you've attached the DataStage materials we'd need.

One thing I want to flag: the Cognos MCP demo and automated Cognos extraction require either environment access or a Cognos report XML to work with. The materials attached are DataStage/ETL only. From our call, Gariashi mentioned working with Vlad to pull a Finance report XML, and Sergey was going to share a sample YAML config from your Databricks framework. We haven't received those yet.

So as it stands, the demo would focus on the ETL migration track you've now prioritized:
- Parsing DataStage job XML and extracting transformation logic
- Interpreting SQL Server stored procedures and views
- Agent orchestration across the parsing, interpretation, and generation steps
- Generating Databricks-compatible output matching your YAML config and Scala framework

If you'd like the demo to also include the Cognos MCP track, we'd still need that Finance report XML and the target Databricks schema info.

Please confirm this aligns with where you want us to focus. Once confirmed, I'll share a scoping document within the next couple of days with everything you can expect in the demo.

Best,
Colin

