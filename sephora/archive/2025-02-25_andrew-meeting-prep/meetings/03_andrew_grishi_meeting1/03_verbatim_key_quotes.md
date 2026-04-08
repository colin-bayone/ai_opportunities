# Meeting 3 - Verbatim Key Quotes

## Overview

Exact quotes from the meeting transcript, organized by theme. All transcription corrections have been applied.

---

## Pain Points

### SSAS to Databricks Connector (Gariashi)
> "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management. We have these aggregated tables in form of cubes, but we have an Excel pivot table that's feeding data from those SSAS cubes, and business just drags and drops those KPIs, so they love the Excel view. Now SSAS doesn't have a connector to Databricks where we can retain that, so we want to run some POCs so that the change is minimal."

### Current Workaround Problem (Gariashi)
> "How we are currently approaching the problem is we move all the data, all the aggregated layer onto Databricks, and we make it accessible through ThoughtSpot. We give the KPIs and they just access it. But then they have to change from Excel to ThoughtSpot, which is two different UIs, two totally different look and feel. So that is our biggest point."

### Agent Automation Need (Gariashi)
> "We want to ideally have an agent that would integrate with Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks. Similarly, we have DataStage tool, which is the ETL tool that grabs data from different sources and dumps it into our SQL data warehouse. So we would want an agent to go integrate with DataStage, read all that and re-engineer code automatically on Databricks."

### Current Manual Process (Gariashi)
> "Now we are picking all the, we are going to each job and getting it, getting an XML, feeding it and checking, getting the re-engineered code and then feeding onto Databricks. So those are the two things is a challenge."

---

## Agent Swarm Vision

### Andrew's Orchestration Concept
> "Can we, you know, is there a way we can create multiple agents, small little agents that can do all this little step by step for us, and they have a big orchestration kind of agent that orchestrates this entire flow? So then, rather than spending money on manual, you know, at the end of the day, we still need to spend the money, you know, in a contractor to do the manual work. Rather than spending that money there, I take the money and resources and spend it upfront to create all these agents so that it will then, once it's all done, then it can parallel run and do all the thing by itself."

### Timeline Ambition (Andrew)
> "So then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half, or something like that."

### Current AI Efficiency (Andrew)
> "The efficiency gain that Gariashi and the team had figured out was about 30%, okay? Now, as you kind of imagine, we still have a lot of manual intervention that needs to happen throughout that process. You still have to manually go to Cognos, and then open the report, then take the SQL out, and then run through the AI, spit out the new SQL, then you have to manually snap it back to the Cognos."

---

## Competitive Landscape

### Andrew's Transparency
> "I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendor right now. Because I know for a fact, right now outside there's no, no one has a pre, a package that we can just say, 'Hey, I will get, I want to buy your package or I want to pay something to get your package in so I can just run through this migration without any human involved or even a little human involved.'"

### What They're Looking For (Andrew)
> "So now I'm just kind of poking a hole and saying, who out there can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing?"

---

## Demo Requirement

### Gariashi's First Ask
> "It would really help me if we could see some kind of a demo or agents that you guys have created or, you know, that has done this kind of job, be ingestion automated this stuff, right? That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working. That is something I would love to see."

### Gariashi's Emphasis
> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this, that done created agents that is capable of doing these kind of things, right? So I think that's something very selfishly, very important for me."

---

## Technical Feasibility

### Legacy Software Concern (Andrew)
> "What I don't know is whether, because of our version of the software, for example Cognos that we have is a very, very old version. We actually, I think it's like a 10.3 or 10.2, something like that. And it's super old version. DataStage, it's not the latest version either. And so what I don't know is whether... in order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL server for some of that kind of database that you can just easily have the AI to go with, or it has an API endpoint or some sort. Otherwise, your agent, it can be as smart as you can be, it won't be able to connect to that software. Then it's moot point."

### On-Prem Advantage (Andrew)
> "And I think it's on-prem. So you're right. From that perspective, it's much easier."

---

## Colin's Approach

### Being the Skeptic
> "I'm always the skeptic. I think probably that's what I can give you. Instead of being the AI guy that says we can do anything at any time, I'm certainly not that person."

### On Commercial Solutions
> "Probably from a commercial solution standpoint, closest solution, which still would involve manual effort and still would be probably prohibitively expensive, to be honest, is Palantir. If you've ever gotten a demo from them, they'll come and say, you know, we can do these migrations. You don't even have to change anything... The problem is that's also going to come with six zeros attached to the price tag. And there is still always that manual effort that's involved."

### Agent Specificity
> "Agents in general work better if they're more specific. So if you try to have, you know, a small subset of agents that, this is my reports agent. No, no, no. Here's the reports validator agent. Here's the one that checks the past state and the present state, just as two small examples. The more specific you go with agents without going overly specific, the better off you are."

