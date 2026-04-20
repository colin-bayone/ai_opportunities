# 03 - Discussion: Infrastructure and Production Architecture

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-14 (Pre-proposal strategy discussion)
**Document Set:** 03 (Working Discussion)
**Pass:** Colin's direction on production infrastructure, Azure hosting, and cost management

---

## Docker: Development vs. Production

Docker containers are for development and isolated testing environments. In production, the platform runs on **Azure Container Apps**. All resources live on Azure.

### Production Stack on Azure

| Component | Azure Service | Notes |
|-----------|--------------|-------|
| Application hosting | Azure Container Apps | Containers with specific compute allocated based on usage, scale up/down automatically |
| Model hosting | Azure AI Foundry | LLM inference, visual understanding models |
| Database | Azure Postgres | Default recommendation, but flexible to use whatever databases Sephora prefers (including on-prem, other cloud, or other database engines) |
| Caching | Azure Hosted Redis | Available if needed for performance, session management, or job queuing |

### Cost Management

Colin emphasized that the Azure Container Apps model is inherently cost-efficient:
- Containers have **specific compute allocated based on usage**, not fixed provisioning
- Containers **scale up or down** automatically based on demand (flexible server)
- The result is **always the best cost for the actual usage**, not paying for idle capacity
- **Pay-by-usage** model across the infrastructure

This is a significant selling point: the platform does not require Sephora to commit to large fixed infrastructure costs. It scales with actual usage, which aligns well with the progressive buildout approach (start small, scale as consumer groups are onboarded).

### Scalability

Colin stated this is "100% production grade." The architecture is not a prototype or development-only system that would need to be rebuilt for production. It is designed to scale from initial deployment through full organizational adoption across all four consumer groups.

## Database Flexibility

Azure Postgres is the default recommendation, but BayOne is flexible on databases. If Sephora has existing database infrastructure (on-prem, different cloud, different engine), BayOne will work with whatever they prefer. This is consistent with the overall philosophy: build with what the client needs, do not force a stack.

## Open WebUI Assistance

Colin noted that BayOne could also help Sephora with their Open WebUI equivalent project if they want involvement there. BayOne has experience building similar systems internally. This is an additional service offering, completely separate from the visual QA platform, but worth mentioning as a demonstration of breadth and willingness to help across their AI initiatives.

---

*This is a blockchain-style document. It will not be edited after creation.*
