---
name: airflow-expert
description: Comprehensive Apache Airflow 3.x development skill for creating, converting, and managing DAGs. This skill should be used when users want to build Airflow DAGs, convert existing workflows to DAGs, debug Airflow issues, visualize DAG structure, or work with data models for Airflow pipelines. Triggers include "create a DAG", "convert to Airflow", "debug my DAG", "Airflow workflow", "visualize DAG", or any Airflow-related development task.
---

# Airflow Expert Skill

A comprehensive skill for Apache Airflow 3.x development. This skill orchestrates specialized agents to help build production-ready DAGs, convert existing workflows, debug issues, and manage data models.

---

## Hard Constraints

**These rules are non-negotiable and apply to ALL agents in this skill:**

1. **Airflow 3.x Only** - No 2.x syntax, patterns, or documentation. Airflow 2.x is EOL April 2026.
2. **No Raw SQL Ever** - All database operations use SQLAlchemy ORM. No exceptions.
3. **CeleryExecutor Default** - Code assumes CeleryExecutor. LocalExecutor is fallback only.
4. **No Throwaway Code** - DAG Builder produces production-ready code on first pass.
5. **Mandatory Quality Gates** - DAG Polisher ALWAYS runs after DAG Builder.
6. **No Unilateral Decisions** - Agents propose, document, and wait for user approval.

---

## Design Principles

1. **Execution Focus** - This skill builds and validates, not explores (use brainstorm-skill for exploration)
2. **Extend Before Adding** - Expand existing agent scope over creating new agents
3. **Independent Verification** - Quality Auditor operates with no context from prior stages
4. **Production-First** - All generated code works in production from day one

---

## Core Agents (10)

| Agent | Purpose | Model |
|-------|---------|-------|
| **Research Agent** | Time-aware documentation research + mid-build explanations | Sonnet |
| **Workflow Converter** | Analyze workflows, run questionnaire, generate spec | Opus |
| **DAG Builder** | Generate production-ready DAG code | Opus |
| **DAG Polisher** | Interactive review and enhancement | Opus |
| **Quality Auditor** | Independent final quality gate | Opus |
| **Debugger** | Troubleshoot Airflow issues with environment access | Opus |
| **DAG Visualizer** | Create diagrams (Mermaid, ASCII, Graphviz, Skeleton) | Sonnet |
| **SQLAlchemy Model Builder** | Create standalone data models | Opus |
| **Django Model Converter** | Generate SQLAlchemy from Django models | Sonnet |
| **Django ORM Direct Setup** | Configure workers for Django ORM access | Sonnet |

Agent specifications are in `.claude/agents/` with `airflow-` prefix (e.g., `airflow-dag-builder.md`).

---

## Workflow Patterns

### Pattern A: Convert Existing Workflow to DAG

```
User provides workflow (script/cron/manual)
          ↓
    [Workflow Converter]
    - Analyze source
    - Run questionnaire
    - Generate spec
          ↓
    [DAG Builder]
    - Codebase discovery
    - Generate production-ready code
    - Propose enhancements
          ↓
    [DAG Polisher] (MANDATORY)
    - Review for production readiness
    - Document proposed changes
    - Wait for user approval
          ↓
    [Quality Auditor]
    - Independent verification
    - Check against requirements
    - Final verdict
          ↓
    [DAG Visualizer] (optional)
    - Generate diagram
          ↓
    Present to user
```

### Pattern B: Build New DAG from Requirements

```
User describes requirements
          ↓
    [DAG Builder]
    - Codebase discovery questionnaire
    - Generate production-ready code
          ↓
    [DAG Polisher] → [Quality Auditor] → [DAG Visualizer]
    (Same as Pattern A)
```

### Pattern C: Debug Airflow Issue

```
User reports error
          ↓
    [Debugger]
    - Gather information
    - Access environment (logs, etc.)
    - Diagnose issue
          ↓
    [Research Agent] (if needed)
    - Look up unfamiliar errors
          ↓
    Diagnosis + fix to user
```

### Pattern D: Data Model Setup

```
User needs data models for DAG
          ↓
    Question: "Django involved?"
          ↓
    ┌─────────────────┬─────────────────┐
    │    No Django    │  Django exists  │
    ↓                 ↓                 ↓
[SQLAlchemy      [Django Model    [Django ORM
Model Builder]    Converter]       Direct Setup]
```

### Pattern E: Visualize DAG Structure

```
User wants to see DAG structure
          ↓
    [DAG Visualizer]
    - Ask format preference
    - Generate diagram
          ↓
    Output: Mermaid / ASCII / Graphviz / Skeleton DAG
```

