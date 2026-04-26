# Set 01 Deep-Dive Extraction (2026-02-09 Initial Discovery Meeting)

Source meeting: In-person discovery between Colin Moore (BayOne, Director of AI) and Guhan Selva (Cisco) at Cisco offices on 2026-02-09. Extraction covers five Set 01 deep-dive files.

---

## 1. Business Drivers and Why This Matters to Cisco

### 1.1 Customer demand for legacy UI parity is the trigger event

[from 01_meeting_business_drivers] Major customers are rejecting the modernized product's user interface and demanding exact replicas of the legacy (EPNM) interface. Guhan: "We rebuilt it. Different experience for customers, but some customers are major customers are coming back and say no, we want exactly the same ones. Because their higher their systems are integrated with it. Whatever their operators are used to, they don't want to change it."

Two distinct customer objections are embedded:

1. System integration dependency. Customer systems (OSS/BSS stacks, NOC dashboards, automation tooling) are integrated with the legacy UI. Changing the UI breaks those integrations. This is an operational dependency, not a preference.
2. Operator familiarity. Network operators are trained on the legacy interface. Retraining costs and workflow disruption are unacceptable to these customers.

### 1.2 Scale: approximately 200 UI screens need conversion

[from 01_meeting_business_drivers, also 01_meeting_technical_landscape] Guhan: "So we are trying to like almost like 200 screen pages of UI." This is from the legacy product to the modernized one.

### 1.3 The staffing model is explicitly broken

[from 01_meeting_business_drivers] Guhan: "I think the usual way of delivering through, putting 10 people to it, that's kind of going away. So you want to experiment something new." The old approach (assign 10 engineers to manually rebuild screens) is recognized as unsustainable. Leadership is actively seeking an AI-accelerated alternative. This is framed as an "experiment."

### 1.4 Timeline pressure

[from 01_meeting_business_drivers] Guhan: "Obviously the bill is about let's do it in one year. That's going to be too late." He also rejected simply over-investing: "Other thing is we also don't want to go in the trout off. It's not scalable at this point with the way our objects and stuffs are going." ("Trout off" is likely a transcription artifact for "trough" or "trade-off.") The legacy architecture has scalability issues with its object model; investing heavily in extending it is not a wise investment.

### 1.5 Multi-generational modernization context

[from 01_meeting_business_drivers, also 01_meeting_technical_landscape] Guhan: "We have been modernizing the Cisco multiple gens, right? We are moving from gen A to gen E to... next one, right? And then when we do that, obviously there's always a demand for not rebuilding everything." The EPNM-to-EMS transition is the latest in a series of generational product transitions. Each carries the same tension: customers want continuity, engineering needs to evolve.

Scale of the portfolio: "We have easily 45-50 million lines of code, which are across like six or eight products, and we can't go and rebuild. And they've been... it's the fact that we can step in the direction with no return of investment for sure, right? That's not where we want to go." Rebuilding from scratch is explicitly ruled out.

### 1.6 The AI inflection point as a parallel pressure

[from 01_meeting_business_drivers] Guhan: "And again, it comes down to the evolving means. As we see more in the next four years, it will also be AI, which we are playing. You know, GTO has been very vocal everywhere. That's real. And that's what customers are telling us also." "GTO" is understood as Cisco's CTO. Cisco's CTO has been publicly committed to AI transformation, and customers are echoing this expectation. Directional tension: immediate need is UI parity (backward-looking), strategic direction is AI-native capabilities (forward-looking).

### 1.7 Modernization must enable agents, not just humans

[from 01_meeting_business_drivers, also 01_meeting_technical_landscape] Guhan: "So we have to use the best of what we have, but to your point, modernize it in a way that agents can work with rather than just the humans can, right?" He is not asking for a simple UI port. He wants modernization that preserves what exists, makes the system accessible to AI agents, and prepares the product for an agentic future.

### 1.8 Customer relationship dynamics: education versus accommodation

[from 01_meeting_business_drivers] Guhan: "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them. Make them move in that direction. It's easy, easy workflow is to stick to what they're used to. But I think it's maybe they have to be disturbed a bit. They have to be a little bit shaken so that they are ready for pretty dirty." ("Pretty dirty" is likely a transcription artifact for "the future" or similar.)

