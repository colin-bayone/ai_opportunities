# Meeting Breakdown: Andrew Ho & Grishi Chakraborty Technical Discovery

## Metadata

| Field | Value |
|-------|-------|
| **Date** | March 5, 2026 (estimated) |
| **Duration** | ~45-50 minutes |
| **Type** | Technical Discovery / Capability Showcase |
| **Meeting Number** | 3 of 3 (in Sephora engagement series) |

## Participants

| Name | Organization | Role | Participation Level |
|------|--------------|------|---------------------|
| **Andrew Ho** | Sephora | Sr. Director, Marketing AI & Enterprise Reporting | Active - strategic questions, decision authority |
| **Grishi Chakraborty** | Sephora | Director, Data Engineering / BI & Analytics | Very Active - technical depth, pain points, requirements |
| **Colin Moore** | BayOne | Director of AI | Lead presenter, technical credibility |
| **Zahra Syed** | BayOne | Director, Strategic Accounts | Facilitation, scheduling, relationship management |
| **Neha Malhotra** | BayOne | Head of Recruiting | Present, minimal speaking |

## Transcription

The following corrections were applied throughout this document:

| Original | Corrected |
|----------|-----------|
| "Moni" / "money" (person context) | Mani |
| "Garishi" / "Greshey" / "Guruji" | Grishi |
| "my hair" | Mahair |
| "Semitic Lair" | Semantic Layer |
| "Card notes" / "Cognize" | Cognos |
| "line graph" | LangGraph |
| "Cloth skills" | Claude skills |
| "coherent" | Coherent |
| "Lake bridge" | [unclear - likely "Lakehouse"] |

---

## Timeline Reconstruction

### Opening (0-5 min)
- Technical difficulties getting Zahra connected
- Brief introductions; Zahra notes "we've been talking about Colin forever, so he's here"
- Colin takes the lead

### Colin's Context Summary (5-12 min)
Colin demonstrates preparation by summarizing understanding:
- Large-scale multi-year data **re-engineering** project (not lift-and-shift)
- SQL Server databases, IBM Cognos reporting, IBM DataStage ETL
- Target: Databricks with Cognos frontend retained during transition
- Scale: 6,000+ reports, 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20 source systems
- Finance track making progress (Grishi corrects: "not completion... it'll go throughout end of this year")

### Semantic Layer Discussion (12-18 min)
- Colin asks about semantic layer priority
- Grishi confirms: ideal state is common semantic layer across all reporting tools (Cognos, ThoughtSpot, cubes)
- Goal: tool-agnostic, same KPIs regardless of which tool queries them
- Prevents "my KPI shows X but yours shows Y" disagreements

### Colin's Background & Credibility (18-25 min)
Colin shares relevant experience:
- Prior role at Coherent ($16B revenue, 40,000 employees)
- Led similar migration: on-prem SQL Server to Snowflake
- BI and AI co-leadership (semantic layer critical for both)
- Multi-geography change management experience
- Emphasizes: "Being tool agnostic is really important"

### CRITICAL: Pain Points Revealed (25-35 min)

**Grishi's Pain Point #1 - SSAS to Databricks Connector:**
> "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management. We have these aggregated tables in form of cubes, but we have an Excel pivot table that's feeding data from those SSAS cubes, and business just drags and drops those KPIs, so they love the Excel view. Now SSAS doesn't have a connector to Databricks where we can retain that."

Current workaround: Move data to Databricks, expose via ThoughtSpot. But this means business users must switch from Excel to ThoughtSpot UI - major change management problem.

**Grishi's Pain Point #2 - Agent Automation:**
> "We want to ideally have an agent that would integrate with Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks. Similarly, we have DataStage tool which is the ETL tool... we would want an agent to go integrate with DataStage, read all that and re-engineer code automatically on Databricks."

Current state: Manual process of going job-by-job, extracting XML, feeding to AI, validating, deploying.

**Andrew's Vision - Agent Swarm:**
> "Can we create multiple agents, small little agents that can do all this little step by step for us, and they have a big orchestration kind of agent that orchestrates this entire flow? Rather than spending money on manual contractors, take the money and resources and spend it upfront to create all these agents so that once it's all done, it can parallel run and do all the thing by itself."

