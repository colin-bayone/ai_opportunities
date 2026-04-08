# 02 - Meeting: Engagement Model and Constraints

**Source:** /cisco/epnm_ems/source/guhan_selva-2-20-2026.txt
**Source Date:** 2026-02-20 (Follow-Up Technical Meeting)
**Document Set:** 02 (Second meeting, deeper technical detail on EPNM-to-EMS conversion)
**Pass:** Focused deep dive on engagement model and practical constraints

---

## 1. Engineering Team Cannot Invest Significant Time

Guhan stated the team bandwidth constraint directly and without ambiguity. This is the single most important structural fact about how this engagement will work:

> "At the moment the team is also on critical or a platform, if you think so, the team itself will not be able to miss time here. But of course, they need to give you the context and everything. They will provide you with that."

The constraint breaks down into three parts:

1. **The team is on "critical platform" work.** The speech-to-text renders this awkwardly, but Guhan is saying the engineering team is doing critical platform-level work -- likely the core EMS microservices platform. This is not optional work they can deprioritize.

2. **The team cannot invest time on the EPNM conversion.** They physically do not have bandwidth. This is not a matter of willingness; they are already committed.

3. **The team WILL provide context.** Guhan drew a clear line: context transfer is the team's obligation, but execution is BayOne's. The team gives the knowledge; BayOne does the work.

**Practical implication:** BayOne cannot plan an engagement model that requires engineering pairing, embedded collaboration, regular working sessions, or ongoing Q&A with individual engineers. The model must be: receive a context dump, go away, come back with results.

---

## 2. BayOne Must Work Independently After Context Transfer

This was stated by both Guhan and Selva, and reinforced by Colin's agreement. The expectation is explicit:

Guhan: "And then if you can take that independently and come back with your analysis and put that up with what you've come up with, that would be good."

Selva (paraphrased from context): "Hopefully, you'll be able to, once we get the context right, you'll be able to move ahead on your own to do this analysis and come back."

Colin confirmed this model works for his methodology: "We don't need too much of their time, I promise. I think this is straightforward as soon as we can get our eyes on the code."

**What "independently" means here:**
- BayOne receives initial context (codebase access, identification of target screens, architecture orientation)
- BayOne performs its own exploration, analysis, and prototyping
- BayOne comes back with findings, working code, and/or demos
- The Cisco team does NOT need to be available for ongoing questions during the work

**What "independently" does NOT mean:**
- No access to anyone for clarification. Checkpoints are explicitly part of the plan (see Section 3).
- No guidance on what to work on. Guhan and Selva committed to identifying and prioritizing the screens for conversion.

---

## 3. Periodic Checkpoints for Progress and Clarification

Guhan established a checkpoint cadence as part of the engagement model:

> "We'll have periodic checkpoints to help clarify anything more and also keep the rest of the folks average with the progress."

The word "average" is a speech-to-text error -- the intended meaning is "apprised" or "aware." Guhan wants periodic checkpoints to serve two purposes:

1. **Clarification:** BayOne can surface questions, ambiguities, or blockers encountered during independent work.
2. **Visibility:** The broader team stays informed of progress. This suggests Guhan intends to keep his engineering team and possibly management aware of BayOne's progress, even though the engineers are not actively involved in the work.

**What was NOT defined:**
- The specific cadence of checkpoints (daily, weekly, biweekly)
- The format (meetings, written updates, async)
- Who attends (just Guhan, or Guhan + Selva, or broader team)

**Open question:** The checkpoint cadence should be proposed in the POC proposal. Given the 4-week decision window (see Section 9), weekly checkpoints would be a reasonable default, with async updates more frequently if needed.

---

## 4. Code Access Is Required and Confirmed

Both sides agreed that BayOne needs access to the source code for both EPNM (legacy) and EMS (modern). This was a direct question from Colin and a direct confirmation from Guhan:

Colin: "From a code access perspective, because for us to convert and move over to the new, we'll probably need to know a little bit more about the new and what the code looks like. Is that going to be possible for a POC to get access to things?"

Guhan: "Yeah, we need to provide you with access to things."

**What code access entails:**
- Access to the EPNM codebase (legacy, Java backend, Dojo/JavaScript frontend)
- Access to the EMS codebase (modern, Java backend, Angular frontend)
- Presumably via Cisco's internal version control system (likely Git-based, but not specified)
- Access must be on Cisco hardware through Cisco infrastructure (see Section 6)

**Dependency:** Code access requires the Cisco laptop and Cisco ID, both of which were pending at the time of this meeting (see Section 7).

---

## 5. Legacy Product Lacks Design Documentation

Guhan set expectations explicitly about the state of documentation for the legacy EPNM product:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view. Most of it. That will be the bulk of the challenge here."

This is a significant statement. Guhan is telling BayOne upfront that:

