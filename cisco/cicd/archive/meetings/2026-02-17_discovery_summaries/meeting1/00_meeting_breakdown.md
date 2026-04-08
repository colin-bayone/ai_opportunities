# Meeting 1: CI/CD Kickoff with Anand, Srinivas, and Divakar

**Date:** February 17, 2026
**Location:** Cisco Office, 3rd Floor (in-person)
**Duration:** ~60 minutes (extended from planned 30 minutes)
**Recording Status:** Not recorded (recommendation made to record future sessions)

---

## Participants

| Name | Organization | Role | Scope in Meeting |
|------|--------------|------|------------------|
| Colin Moore | BayOne | Director of AI, Technical Lead | Asking discovery questions, project accountability |
| Anand | Cisco | Director | Brief appearance; high-level coordination, escalation path |
| Divakar | Cisco | Engineering Lead | Access, infrastructure, build systems, Bazel deployment |
| Srinivas (Srini) | Cisco | Senior Engineering Manager | AI platform (DeepSight), technical strategy, agentic infrastructure |

**Context:** Anand was pulled away early due to Bazel production rollout issues. Srinivas (Srini) was supposed to join in person but was debugging something since morning, so he joined the second half. Divakar handled most access/infrastructure questions.

**Transcription Note:** Speech-to-text rendered "Divakar" as "the worker" throughout, "Bazel" as "basil/bezel", "DeepSight Atlas" as "total less", and "Zahra" as "Java/Gerard/C".

---

## Meeting Structure

Three distinct phases:
1. **Phase 1 (Anand + Divakar):** Brief kickoff, context on Bazel rollout stress (~5 min)
2. **Phase 2 (Divakar primarily):** Access requirements, infrastructure, rapid-fire discovery questions (~25 min)
3. **Phase 3 (Srinivas):** DeepSight AI platform introduction, technical philosophy, working relationship expectations (~30 min)

---

## Context: Current Cisco State

