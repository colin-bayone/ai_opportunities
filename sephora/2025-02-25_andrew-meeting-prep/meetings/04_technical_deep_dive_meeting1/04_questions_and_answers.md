# Meeting 4 - Questions and Answers

## Overview

Catalog of questions asked during the meeting, who asked them, responses given, and follow-up implications.

---

## Questions Asked by Sephora

### Q1: SSAS to Databricks Migration Capability

**Asked by:** Gariashi
**Question:** "Can we talk a little bit about the SSAS to Databricks? Can you describe the capability and what's the percentage of completion if we migrate using the tool?"

**Colin's Response:**
- Databricks is a great modern platform with existing integrations
- Depends on appetite for agentic approach and human-in-the-loop preferences
- Some organizations want hands-off, others want more oversight
- Outlined high-level approach: integrate with reports, build knowledge graph, map both sides (SQL Server and Databricks)

**Implication:** Colin pivoted to explaining general approach rather than specific percentages, as the answer depends on their specific environment.

---

### Q2: MCP Server Outcome

**Asked by:** Maher
**Question:** "So you're building a custom MCP server to talk to Cognos SDK. And what does that, in this scenario, what's the outcome of this activity?"

**Colin's Response:**
1. **Programmatic access** - Report mapping without manual feed, pull data programmatically
2. **Parity verification** - Deeper exploration than screenshots or human notes
3. **Agent tooling** - Gives agents the capability to take actions into Cognos

**Implication:** Maher wanted to understand concrete outcomes, not just technical architecture. Good architect question.

---

### Q3: What Agents Are Needed

**Asked by:** Andrew (implied)
**Context:** After explaining the full manual workflow
**Question:** "Is there any way throughout this step that we can create agents?"

**Colin's Response:**
- Yes, multiple small specialized agents with orchestrator
- Listed example agents: report metadata extraction, SQL parsing, transformation validation, deployment preparation
- Explained stateful agents with knowledge graph
- Described confidence-based routing with human reinforcement

**Implication:** Andrew set up the perfect question for Colin to deliver the agent architecture pitch.

---

### Q4: Security/Access Approach

**Asked by:** Maher (implied through discussion)
**Question:** How do we handle security constraints for external agents?

**Responses (multiple):**
- **Maher:** "We will probably have to go through the whole security thing at Sephora"
- **Maher:** "We tried to run our own agent... we get blocked by security"
- **Colin:** Offered to help talk to IT/security teams
- **Maher's solution:** Do the work without direct system access, validate separately

**Implication:** Security is a known blocker. The workaround (no direct access) was agreed upon.

---

## Questions Asked by BayOne

### Q1: Databricks Migration Progress

**Asked by:** Colin
**Question:** "How deep is Databricks right now? Is everything been migrated or what's the percentage of that migration?"

**Gariashi's Response:**
- "Very less" - only a few tables out of ~1,000 in EDW
- Just started the project in January

**Andrew's Clarification:**
- Databricks environment itself is "very mature"
- Thousands of jobs, P1 applications running
- Many other tables already there (not from EDW)

**Implication:** Important distinction - Databricks is mature as a platform, but EDW-specific migration just started. Agents have plenty of work to do on the migration side.

---

### Q2: Agent Scope Confirmation

**Asked by:** Colin
**Question:** "This agent that we are looking to create, my assumption is not only handling the Cognos migration track, we're also looking for agents to help even the table data migration from SQL Server to Databricks. Are you aligned with that?"

**Andrew's Response:**
- "Yes"
- Clarified they want both sides covered, not just one

**Implication:** Confirmed scope includes both Cognos report migration AND data migration from SQL Server to Databricks.

---

### Q3: Priority Reports

**Asked by:** Colin
**Question:** "For the other reports, are there any that are a big priority to you that are on the to-do list? Is there any kind of forced ranking?"

**Andrew's Response:**
- Yes, they have a full project plan
- Priority order: Finance, dot-com, vendor seller tracks
- Finance reports are first priority

**Implication:** Demo should focus on Finance track reports for maximum relevance.

---

### Q4: Real Data vs Mock Demo

**Asked by:** Colin
**Question:** "If you want us to do it on real data, we can definitely do that... if there was a report that you felt was a good example... we could show you this working on your own system. Now, if you're hesitant about that, I completely understand."

**Maher's Response:**
- Proposed workaround: provide report definition, do conversion without system access
- Sephora validates separately
- Avoids security hurdles

**Gariashi's Response:**
- Agreed to provide Cognos report XML from Finance track
- Will work with Vlad to get it

**Implication:** Demo will use real Cognos report definition but without direct system access. Best of both worlds.

---

### Q5: XML or SQL Query

**Asked by:** Gariashi (clarifying)
**Question:** "Are you looking for the XML or just the SQL query?"

**Colin's Response:** (implied) The full XML is preferred for complete context

**Implication:** Full report definition provides more context than just extracted SQL.

---

## Questions Still Open

| Question | Status | Owner |
|----------|--------|-------|
| Which specific Finance report will be provided? | Pending | Sephora (work with Vlad) |
| What Databricks catalog/schema info will be shared? | Pending | Sephora |
| Will DataStage job also be included in demo scope? | Tentative | Sephora to decide |
| How will security conversation proceed if agents need system access later? | Future | Both parties |

---

## Questions That Should Have Been Asked

| Question | Why It Matters |
|----------|----------------|
| What is the timeline expectation for the demo? | No date was set |
| Who is the decision maker for proceeding after demo? | Is it Gariashi, Andrew, or Mani? |
| What does "success" look like for the demo? | No explicit criteria defined |
| Are there existing YAML config examples for DataStage? | Would help define agent output format |
