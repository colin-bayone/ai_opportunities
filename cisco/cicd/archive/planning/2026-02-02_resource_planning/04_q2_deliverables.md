# Q2 Deliverables

**Status:** Draft
**Last Updated:** 2026-02-02

---

## C – Unified Interface / Cross-Pipeline Visibility

### Problem Being Solved

Information is scattered across multiple systems with no unified view. Engineers submit PRs and have no easy way to monitor progress. They cannot ask one system a single question and get a complete answer. There is no chat or conversational interface to query pipeline status.

Srini described the current state: "We have one CAT tool... then we have a DevX platform that has some DB... and we have these Jenkins and Airflows that are running in silos."

The desired state: A developer pushing 5 bug fixes on different branches has a single view showing status across all of them, and can ask natural language questions like "Where is my PR?" or "Why did this fail?"

---

### Systems to Integrate

This deliverable requires integration with multiple Cisco systems, each with its own APIs, data schemas, and access patterns:

| System | Purpose | Integration Scope |
|--------|---------|-------------------|
| **CAT (Commit Approval Tool)** | Manages which gates are enabled per branch | Read gate configurations, status |
| **DevX Platform** | Internal developer platform with its own database | Query PR metadata, status |
| **Jenkins** | Runs short/quick CI checks | Read job status, logs, results |
| **Apache Airflow** | Runs longer-running jobs | Read DAG status, task results, logs |
| **Grafana** | Analytics on gate performance, PR times | Read metrics, dashboards data |
| **GitHub** | Source control, PR information | Read PR status, metadata |

Each integration requires:
- Understanding the API or data access method
- Handling authentication and access
- Normalizing data into a common schema
- Handling errors, timeouts, and edge cases

---

### Tech Stack (TBD)

Final platform decisions depend on Cisco preferences and deployment constraints. Options include:

- **Backend:** FastAPI or Django for API layer and data normalization
- **Frontend:** React or Django templates for unified interface
- **Chat/NLP:** AI/LLM framework for natural language query handling (specific framework TBD)
- **Hosting:** On-prem deployment required; specifics TBD with Cisco

---

### Deliverables

1. **API Integration Layer**
   - Connections to all relevant Cisco systems (CAT, DevX, Jenkins, Airflow, Grafana, GitHub)
   - Unified authentication/access handling
   - Data normalization across different schemas
   - This is substantial backend work spanning multiple systems with different APIs

2. **Unified Data Layer**
   - Consolidated view of PR status from all sources
   - Common data model that abstracts underlying system differences
   - Foundation for both the UI and the chat interface

3. **Single Pane of Glass Interface**
   - Web interface showing consolidated PR status
   - Developer can see all their PRs across branches in one place
   - Status, blockers, and next actions surfaced clearly

4. **Chat Interface**
   - Natural language query capability
   - "Where is my PR?" / "Why did gate X fail?" / "What PRs are blocked?"
   - Requires NLP/AI to understand queries and route to appropriate data
   - Responses synthesized from unified data layer

---

### What's NOT in Q2

- AI-driven failure diagnosis with root cause analysis (that's B, Q3)
- Suggested code fixes (that's B, Q3)
- Self-healing / automated corrective actions (that's E, Q4)

---

### Team Active in Q2

| Role | Focus |
|------|-------|
| Senior Engineer (Onshore) | Coordination with Cisco teams, API access, architecture decisions |
| Backend/Integration Engineer | Heavy API integration work, Airflow integration, data normalization |
| UI/Application Developer | Unified interface UI, chat interface frontend |
| AI Engineer | NLP for chat interface, query understanding, response generation |
| Agentic AI Specialist | Joins early Q2, learns systems, supports AI work, prepares for E |

---

### Dependencies

- Q1 Discovery and A+F work provides understanding of Cisco systems
- API access and documentation for all systems (quality varies; may require Cisco assistance)
- Cisco decisions on tech stack and hosting

---

### Risks

1. **API documentation quality** – If APIs are poorly documented or require custom work, timeline extends
2. **Access to all systems** – May require separate access grants for each system
3. **Data inconsistencies** – Different systems may have conflicting or incomplete data
4. **Chat interface scope** – Easy to over-scope; need to define what queries are supported

---

### Milestone Summary

| Milestone | Target | Notes |
|-----------|--------|-------|
| All system APIs accessible | Week 2 of Q2 | Dependency on Cisco |
| Integration layer MVP (2-3 systems) | Week 5 of Q2 | Prove the pattern works |
| Full integration layer | Week 9 of Q2 | All systems connected |
| Unified interface MVP | Week 10 of Q2 | Basic UI working |
| Chat interface MVP | Week 12 of Q2 | Basic queries working |
| C feature complete | End of Q2 | Polish and handoff |

**Note for final deliverable:** Do not include week-level targets in the Cisco-facing document. Use percentage-based progress milestones instead to avoid over-committing to specific timelines.
