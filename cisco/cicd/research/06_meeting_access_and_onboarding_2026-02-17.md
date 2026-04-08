# 06 - Meeting: Access and Onboarding

**Source:** /cisco/cicd/source/meeting_discovery_anand_srini_divakar_2026-02-17.txt
**Source Date:** 2026-02-17 (In-person discovery meeting at Cisco office)
**Document Set:** 06 (Discovery meeting with Anand, Srinivas, Divakar)
**Pass:** Access requirements, onboarding steps, and team readiness

---

## Overview

This is the first in-person discovery meeting between BayOne and the Cisco CICD team. The meeting takes place at the Cisco campus, third floor, with Colin physically on-site. Three Cisco participants are present: Anand (the engagement sponsor), Srinivas (AI platform owner for DeepSight), and Divakar (the CI/CD infrastructure engineer who controls repository access and machine provisioning). Zahra (BayOne) coordinated the meeting but is not present -- Srinivas notes she "was supposed to be here joining in person" but got pulled into debugging that morning.

The meeting was scheduled for 30 minutes but runs to 31. It covers two major threads: (1) Colin's open discovery questions against the ~65-question list he prepared, of which roughly 30 get addressed; and (2) the access and onboarding chain that must complete before any development work can begin. This document captures thread (2) exhaustively.

The meeting establishes a critical dependency chain: NDA signing unlocks information sharing, which unlocks GitHub training, which unlocks repository access, which (combined with ADS Linux machine provisioning and VPN) unlocks the ability to view and build code. Every step has a named owner and an estimated turnaround. The chain is sequential -- nothing can be parallelized until training is complete.

## Connection to Prior Sets

Set 02 documented that Sarang (the previous BayOne resource) never got GitHub access and that on-site presence was required. This meeting confirms the access provisioning process is nontrivial and historically slow. Divakar himself raises this: "Any time any new engineer joins... we are spending a lot of time to get the ADS [machines] provisioned to those engineers. And it is done by Cisco but it is taking time from us." He notes there is "no set procedure" and that he ends up repeatedly pinging people to get approvals pushed through. Anand acknowledges this and offers to monitor the process and intervene if things stall.

Set 04 noted Zahra's meeting with Anand on February 4, outcome unknown. This meeting on February 17 is the first time Colin is face-to-face with Anand and the technical team, suggesting the Feb 4 meeting was relationship/logistics and this is the substantive kickoff.

The five-person team structure planned in earlier sets is confirmed explicitly by Colin in this meeting: "Five people total, three onshore, myself included, two offshore."

---

## Access Dependency Chain

The meeting reveals a strict sequential chain of prerequisites that must be satisfied before any BayOne engineer can do development work. Each step has a named Cisco-side owner and an estimated duration.

### Step 1: Background Check

- **Owner:** Cisco (initiated through Rahul Bobbili on BayOne side)
- **Status as of meeting:** Colin's background check is complete. He confirms this in real time during the meeting by pinging Rahul Bobbili, who responds immediately: "My background check is done."
- **For other team members:** In progress. Colin states one person (Person 2) has already completed their background check. Others are pending.
- **Dependency:** Background check completion is a prerequisite for receiving a Cisco ID, which is a prerequisite for accessing Cisco systems and receiving controlled information.

### Step 2: NDA Signing

- **Owner:** BayOne (Colin coordinating with Zahra)
- **Status as of meeting:** Not yet signed. Srinivas asks directly: "Do you guys already signed the NDA and all?" Colin responds: "I believe so... No, but it can't form. But otherwise, I can't share this stuff." He then confirms with Rahul and commits: "NDA, we can get that signed by today, end of day."
- **Dependency:** The NDA must be signed before Srinivas can share DeepSight platform materials, including the recorded presentation and access to the platform itself. Srinivas is explicit: "I assume NDA is signed. I'll share you an email ID. That email ID has my presentation."
- **Urgency:** This was a real-time blocker during the meeting. Srinivas wanted to share the DeepSight recording and platform overview but could not until NDA status was confirmed.

### Step 3: GitHub Enterprise Training

