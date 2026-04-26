# 09 - Meeting: Guhan and Selva — Deep Profile

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused profile of everything Guhan and Selva said, asked, and requested

---

## Selva — Profile from this call

### What Selva said (substantive content)

**Opening rapport and tone-setting.** Selva engaged Colin in extended pre-meeting banter — covering the difficulty of squeezing the call in ("it's at 9 o'clock on Monday"), Colin's wife and how to thank her ("she just wants her time. That's something that money can't buy"), and Colin's justification for pushing through ("if we get these done, these come less frequently, at least for me. That's my justification to get more people"). Selva participated warmly throughout, demonstrating an established personal rapport with Colin.

**Framing of access status as the "final hurdle."** When Colin opened on the access situation, Selva said: *"You guys, everything is good on the access side. I know that's something we're going to address, right? ... So I think it's just kind of the final hurdle for us. But the team's been really responsive. I think it was just bad timing today on the Friday."* He explicitly characterized the remaining VM access work as the *only* outstanding blocker and made a point to defend the team's responsiveness — attributing the delay to Friday timing rather than to the team failing to deliver.

**Time-zone window framing.** Selva offered nuanced commentary on time-zone coordination: *"I know with IST, if we would have met on Friday, he would have been real late at night. Same thing with my team and IST. That's the hard part about time zones, right?"* He went on: *"the good thing is everyone gets a head start on Sundays effectively. The toughest part is whenever daylight savings time kicks in and that's always the most rough."* He drew on his own past experience managing a large Malaysia team to explain how the daylight-savings crossover actually flips the working window.

**Cultural commentary on work ethics.** Selva volunteered an extended observation about European work ethic versus US: *"when you go to places like Paris, or Europe in general, and you just see their work ethics, it's actually, you say like US is the only place that actually doesn't eat lunch."* He referenced his prior organization having many employees in Italy and joked, with disclaimer that he is part Italian, that *"those guys could not work... You'd message them, and it's like 2 p.m. their time, and they're like, yeah, I'm home for the day."* This was paired with the framing that in the US, *"We do lunches. We just do working lunches. Eat at our desk."*

**Validation question on the toggle and backend.** This was Selva's most operationally important contribution. He asked: *"So one thing, the POC, you have the classic view and then you have the... current way to do the UI, right? So you switch back and forth... And then when you do that, it will still talk to the same backend. We're not spawning different backends, right?"* Colin confirmed: *"Absolutely. Absolutely. Identically the same. Yes."* Selva then closed the loop: *"And as we talked about this, just reconfirming that song. Yes. Yes."* The point of the question was to validate, on the record and with Guhan present, a key technical assumption that had been previously discussed.

**Backend gap follow-up.** After Colin confirmed the toggle hits the same backend, Selva continued the technical scope thread: *"And then as we go through the gap, I mean, there are things that we need to build the back into. So that's probably captured in your gap, I think."* This teed up Colin's "42 gaps for back-end" answer.

**Handling of demo timing pivot when Guhan asked for code review first.** When Guhan introduced the code review request and the implication that the demo might slip, Selva absorbed it without resistance: *"Yeah, I think the next thing is Monday they are waiting to give provide access to the systems and everything and I think, well, instead by what Wednesday we will have like a demo or something. I mean, we can do the coder be either part of... I mean after the demo or if you want to do it before?"* He made the offer to flex on sequencing rather than defend the prior plan. After Guhan said "before," Selva accepted and committed: *"And maybe the demo itself may move to Thursday or so. And it would have to be like, I mean, time zone friendly for East Coast, PST and India. So it would have to be our morning, I guess... For him it would be more like noon for us. And also give them heads up about the plans of doing the code review. And we'll take it from there."*

**"Amazing partners" comment.** When Guhan called BayOne amazing partners, Selva immediately echoed: *"You guys really have been amazing partners."* He then went into the most quotable line of his contribution.

**"Good or great" pulse-check ask.** Following the partnership affirmation, Selva asked Colin pointedly: *"And I just have one quick question. Is it good or is it great?"* He clarified the intent: *"Just trying to pulse check."* This is a deliberate barometer question — he was not asking about the technical work, he was asking Colin to characterize the relationship/momentum on a record where Guhan could hear the answer.

