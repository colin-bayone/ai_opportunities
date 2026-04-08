# 07 - Demo: Scaling Discussion and Next Steps

**Source:** /sephora/edw_modernization/source/edw_demo_4-2-2026_formatted.txt
**Source Date:** 2026-04-02 (Demo Meeting)
**Document Set:** 07 (The Actual Demo)
**Pass:** Focused deep dive on scaling questions and the next-steps exchange

---

## 1. Andrew's "Day One" Question: The Pivotal Exchange

At approximately 45 minutes into the demo, Andrew Ho asked the question the entire engagement had been building toward. He had watched the full pipeline demonstration, heard Maher's technical interrogation, seen the auto-fix and validation workflows, and listened to the architecture walkthrough. Now he shifted from "what does this do" to "what happens next."

**Andrew (line 888-901):** "I I I was, I was gonna ask exactly the that question. Well in in other words like I was gonna ask you like are you if we if we gonna let's say great you know what they want we like you guys we want to you know have you guys help us in this. This project then what will be really the step one right? Cuz you you talked about this whole you know past one hour talk about you showcase you know this is a prototype you know we're able to help you guys to convert a job from you know a table and job from data stage and then SQL Server to Databricks and a pipeline and then. Like in in reality like if I was like day one, how are you gonna go about it? It sounds like you will probably looks like a run a profiler on our on our SQL server on our data stage and then and also the the Cognos and and then kind of start building up those kind of the. The bad thing and stuff like that, right?"

This is the buying signal the entire demo was designed to produce. Andrew was not asking a hypothetical question. He was framing the conversation as "if we hire you" -- note the language "if we gonna... have you guys help us in this. This project then what will be really the step one." He was already past the question of whether BayOne could do the work; he was asking how the work would start.

Andrew also demonstrated that he understood the exploration concept intuitively before Colin even pitched it. His reference to running a profiler on SQL Server, DataStage, and Cognos, then "building up those kind of the... bad thing" (likely "mapping," distorted by speech-to-text) shows he had internalized the knowledge graph concept from earlier in the demo and from the prior meetings. He was completing Colin's pitch before Colin delivered it.

**Colin (line 903):** "Sir, I think I preempted you."

Colin had a slide or document ready for this exact moment. The pre-demo strategy document explicitly planned for this exchange: "Do NOT pitch this during the demo. Let the demo land first. After the demo, when they ask 'what is the next step?' (and they will)..." The question came exactly as anticipated.

---

## 2. Colin's Two-Week Exploration SOW Pitch

Colin responded to Andrew's question with a structured proposal, delivered conversationally rather than as a formal pitch. This was consistent with the pre-demo strategy of keeping it conversational and not handing them a proposal document during the demo.

**Colin (line 912-916):** "I I tried my best. I I always listen. So my exactly that I I'd say you know maybe you know what I would propose for this cause at the end of the day we'll have to do a scoping for you right? Cause we'll have to say yes we can do this, yes we can help, but here's how long it would take. Here's so much the effort would be and eventually."

**Colin (line 920-921):** "You know that that ultimate decision of not just can we do this, but is this going to work for everyone? So what I was going to propose is, you know, kind of a two week, you know, SOW that can go on and at the end of that the objective would be to have both of these things done."

### What Colin Proposed

**Colin (line 925-928):** "One, you know, understand the full landscape of everything. So we did, you know, this one part, but absolutely right. There's still more to this and we wanna help you as much as we can, as much as you want us to help. We'll we'll take whatever we can get here, but at the same time."