- **Owner:** Divakar (administers access after training completion)
- **Duration:** 3 to 4 hours
- **Description:** Cisco requires all engineers to complete a GitHub Enterprise training course before being granted repository access. Divakar states: "They need to go to the training. It takes about three hours or four hours of time. Once they do that one, they understand how to work with the GitHub and look at the data and all that one. Then I can give the access to the request."
- **Training link:** Divakar shared a WebEx training link directly in the WebEx space during the meeting.
- **Scope:** Every BayOne team member must complete this training individually. Colin commits to being first: "I'll be the first to have it so he can get me the quickest, but I'll make sure everyone else gets that as well."
- **Dependency:** Training completion is a hard prerequisite for GitHub repository access. There is no bypass.

### Step 4: GitHub Repository Access

- **Owner:** Divakar (provisions after training is verified)
- **Turnaround:** Half a day to one day after training completion. Divakar states: "Should not be more than half a day, maybe a day max."
- **Access level:** Read-only to production repositories. Colin specifically asks about staging and development environments and Divakar confirms: "If you have a read-only access, you cannot stage anything... you cannot do any modifications to the code or anything." Engineers can read code, view pull request (PR) validations, but cannot open new PRs or push code.
- **Separate repo for development:** Srinivas clarifies that the DeepSight platform has repos created for every application: "As a part of the deep side, we have the repos created for every application... So you'll commit a code there. They'll look it through the other people." This means BayOne will commit CICD application code to a DeepSight-managed repository, while having read-only access to the NX-OS production repositories.

### Step 5: ADS Linux Machine Provisioning

- **Owner:** Divakar (initiates the request; Cisco IT provisions)
- **Description:** ADS (Application Development Services) machines are on-premises Linux machines hosted in Cisco data centers. Engineers must log into these machines to check out code, view code, and build. Divakar states: "That would be a Linux machine to be provisioned to these users so they can log into those machines to check out the code or view the code and be able to build and stuff like that. That would be the ninth one. I would be the one to give that access."
- **Dependency:** Requires VPN access first. Divakar is explicit: "There's no VPN. This is going to be on top of VPN. So once you have a VPN, then you can connect to these machines."
- **Known pain point:** Divakar raises this proactively as a bottleneck: "Any time any new engineer joins... we are spending a lot of time to get the ADS [machines] provisioned to those engineers. And it is done by Cisco but it is taking time from us... There is no set procedure on what they need to follow. And sometimes we wait some approval." Anand agrees to monitor this specifically.

### Step 6: VPN Access

- **Owner:** Cisco IT (Rahul Bobbili has initiated equipment requests on BayOne side)
- **Requirement:** Cisco laptop or Cisco image installed on personal laptop. Divakar states: "If you have your own laptop, then you can take the Cisco Image and install that on your laptop. There's some documentation related to that one."
- **Colin's status:** Hardware provisioning is in progress. Colin notes: "For myself, we're already having laptop provisions. I'll get a Cisco Image laptop, I think."
- **Without VPN:** Nothing works. Divakar is blunt: "If you don't have VPN, it probably won't allow you to connect to emails or machines or anything."
- **Hardware management:** Rahul Bobbili on BayOne's side has already initiated equipment requests. Colin notes: "Rahul Bobbili on our side has already initiated that for at least the equipment side for this network access process."

### Summary: The Complete Chain

```
Background Check (complete for Colin, in progress for others)
    → NDA Signing (committed to end of day Feb 17)
        → Cisco ID / Information Access (unlocks DeepSight materials)
            → GitHub Enterprise Training (3-4 hours per person)
                → GitHub Repository Access (half day to one day after training)
            → VPN Setup (Cisco laptop or Cisco image required)
                → ADS Linux Machine Provisioning (Divakar initiates, Cisco IT provisions)
                    → Ability to view, check out, and build code
```

**Critical finding:** The chain is almost entirely sequential. The only parallelizable steps are GitHub training and VPN setup, which can proceed concurrently once background check and NDA are cleared. But the ADS machine requires VPN, and repository access requires training, so both paths must complete before development can begin.

---

## Team Status as Stated in Meeting

Colin provides the team composition explicitly during the meeting. The following reflects exactly what was stated on February 17.

### Team Composition

