# Cisco CI/CD Engagement — Current Understanding

**Last Updated:** 2026-03-31
**Author:** Colin Moore / AI Practice

---

## Engagement Overview

BayOne is engaged to build AI-powered CI/CD pipeline tooling for Cisco's Cloud Networking Group (CN Test team), focused on the Nexus 9000 (switches) product line. The work involves improving visibility, diagnosis, and automation across Cisco's fragmented CI/CD pipeline (Jenkins, Airflow, GitHub Enterprise, CAT, DevX, Grafana).

**SOW Reference:** #33282 — FY26Q3_Building Nexus 9000 (switches) product line_Bayone
**SOW Budget (INR):** Rs 4,393,740.00
**Quarterly Budget Target:** ~$100K/quarter (USD, per Anand)
**Work Location:** Cisco BGL15 (Bangalore) + Bay Area onshore presence

---

## Actual Timeline (What Really Happened)

| Date | Event |
|------|-------|
| ~Nov 2025 | First conversations with Cisco about CI/CD opportunity |
| ~Dec 15, 2025 | Discovery call — identified six problem areas (A-F) |
| Jan 9-20, 2026 | Rahul visits Cisco in person; meetings with Anand's team |
| Jan 16, 2026 | Zahra sends meeting summary email; agreement on A+F as starting focus, ~$100K/quarter budget, discovery-first approach |
| Late Jan 2026 | Agreement conversations completed; BayOne begins internal resource planning |
| Feb 2, 2026 | Resource planning documents finalized (approach, roles, JDs, cost estimates, quarterly phasing) |
| Feb 4, 2026 | Zahra/Colin pricing call — aligned on $150-200K ask, staffing strategy |
| Feb 10, 2026 | Anand creates WebEx group; asks Zahra to add Colin and get started |
| Feb 17, 2026 | Colin's in-person discovery at Cisco office — met Anand, Divakar, Srinivas; learned about DeepSight Atlas platform; Divakar shares GitHub training link; Srinivas shares DeepSight recording |
| Feb 18, 2026 | Colin shares discovery notes and remaining questions in WebEx group |
| Mar 3, 2026 | Anand asks "is everyone on board?" — Zahra responds SOW still pending Cisco procurement approval |
| Mar 12, 2026 | Anand follows up again: "This is losing steam" |
| Mar 13, 2026 | Colin responds: SOW procurement delay resolved, India team picking up equipment 3/16, US hardware in transit for mid-week delivery. Lists access needs (GitHub training, ADS machines, VPN, DeepSight). Offers to visit Bay Area week of 3/23 |
| Mar 17, 2026 | Colin DMs Anand: laptops STILL not ordered despite being told they would arrive this week. Asks Anand to help unblock asset management or allow BayOne to self-procure with Cisco image |
| Mar 18, 2026 | First internal team meeting — Colin with Saurav (offshore) and Askari (offshore). Sets ground rules, walks through problem architecture. Saurav has both laptops; Askari has Cisco only, BayOne laptop just shipped |
| Mar 23, 2026 | Anand asks in group chat: "What are next steps? Is all access/permission taken care?" |
| Mar 25, 2026 | Colin responds: has Cisco hardware, setup complete. Lists remaining access needs (same list as Mar 13). Colin and Rahul physically at Cisco Building 20 for another meeting; offer to stop by informally. Says ready for IC-level discovery meetings |
| Mar 26, 2026 | Anand adds Shih-Ta Chi to help with onboarding. Divakar back from absence. Anand DMs Colin to use WebEx space for needs |
| Mar 27, 2026 | Anand asks: "Can we come up with a tentative plan for next couple of weeks?" Divakar says he can meet starting Monday |
| Mar 30, 2026 | Internal team meeting — Colin with Saurav, Askari, Srikar (new, Bay Area based). Full team walkthrough of problem, solution architecture, Q1 deliverables, discovery plan. Namita (5th member, Airflow specialist) expected next week pending H1B |
| **Mar 31, 2026** | **Anand follows up: "Any update on this?"** — TODAY, needs immediate response |

**Key point:** The SOW document lists "Estimated Start Date: 11/5/2025" but this is a Cisco fiscal placeholder for their Q3 budget allocation. The actual agreement wasn't reached until late January 2026, the SOW wasn't approved by Cisco procurement until mid-March 2026, and then hardware provisioning was further delayed (equipment not ordered despite promises). Two months lost to Cisco's own procurement and provisioning processes.

## BayOne Team (Current as of March 30)

