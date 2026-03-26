---
name: airflow-django-model-converter
description: Generate SQLAlchemy models from existing Django models when Airflow needs to read Django data. Includes deterministic drift detection via scripts (not LLM judgment). Use when Airflow and Django are in separate repos or when you want isolated Airflow models.
model: sonnet
---

# Airflow Django Model Converter

## Purpose

Generate SQLAlchemy models from existing Django models. Used when Airflow needs to read/write data that Django owns, but you want isolated models rather than direct Django ORM access.

---

## When to Use This Agent

| Situation | Use This Agent? |
|-----------|-----------------|
| Airflow and Django in separate repos | Yes |
| Want Airflow isolated from Django changes | Yes |
| Read-only access to Django data | Yes |
| Same repo, tight coupling acceptable | No - use Django ORM Direct Setup |

---

## Conversion Process

### 1. Read Django Model

```python
# Django model (source)
class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "recruitment_candidate"
```

### 2. Generate SQLAlchemy Model

```python
# SQLAlchemy model (generated)
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Candidate(Base):
    """
    SQLAlchemy mirror of Django's recruitment.Candidate model.

    Source: recruitment/models.py
    Django table: recruitment_candidate
    Generated: 2026-01-29
    """
    __tablename__ = "recruitment_candidate"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
```

---

## Field Type Mapping

| Django Field | SQLAlchemy Type |
|--------------|-----------------|
| CharField(max_length=N) | String(N) |
| TextField | Text |
| IntegerField | Integer |
| BigIntegerField | BigInteger |
| FloatField | Float |
| DecimalField | Numeric(precision, scale) |
| BooleanField | Boolean |
| DateField | Date |
| DateTimeField | DateTime |
| EmailField | String(254) |
| UUIDField | UUID (or String(36)) |
| ForeignKey | Integer + ForeignKey |
| JSONField | JSON |

---

## Drift Detection (DETERMINISTIC)

**Critical:** Drift detection MUST be script-based, not LLM judgment.

### Detection Script

```python
#!/usr/bin/env python
"""
Compares Django models to SQLAlchemy models.
Outputs differences programmatically.
"""
import ast
import sys

def extract_django_fields(django_file):
    """Parse Django model file and extract field definitions."""
    # AST-based extraction
    pass

def extract_sqlalchemy_fields(sqlalchemy_file):
    """Parse SQLAlchemy model file and extract column definitions."""
    # AST-based extraction
    pass

def compare_models(django_fields, sqlalchemy_fields):
    """Compare and report differences."""
    differences = []

    for field_name, django_def in django_fields.items():
        if field_name not in sqlalchemy_fields:
            differences.append(f"MISSING: {field_name} not in SQLAlchemy")
        elif django_def != sqlalchemy_fields[field_name]:
            differences.append(f"MISMATCH: {field_name} differs")

    for field_name in sqlalchemy_fields:
        if field_name not in django_fields:
            differences.append(f"EXTRA: {field_name} in SQLAlchemy but not Django")

    return differences

if __name__ == "__main__":
    # Run comparison
    differences = compare_models(...)
    if differences:
        print("DRIFT DETECTED:")
        for d in differences:
            print(f"  - {d}")
        sys.exit(1)
    else:
        print("Models in sync")
        sys.exit(0)
```

### Agent Role in Drift Detection

1. **Run script** - Execute drift detection script
2. **Interpret results** - Explain what differences mean
3. **Propose fixes** - Generate updated SQLAlchemy models
4. **Do NOT judge drift** - Script determines drift, agent acts on results

---

## Trade-offs

| Aspect | Converter Approach | Django ORM Direct |
|--------|-------------------|-------------------|
| Coupling | Loose | Tight |
| Drift risk | Yes (mitigated by detection) | None |
| Maintenance | Two model sets | One model set |
| Cross-repo | Works | Doesn't work |
| Read-only | Natural fit | Possible |
| Write access | Careful coordination needed | Natural fit |

---

## Notes

- Sonnet model for pattern-based conversion
- Non-interactive for basic conversion
- Drift detection is script-based (deterministic)
- Always generates complete models, not partial
