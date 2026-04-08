# 01 - Meeting: Stakeholder Expectations and Next Steps

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on expectations, deliverables, and agreed next steps

---

## 1. Cisco Team Bandwidth: What They Can and Cannot Provide

### Selva's Statement on Team Availability

Selva made a direct, unambiguous statement about team capacity. The team is currently occupied with critical platform work and cannot dedicate significant time to this effort:

> "At the moment the team is also on critical... platform [work]... the team itself will not be able to miss time here."

This was stated matter-of-factly, not apologetically. It was framed as a constraint that Colin needs to work within, not something that might change. The word "critical" signals this is not discretionary work the team is doing -- it is a priority that supersedes this initiative.

### What They Will Provide

Selva immediately followed the bandwidth constraint with what the team *can* do:

> "But of course, they need to give you the context and everything. They will provide you with that."

So the team's role is explicitly scoped to:
- **Context provision:** Background on the codebase, architecture, domain knowledge
- **Identification of conversion candidates:** Selva stated "we will focus on the ones that we've not brought in yet and identify a few screens" -- the team will do the prioritization and selection of which screens/ functionality to target
- **Periodic checkpoints:** For clarification and progress visibility (see section 2)
- **System access:** When the time comes for testing, "we will provide the system to try this out"

### What They Will Not Provide

Implied but clear from context:
- No hands-on engineering time from Cisco engineers on this effort
- No dedicated pairing or co-development sessions
- No ongoing availability for ad-hoc questions (hence "periodic checkpoints" rather than open-door access)

### Selva's Framing of the Team's Prior Work

Selva provided important context about how the team has handled similar work in the past, which sets expectations for what Colin will encounter:

> "That's kind of the exercise the team did for previous ones. And in some cases, we also went through a new UX design and the user experience."

This tells Colin: the team has done this kind of migration before (manually), so they have institutional knowledge about the pitfalls, but they did it the traditional way. The team's experience is a knowledge resource, not a labor resource.

### Selva on Identifying Specific Screens

Selva committed to having the team identify specific screens for conversion, with a strategic angle -- focusing on screens that have *not* yet been brought into the new system:

> "There are some screens we have already brought in functionality with a new idea. There are still some functionality that's remaining in the old. Maybe... we will focus on the ones that we've not brought in yet and identify a few screens, like Guhan has said."

