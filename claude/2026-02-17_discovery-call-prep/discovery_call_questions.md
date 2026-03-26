# Discovery Session: NX-OS CI/CD Pipeline Improvement
**Prepared by:** BayOne Solutions
**For:** Cisco (Anand, Srinivas, Divakar)
**Date:** February 17, 2026
**Purpose:** First technical discovery session for Phase 1 (Items A + F)

---

## Context

On January 16, 2026, Cisco selected **Item A (Developer Box)** and **Item F (Branch Health/ CD Health)** as Phase 1 priorities. This document outlines what we need to understand and what we need from Cisco to begin meaningful work.

**Cisco Q3 began January 26, 2026.** To ensure delivery aligns with Cisco's fiscal calendar, we propose that the engagement timeline begin on the date we have meaningful access to systems and designated Cisco contacts. This allows us to commit to realistic deliverables without timeline slippage due to onboarding delays.

---

## Section 1: Access Requirements

For BayOne to begin discovery and development work, we need Cisco to provide the following. Each item requires a Cisco owner who can drive it to completion.

### 1.1 System Access

| System | What We Need | Cisco Owner |
|--------|--------------|-------------|
| **Jenkins** | Read access to job configurations, build logs, and historical data | TBD |
| **Apache Airflow** | Read access to DAGs, task logs, and execution history | TBD |
| **CAT (Commit Approval Tool)** | Access to view gate configurations and branch settings | TBD |
| **DevX Platform** | Access to PR metadata and pipeline status | TBD |
| **Grafana** | Access to existing dashboards and underlying data sources | TBD |
| **GitHub Enterprise** | Read access to relevant repositories | TBD |
| **Issue Tracking** | Access to pipeline-related tickets and escalation workflows (if applicable) | TBD |

**Questions for Cisco:**
1. Is there an internal ticketing system (ServiceNow, Jira, etc.) we should use to request access? If so, who can grant us access to that system and guide us through the process?
2. Who is the single point of contact responsible for ensuring BayOne team members receive access?
3. What is the typical turnaround time for access provisioning?

### 1.2 Network Access

We understand Cisco's infrastructure is on-premises, including GitHub Enterprise.

**Questions for Cisco:**
4. What is the network access model for external contractors? (VPN credentials, IP whitelisting, etc.)
5. Who initiates the network access process, and what information do you need from us to start it?
6. Are there different access tiers for onshore vs. offshore team members?

### 1.3 Background Checks

We understand background checks are required for this engagement.

**Questions for Cisco:**
7. Who initiates the background check process - does Cisco send us forms, or do we need to contact someone specific?
8. Can we begin non-sensitive discovery work (documentation review, architecture discussions) while background checks are in progress?

### 1.4 Development Environment

For Item A (Developer Box), we need to understand how BayOne engineers will test instrumentation.

**Questions for Cisco:**
9. Will BayOne developers receive Cisco-managed machines, or use their own with VPN access?
10. How can we test developer-side tooling if we don't have the same local environment as Cisco engineers?
11. Is there a staging or dev environment for CI/CD tooling where we can safely test changes before production?

---

## Section 2: Infrastructure & Deployment Environment

Cisco previously asked us "what servers do you need" - to answer that, we need to understand the on-prem deployment environment.

### 2.1 Compute & Database Infrastructure

**Questions for Cisco:**
12. What is the process for provisioning on-prem servers for this project? Do we spec requirements and Cisco provisions, or is there a self-service model?
13. What database options are available on-prem? (PostgreSQL, MySQL, Oracle, etc.)
14. Are there existing shared services we should leverage, or should we plan for isolated infrastructure for this project?
15. Is there a preferred deployment pattern? (containers, VMs, bare metal)

### 2.2 Data Infrastructure

**Questions for Cisco:**
16. Where does raw pipeline data currently live? (data warehouse, direct database, Prometheus TSDB, etc.)
17. What is the logging stack? (ELK, Splunk, Graylog, etc.)
18. What are the data retention policies - how far back can historical analysis go?

### 2.3 Airflow Environment

