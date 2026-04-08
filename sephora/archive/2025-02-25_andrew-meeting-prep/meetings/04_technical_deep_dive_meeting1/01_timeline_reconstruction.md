# Meeting 4 - Timeline Reconstruction

## Overview

This document reconstructs the chronological flow of Meeting 4 between BayOne (Colin, Neha Malhotra, Zahra Syed) and Sephora (Andrew Ho, Gariashi Chakrabarty, Maher Burhan, Sergei Shtypuliak). This was the technical deep dive meeting following strategic alignment in previous meetings.

---

## Phase 1: Opening & Introductions (0-3 min)

**Participants joining:** Zahra, Andrew, Colin, Neha, Gariashi, Maher, Sergei

**Quick introductions:**
- Neha introduces herself as VP of Growth and Customer Success
- Colin introduced as "head of AI"
- Recognition that everyone already knows each other from previous meetings

**Handoff:** Neha asks Colin to recap the last discussion and take the lead.

---

## Phase 2: Colin's Recap & Framing (3-10 min)

**Colin recaps Meeting 3 pain points:**
1. Integrations with old Cognos reports - "I've got some good news to share there. We did some homework for you."
2. Dynamic mapping with AI - addressing manual effort and scale
3. Controlled agentic approach - keeping things aligned across the 3-year effort

**Colin's expectations for today:**
- Technical breakdown of current state
- How AI has been used so far, challenges and successes
- Identify pain points to align demo

**Demo options mentioned:**
- Deep data mapping demo
- Cognos integration demo
- Mentioned he has friends at Databricks and got a demo instance set up

**Key statement:** "From my aspect it's just a matter of knowing what's most valuable to you and aligning ourselves to that."

---

## Phase 3: Expectation Mismatch Revealed (10-15 min)

**Gariashi's response:** "I think we were excited to see the demo today."

**The disconnect surfaces:**
- Sephora expected a demo today
- BayOne expected to gather technical requirements for building a demo

**Neha's diplomatic recovery:**
> "I apologize if there was a little... I thought we left off that discussion intending to have a technical discussion with your architect so that when we do the demo, we have the information we need to make sure that the demo is going to be relevant to you."

**Andrew's clarification and support:**
> "Again, you know, I don't think we necessarily need to have support data to actually demo, but it's really about demoing the capability, right? Whether it's even possible to create all those different smaller agents and have an orchestrator agent to orchestrate all the smaller agents."

**Andrew reframes the session purpose:**
- Opportunity for Colin to ask their experts (Maher, Sergei) questions
- Concern about software versions and whether endpoints are open for AI agents
- Introduced Sergei: "our SME on all our IBM tools... he's been the developer for us throughout the last 10, 15 years"

---

## Phase 4: Colin's Technical Presentation (15-25 min)

**Colin's relief:** "Thank you for that because I was like, oh no, I messed up today."

**Cognos/DataStage Research Findings:**
- Found "beautiful perfect all-inclusive APIs or SDKs for both"
- Available in Java and .NET
- Works for any version after 2003
- "We can definitely link into any of the Cognos reports for any past or current versions"

**MCP Server Explanation:**
- Custom-built, not pre-existing
- "Not uncommon for us at all... we have to do this very often when it comes to legacy platforms"
- Gives programmatic access to Cognos for agents

**Maher's question:** "So you're building a custom MCP server to talk to Cognos SDK. And what does that, in this scenario, what's the outcome of this activity?"

**Colin's response:**
1. Report mapping - pull data programmatically instead of manual feed
2. Parity verification - deeper exploration than screenshots or human notes

**Colin asks key question:** "What do humans do today that we would want to make agentic?"

---

## Phase 5: Andrew's Detailed Workflow Walkthrough (25-35 min)

**Andrew provides comprehensive manual workflow:**

**Two types of Cognos reports:**
1. **Framework Model reports** - Point to IBM Framework Manager Model
   - Report executes, SQL generated dynamically based on model
   - Migration: Update Framework Model to point to Databricks
   - Reports automatically work if model is updated

