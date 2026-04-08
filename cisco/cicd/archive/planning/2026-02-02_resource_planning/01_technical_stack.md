# Technical Stack Context

**Status:** Not final decisions, general preferences for hiring
**Last Updated:** 2026-02-02

---

## Cisco's Existing Stack

- **Orchestration:** Apache Airflow (longer-running jobs)
- **CI:** Jenkins (short/quick checks)
- **Gate Management:** CAT (Commit Approval Tool)
- **Analytics:** Grafana dashboards
- **Test Framework:** pyATS
- **Hosting:** On-prem deployment

---

## Our Technical Preferences

### Data Pipelines / Orchestration

- **Airflow only** - nothing else acceptable (Cisco already uses it)

### AI / LLM Integration

- **Preferred:** LangChain, LangGraph
- **Required:** Direct API integration experience
- **Avoid:** People who only know cloud-managed AI services (Azure AI, AWS Bedrock, GCP Vertex)
- **Reason:** Cisco deploys on-prem; need flexibility in hosting

### Backend

- **If needed:** FastAPI
- **Avoid:** Flask, Streamlit (too basic)
- **Primary language:** Python

### Front-end / Dashboards

- **Options:** React or Django + Bootstrap 5
- **Status:** Not decided yet, depends on Cisco
- **Note:** Front-end person not needed until end of Q1

---

## Hosting Consideration

Cisco deploys on-prem. This affects:
- How AI models are hosted/accessed
- Where services run
- Architecture decisions

Need to think through hosting carefully as we design solutions.