**Colin (line 929-943):** "You know, wherever it's the most value added for you, a guided discovery to understand exactly what we can do and map out not just the databases, but our approach. This one, I said 8 hours. I don't really mean 8 hours. It's more however many people involved, you know, how much time they have. I always say a week for that because not everyone's available all the time. After that, once we have some access, we would build that comprehensive graph for you, classify all the pipelines, identify how we can accelerate this because we'll be able to have a pretty high level overview of patterns and what is. You know the outlier here, and at that point we'll have a good idea of the scope. You know, how much time will this take us? You know, what can we accelerate that we're very confident in? What are we a little bit risky about? That way we'll get a good idea of specifically what the full scope would look like, and at that point we can break it up into smaller. SOWS or we can do one giant thing, whatever is the most agreeable. I know when we were talking to Mani, he he wanted to talk about a couple of different models. Um, so we can talk about that as well."

### How the Pitch Compared to the Pre-Demo Plan

The pre-demo strategy document (`post_demo_next_steps_strategy_2026-04-02.md`) defined the exploration SOW as:

- **Week 1:** Discovery meetings with Sephora's technical team (~8 hours), paced by their availability
- **Week 2:** Autonomous mapping and analysis (~20 hours + 2 hours buffer), building the knowledge graph and dependency map
- **Deliverable:** Complexity mapping, Cognos MCP validation, table migration assessment, and a data-driven engagement proposal

What Colin actually said in the demo tracked closely to the plan but was softer in specifics:

| Planned Element | What Colin Actually Said | Match |
|----------------|--------------------------|-------|
| Two-week timeline | "Kind of a two week, you know, SOW" | Direct match |
| Week 1: ~8 hours of guided discovery | "A guided discovery... I said 8 hours. I don't really mean 8 hours. It's more however many people involved... I always say a week for that" | Match, with a humanizing hedge about the 8-hour number |
| Week 2: Autonomous mapping and classification | "Build that comprehensive graph for you, classify all the pipelines, identify how we can accelerate" | Direct match |
| Deliverable: Data-driven engagement proposal | "At that point we'll have a good idea of the scope... what the full scope would look like, and at that point we can break it up into smaller SOWs" | Direct match |
| Reference to Mani's engagement model request | "I know when we were talking to Mani, he wanted to talk about a couple of different models" | Direct match -- anchored the SOW to what Mani had already blessed |
| Cognos MCP validation | Not mentioned during this exchange | Not raised -- Colin kept the pitch focused on the discovery arc rather than introducing a technical detail |
| Pricing / cost | Not mentioned | Correct per strategy: "Do not frame it as 'paying for a proposal'" |

Colin did not mention the exploration SOW's cost structure, the request for read-only system access, or the specific number of hours. He also did not mention Cognos MCP validation, which was a planned deliverable. This was the right call for the moment -- the question was about "step one," not about scope and pricing. Those details belong in a follow-up conversation.

The one element Colin added that was not in the written plan was the explicit mention of Mani. By referencing the conversation with Mani about engagement models, Colin reminded Andrew that his boss had already been part of this discussion and had expressed a preference for flexibility. This is a subtle but important anchoring move: it signals to Andrew that there is already organizational alignment above him.

---

## 3. Andrew's Scaling Questions: The Full Exchange

After Colin's exploration SOW pitch, Andrew shifted to the scaling question. This was a two-part inquiry: (1) can the system run in parallel across multiple business areas simultaneously, and (2) can it scale from a pilot to full production?

### Part 1: Parallel Execution Across Business Areas

**Andrew (line 944-950):** "OK, coming back, sorry, go back to that that technical part of the question. So what you showed us, right, if and I'm I'm trying to think of it as a in the in the more grand schema we have of of course. Lots of tables, lots of ETL jobs, lots of reports, right? So the the process that the the flow that you've shown today, I'm assuming that it it's it's not just like a one or two report at a time or one or two tables at a time like you know it's it can scale."

Andrew was testing a critical assumption: that the demo they just watched -- which processed one pipeline -- was not the system's ceiling. He was asking whether the system could handle the full scope of Sephora's EDW migration, which includes (from prior meetings) 6,000+ reports, 8 SSAS cubes, 800+ KPIs, 300 dimensions, and 20 source systems.

### Part 2: Cognos Business Area Structure

