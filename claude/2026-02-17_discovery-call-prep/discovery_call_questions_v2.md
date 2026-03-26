# Discovery Session: NX-OS CI/CD Pipeline Improvement (v2)
**Prepared by:** BayOne Solutions
**For:** Cisco (Anand, Srinivas, Divakar)
**Updated:** February 17, 2026
**Purpose:** Remaining open questions after Meeting 1

---

## Context

This is v2 of the discovery questions document, updated after the February 17, 2026 in-person meeting with Anand, Divakar, and Srinivas. Questions that were resolved have been removed.

**Key outcomes from Meeting 1:**
- WebEx space (BayOne CICD WG) is the primary communication channel
- Divakar is the main access contact; Srinivas for DeepSight/AI platform
- DeepSight platform provides all AI infrastructure - BayOne builds on top
- Existing CICD app will be live in 2-3 weeks; BayOne extends it
- Timeline is flexible: "quarter starts when BayOne starts"
- Two-week check-in after onboarding to establish cadence

---

## Section 1: Access Requirements (Remaining Items)

### 1.1 Network Access

**Partially Resolved:**

| Item | Status | Notes |
|------|--------|-------|
| Network access initiation | In progress | Rahul Bobbili coordinating; Cisco-provided equipment expected to resolve most issues. Monitor for any blockers. |

### 1.2 Development Environment

**Questions for Follow-up:**

1. **Development workflow governance:** Where does BayOne's code go? Will Cisco provide a repository, or should BayOne set up independently? *(Note: Srinivas mentioned DeepSight has repos created for every application - need to confirm this covers all BayOne work)*

---

## Section 2: Infrastructure & Deployment Environment (Remaining Items)

### 2.1 Compute & Database Infrastructure

**Partially Resolved:**

| Item | Status | Notes |
|------|--------|-------|
| Server provisioning process | Divakar checking with IT | May be self-service; may need to procure. Awaiting confirmation. |
| Shared vs isolated infrastructure | Clear for DeepSight (use existing) | TBD for database and other non-AI infrastructure |
| Deployment pattern | Podman mentioned | Clarify with Srinivas if Docker is acceptable on Linux servers |

### 2.2 Airflow Environment

**Questions for Follow-up:**

2. Should we deploy our work to Cisco's existing Airflow instance, or stand up a separate instance for isolation?

3. Who is the Airflow SME we should coordinate with?

---

## Section 3: Cisco Team Contacts (Remaining Items)

### 3.1 Required SME Contacts

Several areas still need specific contacts identified:

| Area | Role Needed | Status |
|------|-------------|--------|
| **Developer Workflow** | Lead + IC | Not yet identified |
| **Repository & Code Standards** | Lead-level | Not yet identified |
| **Airflow / Orchestration** | SME | Another team - no name yet |
| **CAT / Gate Configuration** | SME | Not yet identified |
| **Observability / Grafana** | SME | Not yet identified |

*Note: Divakar covers Jenkins and infrastructure. Srinivas covers DeepSight/AI.*

**Questions for Follow-up:**

4. Can contacts be identified for the remaining SME areas above?

5. What is the expected availability of these contacts during discovery? (hours per week)

---

## Section 4: Technical Understanding (Not Yet Covered)

### 4.1 Developer Box (Item A)

**Questions for Follow-up:**

6. Can we schedule a walkthrough of the local development workflow? (developer writes code, runs tests, submits PR)

7. What testing frameworks are used locally? (pyATS, pytest, custom frameworks)

8. How standardized is the local dev environment across teams, or does it vary significantly?

9. What specific telemetry data would be most valuable? (test names, pass/fail, duration, coverage metrics)

10. What is the appetite for a lightweight agent on developer machines vs. alternative collection mechanisms? (CI hooks, IDE plugins, git hooks)

### 4.2 Branch Health / CD Health (Item F)

**Questions for Follow-up:**

11. What specific information do release leads need that they lack today?

12. Are there existing dashboards or reports for release leads, or is this capability net new?

13. What does "automated follow-up identification" look like in practice? (WebEx notifications, Jira tickets, email escalations)

14. What criteria distinguish actionable failures from noise that shouldn't trigger follow-up?

### 4.3 Internal Documentation

**Questions for Follow-up:**

15. Is there existing documentation on the 39 gates - what each gate checks, expected inputs/outputs, common failure modes?

16. Is there documentation on CDT (Context Driven Testing) architecture and how it integrates with the pipeline?

17. Are there internal developer standards or contribution guidelines we should review?

18. Where does this documentation live, and can we get access?

---

## Section 5: Scale & Metrics

We need baseline data to scope infrastructure and measure success. Do you have visibility into the current state for the following?

| Metric | What We Need |
|--------|--------------|
| **PR Volume** | Approximately how many PRs are submitted per day/week? |
| **Developer Count** | How many active developers submit PRs? |
| **Branch Count** | How many branches are actively maintained? |
| **Repository Scope** | How many repositories are in scope for this work? |
| **Merge Time** | Current average PR merge time (end-to-end) |
| **Failure Points** | Top 5 most common gate failure points |

---

## Section 6: Scope Boundaries (Remaining Items)

### 6.1 CDT Clarification

**Questions for Follow-up:**

19. What specific gaps exist in CDT's current coverage tracking?

20. Is condition-level coverage (vs. function-level) the primary gap, or is there something else?

---

## Section 7: Operational Considerations (Not Yet Covered)

### 7.1 Change Management

**Questions for Follow-up:**

21. Is there a Change Advisory Board (CAB) or approval process for deploying new tools to production pipelines?

22. What is the rollback process if our tooling causes issues?

### 7.2 Incident Management

**Questions for Follow-up:**

23. If our deployed tooling causes problems, who do we contact?

24. What is the incident management process we should be aware of?

---

## Summary: Remaining Open Items

| Category | Priority |
|----------|----------|
| **Infrastructure/Environment** | High |
| **SME Contacts** | High |
| **Technical Understanding (Item A & F)** | High |
| **Scale & Metrics** | Medium |
| **Scope/CDT** | Medium |
| **Operational** | Medium |

---

## Next Steps

| Action | Owner | Status |
|--------|-------|--------|
| Complete GitHub training (3-4 hours) | BayOne team | Pending |
| Provision ADS Linux machines | Divakar | Pending access |
| Watch DeepSight platform recording | Colin | In progress |
| Connect with Rui re: existing CICD app | Srinivas to facilitate | Pending |
| Check IT on server provisioning model | Divakar | Pending |
| Two-week check-in meeting | Anand + Colin | ~March 3, 2026 |
| Follow-up discovery session (remaining questions) | All | TBD |
