# Cisco CI/CD Engagement: Resourcing and Role Boundaries

Internal note for BayOne team.

---

## Scope Observations

The discovery call surfaced six distinct potential deliverables (see Potential Scope Items document):

1. Developer Box Instrumentation
2. Unified Data Layer / Chat Interface
3. AI Diagnosis for Gate Failures
4. Coverage Tracking Enhancement
5. Self-Healing / Auto-Resume
6. Branch Health / CD Visibility

Each of these represents a meaningful body of work with its own complexity, dependencies, and integration requirements. Delivering all of them simultaneously would require a larger team; delivering them sequentially would require a phased approach with clear prioritization from Cisco.

**Key question for Cisco:** What is the timeline for an MVP, and which capabilities are required for that MVP to be considered successful? Without this, we cannot determine whether to propose phases or parallel workstreams.

---

## Role Boundaries: AI vs. Platform/Integration

There are two distinct categories of work embedded in this engagement:

### AI Work
- Conversational interface design and implementation (chat for PR status queries)
- Failure diagnosis and root cause analysis using LLMs
- Suggested code fixes and recommendations
- Self-healing logic and decision-making for automated actions
- Persona-based intelligence (developer vs. release lead views)

### Platform / Integration Work
- Data collection from Developer Box (instrumentation, agents, telemetry pipelines)
- API integration with CAT, DevX, Jenkins, Airflow, Grafana
- Data normalization across different schemas and systems
- Building the unified data layer that AI capabilities depend on
- Infrastructure setup, deployment, and ongoing maintenance

**These are codependent.** The AI work cannot proceed without the platform/integration work being in place first. The unified data layer is foundational—without access to the data, there is nothing for the AI to analyze or act upon.

---

## Resourcing Implications

BayOne does not currently have a team staffed and available to execute this work. We will need to source appropriate resources immediately.

Given the scope and codependencies:

- **If Cisco wants rapid delivery:** We would need to staff both platform/integration and AI roles in parallel. This is a larger team with higher cost.

- **If Cisco prefers a phased approach:** We could start with platform/integration work (data layer, instrumentation) and add AI resources once the foundation is ready. This extends the timeline but reduces initial team size.

The right approach depends on Cisco's MVP definition and timeline, which we have asked them to clarify.

---

## Recommendation

Before we can provide an estimate or staff this engagement, we need:

1. Cisco's MVP definition and timeline
2. Clarity on which deliverables are in scope for the first phase
3. Answers to the technical and infrastructure questions (APIs, hosting, AI model constraints)
4. A "day in the life" session to understand the actual developer and release lead workflows

Without these, any estimate would be speculative and carry significant risk of being inaccurate.