**Andrew (line 956-968):** "And run in parallel with multiple tables, multiple reports or and or if I want to for example if we want in in our Cognos side right we are it it all separated by folder by subject business area, finance folder, we have merchandising folder, we have you know .com. And of course in the back end, the EDW database, the SQL Server and also the data stage server. We don't separate it logically by business. It's all like one in a database. The SQL Server is 1 schema for the entire EDW and then in the data stage it's like bunch of job all the job in. In in like maybe one or two a couple folders and but they are not really break it down by uh business area per se right."

This is a critical piece of architectural intelligence that Andrew volunteered:

1. **Cognos is organized by business area** (folders: Finance, Merchandising, .com, etc.)
2. **SQL Server EDW is a single schema** -- it is not partitioned by business area. One monolithic schema for the entire enterprise data warehouse.
3. **DataStage jobs are loosely grouped** -- one or two folders, not cleanly separated by business area.

The implication: the logical separation that would make a pilot easy (pick one business area and convert it) exists cleanly only on the Cognos side. On the SQL Server and DataStage side, the jobs and schemas are entangled. A "finance pilot" in Cognos would require identifying which SQL Server tables and DataStage jobs feed the finance reports -- exactly the kind of dependency mapping the exploration SOW is designed to produce.

### Part 3: Pilot-to-Full-Scale Path

**Andrew (line 969-981):** "So so how do I and I'm assuming that your flow and and your processes it it's gonna allow us to if I want to tackle. Maybe the first thing is, OK, run a pilot, just pick one business area and then you convert that, you know, make that happen, right? Then once we've proven that this is really it works, it it it, you know, it save us, you know, I don't know whatever percentage of the time. And then now we're like, OK, I want to run it full scale. And it can be deployed to a run it in multiple in parallel in multiple business subject area in parallel. Am I am I correct? I just want to make sure that this is not like you know you still have to have a person you know feeding couple report at a time and run through the whole process and then do all that validation."

Andrew articulated the exact engagement arc that BayOne had been planning: pilot one business area, prove it works, then scale to all business areas in parallel. But he added a critical clarification at the end: he wanted confirmation that scaling does not mean "a person feeding a couple reports at a time." He was asking whether the system can operate without being bottlenecked by human throughput.

**Andrew (line 988-990):** "It's not that, right? That's definitely right. OK."

Andrew answered his own question -- he had already concluded that it could scale -- and was seeking confirmation rather than asking from uncertainty.

---

## 4. Colin's Scaling Explanation: Compute, FastAPI, Celery, and the Orchestrator of Orchestrators

Colin's response to Andrew's scaling questions was the most technically detailed scaling explanation he gave to the client during the entire engagement.

### The Compute Constraint

**Colin (line 992-996):** "Yeah. Right, absolutely. So let me, I'll explain the kind of levers you have to pull on. The first thing is, yes, the exclusive thing that we are constrained by in terms of parallelism is the compute. So basically that is determined exclusively by."

Colin started by being transparent about what actually limits scaling: compute resources. Not architecture, not software design, not human availability. The only constraint is how much Azure compute they want to provision.

### FastAPI Is Lean -- The Heavy Lifting Is in Foundry

**Colin (line 1000-1003):** "Effectively what you want for this fast API. That's why I brought up workers because fast API. This is already pretty lean because really the only heavy lifting is not even happening here, it's actually happening in Foundry. So those language model calls."

This is a critical architectural point. The FastAPI server -- the thing BayOne actually deploys and maintains -- is not doing the compute-intensive work. It is orchestrating: routing requests, running deterministic checks, managing state. The expensive computation (large language model inference) is happening in Azure AI Foundry, which is Microsoft's managed infrastructure with its own scaling capabilities. This means the scaling bottleneck is not BayOne's code; it is the Azure AI Foundry quota, which Sephora controls and can increase.

### The $20/Month Worker Cost

