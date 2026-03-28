# 01 - Meeting: Security, Access, and Logistics

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on security requirements, hardware access, and logistics

---

## 1. Security Requirements: Cisco Code Stays in Cisco

### 1.1 Guhan's Security Statement

Guhan raised the security topic directly after Colin's explanation of the AI tooling architecture (Claude Code, LangGraph agent swarms). The transition was pointed -- he moved immediately from Colin's tooling overview to the security concern:

> "So you have access, Colin, to everything that -- with respect to the -- because this is a Cisco code, so we don't want this code to get out of Cisco."

This was stated as a non-negotiable requirement. Guhan's framing was declarative ("we don't want this code to get out of Cisco"), not a question about whether it could be accommodated.

### 1.2 Guhan's Specific Prohibitions

Guhan followed up with explicit prohibitions around two areas:

**No code on personal hardware:**
> "No, nothing on the laptop. No downloading of the code, those kind of things."

This was stated clearly -- no Cisco code on non-Cisco hardware, no local downloads of code to personal machines.

**Use Cisco-licensed AI tools only:**
> "And also use the Cisco license or approval license for the... and others, rather than using their separate own license."

Guhan specifically called out that AI tool licenses must be Cisco-provided or Cisco-approved. This applies to Claude and any other AI tooling used in the engagement. The intent is that all AI interactions with Cisco code occur within Cisco's licensed infrastructure, not through externally-held licenses.

### 1.3 Guhan's Framing of Cisco-Licensed AI Tools

Guhan referenced existing Cisco AI tool availability before making his security stipulation:

> "I mean, there is a -- you have Cloud [Claude] and... as part of our engineers use it already. OK, [there's also Copilot] and stuff, even [Copilot] service point."

This establishes that Cisco already has licensed instances of Claude and GitHub Copilot (or similar) available to their engineers. Guhan was drawing on this existing infrastructure as the basis for his requirement -- the tools are already there, so there is no reason to use external licenses.

He then made the recommendation explicit:

> "So I would suggest using some of the Cisco license to build up anything other than outside of Cisco."

The "rather than outside of Cisco" phrasing reinforces that external tool usage is not acceptable for this engagement.

### 1.4 Colin's Immediate Acceptance

Colin accepted all security requirements without pushback or negotiation:

> "Of course, of course."

And then proactively connected it to the hardware timeline:

> "So maybe what we can do, because this is -- so I'm already working on [Anand's] project for the CI/CD [work]. I'll have my Cisco laptop probably within a week or two. I think they're just finishing up with that setup. So I'll have Cisco hardware that I'll do all Cisco work on. So that won't ever leave your hardware."

Colin explicitly committed to:
1. All Cisco work done on Cisco hardware
2. Nothing leaving Cisco hardware
3. Using Cisco-licensed AI tools "from day one if we can"

> "And likewise with AI tools, definitely. We'll use those from day one if we can, and that way we can keep that kind of security bubble intact. Happy to do it."

The phrase "security bubble" was Colin's -- characterizing the combined hardware + licensing requirement as a single containment boundary.

---

## 2. AI Tool Licensing: Cisco-Licensed Instances

### 2.1 Guhan's Offer to Help Set Up Licenses

After establishing the requirement, Guhan offered direct assistance with getting the licensing set up:

> "It will help you set up the licenses."

Colin's response indicated this was exactly what he needed:

> "Okay, that was what I was going to ask. That would be great."

This exchange establishes that Guhan is willing to actively facilitate the license provisioning, not just mandate it. This is a concrete next step that can be acted on once the Cisco ID is resolved.

### 2.2 Guhan's Rationale

Guhan framed the requirement in terms of protocol compliance:

> "I'm using the Cisco protocols within Cisco rather than trying to use the same protocol."

This suggests the requirement is not ad hoc but part of Cisco's broader security protocols. The expectation is that all tools used on Cisco code follow Cisco's approved toolchain, which already includes Claude and Copilot.

### 2.3 What Tools Are Available

Based on Guhan's (garbled) statement, the following AI tools appear to be available under Cisco license:
- **Claude** (referred to as "Cloud" in transcript -- consistent transcription error throughout)
- **GitHub Copilot** (referred to as "Copilot service point" or similar -- transcription was garbled but contextually clear)

These are referenced as tools "our engineers use it already," meaning they are in active use at Cisco, not experimental.

### 2.4 Implications for POC Tooling