**Proactive coordination commitments.** Selva took on the operational follow-ups without being asked:
- *"let me talk to the team on that"* (regarding the code review)
- *"give them heads up about the plans of doing the code review"*
- Implicit: he is the one talking to the India team about provisioning the code review window and adjusting demo timing.

**Closing.** *"Yes, she'll work out yes, it's a column for your morning time."* (transcription is mangled — likely "Yes, that'll work out, it's a column for your morning time" or similar concession that the new slot works.) *"sounds good."*

### What Selva asked / requested

1. **Toggle-validates-same-backend question** — Confirmed publicly, with Guhan present, that the POC's UI toggle hits the same backend (no backend forking).
2. **Backend gap question** — Confirmed that backend build-out items are captured in the gap analysis ("there are things that we need to build the back into. So that's probably captured in your gap, I think").
3. **Code-review-vs-demo sequencing offer** — "We can do the coder be either part of... after the demo or if you want to do it before?" (offered to flex sequencing).
4. **Pulse-check question** — "Is it good or is it great?" (relationship/momentum barometer).
5. **Coordination role offers** — "let me talk to the team on that" and "give them heads up about the plans of doing the code review" (volunteered to handle India team logistics).

### Selva's engagement style (observed patterns)

- **Warmth and established rapport.** Engaged in extended personal banter with Colin pre-meeting (wife, gifts, schedule pressure). The "Hi Selva. Happy Friday... Hopefully Selva, you're smiling as always" greeting and "the world could be falling apart, but Colin and Selva will always be smiling" line indicate he is the warmth anchor of this Cisco-BayOne dynamic.
- **Validates technical assumptions before letting things move forward.** The toggle-backend question is a pattern: he does not let a technical claim sit unconfirmed in front of Guhan. He repeats / closes the loop ("just reconfirming that song. Yes. Yes.").
- **Acts as buffer between Guhan and BayOne when Guhan is absent.** For the first ~half of this call, Selva was the entire Cisco presence. He held the meeting open, set the tone, and absorbed the access status update as a "final hurdle" rather than a problem.
- **Operationally hands-on.** Proactively tracking access provisioning, demo logistics, code review scheduling, and time-zone slot selection. Not delegating — owning.
- **Keeps interactions positive but does not let technical points slide.** The toggle/backend question is friendly in tone but absolutely substantive. He will smile while asking the question that pins down the technical commitment.
- **Cultural fluency.** Comfortable mixing personal heritage references (part Italian), prior team experience (Malaysia), and observations about Indian and European work culture. Reads as senior/experienced, not junior operational staff.
- **Comfortable deferring to Guhan on scope and process decisions.** When Guhan asked for code review before demo, Selva did not push back on behalf of BayOne or the schedule — he absorbed and adjusted.

### How to work with Selva going forward

- **Treat his validation questions as confirmations, not challenges.** When Selva asks "is X true?" in front of Guhan, the right response is to answer cleanly and let him close the loop. He is making sure the technical position is on the record, not testing Colin.
- **Use him as the proxy when Guhan is unavailable.** Selva will hold the meeting, set tone, and bring Guhan up to speed asynchronously. If Guhan is back-to-back, Colin can run substance through Selva and trust it lands.
- **Match his rapport tone.** He values warmth, humor, and personal conversation. Do not skip the pre-meeting banter — it is part of how he assesses the relationship. The "smiling Colin and Selva" framing is one Selva is actively maintaining.
- **Keep him in the loop on operational changes; he is the coordinator.** Demo timing, code review scheduling, access provisioning, time-zone slots — Selva owns these. Updates on any of them should go to him first.
- **Answer his "good or great" pulse-checks with substance.** When he asks how it is going, give him a real answer he can carry forward — he is using the answer with Guhan and the broader team.
- **He is the one talking to the India team about the code review.** The expectation set in this call is that Selva — not Colin, not BayOne — will warm up the India team for the code review and the new demo slot. Do not duplicate that outreach without coordinating with him.

