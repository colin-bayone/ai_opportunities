# Neha's Follow-Up Email to Sephora - Draft

## Context
This is a follow-up email after Meeting 4 (Technical Deep Dive) with Sephora. The meeting went well despite an initial expectation mismatch (they expected a demo, we expected requirements gathering). Andrew rescued the meeting gracefully, and we ended with clear next steps.

## Tone Goals
- Warm and appreciative (they gave us a lot of their time and expertise)
- Momentum-building (keep things moving without being pushy)
- Collaborative (we're partners, not vendors demanding deliverables)

## Recipients
- Andrew Ho (Sr. Director)
- Gariashi Chakrabarty (Director, Data Engineering)
- Maher Burhan (Enterprise Architect, Consultant)
- Sergei Shtypuliak (IBM SME, Consultant)

## Key Points to Cover
1. Thank them for the detailed workflow walkthrough
2. Recap what we agreed to demo
3. List what we need from them (without sounding demanding)
4. Keep the door open for questions

---

## Draft Email

**Subject:** Next Steps: Demo Preparation for Cognos/DataStage Agent POC

Hi Andrew, Gariashi, Maher, and Sergei,

Thank you for taking the time to walk us through the full workflow today. That level of detail is exactly what we needed to make the demo directly relevant to your environment.

**What we're building:**
- An MCP connector for Cognos that extracts report metadata and SQL programmatically (eliminating the manual XML downloads from Report Studio)
- Agent-based SQL conversion from SQL Server syntax to Databricks-compatible SQL
- If scope allows, a DataStage job conversion that generates YAML config files aligned with your existing Databricks framework

**What we need from your team:**
1. Cognos report XML export from the Finance folder (full export from Report Studio) — Monica or Vlad can help coordinate this
2. Target Databricks schema — catalog/table structure so the agent can map to the correct destination
3. Sample YAML config file from your Databricks framework (so agent output matches your existing format) — Sergei would be best for this
4. (Optional) DataStage job definition — Maher mentioned a candidate that was partially converted via Lakehouse

Once we have these, we can get the demo on the calendar. If any clarification is needed on exactly what to export, we are happy to set up a quick call.

Looking forward to showing you what the agents can do with your actual artifacts.

Best,
Neha

---

## Original Draft from Neha (for reference)

Great discussion today — really appreciate you and the team walking us through the full workflow in detail. That context is exactly what we needed to make the demo directly relevant to your environment.

To recap where we landed, we're going to build out a focused demo that covers:
• An MCP connector for Cognos that can extract report metadata and SQL programmatically (no more manual XML downloads from Report Studio)
• Agent-based SQL conversion from SQL Server syntax to Databricks-compatible SQL
• If time allows, a DataStage job conversion that generates YAML config files aligned with your existing Databricks framework

To get started on our end, we'll need a few things from your team:
1. One Cognos report XML export from the Finance folder (the full export from Report Studio) — Sounds like Monica/Vlad can help pull this
2. The associated SQL queries for that report
3. (Optional but ideal) A sample DataStage job definition — Mahar mentioned the one that was ~85% converted via Slide Bridge
4. A sample YAML config file from your Databricks framework so the agents generate output in the right format — Sergei would be best for this one

No rush, but the sooner we have these, the sooner we can get the demo on the calendar. Happy to jump on a quick call if anything needs clarification on what exactly to export.

Looking forward to showing you what the agents can do with your actual artifacts.

Best,
Neha