Logic chain: Some customers have not even adopted the current (2025-era) product. They cannot leap to a 2030-era product without intermediate steps. Simply building what they want (legacy UI clone) may be wasted effort if it takes too long. The time horizon of the conversion determines whether it is worth doing.

### 1.9 The time-value calculation

[from 01_meeting_business_drivers, also 01_meeting_technical_landscape] Guhan: "Let's say if it's six months and we go, we're able to convert all this, then it's not worth that, that kind of, that the dialogue can happen. In fact, it's going to take two, three years. Then by the time you're done, this could be probably already old or kind of redundant, so you need to go."

- If conversion takes approximately six months: worth doing. Customers get what they need; investment pays off in remaining lifecycle.
- If conversion takes two to three years: not worth doing. Product generation will be obsolete by completion.
- The AI-accelerated approach is attractive precisely because it might compress the timeline into the "worth doing" window.

### 1.10 MOUs with major customers exist

[from 01_meeting_business_drivers] Guhan: "So we have some MOUs with few of them to ensure that, and they are also talking to each other more than before, so they can leverage the best practices and things." Memoranda of Understanding exist with specific major customers around the modernization transition. Customers are coordinating with each other.

### 1.11 Customer-first culture versus strategic discipline

[from 01_meeting_business_drivers] Guhan: "And aligned with PLM too, because there's always usual stuff. Often some big customers when they want, we don't think twice. We just want to go. You are a customer-first company. You want to go take care of it. Maybe try to step back and look at, is this right?" He wants BayOne to provide an external strategic counterweight to Cisco's instinct to immediately fulfill major customer requests.

### 1.12 Product management prioritization is broken

[from 01_meeting_business_drivers] Guhan: "The product has prioritized, which is important. Because everything at this point seems to be priority, which I've just come out of the meeting. We've got to have everything as a priority. We've got to have 10 priorities and run behind everything, all the 10." Product management treats everything as equally important. Guhan intends to force real prioritization: "We have to somewhere to make some tough calls. We have to make a team with the product management. We will enforce some decisions to them that they have to prioritize to be proper."

### 1.13 Two or three additional items in the pipeline beyond UI conversion

[from 01_meeting_business_drivers] Guhan: "But there are, as I said, there are two or three in the lab." And: "There is something we have other areas anyway to look at if at all we get some additional." The UI conversion (200 screens) is most clearly defined; 2-3 other potential work streams are not yet clearly scoped.

### 1.14 Consolidating parallel AI efforts

[from 01_meeting_business_drivers] Guhan: "The teams are also trying multiple things, so we're trying to see consolidate into few things. Everyone trying... that's the area." He articulated a specific engineer-morale concern: "It's not there in the heated or demand stage, but I can envision given experience, six months down line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be. So I would rather tell them now."

Visibility effort: "So that's why I'm trying to build a catalog of things that are happening and have structured way through Jira and other. Give visibility to what is happening because if they don't bring visibility then we can't help it. So trying to bring that kind of certain process." He frames this as a management/leadership challenge separate from the technical work.

### 1.15 What Guhan wants from BayOne

[from 01_meeting_business_drivers] Guhan: "Given your title and your experience, I think it's not just about implementing. What is the right direction? What is the right way to go about it? I think those kind of things will also really help. Strategic. Strategic. Right." He repeated "strategic" for emphasis. Alignment with PLM (product lifecycle management) is required. At the same time: "At the same time, something practical. Yes, I don't want to shoot ourselves by overcommitting something."

### 1.16 Two defined work streams plus a third platform

[from 01_meeting_business_drivers, also 01_meeting_technical_landscape]

