# 02 - Communications: Blocker Analysis and Unblock Strategy

**Source:** cisco/cicd/communications/source/external/chat1.txt, chat2.txt, discovery_meeting_brainstorming.txt
**Source Date:** 2026-03-31 (Analysis of current blockers)
**Document Set:** 02 (External Communications)
**Pass:** Focused on what is actually blocking progress and what can be done immediately

---

## Current Blockers (What Is Actually Preventing Work From Starting)

### Blocker 1: GitHub Enterprise Training

- **What:** A mandatory 3-4 hour Cisco internal training course (COT00325705 on learn.cisco.com) that is a prerequisite before any GitHub Enterprise repository access can be granted. Without completing this, the team cannot see or touch any Cisco source code.
- **Owner:** BayOne (completion) / Cisco (providing access after completion)
- **Outstanding since:** February 17, 2026 — 42 days. Divakar shared the training link on the first day the WebEx group was active.
- **What has been tried:** Colin listed it as a pending item on March 13 and again on March 25. No message in the chat history confirms that Colin or any team member has completed this training. Colin referenced needing "hardware in hand" before completing it, but it is unclear whether the training actually requires Cisco hardware or can be completed via any browser with Cisco credentials.
- **Critical question:** Can this training be completed from any browser with a Cisco SSO login, or does it specifically require the Cisco laptop and VPN? If the former, this has been completable since February 17 and represents 42 days of avoidable delay on BayOne's side.

### Blocker 2: ADS Linux Machine Provisioning

- **What:** Cisco uses ADS (Application Development Server) Linux machines for code checkout, builds, and development. These are on-premises Cisco infrastructure, provisioned by Cisco IT. Without an ADS machine, the team cannot check out repositories or build code even after GitHub access is granted.
- **Owner:** Cisco — Divakar is the identified point of contact for initiating provisioning.
- **Outstanding since:** February 17, 2026 (identified during in-person discovery). Colin flagged it explicitly on March 13 and March 25, noting that "ADS provisioning in particular can take a bit to work through."
- **What has been tried:** Colin mentioned it twice in the group chat. There is no record in the chat of Divakar confirming that provisioning has been initiated or is in progress. Divakar was absent for a period and returned March 27.

### Blocker 3: VPN Setup and Network Access

- **What:** VPN access is required for everything on the Cisco network. Without it, even having a Cisco laptop is insufficient for accessing internal tools, repositories, or platforms.
- **Owner:** Cisco — general onboarding process. Anand added Shih-Ta Chi on March 26 to help with "general onboarding," which likely includes VPN.
- **Outstanding since:** February 17, 2026 (identified during discovery). Listed by Colin on March 13 and March 25.
- **What has been tried:** Colin listed it in both access-needs messages. Anand assigned Shih-Ta Chi on March 26 to help. Colin said he would message Shih-Ta on March 26. No confirmation of completion in the chat.

### Blocker 4: DeepSight Platform Access

- **What:** DeepSight Atlas is Cisco's existing AI platform that BayOne is expected to build on top of. Srinivas is the platform owner. Without DeepSight access, BayOne cannot develop, test, or deploy any AI applications — which is the entire scope of the engagement. This includes both platform access and the SDK/integration onboarding.
- **Owner:** Cisco — Srinivas (Srini) is the platform owner. The handoff from Rui (who built the existing CI/CD app on DeepSight) has not been initiated.
- **Outstanding since:** February 17, 2026. Srinivas shared a recording of the platform and the DeepSight URL on that date. Colin listed DeepSight access as a need on March 13 and March 25.
- **What has been tried:** The team reviewed the DeepSight recording (confirmed by Colin on March 13). Colin mentioned wanting to connect with Srinivas separately. No chat record of a DeepSight access request being formally submitted or acted on.

### Blocker 5: Airflow Subject Matter Expert (SME) Identification

