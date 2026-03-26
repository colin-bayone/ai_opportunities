# Apache Airflow TaskFlow API Best Practices

**Research Date:** 2026-01-29
**Version Coverage:** Airflow 2.0+ through 3.x

---

## Overview

TaskFlow API introduced in Airflow 2.0 - the modern, Pythonic way to write DAGs using decorators.

### Key Benefits

- Eliminates boilerplate code
- Automatic XCom handling
- Inferred task dependencies
- Cleaner, more readable DAGs

---

## Core Concepts

### @dag and @task Decorators

```python
from airflow.decorators import dag, task
from datetime import datetime

@dag(schedule="@daily", start_date=datetime(2025, 1, 1), catchup=False)
def my_dag():

    @task
    def extract():
        return {"data": "value"}

    @task
    def transform(data: dict):
        return data['data'].upper()

    @task
    def load(data: str):
        print(f"Loading: {data}")

    # Dependencies inferred automatically
    load(transform(extract()))

my_dag()
```

### Airflow 3.x Import

```python
from airflow.sdk import dag, task  # Stable authoring interface
```

---

## When to Use TaskFlow API

### Use TaskFlow When:
- Writing custom Python logic
- Simple data passing between tasks
- Want cleaner, more readable code
- Testing focus (unit test business logic)

### Use Traditional Operators When:
- Using specialized operators (SparkOperator, BigQueryOperator)
- Need fine-grained control
- Working with provider packages
- Complex trigger rules

### Best Practice: Combine Both

```python
@dag(start_date=datetime(2026, 1, 1))
def mixed_dag():
    bash_task = BashOperator(task_id='start', bash_command='echo "Starting"')

    @task
    def process():
        return "processed"

    bash_task >> process()
```

---

## Key Patterns

### Multiple Outputs

```python
@task(multiple_outputs=True)
def process_data():
    return {"total": 1000, "count": 50}

results = process_data()
use_total(results["total"])
use_count(results["count"])
```

### Task Configuration Override

```python
@task
def reusable_task(input_data):
    return input_data.upper()

task1 = reusable_task.override(task_id="process_a", retries=5)(data_a)
task2 = reusable_task.override(task_id="process_b")(data_b)
```

### Dynamic Task Mapping

```python
@task
def process_file(filename: str):
    return f"Processed {filename}"

process_file.expand(filename=["file1.csv", "file2.csv", "file3.csv"])
```

### Airflow 3.x Conditional Execution

```python
@task.skip_if(condition=lambda ctx: ctx["dag_run"].conf.get("skip"))
def conditional_task():
    return "Executed"
```

---

## Testing Patterns

### Test Business Logic Separately

```python
# business_logic.py
def calculate_revenue(orders: list) -> float:
    return sum(order["amount"] for order in orders)

# test_business_logic.py
def test_calculate_revenue():
    orders = [{"amount": 100}, {"amount": 200}]
    assert calculate_revenue(orders) == 300
```

### Test TaskFlow Functions

```python
# Access underlying function
def test_process_data():
    result = process_data.function(10)
    assert result == 20
```

---

## Performance Considerations

- XCom practical limit: < 1MB
- Use custom XCom backend for large data
- Pass references (S3 keys) instead of data
- Limit dynamic mapping to < 1000 instances

---

## Common Mistakes

1. **XCom serialization** - Only JSON-serializable values work by default
2. **Large data in DAG file scope** - Loaded every parse cycle
3. **Forgetting to call functions** - `my_task` vs `my_task()`
4. **Nested task mapping** - Not supported

---

## Sources

- [Airflow TaskFlow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html)
- [Astronomer TaskFlow Guide](https://www.astronomer.io/docs/learn/airflow-decorators)
