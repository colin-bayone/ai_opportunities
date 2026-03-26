# XCom Best Practices for Airflow 3.x

**Source:** Airflow 3.x Official Documentation, Astronomer Best Practices
**Last Updated:** 2026-01-30

---

## Overview

XCom (Cross-Communication) enables tasks to exchange small amounts of data. Airflow 3.x introduces breaking changes including immutable context. Understanding XCom limits and alternatives is critical for production DAGs.

---

## Breaking Change: Immutable Context (Airflow 3.x)

**CRITICAL:** In Airflow 3.x, task context is immutable. You cannot modify `context` or `kwargs` directly.

### Old Pattern (Airflow 2.x) - BROKEN

```python
# DON'T DO THIS - Will fail in Airflow 3.x
def my_task(**context):
    context['ti'].xcom_push(key='result', value='data')  # Still works
    context['my_custom_key'] = 'value'  # FAILS - immutable context
```

### New Pattern (Airflow 3.x) - CORRECT

```python
# DO THIS - Airflow 3.x compatible
@task
def my_task(**context):
    ti = context['ti']
    ti.xcom_push(key='result', value='data')
    return {'my_custom_key': 'value'}  # Return data instead
```

---

## Size Limits by Database

XCom storage uses your metadata database. Size limits vary significantly:

| Database | Max XCom Size | Notes |
|----------|---------------|-------|
| PostgreSQL | ~1 GB | BYTEA column, practical limit ~100 MB |
| MySQL | 64 KB | BLOB default, can increase to LONGBLOB (4 GB) |
| SQLite | ~1 GB | Not recommended for production |

### PostgreSQL Configuration

```sql
-- Check current XCom sizes
SELECT dag_id, task_id, key,
       pg_size_pretty(length(value)::bigint) as size
FROM xcom
ORDER BY length(value) DESC
LIMIT 10;
```

### Recommendation

**Keep XComs under 48 KB** regardless of database. Larger data should use external storage.

---

## When to Use XCom

### Good Use Cases

```python
# ✅ Small metadata
@task
def get_record_count():
    return 1523  # Small integer

# ✅ Status flags
@task
def validate_data():
    return {"valid": True, "errors": []}

# ✅ File paths (not file contents)
@task
def generate_report():
    path = "/data/reports/daily_2026-01-30.csv"
    # Write file to shared storage
    return path  # Return path, not content

# ✅ Small configuration
@task
def determine_processing_mode():
    return {"mode": "incremental", "batch_size": 1000}
```

### Bad Use Cases

```python
# ❌ Large DataFrames
@task
def process_data():
    df = pd.read_csv("large_file.csv")
    return df.to_dict()  # DON'T - could be huge

# ❌ File contents
@task
def read_file():
    with open("data.json") as f:
        return f.read()  # DON'T - unknown size

# ❌ Binary data
@task
def process_image():
    with open("image.png", "rb") as f:
        return f.read()  # DON'T - binary in XCom
```

---

## Alternatives to XCom for Large Data

### 1. Object Storage (Recommended)

```python
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
# or
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

@task
def generate_large_data():
    # Generate data
    data = generate_report_data()

    # Write to object storage
    hook = S3Hook(aws_conn_id='my_s3')
    key = f"data/reports/{datetime.now().isoformat()}.parquet"
    hook.load_bytes(
        data.to_parquet(),
        key=key,
        bucket_name='my-bucket'
    )

    # Return only the reference
    return {"bucket": "my-bucket", "key": key}

@task
def consume_large_data(reference):
    hook = S3Hook(aws_conn_id='my_s3')
    data = hook.read_key(reference['key'], reference['bucket'])
    # Process data
```

### 2. Shared Filesystem

```python
import json
from pathlib import Path

SHARED_DATA_PATH = Path("/mnt/airflow-data")

@task
def producer_task(execution_date):
    data = generate_data()

    # Write to shared filesystem
    output_path = SHARED_DATA_PATH / f"output_{execution_date}.json"
    output_path.write_text(json.dumps(data))

    return str(output_path)  # Return path via XCom

@task
def consumer_task(file_path):
    data = json.loads(Path(file_path).read_text())
    # Process data
```

### 3. Database Tables (Staging)

```python
from sqlalchemy import create_engine

@task
def write_staging_data(data, execution_date):
    engine = create_engine("postgresql://...")
    table_name = f"staging_{execution_date.strftime('%Y%m%d')}"

    # Write to staging table
    data.to_sql(table_name, engine, if_exists='replace')

    return table_name  # Return table name via XCom

@task
def read_staging_data(table_name):
    engine = create_engine("postgresql://...")
    return pd.read_sql_table(table_name, engine)
```

### 4. Custom XCom Backend

For organizations needing large XCom with existing patterns:

