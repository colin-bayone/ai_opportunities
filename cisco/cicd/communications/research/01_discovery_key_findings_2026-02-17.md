# 01 - Discovery Meeting: Key Findings and Technical Architecture

**Source:** cisco/cicd/communications/source/meeting1_anand_srini_divakar-2-17-2026.txt
**Source Date:** 2026-02-17 (In-person discovery at Cisco office, 3rd floor)
**Document Set:** 01 (Feb 17 Discovery Meeting)
**Pass:** Focused on technical findings, infrastructure decisions, and architecture

---

## 1. DeepSight Atlas Platform Discovery

The most significant finding from this meeting was the existence of DeepSight Atlas, Cisco's internally built AI platform. This was not known to BayOne prior to the in-person meeting.

### What DeepSight Atlas Is

- A live, production AI platform that Cisco's team (led by Srinivas) has built internally
- Provides a unified infrastructure for multiple AI-powered applications, each surfaced as a distinct app within the platform
- Already has 8-10 applications planned, with several launched or launching imminently:
  - **Triage** -- launched the week prior to the meeting
  - **Prior Jump** -- launched the weekend before the meeting
  - **Runbook** -- scheduled for launch by end of that week
  - **Telemetry** -- aggregation of all applications
  - **CI/CD Pipeline app** -- exists in current form (built by Rui), pending launch on DeepSight Atlas
- The platform provides: UI framework, AI stack (Large Language Model integration), SDK, chat interface, and standard look-and-feel across all applications

### What DeepSight Atlas Means for BayOne's Approach

This fundamentally changes the engagement's technical approach:

- **BayOne is not building from scratch.** The AI infrastructure, UI stack, and deployment platform are already provided. BayOne's work is to build a CI/CD application on top of the existing platform.
- Srinivas was explicit: "You are not building anything in AI stack because all the AI stack is given. Everything else is given to you. All you have to do is build an MCP, build a batch of prompt queries and stitch it here."
- The existing CI/CD app (built by Rui) will be launched on DeepSight Atlas within 2-3 weeks. BayOne's role is to take over from where Rui's work ends and extend it based on new requirements.
- Each application on DeepSight Atlas has its own repository within Cisco's infrastructure, so BayOne will commit code to the designated CI/CD app repo.

### Srinivas's Expectations Based on DeepSight Atlas

- With the infrastructure already in place, Srinivas expects a working app "within like two months" after onboarding and requirements gathering are complete
- BayOne should follow the same look and feel as other DeepSight Atlas applications
- Colin was directed to watch a recorded presentation (approximately 1-1.5 hours) that Srinivas delivered to the entire DCT (Developer Community/Tools) organization, covering the platform's architecture and capabilities

---

## 2. Infrastructure Stack Confirmed

### Database

- **MySQL** -- Cisco's standard. Srinivas confirmed: "All of our services are in MySQL, so I can give you MySQL." Colin's team preferred Postgres but agreed to use MySQL for consistency.
- Divakar noted he would need to check with IT on whether an additional MySQL instance needs to be procured or whether they can use an existing one. Cisco currently has approximately three database services from IT.
- Database sizing details (row counts, transaction volumes, concurrency requirements) are deferred until BayOne has access and can assess data flow volumes through Git and Jenkins.

### Document Store

- **MongoDB** -- confirmed as the store for raw pipeline data. Single location/instance. On-premises.

### Containerization

- **Podman** (Red Hat) -- not Docker. Divakar specified: "It's a container, but it's not a Docker container. It is a Podman container from Red Hat." BayOne had proposed spinning up Docker containers on a Linux machine for early development; this clarifies the container runtime to target.

### Logging

- **Splunk** -- connected to Jenkins, pushes all data into Splunk. However, Splunk access is controlled by the security team and may not be available to BayOne. Divakar offered direct Jenkins access as an alternative for log data.

### CI/CD and Orchestration

- **Jenkins** -- Divakar has full context and will provide access. This is the primary CI/CD system.
- **Airflow** -- requires contact with a separate team. Divakar acknowledged he needs to initiate that connection.
- **GitHub Enterprise** -- requires completion of a training course (3-4 hours) before access can be granted. Training covers how to work with the repository and view data.

### Compute

- **ADS machines** -- Linux machines provisioned within Cisco's on-premises data center. Required for viewing, checking out, and building code. Accessible via VPN after Cisco laptop/image provisioning.

---

## 3. Access Requirements and Onboarding Process

The meeting revealed a multi-step onboarding process:

1. **Background check** -- Colin's was already initiated and confirmed complete during the meeting (Rahul confirmed via message)
2. **NDA** -- not yet signed at the time of the meeting; Colin committed to getting it signed by end of day February 17
3. **Cisco laptop or Cisco image** -- Rahul Bhubali on BayOne's side had already initiated hardware provisioning. Alternatively, engineers can install a Cisco image on their own laptops.
4. **VPN access** -- required for all remote connectivity. Without VPN, no access to email, machines, or any resources.
5. **GitHub Enterprise training** -- mandatory 3-4 hour course before repository access is granted. Should take no more than half a day to a full day to complete.
6. **ADS machine provisioning** -- Divakar provisions these Linux machines. This step has historically been a bottleneck; Divakar flagged that it "is done by Cisco but it is taking time" and there is "no set procedure" for scaling this out.
7. **Repository access** -- initially read-only. Engineers can view PRs, read code, and review validation activity but cannot push or open PRs. Code development happens in local workspaces.

