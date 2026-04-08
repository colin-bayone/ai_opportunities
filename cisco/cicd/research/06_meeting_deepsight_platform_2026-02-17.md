# 06 - Meeting: DeepSight Atlas Platform

**Source:** /cisco/cicd/source/meeting_discovery_anand_srini_divakar_2026-02-17.txt
**Source Date:** 2026-02-17 (In-person discovery meeting at Cisco office)
**Document Set:** 06 (Discovery meeting with Anand, Srinivas, Divakar)
**Pass:** DeepSight platform discovery and scope reframing

---

## Overview

Set 06 is the first in-person discovery meeting at the Cisco campus with Anand, Srinivas, and Divakar. This meeting fundamentally reframes the entire CI/CD engagement. Everything in Sets 01-05 assumed BayOne would build CI/CD tooling from scratch -- custom infrastructure, custom AI stack, custom deployment. That assumption is now obsolete.

Srinivas reveals the existence of **DeepSight Atlas**, a fully built internal AI platform at Cisco with live applications already in production. BayOne's role is not to build CI/CD tools from the ground up. BayOne's role is to build a **CI/CD application on top of an existing AI platform** that already provides the SDK, infrastructure, UI patterns, chat interfaces, and deployment pipeline. This is a categorically different engagement than what was scoped in prior sets.

The meeting has two distinct halves. The first half is a structured discovery session led by Colin with Anand and Divakar present, covering access provisioning, infrastructure, tooling, and logistics. The second half begins when Anand leaves and Srinivas arrives, delivering the DeepSight Atlas revelation that restructures the entire project. The two halves are almost unrelated in content -- the first is tactical onboarding, the second is strategic reframing.

---

## The DeepSight Atlas Platform

### What It Is

DeepSight Atlas is Cisco's internal AI platform. Srinivas describes it as "the entire infrastructure that gives a total" -- a unified platform for building and deploying AI applications within Cisco's environment. It is not a concept or a plan. It is live, in production, with real applications serving real users as of the date of this meeting.

Srinivas shows Colin the platform during the meeting: "You can see that this is already live." The platform provides a standardized application shell -- UI, chat interface, AI stack -- and individual teams build domain-specific applications on top of it.

The platform's design philosophy is one-platform-many-applications. Srinivas states: "We plan to build much of ours. We already have almost like eight or 10 [applications], but we're going to release one at a time." The platform handles the common infrastructure; each application handles domain-specific logic.

### Architecture (As Described in Meeting)

The DeepSight Atlas platform provides:

- **AI stack** -- Srinivas explicitly says "all the AI stack is given to you." BayOne does not select models, configure inference pipelines, or manage AI infrastructure. That layer is provided.
- **SDK** -- "You'll provide SDK and everything." BayOne builds on top of Cisco-provided development tools, not their own.
- **UI framework** -- Standardized look and feel across all applications. Srinivas tells Colin: "Once you go through it you get a pretty understanding of what your app will look like because you follow the same look and feel, chat, AI chat, everything." Every DeepSight application shares a consistent user experience.
- **Deployment infrastructure** -- Applications deploy into the DeepSight platform. There are no separate deployment decisions for individual apps.
- **Telemetry** -- Srinivas mentions "telemetry which is aggregation of all the applications" -- a cross-application monitoring layer.
- **Separate repos per application** -- "As a part of DeepSight, we have the repos created for every application." Each app gets its own repository within the DeepSight ecosystem. Code is committed there, reviewed by platform team members, and merged through their workflow.

### What This Means for BayOne

Srinivas's framing is unambiguous: "You are not building anything in AI stack because all the AI stack is given, AI stack is given to you. Everything else is given to you. All you have to do is build an LCP [likely LLM Chain/Pipeline], build a batch of prompts queries and stitch it here. That's it."

He further says: "So the work becomes simplify the entire thing, the idea is to develop an AI app pretty fast."

This is the single most important statement in all six document sets. It eliminates the entire infrastructure design layer from BayOne's scope. BayOne does not decide what AI models to use, does not design deployment architecture, does not build a UI framework, does not configure monitoring. All of that exists. BayOne writes prompts, chains, and application logic on top of a provided SDK.

---

## Existing Applications on DeepSight Atlas

