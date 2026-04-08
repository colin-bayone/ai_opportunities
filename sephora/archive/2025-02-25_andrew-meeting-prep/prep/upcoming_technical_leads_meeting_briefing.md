# Meeting Prep Briefing: Sephora Technical Leads

**Prepared for:** Colin Moore
**Meeting type:** Technical deep-dive with Sephora architects
**Expected attendees:** Andrew Ho, Grishi Chakraborty, Mahair (Enterprise Architect)
**Date:** Week of March 10, 2026

---

## Executive Summary

You're entering the **technical validation phase** of the Sephora engagement. Grishi has explicitly stated he won't commit time without seeing a working demo. Andrew is actively shopping multiple vendors but disclosed that no one has a ready solution - this is a custom build for everyone.

**Your goal this meeting:** Steer the conversation toward getting access to their environment. This is the fastest path to proving value and avoids wasting effort on mocks.

---

## Synthesis: What We Know from 3 Meetings

### Meeting 1 (Mani - Strategic)
- Mani is the VP and decision-maker
- Wants "proposal-led" conversations, not discovery questions
- Shared the 3-year EDW modernization roadmap
- AI acceleration is explicitly desired
- Budget: ~$105-115/hr acceptable

### Meeting 2 (Mani + Colin - Proposal)
- Colin established credibility (Coherent experience)
- Mani validated approach: "You understood it very well"
- Critical correction: **Re-engineering, not migration**
- Requested 3-tier proposal (full delivery, partnership, staffing)
- Mani wants to attend final proposal review in person

### Meeting 3 (Andrew/Grishi - Technical)
- Pain points crystallized:
  1. **SSAS → Databricks connector** (preserve Excel pivot tables)
  2. **Agent automation** (Cognos + DataStage integration)
- Andrew's vision: Agent swarm to compress 3 years → 1.5 years
- Current state: Using Claude manually, 30% efficiency gain
- **Grishi's demo requirement stated 3 times** - non-negotiable
- Competitive landscape: "Talking to lots of vendors, no one has a package"
- Infrastructure flexibility resonated ("meet you at your home")

### Key Stakeholder Map

| Person | Role | What They Need | Gatekeeper? |
|--------|------|----------------|-------------|
| Mani | VP, Decision-maker | Strategic proposal, 3 options | Final approval |
| Andrew | Sr. Director, Vision owner | Agent swarm validation, timeline compression | Strategic alignment |
| Grishi | Director, Execution lead | **Working demo**, proof of capability | **Technical gatekeeper** |
| Mahair | Enterprise Architect | Architecture compatibility | Architecture approval |

---

## The Demo Challenge (Between Us)

Grishi wants to see agents working. Ideally on Databricks. The problem:

- **Databricks enterprise setup is hard** - You don't have a ready environment
- **Mocking takes time** - Effort spent on mocks doesn't deliver real value
- **They have the infrastructure** - Enterprise accounts with Claude, Azure, GCP

### Your Options (Ranked):

| Option | Effort | Value to Sephora | Likelihood of Success |
|--------|--------|------------------|----------------------|
| **Get access to their environment** | Low | Very High | Medium (need to sell it) |
| POC on exported sample data | Medium | High | High |
| Demo on generic SQL/reports | Medium | Medium | High |
| Demo on mock Databricks data | High | Low | Medium |

**Best path:** Steer toward environment access. If they can't provide full access, request an export of 5-10 representative Cognos reports and 2-3 DataStage jobs.

---

## Strategy: Steering Toward Environment Access

### The Pitch (Conversational)

> "We can absolutely show you agents working on mock data - that's one path. But here's my concern: that's time we spend setting up fake infrastructure that doesn't give you any real value.
>
> What if instead we did something more useful? If you could give us access to a staging environment - or even just an export of a handful of representative Cognos reports and DataStage jobs - we could show you exactly what this looks like on your actual stack.
>
> No commitment required. Just a focused 2-3 day exploration. You'd get immediate value regardless of whether we work together, and we'd get the confidence that our approach works with your specific versions of Cognos 10.2 and DataStage."

### Why This Works for Them

1. **De-risks their evaluation** - They see real results, not demos
2. **Immediate value** - Even if they don't proceed, they learn something
3. **Answers feasibility question** - Andrew's concern about legacy software gets resolved
4. **Faster than alternatives** - We're not wasting weeks on mock setup
5. **No commitment** - Low-risk way to validate

### Objection Handling

| Objection | Response |
|-----------|----------|
| "We can't give external access" | "Totally understand. Could we get an export instead? Even 5-10 report definitions and a couple DataStage XML exports would let us show real value." |
| "Security concerns" | "We can work on your hardware, your image, your VPN. We've done this with other enterprise clients - fully inside their security perimeter." |
| "Need to check with IT" | "Of course. While that's in process, what's the smallest representative sample we could work with? Even metadata would help." |
| "Let's see generic demo first" | "Happy to do that. But I want to be upfront - a generic demo will show capability, not feasibility with your specific stack. The real proof comes from touching your actual systems." |

---

## Realistic POC/Demo Options

### Tier 1: If They Grant Environment Access (Best Case)

**What you'd show:**
1. Agent connecting to their Cognos 10.2 and extracting report definitions
2. Pattern detection across their actual reports
3. SQL transformation from their SQL Server dialect to Databricks SQL
4. Orchestration flow handling their DataStage job XML

**Timeline:** 3-5 days focused work
**Value:** High - directly applicable to their migration

### Tier 2: If They Provide Sample Exports (Good Case)

**What you'd need:**
- 5-10 Cognos report definitions (XML/metadata)
- 2-3 DataStage job exports (XML)
- Sample schema from their SQL Server EDW