This is important: the POC will target screens with no existing new-UI equivalent, meaning Colin will be working on genuinely missing functionality, not duplicating work already done. This also means the back-end for those screens is also not yet ported (see Selva's "vertical" comment about front-end and back-end moving together).

---

## 2. Guhan's Expectation of Independent Work

### The Operating Model

Guhan laid out the expected working model explicitly. After receiving initial context from the team, Colin is expected to operate independently:

> "Hopefully... you'll be able to, once we get the context right, you'll be able to move ahead on your own to do this analysis and come back."

This is a clear three-phase model:
1. **Context transfer** -- Team provides Colin with the background he needs
2. **Independent work** -- Colin works autonomously on analysis and development
3. **Come back with results** -- Colin returns with findings, analysis, and working code

### Periodic Checkpoints

Guhan specified that the engagement would not be entirely hands-off:

> "We'll have periodic checkpoints to help clarify anything more, and also keep the rest of the folks [aware] with the progress."

The checkpoints serve two purposes:
- **Clarification:** Colin can surface questions or blockers
- **Visibility:** Guhan and others stay informed of progress

The word "periodic" suggests scheduled intervals (weekly, perhaps), not on-demand. This reinforces the independent-work expectation -- Colin should batch his questions for checkpoints rather than interrupting the team ad hoc.

### Guhan's Domain Knowledge Concern

Guhan raised one pointed concern about Colin's approach, specifically around domain expertise:

> "How do you try to reach the [gap] for the domain level thing? ...This one is in element management. And how do we ensure that there's no gap in what we bring over? ...This may not have the readily available [tests] for you to go rerun them on the new one. How do you make sure that there's no domain gap or no functionality gap?"

This is Guhan stress-testing whether the AI-assisted approach can handle domain-specific nuance in network element management -- a specialized area where incorrect behavior could affect customers. Colin's response about the "judge" agent, automated gap analysis, and final human review appeared to satisfy this concern, but it is clearly something Guhan will be watching for in the POC results.

---

## 3. The POC as Internal Leverage: Guhan's Exact Framing

### Why Demos Matter

Guhan made the strategic purpose of the POC explicit. This is not just about proving the technology works -- it is about giving Guhan ammunition to secure additional resources internally at Cisco:

> "The POC would, so basically this is also about actually hands-on coding and showing the [results]. That way, if we have to also get the additional resources for this, which we will have to work through, this will help. Show it, even to make it, show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

Breaking this down:
- **"Actually hands-on coding"** -- Guhan wants real code, not a presentation or analysis document. The POC must produce working, demonstrable code.
- **"If we have to also get the additional resources for this, which we will have to work through"** -- Guhan is signaling that scaling this effort beyond POC will require internal approval for headcount or budget. The POC output is the justification.
- **"Show the demo"** -- A visual, interactive demonstration is expected. Not just a report.
- **"This is how we have done it, this is what is working"** -- Guhan wants the narrative to be concrete: here is the approach, here is the proof it works.
- **"It will help you get more confidence"** -- Framed diplomatically as giving Colin/BayOne confidence, but the real audience for the confidence-building is Guhan's internal stakeholders.

### The Estimation Model as a Key Deliverable

Guhan was very specific about one of the POC outputs -- an estimation model that can be used to make customer commitments:

> "One of the outcome I'm looking for, obviously there are like 70, 80, 100 pages, we [are] not expecting everything to be converted. We get a better idea of what it means to do that. In case of like, for example, we are able to do 10 [screens] with this AI... we are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this. With this, we can go back to the customer and promise that, okay, we will deliver this in this time."

This is a critical deliverable. Guhan wants:
1. **A ratio:** If X screens take Y days, they can extrapolate
2. **Customer-facing commitments:** The estimation model feeds directly into delivery promises to customers
3. **Scope awareness:** There are 70-100 screens total; nobody expects all to be done in POC, but the POC needs to produce enough data to extrapolate credibly

This means the POC must not only produce working conversions but also produce *measurable, repeatable* results that can be projected forward.

---

## 4. Colin's Positioning and How It Was Received

### "Proof Is in the Pudding"

Colin positioned the POC as an investment BayOne is making to demonstrate capability:

> "That's the investment I want to make for you, is to show that, because I know this is important. I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

This was well-received. Guhan did not push back or question it. The framing was effective because:
- It acknowledged that words and case studies are not enough
- It positioned BayOne as willing to put skin in the game
- It aligned with Guhan's stated need for a demo and real results

### Colin's At-Cost Commitment

Colin stated the POC will be done at cost to BayOne:

> "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us. So we'll make sure that we're at least proving this out to you."

This was stated plainly and not dwelt upon. It positions BayOne as investing in the relationship, not billing for exploration. Guhan did not react to this statement specifically, which suggests it was expected or already understood.

### Colin's Promise About Team Readiness Beyond POC

Colin proactively signaled that BayOne has depth beyond just him:

> "My team as well, the team that is working on Anand's CI/CD project, they've also done the same as me. So they'll have Cisco hardware, just to say that part out loud, in case you hear me say anyone else's name on the team. I'm going to be probably running this primarily, but at the same time, everyone else has the same NDA signage, the same everything. So just have that confidence in the team as well."

Guhan's response was notable -- he immediately tested whether this meant more people needed access now:

> "So you need access to more than you?"

Colin deflected this cleanly:

> "I don't think I will. I think, especially for the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go. So don't worry about that."

This exchange accomplishes two things: it plants the seed that BayOne can scale up if needed, while keeping the current ask small (just Colin for the POC). Smart framing -- it reduces Cisco's overhead now while showing capacity for later.

---

## 5. What Guhan Wants From the POC Output

Synthesizing all of Guhan's statements, the POC must deliver:

1. **Working code** -- Actual functional conversions of EPNM screens running in the EMS environment. Not mockups, not prototypes -- working, demonstrable code.

2. **A demo** -- Visual proof that the converted screens provide "the same experience, same visualization, everything, operations, everything, the way they would interact" as the original EPNM UI.

3. **An estimation model** -- A data-backed projection: X screens completed in Y days, therefore Z screens would take W days. This must be credible enough for Guhan to "go back to the customer and promise" delivery timelines.

4. **Confidence in the approach** -- Evidence that AI-assisted conversion handles the domain complexity of element management without introducing functionality gaps.

5. **Internal justification material** -- A demo and results package that Guhan can use to "get the additional resources for this, which we will have to work through." This is the meta-deliverable: the POC is a persuasion tool for Guhan's internal stakeholders.

---

## 6. Every Specific Next Step and Ownership

### Immediate (Same Day / Within 24 Hours)

| Action | Owner | Timeline | Notes |
|--------|-------|----------|-------|
| Write up POC proposal summary and send to Guhan/Selva | Colin | "Right after this meeting" | Colin committed explicitly: "I'll send out my summary right after this meeting" |
| Get firm date on Cisco laptop delivery | Colin + Rahul | Same day | Colin: "I'll try to get a firm date on the hardware so that way we can plan around it." Rahul: "There's a call... in the evening... we're gonna get that streamlined and get a firm date on it" |
| Resolve Cisco ID issue | Colin/Rahul via Cisco onboarding | Expected same day | Colin: "I think those are supposed to get resolved today" |

### Near-Term (Before Hardware Arrives, ~2 Weeks)

| Action | Owner | Timeline | Notes |
|--------|-------|----------|-------|
| Internally identify screens/ functionality for conversion | Selva's team | During the 2-week wait | Guhan suggested this: "Once we internally also will identify a few of the things for conversion" |
| Start initial conversations with the team for context | Colin + Selva's team | During the 2-week wait | Guhan: "Maybe we can start those initial conversations... in terms of providing context and everything. And by then, maybe your hardware arrives and then you can access things right away" |
| Set up Cisco-licensed AI tools for Colin | Guhan/Cisco | Before POC starts | Guhan: "I would suggest using some of the Cisco license... It will help you set up the licenses" |

### POC Phase (4 Weeks from Code Access)

| Action | Owner | Timeline | Notes |
|--------|-------|----------|-------|
| Access code and begin analysis | Colin | Immediately upon hardware setup | Code lives on Cisco systems; access requires Cisco hardware |
| Conduct initial code exploration (Cloud Code) | Colin | First phase of POC | Colin described the tooling progression |
| Scale to agent swarm (LangGraph) for deeper analysis | Colin | Mid-POC | When scope grows beyond single-agent capability |
| Convert identified screens (front-end + back-end) | Colin | Throughout POC | "Vertical" conversions -- UI and backend together |
| Produce working demo | Colin | End of POC | Guhan's primary deliverable expectation |
| Deliver estimation model | Colin | End of POC | X screens in Y days extrapolation |
| Periodic checkpoint calls | Colin + Guhan + Selva | Throughout POC | For clarification and progress visibility |

### Post-POC (Implied)

| Action | Owner | Timeline | Notes |
|--------|-------|----------|-------|
| Next call: connect with specific resources | Colin + Guhan | After laptop setup | Colin: "Once we have the install on the laptop, then we could set up a call to see the specific resources" |
| Guhan to use POC results for internal resource justification | Guhan | After POC | To secure headcount/budget for scaled effort |
| Scale BayOne team involvement if POC succeeds | Colin/BayOne | After POC | Colin's team is already NDA'd and will have Cisco hardware |

---

## 7. Timeline: The 4-Week POC and What Happens In Between

### The Two-Week Gap

Colin's Cisco laptop is expected within "a week or two." During this period, Colin cannot access Cisco code or systems. Guhan explicitly addressed this gap:

> "Everything that because you're going to wait for two weeks, you have signed NDA and everything. I'm trying to figure out what we can do in the next two weeks to get you going."

Guhan explored options -- he asked about non-Cisco laptop access but realized that would not work for code access. He then pivoted to a productive alternative:

> "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations... in terms of providing context and everything. And by then, maybe your hardware arrives and then you can access things right away."

So the two-week gap will be used for:
1. Cisco team identifies conversion candidates (screens and functionality)
2. Colin begins context-gathering conversations with the team
3. Colin sends POC proposal and gets alignment on scope
4. Hardware/ID logistics finalize

### The Four-Week POC Window

Guhan set the POC timeline at four weeks from code access:

> "I think we were looking at discussing about like, let's do it in four weeks, so then we [can make] some important decisions around this."

Colin initially suggested "a couple of weeks at most" but Guhan expanded it to four, framing it as enabling "important decisions." This is notable -- Guhan wants enough time for meaningful results, not a rushed proof. The four-week window gives Colin space to produce both the working conversions and the estimation model.

Colin did not push back on the four-week timeline; he accepted it readily.

### Total Elapsed Time

- **Weeks 1-2:** Hardware wait, context conversations, screen identification, POC proposal alignment
- **Weeks 3-6:** POC execution (4 weeks of active development from code access)
- **Week 6+:** Demo, estimation model delivery, decision on scaling

---

## 8. Colin's Ask for Navigational Help

In the closing moments, Colin made a specific request:

> "I would just need some help to navigate and know who to ask for what."

This is a practical ask. Colin is working within a large Cisco organization and needs to know:
- Who owns what parts of the codebase
- Who can grant access to specific systems
- Who has domain knowledge about specific screens/ functionality
- Who to escalate to when blocked

This ask was acknowledged but not explicitly assigned. It is implied that Guhan and Selva will help route Colin to the right people, but no specific "navigator" was designated. This could be a gap that surfaces during the POC if not addressed.

---

## 9. Security and Code Handling Agreements

### Code Stays on Cisco Hardware

Guhan was direct about this requirement:

> "This is a Cisco code, so we don't want this code to get out of Cisco."

He then immediately asked about Colin's access setup. The agreed model:

- **All work on Cisco-issued hardware:** Colin: "I'll have Cisco hardware that I'll do all Cisco work on. So that won't ever leave your hardware."
- **No code downloads to personal machines:** Guhan: "No downloading of the code, those kind of things."
- **Use Cisco-licensed AI tools:** Guhan: "Use the Cisco license or [approved] license for the [AI tools]... rather than using their separate own license." This was specifically about Claude and other AI tools -- Guhan noted Cisco already has licenses ("our engineers use it already") and wants Colin to use those rather than BayOne's own licenses.

Colin agreed to all of this without hesitation: "Of course, of course."

---

## 10. Closing Tone and Energy

The call ended on a notably positive and energized note. Several indicators:

**Colin's enthusiasm was genuine and specific:**
> "We're excited to do this. This is the fun [part] for us because this is work that you can see. That's the way I like to say it."

**Guhan reciprocated:**
> "Let's go from here... keep us posted closely on what you [do] in the space."

**Rahul reinforced urgency on the hardware:**
> "We're gonna get that streamlined and get a firm date on it."

The energy level was high. Both sides expressed genuine interest in moving forward. There was no hedging, no "we'll see" language from Guhan. The closing exchange had the quality of an agreed deal, not a tentative exploration.

Colin's final commitment was action-oriented and specific: summary right after the meeting, get the laptop date, set up the next call once hardware is in place. No ambiguity about what happens next.

---

## 11. Key Observations for Strategic Awareness

### The POC Is a Sales Tool for Guhan

Guhan explicitly framed the POC as a tool for internal persuasion. This means:
- The demo quality matters as much as the code quality
- The estimation model is not a nice-to-have; it is a core deliverable
- Guhan is betting on this POC to unlock resources; if it fails to persuade, the initiative stalls
- Colin should think about what makes a compelling internal demo, not just a technically correct one

### Independent Work Is Both Trust and Necessity

The "work independently" model is partly about trust in Colin's capability, but it is also a constraint -- the team genuinely cannot spare time. Colin should not interpret "periodic checkpoints" as understating available support. It really is periodic, not continuous.

### The "Vertical" Nature Changes the Scope

Selva's statement that front-end and back-end move together means the POC is not just a UI conversion exercise. Colin will need to understand and port back-end logic as well. The screens that have not been brought into EMS are missing "all the way down." This significantly increases the complexity and the value of what the POC would demonstrate.

### Colin's Tooling Description Was Received with Curiosity, Not Skepticism

Guhan and Selva listened to the Cloud Code / LangGraph agent swarm description with interest and asked a substantive follow-up question (about domain gaps). They did not express skepticism about the approach. The follow-up question about domain expertise was the right question to ask and Colin's answer appeared to satisfy it. This suggests Guhan is genuinely open to the AI-assisted approach, provided it delivers results.