As of February 17, 2026, the following applications are either live or imminent:

### Triage (Live)

Launched the week of the meeting. Srinivas: "This week we launched triage, like last class" and "last weekend we launched the [triage app]." This is the first publicly released DeepSight application. Srinivas references it as a completed example that Colin should study.

### Runbook (Launching End of Week)

"End of this week we're gonna launch a runbook." The Runbook application is the second to go live on DeepSight Atlas, launching within days of this meeting.

### CI/CD Application (Rui Building, 2-3 Weeks from Launch)

This is the most critical existing asset for BayOne's engagement. A CI/CD application already exists in development. Rui (an engineer on the Cisco side, working with Arun's team) is actively building it. Srinivas states: "We already have a CICD application built today. In the next two weeks, I work with Arun's team, Rui is there, to launch that application."

Srinivas's plan is for Rui's existing CI/CD app to launch on DeepSight Atlas in its current form within two to three weeks. BayOne then picks it up from there and builds on top of it. Srinivas: "The way I am thinking is for Colin to start, in the next two weeks if Colin is trying to gather the requirement and do that easily to study. By that time, if we get our app like next two to three weeks live on the DeepSight platform with the current form, whatever we have, then Colin can pick it up from there."

Srinivas explicitly describes Rui's app as incomplete but functional: "It is all set up purpose, it does not solve the entire thing. But Colin can actually and team can actually take that, stack whatever we have done and build on top of it the other team based on the new requirements."

### Other Applications (Referenced)

Srinivas mentions "a bunch of other apps like CICD pipeline and what not" and states the platform will eventually host eight to ten applications, released one at a time. Beyond Triage, Runbook, and the CI/CD app, specific names are not provided.

---

## The Handoff from Rui

The transition from Rui's work to BayOne's work is a defined handoff point with a specific timeline and mechanism:

1. **Current state (Feb 17):** Rui is building a CI/CD application on DeepSight Atlas with Arun's team. The application exists but is not yet live on the platform.
2. **Next 2-3 weeks:** Rui and the Cisco team will launch the current CI/CD app on DeepSight Atlas "with the current form, whatever we have." This is a minimal viable deployment -- enough to be live, not feature-complete.
3. **Parallel track:** While Rui finishes the launch, Colin gathers requirements and studies the platform. Colin's first two weeks are onboarding and requirements gathering, not building.
4. **Handoff:** Once the app is live on DeepSight, Colin and BayOne pick it up from there and build additional features based on new requirements.

Srinivas explicitly asks Anand (via Divakar) to formalize this: "Maybe can you put that request to the WebEx group, Rui and us up there, just put that request." The handoff coordination will happen through the WebEx space.

The reason for the handoff: Rui and the Cisco team are "busy with our school and other stuff" and Srinivas notes "Rui also stuck something." The Cisco team has competing priorities (the Basil rollout described in the first half of the meeting, plus other platform launches). BayOne absorbs the CI/CD application development so Cisco's internal team can focus elsewhere.

---

## What Srinivas Explicitly Says NOT to Do

Srinivas draws a hard line on scope: **"I do not want Colin to spend time on say what infra will look like, what it is."**

This is a direct instruction, not a suggestion. The infrastructure decisions are made. The platform is built. BayOne should not revisit, redesign, or second-guess the infrastructure layer. Srinivas continues: "We will already, we are already 90 percent there, just 5-10 percent there is small issues up there. We will fix it and we will launch the CICD app."

The 90/10 framing is important: Srinivas acknowledges the infrastructure is not perfect (5-10% remaining issues) but those issues are Cisco's responsibility, not BayOne's. BayOne builds on the platform as-is.

Earlier in the meeting, when Colin raises the topic of AI services, Srinivas redirects immediately: "It will be an application on the DeepSight... Srinivas is going to help you with that." When Colin probes further about enterprise API subscriptions, Azure, or GCP for model hosting, Srinivas cuts it off: "Since you and your team already have a platform related to that one, you'll be a new application built on top of that platform."

The message is consistent and repeated: do not design infrastructure, do not select AI services, do not build deployment architecture. Use what exists.

---

## The WebEx Recording

