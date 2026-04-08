# 06 - Meeting: Infrastructure Stack

**Source:** /cisco/cicd/source/meeting_discovery_anand_srini_divakar_2026-02-17.txt
**Source Date:** 2026-02-17 (In-person discovery meeting at Cisco office)
**Document Set:** 06 (Discovery meeting with Anand, Srinivas, Divakar)
**Pass:** Technical infrastructure, development environment, and access patterns

---

## Overview

This is the first in-person technical discovery meeting for the CICD engagement, held at the Cisco campus (third floor). Participants are Colin Moore (BayOne), Anand (Cisco, engagement sponsor), Srinivas/Srini (Cisco, DeepSight platform lead), and Divakar (Cisco, infrastructure/access gatekeeper). Colin brought a structured set of discovery questions; the meeting ran approximately 31 minutes before time pressure cut it short. A follow-up was scheduled for the next day.

The transcript is speech-to-text with characteristic distortions: "Walker" consistently maps to **Divakar**, "Srini" and "Cine" map to **Srinivas**, "bezel"/"basil"/"Basil" maps to **Bazel** (the build system), "Jhara"/"Zara"/"Sara" maps to **Zahra** (BayOne coordinator), and "deep side"/"DeepSight" maps to the **DeepSight AI platform**.

This pass extracts the technical infrastructure stack, development environment configuration, access provisioning model, and ownership boundaries that define the operating constraints for BayOne's engagement.

---

## The Fragmented Tool Landscape

Colin brought a prepared inventory of systems to validate. His framing: "This is where I put out, as far as we know, the different systems that are part of this. This does not have to be exhaustive, but this is something that'll be good for us to see if this is complete as part of Discovery, to make sure that it's down."

Divakar's immediate response confirmed the fragmentation: "No, I think that there are different, different teams. I think there are different... Yeah, it's a crossover."

The validated systems and their ownership:

| System | Type | Owner | Divakar's Authority |
|--------|------|-------|---------------------|
| **Jenkins** | CI/CD orchestration | Divakar's team | Full context, direct access control |
| **GitHub Enterprise** | Source control | Cisco-wide (training-gated) | Can grant repo access after training completion |
| **ADS Linux machines** | Development environment | Cisco IT (provisioned by Divakar's request) | Initiates provisioning, but depends on Cisco IT turnaround |
| **Airflow** | Workflow orchestration | Separate team | "I need to get in touch with another team" |
| **CAT** | Pipeline tooling | Separate team | "I need to touch in another team" |
| **DevX** | Developer experience platform | Another team | Mentioned in Colin's inventory |
| **Grafana** | Monitoring/dashboards | Another team | Mentioned in Colin's inventory |
| **Bazel** | Build system | Cross-cutting (recently rolled out) | Divakar involved in rollout |
| **DeepSight** | AI platform | Srinivas's team | Srinivas controls access and architecture |

Divakar directly controls Jenkins and can initiate access for GitHub Enterprise and ADS machines. Airflow, CAT, and the other tools require cross-team coordination that Divakar cannot unilaterally expedite. This is a critical finding: the "fragmented tool landscape" that BayOne is hired to rationalize is also fragmented in terms of who can grant access to it.

---

## Database Layer

### MySQL (Structured Data)

Divakar confirmed MySQL as the standard: "All of our services are in MySQL, so I can give you MySQL."

Colin's team prefers Postgres. Divakar redirected: MySQL is what Cisco provides, and Colin accepted immediately ("That's fine. Completely."). This is a Cisco standard, not a team preference -- Divakar framed it as "all of our services."

Colin asked about scale. Divakar pushed back on the vague "250 GB" estimate and asked the right questions: "What is the number of transactions part of you, what is the rows, maximum rows, 250k, million rows, what is that going to look like?" and "How many panel connections do we need? Any concurrence in other things?" Colin acknowledged the sizing depends on understanding actual Git transaction volume, which is still unknown at this stage.

Divakar also noted uncertainty about provisioning: "I'll check with IT and that one. So we have about three services which we are using from the IT. Do I need to procure another one? I don't know." This means even the database may need an IT procurement cycle.

### MongoDB (Raw Pipeline Data)

The raw pipeline data lives in MongoDB. Divakar confirmed:

- **On-prem**, single location
- One instance ("it's one location")
- This is where the existing CICD pipeline data resides

Colin asked: "What does the raw pipeline data come currently?" Divakar: "It's an on-prem." Colin: "And it's just one of them, or is it, are there other locations where?" Divakar: "No, it's one location."

The single-location MongoDB is significant because it means all raw pipeline data access flows through one on-prem instance. There is no replication or distributed access pattern to work with.

---

## Build System: Bazel

Bazel dominates the meeting's opening context. Before the structured discovery even begins, Anand explains why Srinivas couldn't attend initially: "We just rolled out [Bazel] into production for the next day. And there are a lot of syncs and collapses going on -- PQC coming, IKEA video coming, NGP FM coming, spectrum coming. So we are working with every branch owner to sit and enable Bazel for all of them and bring in that code. And we have sanity issues and build issues. Engineers are trying to work, so it's been crazy."

Key facts about the Bazel rollout:

- **Just rolled out to production** at the time of this meeting (February 2026)
- Causing active disruption: "a lot of syncs and collapses going on"
- Requires individual branch-owner coordination to enable across all branches
- Generating "sanity issues and build issues"
- Multiple major features (PQC, IKEA video, NGP FM, spectrum) competing for integration attention simultaneously
- Srinivas was supposed to be in the discovery meeting but was pulled into Bazel debugging: "Sydney [Srinivas] was supposed to be here joining in person... got to check since morning is debugging something"

Colin also caught that Bazel was missing from his prepared system inventory: "I can tell myself I wrote this, Bazel missing on here." This means the Bazel rollout was not surfaced in any prior engagement communication (Sets 01-05) and is a discovery-stage finding.

The Bazel disruption is context for the entire engagement. BayOne is entering an environment where the fundamental build system just changed and is actively destabilizing the engineering workflow. Any CICD analysis or tooling built during this period will need to account for the Bazel transition as a confounding variable in pipeline metrics.

---

## Containers: Podman (Not Docker)

Colin proposed spinning up Docker containers on a Linux machine for early-stage Airflow development. Divakar corrected him: "It's a container, but it's not a Docker container. It is a Podman container from Red Hat. So we have that provision."

This is a meaningful constraint. Podman is the Red Hat container runtime that runs without a daemon process (unlike Docker). It is rootless by default and OCI-compliant. BayOne engineers familiar with Docker will need to adjust to Podman's workflow differences -- particularly around compose files (podman-compose vs. docker-compose), networking, and volume management.

The fact that Divakar corrected "Docker" to "Podman" immediately and firmly suggests this is a non-negotiable Cisco standard, not a preference. Red Hat's container ecosystem (Podman, Buildah, Skopeo) is common in enterprise environments that have moved away from Docker for licensing, security, or architectural reasons.

---

## Logging: Splunk via Jenkins

Divakar described the logging architecture: "We have Splunk connected to our Jenkins to be able to push all our data into Splunk."

However, Splunk access for BayOne is unlikely: "I don't know if you can access that one." Divakar explained: "Splunk is given for the security team for them to go and snoop and find out if there is anything going on maliciously."

The alternative offered: "I can give you the Jenkins access for you to go directly and pick up the log information from there."

Colin accepted this: "Even if it's direct connection, that'll be fine too. Because that'll be part of that whenever we do the next quarter integration... that'll connect all the different services together." His reasoning: direct Jenkins log access gives BayOne a predictable, stable interface. If they later need to build a logging integration layer, they have a known data source to work from.

The implication: BayOne will work with raw Jenkins logs rather than the aggregated/indexed Splunk data that Cisco's security team uses. This means building any log analysis capability from the Jenkins source, not from a pre-processed Splunk index.

---

## Access Model: Four-Tier Provisioning

The access model revealed in the transcript has four distinct layers, each with its own provisioning process and timeline:

### Tier 1: Network Access (VPN)

**Requirement:** Cisco laptop OR Cisco image installed on personal laptop, plus VPN connection.

Divakar was explicit: "If you don't have VPN, it probably won't allow you to connect to emails or machines or anything."

Colin asked about remote access from Pittsburgh: "If everything's on-prem and I'm looking back in Pittsburgh for that time, is that something where you want me to access everything through VPN?" Divakar: "It will be VPN."

Two paths to network access:
1. **Cisco-provisioned laptop** -- Colin mentioned this is already in process ("we're already having laptop provisions. I'll get a Cisco image laptop, I think")
2. **Cisco image on personal laptop** -- Divakar described documentation for installing a Cisco image on personal hardware

Rahul Bhubali (BayOne side) has already initiated equipment provisioning. Divakar indicated this is well-managed: "He seems to have that pretty well under wraps from the other people that we've put in Cisco."

### Tier 2: ADS Linux Machines (Development Environment)

**Requirement:** VPN active, then SSH/remote connection to on-prem ADS machines in Cisco data center.

Divakar: "You need an ADS machine to view the code and other things over there." And: "That would be a Linux machine to be provisioned to these users so they can log into those machines to check out the code or view the code and be able to build and stuff like that."

Critical access chain: "There's no VPN. This is going to be on top of VPN. So once you have a VPN, then you can connect to these machines."

Divakar controls this access: "I would be the one to give that access."

These machines are in Cisco's data center ("They are in the data center of Cisco") and are the only way to access, check out, and build the NX-OS codebase. The ADS machines are on-prem, not cloud-hosted.

Srinivas flagged provisioning delays as a known pain point: "Any time any new engineer joins, right? And it could be BayOne or something like that. We are spending a lot of time to get the ADS or the provision to those engineers. And it is done by Cisco but it is taking time from us... So there is no set procedure on what they need to follow. And sometimes we wait some approval from the highway [higher-up]. I'll say I keep pinging him, can you approve this guy?" This is a systemic bottleneck, not specific to BayOne.

### Tier 3: GitHub Enterprise (Source Control)

**Requirement:** Complete a 3-4 hour training course, then request repo-level access from Divakar.

Divakar: "GitHub Enterprise, we have a training tool taken... They need to go to the training. It takes about three hours or four hours of time. Once they do that one, they understand how to work with the GitHub and look at the data and all that one. Then I can give the access to the request."

The training is mandatory before any access request can be submitted. Turnaround after training: "Should not be more than half a day, maybe a day max."

### Tier 4: Repository-Level Permissions

**Requirement:** GitHub Enterprise access (Tier 3) active, then specific repo permissions granted.

Two distinct permission models exist:

1. **NX-OS main repositories: Read-only access.** Divakar was clear: "If you have a read-only access, you cannot stage anything... You cannot do any modifications to the code or anything." BayOne can read code, observe PR validations, and review the development flow, but cannot open PRs or push commits. Colin confirmed this is the desired state: "We want to make sure we're not doing things without you."

2. **DeepSight repositories: Commit access.** Srinivas described a separate repo structure: "As a part of the DeepSight, we have the repos created for every application... So you'll commit a code there. They'll look it through, the other people, and they walk a stream or it's contributing there." BayOne's own code for the CICD application lives in DeepSight-managed repos, where they can commit, and code is reviewed by Srinivas's team.

This creates a clean separation: BayOne reads Cisco's production repos (NX-OS) and writes to DeepSight's application repos (CICD app). Colin can "read through the PR validations going on over there" in the NX-OS repos but cannot modify them, while BayOne's application code follows a standard commit-and-review workflow in DeepSight repos.

---

## On-Prem: Everything

Nothing in this transcript suggests any cloud infrastructure. Every system discussed is on-premises:

- MongoDB: on-prem, single location
- MySQL: on-prem ("services from the IT")
- ADS machines: "in the data center of Cisco"
- Jenkins: on-prem (Divakar has direct access)
- Splunk: on-prem (security team's instance)
- GitHub Enterprise: on-prem (training-gated, Cisco-hosted)
- DeepSight platform: on-prem (Srinivas's team)
- Bazel: on-prem (build infrastructure)

Colin tested this implicitly by asking about Airflow deployment -- proposing Docker containers on a Linux machine -- and Divakar's response (Podman, on Red Hat infrastructure) confirmed the on-prem container stack.

When Colin asked about AI services (cloud model hosting on Azure, GCP, etc.), Srinivas redirected entirely to the DeepSight platform: "I think since you and your team already have a platform related to that one, so you'll be a new application built on top of that platform." No cloud AI services are part of the architecture.

---

## DeepSight Platform: The AI Infrastructure Layer

Srinivas joined the meeting after Divakar's infrastructure discussion and introduced the DeepSight platform. This is a complete, in-house AI application platform that BayOne will build on top of -- not alongside.

### What Srinivas Showed Colin

Srinivas walked through a live demo: "You can see that this is already live. And we call this the entire infrastructure that gives a total [unclear]. And we think that if you go here, it does [much of ours]."

The platform already has 8-10 applications ("we already have almost like eight or 10") being released incrementally:
- **Triage**: launched the week of the meeting ("this week we launched triage")
- **Prior Jump** (likely a diagnostic/root-cause tool): launched the preceding weekend
- **Runbook**: planned for launch by end of that week
- **Telemetry**: aggregation of all applications
- **CICD pipeline app**: exists in some form ("we already have a CICD application built today")

### What BayOne Gets

Srinivas was emphatic that BayOne does not build infrastructure: "You are not building anything in AI stack because all the AI stack is given, AI stack is given to you. Everything else is given to you. Right? All you have to do is build an LCP [likely LLM Call Pipeline], build a patch of prompts queries and stitch it here. That's it."

The platform provides:
- SDK for application development
- Standardized UI (chat interface, AI chat)
- Common look and feel across all applications
- Infrastructure for hosting and serving AI applications
- Code repositories per application (DeepSight-managed)

Srinivas set an aggressive timeline based on this: "Once you get the good understanding of the requirements, and once you onboard your engineers, my expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you."

### Existing CICD Application

A CICD application already exists within DeepSight in some form. Srinivas described a handoff plan: "We already have a CICD application built today. In the next two weeks, I work with Arun's team, Rui is there, to launch that application." The plan is for Rui (from Srinivas's team) to get the existing app live on DeepSight, and then BayOne picks it up from there.

Srinivas's exact framing: "It is all set up purpose, it does not solve the entire thing. But Colin can actually and team can actually take that... stack whatever we have done and build on top of it the other requirements."

This means BayOne is not starting from zero. There is an existing CICD application codebase that needs to be launched on DeepSight, and BayOne's work is to extend it based on the new requirements from the discovery process.

### Access to DeepSight

Srinivas attempted to share a recording and presentation with Colin during the meeting but was blocked by the NDA status. Colin's background check was complete, but the NDA had not yet been signed. Srinivas: "I assume that NDA is signed. I'll share you an email ID. That email ID has my presentation... If you go through the recording for one hour, or one and a half hour, you get pretty much a good understanding."

Once the NDA is signed (targeted for end of day February 17), Srinivas will share:
- A recorded presentation (1-1.5 hours) covering the DeepSight platform
- Documentation on platform capabilities
- Access to the WebEx space for ongoing collaboration

---

## Ownership Map: Who Controls What

The meeting revealed clear territorial boundaries:

### Divakar Controls
- Jenkins (full context, direct access granting)
- ADS machine provisioning (initiates requests, depends on Cisco IT)
- GitHub Enterprise repo-level permissions (after training completion)
- MySQL database access
- MongoDB access
- General infrastructure questions ("Six of them I have answers")
- VPN/network access coordination (works with Rahul Bhubali on BayOne side)

### Srinivas Controls
- DeepSight platform architecture and access
- DeepSight application repositories (commit access for BayOne)
- AI stack decisions (SDK, model hosting, application framework)
- CICD application codebase (existing app, Rui managing launch)
- Design direction (extensibility, agentic infrastructure requirements)
- "I need to once you are in I'll talk to the team and see how we can leverage the infrastructure that we have built for the CICD"

### Separate Teams Control
- **Airflow**: Divakar explicitly said "I need to get in touch with another team"
- **CAT**: Divakar explicitly said "I need to touch in another team"
- **DevX**: referenced as part of the system landscape, separate team
- **Bazel**: cross-cutting, being rolled out with branch-by-branch coordination across teams
- **Splunk**: security team controls access; Divakar cannot grant BayOne access

### Anand Controls
- Engagement-level decisions (SOW, staffing, timeline)
- Escalation path ("if something is not moving, then I will expedite")
- Cross-team unblocking ("I'll try to make sure that I'm paying attention")
- Relationship management between BayOne and Cisco teams

---

## No Formal Issue Tracking

Colin asked about issue tracking for infrastructure requests. Divakar's answer revealed a fully informal system:

"We don't have much for [ticketing]. We had it for a year or so. We tried it. But a lot of pushback from the engineers that, hey, I cannot go and create a ticket every single time. And they just ping me and say, yeah, take care of this."

Colin asked: "How do they ask a question? What do they do ask? And how do you go pulling the questions? Is there a tracking for all those requests going in? What is the closure?" The answer is: there is none. Engineers ping Divakar directly, and he handles it informally.

Anand acknowledged this gap and suggested BayOne could introduce structure: "Maybe for future if you want to try new issues, then you can get it at that space, you can stoop in and see what is going on and start writing on that."

This is operationally significant: there is no audit trail for infrastructure requests, no SLA tracking, no queue visibility. Divakar is a single point of contact handling requests through direct messages. This is both a risk (Divakar bottleneck, no visibility for BayOne into queue position) and an opportunity (BayOne's work on pipeline visibility could extend to infrastructure request tracking).

---

## Development Workflow Summary

Based on the full access model, the BayOne development workflow at Cisco will be:

1. **Connect via VPN** from Cisco laptop or Cisco-imaged personal laptop
2. **SSH into ADS Linux machine** in Cisco data center
3. **Access GitHub Enterprise** (after completing 3-4 hour training)
4. **Read NX-OS repositories** (read-only -- observe PRs, review code, understand pipeline patterns)
5. **Commit to DeepSight repositories** (write access -- CICD application code, reviewed by Srinivas's team)
6. **Build using Bazel** on ADS machines (the recently-deployed build system)
7. **Run containers via Podman** (Red Hat container runtime, not Docker)
8. **Access Jenkins directly** for log data and pipeline observation
9. **Interface with DeepSight platform** for AI application development (SDK, standard UI, shared infrastructure)

All of this is on-prem. All of this requires VPN. There is no cloud path, no SaaS tooling, no external service dependency. BayOne engineers are effectively operating as on-prem Cisco developers with a read/write permission boundary between observation (NX-OS repos) and development (DeepSight repos).

---

## Colin's MCP Strategy (Mentioned)

Colin briefly surfaced his approach to GitHub data extraction: "I'm hoping we'll have some kind of an MCP on top of that one to be able to talk to GitHub to get data like how many comments are going through, how many branches are there, what is hard, what is having issue or other things, right?"

This is the first explicit mention in the transcript of what appears to be a Model Context Protocol (MCP) layer for GitHub data. Colin envisions an interface that can query GitHub Enterprise for pipeline activity metrics -- comment volume, branch counts, issue patterns -- as an input to the CICD analysis. This would sit between the read-only GitHub access and the DeepSight AI application, providing structured data about the development workflow.

---

## Staffing and Timeline Context

Colin described the BayOne team: five people total, three onshore (including himself), two offshore. At the time of the meeting:
- Colin: on-site, background check complete, NDA pending (signed end of day)
- One person: background check complete, hardware procurement in process
- One person: available within two weeks
- Two offshore: identified and active

Anand set a two-week checkpoint cadence: "Two weeks from now, let's do a catch-up between maybe three of us here."

The quarter timing pressure is explicit. Colin raised it: "We're already almost a month into Q3 for a year... If we wait a couple more weeks to get it, it's going to get really tight for that Q1 deliverable." Anand's response was accommodating: "Whenever we get started, the quarter starts then."

---

## Key Constraints for BayOne Engineers

1. **Podman, not Docker.** Any container work must use Red Hat's Podman runtime. Docker commands may have equivalents but the workflow differs.
2. **Bazel, not Make or CMake.** The build system is freshly deployed and actively causing issues. Expect instability and undocumented edge cases.
3. **Read-only on NX-OS repos.** BayOne cannot modify production code. All application code goes to DeepSight repos.
4. **No Splunk access.** Log analysis must work from raw Jenkins logs, not pre-indexed Splunk data.
5. **VPN required for everything.** No exceptions. Even email requires VPN.
6. **ADS machines are the only dev environment.** Local development is not possible for anything that touches Cisco code or infrastructure.
7. **GitHub training mandatory.** 3-4 hours, must be completed before any repo access request.
8. **MySQL, not Postgres.** Cisco standard. BayOne team's Postgres preference is irrelevant.
9. **DeepSight is the AI platform.** No external AI services (Azure, GCP model hosting). Everything runs through Srinivas's platform.
10. **No formal ticketing.** Questions and access requests go through direct messages to Divakar. No SLA, no queue, no tracking.