**Colin (line 1007-1011):** "Realistically, in fast API, we're running some very quick Python scripts. There's no throttling that I can see with something that's a reasonably equipped container app instance. So this is something that you're probably not gonna get bottlenecked by, but if you did, all you'd do is set up Celery, set up workers that would increase your cost marginal. We're talking when I say cost, we're talking probably an extra $20.00 a month to run the service for the duration that it's online. So $20 Max is the ceiling and then you could, you know, it's just a matter of how much you want to scale."

Colin gave a specific cost number: $20/month for additional Celery workers. This is a deliberately low number designed to remove cost as a scaling objection. The implication: scaling the system from one pipeline at a time to N pipelines at a time costs almost nothing in infrastructure terms. The real cost is the Azure AI Foundry compute (the language model inference), which is a Sephora-managed cost that they already have budget for.

### Maher's Database Confirmation

**Maher (line 1018-1019):** "That's why you were mentioning that the database, if we have a, you know the scalable database, then it'll be much better than having container running inside the Azure Container apps, right?"

Maher confirmed he understood the architecture: a scalable database (Postgres vs. SQLite) improves performance and persistence at scale. This was a follow-up to his earlier database questions (lines 509-563) and showed he was tracking the scaling implications.

### Redis and the Full-Scale Architecture

**Colin (line 1022-1029):** "Both in terms of performance and persistence. So if you and the other one that would come in if you really wanted to take the training wheels off of this is throw Redis into the mix. Redis again does add on some cost. It's about $30 a month when you deploy an Azure at this. What would you need for this? This tier, but at that point you have, if you wanted to say once we have some confidence, if you wanted to say do everything today, there's not really a reason why we couldn't do that."

Colin laid out the "no training wheels" architecture: FastAPI + Celery workers + Redis + scalable database. Total additional infrastructure cost: approximately $50/month (FastAPI workers at ~$20 + Redis at ~$30). At that point, the system can process all business areas simultaneously.

### The "Orchestrator of Orchestrators" Concept

**Colin (line 1030-1041):** "It's just a matter of this first step. A really easy way to think is to say. Imagine there's one more layer above this that is the orchestrator of the orchestrators. And imagine this just takes this, copies and pastes it up above and says do all these in parallel with each other this and then at the human end of it you would just see your dashboard view at the end. Which would be a collective of all these things across reports. So yeah, so scaling, no problem. This is built to be concurrent as much as the compute has appetite for. We'll say that."

This is the most important conceptual framing of the entire scaling discussion. Colin described a hierarchical orchestration model:

- **Level 1 (what the demo showed):** A single orchestrator managing the conversion pipeline for one business area or one set of related files. This orchestrator routes files to parsers, manages gates, handles SQL generation, and produces the deliverables.
- **Level 2 (the "orchestrator of orchestrators"):** A meta-orchestrator that takes the Level 1 pipeline and replicates it across all business areas simultaneously. Each business area gets its own Level 1 orchestrator running in parallel. The meta-orchestrator collects results from all of them into a single dashboard view.

The phrase "copies and pastes it up above" is deliberately simple. Colin is saying: the system you just saw for one pipeline is a building block. To run 20 business areas, you stack 20 of those building blocks and run them concurrently. The architecture does not change. The pipeline logic does not change. Only the compute allocation changes.

The closing statement -- "This is built to be concurrent as much as the compute has appetite for" -- is the definitive answer to Andrew's question. There is no architectural ceiling. The ceiling is how much Azure compute Sephora wants to allocate.

---

## 5. Andrew's Closing Statement and What It Signals

**Andrew (line 1043-1048):** "Cool. Great. I know. I think some of us need to hop off. We're not a meeting right now, but this is great. Thank you. We appreciate it. You know, it's good to see it's actually running."

The phrase "it's good to see it's actually running" is significant. It directly echoes the demo demand from Set 03, where both Andrew and Grishi said they needed to see a working demonstration before committing. Andrew just confirmed that the demo satisfied that requirement. He did not say "interesting concept" or "we'll think about it" -- he said it was "good to see it actually running," which is validation language, not evaluation language.

