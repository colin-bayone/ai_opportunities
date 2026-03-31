# 01 - Context Build: Discovery Strategy

**Source:** /walmart/supply_chain_store_health_monitoring/source/kanchan_claude.txt, kanchan_walmart_tracker.md, walmart_discovery_call_prep.md
**Source Date:** 2026-03-30 (Pre-engagement context build from Colin's working session)
**Document Set:** 01 (Pre-Engagement Context Build)
**Pass:** Focused deep dive on discovery call strategy and competitive positioning

---

## Call Flow and Role Assignments

The call has three distinct phases with clear ownership.

### Phase 1: Surej Opens

Surej owns the opening. His job is to establish referral warmth (this came through someone he knows personally, and that social capital is the reason Troy is on the call at all), set the relationship context, and reset expectations early. The meeting title says "Showcasing BayOne's AI Capabilities," which Kanchan created and which does not match anyone else's intent. Surej needs to make clear in the first few minutes that this is a conversation to understand Troy's world and see if there is a fit, not a presentation or demo. That title reset is critical. If Troy walked in expecting a product walkthrough, Surej's opening is where that gets corrected before it becomes a problem.

### Phase 2: Colin Takes Over for Technical Discovery

After Surej sets the tone, Colin takes over. His job is a brief credibility setup (60 seconds maximum), then pivot into questions. The remainder of the call is Colin asking questions and listening. Goal is to understand Troy's environment, his pain, and where AI actually fits versus where it does not.

### Phase 3: Surej Closes

At the end, Colin summarizes what he heard back to Troy ("So if I'm hearing you right, the core challenge is X, and you're looking for Y"), asks if anything was missed or misunderstood, and proposes a concrete next step. Then Surej handles the relationship close.

---

## Colin's 60-Second Opening

The opening is scripted to accomplish three things in rapid succession: establish personal credibility through Coherent, connect that credibility to Troy's stated problem, then hand the conversation to Troy.

Colin's planned language:

> "Troy, thanks for making time for this. Before we dive in I want to give you a quick sense of where I'm coming from. My background is in AI and ML at the enterprise level. Before BayOne I led work at Coherent, a global manufacturing company, where we built AI solutions for field service and operations. One of the bigger ones was a predictive diagnostics system for industrial equipment across 40+ countries. Techs in the field could diagnose faults faster, we cut resolution time in half, and we significantly reduced unnecessary expert dispatches. I mention that because when I heard about your interest in health checks and early diagnostics for in-store machines, it felt like a very similar pattern. Different domain, but the same core problem. So I'd love to just understand your world and figure out if there's a real fit here."

Then hand it to Troy. No slides, no capabilities overview, no product pitch. Sixty seconds of "here is why I am credible for this conversation" and then it becomes Troy's floor.

The Coherent case study is the anchor. Colin led a 15-week program with a 12-person squad that built a multimodal SFT visual assistant for field-support diagnostics on 8K+ industrial laser systems across 40+ countries. Results included 50-60% reduction in ticket resolution time, first-pass fix rate from 71% to 91%, 50% reduction in expert dispatches, and $3.2M annual savings in SLA penalties. This is Colin's personal work from his prior organization. It is not a BayOne product or offering. It must be positioned as experience and expertise, never as something BayOne has on a shelf or can demo.

---

## Discovery Themes and Questions

### Theme 1: Understanding Troy's World

**Goal:** Get the lay of the land. What does his team actually do day to day?

- Can you walk us through what your team is responsible for at a high level? We've heard some broad strokes but I'd love to hear it from you.
- When you think about the biggest headaches your team deals with on a regular basis, what comes to mind?
- How many stores or locations are we talking about? What's the scale of the infrastructure you're managing?

**Why this comes first:** Colin does not walk in assuming he knows what Troy's team does. The information from Kanchan has already been wrong once (she described "robotics and automation" when Troy's actual role is Director of IT Operations in Supply Chain). Letting Troy describe his own world avoids building on bad assumptions.

---

### Theme 2: Current State (What Exists Today)

**Goal:** Understand what they already have before digging into the problem. The current state shapes everything, including whether the problem is proactive or reactive and whether the AI conversation is real or premature.

- What does your monitoring and alerting look like today? Is there a platform in place, something homegrown, or are you mostly finding out about issues after they happen?
- What kind of health data are these machines producing right now? Telemetry, logs, error codes, heartbeat signals? Or is it more of a black box until something breaks and a ticket gets filed?
- How does your ticketing and incident management work today? Is there a system of record?
- Have you explored any AI or ML approaches to this before? If so, what worked and what didn't?
- What tools or vendors are already in the mix for monitoring or diagnostics? Anything you've tried that fell short?