Andrew's ambition: Compress 3-year timeline to 1-1.5 years through AI acceleration.

**Andrew's Transparency:**
> "I'm just going to be very transparent. We have been talking this exact same conversation with a lot of different vendors right now. Because I know for a fact, right now outside there's no one has a pre-built package that we can just say 'I want to buy your package' and run through this migration without any human involved."

### Colin's Response & Framework Presentation (35-45 min)

Colin shares screen and presents AI acceleration ideas:

1. **Report Similarity Clustering** - Learn patterns, feed into central knowledge graph
2. **Business Logic Extraction** - Unify and harmonize across reports
3. **Dependency Mapping** - Trace relationships
4. **Schema Mapping Validation** - Multi-phase approach (non-AI first, then AI)

**Schema Mapping Deep Dive (Grishi's Interest):**
Colin explains the process:
1. **Phase 1 (No AI):** Recursive exploration of all tables, schemas, structures - "flat picture of playing field"
2. **Phase 2 (No AI):** Initial mapping based on common fields and routes - gets ~30% certainty
3. **Phase 3 (AI):** Orchestrator agent + Judge agent pattern
   - Orchestrator coordinates tasks
   - Judge ("grumpy old man agent") enforces workflow, rejects deviations
   - Reports generated to keep humans aware (not black box)

**MCP and Tool Integration:**
> "On the actual tool integration part, that becomes more of an MCP problem than an agent problem, because you want to get all these different tools connected. Agents combined with MCP to actually interact with those utilities and tools is much better because it's more reliable."

**Framework Preference:**
> "Even for us, that would be LangGraph. We do something custom with LangGraph, something that scales. That's much better than just trying to do it in Claude Code. Claude Code can get you pretty far, but with 6,000 odd reports, that's pretty tough to do consistently."

### Infrastructure Discussion (45-48 min)

**Grishi asks:** "Would you guys develop the agents in our ecosystem, like using Databricks, or is it something like a new tool you guys bring in?"

**Colin's response - "Meet you at your home":**
> "We don't want to force you into using another tool. You're already getting another tool. For us, it would be built on your infrastructure if that is desired. We can follow all the organizational rules. For other clients we work with, we use everything that's approved from their IT department, or even working on their hardware. We have laptops that are issued and physically have their image on it."

**Cost optimization angle:**
> "If you're on Azure, you have Azure AI Foundry. Everything with Azure AI Foundry is just as secure as when you use Outlook. Using Azure AI Foundry models are way cheaper than their commercial API counterparts. So you can do a lot of cost optimization just by using infrastructure."

### Next Steps Discussion (48-55 min)

**Andrew's question:** "What's the next step?"

**Colin proposes 3-tier model (from Mani conversation):**
1. **Type 1:** BayOne takes full responsibility, delivers on requirements
2. **Type 2:** Partnership model - BayOne does AI work but alongside Sephora team, upskilling happens
3. **Type 3:** Pure staffing (Colin's least favorite - "can't control that")

**Grishi's Request - THE KEY ASK:**
> "It would really help me if we could see some kind of a demo or agents that you guys have created that has done this kind of job, be ingestion automated this stuff. That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working."

**Colin offers 3 options for demo:**
1. **Case studies** - Can share but can't show actual client work
2. **POC on Sephora's data** - Live demo with representative sampling, can feed into SOW
3. **Demo on mock data** - Safest but no value-add

**Andrew's Feasibility Concern:**
> "What I don't know is whether, because of our version of the software, for example Cognos that we have is a very, very old version (10.3 or 10.2)... and DataStage, it's not the latest version either. In order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL server or database, or it has an API endpoint. Otherwise, your agent, it can be as smart as you can be, it won't be able to connect to that software."

**Colin's reassurance on legacy software:**
> "The good news with older software, to be honest with you, is the same reason why it gets old is because... it's easier to get into older software. The more normal things are, the more support there is, the more likely someone already has made a connector."

**Colin's only concern:** Speed and production impact
> "My only concern would be on speed. And if those things are in production or if they're kind of a staging server, because I also wouldn't want to kill the server if it's production and you need that data to do some business function. And I'm querying it a million times with an agent."

### Closing & Scheduling (55-end)

**Andrew proposes:**
1. Architecture session with Mahair (enterprise architect)
2. Demo/POC session

**Grishi reiterates demo requirement:**
> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this, that done created agents that is capable of doing these kind of things. That's something very selfishly, very important for me."

**Scheduling:**
- Zahra to coordinate
- Aim for next Thursday (week of March 10)
- Will include Mahair for architecture deep dive

---

## Key Decisions Made

| Decision | Made By | Context |
|----------|---------|---------|
| Build on Sephora's infrastructure | Colin (proposed), Andrew/Grishi (agreed) | No new tools, use existing Azure/Databricks |
| Demo required before deeper commitment | Grishi | Confidence-building before proposal |
| Architecture session with Mahair | Andrew | Include enterprise architect in next meeting |
| Next meeting: Thursday week of March 10 | All | Zahra to coordinate |

---

## Commitments Made

### BayOne Commits To:
| Commitment | Owner | Timeline |
|------------|-------|----------|
| Prepare demo showing agent capabilities | Colin | Before next Thursday |
| Share case studies | Colin | ASAP |
| Coordinate scheduling for next meeting | Zahra | This week |
| Architecture deep dive with Mahair | Colin | Next Thursday |

### Sephora Commits To:
| Commitment | Owner | Timeline |
|------------|-------|----------|
| Provide priority ranking of pain points/deliverables | Andrew/Grishi | Before next meeting |
| Include Mahair (architect) in next meeting | Andrew | Next Thursday |
| Share architecture details in deep dive | Grishi/Mahair | Next Thursday |

---

## Open Items / Questions

| Item | Owner | Priority |
|------|-------|----------|
| What specific data/reports can be used for POC? | Sephora | High |
| Can we get staging server access vs. production? | Sephora | High |
| Priority ranking of pain points | Sephora | High |
| Mahair's contact info | Grishi | Medium |
| Excel connector feasibility for SSAS→Databricks | Colin | Medium |

---

## Key Quotes

### On the Vision (Andrew):
> "Can we create multiple agents, small little agents that can do all this little step by step for us, and they have a big orchestration kind of agent that orchestrates this entire flow?... Rather than spending money on manual contractors, take the money and resources and spend it upfront to create all these agents."

### On Transparency (Andrew):
> "I'm just going to be very transparent. We have been talking this exact same conversation with a lot of different vendors right now. Because I know for a fact, right now outside there's no one has a pre-built package."

### On Demo Requirement (Grishi):
> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this, that done created agents that is capable of doing these kind of things. That's something very selfishly, very important for me."

### On Infrastructure (Colin):
> "We don't want to force you into using another tool. You're already getting another tool... For us, it would be built on your infrastructure if that is desired."

### On Legacy Software (Colin):
> "The good news with older software, to be honest with you, is the same reason why it gets old is because... it's easier to get into older software."

### On Agent Architecture (Colin):
> "The more specific you go with agents without going overly specific, the better off you are... Model them after real life things. How does this work in real life? Imagine if AI wasn't a part of the picture. What would the team look like? That's how you can think of designing those agent swarms."

---

## Meeting Assessment

### What Went Well:
1. Colin's preparation was evident - summarized context accurately
2. Technical credibility established (Coherent experience, LangGraph, MCP knowledge)
3. Andrew and Grishi were highly engaged and forthcoming
4. Clear alignment on agent swarm approach
5. Infrastructure flexibility ("meet you at your home") resonated

### What Could Have Gone Better:
1. No live demo ready - Grishi explicitly wanted to see something working
2. Didn't probe deeper on production vs. staging server availability
3. Didn't ask about timeline pressure (is 3 years firm? 1.5 years aspiration?)
4. Didn't ask about budget constraints

### Critical Success Factors for Next Meeting:
1. **MUST have a working demo** - Grishi explicitly stated this is "very selfishly, very important"
2. Need to show agent-to-tool integration working (not just conceptual)
3. Architecture deep dive with Mahair
4. Come with POC scope proposal
