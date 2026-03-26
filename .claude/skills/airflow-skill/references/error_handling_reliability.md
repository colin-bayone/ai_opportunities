# Apache Airflow Error Handling and Reliability

**Research Date:** 2026-01-29
**Version:** Airflow 3.x

---

## Retry Configuration

### Basic Retries

```python
@task(retries=3, retry_delay=timedelta(minutes=5))
def my_task():
    pass
```

### Exponential Backoff

```python
@task(
    retries=5,
    retry_delay=timedelta(minutes=1),
    retry_exponential_backoff=True,
    max_retry_delay=timedelta(minutes=30)
)
def api_task():
    pass
```

---

## Callbacks

### Available Callbacks

```python
def on_failure(context):
    send_alert(f"Task {context['task_instance'].task_id} failed!")

def on_success(context):
    log_completion(context['execution_date'])

def on_retry(context):
    log_retry_attempt(context)

@task(
    on_failure_callback=on_failure,
    on_success_callback=on_success,
    on_retry_callback=on_retry
)
def my_task():
    pass
```

### Context Dictionary Contents

- `task_instance` - Current task instance
- `execution_date` / `logical_date` - Run date
- `dag_run` - Current DAG run
- `exception` - Exception that caused failure (in failure callback)

---

## Email Notifications

### Setup

```ini
# airflow.cfg
[smtp]
smtp_host = smtp.gmail.com
smtp_port = 587
smtp_user = airflow@company.com
smtp_password = password
smtp_mail_from = airflow@company.com
```

### Task-Level

```python
task = MyOperator(
    task_id='important_task',
    email=['data-team@company.com'],
    email_on_failure=True,
    email_on_retry=False
)
```

---

## Timeouts

### Task Timeout

```python
@task(execution_timeout=timedelta(hours=2))
def long_task():
    pass
```

### Sensor Timeout

```python
sensor = FileSensor(
    task_id='wait_file',
    filepath='/path/to/file',
    timeout=3600,  # 1 hour max
    poke_interval=60
)
```

---

## Idempotency Patterns

### 1. Use Templated Dates

```python
@task
def process_data(**context):
    date = context['ds']  # YYYY-MM-DD
    output_path = f"/data/processed/{date}/"
    # Write to date-partitioned location
```

### 2. UPSERT Instead of INSERT

```sql
INSERT INTO results (id, value, updated_at)
VALUES (%(id)s, %(value)s, NOW())
ON CONFLICT (id) DO UPDATE SET
    value = EXCLUDED.value,
    updated_at = NOW();
```

### 3. Delete Before Insert

```python
@task
def load_data(**context):
    date = context['ds']
    hook.run(f"DELETE FROM table WHERE date = '{date}'")
    hook.run(f"INSERT INTO table SELECT * FROM staging WHERE date = '{date}'")
```

---

## SLA Monitoring

### Legacy (Airflow 2.x)

```python
@dag(sla_miss_callback=notify_sla_miss)
def my_dag():

    @task(sla=timedelta(hours=2))
    def important_task():
        pass
```

### Airflow 3.1+ Deadline Alerts

New approach using Deadline Alerts - more flexible than legacy SLAs.

---

## Alerting Integrations

### Slack

```python
from airflow.providers.slack.hooks.slack_webhook import SlackWebhookHook

def send_slack_alert(context):
    hook = SlackWebhookHook(slack_webhook_conn_id='slack_webhook')
    message = f":x: Task failed: {context['task_instance'].task_id}"
    hook.send(text=message)
```

### PagerDuty

```python
from airflow.providers.pagerduty.hooks.pagerduty import PagerdutyHook

def send_pagerduty_alert(context):
    hook = PagerdutyHook(pagerduty_conn_id='pagerduty_default')
    hook.create_event(
        summary=f"Airflow task failed: {context['task_instance'].task_id}",
        severity="error"
    )
```

---

## Reliability Checklist

- [ ] Retries configured (3+ for external systems)
- [ ] Timeouts set (prevent runaway tasks)
- [ ] Failure callbacks (alerting)
- [ ] Idempotent operations (safe to rerun)
- [ ] Connection error handling
- [ ] Proper logging
- [ ] Documentation

---

## Sources

- [Airflow Error Handling Guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/notifications.html)
- [Astronomer Error Handling](https://www.astronomer.io/docs/learn/error-notifications-in-airflow)
