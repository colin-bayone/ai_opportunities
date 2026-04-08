# Meeting 3 - Timeline Reconstruction

## Overview

This document reconstructs the chronological flow of Meeting 3 between BayOne (Colin, Zahra, Neha) and Sephora (Andrew Ho, Gariashi Chakrabarty). The meeting was a technical discovery session following strategic alignment with Mani in Meeting 2.

---

## Phase 1: Opening & Technical Difficulties (0-5 min)

### Technical Issues
- Zahra had laptop issues, joined via phone initially
- Brief confusion about meeting invite reaching Zahra
- Minor delay getting everyone connected

### Introductions
Zahra sets context:
> "We've been talking about Colin forever, so he's here. He's real. We had a conversation with Mani just a couple of weeks ago and I'll let Colin take lead."

---

## Phase 2: Colin's Context Summary (5-12 min)

Colin demonstrates preparation by summarizing his understanding:

**What Colin stated:**
- Large-scale multi-year data **re-engineering** project (correctly used "re-engineering" not "migration")
- Current state: SQL Server databases, IBM Cognos reporting, IBM DataStage ETL
- Target: Databricks with Cognos frontend retained during transition
- Scale: 6,000+ reports, 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20 source systems
- Finance track making progress

**Gariashi's Correction:**
> "Not completion, just a quick correction. It'll go throughout, you know, end of this year, but we are making progress."

Colin immediately incorporated the correction - demonstrating listening skills.

---

## Phase 3: Semantic Layer Discussion (12-18 min)

Colin probes on semantic layer priority (mentioned by Mani as important but not blocking).

**Gariashi's response:**
> "That is the ideal state, right, that we are looking for so that the semantic layer stays common between all these different reporting tools... We want to stay tool agnostic so that whichever tool we use, we just point it to the same data set. And the KPIs that they are showing is... we don't have questions on, oh, this is something different."

**Key insight:** Semantic layer is about consistency across Cognos, ThoughtSpot, cubes - preventing "my number vs. your number" disputes.

---

## Phase 4: Colin's Background & Credibility Building (18-25 min)

Colin shares relevant experience:

**Prior role at Coherent:**
- $16B revenue company, 40,000 employees
- Director of AI with BI attached
- Similar migration: on-prem SQL Server to Snowflake
- Multi-geography, change management challenges
- Both AI and BI need same data source (garbage in, garbage out)

**On semantic layer importance:**
> "Semantic layer... that's kind of the glue that holds everything together. So that's a really good thing to prioritize. It's a very tough thing to do retroactively."

**On AI/BI alignment:**
> "AI needs to speak the same language as the reports because those phone calls you get whenever the company chatbot came back with different reporting numbers than the actual report on the screen is a big problem."

---

## Phase 5: Pain Points Revealed - CRITICAL SECTION (25-35 min)

### Pain Point #1: SSAS to Databricks Connector (Gariashi)

> "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management. We have these aggregated tables in form of cubes, but we have an Excel pivot table that's feeding data from those SSAS cubes, and business just drags and drops those KPIs, so they love the Excel view. Now SSAS doesn't have a connector to Databricks where we can retain that."

**Current workaround:** Move data to Databricks, expose via ThoughtSpot UI.
**Problem:** Business users must switch from Excel to ThoughtSpot - major change management friction.

### Pain Point #2: Agent Automation (Gariashi)

> "We want to ideally have an agent that would integrate with Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks. Similarly, we have DataStage tool which is the ETL tool... we would want an agent to go integrate with DataStage, read all that and re-engineer code automatically on Databricks."

**Current state:** Manual job-by-job process - extract XML, feed to AI, check output, deploy.

### Andrew's Vision: Agent Swarm

> "Can we create multiple agents, small little agents that can do all this little step by step for us, and they have a big orchestration kind of agent that orchestrates this entire flow?... Rather than spending money on manual contractors, take the money and resources and spend it upfront to create all these agents."

**Ambition:** Compress 3-year timeline to 1-1.5 years.

### Andrew's Transparency on Competition

> "I'm just going to be very transparent. We have been talking this exact same conversation with a lot of different vendors right now. Because I know for a fact, right now outside there's no one has a pre-built package that we can just say, 'I want to buy your package' and run through this migration without any human involved."

---

## Phase 6: Colin's Framework Presentation (35-45 min)

Colin shares screen and presents AI acceleration ideas:

### Report Similarity & Knowledge Graph
- System learns patterns and feeds into central knowledge graph
- Anything learned in one report preserved for future
- Builds flywheel - things improve over time