1. **There is no design documentation** at the level needed to understand the legacy system's architecture, component relationships, or implementation details.
2. **The code IS the documentation.** The team's knowledge lives in the codebase itself and in the engineers' heads.
3. **Navigating the code is the primary challenge.** Guhan explicitly framed this as "the bulk of the challenge" -- not the conversion itself, but understanding the legacy system well enough to know what to convert.

Colin responded pragmatically: "For the most part, especially with anything legacy, almost always is missing documentation... It's much easier now. But the only reason why I ask is just to help inform the context whenever we do it to save us some time. But if it doesn't exist, it's no problem. We still do the same exploration. Because documentation doesn't always tell the truth."

**Practical implication for the engagement model:** The initial context transfer from the team cannot rely on documentation. It will need to be verbal orientation, architectural walkthroughs, or engineer-guided code tours. Once that initial context is provided, BayOne's AI tooling becomes the mechanism for exploring and documenting the codebase -- which is part of the value proposition Colin presented.

---

## 6. All Work on Cisco Infrastructure with Cisco-Licensed Tools

This constraint was reinforced from the first meeting (Set 01) and reiterated here. Guhan stated it clearly:

> "Because this is a Cisco code, so we don't want this code to get out of Cisco."

The speech-to-text then becomes heavily garbled, but the reconstructed exchange is approximately:

Guhan: You probably have access to VPN and everything. There is a... you have Claude and... as part of... our engineers use it already. [Garbled] ...even Copilot Enterprise. So I would suggest using some of the Cisco-licensed [tools] rather than outside of Cisco.

Colin: "Of course, of course."

Guhan then made the requirement more specific:

> "No downloading of the code, those kind of things."

And extended it to AI tooling:

> "And also use the Cisco license or approval license for the... and others, rather than using their separate own license."

Colin confirmed compliance: "So I'm already working on Anand's project for the CICD board. I'll have my Cisco laptop probably within a week or two. I think they're just finishing up with that setup. So I'll have Cisco hardware that I'll do all Cisco work on. So that won't ever leave your hardware. And likewise with AI tools, definitely. We'll use those from day one if we can, and that way we can keep that kind of security bubble intact."

**The constraints stack as follows:**
1. No code leaves Cisco infrastructure (hard requirement)
2. No downloading code to personal machines (hard requirement)
3. AI tools must be Cisco-licensed (e.g., Copilot Enterprise, Claude if Cisco has licensed it)
4. Personal AI tool licenses cannot be used on Cisco code
5. All work happens on Cisco-provisioned hardware

**Key detail from the garbled speech-to-text:** Guhan appears to reference that Cisco engineers already use "Claude" and "Copilot Enterprise" (or similar). This is significant because it suggests that the AI tools Colin's methodology requires may already be available within Cisco's licensed tooling. The exact tools remain to be confirmed once Colin has hardware and access.

**Open question:** Whether Cisco's enterprise license for Claude (if that is what Guhan referenced) provides API access or only web/IDE access. Colin's LangGraph agent swarm methodology requires API-level access to models, not just chat interfaces.

---

## 7. Cisco Laptop and ID Still Pending

At the time of this meeting (February 20, 2026), Colin still did not have a Cisco laptop or Cisco ID. Both were first mentioned as pending in the Set 01 meeting (February 9, 2026), meaning they had been outstanding for at least 11 days.

Colin stated: "The two things that I'm missing, so I've done all onboarding and completed all onboarding except for having the hardware and my Cisco ID. I think those are supposed to get resolved today."

A BayOne representative on the call added (paraphrased from garbled transcript): "There's a call in the evening... we're going to get that streamlined and get a firm date on it... trying to get that Cisco laptop to Colin, so I'm going to try to see if we can speed that process up."

Colin also committed to follow up: "What I can do today, myself, to help this is I'll try to get a firm date on the hardware so that way we can plan around it."

**Timeline progression:**
- February 9 (Set 01): Colin expects laptop in 1-2 weeks. Cisco ID expected "same day or shortly after."
- February 20 (Set 02): Neither has arrived. Active escalation in progress. Expected resolution "today" or soon after.
- This represents an 11-day slip from the most optimistic estimate given in Set 01.

**Impact on engagement:** Without the laptop and ID, Colin cannot begin any hands-on work. The entire POC is blocked. This makes the hardware delivery date the critical path item for the engagement.

**Guhan's response to the delay:** Guhan acknowledged the constraint and pivoted to what could be done in the interim: "I'm trying to figure out what we can do in the next two weeks to get you going." He suggested that the Cisco team could begin identifying screens for conversion and start initial context-transfer conversations, so that when hardware arrives, Colin can begin immediately.

Specifically: "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations... providing context and everything. And by then, maybe your hardware arrives and then you can access to things right away."

