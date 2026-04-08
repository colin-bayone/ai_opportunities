# Cisco Project Context for Recruiting

## Technical Environment

### Confirmed Stack
| Category | Technology |
|----------|------------|
| **Orchestration** | Apache Airflow, Jenkins |
| **Build System** | Bazel (plus Make, Gradle compatibility) |
| **Code Management** | GitHub with custom integration tools |
| **Database** | PostgreSQL with pgvector |
| **Monitoring** | Grafana dashboards |
| **Programming** | Python-heavy |
| **Deployment** | On-premises only (no cloud AI services) |
| **LLM APIs** | Claude API, OpenAI API (external calls, not self-hosted) |

### Cisco-Specific Tools
- **CAT** (Commit Approval Tool) - manages gate enablement per branch
- **CDT** (Context Driven Testing) - 2+ years live, function-to-test-case mapping
- **pyATS** - Cisco's test automation framework with custom NX-OS libraries
- **DevX** - developer platform

### Scale
- 39+ validation gates before merge
- Multiple developers, repositories, branches
- NX-OS (network operating system) with multi-stage pipeline

---

## The 6 Capability Areas

| Priority | Area | Problem | Solution |
|----------|------|---------|----------|
| **A** | Developer Box | Black box, no tracking of local testing | Telemetry, coverage tracking, AI-assisted debugging |
| **B** | Gate Failures (CI) | Manual root cause investigation | AI diagnosis engine: logs → root cause → suggested fixes |
| **C** | Cross-Pipeline Visibility | Status fragmented across tools | Unified chat interface ("Where is my PR?"), single dashboard |
| **D** | Coverage Confirmation | CDT gaps, incomplete coverage tracking | Condition-level coverage for PRs |
| **E** | Self-Healing | Manual intervention for failed jobs | Autonomous corrective actions with governance (DEFERRED) |
| **F** | Branch Health / CD Health | Release leads lack visibility post-merge | Dashboards, failure attribution, automated follow-up |

**Current Priorities**: A (Developer Box) and F (Branch Health)
**Target Metric**: 20-30% reduction in average PR merge time

---

## Role Differentiation

### Senior AI Solutions Engineer (On-site San Jose)
- **Split**: 60% AI development, 25% client interface, 15% collaboration
- **Core Value**: Prototype-to-production owner; architect + client liaison
- **Unique**: Direct client demos, stakeholder engagement, enterprise navigation
- **Client-Facing**: YES - day-to-day technical interface

### Automation Engineer (On-site San Jose)
- **Split**: 60% CI/CD integration, 20% backend, 15% client interface
- **Core Value**: Systems integrator; owns data pipelines and backend
- **Unique**: Airflow DAGs, Jenkins APIs, data pipeline development
- **Client-Facing**: YES - works with CI/CD and DevOps teams

### AI Engineer (Remote Offshore)
- **Split**: 65% AI features, 20% dashboard/UI, 15% collaboration
- **Core Value**: Feature implementer; chat interfaces and dashboards
- **Unique**: Frontend development (React/Vue), LangChain pipelines
- **Client-Facing**: NO - works under Senior AI Solutions Engineer

### Agentic AI Engineer (Remote Offshore)
- **Split**: 45% autonomous system design, 35% agent development, 20% collaboration
- **Core Value**: Autonomous systems specialist; governance and safety
- **Unique**: Tool-calling, circuit breakers, human-in-the-loop, audit logging
- **Client-Facing**: NO - works under Technical Lead

---

## Constraints That Affect Hiring

### On-Prem Reality
- No cloud AI service dependencies
- Security constraints, access management complexity
- Incomplete documentation common
- Complex approval processes

### What This Means for Candidates
- Must have production systems experience (not research)
- Comfortable navigating enterprise bureaucracy
- Proven patterns over novel approaches
- Safety mechanisms matter
- Offshore engineers need strong self-direction
- Can't rely on cloud sandbox for testing

---

## Success Criteria by Role

### All Roles
- Proactive with incomplete information
- Strong written communication
- AI pair programming proficiency (Claude Code, Cursor, Copilot)
- Self-directed
- Detail-oriented
- Comfortable debugging with limited documentation

### Senior AI Solutions Engineer
- Delivers production AI, not demos
- Earns trust through reliable delivery
- Translates client needs to specs
- Navigates enterprise processes
- Mentors offshore team
- Understands LLM failure modes

### Automation Engineer
- Builds integrations that "just work"
- Deep CI/CD understanding
- Comfortable with data pipeline complexity
- Designs for failure (retry, idempotency, observability)
- Bridges AI engineers' needs with CI/CD constraints

### AI Engineer (Offshore)
- Production-ready on first try (limited feedback loops)
- Comprehensive test coverage for non-deterministic AI
- Self-documents work clearly
- Builds usable chat interfaces and dashboards
- Proactive communicator

### Agentic AI Engineer (Offshore)
- Designs safe autonomous systems
- Thinks deeply about failure modes
- SRE/operations mindset
- Safety mechanisms built in (not bolted on)
- Compliance/audit-aware
- Explains governance decisions clearly
