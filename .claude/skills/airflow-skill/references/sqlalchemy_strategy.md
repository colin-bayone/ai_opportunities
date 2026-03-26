# SQLAlchemy Strategy Analysis for Airflow Skill

**Date:** 2026-01-29
**Purpose:** Analyze data model strategies for Airflow DAGs

---

## The Two Use Cases

| Use Case | Description | Example |
|----------|-------------|---------|
| **Django Integration** | Airflow works with existing Django-managed tables | ETL that reads/writes to Django app's database |
| **Standalone Airflow** | Airflow has its own data models, no Django | Data pipeline with dedicated warehouse |

Both need class-defined models (no raw SQL). Different strategies may apply.

---

## Understanding SQLAlchemy Reflection

### What It Is

SQLAlchemy can inspect a live database and generate model classes automatically:

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('postgresql://user:pass@host/db')
Base = automap_base()
Base.prepare(autoload_with=engine)

# Classes generated from tables
User = Base.classes.users
Candidate = Base.classes.candidates

# Use like normal ORM
session.query(User).filter(User.email == 'test@example.com').first()
```

### Pros and Cons

| Aspect | Pro | Con |
|--------|-----|-----|
| **Drift** | Zero drift - always matches DB | None |
| **Startup** | None (reflection at import) | ~1-3 sec per reflection |
| **Maintenance** | Zero - no models to update | None |
| **IDE Support** | None | No autocomplete, no type hints |
| **Custom Logic** | None | Can't add methods, properties |
| **Relationships** | Auto-detected from FKs | May miss complex relationships |

### When Reflection Makes Sense

- Quick prototyping
- Tables you only read from
- Tables with simple structure
- When you don't need custom model methods

### When Reflection Falls Short

- Need type hints for IDE support
- Need custom methods (e.g., `user.full_name` property)
- Complex relationships not expressed via FK constraints
- Performance-critical (reflection has startup cost)

---

## Django ORM in Airflow: Startup Analysis

### The Key Question

Does `django.setup()` run once or per-task?

### Answer: It Depends on Where You Call It

**Scenario A: Called in DAG file (BAD)**
```python
# my_dag.py - TOP LEVEL
import django
django.setup()  # Called every DAG parse cycle (every 30 sec!)
```
- Scheduler parses DAG files repeatedly
- 50MB + startup time every 30 seconds = bad

**Scenario B: Called inside task (OKAY)**
```python
@task
def my_task():
    import django
    django.setup()
    from myapp.models import MyModel
    # ...
```
- Only runs when task executes
- With CeleryExecutor, worker processes are long-lived
- Django may stay loaded between tasks on same worker
- But: first task on each worker pays setup cost

**Scenario C: Worker initialization (BEST)**
```python
# celery_config.py or worker startup
import django
django.setup()

# Now all tasks on this worker have Django available
```
- Setup once per worker process
- All tasks get Django ORM "for free"
- This is exactly how Django-Celery integration works
- 50MB per worker (not per task) - totally acceptable

### Verdict

**With CeleryExecutor + worker initialization, Django ORM is viable.**

The 50MB is per-worker, not per-task. Workers are long-lived. This is the same pattern used by Django apps running Celery today (like your current setup).

---

## Drift Detection Strategies

### The Problem

If you manually define SQLAlchemy models to match Django models, they can drift apart when Django models change.

### Strategy 1: Automated Generation + Git Diff

1. Agent generates SQLAlchemy models from Django models
2. Output goes to version-controlled file
3. When Django models change, re-run generator
4. Git diff shows what changed
5. Human reviews and commits

**Drift detection:** Git history shows when/what changed.

### Strategy 2: Runtime Schema Comparison

```python
def validate_models_match_db():
    """Run at Airflow startup or in CI."""
    from sqlalchemy import inspect
    inspector = inspect(engine)

    for model in [User, Candidate, Job]:
        table_name = model.__tablename__
        db_columns = {c['name'] for c in inspector.get_columns(table_name)}
        model_columns = {c.name for c in model.__table__.columns}

        if db_columns != model_columns:
            raise DriftDetectedError(f"{table_name} schema mismatch")
```

**Drift detection:** Fails fast if models don't match DB.

### Strategy 3: Hybrid (Reflection + Type Stubs)

```python
# Reflect actual schema
Base = automap_base()
Base.prepare(autoload_with=engine)

