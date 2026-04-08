# 01 - Meeting: BayOne Methodology Presentation

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Focused deep dive on BayOne methodology presentation

---

## 1. Colin's Professional Background and Credibility Establishment

Colin introduced himself by title and background before launching into the methodology. Key claims and details:

- **Title:** Director of AI at BayOne Solutions.
- **Prior role:** Coherent Corp (headquartered in Santa Clara). Colin ran the Center of Excellence for AI there.
- **Company scale:** Coherent is described as "a large company, about 40,000 employees globally."
- **Team size:** Colin personally managed a team of approximately 60 people while at Coherent.
- **Domain range:** "A lot of really cool projects going on. A lot of different domains that go here, which was exciting." Colin noted networking was one domain: "So part of it was networking. So we were more on the data-com, telecom side. Less about where Cisco is, but I at least understand enough to be conversational here."
- **AI practice breadth:** "My team does just about everything. So anything ranging from computer vision on the applied AI space, of course, gen AI is the kind of bread and butter right now... But even just more traditional machine learning, but I'll call this the boring AI that people aren't really as interested in, but still definitely has its place."
- **Core philosophy:** "My focus has always been high reliability systems. So determinism in AI, things that you can actually trust and are transparent, so engineers don't get this great solution built, and then completely reject it, because I'm not sure where any of the information or decisions are coming from."

### Migration Experience at Coherent

Colin established direct relevance to Guhan's problem by citing specific migration projects:

- **C# to Rust migration:** Explicitly named as one of the migrations his team executed. Colin described it as somehow "worse than moving from Spring to Go" in terms of difficulty, noting "That's a huge dump already, but even for us it was C# to Rust."
- **Spring to Go migration:** Referenced as another migration pattern his team has experience with. This is the same type of migration being done on the CI/CD side of the Cisco engagement.
- **Thick client to web-based interface:** Colin specifically called out experience "moving from a thick client over to a web-based interface" and the challenge of keeping "the UI flexible."
- **UI as the bottleneck:** "How do you deal with all of the UI changes? How do you keep the UI flexible? Because that ends up being a big pain point, even though it's sometimes the least technically complex and ends up taking the most time. Because it's very, I think, from a customer standpoint as well as making sure you don't lose any functionality."

## 2. Existing Cisco Engagements Referenced

Colin connected the methodology presentation to work already in progress at Cisco:

- **CI/CD engagement:** "We had a couple of things at Cisco. One that we have right now that we're, I think, about to start this work is on CI-CD side."
- **Code modernization engagement:** "And then there was another project that I think is more close to what you were just talking about, which is taking a legacy code base and potentially either modernizing it, in this case, this was a team that wanted to shift their stack entirely to something new, switch from spring to actually they wanted to go to go, which is a very big shift."
- **Consolidation and technical debt focus:** "In addition to that, to consolidate, make things more maintainable over time, make sure that that technical debt isn't carried forward. If you fix it once, you want it to be done. You don't want to have to redo the same effort in three years because none of the engineers know what's going on, no one can maintain it."

## 3. The Methodology Presentation: Code-Based Modernization

Colin explicitly offered to present a document: "I think if it's okay I can share one that we were looking at for the code-based modernization session. Is that okay?"

He then framed it strategically: "Because that, I think, will be, first of all, strategic. Because if you can build faster, even if your application isn't, let's say, AI facing or having AI features, if you can build faster, that definitely is a huge boost to everyone."

### 3.1 The Anti-Pattern: Vanilla Code Modernization

Colin opened the methodology by describing what does not work -- the naive approach to code modernization:

- "You can go the vanilla way to do code-based modernization. And that's where usually people start, and it sounds really good whenever you start. It doesn't work at all as soon as you get above a certain size of code base."
- **The developer copy-paste pattern:** "What ends up happening is you have developers saying, oh, ChatGPT can do this for me. I can copy and paste code. I can put in a file, get out a file, and it converts."
- **Why it fails -- system integration:** "The problem is that that's not how systems work. If you look at them as individual files, then what happens is, yes, you've done your job of converting, but now it can't talk to anything else. There's no meshing between the two."
- **Cross-language nuance:** "The other issue is the nuance between languages or even frameworks. What exists in one might not even have a concept in the other. For instance, like JavaScript, you have JavaScript versus Rust. These are two entirely different paradigms."
- **The imperative:** "So you have to know those nuances and capture those before you just start planning converting, because anything can convert. You can do that to any AI system today."

