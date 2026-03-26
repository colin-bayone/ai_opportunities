# DAG Testing Patterns for Airflow 3.x

**Source:** Airflow 3.x Official Documentation, Astronomer Best Practices
**Last Updated:** 2026-01-30

---

## Overview

Testing is essential for production-ready DAGs. Airflow 3.x provides built-in testing capabilities that replace the need for external libraries like pytest-airflow (archived 2021).

---

## Testing Stack

**DO NOT USE:**
- `pytest-airflow` - Archived April 2021, version 0.0.3, unmaintained

**USE:**
- `pytest` - Standard Python testing
- `airflow.models.DagBag` - DAG validation
- `dag.test()` - Integration testing (Airflow 2.5+/3.x)
- `unittest.mock` - Mocking external dependencies

---

## Test Categories

### 1. DAG Validation Tests

Verify DAGs load without errors:

```python
# tests/test_dag_validation.py
import pytest
from airflow.models import DagBag

@pytest.fixture
def dagbag():
    """Load all DAGs from the dags folder."""
    return DagBag(dag_folder="dags/", include_examples=False)

def test_no_import_errors(dagbag):
    """Test that all DAGs have no import errors."""
    assert len(dagbag.import_errors) == 0, f"Import errors: {dagbag.import_errors}"

def test_dag_loaded(dagbag):
    """Test that expected DAGs are loaded."""
    expected_dags = ["daily_etl", "hourly_sync", "weekly_report"]
    for dag_id in expected_dags:
        assert dag_id in dagbag.dags, f"DAG {dag_id} not found"

def test_dag_has_tags(dagbag):
    """Test that all DAGs have tags configured."""
    for dag_id, dag in dagbag.dags.items():
        assert dag.tags, f"DAG {dag_id} has no tags"

def test_dag_has_owner(dagbag):
    """Test that all DAGs have an owner."""
    for dag_id, dag in dagbag.dags.items():
        assert dag.default_args.get("owner"), f"DAG {dag_id} has no owner"

def test_dag_retries_configured(dagbag):
    """Test that all DAGs have retries configured."""
    for dag_id, dag in dagbag.dags.items():
        retries = dag.default_args.get("retries", 0)
        assert retries > 0, f"DAG {dag_id} has no retries configured"
```

### 2. DAG Structure Tests

Verify DAG configuration:

```python
# tests/test_dag_structure.py
import pytest
from datetime import timedelta
from airflow.models import DagBag

@pytest.fixture
def dagbag():
    return DagBag(dag_folder="dags/", include_examples=False)

def test_dag_schedule(dagbag):
    """Test that DAGs have valid schedules."""
    for dag_id, dag in dagbag.dags.items():
        # Schedule should be set (not None unless intentional)
        if dag_id not in ["manual_trigger_dag"]:  # Exceptions
            assert dag.schedule is not None, f"DAG {dag_id} has no schedule"

def test_dag_catchup_disabled(dagbag):
    """Test that catchup is disabled (our standard)."""
    for dag_id, dag in dagbag.dags.items():
        assert dag.catchup is False, f"DAG {dag_id} has catchup enabled"

def test_dag_max_active_runs(dagbag):
    """Test that max_active_runs is set."""
    for dag_id, dag in dagbag.dags.items():
        assert dag.max_active_runs is not None, f"DAG {dag_id} missing max_active_runs"
        assert dag.max_active_runs <= 3, f"DAG {dag_id} max_active_runs too high"

def test_task_timeouts(dagbag):
    """Test that tasks have execution timeouts."""
    for dag_id, dag in dagbag.dags.items():
        for task in dag.tasks:
            timeout = task.execution_timeout
            if timeout is None:
                timeout = dag.default_args.get("execution_timeout")
            assert timeout is not None, f"Task {task.task_id} in {dag_id} has no timeout"
```

### 3. Task Unit Tests

Test task logic in isolation:

```python
# tests/test_task_logic.py
import pytest
from unittest.mock import patch, MagicMock
from dags.daily_etl import extract_data, transform_data, load_data

class TestExtractData:
    """Tests for extract_data task."""

    @patch("dags.daily_etl.requests.get")
    def test_extract_success(self, mock_get):
        """Test successful data extraction."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": [1, 2, 3]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = extract_data()

        assert result == {"data": [1, 2, 3]}
        mock_get.assert_called_once()

    @patch("dags.daily_etl.requests.get")
    def test_extract_api_error(self, mock_get):
        """Test extraction handles API errors."""
        mock_get.side_effect = Exception("API unavailable")

        with pytest.raises(Exception, match="API unavailable"):
            extract_data()


class TestTransformData:
    """Tests for transform_data task."""

    def test_transform_valid_data(self):
        """Test transformation with valid input."""
        input_data = {"records": [{"id": 1, "value": 100}]}
        result = transform_data(input_data)

        assert "processed_records" in result
        assert len(result["processed_records"]) == 1

    def test_transform_empty_data(self):
        """Test transformation handles empty input."""
        with pytest.raises(ValueError, match="Empty data"):
            transform_data({})

    def test_transform_idempotent(self):
        """Test transformation is idempotent."""
        input_data = {"records": [{"id": 1, "value": 100}]}
        result1 = transform_data(input_data)
        result2 = transform_data(input_data)

        assert result1 == result2
```

### 4. Integration Tests with dag.test()

Test full DAG execution (Airflow 3.x):

```python
# tests/test_dag_integration.py
import pytest
from datetime import datetime
from airflow.models import DagBag

@pytest.fixture
def dagbag():
    return DagBag(dag_folder="dags/", include_examples=False)

def test_dag_execution(dagbag):
    """Test DAG can execute successfully."""
    dag = dagbag.get_dag("daily_etl")

    # Run the DAG for a specific date
    dag.test(
        execution_date=datetime(2026, 1, 15),
        mark_success_pattern=".*",  # Optional: mark tasks as success
    )

    # If no exception raised, test passed


def test_dag_with_mocked_connections(dagbag, monkeypatch):
    """Test DAG with mocked external connections."""
    # Mock the connection
    monkeypatch.setenv("AIRFLOW_CONN_MY_API", "http://mock-api:8080")

    dag = dagbag.get_dag("api_sync_dag")
    dag.test(execution_date=datetime(2026, 1, 15))
```

---

## Testing Best Practices

### 1. Test File Organization

```
project/
├── dags/
│   ├── daily_etl.py
│   └── weekly_report.py
├── tests/
│   ├── conftest.py           # Shared fixtures
│   ├── test_dag_validation.py
│   ├── test_dag_structure.py
│   ├── test_task_logic.py
│   └── test_dag_integration.py
└── pytest.ini
```

### 2. pytest.ini Configuration

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
filterwarnings =
    ignore::DeprecationWarning
```

### 3. conftest.py Shared Fixtures

```python
# tests/conftest.py
import pytest
import os
from airflow.models import DagBag

# Set Airflow home for tests
os.environ["AIRFLOW_HOME"] = os.path.dirname(os.path.dirname(__file__))

@pytest.fixture(scope="session")
def dagbag():
    """Session-scoped DagBag for all tests."""
    return DagBag(dag_folder="dags/", include_examples=False)

@pytest.fixture
def mock_connection(monkeypatch):
    """Fixture to mock Airflow connections."""
    def _mock(conn_id, conn_uri):
        monkeypatch.setenv(f"AIRFLOW_CONN_{conn_id.upper()}", conn_uri)
    return _mock
```

---

## Testing Anti-Patterns

### DON'T: Test implementation details

```python
# BAD - Testing internal implementation
def test_bad_internal_check():
    dag = get_dag("my_dag")
    # Don't test internal Airflow attributes
    assert dag._dag_id == "my_dag"  # Internal attribute
```

### DON'T: Skip validation tests

```python
# BAD - No validation
def test_nothing():
    pass  # Tests nothing
```

### DON'T: Use production connections in tests

```python
# BAD - Real API calls in tests
def test_with_real_api():
    result = extract_data()  # Hits real API!
```

### DO: Mock external dependencies

```python
# GOOD - Mocked dependencies
@patch("dags.my_dag.external_api_call")
def test_with_mock(mock_api):
    mock_api.return_value = {"data": "mocked"}
    result = extract_data()
    assert result == {"data": "mocked"}
```

---

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=dags --cov-report=html

# Run specific test file
pytest tests/test_dag_validation.py

# Run tests matching pattern
pytest tests/ -k "test_dag"

# Run with verbose output
pytest tests/ -v
```

---

## CI/CD Integration

```yaml
# .github/workflows/test.yml
name: DAG Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install apache-airflow[celery]==3.1.6
          pip install pytest pytest-cov

      - name: Run tests
        run: pytest tests/ --cov=dags
```

---

## Quality Auditor Checks

The Quality Auditor verifies:

1. [ ] DAG validation tests exist
2. [ ] No import errors in DagBag
3. [ ] Task logic has unit tests
4. [ ] External dependencies are mocked
5. [ ] Tests run in CI/CD pipeline