- **What:** Airflow is a key orchestration component in Cisco's CI/CD pipeline. BayOne needs to understand the Airflow layer to build integrations. During discovery, Divakar mentioned that the Airflow SME sits on another team and he would need to reach out to them.
- **Owner:** Cisco — Divakar was going to identify and connect BayOne with the Airflow team.
- **Outstanding since:** February 17, 2026 (raised during discovery). Colin raised it again on March 25 ("identify the Airflow owner/SME").
- **What has been tried:** Colin asked about it. No record of Divakar making the introduction. BayOne has hired Namita specifically as an Airflow specialist, but she cannot begin work without understanding Cisco's Airflow setup.

### Blocker 6: Divakar Availability

- **What:** Divakar is the primary engineering contact at Cisco for access, infrastructure, Jenkins, and builds. He has been the named point of contact for ADS provisioning, Airflow SME introductions, and general technical onboarding. He was absent from the chat from approximately March 13 through March 27.
- **Owner:** Cisco
- **Outstanding since:** Mid-March 2026. Two-week gap in availability.
- **What has been tried:** Anand asked Divakar to help on March 26 ("if you are back today, can you please help?"). Divakar responded on March 27: "I am back today onwards, I can meet starting Monday" (March 30).
- **Current status:** Divakar should now be available as of March 30. This blocker may be resolving, but no meeting has been confirmed yet.

### Blocker 7 (Implicit): No Regular Status Cadence

- **What:** There is no established meeting cadence between BayOne and Cisco. All communication has been ad-hoc via WebEx chat, with Anand periodically asking for updates and Colin responding reactively. This creates the "losing steam" perception even when work is being done behind the scenes.
- **Owner:** BayOne (should have proposed this) / Cisco (needs to agree)
- **Outstanding since:** The engagement start. At no point in the chat history has anyone proposed a standing weekly or biweekly check-in.
- **What has been tried:** Nothing. This is a gap in engagement management.

---

## What Can Start RIGHT NOW Without Waiting

### 1. Complete the GitHub Enterprise Training — TODAY