---

## Guhan — Profile from this call

### What Guhan said (substantive content)

**Acknowledgment that the work is comprehensive.** Guhan's first substantive observation, after reviewing what Colin had shown: *"First of all, it seems like a lot of people have gone in, looking at what's generated. And I'm sure we wouldn't have done this without the AI part."* He recognized the volume of work product and explicitly named that the AI-driven approach was the only way to produce it at this scale and speed.

**Memory and load review request (gating ask, full quote).** This was the most substantive ask of the call:

*"So a couple of things. Can we review this? What is getting generated? I mean, this is generated, but what is running on the system? Right? Let's look under the code with somebody in the [EMS] team and see because we want to be conscious of how much additional memory this is taking, how much additional load is putting on the system and things like that. We need to look at from that point of view."*

This is a gate, not curiosity. He wants a code review with the EMS team that specifically evaluates the generated output's memory footprint and system load before he is comfortable moving to the demo.

**Scoping discipline — DPM coverage request.** Immediately after the memory/load ask: *"Other thing that we have to do also is from the scoping point of view, if it's comprehensive, now that we have this, now we can see something running, then just not slides. So yesterday, I think sometime back, talked about DPM also. It's a key thing, right? The customers use the performance management quite a bit. So we will see that is all part of the whatever you have generated or planning to."* When Colin clarified DPM is not in the POC, Guhan immediately reframed: *"It's not part of the POC, you're right, but that's in the gap."* And then, the discipline line: *"So you want to exclude the gap, whatever will get implemented finally that has got the key areas come out."* Translation: he wants the gap analysis to clearly call out, separately from the POC scope, everything that *will* need to get implemented finally — with the key customer-facing areas (like DPM) called out specifically.

**Product-management positioning framing — the commercial unlock.** Directly following the DPM thread:

*"Based on this, we are going to go to the product management and say, hey, we got this covered. You can go promise the customers that they will get this functionality, right? So I want to ensure that that is taken care of."*

This is the most strategically important sentence in the call. Guhan is explicitly stating the deliverable's purpose: it is the artifact he takes to product management to authorize customer commitments. The work product is in service of an internal Cisco commercial decision, not just a technical POC.

**"Amazing partners" comment (said in two adjacent turns, effectively twice).** When Colin thanked Guhan for joining late: *"Thanks for joining in late to upgrade us. We were back to back and Zara [Zahra] and they have picked us earlier in the day. We couldn't get to it."* Then, after Colin volunteered to handle questions during the demo: *"And you guys have been amazing partners, so I'm happy to do it."* Selva immediately echoed it, after which Guhan said it as well in the closing thanks. It is a deliberate, public partnership affirmation.

**"Really anxious and looking forward to the demo" line.** After Colin gave the "42 gaps for back-end" answer: *"I mean, it's very comprehensive, really anxious and looking forward to the demo."* The word "anxious" reads as eager-anticipation in this context, not nervous-anxious. He coupled it with the assessment "very comprehensive" — a positive characterization of the gap analysis depth.

**Backend gap follow-up.** Guhan asked Colin to confirm the backend gap items are captured. Colin's response — *"It's 42. If you want to know the number, 42 gaps for back-end"* — landed as a direct numeric answer to the question Guhan had teed up.

**Structuring of next steps — code review BEFORE demo, with reasoning.** When Selva offered to do the code review either before or after the demo, Guhan was firm: *"It's good before the day, even if you want to push it by the [day base]. The reason is that way, that way if there's anything the team has, we can go back to the team and also ask questions, right? So that way they are free to root [engage/route]."* He explicitly justified the sequencing — review first so the team can surface questions and engage on the answers before the demo locks in expectations.

