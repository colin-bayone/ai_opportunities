# Apache Airflow Operators and Sensors Guide

**Research Date:** 2026-01-29
**Airflow Version:** 3.1.6

---

## Core Concepts

### Operators vs Sensors

| Type | Purpose | Examples |
|------|---------|----------|
| **Operators** | Execute specific actions | BashOperator, PythonOperator |
| **Sensors** | Wait for conditions | FileSensor, HttpSensor |
| **Transfer** | Move data between systems | S3ToRedshiftOperator |

---

## Common Operators

### Core Operators (Standard Provider)

**Note:** In Airflow 3.0+, install `apache-airflow-providers-standard`

```python
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
```

### Operator Selection Guide

| Use Case | Operator |
|----------|----------|
| Run shell command | BashOperator |
| Custom Python logic | @task or PythonOperator |
| Send email | EmailOperator |
| Run SQL query | SQLExecuteQueryOperator |
| HTTP/API call | HttpOperator |
| Run in container | KubernetesPodOperator |
| Placeholder/grouping | EmptyOperator |

---

## Sensors

### Sensor Modes

| Mode | Behavior | Best For |
|------|----------|----------|
| **poke** | Holds worker slot continuously | Checks every few seconds |
| **reschedule** | Releases slot between checks | Checks every minute+ |
| **deferrable** | Uses triggerer process | Long waits, high concurrency |

### Common Sensors

```python
# Wait for file
FileSensor(
    task_id='wait_for_file',
    filepath='/path/to/file.csv',
    timeout=3600,
    poke_interval=60,
    mode='reschedule'
)

# Wait for another DAG
ExternalTaskSensor(
    task_id='wait_for_other_dag',
    external_dag_id='other_dag',
    external_task_id='final_task',
    mode='reschedule'
)

# Wait for API
HttpSensor(
    task_id='wait_for_api',
    http_conn_id='api_default',
    endpoint='/health',
    response_check=lambda r: "healthy" in r.text,
    mode='deferrable'
)
```

---

## Deferrable Operators

**Problem:** Standard sensors hold worker slots while idle.

**Solution:** Deferrable operators suspend themselves and use triggerer process.

**Benefits:**
- 54% cost reduction (Condé Nast case study)
- Hundreds of deferred tasks per triggerer
- Better scalability

```python
# Enable deferrable mode
file_sensor = FileSensor(
    task_id='wait_file',
    filepath='/path/to/file',
    mode='deferrable'
)
```

---

## Hooks vs Operators

| Aspect | Hooks | Operators |
|--------|-------|-----------|
| Purpose | Connect to systems | Define tasks |
| Visibility | Internal to operators | Used in DAGs |
| Use | Multiple operations | Single task |

**Use hooks directly for complex operations:**

```python
@task
def complex_db_operation():
    hook = PostgresHook(postgres_conn_id='default')
    hook.run("BEGIN;")
    hook.run("INSERT INTO table1 VALUES (...);")
    hook.run("COMMIT;")
```

---

## Provider Packages

80+ providers available. Install as needed:

```bash
pip install apache-airflow-providers-google
pip install apache-airflow-providers-amazon
pip install apache-airflow-providers-postgres
```

---

## Custom Operators

```python
from airflow.sdk import BaseOperator

class HelloOperator(BaseOperator):
    template_fields = ("name",)  # Enable Jinja templating

    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        return f"Hello {self.name}"
```

**Key rules:**
- Create hooks in `execute()`, not `__init__()`
- Ensure idempotency
- Support templating for dynamic values

---

## Sources

- [Airflow Operators Documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html)
- [Airflow Sensors Documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/sensors.html)
- [Astronomer Deferrable Operators Guide](https://www.astronomer.io/docs/learn/deferrable-operators)