Srinivas offers Colin a recording of his platform presentation: "I'll share you an email ID. That email ID has my presentation. It's a basic form of what a platform is. And some of its capabilities, basically. Not everything, but some of it."

The recording is approximately one to one and a half hours long: "If you go through the recording for one hour, or one and a half hour, you get pretty much a good understanding of how the triage app is done and it also has some builds and results of all the other infrastructure pieces that you might, if you will be using because you will be one more app here."

The recording covers:
- What the DeepSight Atlas platform is
- How the Triage application was built on it
- The infrastructure pieces available to application developers
- The look, feel, and interaction patterns that all applications must follow

Srinivas shares this via the WebEx space (the Bay1 CI Studio Workspace). There is a complication around Colin's access: at the time of the meeting, Colin's Cisco ID is not yet provisioned (background check just completed, NDA pending signature by end of day). Srinivas initially hesitates to share controlled information to an external ID but proceeds through the WebEx space channel.

This recording is the single most important onboarding artifact for BayOne's team. It replaces the need for BayOne to do independent infrastructure discovery.

---

## The Agentic Infrastructure Requirement

Srinivas introduces a dual-mandate for all development work. This is not optional -- it is a design principle for the engagement:

**Current need + future extensibility for agentic infrastructure.**

Srinivas: "Anything we do, should be future proof and ready to enable the agentic infrastructure. So while you are solving your current need, we may be solving another agentic infrastructure behind the scenes. So when you complete, we want to just level it just like that."

He frames this as a standing requirement: "Always put two hats when you evaluate. One, will you solve my current need? Two, can it be extensible? Or can I today write the infrastructure in a way that it is available for agentic infrastructure?"

Srinivas goes further, asking Colin to hold him accountable: "So anytime I myself deviate it, you have to correct me. I say that, hey, Srinivas, you are wrong." He wants the team to actively challenge decisions that sacrifice future extensibility for short-term convenience.

This means every feature BayOne builds on the CI/CD application must be evaluated against two criteria: (1) does it solve the immediate CI/CD use case, and (2) can it be consumed by autonomous agents in the future. Pointed solutions that only serve the current need are explicitly unwelcome.

---

## DeepSight Repository Model

Srinivas confirms the repository structure: "As a part of DeepSight, we have the repos created for every application."

The model is:
- Each DeepSight application has its own dedicated repository
- BayOne commits code to the CI/CD application's repo
- Code is reviewed by DeepSight platform team members ("They'll look at it through the other people")
- The repo is part of the DeepSight ecosystem, not a standalone BayOne repository