**Questions for Cisco:**
19. Should we deploy our work to Cisco's existing Airflow instance, or stand up a separate instance for isolation?
20. If using the existing Airflow instance, who is the Airflow SME we should coordinate with?
21. What version of Airflow is currently deployed?

### 2.4 AI & LLM Infrastructure

We understand Cisco will provide enterprise AI API keys (OpenAI, Anthropic, or similar) for this engagement.

**Questions for Cisco:**
22. What AI/LLM services are available to us? (specific providers, model versions)
23. Are there restrictions on what data we can send to these APIs? (code snippets, log data, error messages)
24. Are there rate limits or cost considerations we should design around?
25. Is there an internal AI platform team we should coordinate with?

---

## Section 3: Cisco Team Contacts

We need designated contacts in several areas to ensure we can move forward without bottlenecks.

### 3.1 Required SME Contacts

| Area | Role Needed | Why | Cisco Contact |
|------|-------------|-----|---------------|
| **Developer Workflow** | Lead + IC | Understand day-to-day developer experience, local testing practices, pain points | TBD |
| **Repository & Code Standards** | Lead-level | Understand code review process, contribution guidelines, PR standards | TBD |
| **Deployment / Builds** | SME | Understand official build process, release management, CD pipeline (the "Red Box" in pipeline diagrams) | TBD |
| **Airflow / Orchestration** | SME | Understand DAG patterns, job dependencies, operational practices | TBD |
| **CAT / Gate Configuration** | SME | Understand gate logic, branch policies, approval workflows | TBD |
| **Observability / Grafana** | SME | Understand existing dashboards, data sources, metric schemas for Branch Health work | TBD |
| **Infrastructure / DevOps** | SME | Coordinate server provisioning, network access, deployment | TBD |

**Questions for Cisco:**
26. Can you identify contacts for each of these areas before or during this session?
27. What is the expected availability of these contacts during discovery? (hours per week)
28. Is there a single discovery coordinator on Cisco's side who can help us navigate to the right people?

---

## Section 4: Technical Understanding

### 4.1 Developer Box (Item A)

We need to understand the current state before designing instrumentation.

**Questions for Cisco:**
29. Can we schedule a walkthrough of the local development workflow? (developer writes code, runs tests, submits PR)
30. What testing frameworks are used locally? (pyATS, pytest, custom frameworks)
31. How standardized is the local dev environment across teams, or does it vary significantly?
32. What specific telemetry data would be most valuable? (test names, pass/fail, duration, coverage metrics)
33. What is the appetite for a lightweight agent on developer machines vs. alternative collection mechanisms? (CI hooks, IDE plugins, git hooks)

### 4.2 Branch Health / CD Health (Item F)

**Questions for Cisco:**
34. What specific information do release leads need that they lack today?
35. Are there existing dashboards or reports for release leads, or is this capability net new?
36. What does "automated follow-up identification" look like in practice? (WebEx notifications, Jira tickets, email escalations)
37. What criteria distinguish actionable failures from noise that shouldn't trigger follow-up?

### 4.3 Internal Documentation

**Questions for Cisco:**
38. Is there existing documentation on the 39 gates - what each gate checks, expected inputs/outputs, common failure modes?
39. Is there documentation on CDT (Context Driven Testing) architecture and how it integrates with the pipeline?
40. Are there internal developer standards or contribution guidelines we should review?
41. Where does this documentation live, and can we get access?

---

## Section 5: Scale & Metrics

We need baseline data to size our solution and measure success.

**Questions for Cisco:**
42. Approximately how many PRs are submitted per day/week?
43. How many active developers submit PRs?
44. How many branches are actively maintained?
45. How many repositories are in scope for this work?
46. What is the current average PR merge time (end-to-end)?
47. What are the top 5 most common gate failure points?
48. Can we query this data from existing sources (Grafana, databases), or does new instrumentation need to be built?

---

## Section 6: Scope Boundaries

### 6.1 Internal AI Code Review Project

We understand Cisco has an internal AI code review project going live soon.

**Questions for Cisco:**
49. What is the scope of that project, and where does it overlap with Items A-F?
50. Should our work integrate with that project, extend it, or remain separate?
51. Who owns that project, and should we coordinate with them?