**Bazel Production Rollout (Critical Background):**
- Cisco just rolled out Bazel (Google's build system) to production
- Working with every branch owner to enable Bazel and bring in code
- Multiple concurrent initiatives: PQC, NXOS video, NGP FM, Spectrum
- Dealing with sanity issues and build issues
- Engineers stretched thin - "it's been crazy"
- This explains why Srini was debugging instead of attending in person

**Key Quote (Anand):** "We really want these things to kind of help us a lot... If we do our job right, your job will be easier. That's how I get ready with the maintenance overload or operational overheads."

---

## Discussion Topics (Chronological)

### 1. Systems Architecture Confirmation (with Divakar)

Colin presented understanding of systems; Divakar confirmed/updated:

| System | Owner/Access Point | Notes |
|--------|-------------------|-------|
| GitHub Enterprise | Requires 3-4 hour training | Divakar grants access after training |
| Jenkins | Divakar has full context | Will bring in his engineer |
| Airflow | Different team | Divakar needs to reach out |
| DevX Platform | Different team | Can get data from there |
| **Bazel** | **Missing from Colin's list** | **Critical - added during meeting** |
| CAT (Commit Approval Tool) | - | Mentioned as "CAC retooling" |
| Jira | Divakar | "Not using it anymore" - informal process |

**Key Quote (Divakar):** "There are different teams for different systems. It's a crossover."

**Colin's Forward-Looking Vision:** Mentioned hoping to build "some kind of MCP on top of [Jenkins] to be able to talk to GitHub to get data like how many comments are going through, how many branches are there, what is having issues."

### 2. Access & Onboarding (Rapid-Fire Q&A)

**Formal Ticketing for Access Requests:**
- **Answer: No formal system**
- Engineers pushed back: "I cannot go and create a ticket every single time"
- Process is very informal - just ping and ask
- For new issues, can use WebEx space to post and get answers

**Single Point of Contact:**
- Divakar for technical access
- Anand for escalations and unblocking

**Access Turnaround:**
- Should not be more than half a day, maybe a day max after training completion

**Network Access Model:**
- VPN required for everything
- Options: Cisco laptop OR Cisco image on personal laptop
- Colin's laptop provisioning already initiated by Rahul
- Without VPN: cannot connect to emails, machines, or anything

**Background Check Status:**
- Colin's: **DONE** (confirmed via Rahul ping during meeting)
- NDA: **Can be signed by end of day Feb 17**

**Development Environment:**
- Requires ADS machine (Linux) provisioned by Cisco
- Located in Cisco data center (on-prem)
- Needed to: check out code, view code, build code
- This is ON TOP of VPN access

**Staging/Dev Environment:**
- Development environment exists but "not using it as much"
- **Read-only access only** - cannot commit, cannot push
- Can view PR validations in progress
- Local workspace changes stay local; GitHub rejects pushes
- This isolation is intentional: "we want to make sure we're not doing things without you"

### 3. Infrastructure Details (with Divakar)

**Database:**
- Cisco uses **MySQL** for all services
- Colin's team prefers Postgres, but MySQL is acceptable
- Divakar will check with IT on provisioning (self-service vs request)
- Need to determine: row counts, transactions/day, parallel connections

**Container Runtime:**
- **Podman** (Red Hat apartment containers), **NOT Docker**
- Containers supported for deployment

**Raw Pipeline Data:**
- Stored in **MongoDB**
- Single location, on-prem

**Logging:**
- **Splunk** connected to Jenkins
- Splunk primarily for security team
- Divakar can provide direct Jenkins access for logs
- Colin: "I figured it was Splunk. It makes sense with you guys."

**Colin's Note on Integration:** "That'll be part of that whenever we do the next quarter integration and the box C [Item C: Unified Interface]. That'll connect all the different services together."

### 4. AI/LLM Infrastructure (Transition to Srinivas)

**Initial Clarification (Divakar):**
- Cisco will provide AI services (not BayOne's own)
- Srinivas is the contact for AI-related work
- Colin will be "a new application built on top of that platform"

### 5. DeepSight Platform Introduction (Srinivas)

**What is DeepSight:**
- Cisco's internal AI platform - **already live in production**
- Full name: **DeepSight Atlas** (the entire infrastructure)
- Multiple apps planned (8-10), releasing one at a time

**Current/Upcoming DeepSight Apps:**
| App | Status |
|-----|--------|
| **Triage** | Launched last weekend |
| **Runbook** | Launching end of this week |
| **Telemetry** | Aggregation of all applications |
| **CI/CD App** | Exists, launching in 2-3 weeks |

**CI/CD App Status:**
- **Rui** (on Arun's team) is working on it
- Current form exists, needs to launch on DeepSight platform
- Srini: "In the next two weeks, I work with Arun's team, Rui is there, to launch that application"
- Colin's team picks it up from there and extends it

**What BayOne Will Build:**
- Application ON TOP of DeepSight platform
- All AI stack is provided: SDK, infrastructure, everything
- **Work becomes:** Build MCP/LCP, build prompts, stitch together
- Should NOT spend time on infrastructure - it's 90% done

**Key Quote (Srinivas):** "You are not building anything in AI stack because all the AI stack is given to you. Everything else is given to you. All you have to do is build an [MCP], build a patch of prompts queries and stitch it here."

**Expected Timeline:** "My expectation is within like two months, we should have an app running live here. Because all the infrastructure is already built for you."

**DeepSight Recording:**
- Srinivas will share via WebEx: 1-1.5 hour recording of DCT presentation
- Covers how Triage app is done, infrastructure pieces, look and feel
- Once watched, Colin will understand what the app will look like

**Code Repository for DeepSight:**
- Repos created for every application as part of DeepSight
- Colin commits code there
- Code reviewed and merged by DeepSight team
- Separate access needed for NX-OS code (requires the 3-4 hour training)

**Colin's Observation:** "We have a similar platform, so that's a really cool thing. Yours is much nicer, I have to say, for the UI, but it's similar approach to it."

### 6. Srinivas's Technical Philosophy

**Key Principles (Direct Quotes):**

1. **Extensibility First:**
> "Always put two hats when you evaluate. One, will you solve my current need? Two, can it be extensible? Or can I today write the infrastructure in a way that it is available for agentic infrastructure?"

2. **Agentic Infrastructure:**
> "Anything we do should be future proof and ready to enable the agentic infrastructure. So while you are solving your current need, we may be solving another agentic infrastructure behind the scenes."

3. **Reusability:**
> "You need to step back and say, how do I make this infrastructure generally so that we can leverage it in other places. So you guys are not building a pointed solution, but you're building infrastructure pieces where I can leverage in other places."

4. **Direct Communication:**
> "Once you start working, it's engineer-to-engineer conversation. You'll find a good partner."

5. **Open Disagreement:**
> "You can always correct me saying that you are wrong. I don't mind in the private or for me it doesn't matter. From the technical point of view, it doesn't matter if you can catch me anywhere, even in peak meetings."

6. **Fast Pace:**
> "I go very fast, very, very fast. People know me who are working with me. And sometimes, team might say, why is Srini so aggressive, right? Because that's my nature."

7. **Colleague Relationship:**
> "Once you are onboarding, you are my friend. So I'll treat you the way or treat me the same way as a colleague."

### 7. Progress Tracking & Working Rhythm

**Status Meetings:**
- Two weeks from Feb 17: catch-up meeting with Anand, Divakar, Srinivas
- Following week: determine ongoing cadence
- Anand may involve Arun depending on progress

**Recording Sessions:**
- Srinivas strongly recommends recording all sessions
- Allows team members to catch up
- "You should always say, can we have a recorded session... because many other team members will say, hey, take a day, record, go through all the recording."

**Communication:**
- WebEx space for day-to-day questions
- Use existing "Bay1" space (not Zahra's newly created duplicate)
- If something not moving, escalate to Srinivas
- Srinivas will monitor and ensure questions get answered

### 8. Timeline & Quarter Alignment

**Current State:**
- Cisco Q3 started January 26, 2026
- Almost a month in already

**Agreement Reached:**
- **Quarter starts when access is granted**
- Cisco is flexible on timeline
- "Whenever we get started, the quarter starts then"

**Key Quote (Anand):** "I know practically it's never possible to start quarter here and there, so we understand that, and we're very flexible on that... It's called business reality versus engineering reality."

### 9. SOW Status

- SOW still pending
- Colin accidentally created a tool for Cisco's SOW format (thought it was BayOne internal)
- Anand gave something to internal team
- Zahra is working on it

### 10. Onboarding Other Team Members

**BayOne Team Status:**
| Person | Status |
|--------|--------|
| Colin | On-site immediately, background check done |
| Person 2 | Background check done, hardware being requested |
| Person 3 | Available within 2 weeks |
| Person 4-5 | Offshore, identified and active |

**Onboarding Process Pain Point (Srinivas raised):**
- ADS/machine provisioning takes time for new engineers
- No set procedure - often requires chasing approvals
- "We are spending a lot of time to get the ADS or the provision to those engineers"
- Srinivas asked Anand to help standardize this for scaling

### 11. Post-Meeting Reflection (Colin + Srinivas)

After formal meeting ended, candid discussion about working styles:

**Colin's Mentor Quote (shared with Srinivas):**
> "My first boss... told me the Golden Rule... you have time to do it, or redo it down the line a week done. Where I feel good is whenever I can walk away from things and I don't have to hear about them or touch them in 10 years. That's great for me. That means I did something right."

**On Client Types:**
- Colin: "Sometimes in solutions... there's two types of client. Type one wants you to do something exactly as prescribed, and against all of your instincts, you have to do it. Refreshing that's not [the case here]."
- Srinivas: "We are also forced to do that [sometimes]. There is a customer requirement, there is a timeline requirement... But I think these guys are like-minded."

---

## Decisions Made

| Decision | Made By | Context |
|----------|---------|---------|
| BayOne builds on DeepSight platform, not from scratch | Srinivas | AI infrastructure already exists, 90% done |
| MySQL will be used (not Postgres) | Divakar/Colin | Cisco's standard stack |
| Podman containers for deployment | Divakar | Red Hat standard, not Docker |
| Read-only access to main repos initially | Divakar | Security constraint, intentional isolation |
| Quarter timing starts when access granted | Anand | Flexibility on fiscal alignment |
| All technical sessions should be recorded | Srinivas | For team knowledge transfer |
| Status meeting in 2 weeks | Anand | Initial check-in cadence |
| Use existing "Bay1" WebEx space | All | Not Zahra's newly created duplicate |

---

## Commitments Made

### Cisco Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| Divakar | Add engineers to WebEx space | Ongoing |
| Divakar | Provide Jenkins access | After GitHub training |
| Divakar | Check with IT on MySQL provisioning | TBD |
| Divakar | Provision ADS Linux machines | After onboarding |
| Divakar | Reach out to Airflow team | TBD |
| Srinivas | Share DeepSight presentation recording (via WebEx) | After NDA signed |
| Srinivas | Launch existing CI/CD app on DeepSight | 2-3 weeks (end Feb/early March) |
| Srinivas | Pull Colin into other meetings once CI/CD app running | Post-launch |
| Srinivas | Request Rui to hand off CI/CD app work | Via WebEx group |
| Anand | Ensure questions get answered, unblock as needed | Ongoing |
| Anand | Monitor onboarding process as test case for scaling | This engagement |

### BayOne Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| Colin | Complete GitHub Enterprise training (3-4 hours) | ASAP |
| Colin | Get NDA signed | End of day Feb 17 |
| Colin | Watch DeepSight presentation recording (1-1.5 hours) | Before next meeting |
| Colin | Ensure all 5 team members complete GitHub training | As they onboard |
| Colin | Keep everything organized from project perspective | Ongoing |
| Colin | Ping Divakar for access items | Ongoing |
| Colin | Always request recorded sessions | Going forward |

---

## Open Items / Action Items

| Item | Owner | Priority | Notes |
|------|-------|----------|-------|
| Sign NDA | Colin/BayOne | **Immediate** | Can be done Feb 17 EOD |
| Complete GitHub Enterprise training | Colin + team | **High** | 3-4 hours, unlocks repo access |
| Watch DeepSight presentation | Colin | **High** | 1-1.5 hours, understand platform |
| Provision ADS Linux machines | Divakar | **High** | Blocking for code access |
| Finalize SOW | Zahra/Cisco | **High** | In progress |
| Check MySQL provisioning options | Divakar | Medium | Self-service vs request |
| Reach out to Airflow team | Divakar | Medium | For Airflow access |
| Add Rui request to WebEx for CI/CD handoff | Srinivas | Medium | After app launches |
| Determine detailed data requirements | Colin | Medium | Rows, transactions for DB sizing |
| Schedule 2-week status meeting | Anand | Medium | With Anand, Divakar, Srinivas |
| Hardware provisioning for 2nd BayOne person | Rahul/Cisco | Medium | In progress |

---

## Answers to Discovery Questions

Cross-referenced with `claude/2026-02-17_discovery-call-prep/discovery_call_questions.md`:

| Q# | Question | Answer |
|----|----------|--------|
| 1 | Internal ticketing system for access? | **No formal system.** Very informal - just ping and ask. |
| 2 | Single point of contact for access? | **Divakar** for technical, **Anand** for escalations |
| 3 | Turnaround time for access? | **Half day to 1 day** after training completion |
| 4 | Network access model? | **VPN required.** Cisco laptop or Cisco image on personal laptop. |
| 5 | Who initiates network access? | **Rahul** (BayOne) already initiated for Colin |
| 6 | Different access tiers (onshore/offshore)? | **No**, small team doesn't need tiers |
| 9 | Cisco-managed machines or own? | **ADS machines** (Linux) provisioned by Cisco, on-prem in data center |
| 11 | Staging/dev environment? | **Exists** but not used much. **Read-only access only.** |
| 13 | Database options? | **MySQL** (Cisco standard) |
| 15 | Deployment pattern? | **Podman containers** (Red Hat, not Docker) |
| 16 | Where does raw pipeline data live? | **MongoDB**, single location, on-prem |
| 17 | Logging stack? | **Splunk** (via Jenkins), can also get direct Jenkins access |
| 22-25 | AI/LLM services? | **DeepSight platform** - SDK provided, all infrastructure given |

**Questions Still to Answer:**
- Q7: Background check initiation process (moot for Colin, still relevant for others)
- Q10: Testing developer-side tooling without same local environment
- Q12: Server provisioning process (Divakar checking with IT)
- Q14: Shared services vs isolated infrastructure
- Q18: Data retention policies
- Q19-21: Airflow details (different team - Divakar reaching out)
- Q26+: SME contacts for various areas
- Q42-48: Scale & metrics questions (PR volume, merge times, failure rates)

---

## Cross-References to Project Documents

| Document | Relevant Section | Status After Meeting |
|----------|------------------|---------------------|
| `project/engagement-status.md` | Current phase, priorities | Needs update: Discovery started, DeepSight confirmed |
| `documents/cisco-understanding-of-problem.md` | Pipeline structure | Confirmed: Blue/Green/Red boxes accurate |
| `documents/cisco-questions-for-clarification.md` | 48+ questions | ~12 answered, many still pending |
| `claude/2026-02-02_resource-planning/deliverables/resource_plan_for_cisco.html` | Team structure | Confirmed: 5 people (3 onshore, 2 offshore) |
| `new_context_2-2-2026/meetings/email-1-16-2026.txt` | A+F priorities | Confirmed still active |

**New Information Not in Existing Docs:**
1. **DeepSight Atlas** - Cisco's AI platform, not previously documented
2. **Rui** - New contact on Arun's team, owns existing CI/CD app
3. **Bazel** - Build system rollout, critical current context
4. **2-month timeline** - Srinivas's expectation for live app

---

## People Directory (Updated)

| Name | Organization | Role | Contact Context |
|------|--------------|------|-----------------|
| **Colin Moore** | BayOne | Director of AI, Technical Lead | Primary BayOne contact |
| **Anand** | Cisco | Director | Escalations, status meetings, unblocking |
| **Divakar** | Cisco | Engineering Lead | Access, infrastructure, Jenkins, builds |
| **Srinivas (Srini)** | Cisco | Senior Engineering Manager | DeepSight/AI platform, technical strategy |
| **Rui** | Cisco | Engineer (Arun's team) | Existing CI/CD app, handoff point |
| **Arun** | Cisco | VP | Rui's manager, mentioned but not present |
| **Rahul** | BayOne | President | Hardware/access initiation |
| **Zahra** | BayOne | Sales | SOW, NDA coordination |

---

## Key Insights

1. **Dramatically reduced AI scope:** DeepSight platform means BayOne doesn't need to build AI infrastructure from scratch. This changes the entire engagement model - focus shifts to application logic, prompts, and integration rather than infrastructure.

2. **Existing CI/CD app exists:** There's already a CI/CD application (Rui's work) launching in 2-3 weeks. BayOne extends this rather than starting fresh. Need to coordinate handoff with Rui.

3. **Cultural fit confirmed:** Srinivas explicitly values direct communication, disagreement, and engineering-first thinking. Colin's "10-year test" philosophy resonated. This is a collaborative technical partnership, not a vendor relationship.

4. **Bazel context critical:** The team is stressed from Bazel production rollout. This explains limited availability and sets expectation that Cisco engineers are under pressure.

5. **Infrastructure bottleneck known:** ADS machine provisioning is a known pain point for all new engineers. Anand agreed to monitor this engagement as a test case for improving the process.

6. **Informal culture - risk and benefit:** No ticketing, no formal processes means fast iteration but no paper trail. Need to use WebEx space effectively and request recordings.

7. **MCP mentioned by Colin:** Colin proactively mentioned wanting to build "some kind of MCP" for Jenkins/GitHub integration - aligns with modern tooling patterns.

---

## Clarifications Needed

1. **Jira Status:** Divakar said "not using it anymore" - is there ANY issue tracking? How are bugs and feature requests managed?

2. **WebEx Space Confusion:** Zahra created a duplicate space. Confirmed use "Bay1" original space. Need to clarify with Zahra.

3. **Rui Handoff:** When exactly? What's the current state of the CI/CD app? What will be left to do?

4. **DeepSight Spelling:** Is it "DeepSight" or "Deep Sight"? Transcript unclear.

5. **LCP vs MCP:** Srinivas mentioned "LCP" - is this their term for MCP, or something else?

---

## Next Meeting

**What:** Follow-up discovery session (rapid-fire questions 18-65)
**When:** February 18, 2026 (tomorrow)
**Who:** Colin, Divakar
**Purpose:** Continue through remaining discovery questions

**Status Check-in:**
**What:** Progress catch-up
**When:** ~2 weeks from Feb 17 (early March)
**Who:** Colin, Anand, Divakar, Srinivas
**Purpose:** Review onboarding progress, determine ongoing cadence

---

## Files Referenced

- DeepSight presentation recording (to be shared by Srinivas via WebEx after NDA)
- Colin's discovery questions document (reviewed during meeting)
- SOW documents (in progress with Zahra)
- GitHub Enterprise training materials (required before access)
