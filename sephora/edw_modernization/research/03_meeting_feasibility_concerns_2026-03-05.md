# 03 - Meeting: Feasibility Concerns and Risk Assessment

**Source:** /sephora/edw_modernization/source/andrew-girishi-meeting1_formatted.txt
**Source Date:** 2026-03-05 (Andrew/Grishi Meeting)
**Document Set:** 03 (Andrew/Grishi Meeting)
**Pass:** Focused deep dive on feasibility concerns and Colin's responses

---

## 1. Context for the Feasibility Discussion

The feasibility concerns emerge in the final third of the meeting (approximately lines 488-599), after Colin has presented his understanding of the EDW modernization, explained the agent swarm concept, walked through schema mapping validation methodology, and discussed deployment infrastructure. Up to this point, both Andrew and Grishi have been engaged and receptive — Andrew called it "really aligned with what we're thinking" (line 426) and Grishi said she "loved what you presented today" (line 488).

The feasibility discussion was not prompted by Colin. It arose organically from Grishi and Andrew independently, each raising a distinct but related concern: Grishi wanted to see agents actually working, and Andrew wanted assurance that agents could technically integrate with their old software and that the investment would actually shorten the timeline.

---

## 2. Grishi's Feasibility Concern: Show Me It Working

### The Ask (lines 488-490)

Grishi framed her concern as wanting evidence, not theory:

> "It would really help me if we could see some kind of a demo or, like, agents that you guys have created or, you know, that has done this kind of job, be ingestion automated this stuff, right? That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working."

This is a pragmatic, execution-oriented concern. Grishi runs the team that is already doing the migration work manually. Her team has already achieved approximately 30% efficiency gains using AI for SQL conversion (line 158), but the remaining process is heavily manual — manually opening Cognos reports, extracting SQL, running it through AI, and pasting the converted SQL back (lines 159-160). She understands the pain of the manual workflow firsthand. Her concern is not whether the concept is sound but whether BayOne can actually deliver working agents that automate this, not just describe them in theory.

### What She Wants to See

Grishi's request is specific: a demonstration of agents that have done "this kind of job" — meaning data ingestion, report processing, and code re-engineering automation. She returned to this point again at the end of the meeting (lines 581-584):

> "I just want to see before we go and spend a lot of time, I wanna see that you guys have done something like this, that done created agents that is capable of doing these kind of things, right? So I think that's something very selfishly, very important for me."

The repetition of "very selfishly, very important for me" signals this is her personal gating criterion. She will not be comfortable proceeding to a deeper engagement without seeing agents in action.

### Colin's Response: Three Options (lines 492-511)

Colin acknowledged the constraint that he cannot show client work directly — "I'm a graphic designer, but I can't show you what I worked on because it belongs to someone else" (line 496). He offered three alternatives:

1. **Case studies** — Written documentation of past work.
2. **POC on Sephora's own data** — A live proof of concept using a representative sample from Sephora's environment. Colin noted this could feed directly into a future SOW, meaning "you're not duplicating effort" (line 502) and "if you don't like it at the end, well, you got something for free out of it" (line 504).
3. **Demo on synthetic data** — Build a demo using BayOne-assembled data to show how the agents work. Colin flagged this as "the safest option, but there is kind of no value add" because any time invested does not directly contribute to real work (lines 507-508).

Colin clearly preferred option 2 (the POC on real data) as the most valuable for both sides.

---

## 3. Andrew's Feasibility Concerns: Two-Part Validation

Andrew's concerns were more technically specific and more fundamentally skeptical than Grishi's. He raised them in a single extended statement (lines 512-532) that constitutes the most critical passage in the meeting for understanding the risk calculus of the Sephora decision-makers.

### Concern 1: Can Agents Even Connect to Our Old Software? (lines 512-523)

Andrew opened with the core technical question:

> "We want to make sure that this concept of, you know, all those little multiple little agents and have an orchestrator kind of, you know, orchestrating the entire flow, is it possible?"

He immediately grounded this in specifics about their software versions:

- **Cognos version:** "Card notes that we have is a very, very old version. We actually, I think it's like a 10.3 or 10.2, something like that. And it's super old version." (lines 514-516). Note: "card notes" is a speech-to-text error for "Cognos."
- **DataStage version:** "Data stage, it's not the latest version either." (line 517). Andrew did not specify the DataStage version number, only that it is not current.
- **Both are on-premises** — confirmed later in the discussion (line 541).

Andrew then articulated the technical constraint with precision (lines 518-522):

> "Even in order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL server for some of that kind of database that you can just easily have the AI to go with, or it has an API endpoint or some sort. Otherwise, your agent, it can be as smart as you can be. It won't be able to connect to that software. Then it's moot point, right?"

This is a well-informed concern. Andrew is not asking whether AI is "smart enough" — he is asking whether there is a viable interface layer between the agent and the legacy software. He identified three possible integration paths:
1. An open SQL Server database backing the application
2. An API endpoint
3. "Some sort" of accessible interface

And he correctly noted that without any of these, the agent's intelligence is irrelevant — "it can be as smart as you can be. It won't be able to connect" (lines 520-521).

### Concern 2: Will Agents Actually Shorten the Timeline? (lines 525-527)

Andrew's second validation requirement:

> "Is it even possible that at the end of the day, having those agents created will definitely shorten our time in terms of the flow, right? So before we really committed to deep dive and create those agents, I think that's the whole point."

This concern addresses the economics of the agentic approach. Andrew is weighing two investments: (a) continuing to spend on manual contractor work for the migration, versus (b) spending upfront to build agents that then parallelize the work. He had articulated this trade-off earlier in the meeting (lines 165-170):

> "Rather than spending that money there, I take the money and resources and spend it upfront to create all these agents so that it will then, once it's all done, then it can parallel run and do all the thing by itself... So then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half."

So his second feasibility concern is whether the upfront agent development investment will actually deliver the timeline compression that justifies it. He is not asking for a theoretical argument — he wants proof before commitment.

### The "Wild Thinking" Statement (lines 528-530)

Andrew's most revealing statement:

> "I just want to make sure that the wild thinking is not wild, it's real, it can be done."

This single sentence encapsulates Andrew's risk calculus. He is explicitly acknowledging that the agentic approach sounds ambitious — possibly too ambitious — and he needs validation that it crosses from "wild thinking" to "feasible reality." The word "wild" appears three times in one sentence, suggesting this is a genuine anxiety, not a rhetorical flourish. Andrew is a decision-maker who has heard AI promises from multiple vendors (he noted earlier they have been "talking this exact same conversation with a lot of different vendor right now" — line 173) and is calibrating between excitement about the potential and skepticism about the delivery.

He also added a scope clarification (lines 530-531): the agents need to handle not just report conversion but also "the data behind the scene. That's the biggest part is to move the data and the table over to from EDW SQL Server to data platform as well." This expands the validation requirement beyond Cognos report re-engineering to include the underlying data migration from SQL Server to Databricks.

### Andrew's Framing of What Evidence He Needs (lines 528-532)

Andrew was explicit that he does not care about the format of the proof:

> "Whether it's a do a little proof of concept here without data or using your own data, you just mark something on the short to us, I need to be honest, I really don't care."

What he does care about:
1. That the agents can actually connect to old software versions (Cognos 10.2/10.3, DataStage, on-prem SQL Server)
2. That BayOne is "absolutely capable of delivering that, knowing that our software version is old" (line 530)
3. That the agents handle "the flow" end-to-end — not just SQL conversion but the full pipeline including data movement

---

## 4. Colin's Response to Andrew's Technical Concerns

### Older Software is Easier to Integrate With (lines 534-538)

Colin's response reframed Andrew's concern about old software as an advantage:

> "The good news with older software, to be honest with you, is the same reason why it gets old is because — I shouldn't say it like this, but I will. It's easier to get into older software. That's the most professional way I can say that."

He explained the reasoning: newer software versions exist partly because of added security. The shift to cloud-hosted software puts everything "behind that smoke screen" (line 538), making programmatic access more difficult. Older, on-prem software lacks those layers of security abstraction.