**What you'd show:**
1. Agent parsing their actual report structures
2. Business logic extraction from their queries
3. Schema mapping against their actual tables
4. Dependency graph from their DataStage jobs

**Timeline:** 4-6 days
**Value:** High - demonstrates capability on real artifacts

### Tier 3: Generic Demo (Fallback)

**What you'd show:**
- LangGraph agent swarm on sample SQL Server database
- Report pattern detection on open-source Cognos-like reports
- Schema mapping between sample EDW and Databricks
- Orchestrator + Judge agent pattern in action

**Timeline:** 5-7 days
**Value:** Medium - shows capability, not feasibility

---

## What They're Most Interested In

From the meeting transcript, ranked by emphasis:

### 1. Agent Automation (Highest Priority)

**What Grishi said:**
> "We want to ideally have an agent that would integrate with Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer."

**What Andrew wants:**
> "Multiple agents, small little agents that can do all this little step by step... with a big orchestration agent that orchestrates the entire flow."

**Demo focus:** Show the orchestration pattern. The LangGraph swarm, the Judge agent, the workflow enforcement.

### 2. SSAS to Databricks Connector (Pain Point)

**What Grishi said:**
> "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management... business just drags and drops those KPIs, so they love the Excel view."

**Reality check:** This is more of a connector/infrastructure challenge than an AI challenge. You mentioned the Hyperion Excel connector experience - lean on that.

**Demo focus:** If you can show a working Excel plugin that connects to a non-SSAS data source, that proves the concept.

### 3. Schema Mapping Validation (Grishi Probed)

**What Grishi asked:**
> "I'm a little interested in the schema mapping validation. Where it maps, like, how does it automate?"

**What he shared:**
> "We have done this mapping using Claude. The only thing that we're figuring out is that there is a manual intervention... it's not 100% accurate."

**Demo focus:** Show the 3-phase approach you described. Emphasize the non-AI first phases that establish baseline certainty.

### 4. Legacy Software Feasibility (Andrew's Concern)

**What Andrew asked:**
> "What I don't know is whether, because of our version of the software... Cognos 10.3 or 10.2... the agent won't be able to connect."

**Your answer was good:** "Older software is easier to get into."

**Demo focus:** If you can connect to ANY legacy system and extract data, the principle transfers.

---

## Conversation Flow for the Meeting

### Opening (5 min)
- Thank them for including Mahair
- Ask Mahair for his perspective on the architecture (engage him early)
- Reference the priority ranking you requested (if they prepared it)

### Architecture Deep Dive (20 min)
- Let Mahair walk through their migration architecture
- Ask specific questions:
  - "What Databricks tools have you selected for ETL?"
  - "How is the semantic layer being structured?"
  - "Where does data validation happen in the current flow?"
- Take notes on integration points for agents

### Your Proposal (15 min)
- Present the POC options (Tier 1, 2, 3 from above)
- **Lead with environment access pitch**
- If resistance, fall back to sample exports
- Be specific: "5-10 reports, 2-3 DataStage jobs"

### Demo Discussion (15 min)
- If they agree to access/exports: discuss timeline and logistics
- If they want generic demo: set expectations clearly
- Either way, agree on what "success" looks like for the demo

### Close (5 min)
- Confirm next steps
- Who provides what, by when
- Schedule follow-up

---

## Key Talking Points

### Differentiation
> "Unlike vendors pushing packaged solutions, we're proposing to build on YOUR infrastructure with YOUR enterprise accounts. No new tools to maintain, no ongoing licensing. When we're done, you have capability, not dependency."

### Realism
> "I want to be direct - no one has a pre-built solution for this. Andrew, you said it yourself. This is custom work regardless of who does it. The question is who can execute and build something that lasts."

### Environment Access
> "The fastest way to prove this works is to touch your actual systems. We can mock things up, but that delays getting you real value. What would it take to get us access to a staging environment or even just sample exports?"

### Risk Mitigation
> "Let's de-risk this for both of us. Give us 3 days with representative samples. If we can show progress, we continue. If not, you've lost nothing and learned something."

---

## Questions to Ask

### For Mahair (Architect)
1. "How are you handling the semantic layer - is it a separate abstraction or embedded in Databricks Unity Catalog?"
2. "What's your data validation strategy between SQL Server and Databricks?"
3. "Are there shared patterns across the Cognos reports, or is each one unique?"

### For Grishi
1. "Did you have a chance to put together that priority ranking we discussed?"
2. "What would a successful demo look like to you specifically?"
3. "Is there a staging environment we could access, or would sample exports work?"

### For Andrew
1. "Has Databricks proposed any AI acceleration tools, and how did those evaluate?"
2. "What's the realistic timeline pressure - is 3 years firm or is there pressure to go faster?"
3. "If we prove the agent approach works, what's the path to a larger engagement?"

---

## Red Lines / Things to Avoid

1. **Don't oversell** - They appreciated your "I'm always the skeptic" stance
2. **Don't commit to timeline without data** - You need to see their systems first
3. **Don't compete with Databricks** - Position as complementary, not replacement
4. **Don't dismiss their existing AI work** - They have 30% efficiency gain; build on it
5. **Don't get defensive about vendor shopping** - Andrew's transparency is a trust signal

---

## Success Criteria for This Meeting

| Outcome | Rating |
|---------|--------|
| Get staging environment access | Excellent |
| Get sample exports (reports + DataStage jobs) | Very Good |
| Agreement on demo scope and timeline | Good |
| Generic demo path agreed | Acceptable |
| No clear path forward | Needs recovery |

---

## Final Note

The ideal outcome is them saying: "Let's get you access to try this on our data."

That saves you from Databricks setup, gives them immediate value, and positions you as focused on their success rather than just selling. Everything in this meeting should subtly point toward that outcome.
