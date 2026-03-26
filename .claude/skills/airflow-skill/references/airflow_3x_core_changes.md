# Apache Airflow 3.x - Core Concepts and What's New

**Research Date:** 2026-01-29
**Airflow Version Coverage:** 3.0.0 - 3.1.6

---

## Executive Summary

Apache Airflow 3.0 was released in **April 2025** - the most significant release in Airflow's history.

**Latest Version:** Airflow 3.1.6 (released January 13, 2026)

**Key Statistics:**
- 26% of users already on Airflow 3 as of January 2026
- 84% currently preparing to upgrade
- Airflow 2.x reaches end-of-life in **April 2026**

---

## Major New Features in Airflow 3.0

### 1. Service-Oriented Architecture (AIP-72)

**Task Execution API** - Tasks no longer have direct database access:
- All state transitions go through a hardened API layer
- Better security posture
- Enables multi-language support (Python, Go, Java, R)

### 2. DAG Versioning (AIP-66)

The #1 most requested feature:
- DAGs versioned on every deployment
- Historical runs preserved with exact version
- Blue-green deployments without stopping workflows
- Complete audit trail

### 3. Edge Executor (AIP-69)

For distributed and edge-compute workflows:
- IoT data processing at the edge
- Hybrid cloud deployments
- Resource-limited environments

### 4. Event-Driven Scheduling

Datasets renamed to "Assets" with Watchers:
- React to external events (SQS, Kafka)
- True event-driven execution
- No more polling

### 5. Non-Data-Interval DAGs (AIP-83)

Critical for ML/AI workflows:
- ML inference without scheduling constraints
- Hyperparameter tuning workflows
- Multiple runs without time-based intervals

### 6. Redesigned React UI

Complete rewrite:
- React + FastAPI (replaced Flask-AppBuilder)
- Native dark mode
- Dramatically improved performance

### 7. Scheduler-Managed Backfills (AIP-78)

- Backfills managed by scheduler (not CLI)
- Native UI and REST API support
- Can pause, resume, track via UI

---

## Breaking Changes from Airflow 2.x

### Critical Changes

1. **Direct database access removed** - Tasks can't access metadata DB directly
2. **Scheduling behavior changed** - Default cron uses `CronTriggerTimetable`
3. **Context variables removed** - `tomorrow_ds`, `yesterday_ds`, `execution_date` gone
4. **SubDAGs removed** - Use TaskGroups or Assets instead
5. **Operators moved to Standard Provider** - Must install `apache-airflow-providers-standard`

### New Import Paths

```python
# Airflow 3.x - use airflow.sdk
from airflow.sdk import DAG, dag, task

# Operators from standard provider
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
```

### Migration Tool

```bash
# Check for breaking changes
ruff check --select AIR301,AIR302 dags/

# Auto-fix where possible
ruff check --fix --select AIR dags/
```

---

## Airflow 3.1 New Features

### Human-in-the-Loop (HITL)

Workflows can pause for human decisions:
- AI/ML workflows requiring human judgment
- Content moderation
- Approval processes

---

## Sources

- [Official Airflow Blog - Airflow 3.0 Release](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/)
- [Official Upgrade Guide](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html)
- [AWS Blog - Airflow 3 on MWAA](https://aws.amazon.com/blogs/big-data/introducing-apache-airflow-3-on-amazon-mwaa-new-features-and-capabilities/)
- [Astronomer Upgrade Guide](https://www.astronomer.io/docs/learn/airflow-upgrade-2-3)