Colin described two levels of AI tooling in his approach:
1. **Claude Code** -- for initial exploration, code understanding, pattern recognition
2. **LangGraph agent swarms** -- for deeper multi-agent analysis and conversion work

The security requirement means both levels must operate within Cisco's infrastructure. Claude Code can presumably use the Cisco Claude license. The LangGraph implementation is custom BayOne tooling that calls Claude (and potentially other models) -- this would also need to use Cisco-licensed model access.

This was not explicitly discussed in the meeting. The agreement was high-level: use Cisco licenses for AI tools. The specific mechanics of how custom agent orchestration (LangGraph) would use Cisco-licensed model endpoints was not addressed.

---

## 3. Hardware Timeline and Delivery

### 3.1 Colin's Statement on Expected Delivery

Colin stated the hardware timeline in the context of the security discussion:

> "I'll have my Cisco laptop probably within a week or two. I think they're just finishing up with that setup."

This places expected delivery approximately between 2026-04-01 and 2026-04-08 (one to two weeks from the March 25 meeting).

### 3.2 Colin's Commitment to Get a Firm Date

Later in the meeting, Colin committed to nailing down the exact date:

> "And what I can do today, myself, to help this is I'll try to get a firm date on the hardware so that way we can plan around it."

This was stated as something he would do the same day as the meeting.

### 3.3 BayOne Participant's Confirmation of Hardware Push

A BayOne participant (likely Rahul or Amit, based on the reference to an evening call) piggybacked on Colin's statement:

> "We're gonna get an answer on the hardware today. There's a call... in the evening... we're gonna get that streamlined and get a firm date on it."

And further:

> "Just [our BayOne team is] trying to get that Cisco laptop to Colin, so I'm gonna try to see if we can, you know, speed that process up."

This confirms BayOne is actively pushing on the hardware delivery timeline through their own channels. The "evening call" reference suggests there is a separate operational call (possibly with Cisco IT or the CI/CD engagement team under Anand) where this can be escalated.

### 3.4 Hardware for Colin's Team

Colin also noted that his team members will have Cisco hardware:

> "My team as well, the team that is working on Anand's CI/CD project, they've also done the same as me. So they'll have Cisco hardware."

This establishes that Cisco hardware provisioning is not unique to Colin -- the full BayOne team engaged on Cisco work will be on Cisco hardware. This is relevant for scaling beyond the POC.

---

## 4. Onboarding Status: What Is Complete vs. Pending

### 4.1 Completed Steps

Colin enumerated his onboarding status:

> "I've done all onboarding and completed all onboarding except for having the hardware and my Cisco ID."