---

## 8. Running Systems Needed for Testing

Colin asked about access to running instances of both EPNM and EMS for testing purposes. The exchange:

Colin: "The old version and the new version, are there running instances of those that are available to see this?"

Selva: "Yeah, probably we can have the team provide some point of view. So you need dedicated systems to work with on this one? You're saying all the time or it's only when you're ready?"

Colin: "I would say only when we're ready."

Colin then expanded on the need, connecting it to automated UX testing: "If you want us to be able to test and guarantee the UI, part of this is also the testing of it to make sure that it has faithfully been converted. We can do the automated UX testing as well, even if it's a precursor to formal UX testing from your team, but that can save you some time too."

Selva's response: "I mean, when we get to that stage, we guess we will provide the system to try this out, yes."

**What was agreed:**
- Running instances of EPNM and EMS will be provided for testing
- Not needed immediately -- only when BayOne is "ready" (i.e., after initial code exploration and prototyping)
- The systems are for verifying that converted functionality works end-to-end

**What was NOT agreed:**
- Whether these are dedicated instances or shared development environments
- Whether BayOne gets admin access or limited access
- Whether data will be pre-populated for testing scenarios
- The specific timing of when these systems will be made available

**Open question:** The automated UX testing Colin proposed (using Playwright for screen capture comparison) was acknowledged but not formally accepted as part of the POC scope. It was left as an "if we get to that stage" item.

---

## 9. Four-Week Decision Window

Guhan established a firm timeline for the POC:

> "I think we were looking at discussing about like, let's do it in four weeks, so then we made some important decisions around this."

This means the POC must produce results within four weeks that are sufficient for Guhan to make "important decisions" -- likely about whether to proceed with a full-scale conversion engagement, how to scope it, and what to promise customers.

Colin had initially suggested "a couple of weeks at most" for the POC: "I'm hoping something we can do in a couple of weeks for you at most."

Guhan pushed this out to four weeks, which is more realistic given the hardware delays and context-transfer requirements.

**The four-week clock:**
- It is unclear whether the four weeks start from the meeting date (February 20), from when Colin gets hardware, or from when code access is established. Given the hardware delay, it is most likely measured from when Colin can actually begin hands-on work.
- Within four weeks, BayOne must deliver: converted screens (UI + backend), working demos, and an estimation methodology for the remaining screens.

---

## 10. Two-Week Gap Before Hands-On Work Can Begin

Guhan acknowledged that there would be approximately two weeks before Colin could begin hands-on work (waiting for hardware). He tried to make this gap productive:

> "You have signed NDA and everything. That's right. I'm trying to figure out what we can do in the next two weeks to get you going."

The proposed use of this gap period:

1. **Colin writes the POC proposal.** Colin committed to sending a summary and proposal after the meeting: "I'll write this up. I have all minutes from today, so I'll write it up as a POC proposal."

2. **Cisco team identifies target screens.** Guhan and Selva's team would internally identify which screens/functionality should be the focus of the conversion POC.

3. **Initial context conversations.** Even without code access, verbal or document-based context transfer could begin.

4. **Hardware escalation.** Both Colin and the BayOne representative committed to getting a firm hardware delivery date.

**The gap creates a sequencing challenge:**
- Weeks 1-2: No hardware. Context transfer and planning only.
- Weeks 3-6 (approximately): Hardware arrives, code access established, hands-on POC work begins.
- Week 6 boundary: Four-week decision deadline (if counted from hardware arrival).

---

## 11. Colin Already Working on Anand's CICD Project (Same Hardware Pipeline)

Colin referenced the existing CICD engagement with Anand as relevant context for the hardware situation:

> "I'm already working on Anand's project for the CICD board. I'll have my Cisco laptop probably within a week or two. I think they're just finishing up with that setup."

This establishes:

1. **The same Cisco laptop serves both engagements.** Colin is not requesting separate hardware for EPNM-to-EMS. The laptop being provisioned for the CICD project will also be used for this engagement.

2. **The hardware delay affects both engagements.** Any slip in laptop delivery impacts not just EPNM-to-EMS but also the CICD work for Anand.

3. **Colin is already a known entity within Cisco.** The onboarding process is shared across both engagements. He has already completed all steps except hardware and ID.

---

## 12. BayOne Team Members Also Have NDA/Hardware Setup in Progress

Colin proactively disclosed that the broader BayOne team is going through the same onboarding pipeline:

> "My team as well, the team that is working on Anand's CICD project, they've also done the same as me. So they'll have Cisco hardware, just to say that part out loud, in case you hear me say anyone else's name on the team. I'm going to be probably running this primarily, but at the same time, everyone else has the same NDA signage, the same everything."

Guhan's follow-up question: "So you need access to more than you?"

Colin's answer: "I don't think I will. I think, especially for the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go."