```python
# airflow_settings.py or airflow.cfg
# [core]
# xcom_backend = my_company.xcom.S3XComBackend

# Custom backend implementation
from airflow.models.xcom import BaseXCom
import json

class S3XComBackend(BaseXCom):
    @staticmethod
    def serialize_value(value):
        # Serialize large values to S3
        if len(json.dumps(value)) > 48000:  # 48KB threshold
            key = upload_to_s3(value)
            return json.dumps({"__s3_key__": key})
        return json.dumps(value)

    @staticmethod
    def deserialize_value(result):
        value = json.loads(result.value)
        if isinstance(value, dict) and "__s3_key__" in value:
            return download_from_s3(value["__s3_key__"])
        return value
```

---

## Security Considerations

### XCom is NOT Encrypted

XCom values are stored in plain text in the metadata database.

```python
# ❌ NEVER store secrets in XCom
@task
def bad_example():
    return {"api_key": "secret123"}  # EXPOSED IN DATABASE

# ✅ Use Airflow Connections or Secrets Backend
from airflow.hooks.base import BaseHook

@task
def good_example():
    conn = BaseHook.get_connection("my_api")
    # Use conn.password, conn.extra_dejson, etc.
```

### XCom Visible in UI

Anyone with Airflow UI access can view XCom values:
- **Admin > XComs** shows all values
- Task logs may include XCom data
- API endpoints expose XCom

**Rule:** Never store PII, credentials, or sensitive data in XCom.

---

## TaskFlow API and Automatic XCom

TaskFlow API (`@task` decorator) automatically handles XCom:

```python
from airflow.decorators import dag, task

@dag(schedule="@daily", start_date=datetime(2026, 1, 1), catchup=False)
def my_dag():

    @task
    def extract():
        return {"count": 100, "status": "ok"}  # Auto-pushed to XCom

    @task
    def transform(data):  # Auto-pulled from XCom
        return data["count"] * 2

    @task
    def load(result):
        print(f"Loading {result} records")

    # Explicit data flow - XCom handled automatically
    data = extract()
    result = transform(data)
    load(result)

my_dag()
```

### Multiple Outputs

```python
@task(multiple_outputs=True)
def extract():
    return {
        "users": [1, 2, 3],
        "orders": [101, 102],
        "timestamp": "2026-01-30"
    }

@task
def process_users(users):
    # Receives [1, 2, 3]
    pass

@task
def process_orders(orders):
    # Receives [101, 102]
    pass

# Usage
data = extract()
process_users(data["users"])
process_orders(data["orders"])
```

---

## XCom Cleanup

XCom values accumulate over time. Clean them up:

### Automatic Cleanup (Recommended)

```python
# airflow.cfg
[scheduler]
min_file_process_interval = 30

[core]
# Clean XComs older than 30 days
max_xcom_age_in_days = 30
```

### Manual Cleanup

```python
from airflow.models import XCom
from airflow.utils.db import provide_session
from datetime import datetime, timedelta

@provide_session
def cleanup_old_xcoms(session=None):
    cutoff = datetime.now() - timedelta(days=30)
    session.query(XCom).filter(XCom.timestamp < cutoff).delete()
    session.commit()
```

### DAG-Specific Cleanup

```python
@task
def cleanup_xcoms(**context):
    """Clean up XComs after DAG completion."""
    from airflow.models import XCom

    XCom.clear(
        dag_id=context['dag'].dag_id,
        task_id=None,  # All tasks
        execution_date=context['execution_date'],
    )
```

---

## Performance Considerations

### Serialization Overhead

XCom uses JSON serialization by default:

```python
# Fast - simple types
return 42
return "string"
return [1, 2, 3]

# Slower - complex nested structures
return {
    "level1": {
        "level2": {
            "level3": [{"nested": "data"}] * 1000
        }
    }
}
```

### Query Performance

XCom queries can slow down with large volumes:

```python
# Avoid pulling all XComs
ti.xcom_pull(task_ids='*')  # SLOW - pulls everything

# Be specific
ti.xcom_pull(task_ids='specific_task', key='specific_key')  # FAST
```

---

## Best Practices Summary

| Practice | Description |
|----------|-------------|
| **Keep it small** | Under 48 KB per XCom value |
| **Return paths, not content** | Store files externally, pass references |
| **No secrets** | Use Connections and Secrets Backend |
| **Clean up** | Configure automatic XCom cleanup |
| **Be specific** | Pull specific keys, not wildcards |
| **Use TaskFlow** | Let Airflow handle XCom automatically |
| **Mind immutability** | Don't modify context in 3.x |

---

## Quality Auditor Checks

The Quality Auditor verifies:

1. [ ] No XCom values exceed 48 KB
2. [ ] No secrets or PII in XCom
3. [ ] Large data uses external storage
4. [ ] TaskFlow API used where appropriate
5. [ ] Context not modified (3.x compliance)
