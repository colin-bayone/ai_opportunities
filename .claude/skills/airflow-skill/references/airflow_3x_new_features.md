# Airflow 3.x New Features Overview

**Source:** Airflow 3.x Official Documentation, Nextlytics Analysis
**Last Updated:** 2026-01-30

---

## Overview

Airflow 3.x (3.0 released December 2024, 3.1 released 2025) introduces significant new features. This document covers the most impactful additions for DAG development.

**Note:** Airflow 2.x reaches End-of-Life April 2026. All new DAGs must target 3.x.

---

## Major New Features

### 1. DAG Versioning

DAG runs now track the exact version of code that executed them.

**Why It Matters:**
- Reproducibility: Know exactly what code ran
- Debugging: Compare code between runs
- Auditing: Track changes over time

**How It Works:**
```python
# Automatic - no code changes needed
# Each DAG run stores a hash of the DAG code at execution time

# View version in UI: DAG Runs > Select Run > Version Info
# Access programmatically:
dag_run.dag_version  # Hash of DAG code
```

**Benefits:**
- Roll back to previous DAG versions
- Compare behavior between versions
- Audit trail for compliance

---

### 2. Assets (formerly Datasets)

Data-aware scheduling based on data availability, not time.

**Renamed:** `Dataset` → `Asset` in Airflow 3.x

```python
from airflow.sdk import Asset, DAG, task

# Define assets (data dependencies)
raw_data = Asset("s3://bucket/raw/data.parquet")
processed_data = Asset("s3://bucket/processed/data.parquet")

# Producer DAG - declares what it produces
@dag(schedule="@daily", start_date=datetime(2026, 1, 1))
def producer_dag():

    @task(outlets=[raw_data])  # Declares output
    def extract():
        # Extract data to raw_data location
        pass

# Consumer DAG - schedules based on asset availability
@dag(schedule=[raw_data], start_date=datetime(2026, 1, 1))
def consumer_dag():

    @task(outlets=[processed_data])
    def transform():
        # Triggered when raw_data is updated
        pass
```

**Key Concepts:**
- **Outlets:** What a task produces
- **Inlets:** What a task consumes (for lineage)
- **Schedule:** DAG triggers when ALL listed assets update

**Multiple Asset Dependencies:**
```python
# Triggers when BOTH assets are updated
@dag(schedule=[asset_a, asset_b])
def dependent_dag():
    pass

# Conditional with AssetAlias
from airflow.sdk import AssetAlias

# Triggers when ANY asset matching pattern updates
any_sales = AssetAlias("s3://bucket/sales/*")

@dag(schedule=[any_sales])
def sales_processor():
    pass
```

---

### 3. Asset Watchers

Monitor external systems and trigger DAGs based on external events.

```python
from airflow.sdk import Asset, AssetWatcher
from airflow.providers.amazon.aws.triggers.s3 import S3KeyTrigger

# Define asset with watcher
s3_file = Asset(
    uri="s3://bucket/incoming/",
    watchers=[
        AssetWatcher(
            name="s3_file_watcher",
            trigger=S3KeyTrigger(
                bucket_name="bucket",
                bucket_key="incoming/*.csv",
                aws_conn_id="my_aws"
            )
        )
    ]
)

# DAG triggers when new file appears
@dag(schedule=[s3_file])
def file_processor():
    @task
    def process_new_file():
        pass
```

**Supported Watchers:**
- S3 file arrival
- GCS file arrival
- Azure Blob events
- Custom triggers

---

### 4. Event-Driven Scheduling

React to events instead of polling.

```python
from airflow.sdk import dag, task
from airflow.providers.http.triggers.http import HttpTrigger

@dag(schedule="@once")
def event_driven_dag():

    @task.sensor(
        trigger=HttpTrigger(
            http_conn_id="webhook",
            endpoint="/events",
            method="GET"
        ),
        mode="deferrable"
    )
    def wait_for_event():
        """Wait for external event without holding worker."""
        pass

    @task
    def process_event():
        pass

    wait_for_event() >> process_event()
```

---

### 5. Human-in-the-Loop (HITL)

Pause workflows for human approval.

```python
from airflow.sdk import dag, task
from airflow.operators.python import get_current_context

@dag(schedule="@daily")
def approval_workflow():

    @task
    def prepare_report():
        return {"report_url": "https://..."}

    @task.approval(
        approvers=["manager@company.com"],
        timeout=timedelta(hours=24)
    )
    def await_approval(report):
        """Pauses for human approval."""
        return report

    @task
    def publish_report(approved_report):
        # Only runs after approval
        pass

    report = prepare_report()
    approved = await_approval(report)
    publish_report(approved)
```

