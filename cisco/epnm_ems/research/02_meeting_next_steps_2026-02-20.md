# 02 - Meeting: Next Steps

**Source:** /cisco/epnm_ems/source/guhan_selva-2-20-2026.txt
**Source Date:** 2026-02-20 (Follow-Up Technical Meeting)
**Document Set:** 02 (Second meeting, deeper technical detail on EPNM-to-EMS conversion)
**Pass:** Focused deep dive on next steps and action items

---

## 1. Colin to Write POC Proposal Based on Both Meetings

Colin explicitly committed to writing a formal POC proposal immediately after this meeting. His exact framing: "I'll put together a proposal to you to make sure, based on all of our discussion today, I've been taking minutes, I can put together the POC proposal for you." He further specified: "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us."

Key details on the proposal's purpose:

- Colin positioned this as a **proof of capability**, not a theoretical pitch: "I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."
- Guhan reinforced that the POC needs to produce a **working demo with hands-on code**, not just an analysis: "The POC would, so basically this is also about actually hands-on coding and showing the [result]. That way, if we have to also get the additional resources for this, which we will have to work through, this will help."
- Guhan explicitly stated the demo serves an internal justification purpose: "Show it, even to make it, show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."
- The proposal draws from both the February 9 meeting (initial discovery with Guhan) and this February 20 follow-up (deeper technical discussion with Guhan and Selva).

**Status:** Firm commitment from Colin. He stated he would send a summary "right after this meeting" and write up the proposal based on his meeting minutes.

---

## 2. Colin to Send Meeting Summary Immediately After the Call

Colin committed to sending a written summary of this meeting same-day: "Like I said, I'll send out my summary right after this meeting, and then we can go from there."

This is a separate deliverable from the POC proposal -- a near-term summary of what was discussed and agreed, to keep all parties aligned before the formal proposal is written.

**Status:** Firm commitment, same-day delivery.

---

## 3. Code Access to Be Arranged by Cisco Team

Both parties agreed that Colin needs access to the EPNM and EMS codebases as a prerequisite for the POC. Selva confirmed: "Yeah, we need to provide you with access to things."

Several constraints were explicitly discussed regarding code access:

- **Security requirement -- Cisco hardware only:** Guhan stated: "This is a Cisco code, so we don't want this code to get out of Cisco." He specified: "No downloading of the code, those kind of things."
- **Cisco-licensed AI tools only:** Guhan emphasized: "I would suggest using some of the Cisco license [tools] rather than outside of Cisco." He clarified further: "Use the Cisco license or approved license for the [AI tools], rather than using their separate own license." Colin agreed without hesitation: "Of course, of course."
- **Code access is blocked on hardware delivery:** Colin noted he cannot access the code until his Cisco laptop arrives because he does not currently have Cisco hardware. He said: "I'm already working on this announced project for the CICD board. I'll have my Cisco laptop probably within a week or two. I think they're just finishing up with that setup."
- **Legacy code lacks documentation:** Selva acknowledged this explicitly: "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the [new system]." Colin's response: "For the most part, especially with anything legacy, almost always is missing documentation. It's way easier to do it now... But if it doesn't exist, it's no problem. We still do the same exploration. Because documentation doesn't always tell the truth."

**Status:** Agreed in principle. Blocked on Cisco laptop delivery and Cisco ID provisioning. Guhan and Selva will arrange access once hardware is in place.

**Open question:** What specific code repositories or systems will Colin need access to? This was not specified -- Colin said he would need help navigating: "I would just need some help to navigate and know who to ask for what."

---

## 4. Initial Conversations with Engineering Team for Context Transfer

Both Guhan and Selva made clear that the engineering team is under heavy load and cannot invest significant time in this effort, but they committed to providing initial context.

Selva stated: "The team as well, the team that is working on [the platform], they need to give you the context and everything. They will provide you with that. And then if you can take that independently and come back with your analysis and put that up with what you've come up with, that would be good."

Guhan explicitly set the expectation of independence: "You'll be able to, once we get the context right, you'll be able to move ahead on your own to do this analysis and come back."

