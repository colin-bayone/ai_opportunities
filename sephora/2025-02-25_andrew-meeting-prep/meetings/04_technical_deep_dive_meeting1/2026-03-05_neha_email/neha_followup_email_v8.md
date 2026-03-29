# Neha Follow-Up Email v8

---

Great discussion today! Really appreciate you and the team walking us through the full Cognos workflow. Understanding how reports use the Framework Model versus having embedded SQL, and hearing about the manual steps involved in extracting and converting everything, gives us exactly what we need to build a demo that's directly relevant to your environment.

To recap where we landed, we're going to build out a focused demo that covers:
• An MCP connector for Cognos that can extract report metadata and SQL programmatically, so no more manual XML downloads from Report Studio
• Agent-based conversion that handles the Framework Model mapping or embedded SQL translation, producing output that maps to your Databricks environment
• A validation approach where you can test the output on your end without us needing direct system access

To get started, we need two things from your side:
1. A Cognos report XML export from the Finance folder, the full export from Report Studio. Vlad can help coordinate pulling this.
2. The target Databricks schema, catalog and table structure, so we can wire up the mapping on our end.

No rush, but the sooner we have these, the sooner we can get the demo on the calendar. Happy to hop on a quick call if anything needs clarification on what exactly to export.

Looking forward to showing you what the agents can do with your actual report.

Best,
Neha