**Why current state comes before problem:** This was a deliberate reordering based on Colin's feedback. His reasoning: understanding what exists shapes whether the AI conversation is real or premature. If Troy describes a data-rich environment (telemetry, logs, existing monitoring platforms), then predictive models, anomaly detection, and smarter alerting are all viable and Colin's Coherent experience maps directly. If Troy describes a data-poor environment (reactive, no telemetry, manual processes, black box until something breaks), then the first problem is instrumentation and data infrastructure, not AI. Colin should be honest about that rather than selling AI where the foundation is not there.

The question about existing tools and vendors also serves a hidden purpose: it surfaces the competitive landscape naturally. If Troy names specific platforms he is already using or has evaluated, that tells you what has been tried, what failed, where the gaps are, and whether he is shopping for a turnkey product or looking for help building something custom, all without asking "are you looking to build or buy?" directly.

---

### Theme 3: The Problem (Health Checks and Early Diagnostics)

**Goal:** Understand whether this is a proactive initiative or a response to active pain. Then understand both the failure modes AND the resolution modes.

- Is proactive health monitoring something your team is building toward, or is this a response to problems you're actively dealing with right now?
- When a machine goes down today, how does your team find out? Monitoring picks it up, a ticket comes in from the store, or someone physically notices?
- What's the typical time from "something is wrong" to "it's fixed"? Where does the most time get lost in that process?
- Are there certain systems that are more problematic than others? POS, self-checkout, network, associate devices, or is it across the board?
- Here's something I think about a lot from my previous work. Predicting an outage is one piece, but what happens after the prediction matters just as much. If we know a self-checkout unit is going to fail, what does the resolution path actually look like? Is there a tech dispatched to the store, a remote fix, a parts replacement? How does that whole chain work today?
- What does downtime on these systems actually cost you? Not just dollars but operationally. Checkout lanes going dark, payment capability, associates unable to work?

**The resolution mode angle (critical insight):** Colin flagged this explicitly during the working session. Predicting an outage is only half the value. The other half is what happens after the prediction. If a prediction does not connect to a clear action (dispatch a tech, trigger a remote restart, swap a part), the value proposition changes significantly. At Coherent, the resolution was straightforward: a field technician was the one resolving it, and the AI tool made that technician faster and more accurate. At Walmart, it is a very different situation. Predicting that a self-checkout unit will fail is only useful if there is a resolution path that can act on that prediction. Does a tech get dispatched? Can something be fixed remotely? Is there a parts supply chain involved? How does the repair chain actually work? This question demonstrates to Troy that Colin has actually done this before, because most people pitching predictive maintenance have not thought past the prediction itself.

---

### Theme 4: What Success Looks Like

**Goal:** Understand what Troy is actually trying to achieve and how he would measure it.

- If we fast forward a year and this is working, what does that look like for your team?
- Are there specific metrics you're trying to move? Mean time to resolution, uptime percentage, number of incidents, something else?
- Is this primarily about reducing downtime, reducing cost, improving the associate or customer experience, or all of the above?

---

### Theme 5: Priority, Timeline, and Next Steps

**Goal:** Get a sense of how real and how urgent this is without putting Troy in an awkward spot.

- Where does this initiative sit in terms of priority for your team right now? Is this something you're actively trying to move on, or more in the exploratory phase?
- Is there a timeline or milestone driving this? For example, a budget cycle, a leadership mandate, a particular pain point that's creating urgency?
- What would a good next step look like from your perspective? We want to make sure we're useful to you and not just adding another meeting to your calendar.
- How does something like this typically get approved or funded on your side? (Only if the conversation is flowing naturally and Troy is being open. Do not force this.)

**How this was constructed:** Colin gave specific feedback that this theme should not create an awkward binary. The original version included questions like "do you have an internal data science or ML team?" which Colin rejected because if the answer is no, the implication is obvious and the call gets awkward. His guidance: "What you're doing is a yes or a no, and if it's a no, the call is going to get really awkward." Instead, these questions let Troy volunteer information about priority, timeline, budget, and approval process in a conversational way. Things he might share naturally if he is comfortable, not things he is being interrogated on. Colin specifically said: "The chances that on a discovery call he is going to share that are very low. If we can sneak it in or maybe slyly get him to say those things, that's a great thing."

---

## Closing the Call