Selva further noted: "At the moment the team is also on critical [work] or a platform, if you think so, the team itself will not be able to [invest] time here. But of course, they need to give you the context and everything."

The plan for initial conversations:

- Context transfer conversations would happen during the two-week waiting period for hardware, or immediately once hardware arrives.
- Guhan said: "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations... in terms of providing context and everything. And by then, maybe your hardware arrives and then you can access things right away."
- Colin described the format he envisions: "I think probably once we have the [Cisco laptop] installed, then we could set up a call to see the specific resources."
- Colin promised minimal disruption: "We don't need too much of their time, I promise. I think this is straightforward as soon as we can get our eyes on the [code]."

**Status:** Agreed in principle. Timing depends on hardware delivery and Cisco's internal prioritization of which screens to convert.

---

## 5. Cisco Laptop Hardware Timeline to Be Confirmed

The Cisco laptop is a critical-path dependency for the entire POC. Colin does not yet have the hardware, and multiple aspects of the engagement are blocked on it.

Colin stated: "What I can do today, myself, to help this is I'll try to get a firm date on the hardware so that way we can plan around it." He further noted: "I've done all onboarding and completed all onboarding except for having the hardware and my Cisco ID. I think those are supposed to get resolved today."

There was specific mention of a call happening the same evening to resolve this. An unnamed third party (likely from BayOne operations) said: "There's a call in the evening... we're going to get that streamlined and get a firm date on it." They elaborated: "It's more [that the company] is saying they're trying to get a date... trying to get that Cisco laptop to Colin, so I'm going to try to see if we can speed that process up."

Colin estimated timeline: "I'll have my Cisco laptop probably within a week or two."

**What the laptop unblocks:**

- Code access to EPNM and EMS repositories
- Cisco ID provisioning (also pending)
- Access to Cisco-licensed AI tools (Claude and others already approved within Cisco)
- Access to cloud instances of the running systems
- Compliance with Cisco security requirements (no code on non-Cisco hardware)

**Status:** Firm commitment from Colin to get a confirmed date the same day. A call was scheduled for the evening of February 20 to expedite. Colin estimated one to two weeks for delivery.

---

## 6. Cisco ID Provisioning Still Pending

Separate from the laptop hardware, Colin's Cisco ID had not yet been provisioned at the time of this meeting. Colin said: "The two things that I'm missing... I've done all onboarding and completed all onboarding except for having the hardware and my Cisco ID."

He noted the Cisco ID is relevant because: "Even probably for access to the cloud instance, I'm guessing that would be preferable if it's using the Cisco ID."

Colin believed this would also be resolved soon: "I think those are supposed to get resolved today, but once I have those, that way... I can let you know immediately."

**Status:** Pending. Expected resolution same day or shortly after. Dependency for code access and cloud system access.

---

## 7. Four-Week Decision Window (Reinforced from Set 01)

The four-week decision window originally established in the February 9 meeting was explicitly reinforced by Guhan in this meeting. Guhan stated: "I think we were looking at discussing about like, let's do it in four weeks, so then we made some important decisions around this, right? So that is one. Right, so let's do what we can in the four weeks, right? That's a good spread."

This four-week window (starting from approximately the February 9 meeting) means:

- **Approximate deadline: early to mid March 2026** for demonstrating POC results.
- Results from the POC feed directly into Guhan's decision-making about how to handle customer demands for legacy UI preservation.
- The POC must produce a working demo within this window, not just an analysis.

Colin had suggested a shorter timeline for the initial POC work: "I'm hoping something we can do in a couple of weeks for you at most." However, Guhan extended this to the full four weeks, which gives more breathing room especially given the hardware delivery delays.

**Status:** Firm timeline. Both parties acknowledged it and are working toward it.

---

## 8. Two-Week Waiting Period and What to Accomplish During It

Guhan explicitly identified the two-week hardware waiting period as an opportunity to prepare. He said: "You're going to wait for two weeks, you have signed NDA and everything. I'm trying to figure out what we can do in the next two weeks to get you going."

Guhan's proposed use of this time:

- **Send the POC proposal:** Colin can write and deliver this without Cisco hardware.
- **Cisco to identify specific functionality for conversion:** Guhan said: "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations."
- **Start context transfer conversations:** Guhan suggested beginning knowledge transfer before hardware arrives, though he acknowledged access to code itself would not be possible.
- **Explore non-Cisco-hardware access:** Guhan briefly explored whether Colin's personal laptop could access certain systems, but quickly recognized that would not work: "You have a laptop that's not Cisco, but I can get them to the network, I'm not sure about that. Okay, got it."

What cannot happen during this period:

- No code access without Cisco hardware and Cisco ID.
- No direct exploration of the codebase.
- No running of Cisco-licensed AI tools against the code.

**Status:** Both parties acknowledged this gap. Guhan is trying to maximize productivity during the wait; Colin committed to delivering the proposal and confirming hardware dates.

---

## 9. Priority Screens to Be Identified by Cisco Team

Selva made clear that the Cisco team would select which screens to target for conversion. Selva stated: "We will focus on the ones that we've not brought in yet and identify a few screens, like Guhan has said."

Selection criteria were specified:

- **Focus on functionality not yet migrated to EMS:** Selva said: "Just to add more value to this exercise, we will focus on the ones that we've not brought in yet."
- **Missing reports as a concrete starting point:** Selva mentioned: "I have some missing reports that I've not brought in from the old thing. So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new."
- **Full vertical slices, not UI-only:** Selva emphasized: "It's not a UI alone. There is a... along with it comes the backend logic. Only then... it needs to have a fully functional thing."
- **End-to-end working functionality:** Selva said: "Make it work end-to-end, right? So that will be the goal for this exercise."

Guhan framed the expected outcome of the screen selection and conversion: "We get a better idea of what it means to do that. In case of, for example, we are able to do 10 [screens] with this AI... we are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this. With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

**Status:** Cisco's responsibility. Selva and the team will identify specific screens during the two-week waiting period. No specific date commitment for when this list would be delivered.

---

## 10. Running Systems to Be Provided When Ready

Colin asked about access to running instances of both EPNM and EMS. Selva confirmed that running systems would be provided: "When we get to that stage, we guess we will provide the system to try this out."

Colin clarified that running systems are not needed immediately: "Only when we're ready because what we'd want to do... there's two sides to it."

Colin connected running systems to automated UX testing: "If you want us to be able to test and guarantee the UI, part of this is also the testing of it to make sure that it is faithfully been converted. We can do the automated UX testing as well, even if it's a precursor to formal UX testing from your team, but that can save you some time too, if that's a desirable thing."

Selva's response was positive but deferred: "When we get to that stage, we guess we will provide the system to try this out, yes."

**Status:** Agreed in principle. Running systems will be provided when the POC reaches the testing stage. Not an immediate need.

---

## 11. Automated UX Testing Offered as Additional Value-Add

Colin proactively offered automated UX testing using Playwright as part of the POC deliverables: "We can do the automated UX testing as well, even if it's a precursor to formal UX testing from your team, but that can save you some time too, if that's a desirable thing."

Later, when Guhan asked about ensuring no domain or functionality gaps, Colin described the automated testing approach in more detail: "From a visuals perspective, we can definitely have that already, but that's what we have the automated inspection tools. So it uses Playwright for the most part. Basically doing screen [capture] things, even as we're doing it. We don't even need to have the application running. We can just have certain screens loaded up with data, make sure that we can check the functionality there."

Selva responded with qualified interest: "Sure. I mean, when we get to that stage."

**Status:** Offered by Colin, received positively but no firm commitment from Cisco to include it in the POC scope. This is a differentiator Colin is offering, not something Cisco explicitly requested.

---

## 12. Periodic Checkpoints Agreed

Selva explicitly stated: "We'll have periodic checkpoints to help clarify anything more and also keep the rest of the folks [aware] with the progress."

This means:

- Regular check-ins between Colin and the Cisco team during the POC.
- Checkpoints serve two purposes: (1) clarify technical questions, and (2) keep stakeholders informed of progress.
- No specific cadence was established (weekly, biweekly, etc.).

**Status:** Firm agreement on the concept. No specific schedule set.

---