### 3.2 Step One: Simplification

Colin described the first phase of his methodology:

- "The first thing that we do is we start out with basically what I do for all AI projects, regardless of domain, regardless of type, which is simplification. For code bases, especially."

This was as far as Colin got in the formal presentation before Guhan interrupted (see Section 4 below). Based on the topic map context, the full methodology includes:

- Simplification first, then knowledge graphs
- Claude Code as backbone for exploration
- LangGraph agent swarm: architect, engineer, foreman, judge pattern
- Blockchain-style documentation approach
- Automated UX testing with Playwright
- Gap analysis through peer-to-peer agent communication

**Note:** These additional elements were NOT presented during this portion of the meeting. Colin was interrupted after describing only the simplification step. They were presumably covered in the follow-up 3:30 PM session referenced later in the conversation, which may be captured in a separate transcript.

### 3.3 Knowledge Graph Reference (Guhan's Interruption)

Guhan interrupted Colin's presentation with a highly specific question that suggests he had either seen a preview of the document or could see enough of the shared screen to anticipate where Colin was heading:

- **Guhan:** "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? Yes. And all those things, right? Yes."

Colin confirmed the knowledge graph component. Guhan then immediately pivoted to scheduling a deeper session rather than continuing the abbreviated overview. This indicates the methodology resonated strongly enough that Guhan wanted to give it proper time and attention rather than rushing through it.

## 4. Guhan's Reaction: Interrupted to Schedule a Deeper Session

This is one of the most significant moments in the meeting. Guhan's reaction to the methodology presentation was not passive interest -- he actively interrupted Colin mid-presentation to ensure a dedicated follow-up session was scheduled:

- **Guhan (interrupting):** "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? Yes. And all those things, right? Yes. Can we set up? Do you have some time in the afternoon?"
- **Colin confirmed:** "Of course, yes."
- **Guhan:** "Then I can meet with him and then go through this level."
- **Guhan clarified the time constraint:** "11:30, we're not going to meet in person. But I don't want to ask you that. No, totally fine."

The group then worked through calendar logistics and settled on a 3:00 to 3:30 PM follow-up session. Guhan explicitly stated he wanted to go deeper:

- **Guhan:** "I don't want to understand more about this one. Then I can do a little bit of touch and relations with it. He's doing the work."

This reaction pattern -- interrupting a presentation to demand a deeper dedicated session -- is a strong buying signal. Guhan did not ask clarifying questions, express skepticism, or request references. He immediately moved to logistics for a deeper dive.

## 5. Strategic and Consulting Positioning

### 5.1 Colin's Consulting Philosophy

Colin explicitly positioned BayOne as more than an implementation shop:

- "Because for me, it's as much, I actually just kept on telling them, it's as much for me a solution as it is consulting in a way. Because our job can't just be to do for solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next. That's at least my goal."
- **Technology landscape awareness:** "Even from an AI perspective, there's so many things coming out. Every week, every day, you read something new. But we can't feature-proof things. I think there's a lot of things that are in flux, of course. But even the stack that you choose, the tools that you choose, the frameworks that you choose, those have huge downstream implications."

### 5.2 Consolidation of Siloed Efforts

Colin connected his Coherent experience to a problem Guhan had described (multiple teams trying different AI approaches in parallel):

- "Even what you had said about trying to consolidate some of the efforts too, that's a huge one for me, because that was exactly coherent, the same problem that we had. There were a lot of really amazing siloed teams, and they were all kind of going in a similar direction. But no one was talking."
- **Consequences of non-consolidation:** "And then what ends up happening is you build this massive mountain of technical debt, and you can't do anything about it. And you end up having these really heated, at times, engineering discussions that are like, this platform versus this one, or this framework versus that."
- **Timing of the conversation:** "And it's not the right conversation. It's a conversation that should have happened a year prior before anyone started their work."