- UI Conversion (Varel's team). Approximately 200 UI screens from legacy (EPNM) to modern (EMS). Cannot take a year; must be accelerated through AI. Primary BayOne opportunity.
- Agentic AI Platform (Meryl's team). Meryl is based in New York, was traveling the following weekend. Guhan: "I checked with her on what she needs something there at this point" (implying Meryl may not currently need external help). Meryl had earlier told Colin the CI/CD work was "somewhat relevant" to her.
- Azure HD Platform. Guhan: "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that." Staffed, in GA phase, not the primary focus for BayOne.

---

## 2. Initial Technical Landscape (as understood 2026-02-09)

### 2.1 Nature of the EMS product

[from 01_meeting_technical_landscape] Guhan's direct description: "It is about, it's not an agentic product, it's a traditional network management product, but modernized product. With capabilities that were previously in the previous version is missing, the previous generation is missing, especially on the UI."

- The new product (EMS) is functionally incomplete relative to the legacy product (EPNM).
- Missing capabilities are concentrated in the UI layer.
- The backend modernization is further along than the frontend.
- EMS is explicitly not an agentic product.

### 2.2 Quantitative scale metrics

[from 01_meeting_technical_landscape]

| Metric | Value |
|--------|-------|
| Total lines of code | 45-50 million |
| Number of products in portfolio | 6-8 |
| UI screens needing conversion | Approximately 200 |
| Target timeline | Less than one year ("one year is too late") |
| Traditional staffing approach | 10 people (explicitly rejected) |

### 2.3 EPNM (legacy product) characteristics as described in this meeting

[from 01_meeting_technical_landscape]

- UI technology is legacy. (Dojo/JavaScript is referenced in the topic map for this set; not explicitly named in the 2026-02-09 transcript itself.)
- Customers' systems have programmatic integrations with the legacy UI.
- Operators are trained on existing workflows.
- Part of a larger portfolio spanning 45-50 million lines of code.

### 2.4 EMS (new product) characteristics

[from 01_meeting_technical_landscape]

- Rebuilt with a "different experience for customers."
- Described as a traditional (not agentic) network management product, modernized.
- Has an Azure HD platform in GA phase.
- Currently staffed; team is "working through the list of things to do there."
- (Angular frontend and microservices architecture are referenced in the topic map; not explicitly named in the transcript itself.)

### 2.5 Azure HD platform

[from 01_meeting_technical_landscape, 01_meeting_security_and_access] Guhan: "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that. But that's, I think that's more like at this point staffed and we are continuing to review what is needed." What "HD" stands for and whether it is Azure Hybrid Developer, Azure DevOps, or something else remained unresolved in this meeting.

### 2.6 AI as development accelerator, not product feature

[from 01_meeting_technical_landscape, 01_meeting_bayone_methodology_presentation] Guhan: "So how do we ensure we have that capability? So using AI, how do we deliver it? So customers won't see the, maybe it's like AI generated code. So they won't see AI or anything in the frontend or even in the backend. So that is one."

Three distinct AI uses emerged:

1. AI as development tool for UI conversion (the BayOne opportunity). Output is conventional code; customers never see AI.
2. Agentic AI platform (Meryl's effort). Separate product capability.
3. Independent team experiments across the organization. Consolidation target for Guhan.

### 2.7 Treadmill concern regarding legacy architecture

[from 01_meeting_technical_landscape] Guhan: "Other thing is we also don't want to go in the trout off [treadmill]. It's not scalable at this point with the way our objects and stuffs are going. I think I don't think there's something that that's a wise investment to go." The legacy architecture has scalability issues with its data model (objects).

### 2.8 Technical details not confirmed in this meeting

[from 01_meeting_technical_landscape] Explicitly unconfirmed from the 2026-02-09 transcript alone:

- Specific stack of the legacy product (Java/Dojo referenced in topic map only)
- Specific stack of the new product (Angular referenced in topic map only)
- Architecture of the new product (microservices referenced in topic map only)
- Which of the 6-8 products is the specific focus
- Azure HD expansion and architecture
- Breakdown of complexity across the 200 screens
- Varel's team size and structure
- Enumeration of the teams experimenting with AI

---

## 3. BayOne Methodology as Presented

### 3.1 Colin's credibility establishment

[from 01_meeting_bayone_methodology_presentation]

- Title: Director of AI at BayOne Solutions.
- Prior role: Coherent Corp (headquartered in Santa Clara), where Colin ran the Center of Excellence for AI. Coherent is approximately 40,000 employees globally.
- Team size at Coherent: approximately 60 people.
- Domain coverage: "So part of it was networking. So we were more on the data-com, telecom side. Less about where Cisco is, but I at least understand enough to be conversational here."
- Practice breadth: "My team does just about everything. So anything ranging from computer vision on the applied AI space, of course, gen AI is the kind of bread and butter right now... But even just more traditional machine learning, but I'll call this the boring AI that people aren't really as interested in, but still definitely has its place."
- Core philosophy: "My focus has always been high reliability systems. So determinism in AI, things that you can actually trust and are transparent, so engineers don't get this great solution built, and then completely reject it, because I'm not sure where any of the information or decisions are coming from."

### 3.2 Prior migration experience cited

[from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]

- C# to Rust migration: executed by Colin's team at Coherent. Colin described it as "somehow worse than moving from Spring to Go."
- Spring to Go migration: cited as the pattern being done on the CI/CD side at Cisco.
- Thick client to web-based interface: Colin specifically called this out as relevant to UI modernization, noting "how do you deal with all of the UI changes? How do you keep the UI flexible? Because that ends up being a big pain point, even though it's sometimes the least technically complex and ends up taking the most time."

### 3.3 Referenced existing Cisco engagements

[from 01_meeting_bayone_methodology_presentation] Colin: "We had a couple of things at Cisco. One that we have right now that we're, I think, about to start this work is on CI-CD side." And: "another project that I think is more close to what you were just talking about, which is taking a legacy code base and potentially either modernizing it, in this case, this was a team that wanted to shift their stack entirely to something new, switch from spring to actually they wanted to go to go, which is a very big shift."

On consolidation focus: "In addition to that, to consolidate, make things more maintainable over time, make sure that that technical debt isn't carried forward. If you fix it once, you want it to be done. You don't want to have to redo the same effort in three years because none of the engineers know what's going on, no one can maintain it."

### 3.4 The anti-pattern: vanilla code modernization

[from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]

- Colin: "You can go the vanilla way to do code-based modernization. And that's where usually people start, and it sounds really good whenever you start. It doesn't work at all as soon as you get above a certain size of code base."
- Developer copy-paste pattern: "What ends up happening is you have developers saying, oh, ChatGPT can do this for me. I can copy and paste code. I can put in a file, get out a file, and it converts."
- Why it fails (integration): "The problem is that that's not how systems work. If you look at them as individual files, then what happens is, yes, you've done your job of converting, but now it can't talk to anything else. There's no meshing between the two."
- Cross-language nuance: "The other issue is the nuance between languages or even frameworks. What exists in one might not even have a concept in the other. For instance, like JavaScript, you have JavaScript versus Rust. These are two entirely different paradigms."
- Imperative: "So you have to know those nuances and capture those before you just start planning converting, because anything can convert. You can do that to any AI system today."

### 3.5 Step one: simplification

[from 01_meeting_bayone_methodology_presentation] Colin: "The first thing that we do is we start out with basically what I do for all AI projects, regardless of domain, regardless of type, which is simplification. For code bases, especially."

This is as far as Colin got in the formal presentation before Guhan interrupted.

### 3.6 Knowledge graph reference (Guhan's interruption)

[from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape] Guhan interrupted at the mention of knowledge graphs: "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? Yes. And all those things, right? Yes." Colin confirmed. Guhan immediately pivoted to scheduling a deeper session rather than continuing the abbreviated overview.

### 3.7 Full methodology components (confirmed existing in document, not presented in full at this meeting)

[from 01_meeting_bayone_methodology_presentation] Per the topic map and Colin's document, the full methodology includes:

- Simplification first, then knowledge graphs
- Claude Code as backbone for exploration
- LangGraph agent swarm: architect, engineer, foreman, judge pattern
- Blockchain-style documentation approach
- Automated UX testing with Playwright
- Gap analysis through peer-to-peer agent communication

These elements were NOT presented in detail during this morning session. They were covered (or intended to be covered) in the 3:00 PM same-day follow-up with Varel's team lead.

### 3.8 Strategic consulting positioning

[from 01_meeting_bayone_methodology_presentation]

- Colin: "Because for me, it's as much, I actually just kept on telling them, it's as much for me a solution as it is consulting in a way. Because our job can't just be to do for solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next. That's at least my goal."
- Technology landscape awareness: "Even from an AI perspective, there's so many things coming out. Every week, every day, you read something new. But we can't feature-proof things... even the stack that you choose, the tools that you choose, the frameworks that you choose, those have huge downstream implications."

### 3.9 Consolidation of siloed efforts (Coherent analogy)

[from 01_meeting_bayone_methodology_presentation, 01_meeting_business_drivers] Colin: "Even what you had said about trying to consolidate some of the efforts too, that's a huge one for me, because that was exactly coherent, the same problem that we had. There were a lot of really amazing siloed teams, and they were all kind of going in a similar direction. But no one was talking. And then what ends up happening is you build this massive mountain of technical debt, and you can't do anything about it. And you end up having these really heated, at times, engineering discussions that are like, this platform versus this one, or this framework versus that. And it's not the right conversation. It's a conversation that should have happened a year prior before anyone started their work."

### 3.10 Future-proofing for agentic AI

[from 01_meeting_bayone_methodology_presentation]

- Colin: "Even for, let's say, for a Gentakai [agentic AI]. If you want to do a Gentakai [agentic AI], there's a certain way that you should build things. Or even if you're modernizing, you should build it with this in mind so that whenever you get to the end of that project, you can now pick up on it for the next one whenever it comes."
- Bolt-on anti-pattern: "Agentic AI specifically. That one is the toughest because people tend to bolt things on. It always ends up being, hey, I wrote this plugin for this tool integration. Great. That's one more thing that we have to worry about."
- Backend modernization opportunity: "Even if the UI is the same, the backend and the things that the customer doesn't see could be different. And it can allow you to have better capabilities that are going to be more future proof."

### 3.11 Guhan's reaction signal

[from 01_meeting_bayone_methodology_presentation] Guhan interrupted mid-presentation to ensure a dedicated follow-up was scheduled. He did not ask clarifying questions, express skepticism, or request references. He immediately moved to logistics for a deeper dive. Guhan: "I don't want to understand more about this one. Then I can do a little bit of touch and relations with it. He's doing the work."

---

## 4. Security, Access, and Compliance Baseline

### 4.1 Code must remain on Cisco hardware

[from 01_meeting_security_and_access] BayOne engineers cannot download Cisco source code to personal machines. All development, exploration, and AI-assisted work must happen on Cisco-provisioned hardware connected to Cisco networks. Any AI model that processes code must run within Cisco infrastructure or be a Cisco-licensed service. Personal API keys, personal IDE extensions, and SaaS tools running outside Cisco's perimeter are not acceptable.

### 4.2 Cisco-licensed AI tools required

[from 01_meeting_security_and_access] AI tools used on the engagement must be Cisco-licensed, not personal licenses. The exact phrasing in the transcript is garbled ("coded service point"), but the intent from context is that Cisco has enterprise-licensed AI tooling and that is what must be used.

Practical implications:

- Colin cannot install his preferred AI tools on a Cisco laptop and start working.
- The AI platform/tools must be whatever Cisco has licensed at the enterprise level.
- This may constrain which models (Claude, GPT-4, Gemini, etc.) are available.
- The Claude Code / LangGraph methodology would need to either run within Cisco's approved tooling or require Cisco to approve/license those specific tools.

Open question at the time: what specific AI tools does Cisco currently have licensed at the enterprise level.

### 4.3 NDA status

[from 01_meeting_security_and_access] The NDA between BayOne and Cisco has been signed. It was in place before this meeting occurred. The NDA appears to cover both Colin and the broader BayOne team that would come on after a POC. Guhan's willingness to share internal details during this meeting confirms the NDA provided sufficient comfort for an open conversation.

### 4.4 Cisco laptop pending

[from 01_meeting_security_and_access] Colin did not have a Cisco laptop at the time of the meeting. Timeline stated: 1-2 weeks from 2026-02-09 (approximately 2026-02-16 to 2026-02-23). A BayOne representative referenced a call about hardware in the evening of the meeting day, suggesting active follow-up. Without the laptop, Colin cannot access Cisco source code, connect to Cisco's internal network, use Cisco-licensed AI tools, or begin any code exploration or POC work.

### 4.5 Cisco ID pending

[from 01_meeting_security_and_access] A Cisco ID (badge/identity credentials) was expected to be issued the same day or shortly after the meeting. This is separate from the laptop. The badge provides building access, network authentication, and identity within Cisco systems. Attendee statement: "You can use your setup with the badge then you can connect to it" (referring to conference room displays).

### 4.6 Wi-Fi and WebEx connectivity constraints during the meeting

[from 01_meeting_security_and_access] The meeting itself was disrupted because Colin could not connect to Cisco Wi-Fi (no badge/credentials). He used his phone as connectivity workaround. The methodology PDF had to be sent via Teams and pulled up by Guhan rather than presented directly. Even basic meeting logistics require Cisco network access, which requires Cisco credentials.

### 4.7 Team NDA and hardware requirements (for scaling)

[from 01_meeting_security_and_access] Colin: "For the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go." Each BayOne team member joining after the POC would need: individual NDA execution, a Cisco-provisioned laptop, a Cisco ID/badge, and access to Cisco-licensed AI tools. The 1-2 week hardware timeline per person is a potential bottleneck.

### 4.8 Cloud instances for testing

[from 01_meeting_security_and_access] Cisco has cloud instances available (via Azure HD platform). Whether the EPNM-to-EMS conversion work specifically will have access to those cloud instances, or whether all testing must occur on local Cisco hardware, was not resolved. Relevant for Colin's methodology because the multi-agent approach may require significant compute resources.

### 4.9 No downloading code to personal machines (corollary)

[from 01_meeting_security_and_access] Code must never leave Cisco infrastructure at any point:

- No cloning repositories to personal laptops
- No copying code snippets to external tools for analysis
- No using personal SaaS-based AI tools (ChatGPT web interface, personal Claude account) to analyze code
- No exfiltrating code via email, messaging, or file transfer to non-Cisco systems

### 4.10 Physical access and on-site logistics

[from 01_meeting_security_and_access]

- Conference rooms: a preferred room was taken; they used an alternate.
- Conference room displays require a Cisco badge to connect.
- Colin was on-site at Cisco offices for two weeks, available "in and out, including today."
- An unnamed BayOne representative was also physically present and facilitated logistics.
- Guhan committed to making introductions: "I can introduce and then you can walk through."

---

## 5. Initial Next Steps and Mutual Expectations

### 5.1 Same-day 3:00 PM deeper technical session

[from 01_meeting_next_steps_and_expectations] Scheduled during the meeting, after Guhan interrupted the methodology walkthrough.

- Time: 3:00 PM (or 3:00-3:30 as a start) on 2026-02-09.
- Purpose: bring the technical lead from Varel's team to discuss UI conversion, with Colin presenting the full codebase modernization approach.
- Format: mutual exchange ("They can explain what is here and then you can bring what you have done before and then you can see").
- Status: firm, scheduled during this meeting.

### 5.2 Priority screen identification by Guhan's team

[from 01_meeting_next_steps_and_expectations] Guhan committed to working internal prioritization with product management. Current state is that "everything is priority"; specific priority screens among the approximately 200 have not been identified. Guhan: "Let me work on the other couple of things. So then we can have a next level discussion." Status: in progress on Cisco's side, no firm date.

### 5.3 Four-week decision timeline (aspirational)

[from 01_meeting_next_steps_and_expectations] Implied rather than explicitly stated as a hard deadline. Guhan wants decisions on which efforts to pursue before teams invest further in divergent approaches. Driven by the morale concern ("I would rather tell them now"). Status: aspirational but time-pressured.

### 5.4 Colin to write POC proposal

[from 01_meeting_next_steps_and_expectations] Not explicitly stated as a formal action item, but groundwork was laid. Colin needs to formulate a proposal after gathering more technical detail in the afternoon session. Status: implicit commitment.

### 5.5 Commercial model implicit

[from 01_meeting_next_steps_and_expectations] Commercial terms not explicitly discussed in this transcript. POC-first approach is the direction; details remain undefined. (Commercial detail excluded from this extraction per handoff rules.)

### 5.6 Connecting with Meryl about agentic AI platform

[from 01_meeting_next_steps_and_expectations] Colin volunteered: "Meryl and I were supposed to have a follow-up conversation as well. She mentioned that I talked about what we're doing with CICD. She said it's somewhat relevant to us. So I can go ahead and take the lead and just connect." Guhan approved. Meryl travels the following week; time-sensitive to connect during the week of 2026-02-09. Status: firm, time-sensitive.

### 5.7 Varel's team confirmed as UI conversion owner

[from 01_meeting_next_steps_and_expectations] Colin asked whether Varel would be involved; Guhan confirmed: "Yeah, one idea is Varel's team, which is the... the one he said was the one that referred to the UI." The 3:00 PM same-day session was specifically to bring Varel's team lead into a deeper technical discussion. Status: firm identification.

### 5.8 Periodic checkpoints (aspirational)

[from 01_meeting_next_steps_and_expectations] Cadence implied, no recurring schedule established. Guhan also invited Colin to explore independently: "Or you want to explore something that is happening around and you want to... you are welcome to also."

### 5.9 Hardware timeline confirmation

[from 01_meeting_next_steps_and_expectations, 01_meeting_security_and_access] Referenced but not resolved in this transcript. Follow-up evening call about hardware was referenced.

### 5.10 Team beyond POC already available (BayOne positioning)

[from 01_meeting_next_steps_and_expectations] Colin signaled readiness to scale: 60-person team at Coherent, practice breadth across CV, gen AI, classical ML. Implicit message: scaling from POC to full engagement would not require a long ramp-up.

### 5.11 Strategic consulting role beyond implementation (firm mutual agreement)

[from 01_meeting_next_steps_and_expectations] Both parties explicitly agreed BayOne's role should include strategic advising, not just implementation. Guhan: "Given your title and your experience, I think it's not just about implementing. What is the right direction?" Colin: "Our job can't just be to do for solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next."

### 5.12 Action item summary

| # | Action | Owner | Timeline | Status |
|---|--------|-------|----------|--------|
| 1 | Deeper technical session with Varel's team lead | Colin + Guhan | 3:00 PM same day (2026-02-09) | Firm, scheduled |
| 2 | Identify priority screens from approximately 200 UI pages | Guhan + Product Management | Unspecified (within approximately 4 weeks) | In progress |
| 3 | Make prioritization decisions across AI initiatives | Guhan | Within approximately 4 weeks | Aspirational, urgent |
| 4 | Write POC proposal for UI conversion | Colin | After technical deep-dive | Implicit |
| 5 | Connect with Meryl about agentic AI platform | Colin | Week of 2026-02-09 | Firm, time-sensitive |
| 6 | Connect with Varel's team for UI conversion details | Colin (via Guhan introduction) | Started same day | Firm, in progress |
| 7 | Consolidate catalog of AI experiments via Jira | Guhan | Ongoing | In progress internally |
| 8 | Establish periodic checkpoint cadence | Both parties | TBD | Aspirational |

---

## 6. Verbatim Statements That Shape Scope

Statements from this meeting that could still bind the POC today. Grouped by binding theme. Source file citations indicate which deep-dive files surfaced each quote.

### 6.1 Why this work exists (customer demand)

- Guhan: "We rebuilt it. Different experience for customers, but some customers are major customers are coming back and say no, we want exactly the same ones. Because their higher their systems are integrated with it. Whatever their operators are used to, they don't want to change it." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.2 Scale and timeline constraints

- Guhan: "So we are trying to like almost like 200 screen pages of UI." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]
- Guhan: "Obviously the bill is about let's do it in one year. That's going to be too late." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]
- Guhan: "I think the usual way of delivering through, putting 10 people to it, that's kind of going away. So you want to experiment something new." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]
- Guhan: "Let's say if it's six months and we go, we're able to convert all this, then it's not worth that, that kind of, that the dialogue can happen. In fact, it's going to take two, three years. Then by the time you're done, this could be probably already old or kind of redundant, so you need to go." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.3 Portfolio scope and no-rebuild