## 13. Cisco-Licensed AI Tools to Be Used (Security Requirement)

Guhan established a clear security boundary: all AI tools used must be Cisco-licensed or Cisco-approved. His key statements:

- "There is a... you have Cloud and [something] and as part of our engineers use it already." (Acknowledging that Claude is already available within Cisco.)
- "I would suggest using some of the Cisco license to build up anything other than outside of Cisco."
- "Use the Cisco license or approved license for the [AI tools], rather than using their separate own license."

Colin agreed fully: "Of course, of course. So maybe what we can do, because this is -- so I'm already working on this announced project for the CICD board. I'll have Cisco hardware that I'll do all Cisco work on. So that won't ever leave your hardware. And likewise with AI tools, definitely. We'll use those from day one if we can, and that way we can keep that kind of security bubble intact."

Guhan noted that Cisco already has Claude and other coding tools available: "[Cisco has] Cloud and [tools] and as part of our engineers use it already... [and] coded [Copilot] service."

**Status:** Firm security requirement from Cisco. Colin accepted without reservation. This must be reflected in the POC proposal as an operating constraint.

---

## 14. BayOne Team Beyond Colin Already NDA-Cleared

Colin proactively informed Guhan and Selva that other team members are ready: "My team as well, the team that is working on Anand's CICD project, they've also done the same as me. So they'll have Cisco hardware, just to say that part out loud, in case you hear me say anyone else's name on the team."

He specified: "Everyone else has the same NDA signage, the same everything. So just have that confidence in the team as well."

Guhan asked whether additional access would be needed: "So you need access to more than you?" Colin responded: "I don't think I will. I think, especially for the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go."

**Status:** Informational. For the POC, Colin will work solo. For post-POC scaling, the team is already cleared. No action needed now, but this is relevant for the proposal's discussion of scaling.

---

## 15. Post-Meeting Sequencing: The Critical Path

Based on the meeting discussion, the critical path from this meeting to POC delivery is:

1. **Same day (Feb 20):** Colin sends meeting summary; Colin confirms hardware date via evening call.
2. **Week of Feb 20-27:** Colin writes POC proposal and sends to Guhan and Selva.
3. **Weeks 1-2 (Feb 20 - ~Mar 6):** Waiting period for Cisco laptop and Cisco ID. During this time:
   - Cisco team internally identifies priority screens/functionality for conversion.
   - Initial context transfer conversations may begin (without code access).
   - Colin receives and confirms hardware.
4. **~Mar 6 onward (hardware arrival):** Colin gets code access, begins exploration with Cisco-approved AI tools.
5. **Within 4 weeks of Feb 9 (~Mar 9):** POC results expected -- working demo of converted screens with estimation methodology for remaining work.

**Critical dependency:** The four-week clock started at the February 9 meeting, but hardware may not arrive until approximately March 6. This compresses the actual working time for the POC to potentially one week or less if hardware delays persist.

Guhan appeared to acknowledge this tension implicitly by saying "let's do what we can in the four weeks" rather than demanding a completed POC by that date.

---

## Summary: Action Item Table

| # | Action Item | Owner | Timeline | Status | Dependency |
|---|-------------|-------|----------|--------|------------|
| 1 | Send meeting summary from Feb 20 call | Colin | Same day (Feb 20) | Firm commitment | None |
| 2 | Confirm Cisco laptop delivery date | Colin + BayOne ops | Same day (Feb 20 evening call) | Firm commitment | None |
| 3 | Write POC proposal based on Feb 9 and Feb 20 meetings | Colin | Within days of Feb 20 | Firm commitment | None |
| 4 | Resolve Cisco ID provisioning | Cisco onboarding / BayOne ops | Expected ~Feb 20 | Pending | None |
| 5 | Identify priority screens/functionality for conversion | Selva + Cisco engineering team | During 2-week waiting period | Firm commitment | None |
| 6 | Arrange code access for Colin | Guhan / Selva | After laptop delivery | Firm commitment | Cisco laptop + Cisco ID |
| 7 | Set up Cisco-licensed AI tools for Colin | Guhan / Cisco IT | After laptop delivery | Firm commitment | Cisco laptop |
| 8 | Initial context transfer conversations with engineering team | Selva's team + Colin | During or after waiting period | Firm commitment | Priority screen identification |
| 9 | Provide running systems (EPNM and EMS instances) | Selva's team | When POC reaches testing stage | Agreed in principle | POC progress |
| 10 | Deliver POC results -- working demo + estimation methodology | Colin | Within 4-week window (~Mar 9) | Firm commitment | Items 4-8 above |
| 11 | Establish periodic checkpoint cadence | Both parties | After POC work begins | Agreed in principle | POC kickoff |
| 12 | Deliver Cisco laptop hardware | Cisco IT / procurement | ~1-2 weeks from Feb 20 | Pending confirmation | None |

