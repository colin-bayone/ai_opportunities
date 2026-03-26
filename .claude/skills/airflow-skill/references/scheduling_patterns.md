# Apache Airflow Scheduling and Triggers

**Research Date:** 2026-01-29
**Version:** Airflow 3.x

---

## Airflow 3.0 Scheduling Changes

**Critical changes:**
- Default timetable changed to `CronTriggerTimetable`
- Default `catchup` changed to `False`
- `logical_date` now equals `run_after` (not data interval start)
- Datasets renamed to "Assets"

---

## Scheduling Methods

### 1. Cron Expressions

```python
@dag(schedule="0 2 * * *")  # Daily at 2 AM
def my_dag():
    pass
```

### 2. Preset Schedules

| Preset | Cron Equivalent |
|--------|-----------------|
| `@once` | None |
| `@hourly` | `0 * * * *` |
| `@daily` | `0 0 * * *` |
| `@weekly` | `0 0 * * 0` |
| `@monthly` | `0 0 1 * *` |
| `@yearly` | `0 0 1 1 *` |

### 3. Timedelta

```python
from datetime import timedelta

@dag(schedule=timedelta(hours=6))  # Every 6 hours
def my_dag():
    pass
```

### 4. Manual Only

```python
@dag(schedule=None)  # Manual trigger only
def my_dag():
    pass
```

### 5. Data-Aware Scheduling (Assets)

```python
from airflow.datasets import Dataset

my_dataset = Dataset("s3://bucket/data.csv")

@dag(schedule=[my_dataset])  # Triggered when dataset updates
def downstream_dag():
    pass
```

---

## Key Concepts

### Data Interval (Critical!)

DAGs run at the **END** of intervals, not the start.

```
Data Interval: 2026-01-29 00:00 to 2026-01-30 00:00
DAG runs at: 2026-01-30 00:00:00 (after interval ends)
```

### Catchup vs Backfill

| Feature | Catchup | Backfill |
|---------|---------|----------|
| Trigger | Automatic | Manual |
| Control | `catchup=True/False` | CLI/UI/API |
| Use | Fill gaps when DAG paused | Historical processing |

```python
@dag(catchup=False)  # Don't run historical intervals
def my_dag():
    pass
```

### Trigger Rules

| Rule | Behavior |
|------|----------|
| `all_success` | All upstream succeeded (default) |
| `all_done` | All upstream completed (any state) |
| `one_failed` | At least one failed |
| `none_failed` | No failures |
| `always` | Always run |

```python
cleanup = BashOperator(
    task_id='cleanup',
    bash_command='rm -rf /tmp/data',
    trigger_rule='all_done'  # Run even if upstream fails
)
```

---

## Common Pitfalls

1. **Timezone confusion** - Airflow uses UTC by default
2. **Dynamic start_date** - Never use `datetime.now()`
3. **Catchup overload** - Set `catchup=False` unless needed
4. **Start date misalignment** - Align with schedule interval

---

## Decision Matrix

| Scenario | Schedule Method |
|----------|-----------------|
| Fixed time daily | Cron preset `@daily` |
| Every N hours | `timedelta(hours=N)` |
| After data arrives | Asset/Dataset |
| External event | Asset Watchers (SQS, etc.) |
| Manual only | `schedule=None` |
| Complex rules | Custom Timetable |

---

## Sources

- [Airflow Scheduling Documentation](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html)
- [Astronomer Scheduling Guide](https://www.astronomer.io/docs/learn/scheduling-in-airflow)