### 6.2 CDT Clarification

CDT was described as "already solved" but also noted as having gaps.

**Questions for Cisco:**
52. What specific gaps exist in CDT's current coverage tracking?
53. Is condition-level coverage (vs. function-level) the primary gap, or is there something else?

---

## Section 7: Operational Considerations

### 7.1 Change Management

**Questions for Cisco:**
54. Is there a Change Advisory Board (CAB) or approval process for deploying new tools to production pipelines?
55. What is the rollback process if our tooling causes issues?

### 7.2 Incident Management

**Questions for Cisco:**
56. If our deployed tooling causes problems, who do we contact?
57. What is the incident management process we should be aware of?

---

## Section 8: Working Rhythm & Reporting

**Questions for Cisco:**
58. What are Cisco's expectations for progress reporting? (weekly status, bi-weekly demos, ad-hoc updates)
59. What format works best? (written updates, slide decks, live demos)
60. Who should receive status updates, and who has authority to approve direction changes?
61. If helpful, we can propose a reporting cadence - would that be useful?
62. What channel should BayOne use for day-to-day technical questions? (WebEx space, email distribution list, etc.)

---

## Section 9: Timeline Alignment

**Current State:**
- Cisco Q3: January 26, 2026 - present
- BayOne onboarding status: In progress (access and contacts pending)

**Proposal:**
We recommend defining the engagement start date as the date we have:
1. System access provisioned (at minimum: Jenkins, Airflow, Grafana, GitHub)
2. Designated Cisco SME contacts identified and available
3. Background check clearance (or approval to begin non-sensitive work)

This ensures our delivery commitments are realistic and tied to actual working time rather than calendar time. If there are concerns about Q3 delivery targets, we should discuss scope adjustments or phasing now.

**Questions for Cisco:**
63. What are Cisco's delivery expectations for Q3?
64. Given current onboarding status, is there flexibility on timeline, or should we adjust scope to fit available time?
65. What is the realistic target date for BayOne to have meaningful access?

---

## Summary: What We Need From Cisco

| Category | Items Needed | Priority |
|----------|--------------|----------|
| **Access** | System access to Jenkins, Airflow, CAT, DevX, Grafana, GitHub Enterprise | Blocking |
| **Access** | Network/VPN access for BayOne team | Blocking |
| **Access** | Background check initiation | Blocking |
| **Contacts** | Single discovery coordinator | High |
| **Contacts** | SMEs for Developer, Repo, Deployment, Airflow, CAT, Grafana, Infrastructure | High |
| **Infrastructure** | Clarity on server provisioning process | High |
| **Infrastructure** | AI/LLM service availability and restrictions | High |
| **Infrastructure** | Data infrastructure details (logging stack, retention) | High |
| **Environment** | Staging/dev environment for testing our tooling | High |
| **Documentation** | Access to internal docs on gates, CDT, developer standards | Medium |
| **Metrics** | Baseline data on PR volume, merge times, failure rates | Medium |
| **Clarity** | Boundary with internal AI code review project | Medium |
| **Operational** | Change management and incident escalation processes | Medium |
| **Timeline** | Agreed start date tied to access provisioning | High |

---

## Appendix: Items Not Covered Here

The following topics are important but are not the focus of this discovery session:

- **Budget and contracting** - Separate track with Rahul/Zahra
- **Detailed API specifications** - Requires system access first
- **Feature designs** - Discovery informs design; premature to discuss now
- **Items B, C, D, E** - Deferred to future phases per January 16 decision

---

## Next Steps (To Confirm)

| Action | Owner | Target Date |
|--------|-------|-------------|
| Identify Cisco discovery coordinator | Cisco | TBD |
| Initiate access provisioning | Cisco | TBD |
| Initiate background check process | Cisco | TBD |
| Provide SME contact list | Cisco | TBD |
| Schedule developer workflow walkthrough | Cisco + BayOne | TBD |
| Confirm AI/LLM service availability | Cisco | TBD |
| Confirm staging environment availability | Cisco | TBD |
| Agree on engagement start date | Cisco + BayOne | TBD |
