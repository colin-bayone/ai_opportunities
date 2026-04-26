# 09 - Meeting: Guhan's Scope Signals and Asks

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on Guhan's three substantive asks: memory/load review, DPM coverage, product-management positioning

---

## Overview

This pass extracts the three substantive asks Guhan surfaced during the 2026-04-24 POC progress check-in, plus the supporting moments around them that establish his framing, tone, and structuring of next steps. These three asks are not equivalent in nature: one is a technical gate on production endorsement, one is a scope-expansion signal for the post-POC engagement, and one is the commercial unlock that converts the POC into a customer-facing product commitment. Together they define the next phase of the engagement.

Guhan's tone throughout was engaged, rigorous, and partnership-oriented. He asked precise, well-formed questions, structured the next steps explicitly with reasoning, and twice characterized BayOne as "amazing partners." He framed the work as "very comprehensive" and said he was "really anxious and looking forward to the demo." He absorbed Colin's "good or great" pulse-check question with the answer "It's completely in the direction that we were looking" — he did not commit to "great" yet, and reasonably so, because the demo and code review are still ahead.

---

## Ask 1: Memory and Load Review (Technical Gate Before Production Endorsement)

### Direct quote

> "First of all, it seems like a lot of people have gone in, looking at what's generated. And I'm sure we wouldn't have done this without the AI part. Right, Anu? Yes. So a couple of things. Can we review this? What is getting generated? I mean, this is generated, but what is running on the system? Right? Let's look under the code with somebody in the [Cisco] team and see because we want to be conscious of how much additional memory this is taking, how much additional load is putting on the system and things like that. We need to look at from that point of view."

### What Guhan is actually asking

Guhan is distinguishing between two questions that often get conflated in agentic-AI work:

1. **What is getting generated?** — the artifact question. What code, configuration, and assets has the agentic workflow produced?
2. **What is running on the system?** — the runtime question. What is the operational footprint of that generated code once deployed inside EPNM/EMS?

He explicitly draws this distinction with the phrase "this is generated, but what is running on the system?" That is the heart of the ask. He is not satisfied with reviewing the generated artifacts; he wants the Cisco team — specifically the EMS team — to look "under the code" and assess the operational impact:

- **Memory footprint:** "how much additional memory this is taking"
- **System load:** "how much additional load is putting on the system"
- **And things like that** — implicitly, anything else that would affect production stability, performance, or scalability

### Reasoning behind the ask

EPNM and EMS are network-management products that customers deploy on their own infrastructure. Any UI conversion that adds non-trivial memory or CPU overhead is a potential blocker for production endorsement. Guhan is responsible for what gets promised to customers (see Ask 3) — he cannot have the Cisco product management team commit to functionality that quietly degrades the runtime envelope of the application. This is a gate before the work is endorsed for production.

He is also signaling that AI-generated code carries a specific class of risk that requires deliberate human review. His phrasing "I'm sure we wouldn't have done this without the AI part" acknowledges the AI as the enabler, but immediately pivots to "let's look under the code with somebody in the team" — he wants experienced Cisco engineers to validate the runtime characteristics, not just the functional correctness.

### How Colin responded

Colin did not push back on the ask; he absorbed it as a natural next step and connected it to the broader code-review request that Guhan structured later in the meeting. Colin then offered something additive: he said he had architectural-decision content ready that he had "didn't want to bring up for the POC," including observations about technical debt that has been carried over to EMS — for example, "different ways to do the same thing" such as how columns are handled in tables. He framed this as something the Cisco team could fix along the way once they were involved, and noted that team involvement could "definitely accelerate the timeline even further."

This response is well-aimed at Guhan's concern: it shows that BayOne is already thinking past artifact generation into runtime quality and architectural cleanup, and that BayOne welcomes the Cisco team's deeper involvement rather than treating code review as an audit hurdle.

### Strategic implication

This is a **technical gate**. Until Guhan and the EMS team have looked under the code and confirmed the memory/load profile is acceptable, the work is not endorsed for production. Crucially, Guhan structured the code review to happen **before the demo** (see Next Steps section below) for a specific reason — he wants the Cisco team free to ask questions and the BayOne team free to respond before the demo turns into a public commitment moment. The demo is therefore positioned as the milestone that follows technical validation, not the milestone that triggers it.

---

## Ask 2: Device Performance Management (DPM) Coverage (Scope Expansion Signal)

### Direct quote