- Summarize what you heard back to Troy. "So if I'm hearing you right, the core challenge is X, and you're looking for Y."
- Ask if there is anything missed or gotten wrong.
- Propose a concrete next step: "I'd like to take a few days, put together some initial thinking on how we might approach this, and come back to you with something more specific. Would that be useful?"
- Let Surej handle the relationship close.

**Why the next step matters:** BayOne has a capacity constraint. Colin's team is stretched and cannot take on immediate new work until the team grows. This is a leadership issue Colin has been pushing on for months. The next step framing ("let me put some thinking together and come back to you") buys time without sounding evasive. It positions BayOne as thoughtful rather than desperate, and it avoids making commitments on the call that the team cannot deliver on.

---

## Signals to Listen For

### Data-Rich vs. Data-Poor Environment
If Troy describes telemetry, logs, existing monitoring platforms, and health data flowing from machines, the AI layer conversation is real. Predictive models, anomaly detection, smarter alerting. This is where the Coherent experience maps directly. If Troy describes a reactive environment with no telemetry, manual processes, and black-box machines that only surface problems when something breaks and a ticket gets filed, the first problem is instrumentation and data infrastructure, not AI. Be honest about that.

### Resolution Path Clarity
If the resolution path is unclear or manual, predicting outages is only half the problem. If a prediction does not connect to a clear action (dispatch a tech, trigger a remote restart, swap a part), the value proposition changes significantly. Listen for how their repair and resolution chain works. This is one of the most important signals on the call.

### Vendor Mentions
If Troy talks about specific vendors or platforms he has already evaluated or is using, pay attention. That tells you what has been tried, what failed, and where the gaps are. It also tells you whether he is shopping for a product or looking for help building something custom, without you having to ask directly. This is how the competitive landscape question gets answered organically.

### Visual Assistant Connection
If the conversation naturally connects to the visual assistant / field support angle, bring the Coherent case study into more detail. Tech snaps a photo, model diagnoses the issue, returns a repair checklist. If Troy's techs are troubleshooting hardware in stores, this is directly relevant. Do not force it. Only expand if it connects naturally to what Troy is describing.

### Volunteered Budget, Timeline, or Approval Process
If Troy volunteers any of this, take note. On a first discovery call this is a bonus, not an expectation. Do not push for it.

---

## What NOT to Do

### No Capability Deck
Do not present a capability deck or try to cover everything BayOne does. This is discovery, not a showcase. The meeting title says "Showcasing BayOne's AI Capabilities" but that title was Kanchan's doing, does not match Surej's intent, and should be actively corrected in the opening. Troy was never promised a presentation. He was told verbally that BayOne has experience with predictive diagnostics and that "we can talk more deeply about how we did all of this." He is expecting a conversation, not a demo.

### No Promises
Do not promise anything on the call. "Let me take this back and put some thinking together" is always the right move. BayOne has a capacity constraint (team is stretched, needs to grow before taking on new work), and there is no reason to commit to anything until the opportunity is understood and the team capacity question is addressed.

### No Pretending Retail Experience
Do not pretend BayOne has retail-specific experience. Be honest that the pattern is the same (infrastructure monitoring, predictive diagnostics, health checks, early fault detection) but the domain is new. Colin flagged this directly: "We don't have experience connecting with retail things. That's just the fact of it." The credibility comes from the pattern being domain-agnostic at the architectural level, not from claiming to know POS protocols or self-checkout machine telemetry formats.

### No Talking More Than 30%
Do not let the conversation become BayOne talking more than Troy. If you are talking more than 30% of the time, course correct. This is Troy's floor. The entire purpose of the call is to listen and understand.

---

## Colin's Strategic Thinking: Competitive Positioning

### The Core Concern
Colin raised a specific concern about competitive landscape during the working session: Troy's team manages store technology infrastructure (POS, self-checkout, payment systems, associate devices, store networks, IoT), and there are massive vendors already in that space with turnkey solutions. Walmart almost certainly already has relationships with those vendors. Colin's exact framing: "I can't see them wanting to do a Python demo for how we can integrate a POS system, considering there's probably a trillion companies that do that as a ready-made, out-of-the-box system."

This concern shaped the entire discovery strategy. The call is not about pitching BayOne's capabilities. It is about understanding whether the opportunity is one where BayOne can differentiate, or one where an off-the-shelf vendor would be the obvious choice.

