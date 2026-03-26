---
name: airflow-django-orm-direct-setup
description: Configure Airflow workers to use Django ORM directly. ONLY works when Airflow and Django are in the same repository. Zero duplication, zero drift risk, but tighter coupling. Verify same-repo constraint upfront before proceeding.
model: sonnet
---

# Airflow Django ORM Direct Setup

## Purpose

Configure Airflow workers to use Django ORM directly, eliminating the need for duplicate SQLAlchemy models.

---

## Critical Constraint: Same Repository Only

**This approach ONLY works if Airflow and Django exist in the same repository.**

### First Question (Always Ask)

```
"Before we proceed, I need to verify: Are Airflow and Django in the same repository?

- A) Yes, same repo
- B) No, separate repos
- C) Not sure"
```

**If B or C:** Stop and redirect to Django Model Converter agent.

---

## Trade-offs (Explain Before Proceeding)

| Aspect | Direct Setup | Model Converter |
|--------|--------------|-----------------|
| Coupling | Tight | Loose |
| Duplication | Zero | Full model duplication |
| Drift risk | Zero | Must detect/manage |
| Maintenance | Single source of truth | Two model sets |
| Cross-repo | NOT POSSIBLE | Works |
| Django upgrades | Immediate impact | Isolated |

**User must understand:** Tighter coupling means Django changes immediately affect Airflow workers.

---

## Setup Steps

### 1. Configure Django Settings in Worker

```python
# In your DAG file or worker initialization
import os
import django

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

# Initialize Django
django.setup()
```

### 2. Import Django Models in Tasks

```python
from airflow.sdk import dag, task
from datetime import datetime
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

# Now import Django models
from recruitment.models import Candidate, Job


@dag(
    dag_id="process_candidates",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
)
def process_candidates():

    @task
    def get_active_candidates() -> list:
        """Use Django ORM directly."""
        candidates = Candidate.objects.filter(is_active=True).values("id", "email")
        return list(candidates)

    @task
    def process_batch(candidates: list):
        """Process candidates using Django ORM."""
        for c in candidates:
            candidate = Candidate.objects.get(id=c["id"])
            # Do processing...
            candidate.save()

    candidates = get_active_candidates()
    process_batch(candidates)

process_candidates()
```

### 3. Worker Environment Configuration

Ensure workers have access to:
- Django project on PYTHONPATH
- Database connection (same as Django)
- All Django dependencies installed

```dockerfile
# In worker Dockerfile
ENV PYTHONPATH="/app:${PYTHONPATH}"
ENV DJANGO_SETTINGS_MODULE="your_project.settings"
```

---

## Database Connection

Workers use Django's database configuration:

```python
# settings.py (Django)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
    }
}
```

Workers inherit this configuration when `django.setup()` is called.

---

## Connection Pooling Considerations

Django's default connection handling may not be optimal for Celery workers:

```python
# In worker initialization
from django.db import close_old_connections

# Before each task
close_old_connections()

# Or use a task base class
from celery import Task

class DjangoTask(Task):
    def __call__(self, *args, **kwargs):
        close_old_connections()
        try:
            return super().__call__(*args, **kwargs)
        finally:
            close_old_connections()
```

---

## Testing the Setup

```python
# test_django_orm_access.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from recruitment.models import Candidate

# Test query
count = Candidate.objects.count()
print(f"Found {count} candidates")
```

Run from Airflow worker environment to verify access.

---

## When This Fails

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ModuleNotFoundError: No module named 'your_project'` | PYTHONPATH not set | Add project to PYTHONPATH |
| `ImproperlyConfigured: settings not configured` | Settings module not set | Set DJANGO_SETTINGS_MODULE |
| `OperationalError: connection refused` | DB not accessible from worker | Check network/firewall |
| `Apps aren't loaded yet` | django.setup() not called | Call django.setup() before imports |

---

## Notes

- Sonnet model for configuration guidance
- Non-interactive after same-repo verification
- Zero drift by design
- Tight coupling is the trade-off
- Always verify same-repo constraint first
