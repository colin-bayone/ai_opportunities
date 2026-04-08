# Q4 Deliverables

**Status:** Draft
**Last Updated:** 2026-02-02

---

## E – Self-Healing / Automated Corrective Actions

### Problem Being Solved

For failures that don't require human judgment, engineers still have to manually intervene to retry or fix. Srini stated: "If the user intervention is not required, technically the system should be able to correct itself and move on."

This is the most complex deliverable in the engagement. It involves building AI systems that take real actions autonomously in production environments, which requires careful governance, safety mechanisms, and clear boundaries.

---

### What Self-Healing Means (and Doesn't Mean)

**Self-Healing IS:**
- Automated retry for transient failures (e.g., network timeouts, flaky tests)
- Automated simple corrections for well-defined issues (e.g., copyright check failures, formatting issues)
- Actions taken within a defined governance framework
- Logged, auditable, and reversible where possible

**Self-Healing IS NOT:**
- AI making arbitrary code changes without human review
- Bypassing code review or approval processes
- Taking actions outside the defined governance boundaries
- A replacement for human judgment on complex issues

---

### Governance Framework

Before any automated actions can be implemented, a governance framework must be defined with Cisco. This includes:

1. **What types of failures can be auto-corrected?**
   - Transient/infrastructure failures (retry-safe)
   - Simple, well-defined fixes (copyright, formatting)
   - What's explicitly excluded?

2. **What actions can the system take?**
   - Retry a job
   - Apply a templated fix
   - Escalate to a human
   - What's explicitly forbidden?

3. **Who defines and approves the rules?**
   - Cisco engineering leadership
   - Release leads
   - How are rules updated over time?

4. **Audit and accountability**
   - All actions logged
   - Clear trail of what was done and why
   - Ability to review and adjust

**Note:** The governance framework definition is a collaborative effort with Cisco and must be completed before implementation begins.

---

### Tech Stack (TBD)

Agentic AI approach depends on Cisco preferences, model availability, and on-prem deployment constraints. Specific frameworks and models TBD with Cisco. On-prem deployment required.

Key technical considerations:
- Integration with Jenkins and Airflow for triggering actions
- Safety mechanisms to prevent runaway automation
- Rollback capabilities

---

### Deliverables

1. **Governance Framework Definition**
   - Collaborative effort with Cisco
   - Document what can/cannot be auto-corrected
   - Approval process for the framework
   - This must be completed before implementation

2. **Automated Action Triggers**
   - Integration with Jenkins and Airflow
   - Ability to trigger retries, apply fixes, or escalate
   - Respects governance boundaries

3. **Decision Logic**
   - AI-driven decision-making for which action to take
   - Based on failure type, history, and governance rules
   - Agentic AI Specialist leads this work

4. **Safety Mechanisms**
   - Limits on automated actions (e.g., max retries)
   - Circuit breakers to prevent cascading issues
   - Human escalation when confidence is low

5. **Rollback Capabilities**
   - Ability to undo automated actions where possible
   - Clear process for reverting if something goes wrong

6. **Audit and Visibility**
   - All actions logged with full context
   - Dashboard showing what actions were taken and why
   - Integration with unified interface from Q2

---

### What's NOT in Q4 for E

- Auto-correcting complex code issues (out of scope)
- Bypassing human review for significant changes
- Actions outside the governance framework

---

### Team Active in Q4

| Role | Focus |
|------|-------|
| Senior Engineer (Onshore) | Governance discussions with Cisco, architecture decisions |
| Backend/Integration Engineer | Triggers, Jenkins/Airflow integration |
| UI/Application Developer | Audit dashboard, visibility into actions |
| AI Engineer | Supporting agentic work, integration with diagnosis (B) |
| Agentic AI Specialist | Heavy focus - leads decision logic, safety mechanisms, governance implementation |

---

### Dependencies

- Q3 AI diagnosis (B) provides understanding of failures
- Q2 unified interface for surfacing actions and audit trail
- Governance framework agreement with Cisco (critical path)
- Access to Jenkins/Airflow for action triggers

---

### Risks

1. **Governance delays** – If Cisco can't agree on governance framework, implementation is blocked
2. **Scope creep** – "Self-healing" can mean many things; must keep boundaries tight
3. **Safety concerns** – Automated actions in production require extreme care
4. **Complexity** – This is the hardest deliverable; may extend into Year 2
5. **Trust** – Cisco needs to trust the system before enabling automated actions

---

### Milestone Summary

| Milestone | Target | Notes |
|-----------|--------|-------|
| Governance framework agreed | Early Q4 | Critical path - blocks implementation |
| Action trigger integration MVP | Mid Q4 | Basic retry capability |
| Decision logic MVP | Mid Q4 | Simple cases working |
| Safety mechanisms in place | Late Q4 | Before broader rollout |
| E feature complete (or scope defined for Year 2) | End of Q4 | May continue into Year 2 |

**Note for final deliverable:** Do not include week-level targets in the Cisco-facing document. Use percentage-based progress milestones instead to avoid over-committing to specific timelines.

---

### Timeline Considerations

E is unique among the deliverables because it requires organizational alignment beyond technical implementation. The governance framework involves policy decisions, stakeholder buy-in, and risk acceptance that extend beyond development work.

**Recommendation:** Begin governance conversations in Q2-Q3, in parallel with other work. This allows time for Cisco stakeholders to align on policy questions before technical implementation begins.

**Timeline Range:**

| Scenario | Governance | Technical | Completion | Notes |
|----------|------------|-----------|------------|-------|
| Optimistic | Q2-Q3 (parallel) | Q4 | End of Q4 | Governance agreed early, full Q4 for implementation |
| Realistic | Q3-Q4 | Q4 + Year 2 | Q1-Q2 Year 2 | Governance takes time, MVP in Q4, full scope Year 2 |
| Extended | Q4+ | Year 2 | Mid Year 2 | Governance requires extended alignment |

**What drives the timeline:**
- Speed of governance framework agreement (requires Cisco stakeholder alignment)
- Scope of automated actions Cisco wants to enable (key driver - see below)
- Safety and testing requirements Cisco defines
- Availability of Cisco engineering partners for integration

**Scope definition is critical:** The scope of automated actions that Cisco wants to enable is a key driver of the timeline. Cisco needs to establish the scope they are requiring for success in order to accurately estimate this deliverable. BayOne can propose our view on what's achievable and appropriate, but Cisco must accept and define the boundaries. Without a defined scope from Cisco, timeline estimates remain variable.

**Our commitment:** BayOne will be technically ready to implement in Q4. The Agentic AI Specialist joins early Q2 specifically to prepare for this work. We can support governance discussions as early as Cisco is ready to have them.

**Cisco's role:** Timely engagement on governance questions is critical to Q4 delivery. Delays in policy decisions will extend the timeline, as technical implementation cannot proceed without agreed boundaries.

This is framed not as a risk, but as a natural characteristic of work that involves organizational policy alongside technical development. Early and sustained engagement from Cisco leadership ensures the best outcome.
