# Speaker Notes: Andrew Ho & Grishi Chakraborty Meeting

## Grishi Chakraborty (Director, Data Engineering / BI & Analytics)

### Role in Meeting
Primary technical voice. Most engaged participant on Sephora side. Drove the pain point discussion and articulated specific technical requirements. Expressed clear need for confidence-building through demo.

### Topics Owned
- SSAS to Databricks connector challenge
- Agent automation requirements
- Technical feasibility concerns (legacy software versions)
- Demo/POC requirements

### Key Quotes

**On biggest pain point:**
> "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management. We have these aggregated tables in form of cubes, but we have an Excel pivot table that's feeding data from those SSAS cubes, and business just drags and drops those KPIs, so they love the Excel view."

**On agent needs:**
> "We want to ideally have an agent that would integrate with Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks."

**On current manual process:**
> "Now we are picking all the, we are going to each job and getting it, getting an XML, feeding it and checking, getting the re-engineered code and then feeding onto Databricks. So those are the two things is a challenge."

**On schema mapping interest:**
> "I'm a little interested in the schema mapping validation. Where it maps, like, how does it automate? Like, what is the process? How does it do it?"

**On existing AI usage:**
> "We have done this mapping using Claude. The only thing that we're figuring out is that there is a manual intervention, right? We have to feed it the schema and then whatever we are looking for... it's not 100% accurate."

**On legacy software concern:**
> "What I don't know is whether, because of our version of the software, for example Cognos that we have is a very, very old version. We actually, I think it's like a 10.3 or 10.2, something like that. And it's super old version. DataStage, it's not the latest version either."

**On demo requirement (CRITICAL):**
> "It would really help me if we could see some kind of a demo or agents that you guys have created that has done this kind of job, be ingestion automated this stuff. That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working. That is something I would love to see."

> "I just want to see before we go and spend a lot of time, I want to see that you guys have done something like this, that done created agents that is capable of doing these kind of things. That's something very selfishly, very important for me."

**On infrastructure preference:**
> "I would say, I do ideal would be like my ideal would be Databricks, right? I don't want to add too many things if you have it on Databricks."

### Commitments Made
- Will include Mahair (enterprise architect) in next meeting
- Will participate in architecture deep dive

### Sentiment
Engaged, technically curious, appropriately skeptical. Wants proof before commitment. Direct about what he needs ("very selfishly, very important").

---

## Andrew Ho (Sr. Director, Marketing AI & Enterprise Reporting)

### Role in Meeting
Strategic voice. Articulated the big-picture vision for agent swarms and timeline compression. Transparent about competitive landscape and budget thinking.

### Topics Owned
- Agent swarm orchestration vision
- Competitive landscape transparency
- Timeline ambitions
- Decision-making on next steps

### Key Quotes

**On agent vision:**
> "Can we, you know, is there a way we can create multiple agents, small little agents that can do all this little step by step for us, and they have a big orchestration kind of agent that orchestrates this entire flow?"

**On spending philosophy:**
> "Rather than spending money on manual, you know, at the end of the day, we still need to spend the money, you know, in a contractor to do the manual work. Rather than spending that money there, I take the money and resources and spend it upfront to create all these agents so that it will then, once it's all done, then it can parallel run and do all the thing by itself."

**On timeline ambition:**
> "So then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half, or something like that."

**On competitive transparency (IMPORTANT):**
> "I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendor right now. Because I know for a fact, right now outside there's no, no one has a pre, a package that we can just say, 'Hey, I will get, I want to buy your package or I want to pay something to get your package in so I can just run through this migration without any human involved or even a little human involved.'"

**On what they're looking for:**
> "So now I'm just kind of poking a hole and saying, who out there can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing?"

**On AI maturity:**
> "The efficiency gain that Grishi and the team had figured out was about 30%, okay? Now, as you kind of imagine, we still have a lot of manual intervention that needs to happen throughout that process."

**On current manual flow:**
> "You still have to manually go to Cognos, and then open the report, then take the SQL out, and then run through the AI, spit out the new SQL, then you have to manually snap it back to the Cognos. This entire process, what we're thinking is, hey, knowing that this whole AI is so mature right now... people are creating agents left and right."

**On feasibility validation:**
> "I think we want to make sure that this concept of, you know, all those little multiple little agents and have an orchestrator kind of, you know, orchestrating the entire flow, is it possible?"

**On next steps:**
> "Next step, probably we have maybe one more just to kind of give that session in terms of architecture. And even, Grishi has an enterprise architect working for her right now that have been laying out architecturally, in terms of the data migration."

### Commitments Made
- Provide priority ranking of pain points/deliverables
- Coordinate with Mahair for architecture session

### Sentiment
Visionary, transparent, actively shopping. Appreciates Colin's approach but needs validation. Investing time = positive signal.