| Name | Role | Location | Status |
|------|------|----------|--------|
| Colin Moore | Director of AI, project lead | Remote (Pennsylvania), travels to Bay Area | Has Cisco hardware, setup complete |
| Srikar | AI Engineer, on-site at Cisco | San Francisco Bay Area | Has Cisco hardware, awaiting BayOne laptop |
| Namita | Agentic AI / Airflow specialist, on-site at Cisco | California (Bay Area) | H1B transfer in progress; expected to start next week |
| Saurav Kumar Mishra | AI/ML Engineer | Offshore (India) | Has both BayOne and Cisco laptops |
| Askari Sayed | AI Engineer | Offshore (India) | Has Cisco laptop; BayOne laptop shipped Mar 18 |

---

## What the SOW Covers (Six Deliverables, A-F)

### A — Developer Box Instrumentation
- Capture local test runs, coverage metrics, pass/fail before PR submission
- Build telemetry system and data pipeline
- Condition-level coverage tracking
- **Priority: Q1 focus (agreed with Anand)**

### B — Gate Failures / AI Diagnosis
- AI-driven root cause analysis of gate failures across 39 gates
- Analyze logs, suggest fixes
- Surface diagnosis in unified interface
- **Priority: Q3**

### C — Unified Data Layer / Chat Interface
- Consolidate data from CAT, DevX, Jenkins, Airflow, Grafana
- Natural language chat interface ("Where is my PR?")
- Single pane of glass across fragmented tools
- **Priority: Q2**

### D — Coverage Tracking Enhancement
- Condition-level tracking beyond what CDT provides
- Confirm PR changes were actually exercised by tests
- End-to-end visibility from Developer Box through CI
- **Priority: Q3**

### E — Self-Healing / Auto-Resume
- Automated corrective actions for qualifying failures
- Governance framework, safety mechanisms, rollback
- **Most complex deliverable; deferred to Q4 or Year 2**

### F — Branch Health / CD Visibility
- Consolidated dashboard for release leads
- Failure attribution (which PRs caused issues)
- Automated follow-up notifications/escalations
- **Priority: Q1 focus (agreed with Anand)**

**Agreed starting focus:** A + F as quick wins to build credibility, then expand.

---

## Planned Team Structure

| Role | Location | Start | Rate/Quarter |
|------|----------|-------|-------------|
| Senior Engineer (technical lead, Cisco interface) | Onshore, Bay Area | Q1 | ~$47K |
| Backend/Integration Engineer (Airflow required) | Offshore, India | Q1 | ~$12K |
| AI Engineer (LLMs, NLP, LangChain) | Offshore, India | Q1 | ~$12.5K |
| UI/Application Developer | Offshore, India | Late Q1/Q2 | ~$12K |
| Agentic AI Specialist | Offshore, India | Early Q2 | ~$16K |

**Year total:** ~$370K (under $400K by $30K)
**Colin Moore:** Director of AI, final decisions, oversight, hands-on during discovery

---

## Key Discovery Findings (Feb 17 In-Person)

### DeepSight Atlas — Major Scope Change
- Cisco has an **existing AI platform** (DeepSight Atlas) already live in production
- Multiple apps: Triage (live), Runbook (launching), CI/CD app (Rui building, was 2-3 weeks from launch as of Feb 17)
- BayOne builds **on top of** DeepSight, not from scratch
- SDK and AI infrastructure provided — focus shifts to application logic, prompts, MCP integration
- Srinivas's expectation: "within two months, we should have an app running live"

### Infrastructure Stack Confirmed
- **Database:** MySQL (Cisco standard)
- **Raw pipeline data:** MongoDB (on-prem, single location)
- **Containers:** Podman (Red Hat), not Docker
- **Logging:** Splunk via Jenkins; direct Jenkins access offered
- **Code access:** ADS Linux machines (provisioned by Cisco, on-prem)
- **Network:** VPN required for everything; Cisco laptop or Cisco image

### Access & Onboarding Status (as of Feb 17)
- Colin: background check done, NDA signed, GitHub training pending (3-4 hours)
- Person 2: background check done, hardware being requested
- Person 3: available within 2 weeks
- Persons 4-5: offshore, identified
- Divakar: primary contact for technical access
- Turnaround after training: half day to one day

### Unanswered Discovery Questions (~30 of 65 still open)
- Data retention policies
- Airflow details (version, SME, deployment)
- Scale metrics (PRs/day, active developers, branches, failure rates)
- Data restrictions for AI APIs
- Server provisioning process ownership
- Development workflow governance (where does BayOne commit code?)