**Andrew (line 1054-1057):** "Yeah, very, very nice. Thank you very much for for for your time, Colin. Well, yeah. So Girishi, Mahay and I and you know we're and Vishal, we we're gonna, you know go back and we'll we'll discuss this further and then we'll we'll let's figure out what's the next steps."

### Parsing Andrew's Closing

Several elements of this statement are worth extracting:

1. **"Very, very nice."** Doubled superlative. Andrew is not a person who uses inflated language casually -- across four meetings, his communication style has been direct and measured. "Very, very nice" is genuine enthusiasm, not politeness.

2. **"Grishi, Maher... and Vishal."** Andrew named the three people he is going to deliberate with. This is the decision-making group. Notably absent from this list: Mani (who is Andrew's boss and the VP), Malika (the enterprise architect), and Sergey (the technical lead). The deliberation is happening at Andrew's level with his direct team and the Xebia consultants, not escalated to Mani. This suggests Andrew has decision authority for the next step, or at minimum the authority to recommend it.

3. **"We're gonna go back and discuss this further."** Standard post-demo language, but the "further" is meaningful. It implies there is already a discussion in progress -- they are continuing a conversation, not starting one. This is consistent with the engagement being at an advanced stage.

4. **"Let's figure out what's the next steps."** Plural "next steps." Andrew is not saying "we'll get back to you" (passive). He is saying "let's figure out what's next" (active, collaborative). The framing includes BayOne in the next-steps determination -- "let's" not "we'll."

### What This Signals for the Deal

Andrew's closing is a positive signal. He acknowledged the demo worked ("it's actually running"), expressed enthusiasm ("very, very nice"), named a deliberation group (indicating a structured next step internally), and used collaborative language about next steps. He did not raise any concerns, objections, or follow-up questions. He did not ask about pricing. He did not ask about alternatives.

The absence of questions is itself a signal. At the end of the Set 03 meeting, Andrew had multiple follow-up requests (demo, deep dive, architecture session). At the end of this demo, he had none. This suggests the demo answered the outstanding questions from Set 03.

---

## 6. Neha and Zahra's Follow-Up Offer

**Neha Malhotra (line 1066-1068):** "Thank you. Hi, Andrew and Grishi. If you guys want to set up some time tomorrow, if you have any questions, you know that come up and include them in that session, we have time tomorrow as well."

**Zahra Syed (line 1077-1078):** "And then real quick, Andrew and Grishi, if you guys want to set up some time tomorrow, if you have any questions, you know that come up and include money in that session, we have time tomorrow as well. Let us know."

Both Neha and Zahra made essentially the same offer simultaneously (or in very close sequence -- the timestamps overlap at 00:53:47-48). The offer was specific: time tomorrow (April 3), with the invitation to include Mani ("money" in Zahra's speech-to-text is almost certainly "Mani"). This is a deliberate move to maintain momentum and prevent the post-demo deliberation from going cold.

The fact that both made the same offer suggests this was coordinated -- BayOne's account team had agreed in advance to offer immediate follow-up time. This is standard account management practice after a high-stakes demo: do not let the client go dark for a week.

**Andrew (line 1080-1083):** "OK, we'll we'll let you know. Cool. Thank you. Bye."

Andrew did not commit to the follow-up but did not decline it either. "We'll let you know" is neutral -- it preserves optionality. His sign-off was warm ("Cool. Thank you. Bye.") but did not include a time commitment.

---

## 7. What Maher, Grishi, and Vishal Said About Next Steps

### Maher Burhan

Maher did not make any closing statement about next steps. His last substantive contribution was a "thank you" at line 1070-1071: "Thank you. Thank you, Paul." (The "Paul" is likely speech-to-text distortion of "Colin" or "all.") Throughout the demo, Maher was the most active technical questioner -- he drove the validation methodology discussion, the Azure deployment architecture discussion, the auto-fix workflow, and the database choice. His silence at the close suggests satisfaction rather than reservation: he had asked his questions and received answers.

### Grishi (Gariashi Chakrabarty)

Grishi said only "Thank you all" at line 1064. This is minimal, but context matters. In Set 03, Grishi was the one who most forcefully demanded a working demo and said it was "very selfishly, very important for me." She saw the demo. She did not express further skepticism or additional requirements. Her single statement of thanks, while brief, is the absence of the concerns she had previously raised.

### Vishal Sharma

Vishal did not make a closing statement. His last contribution was at line 702-703: "Great, great. And last question about is there any way you guys support data reconciliation?" followed by the reconciliation discussion. Vishal's questions during the demo were probing and specific (FastAPI orchestration, XML parsing coverage, future platform lock-in, data reconciliation), and Colin addressed each one. Vishal's silence at the close, like Maher's, suggests his questions were answered.

---

## 8. Complete Cast Behavior in the Scaling/Next-Steps Section

| Person | Role | Behavior During Scaling Discussion | Closing Statement |
|--------|------|-----------------------------------|-------------------|
| Andrew Ho | Director / Decision-maker | Asked the "day one" question, asked scaling questions, confirmed understanding | "Very, very nice... we're gonna go back and discuss this further and then figure out next steps" |
| Colin Moore | BayOne / Presenter | Pitched two-week exploration SOW, explained compute scaling, described orchestrator of orchestrators | "I'll send you over the documents too. Hopefully you enjoyed today." |
| Maher Burhan | Xebia Consultant | Confirmed database scaling understanding, asked about Redis architecture | "Thank you. Thank you." |
| Grishi (Gariashi Chakrabarty) | Data Engineering Lead | Silent during scaling discussion (her questions were earlier, about schema and reconciliation) | "Thank you all." |
| Vishal Sharma | Xebia Consultant | Silent during scaling discussion (his questions were earlier, about FastAPI, parsing, reconciliation) | None |
| Malika Seth | Enterprise Architect | Silent during scaling discussion (her questions were earlier, about parser routing and data mapping) | None |
| Neha Malhotra | BayOne Account Team | Silent during scaling discussion | Offered follow-up time tomorrow |
| Zahra Syed | BayOne Account Team | Silent during scaling discussion | Offered follow-up time tomorrow, including Mani |

---

## 9. Overall Tone at Closing

The closing tone was **unambiguously positive**. Several markers:

1. **No unresolved objections.** Every technical question raised during the demo received an answer. Maher's validation methodology questions, Vishal's XML parsing and platform lock-in concerns, Grishi's schema mismatch question, Malika's parser routing question -- all were addressed. No one left a question hanging at the end.

2. **No skepticism expressed.** In prior meetings (especially Set 03), there was explicit skepticism: Grishi saying "I just want to see before we go and spend a lot of time" and Andrew questioning whether agents could connect to old Cognos. Neither expressed any skepticism in the closing of this demo.

3. **Action-oriented closing language.** Andrew said "figure out what's the next steps," not "we'll think about it" or "we'll get back to you." Neha and Zahra immediately offered follow-up time the next day. The conversation ended with forward momentum, not with a pause.

4. **Andrew's doubled superlative.** "Very, very nice" is stronger language than Andrew used at the close of any prior meeting. In Set 03, his closing was more measured. In Set 04, his closing was more directive (requesting the demo). Here, he expressed genuine appreciation for what he saw.

5. **"It's good to see it's actually running."** This validates the demo's core purpose. The demo was demanded as proof of capability (Set 03). Andrew confirmed it delivered that proof.

6. **No pricing discussion.** Andrew did not ask what the exploration SOW would cost. He did not ask about rates. He did not raise budget constraints. This is either because pricing is Mani's domain (and Andrew does not need to address it at this level) or because the demo was convincing enough that cost was not the immediate concern. Either interpretation is favorable.

The one neutral-to-ambiguous signal was Andrew's response to Neha/Zahra's follow-up offer: "We'll let you know." This is not a decline, but it is not a commitment either. It suggests Andrew wants time to deliberate with his team before re-engaging with BayOne, which is a normal and healthy buying signal. Buyers who are not interested say "we'll be in touch" and disappear. Buyers who are interested say "we'll let you know" and come back within days.

---

## 10. The Exploration SOW as the Next Gate

The demo meeting established a clear path forward:

1. **Andrew's internal deliberation** with Grishi, Maher, and Vishal to process what they saw and align on appetite.
2. **A follow-up conversation** (potentially the next day, per Neha/Zahra's offer, or within the coming days) to discuss next steps.
3. **The exploration SOW** as the defined next step, already pitched by Colin and implicitly accepted by Andrew's lack of pushback.

The exploration SOW is positioned perfectly because it is the logical answer to the gap Andrew himself identified. Andrew asked "what is step one?" and Colin answered "a two-week exploration." Andrew then asked "can it scale?" and Colin answered "yes, but to give you accurate numbers, we need to see the full landscape." Both answers point to the same conclusion: the exploration is the necessary next step regardless of which question you start from.

What remains to be resolved:
- **Pricing and commercial terms** for the exploration SOW (not discussed in the demo, appropriately)
- **Whether Mani needs to approve** the next step or whether Andrew has authority to proceed
- **Timeline for access provisioning** (Sephora granting read-only system access to BayOne)
- **Which business area for the pilot** (Andrew mentioned Cognos business areas: Finance, Merchandising, .com -- the exploration would identify the best candidate)

---

## 11. Key Architectural Details Revealed by Andrew

Andrew's scaling questions incidentally revealed architectural details about Sephora's environment that were not previously documented in the research library:

1. **Cognos is organized by business area folders:** Finance, Merchandising, .com, and others. This is the logical partitioning that would define pilot boundaries.

2. **SQL Server EDW is a single schema:** "The SQL Server is 1 schema for the entire EDW." This means there is no clean way to extract just the finance-related tables without dependency analysis. The exploration SOW's knowledge graph would map these dependencies.

3. **DataStage jobs are loosely organized:** "Bunch of job... maybe one or two a couple folders... they are not really break it down by business area per se." DataStage job grouping does not mirror the Cognos business area structure. Mapping DataStage jobs to Cognos business areas requires cross-referencing which jobs feed which reports -- again, exactly what the exploration phase is designed to do.

These details strengthen the case for the exploration SOW: the pilot that Andrew wants to run ("pick one business area and then you convert that") requires first understanding which SQL Server tables and DataStage jobs belong to that business area. Without the exploration, picking a pilot is guesswork.

---

## 12. Comparison to Prior Meetings' Closing Dynamics

| Meeting | Closing Tone | Key Closing Signal | What Came Next |
|---------|-------------|-------------------|----------------|
| Set 01 (Mani) | Warm, exploratory | Mani requested follow-up with his team | Set 02 meeting with expanded group |
| Set 02 (Mani) | Supportive, directive | Mani requested three engagement model options | Set 03 meeting with Andrew/Grishi |
| Set 03 (Andrew/Grishi) | Interested but gated | "Show me a demo before I commit" | Demo development sprint |
| Set 04 (Technical deep dive) | Technically engaged | Demo scope and timeline agreed | Demo date set |
| **Set 07 (Demo)** | **Enthusiastic, action-oriented** | **"Very, very nice... figure out next steps"** | **Exploration SOW negotiation (expected)** |

The demo closing is the strongest positive signal of any meeting in the engagement. Each prior meeting ended with a gate ("show me X before I proceed"). This meeting ended without a new gate -- Andrew did not ask for another demo, another meeting, or another proof point. He said "let's figure out what's the next steps," which implies the evaluation phase is complete and the planning phase is beginning.