2. **Freehand SQL reports** - Custom SQL written directly in queries
   - Must manually extract SQL
   - Convert to Databricks SQL syntax
   - Test, then paste back into report

**Andrew's ask:** "Is there any way throughout this step that we can create agents? Again, the agent doesn't... I'm not expecting one agent do it... it's like a lot of smaller agents... and then you have that one orchestrator to just orchestrating this whole entire all the smaller agents."

**Gariashi adds current state:**
- Using Claude for extraction from XML
- Using Claude for SQL Server to Databricks code translation
- Getting XML is still manual (login, download from Report Studio)
- No end-to-end agent yet

---

## Phase 6: Colin's Schema Mapping Methodology (35-42 min)

**Colin walks through the 3-phase approach:**

**Phase 1: Structural Discovery (No AI)**
- Recursive crawler script
- Map tables, databases, columns, relationships, data types
- Both SQL Server and Databricks sides

**Phase 2: Rule-Based Mapping (No AI)**
- Matching verification
- Not 1:1 mapping - confirms 100% accuracy cases only

**Phase 3: AI-Assisted Mapping**
- Fills in gaps from phases 1 and 2

**Confidence-based routing explained:**
- Confidence comes from human reinforcement, not LLM
- "If I've said, yes, you can do this five times in a row, and time number six, you don't need to ask me to do it"

**Knowledge Graph:**
- Maintains state of the system
- Prevents infinite loops
- Tracks changes in both environments

**Guardrails and failure handling discussed**

---

## Phase 7: Q&A and Demo Scoping (42-50 min)

**Colin's questions:**
1. "How deep is Databricks right now? Is everything migrated?"
   - Answer: Databricks very mature, thousands of jobs in production
   - EDW to Databricks migration just started January, very few tables migrated

2. "Are there priority reports on the to-do list?"
   - Answer: Yes, project plan exists - Finance first, then dot-com, vendor seller

**Maher's practical proposal:**
- Pick a Cognos report that does not need query restructuring
- Lift and shift, point to Databricks
- Validate separately (bypasses security concerns)

**Sergei's key input on DataStage:**
- Goal is to convert to existing Databricks framework (YAML configs)
- No need to write Scala/Python code
- Just need to generate config files
- Problem with Lakehouse: "spaghetti code... hundreds of notebooks... nightmare to debug"

**Security discussion:**
- Sephora IT has blocked internal MCP server attempts before
- Colin offers to help talk to IT/security teams
- Proxy approach acceptable

---

## Phase 8: Next Steps Agreement (50-52 min)

**Agreed deliverables:**
1. Sephora provides one Cognos report XML (from Finance track, work with Vlad)
2. Sephora provides Databricks catalog/schema info for target mapping
3. BayOne builds demo: lift-and-shift conversion without direct system access
4. Optional: Simple DataStage job definition for additional demo

**Neha's summary:** "Just waiting on those reports from you, and then we set up a time for that first level demo to showcase capabilities."

**Meeting ends positively:**
- Gariashi: "Yeah, that sounds good."
- Colin's closing thought (after call): "Whoo!"

---

## Key Turning Points

1. **Expectation mismatch recovery** - Could have derailed the meeting but handled gracefully by Neha and Andrew
2. **Andrew's workflow walkthrough** - Provided exactly what Colin needed to scope the demo
3. **Maher's practical proposal** - Simplified the demo scope by removing system access requirement
4. **Sergei's framework insight** - Clarified DataStage conversion should output YAML configs, not code

---

## Meeting Dynamics

| Aspect | Observation |
|--------|-------------|
| Energy | Started tense (expectation mismatch), recovered to collaborative |
| Leadership | Andrew provided air cover when confusion arose |
| Technical depth | High - Maher and Sergei provided real implementation details |
| Outcome | Clear, actionable next steps agreed |