---

## Colin Moore (Director of AI, BayOne)

### Role in Meeting
Technical lead and presenter. Established credibility through prior experience, demonstrated deep understanding of the challenge, proposed concrete approaches.

### Topics Owned
- AI acceleration framework presentation
- Schema mapping validation methodology
- Agent swarm architecture
- Infrastructure flexibility positioning

### Key Quotes

**On preparation (opening):**
> "My understanding of this is this is a very large scale multi-year data re-engineering project. So for an enterprise data warehouse. From what I understand, the team is doing more. It's not a lift and shift. It's more total re-engineering from the ground up."

**On being a skeptic:**
> "I'm always the skeptic. I think probably that's what I can give you. Instead of being the AI guy that says we can do anything at any time, I'm certainly not that person."

**On commercial solutions:**
> "Probably from a commercial solution standpoint, closest solution, which still would involve manual effort and still would be probably prohibitively expensive, to be honest, is Palantir... The problem is that's also going to come with six zeros attached to the price tag. And there is still always that manual effort that's involved."

**On agent specificity:**
> "Agents in general work better if they're more specific. So if you try to have a small subset of agents that, this is my reports agent. No, no, no. Here's the reports validator agent. Here's the one that checks the past state and the present state. The more specific you go with agents without going overly specific, the better off you are."

**On schema mapping approach:**
> "We actually stay away from AI until we have to. The reason for that is the higher up in the food chain AI gets implemented in, the more kind of telephone effect happens. So if you can wait to use AI until a little bit later in the process, it works better."

**On orchestration architecture:**
> "There is an agent that is the orchestrator. He's not the only one though. There's an orchestrator agent there, but there's also a judge. And the judge and the orchestrator have to be in sync. The judge, I call him like the grumpy old man agent, kind of yells at everyone, stay on track, follow this workflow, do not deviate."

**On infrastructure flexibility:**
> "My language, I like to say, I'll meet you at your home. So we don't want to force you into using another tool. You're already getting another tool... For us, it would be built on your infrastructure if that is desired."

**On legacy software advantage:**
> "The good news with older software, to be honest with you, is the same reason why it gets old is because... it's easier to get into older software... The more time passes and the more people use that. You have tools, they might be legacy, but they're not out of the ordinary."

**On the three tiers (from Mani):**
> "Type two, which to me is the best type, and I think the healthiest type, even from an org standpoint, is kind of a partner. Where we're doing a lot of the work, we're taking care of that AI load, but we're also at the same time kind of working alongside your team to help them understand what we're doing."

**On POC fun:**
> "I think the POC, I think we have fun doing those. So even to show you this in action, it's a lot of fun to watch, I will say. So it's kind of like you're watching almost like an army of little ants crawl across the screen."

### Commitments Made
- Prepare demo for next Thursday
- Share case studies
- Conduct architecture deep dive with Mahair
- Build on Sephora's infrastructure (no new tools)

### Performance Assessment
Strong technical credibility established. Good balance of confidence and realism. "Meet you at your home" messaging resonated. Only gap: no live demo ready when Grishi explicitly wanted one.

---

## Zahra Syed (Director, Strategic Accounts, BayOne)

### Role in Meeting
Facilitator and relationship manager. Kept meeting on track, handled scheduling logistics.

### Key Quotes

**On introducing Colin:**
> "We've been talking about Colin forever, so he's here. He's real."

**On scheduling:**
> "We're going to put together a demo for you. Colin, do you think, how much time do you think you'll need?"

> "We're going to send an email. I'll copy Colin on that email. Let's aim for next Thursday."

### Commitments Made
- Coordinate next meeting scheduling
- Send calendar invites

---

## Neha Malhotra (Head of Recruiting, BayOne)

### Role in Meeting
Present but minimal participation in this technical discussion. Asked one off-topic question about interview scheduling at the end.

### Key Quotes
> "I have one quick question. This is off-topic. Regarding the email you sent earlier, both of them are confirmed. I want to check whom you want to schedule."

---

## Cross-Speaker Dynamics

### Andrew ↔ Grishi
- Clear division: Andrew = vision/strategy, Grishi = execution/technical
- Andrew defers to Grishi on technical feasibility ("I don't know, Grishi, if you have in your mind anything")
- Grishi defers to Andrew on decisions ("Grishi, you're good with that, right?")

### Colin ↔ Grishi
- Strong technical rapport
- Grishi probed Colin's schema mapping approach - Colin responded with detailed process explanation
- Trust building through technical depth

### Andrew ↔ Colin
- Strategic alignment on agent swarm approach
- Andrew's transparency ("talking to lots of vendors") = testing Colin's reaction
- Colin's response (no defensiveness, offered multiple options) = passed the test