Andrew immediately validated this logic (lines 540-543):

> "Yeah, that's true."
> "And I'll think it's on-prem. So you're right. From that perspective, it's much easier."
> "Yes. You are actually correct."

This was a significant moment in the meeting. Andrew, who had been in skeptic mode, conceded the point readily. The on-prem nature of their stack, which might seem like a liability, becomes an advantage for agent connectivity because there are fewer security barriers to programmatic access.

### Normal Stack Means More Community Support (lines 547-553)

Colin's second argument: Sephora's tools, while old, are standard enterprise tools — not custom-built internal systems. This matters because standard tools have existing connectors, community documentation, and established integration patterns:

> "The more normal things are, the more support there is, the more likely it is that someone already has made a connector or that we can go back and get an existing connector. So it's actually sometimes better."

He drew a contrast with the worst-case scenario (lines 552-553): "It would be different if you said we had an on-prem thing that our in-house team developed themselves and then didn't look at for 15 years. That would be a way different conversation." The implication is clear — Cognos and DataStage, even at old versions, are IBM products with known architectures, documented APIs, and existing community tooling.

### The Production Server Performance Concern (lines 554-557)

Colin raised a concern that Andrew had not mentioned — production server impact:

> "My only concern would be on speed. And if those things are in production or if they're kind of a staging server, because I also wouldn't want to kill the server if it's production and you need that data to do some business function. And I'm querying it a million times with an agent."

This is notable because Colin proactively identified a risk rather than waiting for Sephora to discover it. If agents are querying on-prem production databases at high frequency, they could degrade performance for business users who depend on those same systems. This is a practical operational concern that demonstrates Colin's awareness of the real-world implications of running agent swarms against legacy infrastructure.

The concern was not resolved in this meeting. Colin flagged it as something that would need to be assessed — whether the target systems are production or staging, and how to manage query load.

### Colin's Personal Experience with Legacy Systems (lines 558-563)

Colin provided a specific anecdote to build credibility:

> "I'll tell you right now we had a version of SQL Server that we were using that made our cybersecurity team literally shut it down behind a virtual net because it was that kind of old that even through VPN it wasn't accessible. But that's what our Oracle instance was on."

This references his prior role at Coherent (a $16 billion revenue company with approximately 40,000 employees, as described at lines 98-99). The anecdote serves dual purposes: (1) it demonstrates Colin has personal experience working with legacy systems that are even more constrained than Sephora's, and (2) it normalizes Sephora's situation — "people don't like to change things and update them. That's a very common scenario because it works now" (lines 560-561).

### Integration Validation as Part of the POC (lines 564-568)

Colin proposed that verifying agent connectivity to Sephora's old software should be an explicit part of the POC scope:

> "If even that is something that would be something good for the POC, that would actually be part of it for me, because that would also be part of the time estimate. So if we positively cannot interact with something, there's no possible way to do it, you're right."

He then added an important credibility statement (lines 567-568): "So we would want to have that confidence on our own, because even if you give us your confidence, and we still can't do it, we're still a fish out of water at that point." This signals that Colin is not just trying to win the deal — he is saying BayOne needs to validate feasibility for their own risk management, not just Sephora's.

---

## 5. The Vendor Landscape Context

Andrew's feasibility concerns do not exist in isolation. He provided important context about the competitive landscape (lines 172-176):

> "I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendor right now. Because I know for a fact, right now outside there's no, no one has a pre, a package that we can just say, hey, I will get, I want to buy your package... so I can just run through this migration without any human involved or even a little human involved."

Andrew's conclusion from vendor conversations: no off-the-shelf solution exists. He described what he wants as someone who "can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing" (line 176). This is custom development, not product procurement.

Colin validated this assessment (lines 187-196, 211-212). He named Palantir as the closest commercial solution but noted it would come "with six zeros attached to the price tag" and would still require manual effort. He then stated directly: "If I had a commercial solution, I could recommend I would tell you right now and skip our involvement, because it's going to be better for both of us. But it doesn't exist" (lines 211-212).