| Role | Status (Feb 17) | Details from transcript |
|------|-----------------|------------------------|
| **Colin (Person 1)** | Active, on-site | Background check complete (confirmed in real time via Rahul Bobbili). NDA to be signed by end of day. Hardware provisioning in progress (Cisco Image laptop). Will be first to complete GitHub training. |
| **Person 2** | Available immediately | "I have one person that's with me immediately today." Background check already completed: "The one person has already completed their background check." Hardware is being requested: "We're in the process of requesting the hardware now." |
| **Person 3** | Available within two weeks | "Another person that'll be available within two weeks." No further details provided on background check or hardware status. Likely the person referenced as "pending the SOW" earlier: "We have two more people, one more that we're about to close on, I think pending the SOW." |
| **Persons 4-5** | Identified, offshore | "We have both of our offshore resources identified and active right now." No further details on their onboarding status. |

### Team Structure

- **Total:** Five people
- **Onshore:** Three (Colin plus two others)
- **Offshore:** Two
- Colin's exact words: "Really, five people total, three onshore, myself included, two offshore, so it's small enough that we don't..."

### Onboarding Implication

Every team member must independently complete the GitHub Enterprise training (3-4 hours) and get ADS machine access provisioned. Given the known bottleneck Divakar raised about ADS provisioning delays, the onboarding of five engineers will need active monitoring. Colin commits to sequencing himself first to unblock quickly, then ensuring the rest follow.

---

## DeepSight Platform Onboarding

A significant portion of the meeting -- the second half after Anand departs -- is a one-on-one between Colin and Srinivas about the DeepSight AI platform. This has direct access and onboarding implications.

### What Srinivas Shared

- **DeepSight recording:** Srinivas shared a WebEx link and password for a recorded presentation of the DeepSight platform. He describes it as "a basic form of what a platform is. And some of its capabilities, basically. Not everything, but some of it." Duration: approximately one to one and a half hours. Srinivas states: "If you go through the recording for one hour, or one and a half hour, you get pretty much a good understanding."
- **The recording was shared in the WebEx space** (Bay1 CICD workspace). Srinivas provides the link and password directly in chat.
- **Conditional on NDA:** Srinivas initially hesitates because NDA is unsigned. After Colin confirms NDA will be signed same day, Srinivas proceeds: "I assume that NDA is signed."

### What DeepSight Means for the Engagement

- The CICD application will be built as an app on top of the DeepSight platform, not as a standalone system. Srinivas is explicit: "You are not building anything in AI stack because all the AI stack is given. Everything else is given to you. All you have to do is build an LCP [likely LLM Connection Point or similar], build a batch of prompts queries and stitch it here."
- DeepSight already has a CICD application in early form. Srinivas states: "We already have a CICD application built today. In the next two weeks, I work with Arun's team, Rui is there, to launch that application." The plan is for Rui's team to get the existing CICD app live on DeepSight within two to three weeks, then Colin's team picks it up from there: "If we get our app like next two to three weeks or live on the deep side platform with the current form, whatever we have, then Colin can pick it up from there."
- Srinivas provides SDKs and infrastructure. Colin's team writes application logic on top.
- Srinivas's timeline expectation: "My expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you."

### DeepSight Access Requirements

- Requires a Cisco ID (which requires background check completion).
- Once Colin has Cisco ID, Srinivas will coordinate with his team to provide platform access.
- Code for the CICD application will be committed to DeepSight-managed repositories (separate from the NX-OS production repos that Divakar controls).

---

## WebEx Space and Communication Channels

### Existing WebEx Space

- A "Bay1 CICD Studio Workspace" WebEx space already exists. This was apparently created earlier (possibly by Zahra), and there was brief confusion during the meeting about duplicate spaces. Zahra had created a second one, which Srinivas notes is "not needed actually."
- Resolution: The team will use the original Bay1 space, not the duplicate.

### Engineer Addition

- Colin and the Cisco team discuss adding engineers to the WebEx space as they onboard. Currently only "high level" participants are in the space. Anand asks: "Do you have the engineers also added to that group or is it only high level right now?" Colin confirms it is currently high-level only.
- Divakar's engineers and Colin's engineers will be added as they come online.

### Communication Model

- Anand establishes the WebEx space as the primary communication channel for questions: "If something is not moving, then I will be monitoring... I'll try to make sure that I'm paying attention and if I feel something is stalled I can resolve it."
- Anand explicitly offers escalation support: "On the WebEx group, if something is not moving, then I will expedite."
- Srinivas reinforces: "Keep using the WebEx space."