---

## Key Cisco Contacts

| Name | Role | Scope |
|------|------|-------|
| Anand | Director | Escalations, status meetings, budget authority |
| Divakar | Engineering Lead | Access, infrastructure, Jenkins, builds |
| Srinivas (Srini) | Senior Engineering Manager | DeepSight/AI platform, technical strategy |
| Rui | Engineer (Arun's team) | Existing CI/CD app on DeepSight |
| Arun | VP | Rui's manager; significant budget authority |
| Mahaveer Jinka | SOW Owner | SOW preparation/procurement side |

## Key BayOne Contacts

| Name | Role |
|------|------|
| Colin Moore | Director of AI, technical lead |
| Zahra | Sales, SOW/NDA coordination, Cisco relationship |
| Rahul Bobbili | Delivery, hardware/access initiation |

---

## The Crisis (March 31, 2026)

**Cisco agreed to this engagement in late January. It is now end of March — no development work has started.**

The delays break down as:
1. **Nov 2025 - late Jan 2026 (~3 months):** Normal pre-engagement: conversations, discovery calls, scope alignment, agreement on A+F starting focus and ~$100K/quarter budget.
2. **Late Jan - mid Mar 2026 (~6 weeks):** Cisco procurement sat on the SOW for 6+ weeks. BayOne used this time productively (resource planning, hiring, JDs, cost modeling). Colin did in-person discovery Feb 17.
3. **Mid Mar 2026:** SOW finally approved. But then hardware not ordered despite promises. Colin had to escalate to Anand on Mar 17 after learning equipment hadn't even been ordered yet.
4. **Late Mar 2026:** Hardware finally arriving. India team picking up equipment. Colin has his Cisco laptop and is set up. But GitHub training, ADS machines, VPN, DeepSight access all still outstanding.

**The pattern in the WebEx chat is clear:** Anand checks in, gets told things are delayed, waits, checks in again, gets told things are still delayed. His messages are getting shorter and more direct:
- Mar 3: "How is it going? Is everyone on board?"
- Mar 12: "Do you have any visibility? Anywhere I can help? This is losing steam."
- Mar 23: "What are next steps? Is all access/permission taken care?"
- Mar 27: "Can we come up with a tentative plan for next couple of weeks?"
- Mar 31: "Any update on this?"

**What BayOne HAS accomplished (not visible to Cisco):**
- Full 5-person team assembled: Colin (lead), Srikar (Bay Area on-site), Namita (Bay Area, H1B pending), Saurav (offshore), Askari (offshore)
- Complete resource planning for a full year (roles, quarterly phasing, cost estimates)
- In-person discovery Feb 17 with major findings (DeepSight platform, infrastructure stack, access requirements)
- ~45 of 65 discovery questions answered
- Two internal team meetings (Mar 18, Mar 30) — team is briefed on the problem, architecture, key contacts, and ground rules
- Team has reviewed DeepSight platform recording
- Colin physically at Cisco campus Mar 25 (for another meeting), offered to meet informally

**What has NOT happened:**
- No GitHub Enterprise training completed (prerequisite for repo access)
- No ADS Linux machine access (needed for code checkout and builds)
- No VPN access for full team
- No code written
- No deliverables produced
- No formal status cadence with Cisco
- DeepSight CI/CD app handoff from Rui not initiated
- Airflow SME at Cisco not identified

**The contract renewal date is April 30.** Colin has told his team there's no way Q1 deliverables will be done by then, but they MUST show visible progress and momentum before that date.

---

## Immediate Priority: Respond to Anand (Mar 31)

Anand asked "Any update on this?" — referring to the tentative 2-week plan he requested on Mar 27. This needs a response TODAY that:

1. **Provides a concrete 2-week plan** with specific discovery sessions and outcomes
2. **Shows the team is ready** — hardware in hand, team assembled, briefed on problem
3. **Requests specific help** — GitHub training access, ADS provisioning, Airflow SME, DeepSight onboarding
4. **Proposes a regular status cadence** so Anand doesn't have to keep chasing updates
5. **Frames momentum** — team has been preparing during the procurement delay, ready to execute immediately

Colin's brainstormed discovery topics for the 2-week plan:
- Local developer workflow
- Branching / ownership / access to relevant repositories (read-level permissions for svc account)
- Airflow / cross-application flow
- Hosting / infra / deployment
- AI access and DeepSight access