**Approval Options:**
- Email notifications to approvers
- Slack integration
- Custom approval hooks
- Timeout handling

---

### 6. Improved Backfill

First-class backfill operations with better control.

```bash
# New backfill command
airflow dags backfill \
  --dag-id my_dag \
  --start-date 2026-01-01 \
  --end-date 2026-01-15 \
  --reset-dagruns  # Clear existing runs
  --rerun-failed-tasks  # Only rerun failures
```

**Programmatic Backfill:**
```python
from airflow.api.client.local_client import Client

client = Client(None, None)
client.trigger_dag(
    dag_id='my_dag',
    run_id='backfill_2026-01-01',
    execution_date=datetime(2026, 1, 1),
    conf={'backfill': True}
)
```

---

### 7. Task SDK

Modern task development with improved typing and testing.

```python
from airflow.sdk import task, dag
from airflow.sdk.types import Context
from typing import TypedDict

class ExtractOutput(TypedDict):
    records: list[dict]
    count: int

@dag(schedule="@daily", start_date=datetime(2026, 1, 1))
def typed_dag():

    @task
    def extract() -> ExtractOutput:
        """Typed return value."""
        records = [{"id": 1}, {"id": 2}]
        return {"records": records, "count": len(records)}

    @task
    def transform(data: ExtractOutput) -> list[dict]:
        """Typed input parameter."""
        return [{"id": r["id"], "processed": True} for r in data["records"]]

    data = extract()
    transform(data)
```

**Benefits:**
- Better IDE support
- Runtime type validation (optional)
- Clearer documentation

---

### 8. OpenTelemetry Support

Native observability integration.

```python
# airflow.cfg
[metrics]
otel_on = True
otel_host = otel-collector.monitoring.svc
otel_port = 4317
otel_ssl_active = True

[traces]
otel_on = True
otel_host = otel-collector.monitoring.svc
otel_port = 4317
```

**What's Traced:**
- DAG parsing
- Task execution
- XCom operations
- Database queries
- External hook calls

**Integration:**
- Jaeger
- Zipkin
- Azure Monitor
- Datadog
- New Relic

---

### 9. Breaking Changes Summary

| Feature | Airflow 2.x | Airflow 3.x |
|---------|-------------|-------------|
| Context modification | Allowed | **Immutable** |
| Dataset | `Dataset` | `Asset` |
| Import paths | `airflow.operators.*` | `airflow.providers.standard.*` |
| XCom defaults | Pickling allowed | **JSON only** |
| Python | 3.8+ | **3.9+** |

---

### 10. Migration Checklist

When migrating from 2.x to 3.x:

1. [ ] Update imports to `airflow.providers.standard`
2. [ ] Replace `Dataset` with `Asset`
3. [ ] Remove context modifications
4. [ ] Verify XCom data is JSON-serializable
5. [ ] Update Python to 3.9+
6. [ ] Test all DAGs with `dag.test()`
7. [ ] Update provider packages to 3.x compatible versions

---

## Feature Availability Matrix

| Feature | 3.0 | 3.1 |
|---------|-----|-----|
| DAG Versioning | ✅ | ✅ |
| Assets (Datasets) | ✅ | ✅ |
| Asset Watchers | ❌ | ✅ |
| Event-Driven | Partial | ✅ |
| HITL | ❌ | ✅ |
| Improved Backfill | ✅ | ✅ |
| Task SDK | ✅ | ✅ |
| OpenTelemetry | ✅ | ✅ |

---

## When to Use New Features

### Use Assets When:
- DAGs depend on data availability, not time
- Multiple DAGs share data dependencies
- You need data lineage tracking

### Use Asset Watchers When:
- External systems push data (S3, Azure Blob)
- You want to avoid polling
- Real-time processing requirements

### Use HITL When:
- Workflows need approval gates
- Compliance requires sign-off
- High-risk operations need review

### Use OpenTelemetry When:
- Operating at scale
- Debugging performance issues
- Integration with existing observability

---

## Quality Auditor Checks

The Quality Auditor verifies:

1. [ ] No deprecated 2.x patterns
2. [ ] Assets used instead of Dataset
3. [ ] Context not modified
4. [ ] Provider imports from correct paths
5. [ ] Python 3.9+ compatible