- Guhan: "We have easily 45-50 million lines of code, which are across like six or eight products, and we can't go and rebuild." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.4 Nature of the EMS product and where AI fits

- Guhan: "It is about, it's not an agentic product, it's a traditional network management product, but modernized product. With capabilities that were previously in the previous version is missing, the previous generation is missing, especially on the UI." [from 01_meeting_technical_landscape]
- Guhan: "So how do we ensure we have that capability? So using AI, how do we deliver it? So customers won't see the, maybe it's like AI generated code. So they won't see AI or anything in the frontend or even in the backend. So that is one." [from 01_meeting_technical_landscape, 01_meeting_bayone_methodology_presentation]

### 6.5 Modernize for agents, not just humans

- Guhan: "So we have to use the best of what we have, but to your point, modernize it in a way that agents can work with rather than just the humans can, right?" [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.6 Strategic positioning (not just implementation)

- Guhan: "Given your title and your experience, I think it's not just about implementing. What is the right direction? What is the right way to go about it? I think those kind of things will also really help. Strategic. Strategic. Right." [from 01_meeting_business_drivers, 01_meeting_next_steps_and_expectations]
- Guhan: "And aligned with PLM too, because there's always usual stuff." [from 01_meeting_business_drivers]
- Guhan: "At the same time, something practical. Yes, I don't want to shoot ourselves by overcommitting something." [from 01_meeting_business_drivers]
- Colin: "It's as much for me a solution as it is consulting in a way. Because our job can't just be to do for solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next." [from 01_meeting_bayone_methodology_presentation, 01_meeting_next_steps_and_expectations]

### 6.7 Anti-pattern commitment (why a naive approach will not be used)

- Colin: "You can go the vanilla way to do code-based modernization. And that's where usually people start, and it sounds really good whenever you start. It doesn't work at all as soon as you get above a certain size of code base." [from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]
- Colin: "The problem is that that's not how systems work. If you look at them as individual files, then what happens is, yes, you've done your job of converting, but now it can't talk to anything else. There's no meshing between the two." [from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]
- Colin: "The other issue is the nuance between languages or even frameworks. What exists in one might not even have a concept in the other." [from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]

### 6.8 Methodology commitments introduced

- Colin: "The first thing that we do is we start out with basically what I do for all AI projects, regardless of domain, regardless of type, which is simplification. For code bases, especially." [from 01_meeting_bayone_methodology_presentation]
- Guhan: "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? Yes. And all those things, right? Yes." [from 01_meeting_bayone_methodology_presentation, 01_meeting_technical_landscape]

### 6.9 Customer education versus accommodation

- Guhan: "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them. Make them move in that direction." [from 01_meeting_business_drivers, 01_meeting_technical_landscape, 01_meeting_bayone_methodology_presentation]
- Guhan: "That's because they are not even moving to 2025, they can't move to 2030, which we are having the conversation." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.10 MOUs with customers

- Guhan: "So we have some MOUs with few of them to ensure that, and they are also talking to each other more than before, so they can leverage the best practices and things." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.11 Work-stream ownership

- Guhan: "One idea is Varel's team, which is the... the one he said was the one that referred to the UI." [from 01_meeting_bayone_methodology_presentation, 01_meeting_next_steps_and_expectations]
- Guhan: "Other part, the agency platform is being built by Meryl." [from 01_meeting_bayone_methodology_presentation]

### 6.12 Prioritization dependency

- Guhan: "The product has prioritized, which is important. Because everything at this point seems to be priority, which I've just come out of the meeting. We've got to have everything as a priority. We've got to have 10 priorities and run behind everything, all the 10." [from 01_meeting_business_drivers, 01_meeting_next_steps_and_expectations]
- Guhan: "So we have to somewhere to make some tough calls. We have to make a team with the product management. We will enforce some decisions to them that they have to prioritize to be proper." [from 01_meeting_business_drivers]
- Guhan: "So based on that, we'll know which is more important than that. And that's when we can have the solid, honest, true discussion about it." [from 01_meeting_business_drivers]

### 6.13 Consolidation of parallel AI efforts

- Guhan: "The teams are also trying multiple things, so we're trying to see consolidate into few things." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]
- Guhan: "I can envision given experience, six months down line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be. So I would rather tell them now." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]

### 6.14 Security and access constraints (implicit policy)

- Attendee, to Colin: "You can use your setup with the badge then you can connect to it." [from 01_meeting_security_and_access]
- Colin: "I'm on my phone because I don't have the Wi-Fi." [from 01_meeting_security_and_access]
- Colin: "For the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go." [from 01_meeting_security_and_access]

### 6.15 Follow-up session commitment

- Guhan: "Can we set up? Do you have some time in the afternoon?" [from 01_meeting_bayone_methodology_presentation, 01_meeting_next_steps_and_expectations]
- Guhan: "I can introduce and then you can walk through. We love that." [from 01_meeting_bayone_methodology_presentation, 01_meeting_security_and_access]

### 6.16 Four-year AI horizon

- Guhan: "And again, it comes down to the evolving means. As we see more in the next four years, it will also be AI, which we are playing. You know, GTO has been very vocal everywhere. That's real. And that's what customers are telling us also." [from 01_meeting_business_drivers, 01_meeting_technical_landscape]