**Delivery package mechanism question.** Earlier in his contribution, Guhan asked: *"Let's, I hope you're going to take a CIPP cap [transcription unclear] out of this or something, and then you're going to, I know what's the delivery package mechanism? What's it, what's it, I mean, how is it going to look like in the system?"* He wanted to understand how the converted UI is actually packaged and delivered into the EMS system. Colin answered with the toggle explanation: *"in the system, the way that we have it right now, it's just a simple UI toggle... whenever you get to the inventory or the fault management screens, there's now just a toggle at the top and you switch back and forth... we kept all the Angular there. So it's just a bunch of packages in parallel."* Guhan's response: *"Super, super. Okay, so let's have the coder be [code review] right there."*

**Closing thanks and forward-looking commitment.** *"Thanks for taking this time to walk us through this and expect more questions during the demo. I can handle them. I can handle them."* (The "I can handle them" is Colin's commitment to absorb the questions.) Guhan: *"Yeah. Looking forward. Thank you."* And finally: *"Thank you so much. Thank you Colin. Thanks for that day. Have a good weekend."*

### What Guhan asked / requested

1. **Memory and load review (gating ask).** Code review with the EMS team that explicitly assesses the generated output's memory footprint and system load impact, before the demo.
2. **DPM coverage confirmation (scope ask).** Confirm that DPM is captured in the gap analysis as a future implementation item, even if it is not in the POC.
3. **Code review before demo (process ask).** Sequence the code review ahead of the demo so the team has time to surface questions and re-engage on answers.
4. **Confirmation that backend gaps are captured.** Implicit ask that surfaced the "42 gaps for back-end" answer.
5. **Delivery package mechanism explanation.** "What's the delivery package mechanism? How is it going to look like in the system?"

### Guhan's engagement style (observed patterns)

- **Joins late, contributes densely.** He missed the first portion of the call because he was back-to-back with Zahra earlier in the day. When he arrived, he made the call's most consequential asks within minutes and structured the entire follow-up sequence.
- **Asks rigorous questions but frames them collaboratively.** The memory/load review is a serious gate, but he frames it as "let's look under the code with somebody in the EMS team" — a collaborative working session rather than an audit.
- **Thinks in terms of customer commitments and product-management implications.** Every technical decision is evaluated for its downstream impact on what product management can promise customers. The work product is, to him, an input to a commercial commitment decision.
- **Strong on operational discipline (memory/load, system impact).** He immediately raised resource consumption as a first-order concern. He is not going to accept "it works" as sufficient — he wants to know what it costs to run.
- **Will publicly affirm the partnership when warranted.** The "amazing partners" comment was unprompted and reinforced by repetition. He reads the work and reacts to substance.
- **Late arrival pattern suggests heavy schedule; respect his time when offered.** His apology — "We were back to back and Zahra and they have picked us earlier in the day. We couldn't get to it" — and the meeting context (he carved out evening East Coast time on a Friday) signal his time is constrained. When he is on the call, the agenda should serve him.
- **Treats backend gaps and DPM as the long-tail scope items he wants accounted for.** DPM is the canary — he wants to see how the gap analysis handles the things that matter to customers but are out of POC scope. If DPM is well-captured, he trusts the rest.
- **Reads the work product, not just the slides.** The line "now we can see something running, then just not slides" is telling. He wants running code and concrete artifacts. Slides alone will not move him.
- **Sequences process for risk reduction.** Code review before demo, not after, because he wants the team's questions surfaced before the demo locks in expectations.

### How to work with Guhan going forward

- **Lead with substance; he reads the work product, not just the slides.** GitHub commits, gap analysis files, and running code are the artifacts that move him. Slides are at best a navigation aid.
- **Anticipate his rigor questions and pre-answer them where possible.** Memory footprint, system load, delivery packaging mechanism, behavioral parity — these will recur. Have answers (and ideally measurements) ready before he asks.
- **Frame everything in terms of customer/product-management implications when relevant.** When presenting scope, capability, or gap analysis, tie it to "what can product management promise customers." That is the language he is using internally.
- **Treat his "asks" as gates, not curiosity.** The memory/load review, the DPM coverage, the code review before demo — these are not optional. Treat them as deliverable prerequisites and pull them forward in the schedule.
- **The product-management positioning he offered is the engagement's commercial unlock — protect that thread.** "We got this covered. You can go promise the customers" is the sentence that justifies a broader-scope engagement. Every artifact going forward should support Guhan's ability to take that message to product management.
- **Respect his time when he gives it.** He carved out evening East Coast Friday for a 30-minute call. Do not waste any of that window on anything he could have read asynchronously.
- **Document decision rationales explicitly.** Colin's "human in the loop" framing — "Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly" — is exactly what Guhan needs to see. Continue calling out which decisions are AI-generated and which are human-rationalized.
- **Surface scope discipline proactively.** Guhan's "you want to exclude the gap, whatever will get implemented finally that has got the key areas come out" is the standard. The gap analysis should clearly separate POC scope from the broader-scope items, with the key customer-facing areas (DPM and others) called out by name.

---

## Joint Dynamics (Selva + Guhan together)

How they interact with each other and with Colin:

- **Selva opens; Guhan closes the substantive content.** Selva held the meeting for the first portion, set tone, validated the technical baseline. Guhan arrived and structured the substantive next-steps and gates.
- **Selva validates technical assumptions; Guhan validates scope and customer implications.** Selva's "same backend, right?" is an architectural confirmation. Guhan's "DPM is in the gap, right?" is a scope/customer-coverage confirmation. Together they triangulate completeness.
- **They agree visibly (no disagreement observed in this call).** When Guhan introduced the code review gate, Selva did not push back. When Selva asked the toggle/backend question, Guhan let it stand. There is no observable friction between them.
- **Guhan defers operational logistics to Selva.** Selva is the one who will talk to the India team about the code review and adjust the demo to Thursday. Guhan structures *what* needs to happen; Selva owns *when* and *with whom*.
- **They both reinforce the partnership framing.** "Amazing partners" was said by Guhan and immediately echoed by Selva, then reinforced again at the close. This is a deliberate, paired affirmation — both of them, on the record, with Colin.
- **Selva's "good or great" pulse-check sits inside Guhan's frame.** Selva asked the question after Guhan had already made the substantive asks. This is Selva using Guhan's presence to get a relationship reading on the record, not a private check-in.
- **Both treat the work as exceeding expectations.** Guhan: "very comprehensive, really anxious and looking forward to the demo." Selva: "amazing partners." Guhan: "I'm sure we wouldn't have done this without the AI part." The signal is that the POC's depth has earned the broader-scope conversation.

---

## Open Questions for Colin

Items Colin should consider asking or addressing in subsequent interactions:

1. **What is Guhan's exact title and reporting line?** Set 07 had this as "exact title TBD." The product-management framing in this call ("we are going to go to the product management and say, hey, we got this covered") suggests he sits adjacent to but not inside product management — confirm.
2. **What does Guhan need to take to product management? Specific deliverable format?** He clearly intends to package the gap analysis + POC + scope coverage into a product-management ask. Does he want a one-page brief? A deck? A read-out meeting? Should BayOne pre-build that artifact for him?
3. **Who in the Cisco team does the memory/load review?** Ramesh? Praveen? The "let's look under the code with somebody in the [EMS] team" was non-specific. Confirm with Selva who runs that session.
4. **Will DPM coverage be expected in the broader-scope conversation?** Almost certainly yes. Should BayOne pre-build a DPM gap brief — the same depth as the fault management / inventory analysis but scoped to performance management — so it is ready when the broader-scope conversation opens?
5. **Is the "delivery package mechanism" question fully answered?** Colin gave the toggle answer and Guhan said "super, super," but the production deployment story (release packaging, version compatibility, rollback) was not covered. Worth proactively addressing in the next deliverable.
6. **What is the threshold for "great" vs "good"?** Selva's pulse-check was answered with "Not yet. Not yet." — meaning Colin reserved "great" for after the demo and broader-scope conversation. What does Colin need to deliver to claim "great" at the next checkpoint?
7. **Is there a scheduled product-management read-out?** Guhan implied he will take this to product management, but no date was set. Worth asking Selva for the timeline so BayOne can have the right artifacts ready.
8. **Code review session format.** Live walkthrough? Async PR review? Recorded session? Selva will set this up but the format will affect how BayOne prepares — get clarity on the next touch.