This shared acknowledgment that no off-the-shelf solution exists is the foundation for the feasibility discussion. Both sides understand this would be a custom build, which raises the stakes of the feasibility question — if it is custom, the risk of failure is higher than buying a proven product.

---

## 6. Summary of Software Version Details

| System | Version | Notes |
|---|---|---|
| IBM Cognos | 10.2 or 10.3 | Andrew described as "super old version" (line 516). Speech-to-text renders "Cognos" as "card notes" throughout the transcript. |
| IBM DataStage | Not specified | Andrew said "it's not the latest version either" (line 517). No version number given. This is the ETL tool that moves data from source systems into the SQL data warehouse. |
| SQL Server | Not specified | The current EDW runs on SQL Server (confirmed multiple times). On-prem. |
| Infrastructure | On-premises | Confirmed by Andrew: "I'll think it's on-prem" (line 541). |

Target state systems mentioned in the meeting:
- **Databricks** — Target data platform (speech-to-text renders as "data breaks" in some places)
- **ThoughtSpot** — Target reporting tool for some use cases (replacing SSAS cube / Excel pivot table workflow)
- **Cognos** — Being retained as front-end during transition to minimize change management

---

## 7. Unresolved Concerns After the Discussion

Several feasibility concerns remained open at the conclusion of the meeting:

### Resolved in the Meeting
- **Can agents connect to old on-prem software?** — Colin argued persuasively that older, on-prem systems are actually easier to access programmatically. Andrew conceded the point. However, this remains theoretical until the POC validates it against Sephora's specific environment.

### Explicitly Deferred to POC/Deep Dive
- **Actual connectivity to Cognos 10.2/10.3** — No one tested whether agents can programmatically access Cognos at this version. Colin proposed making this part of the POC (line 565).
- **Actual connectivity to DataStage** — Same situation. The version was not even specified precisely.
- **Whether agents will compress the timeline** — Andrew's second validation requirement. Colin described how agent swarms scale ("the work to take on 100 tables or 100 different reports is about the same as if we were to do 1,000" — lines 478-479), but no quantitative estimate was offered. This would require the technical deep dive and POC to validate.
- **Production server performance impact** — Colin raised this concern but no assessment was made. Needs to be evaluated during the architecture deep dive.

### Not Explicitly Discussed but Implied
- **Data sensitivity and security** — Colin mentioned the POC on Sephora data as an option and Sephora's enterprise AI accounts (Azure, Google Vertex, Claude), but no explicit discussion of data handling, security approvals, or compliance requirements for letting an external vendor's agents access production systems.
- **Agent reliability at scale** — Colin acknowledged that AI-assisted SQL conversion is "hot and cold sometimes. Sometimes it works really, really well. Other times it completely doesn't work" (lines 232-233). The 30% efficiency gain Grishi's team already achieved with manual AI usage (line 158) provides a baseline, but whether orchestrated agents can do substantially better at scale was asserted but not demonstrated.
- **Cost of building the agent swarm versus continuing manual work** — Andrew framed the economics as a trade-off (invest upfront in agents to compress a three-year timeline), but no cost estimate or ROI analysis was discussed.

---

## 8. Agreed Next Steps Addressing Feasibility

The meeting concluded with two concrete next steps directly responsive to the feasibility concerns:

1. **Demo / POC** — Scheduled for the following Thursday (approximately March 13, 2026). Colin would demonstrate agent capabilities. Grishi emphasized this was "very selfishly, very important for me" (line 583). Andrew was open to any format (on their data, on synthetic data, or a general demo) as long as it proves feasibility.

2. **Technical architecture deep dive** — To include Grishi's enterprise architect (name rendered as "my hair" in the transcript — unclear, but the architect's name was to be sent via email). This session would provide Colin with the technical details needed to assess connectivity, performance constraints, and scope for a realistic proposal.

Both next steps are gating — Andrew and Grishi need to see evidence before committing to a deeper engagement, and Colin needs architectural detail before he can make honest estimates.