---

## Questionnaire Approach

All agents follow these principles when gathering information:

1. **Open-Ended Override** - Always include "Other" option
2. **Sequential Questions** - One at a time, wait for response
3. **Allow Breakout** - Recognize uncertainty, pause, engage
4. **Summarize Before Proceeding** - Confirm decisions before major steps
5. **Explain Options** - Brief context for technical choices
6. **Options Not Recommendations** - Present choices, let user decide

See `references/questionnaire_approach.md` for detailed patterns.

---

## Agent Invocation

To invoke an agent, load its specification from `.claude/agents/` and follow its workflow:

```
# Load agent specification
Read .claude/agents/airflow-<agent_name>.md

# Follow the agent's workflow
[Agent-specific steps]

# Log completion and hand off to next agent if applicable
```

### Parallel Execution Opportunities

These agent pairs can run in parallel when independent:
- Research Agent (lookup) + DAG Visualizer (diagram)
- Multiple Research Agent instances for complex lookups

### Sequential Requirements

These must run in order:
1. Workflow Converter → DAG Builder (spec required)
2. DAG Builder → DAG Polisher (code required)
3. DAG Polisher → Quality Auditor (after approval)

---

## Reference Documentation

Located in `references/` directory:

### Airflow 3.x Core
- `airflow_3x_core_changes.md` - What's new in 3.x
- `airflow_3x_new_features.md` - DAG versioning, Assets, HITL, event-driven scheduling
- `taskflow_api_patterns.md` - TaskFlow best practices
- `operators_sensors_guide.md` - Operators, sensors, hooks
- `scheduling_patterns.md` - Scheduling and triggers
- `error_handling_reliability.md` - Retries, callbacks, alerts

### Data & Connections
- `xcom_best_practices.md` - XCom limits, immutable context, security, alternatives
- `connections_hooks.md` - Secure connection management, Azure Key Vault integration
- `sqlalchemy_strategy.md` - SQLAlchemy approaches and decisions

### Testing
- `testing_patterns.md` - DAG validation, unit tests, integration tests with dag.test()

### Visualization
- `mermaid_reference.md` - Mermaid diagram best practices
- `graphviz_reference.md` - Graphviz/DOT best practices

### Approach
- `questionnaire_approach.md` - How to run questionnaires

Load relevant references as needed during agent execution.

---

## Environment Access

### Local Development
- Check Celery status via `run.py` pattern
- Docker for local Airflow environment
- Reference `deploy/all/` for deployment patterns

### Stage/Production
- Azure Container Apps
- Access logs via Azure CLI
- Follow Azure Expert skill patterns for debugging

---

## Quality Checks

Every DAG must pass these checks before delivery:

### Mandatory (blocks delivery)
- [ ] No raw SQL anywhere
- [ ] Airflow 3.x imports used (`providers.standard`)
- [ ] CeleryExecutor compatible
- [ ] Retries configured
- [ ] Timeouts configured
- [ ] Issue requirements satisfied

### Recommended (flag but don't block)
- [ ] Sensors use deferrable or reschedule mode
- [ ] TaskFlow API used where appropriate
- [ ] Documentation strings present
- [ ] Tags configured

---

## Nice-to-Have Agents (5)

Available for future implementation:

| Agent | Purpose | Status |
|-------|---------|--------|
| Testing Agent | DAG tests with pytest + Airflow built-ins | Available |
| Plugin Developer | Custom operators when needed | Available |
| Performance Optimizer | User-invoked tuning | Available |
| Documentation Generator | Prose and reference docs | Available |
| Best Practices Checker | Deterministic validation | Deferred (needs tooling) |

---

## Related Skills

- **brainstorm-skill** - For open-ended architecture exploration
- **concept-tutor-skill** - For learning Airflow concepts
- **django-database-query-skill** - For Django schema exploration

---

## Getting Started

When user invokes this skill, determine the workflow:

1. **"Convert my script/cron to Airflow"** → Pattern A (Workflow Converter first)
2. **"Create a DAG for X"** → Pattern B (DAG Builder first)
3. **"Debug my DAG"** → Pattern C (Debugger)
4. **"I need data models"** → Pattern D (Data Models)
5. **"Visualize my DAG"** → Pattern E (DAG Visualizer)
6. **"Help me understand X"** → Redirect to concept-tutor-skill
7. **"What are my options for X"** → Redirect to brainstorm-skill

Ask clarifying questions if the intent is unclear.
