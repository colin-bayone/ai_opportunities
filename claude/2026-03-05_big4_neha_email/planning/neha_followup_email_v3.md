# Neha Follow-Up Email v3

---

Really enjoyed today's call. It was great finally getting into the weeds with the full team. Andrew, that walkthrough of the Framework Model vs Freehand SQL workflow was exactly what we needed, and Sergei, your point about generating YAML configs instead of code clicked everything into place for us.

So here's what we're going to build for the demo:
• A Cognos connector that grabs report metadata and SQL directly from the system, so no more manual XML exports from Report Studio
• SQL translation that takes your SQL Server queries and converts them to Databricks
• If we have time, a DataStage conversion that spits out YAML configs the way Sergei described, ready to commit to your repo

To make this happen, we just need a few things:
1. A Cognos report XML from Finance (Gariashi, you mentioned Vlad could help with this one)
2. The target Databricks schema (catalog and table structure) so we can wire up the remapping
3. One of your existing YAML configs so we match your format (Sergei, you'd be the one for this)
4. If it's easy to grab, a DataStage job we can use as a test case (Maher, you mentioned having one)

No pressure on timing, but the sooner we get these, the sooner we can get the demo on the calendar and show you what this actually looks like with your own stuff.

If anything's unclear about what to pull, just let me know. Happy to hop on a quick call.

Best,
Neha