### 5.3 Future-Proofing for Agentic AI

Colin made a specific forward-looking argument about building with agentic AI in mind:

- "Even for, let's say, for a Gentakai [agentic AI]. If you want to do a Gentakai [agentic AI], there's a certain way that you should build things. Or even if you're modernizing, you should build it with this in mind so that whenever you get to the end of that project, you can now pick up on it for the next one whenever it comes."
- **The bolt-on anti-pattern:** "Agentic AI specifically. That one is the toughest because people tend to bolt things on. It always ends up being, hey, I wrote this plugin for this tool integration. Great. That's one more thing that we have to worry about."
- **Backend modernization opportunity:** "Even if the UI is the same, the backend and the things that the customer doesn't see could be different. And it can allow you to have better capabilities that are going to be more future proof."

## 6. Guhan's Framing of the Problem (Context for the Methodology)

Guhan provided critical context that explains why the methodology presentation resonated. His framing of the problem:

### 6.1 Scale of the Challenge

- **200 UI screens:** "So we are trying to like almost like 200 screen pages of UI."
- **Timeline pressure:** "Obviously the bill is about let's do it in one year. That's going to be too late."
- **Codebase size:** "We have easily 45-50 million lines of course [code], which are across like six or eight parts."
- **Non-starter to rebuild:** "We can't go and rebuild... it's the fact that we can step in the direction with no return of investment for sure, right? That's not where we want to go."

### 6.2 Nature of the UI Migration

- **Customer demand for exact parity:** "Some customers are major customers are coming back and say no, we want exactly the same ones. Because their systems are integrated with it... whatever their operators are used to, they don't want to change it."
- **Previous product (EPNM) vs. new product (EMS):** "This is about all the UI that we have in our previous product. We rebuilt it. Different experience for customers."
- **Traditional staffing not viable:** "I think the usual way of delivering through, putting 10 people to it, that's kind of going away."

### 6.3 Modernization Philosophy

Guhan articulated a nuanced view of modernization that aligned with Colin's methodology:

- **Build for agents, not just humans:** "We have to use the best of what we have, but to your point modernize it in a way that agents can work with rather than just the humans can, right?"
- **Customer education needed:** "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them. Make them move in that direction."
- **Time horizon argument:** "They are not even moving to 2025, they can't move to 2030, which we are having the conversation. So we have to make some choices."
- **ROI calculation for conversion:** "If it's six months and we go, we're able to convert all this, then it's not worth that... if it's going to take two, three years, then by the time you're done, this could be probably already old or kind of redundant."

### 6.4 Strategic vs. Tactical Need

Guhan explicitly asked for strategic input, not just implementation:

- **Guhan:** "Given your title and your experience, I think it's not just about implementing. What is the right direction? What is the right way to go about it? I think those kind of things will also really help. Strategic. Strategic."
- **Alignment with product management:** "Aligned with PLM2 [product line management] because there's always usual stuff often. Some big customers when they want, we don't think twice. We just want to go and, your customer first company."
- **Need for discipline:** "You want to go take care of it. Maybe try to step back and look at, is this right?"
- **Practical constraint:** "I don't want to shoot ourselves by overcoming something."

## 7. The Consolidation Problem (Guhan's Parallel Concern)

Guhan described a consolidation challenge across his teams that directly validated Colin's methodology and Coherent experience:

- **Multiple teams trying multiple things:** "The teams are also trying multiple things so we're trying to see consolidate into few things."
- **Risk of future disappointment:** "I can envision given experience, six months down line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be."
- **Preference to communicate early:** "So I would rather tell them now."
- **Building a catalog and process:** "So that's why I'm trying to build a catalog of things that are happening and have structured way through Jira and other, give visibility to what is happening."
- **Management effort underway:** "We have been trying to get some order to some method to madness, right?"

## 8. Key People and Organizational References

People mentioned in context of methodology follow-up and related engagements:

- **Varel:** One of Guhan's team leads. His team owns the UI migration work specifically. Guhan confirmed: "One idea is Varel's team, which is the... the one he said was the one that referred to the UI."
- **Meryl (Merill):** Leads the agentic AI platform being built separately. "Other part, the agency platform is being built by Meryl." Meryl is based in New York, was traveling the following week. Colin noted: "Meryl and I were supposed to have a follow-up conversation as well. She mentioned that I talked about what we're doing with CI/CD. She said it's somewhat relevant to us."
- **Salva:** Someone Colin had recently met: "I just met with Salva the other day, actually."
- **Mycat / Mecha (likely Mukesh or similar):** Referenced as having initially suggested BayOne could help: "Mecha did chat with me about one of the things that we could do, and there was some interesting opportunities that we had to accelerate some area."

## 9. Meeting Logistics and Follow-Up Structure

- The initial methodology presentation occurred in the morning (around 11:00-11:30 AM).
- Guhan interrupted the presentation and scheduled a deeper dive for 3:00-3:30 PM the same day.
- Colin and the BayOne team (including someone referred to as being "from Pennsylvania" who works remotely) were on-site at Cisco for two weeks.
- The group had a 2:00-2:30 PM commitment but was otherwise free.
- Guhan offered to introduce Colin to his technical teams: "I can introduce and then you can walk through. We love that."
- Guhan also suggested Colin could explore other projects happening in the group: "If your team has time, I have time."

## 10. Guhan's Description of EMS Platform Status

Context that frames what the methodology would be applied to:

- **Azure HD platform:** "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that."
- **Staffing status:** "At this point staffed and we are continuing to review what is needed. Each can take more and more people always, but we are working through the list of things to do there."
- **Nature of the product:** "It is not an agentic product, it's a traditional network management product, but modernized product. With capabilities that were previously in the previous version is missing, the previous generation is missing, especially on the UI."
- **How AI would be used:** "Using AI, how do we deliver it? So customers won't see the, maybe it's like AI generated code. So they won't see AI or anything in the frontend or even in the backend."

## 11. Open Questions and Unresolved Points

1. **What was in the full methodology document?** Colin was showing a PDF or document ("MDS code-based modernization") that he had prepared for the CI/CD engagement. Only the first step (simplification) was presented before Guhan interrupted. The knowledge graph, LangGraph agent swarm, blockchain documentation, Playwright testing, and gap analysis components were confirmed to exist in the document but not discussed in this transcript segment.

2. **Did the 3:00-3:30 PM deeper session occur?** Guhan scheduled a follow-up for later that afternoon. If a transcript of that session exists, it would contain the detailed methodology walkthrough. This transcript ends before that session.

3. **Which engagement gets priority?** Guhan described two or three potential work areas but noted the product line has not yet prioritized them: "The product lies prioritized, which is important. Because everything at this point seems to be priority... We've got to have 10 priorities and run behind everything, all the 10. So we have to somewhere to make some tough calls."

4. **Varel's team vs. Meryl's team:** Two distinct engagement tracks were identified -- UI migration (Varel) and agentic AI platform (Meryl). Guhan suggested BayOne could weigh in on prioritization: "If everything comes down to all that both of them are important priority then you will also have us, you can also weigh in and then say which is where you want to."

5. **What is the "Azure HD platform"?** Guhan referenced this as the modernized product currently in GA phase. The exact nature and how it relates to the UI migration work needs clarification.

6. **CTO reference (GTO):** Guhan mentioned "GTO has been very vocal everywhere" about AI -- likely referring to Cisco's CTO. This suggests executive-level mandate for AI adoption that creates top-down pressure on Guhan's group.

7. **MOUs with customers:** Guhan mentioned having "some MOUs with few of them [customers] to ensure that, and they are also talking to each other more than before, so they can leverage the best practices." The nature of these MOUs and how they constrain or shape the modernization work is unclear.

8. **Colin's document provenance:** Colin referred to the methodology document as something "we put together for him for a code-based modernization" -- the "him" appears to refer to the CI/CD engagement contact, suggesting this was originally prepared for a different Cisco engagement and was being shown to Guhan as an analogous approach.
