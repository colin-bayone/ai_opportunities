# Meeting 3 - Questions and Answers

## Overview

Catalog of questions asked during the meeting, who asked them, responses given, and follow-up implications.

---

## Questions Asked by Sephora

### Q1: Schema Mapping Automation (Gariashi)

**Question:**
> "I'm a little interested in the schema mapping validation. Where it maps, like, how does it automate? Like, what is the process? How does it do it?"

**Context:** Asked after Colin mentioned "automated source to target column mapping" in his framework presentation.

**Response (Colin):**
Detailed 3-phase explanation:
1. **Phase 1 (No AI):** Recursive exploration of all tables, schemas, structures - flat picture
2. **Phase 2 (No AI):** Initial mapping based on common fields, routes - ~30% certainty
3. **Phase 3 (AI):** Orchestrator + Judge agent pattern for remaining mapping

**Follow-up from Gariashi:**
> "We have done this mapping using Claude. The only thing that we're figuring out is that there is a manual intervention, right? We have to feed it the schema and then whatever we are looking for... it's not 100% accurate."

**Implication:** Gariashi already has experience with AI-assisted mapping but wants to eliminate manual intervention and improve accuracy.

---

### Q2: Infrastructure/Ecosystem (Gariashi)

**Question:**
> "Would you guys develop like the agents in our ecosystem, like using Databricks, cloud, or is it something like a new tool you guys bring in or we have to work through, you know, how does that look like?"

**Context:** Asked after Colin's framework presentation, wanting to understand delivery model.

**Response (Colin):**
> "We don't want to force you into using another tool. You're already getting another tool... For us, it would be built on your infrastructure if that is desired."

Also mentioned:
- Can follow organizational rules
- Have worked on client-issued hardware with client images
- Azure AI Foundry as cost-effective option

**Gariashi's Acknowledgment:**
> "Yeah, and it will, I'm assuming, you can use more account infrastructure. Because as you run through those agents, like you mentioned, it's going to use tokens. And we have enterprise account or whatnot, right, with cloud and with all those stuff, even Google Vertex AI."

**Implication:** Infrastructure flexibility is important to Sephora. They have existing enterprise accounts with cloud providers.

---

### Q3: What's Next? (Andrew)

**Question:**
> "What's the next step, I guess?"

**Context:** Asked after Colin's framework presentation, moving to action.

**Response (Colin):**
- Technical deep dive would help
- Can start small to build confidence
- Proposed 3-tier model from Mani conversation
- Offered case studies, POC on their data, or mock demo options

**Implication:** Andrew is actively driving toward action, not just information gathering.

---

### Q4: Demo Capability (Gariashi)

**Question:**
> "It would really help me if we could see some kind of a demo or agents that you guys have created... that has done this kind of job... to see it actually working. That is something I would love to see."

**Context:** Asked after discussing next steps, expressing need for validation.

**Response (Colin):**
Three options:
1. Case studies (can't show actual client work)
2. POC on Sephora's data (preferred - feeds into SOW)
3. Demo on mock data (safest but no value-add)

**Gariashi's Reiteration:**
> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this... very selfishly, very important for me."

**Implication:** Demo is non-negotiable requirement. Without it, engagement stalls.

---

### Q5: Feasibility with Legacy Software (Andrew)

**Question:**
> "What I don't know is whether, because of our version of the software, for example Cognos that we have is a very, very old version... In order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL server or database, or it has an API endpoint or some sort. Otherwise, your agent... won't be able to connect to that software. Then it's moot point."

**Context:** Asked after discussing demo, expressing feasibility concern.

**Response (Colin):**
> "The good news with older software... it's easier to get into older software... The more normal things are, the more support there is, the more likely someone already has made a connector."

Also noted only concern: speed and production impact
> "My only concern would be on speed. And if those things are in production or if they're kind of a staging server, because I also wouldn't want to kill the server if it's production."

**Andrew's Acknowledgment:**
> "And I think it's on-prem. So you're right. From that perspective, it's much easier."

**Implication:** Legacy software concern addressed. Production vs. staging access is open question.

---

## Questions Asked by BayOne

### Q1: Semantic Layer Priority (Colin)

**Question:**
> "He had mentioned that throughout this effort there is a desire for a common semantic layer to be formed? Is that work ongoing as well?"

**Context:** Colin probing on Mani's semantic layer comments.

**Response (Gariashi):**
> "That is the ideal state, right, that we are looking for so that the semantic layer stays common between all these different reporting tools... We want to stay tool agnostic so that whichever tool we use, we just point it to the same data set."

**Implication:** Semantic layer is confirmed priority, not just Mani's preference.

---

### Q2: Pain Points (Colin)

**Question:**
> "For me, I just kind of want to know from both of you, because I don't know too much in my events about either of you, what your take is, if there's pain points."

**Context:** Colin opening discussion to understand execution-level challenges.

**Response (Gariashi):**
Two main pain points:
1. SSAS to Databricks connector (Excel pivot table preservation)
2. Agent automation (Cognos and DataStage integration)

**Response (Andrew):**
Added context on 30% efficiency gain from current Claude usage and vision for agent swarm to compress timeline.

**Implication:** Pain points clearly articulated - these become the focus areas for any proposal.

---

### Q3: Priority Ranking Request (Colin)

**Question:**
> "If I can add one more item onto that would just be of and this does not have to be granular or deep if there's a priority ranking of things that would be, even from our concerns perspective, or things that we'd like to be done as pain points or deliverables perspective, that'd be super helpful."

**Context:** Colin's closing request before scheduling.

**Response (Andrew):**
Implicit agreement - deferred to "Gariashi, you're good with that, right?"

**Status:** Open item - priority ranking expected before next meeting.

**Implication:** Colin wants to focus demo/proposal on highest-value items.

---

## Unanswered Questions / Open Items

| Question | Who Should Answer | Priority |
|----------|-------------------|----------|
| What data/reports can be used for POC? | Sephora | High |
| Production vs. staging server access? | Sephora | High |
| Priority ranking of pain points? | Andrew/Gariashi | High |
| Budget range for engagement? | Andrew/Mani | Medium |
| Timeline flexibility (is 3 years firm?) | Andrew/Mani | Medium |
| What did Databricks propose for AI acceleration? | Gariashi | Medium |

---

## Questions NOT Asked (Potential Gaps)

### From Colin:
1. **Budget:** No discussion of budget constraints or ranges
2. **Decision process:** Who else needs to approve beyond Andrew/Gariashi/Mani?
3. **Timeline pressure:** Is the 3-year timeline firm or aspirational?
4. **Databricks proposals:** What has Databricks already offered for AI acceleration?
5. **Existing AI tools:** Deeper probe on Lutra, Flow effectiveness

### From Sephora:
1. **Team composition:** Who specifically would work on this from BayOne?
2. **Timeline for delivery:** How long to create the agent swarm?
3. **Pricing:** What would this cost?
4. **References:** Who else has BayOne done this for?
