# 04 - Meeting: People

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive with Malika, Sergey)
**Pass:** People identification and dynamics

---

## On the Call

### Colin Moore (BayOne)
- **Tone:** Came prepared with homework (Cognos SDK/API research, MCP architecture slides). Initially thought this was demo day and had a brief disconnect, quickly recovered. Walked through detailed agent architecture, mapping methodology, and MCP approach. Very technical, very transparent about what requires setup effort vs what's easy.

### Andrew Ho (Sephora)
- **Role:** Strategic owner, setting expectations for the session
- **Key moment:** Clarified the session intent: "This is an opportunity for you to ask our experts questions. We have an enterprise architect, we have Sergey who is the SME on IBM tools for 10-15 years."
- **Tone:** Direct, managed the meeting flow, kept things on track

### Grishi (Sephora)
- **Role:** Execution owner, asked pointed questions about demo scope
- **Key signal:** Still pushing for demo/POC evidence. "We need to see a demo, really."
- **Clarified:** They're also looking for agents to help with table data migration from SQL Server to Databricks, not just the report side.

### Sergey (Sephora) - **NEW**
- **Role:** Senior developer / SME on IBM tools (Cognos, DataStage). Has been the backend developer for 10-15 years.
- **Tone:** Pragmatic, experienced, slightly skeptical. "It's easy said than done. I worked with Cognos, I wrote code for the BI server, and that's complicated."
- **Critical contribution:** Explained the existing AggregationApplication framework on Databricks. Developers don't write Scala code. They write YAML configuration files (3 per job: pipeline YAML, deployment YAML, create HQL). The framework already exists with logging, file flows, production support. He explicitly said: "No need to create new framework. No need to write Scala code. Just create config files."
- **Key concern:** "Lake bridge" (Claude) produces "spaghetti code" in Databricks notebooks. Hundreds of windows, nightmare to debug and maintain. Wants output that fits their existing support model.
- **This is the person whose guidance shaped the entire demo output format.**

### Malika / "Meher" / "My hair" (Sephora) - **NEW**
- **Role:** Enterprise architect
- **Tone:** Practical, solution-oriented. Suggested the disconnected approach (no need to access Sephora environment for demo). Proposed the two-step demo: (1) lift and shift Cognos report, (2) do the remapping.
- **Key contribution:** Outlined how to get Colin what he needs without going through Sephora security: share the Cognos report XML + Databricks schema info.

### Neha (BayOne)
- **Role:** VP of Growth and Customer Success. Did introductions.

### Zahra (BayOne)
- **Role:** Wrapped up with next steps and coordination

---

## Key Dynamics

- Brief disconnect at the start: Sephora expected technical Q&A, Colin expected demo day. Quickly resolved by Andrew and Neha.
- Sergey's input is the most consequential of the meeting. His YAML configuration framework explanation is what defines Track B and what Saurav ultimately built the demo around.
- Malika's pragmatism on the disconnected approach (share XML + schema, skip security hurdles) is what made the POC feasible on a fast timeline.
- The meeting ended with concrete deliverables: Sephora will share a Cognos report XML, and Colin will build a demo around it.
- Security blocking was acknowledged as a known issue. Colin offered to help navigate IT conversations.