**What this establishes:**
- Colin will run the POC solo
- Other BayOne team members are already NDA'd and in the hardware pipeline
- Scaling beyond the POC does not require starting onboarding from scratch for additional people
- Colin framed this as a strength: "Don't worry about that" -- the bench is ready

**Open question:** Whether the additional team members' hardware has arrived or is also still pending. If their hardware arrives before Colin's, there may be an opportunity to begin some exploration sooner, though Colin clearly positioned himself as the primary person for the POC.

---

## 13. Cloud Instances -- Available but Unclear for This Engagement

There is an oblique reference to cloud infrastructure during the discussion about whether running systems would be available. The speech-to-text garbles much of this, but the context suggests:

- Cisco has cloud instances (likely Azure-based, referenced in Set 01 as "Azure HD platform")
- Colin mentioned: "Even probably for access to the cloud instance. I'm guessing that would be preferable if it's using the Cisco ID."
- The connection between cloud instances and this specific engagement was not clarified

**From Set 01 context:** Cisco has an Azure-based development platform that was built for an agentic AI initiative under a different team (Meryl's). Whether the EPNM-to-EMS engagement has access to similar cloud infrastructure was not resolved.

**Open question:** If the EPNM and EMS running instances for testing are cloud-hosted, does Colin's Cisco ID grant access, or is additional provisioning required?

---

## 14. What the Team Can and Cannot Provide

Synthesizing from the full meeting, the division of responsibilities is:

**What Cisco's engineering team WILL provide:**
- Initial context and orientation (architecture, code layout, key patterns)
- Identification and prioritization of screens for conversion
- Running systems for testing (when ready)
- Code access (via Cisco infrastructure)
- Periodic availability for checkpoint meetings
- Clarification on domain-specific questions during checkpoints
- Hardware and ID provisioning (in progress)

**What Cisco's engineering team CANNOT provide:**
- Ongoing engineering pairing or collaboration during the POC
- Dedicated engineer time for supporting BayOne's work
- Design documentation for the legacy system (it does not exist)
- Immediate hardware/access -- there is a provisioning delay

**What BayOne is expected to provide:**
- Independent code exploration and analysis
- AI-assisted conversion of identified screens (UI + backend)
- Working demos of converted functionality
- Estimation methodology for remaining screens
- POC proposal document (Colin committed to writing this immediately after the meeting)
- All work done on Cisco hardware using Cisco-licensed tools

---

## 15. POC Structure: At Cost to BayOne

Colin explicitly stated the POC would be done at BayOne's cost:

> "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us."

And: "I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

Guhan reinforced why the POC matters: "So basically this is also about actually hands-on coding and showing the credit. That way, if we have to also get the additional resources for this, which we will have to work through, this will help."

**What this means for the engagement model:**
- BayOne absorbs the cost of the POC
- The POC is an investment to earn the larger engagement
- The POC must produce tangible, demonstrable results (working code, demos)
- Guhan needs the POC results not just for his own confidence, but to justify bringing in additional BayOne resources through whatever internal approval process Cisco requires ("get the additional resources for this, which we will have to work through")
- The scope must be "reasonable" -- Colin explicitly flagged this, meaning BayOne will not do unlimited free work

---

## Summary of Open Questions and Unresolved Items

1. **When will the Cisco laptop and ID be delivered?** Both were pending as of February 20. A follow-up call was scheduled for the same evening to get a firm date. This is the critical path blocker for all hands-on work.

2. **What is the exact checkpoint cadence?** "Periodic" was agreed to but no specific frequency was defined. This should be proposed in the POC proposal.

3. **What Cisco-licensed AI tools are available?** Guhan appeared to reference Claude and Copilot Enterprise as tools Cisco engineers already use, but the transcript is garbled. The specific tools and their access levels (API vs. IDE vs. web) are unknown.

4. **Are cloud instances accessible for this engagement?** Cisco has cloud infrastructure, but whether the EPNM-to-EMS work can use it was not confirmed.

5. **What format will context transfer take?** Without design documentation, the initial knowledge transfer from the engineering team must be verbal or code-walkthrough-based. The logistics of this (who, when, how long) were not defined.

6. **Does the four-week clock start from the meeting date or from hardware delivery?** Given the hardware delay, this distinction matters significantly. If from the meeting date, two of the four weeks are already consumed by the gap.

7. **Will the additional BayOne team members' hardware arrive on the same timeline as Colin's?** If their onboarding is further along or on the same track, it affects scaling options.

8. **What does "running system" mean for testing?** Dedicated instance vs. shared dev environment, data availability, access level -- none of this was specified.

9. **Is the automated UX testing (Playwright-based screen comparison) formally part of the POC scope?** Colin offered it, Selva acknowledged it as a possibility, but it was not confirmed as a deliverable.