---

## Questions Answered vs. Open

### What Was Covered

Colin arrived with approximately 65 prepared discovery questions. The meeting addressed roughly the first 17 (Colin states "We're finished till 17" when time runs short). Of those, Colin characterizes a subset as answered:

- **Question 1:** Issue tracking / ticket system. Answer: No formal system. Jira was tried for about a year but engineers pushed back: "I cannot go and create a ticket every single time. And they just ping me and say, yeah, take care of this." Current process is entirely informal -- engineers message Divakar directly.
- **Access provisioning turnaround:** Half a day to one day after training (Divakar).
- **Network access model:** VPN required. Cisco laptop or Cisco image on personal laptop.
- **Operating system preference:** No strong preference. Mixed Mac and Windows across the team.
- **Protected tiers / restricted environments:** No. "I don't think so."
- **Development vs. staging separation:** Development environment exists but is underused. Read-only access means BayOne cannot stage or push code to production repos.
- **Database:** Cisco uses MySQL for their services (Colin's team prefers Postgres but agrees to MySQL). Database sizing to be determined once transaction volumes are understood.
- **Pipeline data storage:** MongoDB, single location, on-premises.
- **Logging:** Splunk connected to Jenkins, but Splunk access may not be available (security team controlled). Divakar can provide direct Jenkins access for log information.
- **Container platform:** Not Docker -- Podman (Red Hat container platform). "It's a container, but it's not a Docker container. It is a [Podman] container from Red Hat."
- **Airflow:** Exists at Cisco. Colin proposes using Docker containers on a Linux machine for development Airflow, or leveraging Cisco's existing Airflow instance.
- **AI platform:** DeepSight (Srinivas's platform). No external AI services needed. Colin's team builds on top of DeepSight's infrastructure.
- **Code repository for new work:** DeepSight-managed repos, separate from NX-OS production repos.

### What Remains Open

Approximately 48 questions remain unaddressed. Colin notes: "I don't know if we can get to all the questions today." The plan is to continue discovery in a follow-up meeting the next day (February 18). Key areas still open:

- Detailed transaction volumes and data sizing
- Specific GitHub workflow details beyond basic access
- Airflow configuration specifics
- Jenkins pipeline architecture details (Colin notes: "I have the full context... I'm hoping we'll have some kind of an MCP on top of that one to be able to talk to GitHub to get data")
- DEGAS platform details (Colin: "I think I need to get in touch with another team")
- Detailed integration requirements across services

---

## Anand's Escalation Commitment

Anand makes several explicit commitments about expediting access and unblocking the team:

1. **Monitoring the WebEx space:** "I will be monitoring... if something is not moving, then I will expedite."
2. **Keeping Divakar responsive:** "If the doctor [Divakar] is busy for some reason, don't mind pinging him or pinging any of us to expedite."
3. **Willingness to intervene on ADS provisioning:** After Divakar raises the ADS bottleneck concern, Anand says: "Let's take this example, I want to monitor how this one goes."
4. **Two-week check-in:** Anand proposes a status meeting in two weeks with the three of them (Anand, Srinivas, Colin/Divakar) to assess onboarding progress and begin regular status cadence.

---

## Timeline Pressure and Quarter Alignment

Colin raises the timeline concern directly: "We're already almost a month into Q3 for a year. So I think we'll be okay right now if we keep going right now at this pace. But if we wait a couple more weeks to get access, it's going to get really tight for that Q1 deliverable."

Anand's response is accommodating: "I know practically it's never possible to start quarter here and there, so we understand that, and we're very flexible on that. So whenever we get started, the quarter starts then."

This is significant -- it means the engagement quarter starts when onboarding completes, not from a fixed calendar date. This removes artificial deadline pressure during the access provisioning process, but also means any delay in access directly delays the entire engagement timeline.

Colin also raises the outstanding SOW: "I think this SOW is still pending." He mentions accidentally creating a tool for the wrong SOW structure. Anand indicates his team handles SOWs and that Zahra has started on it.

---

## Srinivas's Expectations for the Team

Srinivas sets several cultural and technical expectations during his one-on-one with Colin:

1. **Speed:** "I go very fast, very, very fast. People know me who are working with me. And sometimes, team might say, why Srinivas is so aggressive? Because that's my nature."
2. **Push back welcome:** "You can always correct me... I don't mind in the private or for me it doesn't matter. From the technical point of view, it doesn't matter if you catch me anywhere, even in big meetings."
3. **Two-hat requirement:** Every piece of work should address (a) the current CICD need and (b) future extensibility for agentic infrastructure. Srinivas states: "Anything we do should be future proof and ready to enable the agentic infrastructure. So while you are solving your current need, we may be solving another agentic infrastructure behind the scenes."
4. **Colleague treatment:** "Once you are onboarding, you are my team. So I'll treat you the way, treat me the same way as a colleague."
5. **Recorded sessions:** Srinivas insists all working sessions with engineers be recorded. "Since you are new to jargon and technology, you should always say, can we have a recorded session... make sure that they are recorded and you can refer back." He frames this as essential for onboarding efficiency: "Many other team members will say, hey, take a day, record, go through all the recording."

---

## Items That Must Happen Before Development Can Start

Consolidating from the entire meeting, the following is the complete list of prerequisites before BayOne can begin any development work:

1. **NDA signed** -- Committed to end of day February 17
2. **Cisco IDs issued** -- Requires background check completion (done for Colin, done for Person 2, pending for others)
3. **Hardware provisioned** -- Cisco laptops or Cisco images (Rahul Bobbili managing, in progress for Colin and Person 2)
4. **VPN configured** -- Requires Cisco laptop or Cisco image
5. **GitHub Enterprise training completed** -- 3-4 hours per person, link shared by Divakar in WebEx space
6. **GitHub repository access granted** -- Divakar provisions after training, half day to one day turnaround
7. **ADS Linux machines provisioned** -- Divakar initiates request, Cisco IT provisions (known bottleneck, no set procedure, Anand monitoring)
8. **DeepSight platform access granted** -- Srinivas coordinates after Cisco ID is available
9. **DeepSight recording reviewed** -- Shared in WebEx space, 1-1.5 hours, provides platform understanding
10. **Existing CICD app launched on DeepSight** -- Rui's team target: 2-3 weeks from Feb 17, provides the baseline Colin's team builds on

Items 1-7 are hard blockers. Items 8-10 are soft blockers -- Colin can do discovery and requirements work without them, but cannot begin application development until the DeepSight baseline exists.

---

## Key Findings

1. **The access chain is sequential and long.** From NDA to buildable code access involves at minimum six discrete steps with different owners (BayOne legal, Cisco IT, Divakar, Srinivas's team). Even with Anand's offer to expedite, the realistic timeline to full developer access is one to two weeks after NDA signing, assuming no delays in ADS provisioning.

2. **ADS machine provisioning is the known bottleneck.** Divakar proactively flags this as a historical pain point with no set procedure and unpredictable approval timelines. This matches the Set 02 finding that Sarang never got GitHub access -- the provisioning process is where previous onboarding attempts stalled.

3. **Read-only access is the default.** BayOne engineers will not be able to push code to NX-OS production repositories. Development code goes to DeepSight-managed repos with a separate review process. This is a deliberate isolation -- Colin confirms this is desirable: "We want to make sure we're not doing things without you."

4. **The DeepSight dependency changes the engagement model.** The CICD application is not standalone -- it is an app within an existing AI platform. This means Colin's team is dependent on Srinivas's infrastructure team for SDK access, deployment, and platform conventions. The two-to-three week wait for Rui to launch the existing CICD app on DeepSight creates a natural onboarding window where Colin's team can complete access prerequisites and discovery simultaneously.

5. **Anand is an active sponsor.** Unlike passive executive sponsors, Anand commits to monitoring the WebEx space, expediting stalled requests, and conducting regular check-ins. His statement -- "if something is not moving, then I will expedite" -- is an explicit promise to remove organizational friction, which is the primary risk to onboarding based on historical patterns (Set 02).

6. **The informal culture extends to access management.** There is no ticketing system for access requests, no formal onboarding procedure for contractors, and no documented provisioning workflow. Everything flows through personal relationships and direct messages. This means BayOne's onboarding success depends on maintaining active communication with Divakar and escalating to Anand when responses stall -- not on following a documented process.