The training link (https://learn.cisco.com/?courseID=COT00325705) was shared on February 17. If this training can be accessed with Cisco SSO credentials from any browser — which is the typical pattern for Cisco learning portal courses — then Colin, Saurav, Askari, and Srikar can all complete it today. Even if it requires VPN, Colin has his Cisco laptop and should be able to access it.

**Action:** Colin should attempt to access the training right now. If it works, the entire team with Cisco credentials should complete it by end of day tomorrow. If it requires VPN or specific access that is not yet available, document exactly what error appears and send that to Divakar and Shih-Ta immediately.

### 2. Analyze the DeepSight Recording in Structured Detail

Srinivas shared a DeepSight platform recording on February 17 with a direct link and password. Colin confirmed the team has reviewed it, but "reviewed" and "produced a structured technical analysis" are different things. The team can produce right now:

- A written architecture diagram of DeepSight as understood from the recording
- A list of SDK capabilities, endpoints, and integration patterns observed
- A gap analysis: what BayOne needs to know that was not covered in the recording
- A list of specific technical questions for Srinivas, organized by topic
- A proposed application architecture for the CI/CD tool built on top of DeepSight

This is real, visible, shareable work product that demonstrates the team has been doing more than waiting.

### 3. Build the Discovery Question List Into a Formal Document

Colin noted that approximately 45 of 65 discovery questions have been answered and about 20 remain open. The brainstorming notes list five discovery sessions for the next two weeks:

1. Local developer workflow
2. Branching / ownership / access to relevant repositories
3. Airflow / cross-application flow
4. Hosting / infra / deployment
5. AI access and DeepSight access

For each of these sessions, the team can prepare right now:
- A structured agenda with specific questions
- What is already known (from the Feb 17 discovery and the DeepSight recording)
- What specifically needs to be answered
- Who at Cisco needs to be in the room

This preparation document can be shared with Anand and Divakar immediately, showing that BayOne is organized and ready.

### 4. Draft the Technical Approach for Deliverables A and F

Deliverables A (Developer Box Instrumentation) and F (Branch Health / CD Visibility) were agreed as the Q1 starting focus. Based on what is already known from discovery:

- Developer Box Instrumentation requires telemetry capture of local test runs, coverage metrics, and pass/fail data before PR submission. The team can design the data model, telemetry schema, and collection approach without Cisco access.
- Branch Health / CD Visibility requires a consolidated dashboard for release leads with failure attribution. The team can design the dashboard wireframes, data requirements, and integration architecture using what is known about Jenkins, Airflow, CAT, DevX, and Grafana.

These are deliverable-quality work products that show engineering thinking, not just project management activity.

### 5. Prototype a Dashboard Mockup

Using the information from discovery about the tools in play (Jenkins, Airflow, GitHub Enterprise, CAT, DevX, Grafana) and the problems to solve (fragmented visibility, "where is my PR?" problem, failure attribution), the team can build a clickable mockup or static HTML prototype of what the unified dashboard could look like. This is a powerful demonstration artifact — it makes the abstract tangible.

### 6. Conduct Discovery Sessions via WebEx

Most of the remaining discovery questions do not require Cisco system access. They require conversations with Cisco engineers. These can happen over WebEx immediately:

- Local developer workflow: a 30-minute screen share with one Cisco developer walking through their daily process
- Branching and repository structure: Divakar can explain this verbally or share screenshots
- Airflow orchestration flow: requires the Airflow SME introduction, but the questions can be sent in advance

The brainstorming notes already list these as the planned sessions. The ask is simply to schedule them this week.

---

## Proposed Unblock Strategy

### Blocker 1: GitHub Enterprise Training

**Specific ask:** Colin to Divakar and Shih-Ta Chi — "Does the GitHub Enterprise training (COT00325705) require VPN access, or can it be completed from any browser with Cisco SSO? If VPN is required, what is the fastest path to get VPN configured for my team?"

**Fallback (48 hours):** If no response by April 2, escalate to Anand: "We need to confirm whether the training requires VPN. Can you check with your IT team?"

**Parallel action:** Every team member with Cisco credentials attempts to access the training portal today. Document results (success or specific error messages) and share in the WebEx group.

### Blocker 2: ADS Linux Machine Provisioning

**Specific ask:** Colin to Divakar — "Can you initiate ADS Linux machine provisioning for the following team members? [list names and Cisco IDs]. You mentioned this can take time, so I want to get it started immediately. Please let me know what information you need from us and I will have it to you within the hour."

**Fallback (48 hours):** If Divakar does not respond by April 2, escalate to Anand: "ADS provisioning has been identified as a blocker since February 17. Divakar is the owner but we have not been able to get this initiated. Can you help us get this moving or connect us with someone in Cisco IT who can process the request directly?"

**Parallel action:** While waiting for ADS machines, the team works on architecture design, DeepSight analysis, and prototype development using local environments.

### Blocker 3: VPN Setup and Network Access

**Specific ask:** Colin to Shih-Ta Chi — "Hi Shih-Ta, Anand connected us. I need VPN setup for myself and four team members. Here are our Cisco IDs and the access we need. What is the process, and what do you need from us to get started?"

**Fallback (48 hours):** If Shih-Ta does not respond by April 2, escalate to Anand: "I reached out to Shih-Ta on [date] about VPN setup and have not heard back. Can you help connect us with the right person to process VPN access?"

**Parallel action:** Colin should test whether his Cisco laptop already has VPN configured (it may have been included in the standard image). If so, document the process and share with the team.

### Blocker 4: DeepSight Platform Access

**Specific ask:** Colin to Srinivas — "Srini, my team has reviewed your DeepSight recording in depth and I have attached our technical analysis and questions. We are ready to start building. Can we schedule a 60-minute DeepSight onboarding session this week where you walk us through the SDK, show us the development workflow, and grant platform access? I also want to connect with Rui about the existing CI/CD app he built, so we can build on top of that work rather than duplicating it."

**Fallback (48 hours):** If Srinivas does not respond by April 2, escalate to Anand: "We need DeepSight platform access and an onboarding session with Srinivas to begin AI development. We also need to connect with Rui about the existing CI/CD app. Can you help facilitate?"

**Parallel action:** Complete the structured DeepSight analysis from the recording. Design the proposed application architecture. Prepare a written technical approach document that can be reviewed during the onboarding session.

### Blocker 5: Airflow SME Identification

**Specific ask:** Colin to Divakar — "During our February 17 discovery, you mentioned the Airflow SME sits on another team and you would reach out. Can you make that introduction this week? We have an Airflow specialist (Namita) joining our team and want to schedule a technical deep-dive on how Airflow orchestrates the CI/CD pipeline."

**Fallback (48 hours):** If Divakar does not respond, ask Srinivas: "Do you know who owns the Airflow layer in the CI/CD pipeline? We need to connect with them for our integration design work."

**Parallel action:** Namita (once onboarded) can document BayOne's Airflow integration approach based on what is known, preparing specific questions for the SME session.

### Blocker 6: Divakar Availability

**Specific ask:** Colin to Divakar — "Welcome back, Divakar. Can we schedule a 30-minute call on Monday or Tuesday this week? I have a short list of items I need your help with: ADS provisioning, Airflow SME introduction, and repository access. I want to make sure we are unblocked and moving."

**Fallback (48 hours):** If Divakar does not respond, escalate to Anand: "Divakar mentioned he is back and available starting Monday. I have reached out to schedule time but have not heard back. Can you help us connect?"

**Parallel action:** Send the specific asks to the WebEx group (not just to Divakar privately) so Anand has visibility into what is needed.

### Blocker 7: No Regular Status Cadence

**Specific ask:** Colin to Anand — "I would like to propose a weekly 15-minute status sync so you always have visibility into progress without needing to chase updates. Would Tuesday or Wednesday work? I will send a standing agenda: what was accomplished, what is planned, and what is blocked."

**Fallback:** This is entirely within BayOne's control. Propose it and schedule it. If Anand declines a live meeting, offer a weekly written status update sent every Monday or Friday.

**Parallel action:** Start sending structured weekly updates immediately, regardless of whether a meeting is established. The next one goes out today as part of the response to Anand's "any update?" message.

---

## What "Coming Out Swinging" Looks Like

The contract renewal date is April 30. That is 30 days away. The team has been assembled, briefed, and is idle waiting on access. The following is a concrete plan to demonstrate visible momentum in the next 1-2 weeks, independent of whether Cisco access issues are resolved.

### Week 1 (March 31 - April 4): Demonstrate Preparation and Technical Depth

**Deliverable 1: DeepSight Integration Technical Analysis**
A written document (3-5 pages) that demonstrates the team has studied the DeepSight platform recording in depth. It should include:
- Architecture diagram of DeepSight as understood from the recording
- Identified integration points for the CI/CD application
- Technical questions organized by topic for the onboarding session with Srinivas
- Proposed application architecture showing how Deliverables A and F will be built on DeepSight

This can be shared with Srinivas and Anand. It signals that BayOne is not waiting passively — the team is engineering.

**Deliverable 2: Structured Discovery Agenda Package**
For each of the five planned discovery sessions, produce a one-page document with:
- Session objective
- What is already known
- Specific questions to be answered
- Required attendees from Cisco
- Estimated duration

Share this with Anand and Divakar as "here is our plan for the next two weeks — we need your help scheduling these." This directly answers Anand's March 27 request for a tentative plan.

**Deliverable 3: GitHub Training Completion Confirmation**
Every team member who can access the training completes it and reports completion in the WebEx group. This is the single most visible, zero-ambiguity proof of progress. It eliminates one blocker entirely and shows the team is executing, not waiting.

**Action: Weekly Status Update #1**
Send a structured update to the WebEx group (and directly to Anand) covering:
- Team status: five members assembled, hardware in hand, DeepSight recording reviewed
- Training status: GitHub training completed (or specific blocker preventing it)
- Access status: what has been requested, from whom, current status
- Work in progress: DeepSight analysis, discovery preparation, architecture design
- Asks: specific items needed from Cisco with owner names

### Week 2 (April 7 - April 11): Demonstrate Engineering Capability

**Deliverable 4: Developer Box Instrumentation Design Document**
A technical design document for Deliverable A covering:
- Telemetry data model and schema
- Collection approach (how local test run data will be captured)
- Pipeline design for ingesting data into DeepSight
- Coverage metrics to be tracked
- Integration points with existing Cisco tools

This does not require Cisco access to produce. It requires engineering thinking applied to what is already known from discovery.

**Deliverable 5: Branch Health Dashboard Prototype**
A static HTML mockup or interactive prototype of the Branch Health / CD Visibility dashboard (Deliverable F). Based on the known data sources (Jenkins, Airflow, CAT, DevX, Grafana), show:
- What a release lead would see on their main dashboard view
- Failure attribution view (which PRs caused which failures)
- Notification and escalation workflow

This is the kind of artifact that makes stakeholders say "they are already building." It transforms the conversation from "when will you start?" to "let me give you feedback on this."

**Deliverable 6: Remaining Discovery Questions — Answered or Specifically Assigned**
By end of Week 2, every remaining discovery question should either be answered (from the scheduled sessions) or have a specific Cisco person and date assigned to answer it. No open questions should remain unassigned.

**Action: Weekly Status Update #2**
Second structured update showing:
- Discovery sessions completed and key findings
- Design documents produced
- Prototype demonstrated (screenshots or link)
- Remaining blockers with escalation timeline

### The Result by April 14

Two weeks from today, BayOne should be able to show Anand and Cisco:

1. GitHub training completed for the full team
2. A technical analysis of DeepSight with a proposed integration architecture
3. A design document for Developer Box Instrumentation (Deliverable A)
4. A prototype dashboard for Branch Health / CD Visibility (Deliverable F)
5. All discovery sessions completed or scheduled with specific dates
6. ADS provisioning and DeepSight access either granted or formally escalated with documentation
7. Two structured weekly status updates delivered on time

This is what "coming out swinging" looks like. It shifts the narrative from "BayOne has been waiting for two months" to "BayOne has been engineering for two weeks and is ready to deploy the moment access is granted." It gives Anand something concrete to point to when the April 30 renewal conversation happens. And it makes it clear that the remaining blockers are on the Cisco side, not the BayOne side — but framed constructively as "here is what we built while we waited, and here is what we will build the moment you unblock us."

---

## Summary: Blocker Ownership Matrix

| Blocker | Owner | Days Outstanding | BayOne Can Act Today? | Cisco Action Required? |
|---------|-------|------------------|-----------------------|------------------------|
| GitHub Enterprise Training | BayOne (completion) | 42 days | YES — attempt access immediately | Only if VPN is required |
| ADS Linux Machine Provisioning | Cisco (Divakar) | 42 days | No — Cisco infrastructure | YES — initiate provisioning |
| VPN Setup and Network Access | Cisco (Shih-Ta / IT) | 42 days | Partially — test Cisco laptop | YES — process VPN requests |
| DeepSight Platform Access | Cisco (Srinivas) | 42 days | Partially — analyze recording, design architecture | YES — grant access, schedule onboarding |
| Airflow SME Identification | Cisco (Divakar) | 42 days | No — need the introduction | YES — make the introduction |
| Divakar Availability | Cisco | Resolving (back Mar 27) | No | Schedule meeting this week |
| No Status Cadence | BayOne | 42 days | YES — propose and start immediately | Agree to cadence |

**Bottom line:** Of seven blockers, two are fully within BayOne's control to act on today (GitHub training and status cadence). Two more can be partially advanced by BayOne in parallel (DeepSight analysis and VPN testing). Three require Cisco action that has been requested but not executed. The single most important thing BayOne can do right now is complete the GitHub training and propose a regular status cadence — these are zero-dependency actions that demonstrate initiative and eliminate excuses.