### Where BayOne Can Differentiate
The bucket that connects most directly to Colin's experience and most likely to be where BayOne adds value that an off-the-shelf vendor does not: predictive outages and real-time monitoring of store tech systems. Predictive models for a specific environment like Walmart's store infrastructure would need to be trained on their data, their failure patterns, their system configurations. That is not something you buy from a vendor. That is something you build. This is the lane where Colin's Coherent experience becomes a genuine differentiator rather than a nice story.

### Where BayOne Would Be Outmatched
Standard store technology solutions (POS integration, payment processing, network management) are dominated by massive vendors with off-the-shelf products. If Troy is shopping for a turnkey platform, BayOne is not the answer and should not try to be. The discovery questions are designed to surface this early so no one wastes time.

### How the Discovery Questions Resolve This
The competitive positioning question is answered organically through Theme 2 (current state) and Theme 5 (priority/timeline). If Troy names specific vendors he has evaluated or is using, that tells you the competitive landscape. If he describes wanting something custom built on his data, that is BayOne's lane. If he describes wanting a ready-made platform, that is not. The discovery framework is designed so that this becomes clear without ever asking "are you looking to build or buy?"

---

## Colin's Insight: Current State Before Problem

Colin explicitly reordered the discovery themes so that understanding the current state (Theme 2) comes before understanding the problem (Theme 3). His reasoning: what exists today shapes whether the AI conversation is real or premature. If there is no monitoring, no telemetry, no data infrastructure, then the first problem to solve is not AI. It is instrumentation. Leading with the problem before understanding the current state risks having a conversation about AI solutions when the foundation for AI does not exist yet. Getting the current state first lets Colin calibrate every subsequent question to the reality of Troy's environment.

---

## Colin's Insight: Resolution Modes

This was one of the most substantive strategic points Colin raised during the working session. His observation: just saying that something is going to have an issue or experience an outage is not sufficient. There has to be a way to act on that prediction.

At Coherent, the resolution was clear. A field technician was physically present, and the AI tool made that technician faster and more accurate at diagnosing faults and following repair procedures. The prediction connected directly to an action.

At Walmart, the resolution path is unknown. If the AI predicts a self-checkout unit is going to fail, then what? Does someone get dispatched to the store? Can the issue be fixed remotely? Is there a parts replacement chain involved? How long does that take? Who decides?

This matters because the value proposition of predictive diagnostics depends entirely on the resolution path. If you can predict a failure but the resolution takes three days because a part has to be ordered and shipped, the prediction is useful but the value ceiling is lower. If the prediction triggers an immediate remote fix or a same-day tech dispatch with the right part already in hand, the value is transformational.

Colin's instruction: ask this on the call. It demonstrates that he has actually done this work before, because most people selling predictive maintenance have not thought past the prediction itself.

---

## How to Handle Build vs. Buy

Colin gave explicit feedback on how not to handle this. The original call prep included a direct question about whether Troy has an internal data science or ML team, or whether the work would need to be done externally. Colin rejected this approach.

**What was wrong with the original approach:** It creates a binary. If Troy says "we're looking for a ready-made platform," the call gets awkward. If he says "we don't have internal ML capabilities," the implication is obvious and does not need to be stated. Either way, you end up in a yes-or-no moment that can kill the conversation.

**What Colin wants instead:** Weave it into natural conversation about timeline, priority, and how things get approved. Let Troy reveal his situation through the way he talks about next steps, urgency, and organizational process. If he is actively trying to move on this and has a budget cycle coming up, that tells you something. If he is in pure exploration mode with no timeline, that tells you something different. Neither answer is bad, but you learn more by letting it emerge than by asking directly.

**The practical execution:** Theme 5 questions are soft, conversational, and framed from Troy's perspective ("What would a good next step look like from your perspective?"). The hardest question (how does something like this get funded on your side?) is gated behind the condition "only if the conversation is flowing naturally and Troy is being open." Do not force it.

---

## The Capacity Constraint and Next-Step Framing

If the opportunity is real, BayOne does not currently have the bandwidth to take on immediate new work. Colin's team is stretched and needs to grow before taking on additional projects. This is a leadership issue that Colin has been pushing on for months. It is not Kanchan's problem and should not be positioned as a limitation to Troy.

This affects next-step framing. The proposed close ("I'd like to take a few days, put together some initial thinking on how we might approach this, and come back to you with something more specific") is not just good discovery etiquette. It is also a practical necessity. Colin cannot commit to timelines or deliverables on this call because the team capacity to deliver does not currently exist. The "take it back and put thinking together" framing buys time to assess whether this opportunity is worth prioritizing and what it would take to staff it, without sounding evasive or unprepared.