# Add type hints via stub file or wrapper
class User(Base.classes.users):
    """Typed wrapper with IDE support."""
    id: int
    email: str
    first_name: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
```

**Drift detection:** Reflection ensures base matches; you maintain only the typed wrapper.

---

## Proposed Agent Structure

Given the two use cases and various strategies, I propose **three specialized capabilities** (could be agents or modes of one agent):

### 1. SQLAlchemy Model Builder (Standalone)

**Purpose:** Create SQLAlchemy models from scratch for Airflow-only data.

**When used:**
- New data pipeline with no existing schema
- Airflow-specific tables (audit logs, pipeline metadata)
- Data warehouse tables

**How it works:**
1. User describes data requirements conversationally
2. Agent generates SQLAlchemy model classes
3. Optionally generates Alembic migration (if user wants)
4. Outputs to specified file location

**No Django involvement.**

### 2. Django Model Converter

**Purpose:** Generate SQLAlchemy models from existing Django models.

**When used:**
- Airflow needs to read/write Django app's database
- Want SQLAlchemy independence (no Django in Airflow workers)

**How it works:**
1. Agent reads Django model files (or inspects via `django.setup()`)
2. Generates equivalent SQLAlchemy models
3. Includes drift detection script
4. Outputs to Airflow project

**Input:** Django models → **Output:** SQLAlchemy models + validation script

### 3. Django ORM Direct Mode

**Purpose:** Use Django ORM directly in Airflow tasks.

**When used:**
- Same database as Django app
- Want zero model duplication
- Okay with Django dependency in workers

**How it works:**
1. Agent generates worker initialization code (`django.setup()`)
2. Configures Celery workers to initialize Django at startup
3. Tasks can import Django models directly
4. No SQLAlchemy needed

**Trade-off:** Tighter coupling, but zero drift and no duplication.

---

## Decision Matrix

| Situation | Recommended Approach |
|-----------|---------------------|
| Airflow-only, no Django | SQLAlchemy Model Builder |
| ETL for Django app, want independence | Django Model Converter |
| ETL for Django app, same team/deploy | Django ORM Direct Mode |
| Quick prototype, existing DB | SQLAlchemy Reflection |
| Data warehouse with strict types | SQLAlchemy Model Builder |

---

## Workflow Clarity

### Workflow A: Standalone SQLAlchemy

```
User: "I need models for a data pipeline"
    ↓
[SQLAlchemy Model Builder Agent]
    ↓
Questionnaire: table names, columns, relationships
    ↓
Generated: models.py with SQLAlchemy classes
    ↓
Optional: Alembic migration if needed
```

### Workflow B: Django → SQLAlchemy Conversion

```
User: "Convert my Django models for Airflow"
    ↓
[Django Model Converter Agent]
    ↓
Input: path to Django models or app name
    ↓
Agent inspects Django models
    ↓
Generated: sqlalchemy_models.py + validate_schema.py
    ↓
User runs validation in CI to catch drift
```

### Workflow C: Django ORM Direct

```
User: "I want to use Django ORM in my DAGs"
    ↓
[Django ORM Direct Mode Agent]
    ↓
Agent generates:
  - Minimal Django settings for Airflow
  - Worker initialization script
  - Example task using Django models
    ↓
User configures Celery workers to run init script
    ↓
Tasks import Django models directly
```

---

## My Recommendation

**Support all three approaches** because they serve different needs:

1. **SQLAlchemy Model Builder** - Default for new/standalone work
2. **Django Model Converter** - When you want independence from Django runtime
3. **Django ORM Direct** - When same team owns both and zero duplication matters

The skill should help users **choose** the right approach via questionnaire, then execute that strategy.

---

## Open Questions for You

1. **Does supporting all three approaches make sense**, or do you want to pick one as the blessed path?

2. **For drift detection**, do you prefer:
   - A: Automated regeneration + git diff (human reviews changes)
   - B: Runtime validation (fails if drift detected)
   - C: Both

3. **Alembic:** You mentioned it's complex for ETL. For Airflow-specific tables, would you prefer:
   - A: No migrations (manually manage schema)
   - B: Simple migration scripts (not full Alembic)
   - C: Alembic but only for Airflow-owned tables

---

## Next Steps

Once you confirm direction, I'll:
1. Add these agents to the architecture
2. Define the questionnaire flow for choosing approaches
3. Integrate with the brainstorm agent for discussing trade-offs