### On Agent Specificity
> "Agents in general work better if they're more specific. So if you try to have a small subset of agents that, this is my reports agent. No, no, no. Here's the reports validator agent. Here's the one that checks the past state and the present state."

### Schema Mapping Deep Dive (Gariashi Probed)

Gariashi asked: "I'm a little interested in the schema mapping validation. Where it maps, like, how does it automate?"

**Colin's 3-phase approach:**
1. **Phase 1 (No AI):** Recursive exploration of all tables, schemas, structures
2. **Phase 2 (No AI):** Initial mapping based on common fields - gets ~30% certainty
3. **Phase 3 (AI):** Orchestrator + Judge agent pattern

**On Judge agent:**
> "The judge, I call him like the grumpy old man agent, kind of yells at everyone, stay on track, follow this workflow, do not deviate. If it deviates, it rejects immediately."

### MCP for Tool Integration
> "On the actual tool integration part, that becomes more of an MCP problem than an agent problem... Agents combined with MCP to actually interact with those utilities and tools is much better because it's more reliable."

### Framework Choice
> "Even for us, that would be LangGraph. We do something custom with LangGraph, something that scales. That's much better than just trying to do it in Claude Code."

---

## Phase 7: Infrastructure Discussion (45-48 min)

### Gariashi's Question
> "Would you guys develop the agents in our ecosystem, like using Databricks, or is it something like a new tool you guys bring in?"

### Colin's "Meet You at Your Home" Response
> "We don't want to force you into using another tool. You're already getting another tool... For us, it would be built on your infrastructure if that is desired. We can follow all the organizational rules."

**Examples given:**
- Use client-approved IT tools
- Work on client-issued hardware with their image
- Deploy on client infrastructure

### Cost Optimization Angle
> "If you're on Azure, you have Azure AI Foundry. Everything with Azure AI Foundry is just as secure as when you use Outlook. Using Azure AI Foundry models are way cheaper than their commercial API counterparts."

---

## Phase 8: Next Steps & Demo Requirement (48-55 min)

### Andrew Asks "What's Next?"

Colin proposes 3-tier model (from Mani):
1. **Type 1:** BayOne takes full responsibility
2. **Type 2:** Partnership model (Colin's preference)
3. **Type 3:** Pure staffing (Colin's least favorite)

### Gariashi's Critical Demo Requirement

> "It would really help me if we could see some kind of a demo or agents that you guys have created that has done this kind of job... That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working."

And later, more emphatically:
> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this... That's something very selfishly, very important for me."

### Colin's 3 Demo Options
1. **Case studies** - Can share but can't show actual client work
2. **POC on Sephora's data** - Live demo with representative sampling
3. **Demo on mock data** - Safest but no value-add

### Andrew's Feasibility Concern
> "What I don't know is whether, because of our version of the software, for example Cognos that we have is a very, very old version (10.3 or 10.2)... In order for the AI agent to go in and read stuff... either this software has an open SQL server or database, or it has an API endpoint. Otherwise, your agent won't be able to connect."

### Colin's Reassurance
> "The good news with older software... it's easier to get into older software... The more normal things are, the more support there is, the more likely someone already has made a connector."

---

## Phase 9: Closing & Scheduling (55-end)

### Andrew's Proposal
1. Architecture session with Mahair (enterprise architect)
2. Demo/POC session

### Scheduling
- Zahra to coordinate
- Target: Next Thursday (week of March 10)
- Will include Mahair

### Colin's Request
> "If I can add one more item... if there's a priority ranking of things that would be, even from our concerns perspective, or things that we'd like to be done as pain points or deliverables perspective, that'd be super helpful."

### Meeting Close
- Zahra wraps up due to their 12:30 conflict
- Off-topic question from Neha about interview scheduling
- Positive energy: "We're super excited"

---

## Meeting Flow Summary

| Time | Phase | Key Moment |
|------|-------|------------|
| 0-5 | Opening | Technical difficulties resolved |
| 5-12 | Context | Colin demonstrates preparation |
| 12-18 | Semantic Layer | Gariashi confirms importance |
| 18-25 | Credibility | Colin's Coherent experience shared |
| 25-35 | **Pain Points** | SSAS connector + agent automation revealed |
| 35-45 | Framework | Schema mapping deep dive |
| 45-48 | Infrastructure | "Meet you at your home" resonates |
| 48-55 | Next Steps | Demo requirement established |
| 55+ | Closing | Thursday scheduled, Mahair to join |