**Completed:**
- NDA executed (confirmed: "you have signed NDA and everything" -- Guhan's acknowledgment)
- All other onboarding steps (unspecified but described as complete)

### 4.2 Pending Steps

**Pending (as of meeting date):**
- **Cisco ID** -- Colin expected this to be resolved the same day: "I think those are supposed to get resolved today"
- **Cisco hardware (laptop)** -- expected in 1-2 weeks

### 4.3 Cisco ID Significance

Colin connected the Cisco ID to access:

> "Once I have those, that way, even probably for access to the cloud [Claude] instance. I'm guessing that would be preferable if it's using the Cisco ID."

This suggests the Cisco ID is a prerequisite for:
- Accessing Cisco-licensed AI tools (Claude instance)
- Potentially accessing code repositories
- General Cisco network/systems access

Colin committed to notifying the team immediately upon receiving it:

> "So once I have that, I can let you know immediately."

### 4.4 Team Onboarding Status

Colin confirmed his team's onboarding status:

> "My team as well, the team that is working on Anand's CI/CD project, they've also done the same as me. So they'll have Cisco hardware, just to say that part out loud, in case you hear me say anyone else's name on the team."

And specifically on NDAs:

> "Everyone else has the same NDA signage, the same everything. So just have that confidence in the team as well."

This means the full BayOne team working on Cisco engagements has:
- NDAs signed
- Cisco hardware expected (same pipeline as Colin's)
- Same onboarding steps completed

---

## 5. CI/CD Engagement Cross-Reference

### 5.1 Colin's Existing Cisco Work

Colin referenced his existing engagement multiple times:

> "So I'm already working on [Anand's] project for the CI/CD [work]."

This establishes that Colin is not new to Cisco -- he is already engaged on a separate workstream under Anand's team focused on the NX-OS CI/CD pipeline. The onboarding (NDA, hardware, Cisco ID) was initiated for that engagement and carries over to this UI conversion POC.

### 5.2 Team Overlap

The team working on Anand's CI/CD project is the same team Colin referenced as being available for beyond-POC work:

> "My team as well, the team that is working on Anand's CI/CD project, they've also done the same as me."

This means personnel, security clearances, and hardware provisioning are shared across both engagements.

---

## 6. Running Instances: When Needed and Who Provides

### 6.1 Colin's Question About Running Systems

Colin asked whether running instances of EPNM and EMS are available:

> "The old version and the new version, are there running instances of those that are available to see this? So like, for instance, for us to take something from the old and put it on the new, do we have things to go off of basically? The running system."

### 6.2 Selva's Response: Available When Ready

Selva (referred to in transcript as the second Cisco speaker after Guhan) responded with a clarifying question:

> "So you need dedicated systems to work with on this one? You're saying all the time or it's only when you're ready to?"

Colin clarified that running instances are only needed when ready to test:

> "I would say only when we're ready because what we'd want to do, what we could do as well, there's two sides to it."

Colin then elaborated that running instances would be used for:
1. Testing converted UI to ensure faithful conversion
2. Automated UX testing as a precursor to formal testing

> "If you want us to be able to test and guarantee the UI, part of this is also the testing of it to make sure that it has faithfully been converted. We can do the automated UX testing as well, even if it's a precursor to formal UX testing from your team, but that can save you some time too, if that's a desirable thing."

### 6.3 Selva's Commitment

Selva confirmed systems would be provided at the appropriate time:

> "I mean, when we get to that stage, we guess we will provide the system to try this out, yes."

This means running instances are **not a blocker** for the initial analysis and code exploration phases. They become necessary only during the testing/validation phase of the POC.

---

## 7. What Can and Cannot Happen Before Hardware Arrives

### 7.1 Guhan's Recognition of the Gap

Guhan explicitly recognized the gap between the meeting and hardware arrival and tried to find productive use of that time:

> "You're going to wait for two weeks, you have signed NDA and everything. That's right. I'm trying to figure out what we can do in the next two weeks to get you going."

He then listed potential pre-hardware activities:

> "Not the estimate, but the plan or whatever you're going to provide if you want to have idea of what this is about, access to the code and stuff like that."

### 7.2 Guhan Explored Remote Code Access

Guhan briefly explored whether Colin could access code without Cisco hardware:

> "So, it's possible to set up a [program] like this or something, what we can do to give this..."

Then self-corrected:

> "Okay, so you have a laptop that's not Cisco, but I can get them to the network, I'm not sure about that. Okay, got it."

This indicates Guhan considered and then abandoned the idea of providing code access on non-Cisco hardware. His own security requirements precluded this approach. The conclusion was that **code access cannot happen before Cisco hardware arrives**.

### 7.3 What CAN Happen Before Hardware

Guhan identified activities that can proceed:

> "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations [with the team] in terms of providing context and everything. And by then, maybe your hardware arrives and then you can access to things right away."

Pre-hardware activities identified:
1. **Cisco team identifies screens for conversion** -- Guhan and Selva's team will prioritize which screens/features to target
2. **Initial context conversations** -- Colin can have discussions with the engineering team to understand architecture, patterns, and requirements
3. **Colin writes the POC proposal** -- Colin committed to writing this immediately after the meeting
4. **Colin gets firm hardware date** -- Same-day action item
5. **Colin gets Cisco ID resolved** -- Expected same day

Post-hardware activities (require hardware):
1. Code access and exploration
2. AI-assisted analysis of codebase
3. Actual conversion work
4. Testing against running instances (requires instances + hardware)

### 7.4 Colin's Pre-Hardware Commitments

Colin committed to several immediate actions:

> "I'll send out my summary right after this meeting, and then we can go from there."

> "I'll try to get a firm date on the hardware so that way we can plan around it."

> "I'll also figure out, because the two things that I'm missing... my Cisco ID. I think those are supposed to get resolved today."

---

## 8. Network Access, VPN, and Development Environment

### 8.1 Lack of Explicit VPN Discussion

The transcript does not contain an explicit discussion of VPN setup, network access procedures, or development environment configuration. These topics were not raised by either side.

### 8.2 Implied Network Access Model

Based on Guhan's comment about not being able to get Colin on the Cisco network without Cisco hardware:

> "So you have a laptop that's not Cisco, but I can get them to the network, I'm not sure about that."

This implies that network access to Cisco's internal systems (code repositories, CI/CD systems, etc.) requires Cisco hardware as a prerequisite. The Cisco laptop presumably comes pre-configured with VPN and network access, or that setup happens as part of the laptop provisioning process.

### 8.3 Development Environment

No specific discussion of IDE setup, local development environment, build toolchain, or similar occurred in this meeting. The expectation appears to be that once Cisco hardware arrives and the Cisco ID is active, Colin will have what he needs to access the code. The specifics were deferred.

Colin referenced a follow-up call for navigating resources:

> "I think probably once we have the [laptop] install, then we could set up a call to see the specific resources. I would just need some help to navigate and know who to ask for what."

This indicates the development environment setup is expected to happen **after** hardware delivery, guided by the Cisco team.

---

## 9. Code Access Details

### 9.1 Colin's Question About Code Access

Colin raised code access as one of his final questions:

> "From a code access perspective, because for us to convert and move over to the new, we'll probably need to know a little bit more about the new and what the code looks like. Is that going to be possible for a POC to get access to things?"

### 9.2 Guhan's Confirmation

Guhan confirmed code access would be provided:

> "Yeah, we need to provide you with access to things, that I can [arrange]."

This was stated as a necessity, not a maybe. Guhan acknowledged that code access is required for the work.

### 9.3 Documentation Caveat

Guhan set expectations about documentation:

> "There is like some cases... this is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

Colin acknowledged this is normal and not a problem:

> "For the most part, especially with anything legacy, almost always is missing documentation. It's way easier to do it now, so we're kind of modern day cheating. It's much easier now."

And noted documentation's limited reliability:

> "Because documentation doesn't always tell the truth."

---

## 10. POC Staffing and Team Readiness

### 10.1 POC: Colin Solo

When asked about whether more than one person needs access, Colin was clear:

> Guhan: "So you need access to more than you?"
> Colin: "I don't think I will. I think, especially for the POC, I'll just handle this."

### 10.2 Beyond POC: Team Ready

Colin immediately followed with the scaling plan:

> "But then when we go beyond the POC, I just know I already have an asset of people ready to go. So don't worry about that."

This positions the POC as a solo effort with a ready team behind it, reducing Cisco's immediate access/provisioning burden while keeping the option to scale.

### 10.3 Team Credentials

Colin proactively addressed team credentialing:

> "Just to say that part out loud, in case you hear me say anyone else's name on the team. I'm going to be probably running this primarily, but at the same time, everyone else has the same NDA signage, the same everything. So just have that confidence in the team as well."

---

## 11. Timeline and Checkpoints

### 11.1 Four-Week POC Window

Guhan set the overall timeline:

> "I think we were looking at discussing about like, let's do it in four weeks, so then we [make] some important decisions around this, right?"

Colin accepted:

> "Yes. Right, so let's do what we can in the four weeks, right? That's a good spread."

### 11.2 Timeline Breakdown (Implied)

- **Weeks 1-2 (approx):** Pre-hardware period. POC proposal, context conversations, Cisco team identifies target screens, Cisco ID resolution
- **Weeks 2-4 (approx):** Hardware available. Code access, AI-assisted analysis, initial conversion attempts, demo preparation

### 11.3 Periodic Checkpoints

Guhan mentioned ongoing check-ins:

> "We'll have periodic checkpoints to help clarify anything more and also keep the rest of the folks [aware] with the progress, right?"

### 11.4 Post-Hardware Kickoff Call

Colin proposed a specific call once hardware arrives:

> "I think probably once we have the [laptop] install, then we could set up a call to see the specific resources. I would just need some help to navigate and know who to ask for what."

---

## 12. Summary of Action Items (Logistics-Specific)

| Action Item | Owner | Timeline |
|---|---|---|
| Write POC proposal based on meeting minutes | Colin | Immediately after meeting |
| Get firm date on Cisco hardware delivery | Colin + BayOne team | Same day (evening call referenced) |
| Resolve Cisco ID | Colin / Cisco IT | Expected same day |
| Identify target screens/features for conversion | Guhan / Selva / Cisco team | During pre-hardware period |
| Set up Cisco-licensed AI tool access | Guhan (offered to help) | After Cisco ID is active |
| Provide code access | Guhan / Cisco team | After hardware delivery |
| Set up initial context conversations with engineering team | Both sides | Pre-hardware period |
| Provide running instances of EPNM and EMS | Selva / Cisco team | When ready for testing (later in POC) |
| Post-hardware kickoff call for resource navigation | Both sides | After laptop arrives |