> "Other thing that we have to do also is from the scoping point of view, if it's comprehensive, now that we have this, now we can see something running, then just not slides. So yesterday, I think sometime back, talked about DPM also. It's a key thing, right? The customers use the performance management quite a bit. So we will see that is all part of the whatever you have generated or planning to."

Colin: "It's not in the POC, but..."

Guhan (interrupting Colin's clarification, then taking it in stride): "It's not part of the POC, you're right, but that's in the gap."

Guhan continued: "Yeah, yeah. So you want to exclude the gap, whatever will get implemented finally that has got the key areas come out."

### What Guhan is actually asking

Guhan is signaling that **Device Performance Management (DPM)** is a key functional area that customers use heavily, and that any final implementation must cover it. He confirms his own acronym immediately by saying "performance management quite a bit" right after "DPM" — "DPM" was actually said and it stands for Device Performance Management. This is the third functional area beyond inventory and fault management, which were the two areas in the POC scope. **This is new scope for the engagement narrative.**

His phrasing "you want to exclude the gap, whatever will get implemented finally that has got the key areas come out" is mangled by the speech-to-text but the meaning is clear: the final implementation (post-POC) must cover the key customer-facing areas, and DPM is one of them. He is asking for confirmation that DPM is captured in BayOne's gap analysis even if it is out of POC scope.

### Reasoning behind the ask

Guhan is thinking past the POC. He explicitly frames the moment: "now that we have this, now we can see something running, then just not slides." The POC has graduated the conversation from slide-deck speculation to running software, so the scoping conversation now needs to address what the **final** implementation covers, not just what the POC covers. DPM is high on his list because customer usage of performance management is heavy.

He is also doing his own commercial math: if he is going to walk into product management and say "we have this covered" (Ask 3), the "this" needs to include DPM, because product management will immediately ask whether customers' most-used capability area is part of the migration story.

### How Colin responded

Colin confirmed two things:

1. DPM is **not in POC scope** — the POC focuses on inventory and fault management.
2. DPM **is in the gap analysis** — BayOne's comprehensive mapping of EPNM and EMS captured DPM as part of the 14-repository sweep, including UI gaps, feature gaps, backend gaps, and data gaps.

Later in the conversation, when Guhan circled back with "as we go through the gap, I mean, there are things that we need to build the back into. So that's probably captured in your gap, I think," Colin confirmed: "It's 42. If you want to know the number, 42 gaps for back-end."

The "42 backend gaps" number is load-bearing here. It tells Guhan that BayOne's gap analysis is precise, quantified, and ready to feed scope decisions for the next phase — including DPM coverage.

### Strategic implication

This is a **scope expansion signal**. The engagement narrative going forward needs to position DPM as the third functional area alongside inventory and fault management. The POC will validate the conversion approach on inventory and fault; the gap analysis already maps DPM; the next-phase scope conversation should treat DPM as the obvious next functional area to convert. BayOne should expect DPM to come up in the next-phase pricing and timeline discussion, and should preemptively reference the gap analysis as the basis for sizing it.

It is also worth noting Guhan's framing "from the scoping point of view, if it's comprehensive" — he is using "comprehensive" as the test. The 14-repository sweep, the 42 backend gaps, the UI/feature/data gap files — all of that comprehensiveness is what unlocks Guhan's confidence that DPM and other customer-facing areas are tractable.

---

## Ask 3: Product-Management Positioning (Commercial Unlock)

### Direct quote

> "Based on this, we are going to go to the product management and say, hey, we got this covered. You can go promise the customers that they will get this functionality, right? So I want to ensure that that is taken care of."

### What Guhan is actually asking

This is the engagement's **commercial unlock**. Guhan is telling BayOne, plainly, what he intends to do with the POC results: walk into the Cisco product management organization and tell them the EPNM-to-EMS UI conversion is covered, and that product management can in turn commit to customers that the functionality will be delivered. He is asking BayOne to ensure the work supports that conversation — that there are no surprises, no overlooked customer-critical areas, no runtime concerns that would make him retract the commitment.

### Reasoning behind the ask

Cisco product management owns the customer-facing roadmap promises. For Guhan's engineering organization to influence what product management commits to, Guhan needs evidence-grade confidence that the migration approach works, performs, and is comprehensive. The POC plus the gap analysis gives him that evidence package. His sentence structure — "based on this, we are going to go to the product management and say, hey, we got this covered" — places the POC as the foundation and product management as the audience.

The explicit "I want to ensure that that is taken care of" is Guhan asking BayOne to be a partner in making this conversation succeed. It is not a casual remark; it is a stake in the ground. It also explains why Guhan is so engaged in the technical gate (Ask 1) and the scope coverage (Ask 2) — both feed directly into whether his product-management conversation lands.

### How Colin responded

Colin's response — "Of course. Of course." — was direct and committed. He then immediately pivoted to additive value: he had architectural-decision recommendations ready that he had held back from the POC because he didn't want to make those calls without the team involved. He framed Cisco team involvement as the accelerator: "with the team getting involved with us, that's a really easy way. We can make that go a lot quicker than not. So we can definitely accelerate the timeline even further with that in mind."

This is exactly the right tone for the commercial unlock: BayOne acknowledges the responsibility, signals additional value already prepared, and positions deeper Cisco team partnership as the lever that accelerates delivery.

### Strategic implication

This is the **commercial unlock**. Once Guhan walks into product management with "we got this covered," and product management commits to customers, the engagement converts from POC to funded next-phase delivery. BayOne's job between now and the demo is to make sure Guhan can deliver that message with full confidence:

- The technical gate (Ask 1) must pass — memory and load must be acceptable.
- The scope coverage (Ask 2) must be visible — DPM and other customer-critical areas must be clearly mapped in the gap analysis.
- The demo must show running software that matches the EMS backend identically — Guhan reconfirmed this during the meeting: "And then when you do that, it will still talk to the same backend. We're not spawning different backends, right?" Colin: "Absolutely. Absolutely. Identically the same."

If those three conditions hold, Guhan's product-management conversation succeeds and the engagement scales.

---

## Supporting Guhan Moments

### "Very comprehensive, really anxious and looking forward to the demo"

> "I mean, it's very comprehensive, really anxious and looking forward to the demo."

This came right after Colin shared the 42-backend-gaps number. Guhan's word "comprehensive" is the operative test — it is the same word he used in the DPM ask ("if it's comprehensive"). The 14-repository sweep, the UI/feature/backend/data gap files, the 250-file output, and the quantified 42 backend gaps all combine to satisfy his comprehensiveness test. "Anxious" here means eager, not worried — he is leaning forward into the demo.

### "Amazing partners" (said twice)

> "And you guys have been amazing partners, so I'm happy to do it."
> "You guys really have been amazing partners."

Guhan said this twice in rapid succession, the second time as an unforced reinforcement. This is a partnership signal — he is characterizing BayOne as a delivery partner, not a vendor under audit. The repetition matters; it is the kind of language that gets remembered when budget, scope, and next-phase decisions are made.

### Acknowledgment of the BayOne work effort

> "Thanks for joining in late to upgrade us. We were back to back and Zara and they have picked us earlier in the day. We couldn't get to it. I know you're on the East Coast. Thanks for taking this later in your evening."

Guhan opened the substantive portion of the call by thanking Colin for taking the meeting late in his East Coast evening, after the Cisco team had been back-to-back all day. This acknowledgment of effort and time-zone burden is consistent with the partnership tone of the call and reinforces that Guhan sees the engagement as a mutual investment.

### "Good or great" framing

Colin asked, mid-meeting, "Is it good or is it great? Not yet. Not yet. Just trying to pulse check."

Guhan's answer: **"It's completely in the direction that we were looking."**

This is a careful, well-calibrated answer. He did not commit to "great" — that would be premature before the demo and code review. He did commit to direction, which is the more important commitment at this stage. Direction means the fundamental approach (UI toggle, identical backend, comprehensive gap mapping, agentic workflow) is the right approach. Once direction is confirmed, "great" becomes a function of execution quality, which is what the demo and code review will assess.

### Backend gaps follow-up

> "And then as we go through the gap, I mean, there are things that we need to build the back into. So that's probably captured in your gap, I think."

Guhan circled back to confirm that backend gaps — things that need to be built back into EMS to support the converted UI — are captured in BayOne's gap analysis. Colin confirmed with the precise number: 42 backend gaps. This number anchors the next-phase conversation. It also reinforces Ask 2: the gap analysis is the source of truth for what the final implementation must cover, including DPM.

---

## Guhan's Structuring of Next Steps

Guhan structured the next steps with explicit sequencing and reasoning, which is itself worth capturing because it tells BayOne how he thinks the engagement should be paced:

### The structure

1. **Monday:** Cisco team provides access to the EPNM and EMS virtual machines (the only remaining access blocker on BayOne's side).
2. **Code review (before the demo):** Guhan said "let's have the coder be right there. So what? Somebody in the... Yeah, I think the next thing is Monday they are waiting to give provide access to the systems and everything and I think, well, instead by what Wednesday we will have like a demo or something. I mean, we can do the coder be either part of... I mean after the demo or if you want to do it before? It's good before the day, even if you want to push it by the mobile base." Despite the speech-to-text mangling, the intent is clear: Guhan prefers code review **before** the demo, even if it means pushing the demo by a day.
3. **Demo (potentially moved to Thursday):** Guhan said "the demo itself may move to Thursday or so" to accommodate the code review and to find a slot that is "time zone friendly for East Coast, PST and India" — meaning Cisco PST morning, which would be Cisco India team's noon.

### Guhan's reasoning for code review before demo

> "The reason is that way, that way if there's anything the team has, we can go back to the team and also ask questions, right? So that way they are free to root."

"Free to root" is mangled by the speech-to-text. Interpreting against context, Guhan means "free to engage" or "free to investigate" or "free to roll" — i.e., the Cisco team is free to ask questions, raise concerns, and dig into the code without the pressure of an in-progress demo. Doing code review first lets BayOne and Cisco resolve any code-level questions in private before the demo turns into a public commitment moment.

This is a sophisticated piece of meeting choreography. Guhan is protecting both sides:

- **BayOne** is protected from being surprised in the demo by a code-level question that should have been worked out beforehand.
- **Cisco's engineering team** is protected from feeling pressured to either rubber-stamp or publicly challenge the work in front of stakeholders.
- **The demo itself** is protected as a milestone moment focused on demonstrating running software, not adjudicating code quality.

### Speech-to-text variants for "code review"

The transcript contains several mangled variants — "designated coding," "court review," "coder be right there" — all of which mean "code review." Guhan's intent in every instance is the same: experienced Cisco engineers reviewing the BayOne-generated code before it is endorsed.

### Next-step touchpoint

Guhan committed to touching base on Tuesday after the Monday access provisioning, talking to the Cisco team about the code review, and coordinating the demo timing.

---

## Synthesis: Why These Three Asks Define the Next Phase

The three asks, taken together, form a complete decision framework for the next phase of the engagement:

| Ask | Type | What it gates | What BayOne must deliver |
|---|---|---|---|
| 1. Memory/load review | Technical gate | Production endorsement | Code accessible for review; BayOne available to walk Cisco engineers through architectural decisions; runtime impact characterized honestly |
| 2. DPM coverage | Scope expansion | Next-phase scope and pricing | DPM clearly mapped in gap analysis; positioning that treats DPM as the natural third functional area beyond inventory and fault |
| 3. Product-management positioning | Commercial unlock | Customer-facing commitment and funded next-phase delivery | Demo that shows running software identical to EMS backend; gap analysis that gives Guhan defensible coverage claims; a partnership posture that supports Guhan inside Cisco |

The asks are sequenced in the order they will be tested:

- The **technical gate** is tested first, in the code review before the demo.
- The **scope coverage** is tested at the demo and in the post-demo scoping conversation.
- The **commercial unlock** is activated after both prior tests pass, when Guhan walks into product management.

DPM is the new piece of the engagement narrative. Until this meeting, the BayOne-side framing emphasized inventory and fault management as the POC scope. Guhan's surfacing of DPM as a "key thing" that "customers use quite a bit" promotes it to first-class status in the next-phase scope. Future BayOne-side materials — proposals, scope documents, pricing models, executive summaries — should treat inventory, fault management, and DPM as the three primary functional areas of the EPNM-to-EMS UI conversion, with the gap analysis as the reference for sizing each one.

---

## Tone Summary

Guhan in this meeting was:

- **Engaged** — leaning into the work, asking precise questions, not phoning it in
- **Rigorous** — distinguishing artifact from runtime, asking for code-level review, structuring next steps with reasoning
- **Partnership-oriented** — twice characterizing BayOne as "amazing partners," thanking Colin for the late-evening time, framing Cisco team involvement as collaborative
- **Commercially honest** — not committing to "great" before the evidence is in, but committing to direction
- **Forward-leaning** — already thinking past the POC to product management, customer commitments, and the full scope including DPM

This is the tone of a senior Cisco leader who sees the engagement as one he wants to land successfully, both for his own organization and for the customers who depend on the migration. BayOne should treat this meeting as confirmation that the engagement has graduated from "vendor delivers POC" to "partner co-delivers a customer-facing product commitment."