This means BayOne does not need to set up its own repository infrastructure. The CI/CD application repo already exists (or will exist once Rui's app launches). BayOne works within the DeepSight team's code review and merge workflow.

This is separate from access to the NX-OS code repositories, which requires specific training (approximately 3-4 hours) and separate provisioning through ADS machines.

---

## Srinivas's Timeline Expectation

Srinivas sets an explicit performance expectation: "My expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you. All you have to do is write on top of it. You're not doing anything from scratch."

The logic chain:
1. Infrastructure is done (DeepSight provides everything)
2. SDK is provided (no framework decisions)
3. Rui's existing app provides a starting point (not starting from zero)
4. Therefore, two months to a live application is achievable

This timeline is aggressive but rational given the platform's maturity. Srinivas is not asking BayOne to build infrastructure in two months. He is asking BayOne to build application logic -- prompts, chains, domain-specific workflows -- on top of existing infrastructure in two months. With the SDK, UI framework, deployment pipeline, and a starting codebase all provided, two months is a platform-informed expectation, not an arbitrary one.

---

## How This Reframes the Engagement

### Before Set 06

Based on Sets 01-05, the engagement was understood as:

- BayOne builds CI/CD tools for Cisco's NX-OS pipeline
- The AI stack decisions (model selection, hosting, inference) were open questions
- Infrastructure design (databases, deployment, orchestration) was BayOne's responsibility
- The engagement was greenfield development with BayOne making architectural decisions
- Questions about on-prem vs. cloud, Postgres vs. MySQL, Airflow orchestration were all live design decisions

### After Set 06

The engagement is now understood as:

- BayOne builds a **CI/CD application on the DeepSight Atlas platform**
- The AI stack is provided by DeepSight (not BayOne's decision)
- Infrastructure is provided by DeepSight (not BayOne's responsibility)
- The UI framework, chat interface, and look-and-feel are standardized across DeepSight (not BayOne's design)
- A starting CI/CD application already exists (Rui's work), to be live in 2-3 weeks
- BayOne's value-add is domain expertise in CI/CD workflows, prompt engineering, and application logic -- not infrastructure
- The SDK, repos, deployment pipeline, and telemetry are provided
- Every feature must be dual-purpose: solve current CI/CD needs and enable future agentic infrastructure
- Timeline: two months to a live application (infrastructure already exists)

### What Survives from Sets 01-05

The following elements from prior sets remain relevant:

- **Domain discovery:** Understanding the NX-OS pipeline, Jenkins workflows, Basil, GitHub Enterprise, and the developer pain points is still essential. The application needs to solve real CI/CD problems regardless of what platform it runs on.
- **Access provisioning:** ADS machines, VPN, GitHub training, Cisco ID -- all still required. The DeepSight platform does not bypass Cisco's security and access requirements.
- **People and relationships:** Anand as the engagement sponsor, Divakar as day-to-day contact, Srinivas as AI/technical strategy owner, Zahra as BayOne account manager -- all unchanged.
- **MongoDB as raw pipeline data source:** The on-prem MongoDB instance holding pipeline data is still the data source. DeepSight does not replace the need to connect to and query this data.
- **Jenkins access:** Direct Jenkins log access is still the mechanism for pipeline data. DeepSight provides the AI and UI layer, not the data connections.

### What Is Obsolete from Sets 01-05

The following planning assumptions from prior sets are now invalid:

- **Database provisioning questions** (Postgres vs. MySQL debate from the first half of this very meeting) -- the DeepSight platform handles data persistence for the application layer. The MySQL/Postgres discussion may still apply to domain-specific data storage, but the application's primary data architecture is platform-determined.
- **Airflow orchestration planning** -- Colin raised Airflow in the first half as a potential orchestration tool. The DeepSight platform has its own orchestration. Whether Airflow is still relevant depends on whether it is used for pipeline-adjacent automation outside of DeepSight.
- **AI model selection and hosting** -- All questions about Azure, GCP, enterprise API subscriptions, and model choices are answered: DeepSight provides the AI stack.
- **Custom UI design** -- The application follows DeepSight's standardized UI. BayOne does not design screens from scratch.
- **Greenfield architecture planning** -- There is no greenfield architecture. There is a platform with an SDK and a starting codebase.

---

## First Half: Structured Discovery (Anand + Divakar Present)

The first half of the meeting, before Srinivas arrives, covers tactical onboarding and infrastructure discovery. While much of this is superseded by the DeepSight revelation in the second half, the following details remain relevant:

### Access and Provisioning

- **GitHub Enterprise:** Requires 3-4 hours of training before access is granted. Divakar can provision access after training is complete. Training covers how to work with GitHub and access data.
- **ADS machines:** Linux machines in Cisco's data center, accessed via VPN. Required to check out code, view code, and build. Divakar provisions these.
- **VPN:** Required for all remote access. Cisco laptop or Cisco image installed on personal laptop. Colin's laptop provisioning already initiated by Rahul Bhubali.
- **Background check:** Colin's background check completed as of this meeting. NDA to be signed by end of day February 17.
- **Timeline for provisioning:** "Should not be more than half a day, maybe a day max" once training is complete.
- **Read-only access model:** Engineers get read-only access to NX-OS repositories. Cannot push code to production repos. Can view PRs, read code, build locally. GitHub rejects push attempts from read-only accounts. This is by design -- BayOne works in its own space (DeepSight repos) and does not commit directly to NX-OS production code.

### Current CI/CD Environment

- **Jenkins:** Primary CI/CD system. Divakar has full context and plans to bring in his engineer. Colin proposes building an MCP (Model Context Protocol) layer on top of Jenkins and GitHub to query data: "how many commits are going through, how many branches are there, what is having issues."
- **MongoDB:** On-prem, single location. Stores raw pipeline data.
- **Splunk:** Connected to Jenkins for log ingestion. Primarily used by the security team. Direct Jenkins access is available as an alternative for BayOne.
- **Jira:** Previously used for ticketing but abandoned due to engineer pushback ("I cannot go and create a ticket every single time"). Current request tracking is entirely informal -- engineers ping Divakar directly.
- **Basil:** A new system actively rolling out to production during this meeting. Multiple teams (PQC, IKEA video, NGP FM, spectrum) are being onboarded. Basil is causing significant operational load -- Divakar was pulled from another sync to attend this meeting because of Basil-related build and sanity issues.
- **Airflow:** Colin raises it as a potential orchestration tool. Divakar notes he needs to check with another team. The DeepSight platform may make this question moot for the AI application layer.
- **Container environment:** Podman containers (Red Hat), not Docker. This is the on-prem container runtime.

### Staffing Status

- **Onshore:** Colin (immediate), one additional person (background check complete, hardware being requested), one more pending SOW signature
- **Offshore:** Two resources identified and active
- **Total:** Five people (three onshore including Colin, two offshore)

### Communication and Tracking

- **WebEx space:** The Bay1 CI Studio Workspace is the primary collaboration channel. Engineers will be added as they onboard.
- **No formal issue tracking:** Informal ping-based requests. Divakar acknowledges this and suggests the WebEx space could serve as an informal tracking mechanism.
- **Recorded sessions:** Srinivas insists all knowledge-transfer sessions be recorded. Rationale: Colin and team are new to Cisco's jargon and technology; recordings let other team members self-serve onboarding rather than requiring repeated live sessions.
- **Status cadence:** Two-week check-in cadence agreed upon. First check-in in approximately two weeks. Srinivas, Colin, and Divakar as attendees. Arun may be pulled in depending on progress.

---

## Srinivas's Working Style and Expectations

Srinivas provides explicit guidance on how the working relationship should function:

1. **Speed:** "I go very fast, very, very fast. People know me who are working with me." He warns that he may come across as aggressive in meetings and asks the team not to interpret it personally.

2. **Open challenge expected:** "You can always correct me saying that you are wrong here. I don't mind in the private or for me it doesn't matter." He explicitly wants Colin to push back on technical decisions, including in group meetings.

3. **Engineer-to-engineer:** "Once you start working, it's an engineer-to-engineer conversation. You'll find a good partner." Srinivas frames the relationship as peer collaboration, not client-vendor.

4. **Dual-hat thinking:** Current need plus agentic future-proofing on every decision. Not optional.

5. **Extensibility mindset:** "You need to step back and say, how do I make this infrastructure generally so that we can leverage it in other places. So you guys are not building a pointed solution, but you're building infrastructure pieces where I can leverage in other places."

6. **Future visibility:** "At some point, we'll pull you into other set of meetings also, so that when the CICD applications are running, I'll make pull you guys in, so that you know what's happening behind the scene, so that once we come into phase one, you will have, you will start to have income failure on this also." Srinivas plans to expose BayOne to the broader DeepSight ecosystem, not just the CI/CD silo.

---

## SOW and Timeline Status

- **SOW:** Still pending. Colin mentions accidentally creating an SOW for the wrong structure (generated a Cisco SOW template thinking it was BayOne's internal format). Zahra's team is handling the actual SOW. Srinivas says to proceed: "We can start it off. I think first time it's always a challenge."
- **Quarter alignment:** Originally scoped as quarterly deliverables. Already almost a month into Q3 (Cisco fiscal year). Srinivas confirms flexibility: "Whenever we get started, the quarter starts then." No penalty for late start relative to the fiscal quarter.
- **Practical timeline:** Two weeks for onboarding and access provisioning. Two months to a live application on DeepSight Atlas.

---

## Colin's Reaction and Positioning

Colin recognizes the significance of DeepSight immediately. He tells Srinivas: "We have a similar platform, so that's a really cool thing. Yours is much nicer, I have to say, for the UI, but it's a similar approach to it."

This is significant positioning: Colin is signaling familiarity with platform-based AI application development, which validates Srinivas's expectation that BayOne can ramp quickly. It also suggests BayOne has internal experience with this development pattern, which should reduce the learning curve.

After Srinivas leaves, Colin tells Divakar: "Usually, I mean, I shouldn't say this, but sometimes in solutions and things like this, there's two types of client. There's type one that wants you to do something exactly as prescribed, and against all of your instincts, you have to do it. Refreshing, that's not [the case here]." Colin is signaling genuine enthusiasm for the engagement's technical direction.

---

## Divakar's Operational Role

Divakar emerges in this meeting as the operational bridge between BayOne and Cisco's infrastructure. He is the person who:

- Provisions ADS machine access
- Manages GitHub Enterprise access (after training completion)
- Coordinates with IT on database provisioning
- Manages the engineer onboarding pipeline (and flags that it is a known bottleneck: "We are spending a lot of time to get the ADS or the provision to those engineers. And it is done by Cisco but it is taking time")
- Serves as the day-to-day contact for infrastructure questions

Divakar also surfaces an important operational pain point: provisioning new engineers is slow and unpredictable. "There is no set procedure on what they need to follow. And sometimes we wait some approval." He asks whether this should be formalized now that the team is scaling with BayOne additions. This is a process improvement opportunity that BayOne could address as a side benefit.

---

## What We Still Don't Know

1. **DeepSight Atlas technical details.** The meeting provides a high-level description but no architecture diagrams, API documentation, or SDK reference. The WebEx recording is the next source of detail.
2. **Rui's CI/CD application status.** What features does it currently have? What data sources does it connect to? What is the "current form" that will launch in 2-3 weeks? No specifics in this meeting.
3. **The SDK specifics.** What language(s) does the DeepSight SDK support? What abstractions does it provide? What are the constraints? Unknown until Colin reviews the recording and documentation.
4. **How DeepSight handles data connections.** Does the platform provide data connectors (to MongoDB, Jenkins, etc.), or does each application build its own? This affects how much integration work BayOne needs to do.
5. **The review/merge workflow.** Who reviews code committed to DeepSight repos? What is the approval process? How fast is the deployment cycle from commit to live?
6. **Rui's availability for handoff.** Srinivas says Rui is "stuck" on something. Will Rui be available for a structured knowledge transfer, or will BayOne inherit the code without context?
7. **Other DeepSight team members.** Who else works on the platform? Who maintains the SDK? Who is the point of contact for platform issues?
8. **The Triage and Runbook applications.** What do they do? They serve as reference implementations -- understanding their architecture would accelerate CI/CD app development.

---

## Connection to Prior Sets

| Topic | Before Set 06 | After Set 06 |
|-------|--------------|--------------|
| Engagement scope | Build CI/CD tools from scratch | Build CI/CD application on DeepSight Atlas platform |
| AI infrastructure | Open question (Azure? GCP? Enterprise API?) | Provided by DeepSight. Not BayOne's decision. |
| UI/UX | BayOne designs | Standardized DeepSight look and feel |
| Starting point | Greenfield | Rui's existing CI/CD app (live in 2-3 weeks) |
| Timeline expectation | Quarterly deliverables | "Within two months, we should have an app running live" |
| Srinivas's role | AI/technical strategy owner (Set 02) | AI platform owner. Built DeepSight Atlas. Hands-on technical leader. |
| Divakar's role | Not previously identified in CICD sets | Day-to-day operational contact. Provisions access, manages infrastructure. |
| Rui | Not previously identified | Current CI/CD app developer. Handoff source for BayOne. |
| Arun | Not previously identified | Team lead whose team includes Rui. Involved in CI/CD app launch. |
| Deployment model | Unknown | DeepSight platform handles deployment. Separate repos per app. |
| Agentic requirement | Not previously mentioned | Standing requirement: all work must be extensible for agentic infrastructure |

## Next Steps (As Defined in Meeting)

1. Colin watches the DeepSight Atlas WebEx recording (1-1.5 hours)
2. NDA signed by end of day February 17
3. Colin's Cisco ID provisioned (background check complete)
4. Colin begins requirements gathering during the 2-3 week window before Rui's app launches
5. Rui launches current CI/CD app on DeepSight Atlas (target: early March 2026)
6. Colin and BayOne team pick up from Rui's baseline and build new features
7. Two-week status check-in with Srinivas, Colin, and Divakar
8. Follow-up discovery meeting (referenced as "maybe we can do one more tomorrow")
