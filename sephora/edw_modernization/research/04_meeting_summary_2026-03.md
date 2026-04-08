# 04 - Meeting: Summary

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive with Malika, Sergey)
**Pass:** Summary (final document for set)

---

## What This Meeting Was

The critical technical deep dive where Colin met Sephora's technical team: Sergey (10-15 year IBM tools SME) and Malika (enterprise architect). Brief disconnect at the start (Colin expected demo day, Sephora expected Q&A), quickly resolved. Colin presented detailed agent architecture and shared homework on Cognos/DataStage SDK availability. Sergey and Malika provided the technical inputs that shaped everything built afterward.

## Key Outcome

Two demo tracks crystallized, materials were committed, and the output format was defined. This meeting produced the blueprint for the demo being given today.

## Documents in This Set

| File | What It Covers |
|------|---------------|
| `04_meeting_people_2026-03.md` | Sergey and Malika enter the conversation. Sergey is the most consequential new voice. |
| `04_meeting_cognos_mcp_and_sdk_2026-03.md` | Cognos and DataStage have full SDKs (Java/.NET, back to 2003). MCP server approach. Demo vs production distinction. |
| `04_meeting_sergeys_framework_and_yaml_2026-03.md` | **The most important file.** AggregationApplication framework: no Scala code, just 3 YAML configs per job. Sergey's critique of Claude's "spaghetti code" notebooks. 10 non-negotiable requirements for output. |
| `04_meeting_agent_architecture_detailed_2026-03.md` | Three-phase mapping, knowledge graph, confidence via human reinforcement, blockchain-style context, guardrails, failure handling, playbook concept. |
| `04_meeting_demo_scope_and_materials_2026-03.md` | Disconnected approach (no env access), two tracks (Cognos conversion + DataStage ETL), materials Sephora will share, security workaround, next steps. |
| `03-04_changes_2026-03.md` | Bridge: Sergey and Malika enter, YAML framework defined, disconnected approach, two tracks emerge. |

## The Three Things That Matter Most From This Meeting

1. **Sergey's YAML framework is the law.** The demo output MUST be YAML configuration files (pipeline YAML, deployment YAML, create.HQL) for the existing AggregationApplication framework. Not Scala code. Not Databricks notebooks. Not raw SQL files. YAML configs with 20-50 parameters that fit the existing production support model. This is non-negotiable. Sergey described Claude producing "spaghetti code" notebooks as a nightmare. The demo Saurav built respects this completely.

2. **Two demo tracks defined:**
   - **Track A (Cognos):** Take exported Cognos report XML, dissect it with MCP, remap SQL to Databricks. Shows agent integration with legacy reporting tools.
   - **Track B (DataStage ETL):** Take DataStage job XML + stored procedures, convert to Spark SQL, generate YAML configs. Shows agent-driven code conversion fitting existing framework.
   - Sephora chose Track B (confirmed in Set 04a emails). Track A remains as a future engagement item because MCP connectivity requires Cognos environment access.

3. **Disconnected approach is the path.** Malika solved the security blocker by proposing: share exported artifacts, build the demo externally, skip live validation. This made the fast-turnaround POC possible.

## What Happens Next

Malika sends the Cognos report XML and DataStage materials (Set 04a email thread). Sephora selects Track B. Colin and Saurav build the demo. The Saurav debrief (Set 05) captures the competitive intel that Sephora dismissed all other vendors.