### Known Onboarding Friction

Divakar raised a pain point: every time a new engineer joins (whether BayOne or otherwise), the ADS provisioning process is slow and requires manual follow-up. He described repeatedly pinging people for approvals. Anand acknowledged this and agreed to monitor the BayOne onboarding as a test case for improving the process.

---

## 4. Existing CI/CD App and Handoff Plan

- An existing CI/CD application was built by **Rui** (a member of Srinivas's team, working under Arun's team)
- Rui is currently stuck or blocked on something, and the team is busy with the Bazel rollout
- Srinivas's plan: within the next 2-3 weeks, the existing CI/CD app will be launched on DeepSight Atlas "with the current form, whatever we have"
- Colin's team will then "pick it up from there" -- take the existing app, understand the codebase, and extend it based on new requirements
- Srinivas explicitly requested that Colin not spend time designing infrastructure: "I do not want Colin to spend time on say what infra will look like, what it is. We are already 90 percent there, just 5-10 percent there is small issues."
- During the 2-3 week gap before the app launches, Colin's team should focus on gathering requirements and studying the platform via the recorded presentation

---

## 5. Bazel Production Rollout Context

The Bazel rollout was the dominant operational concern during the meeting and directly impacted the meeting logistics:

- Cisco had just rolled Bazel out to production "for the next day" (the day before or day of the meeting)
- Multiple concurrent integration efforts: PQC, IKEA Video, NGP FM, Spectrum -- all requiring coordination with branch owners to enable Bazel and integrate code
- Sanity issues and build issues were active; engineers were debugging in real time
- **Zahra** (described as "wave and sea coordinator" -- likely the release coordinator) was supposed to coordinate the discovery meeting but could not attend because she was debugging since morning
- Srinivas himself was supposed to attend in person but was pulled into Bazel-related syncs
- This context explains the compressed meeting format (intended as 30 minutes) and the need to schedule a follow-up for the next day

---

## 6. Key Technical Decisions Made

| Decision | Detail |
|---|---|
| Build on DeepSight Atlas, not from scratch | BayOne builds an application on the existing AI platform using provided SDK, UI framework, and AI stack |
| MySQL, not Postgres | Aligning with Cisco's existing database standard despite BayOne's preference for Postgres |
| Read-only repository access initially | BayOne can view PRs and code but cannot push; development happens in local workspaces |
| Podman, not Docker | Container runtime is Podman (Red Hat), not Docker |
| Direct Jenkins access, not Splunk | For log data, BayOne will connect directly to Jenkins since Splunk access is controlled by the security team |
| VPN-based remote access | All remote work goes through Cisco VPN to on-premises ADS machines |
| Record all sessions | Srinivas insisted that all knowledge-transfer sessions be recorded so BayOne engineers can self-serve and ramp up asynchronously |

---

## 7. Srinivas's Philosophy and Expectations

Srinivas articulated a clear philosophy for how BayOne should approach the work:

### Extensibility and Reusability

- "Always put two hats when you evaluate. One, will you solve my current need? Two, can it be extensible? Or can I today write the infrastructure in a way that it is available for agentic infrastructure?"
- He wants every deliverable to be future-proof: solve the immediate CI/CD need while simultaneously building infrastructure pieces that can be leveraged elsewhere
- Framed this as "not building a pointed solution, but building infrastructure pieces where I can leverage in other places"

### Agentic Infrastructure

- Explicitly mentioned "agentic infrastructure" as the long-term vision
- Wants BayOne to correct him if he deviates from this principle: "Anytime I myself deviate it, you have to correct me."

### Fast Pace

- Self-described as moving "very, very fast" and acknowledged his style can come across as aggressive in meetings
- Set the expectation that BayOne should push back technically when appropriate: "You can hold me saying that, hey, we are looking at the other requirements"
- Once onboarded, the relationship should be "engineer-to-engineer conversation" -- open disagreement, direct feedback, treated as internal colleagues

### Integration Into Cisco's Working Rhythm

- Plans to pull Colin into additional meetings beyond the CI/CD scope so BayOne has context on the broader platform direction
- Wants BayOne to participate in "heated discussions" -- agree, disagree, and contribute as peers

---

## 8. "Quarter Starts When Access Granted" Agreement

Colin raised a timing concern: BayOne was already almost one month into Cisco's Q3 fiscal calendar. If onboarding and access provisioning dragged out further, the Q1 deliverable window (aligned to Cisco's fiscal quarter) would be too tight.

Anand's response was definitive: "Whenever we get started, the quarter starts then." He acknowledged:

- First-time onboarding friction is expected
- Cisco would have liked to start earlier, but understands the practical constraints
- They will "manage it entirely whatever way, most logical way"
- He characterized it as "business reality versus engineering reality"

This agreement effectively de-risks the timeline pressure for BayOne. The engagement clock starts when access is granted, not when the SOW was signed or the fiscal quarter began.