---

## Open Questions and Unresolved Points

1. **Compressed POC timeline.** The four-week decision window was established from the February 9 meeting (~Mar 9 deadline), but hardware may not arrive until ~Mar 6. This leaves potentially less than one week of actual hands-on time. Neither party explicitly addressed this compression. Will the four-week window be extended if hardware is delayed?

2. **Which specific screens will be selected?** Selva committed to identifying priority screens but did not specify how many or which ones. Missing reports were mentioned as one concrete example. The total number for the POC is undefined.

3. **Cloud instance access mechanism.** Colin mentioned needing cloud access ("for access to the cloud instance, I'm guessing that would be preferable if it's using the Cisco ID"), but the specific mechanism for accessing the running systems was not discussed.

4. **Cisco-licensed AI tools: which ones specifically?** Guhan referenced Claude and "coded [Copilot] service" as available within Cisco, but the specific approved tool list was not enumerated. Will Colin be able to use Claude Code (his primary tool) under a Cisco license, or will he need to use a different tool?

5. **Non-Cisco-hardware access during waiting period.** Guhan briefly explored whether Colin could access systems without the Cisco laptop but concluded it probably would not work. No alternative was found. Is there any read-only or documentation-level access that could be granted during the waiting period?

6. **POC success criteria.** Guhan described the desired outcome as estimation capability ("if 10 screens take X days, we can extrapolate"), but formal success criteria were not defined. What constitutes a successful POC -- a working demo of N screens? An estimation model? Both?

7. **Backend complexity for selected screens.** Selva confirmed that the conversion is "not just UI" and requires backend work as well. The extent of backend work for the selected priority screens is unknown until those screens are identified.

8. **Who specifically on the engineering team will provide context?** Selva and Guhan referenced "the team" multiple times but did not name specific individuals who would participate in context transfer conversations. In the February 9 meeting, Varel's team was identified as owning the UI conversion work. Will those same people be involved here?

9. **Automated UX testing scope.** Colin offered Playwright-based automated UX testing, and Selva expressed conditional interest. Whether this is in scope for the POC or deferred to a later phase is not settled.

10. **Post-POC commercial model.** Colin explicitly said the POC is "at cost to us" (BayOne investment). The commercial terms for the work that follows a successful POC were not discussed in either meeting.

---

## Distinguishing Firm Commitments from Aspirational Statements

**Firm commitments (specific, with owners and implied or explicit timelines):**

- Colin will send the meeting summary same-day.
- Colin will write the POC proposal.
- Colin will confirm the hardware date via the evening call.
- Cisco will provide code access once hardware is in place.
- Selva's team will identify priority screens for conversion.
- Selva's team will provide initial context to Colin.
- All work will be done on Cisco hardware with Cisco-licensed tools.
- Colin will handle the POC solo (no additional team access needed).
- Periodic checkpoints will occur.

**Aspirational or conditional statements (dependent on external factors, less specific):**

- The four-week decision window as a hard deadline (Guhan said "let's do what we can" rather than demanding completion).
- Running systems will be provided "when we get to that stage."
- Automated UX testing will happen "when we get to that stage."
- Context transfer conversations "maybe we can start those initial conversations" -- conditional on Cisco identifying the screens first.
- Hardware arriving within "a week or two" -- Colin's estimate, not a confirmed date.
- Non-code activities during the two-week waiting period -- Guhan explored this but found no clear path beyond the proposal writing.