### Judge Agent Pattern
> "There is an agent that is the orchestrator. He's not the only one though. So there's an orchestrator agent there, but there's also a judge. And the judge and the orchestrator have to be in sync. The judge, I call him like the grumpy old man agent, kind of yells at everyone, stay on track, follow this workflow, do not deviate. If it deviates, it rejects immediately and lives back."

### On Schema Mapping Process
> "We actually stay away from AI until we have to. The reason for that is the higher up in the food chain AI gets implemented in, the more kind of telephone effect happens. So if you can wait to use AI until a little bit later in the process, it works better."

### MCP for Tool Integration
> "On the actual tool integration part, that becomes more of an MCP problem than an agent problem, because you want to get all these different tools connected. Agents can definitely do that. But agents combined with MCP to actually interact with those utilities and tools is much better because it's more reliable."

### Framework Choice
> "Even for us, that would be LangGraph. We do something custom with LangGraph, something that scales. That's much better than just trying to do it in Claude Code. Claude Code can get you pretty far, but with 6,000 odd reports. That's pretty tough to do and tough to do consistently."

---

## Infrastructure & Delivery

### "Meet You at Your Home" (Colin)
> "My language, I like to say, I'll meet you at your home. So we don't want to force you into using another tool. You're already getting another tool... For us, it would be built on your infrastructure if that is desired. If you tell us, though, you want us to build it off on ours and bring it to you, we can do that as well. But first preference is to build it on yours."

### Working on Client Hardware (Colin)
> "We can follow kind of all the organizational rules, I can say. So, for instance, for other clients that we work with, we use everything that's approved from their IT department or even working on their hardware. We have laptops that are issued and physically have their image on it, even just for the development itself."

### Cost Optimization (Colin)
> "If you're on Azure, for instance, you have Azure AI Foundry. So then you even have another level of sophistication there because everything with Azure AI Foundry is just as secure as when you use Outlook as one example. So using Azure AI Foundry models are way cheaper as well than their commercial API counterparts."

### Legacy Software Advantage (Colin)
> "The good news with older software, to be honest with you, is the same reason why it gets old is because... it's easier to get into older software. That's the most professional way I can say that... the more normal things are, the more support there is, the more likely it is that someone already has made a connector or that we can go back and get an existing connector."

---

## Semantic Layer

### Gariashi on Tool Agnosticism
> "That is the ideal state, right, that we are looking for so that the semantic layer stays common between all these different reporting tools. Cognos, ThoughtSpot, cubes that will be migrated to, you know, ThoughtSpot or whichever tool is efficient, right? So that we can use these common semantic layer, feed all these tools. We want to stay tool agnostic so that whichever tool we use, we just point it to the same data set."

### On KPI Consistency (Gariashi)
> "And the KPIs that they are showing is... we don't have questions on, oh, this is something different. That's something different. It's the same KPI. It's coming from different tables, and it's updating at different times."

### Colin on Semantic Layer Importance
> "Semantic layer... that's kind of the glue that holds everything together. So that's a really good thing to prioritize. It's a very tough thing to do retroactively. Because once the reports are out there, now you have to again, kind of do the exact same extent of effort to kind of bring them all into one place."

### AI/BI Alignment (Colin)
> "AI needs to speak the same language as the reports because those phone calls you get whenever the company chatbot came back with different reporting numbers than the actual report on the screen is a big problem. So having that harmonization between the two is good."

---

## Engagement Model

### Three Tiers (Colin)
> "Type one, where you're pretty much doing this ourselves. We give you a big chunk of work, we give you requirements, you deliver on it, and that's that. Type two, which to me is the best type, and I think the healthiest type, even from an org standpoint, is kind of a partner. Where we're doing a lot of the work, we're taking care of that AI load, but we're also at the same time kind of working alongside your team to help them understand what we're doing. So we're not doing this in a vacuum, there's not secret sauce to this. It's you're kind of getting people that are now upskilled as a result."

### On Pure Staffing (Colin)
> "In type three would be pure staffing, where we just hand you off people that we know can do the work. That one is my least favorite because I can't control that. After it happens, can give you the best people, but it's almost like the Olympics a little bit. Who saw USA winning that? I didn't. So sometimes the right team with the right leader can result in amazing outcome. But I've also seen things totally fall on their face if you have an amazing team, but maybe the direction isn't perfectly clear."

---

## Closing Energy

### Zahra's Wrap
> "We're super excited. Super, super excited."

### Andrew on Next Steps
> "Next step, probably we have maybe one more just to kind of give that session in terms of architecture. And even, Gariashi has an enterprise architect working for her right now that have been laying out architecturally, in terms of the data migration."
