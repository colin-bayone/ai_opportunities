# Connection & Hook Patterns for Airflow 3.x

**Source:** Airflow 3.x Official Documentation, Astronomer Best Practices
**Last Updated:** 2026-01-30

---

## Overview

Connections store credentials and connection parameters securely. Hooks provide the interface to interact with external systems. Proper connection management is critical for security and maintainability.

---

## Connection Storage Methods

### 1. Environment Variables (Development)

Good for local development and simple setups:

```bash
# Format: AIRFLOW_CONN_{CONN_ID}='{conn_type}://{login}:{password}@{host}:{port}/{schema}?{extras}'

# PostgreSQL example
export AIRFLOW_CONN_MY_POSTGRES='postgresql://user:pass@localhost:5432/mydb'

# HTTP API example
export AIRFLOW_CONN_MY_API='http://api-key@api.example.com:443?headers={"Authorization":"Bearer+token"}'

# With extras (URL-encoded JSON)
export AIRFLOW_CONN_AZURE_BLOB='wasb://account:key@blob.core.windows.net?extra__azure_blob__sas_token=xxx'
```

### 2. Secrets Backend (Production)

**Recommended for production.** Integrates with external secrets managers.

#### Azure Key Vault (Our Infrastructure)

```python
# airflow.cfg or environment variable
[secrets]
backend = airflow.providers.microsoft.azure.secrets.key_vault.AzureKeyVaultBackend
backend_kwargs = {
    "connections_prefix": "airflow-conn",
    "variables_prefix": "airflow-var",
    "vault_url": "https://my-keyvault.vault.azure.net/"
}
```

Secret naming in Key Vault:
```
# Connection: my_postgres
airflow-conn-my-postgres

# Variable: my_setting
airflow-var-my-setting
```

#### AWS Secrets Manager

```python
[secrets]
backend = airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend
backend_kwargs = {
    "connections_prefix": "airflow/connections",
    "variables_prefix": "airflow/variables"
}
```

#### HashiCorp Vault

```python
[secrets]
backend = airflow.providers.hashicorp.secrets.vault.VaultBackend
backend_kwargs = {
    "url": "https://vault.example.com",
    "mount_point": "airflow",
    "connections_path": "connections",
    "variables_path": "variables"
}
```

### 3. Airflow Metadata Database

**Not recommended for production** - credentials stored in metadata DB.

```python
from airflow.models import Connection
from airflow.utils.db import provide_session

@provide_session
def create_connection(session=None):
    conn = Connection(
        conn_id='my_connection',
        conn_type='postgres',
        host='localhost',
        login='user',
        password='secret',
        port=5432,
        schema='mydb'
    )
    session.add(conn)
    session.commit()
```

---

## Using Connections in DAGs

### Via Hooks (Recommended)

```python
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

@task
def query_database():
    hook = PostgresHook(postgres_conn_id='my_postgres')
    records = hook.get_records("SELECT * FROM users LIMIT 10")
    return records

@task
def call_api():
    hook = HttpHook(http_conn_id='my_api', method='GET')
    response = hook.run('/endpoint')
    return response.json()

@task
def read_blob():
    hook = WasbHook(wasb_conn_id='azure_blob')
    data = hook.read_file('container', 'path/to/file.csv')
    return data
```

### Via BaseHook (Generic)

```python
from airflow.hooks.base import BaseHook

@task
def use_connection():
    conn = BaseHook.get_connection('my_connection')

    # Access connection attributes
    host = conn.host
    login = conn.login
    password = conn.password  # Decrypted automatically
    port = conn.port
    schema = conn.schema

    # Access extra parameters
    extras = conn.extra_dejson  # Parsed JSON from extra field

    # Use in your code
    client = MyClient(
        host=host,
        username=login,
        password=password,
        **extras
    )
```

### Via Operators (Built-in)

```python
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.operators.http import HttpOperator

# SQL execution
query_task = PostgresOperator(
    task_id='run_query',
    postgres_conn_id='my_postgres',
    sql='SELECT COUNT(*) FROM orders'
)

# HTTP request
api_task = HttpOperator(
    task_id='call_api',
    http_conn_id='my_api',
    endpoint='/data',
    method='GET'
)
```

---

## Hook Best Practices

### 1. Use Provider Hooks

Airflow 3.x uses provider packages. Use the appropriate hook:

```python
# ✅ Correct - Provider hooks
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow.providers.http.hooks.http import HttpHook

# ❌ Deprecated - Old locations
# from airflow.hooks.postgres_hook import PostgresHook  # OLD
# from airflow.hooks.S3_hook import S3Hook  # OLD
```

### 2. Context Manager Pattern

For connections that need cleanup:

```python
@task
def safe_database_operation():
    hook = PostgresHook(postgres_conn_id='my_postgres')

    # Use context manager for connection handling
    with hook.get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()

    return results
```

### 3. Connection Testing

Test connections before using in production:

```python
@task
def test_connection():
    hook = PostgresHook(postgres_conn_id='my_postgres')
    try:
        hook.get_conn()
        return {"status": "success"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
```

---

## Custom Hooks

When provider hooks don't meet your needs:

```python
from airflow.hooks.base import BaseHook
from typing import Any

class MyCustomHook(BaseHook):
    """Hook for MyCustomService."""

    conn_name_attr = 'my_custom_conn_id'
    default_conn_name = 'my_custom_default'
    conn_type = 'my_custom'
    hook_name = 'My Custom Service'

    def __init__(self, my_custom_conn_id: str = default_conn_name):
        super().__init__()
        self.my_custom_conn_id = my_custom_conn_id
        self._client = None

    def get_conn(self) -> Any:
        """Get connection to MyCustomService."""
        if self._client is None:
            conn = self.get_connection(self.my_custom_conn_id)
            self._client = MyCustomClient(
                host=conn.host,
                api_key=conn.password,
                **conn.extra_dejson
            )
        return self._client

    def run_query(self, query: str) -> list:
        """Execute query on MyCustomService."""
        client = self.get_conn()
        return client.query(query)
```

### Register Custom Connection Type

```python
# plugins/my_plugin.py
from airflow.plugins_manager import AirflowPlugin

class MyCustomPlugin(AirflowPlugin):
    name = "my_custom_plugin"
    hooks = [MyCustomHook]

    # Connection form fields for UI
    connection_form_widgets = {
        "extra__my_custom__api_version": StringField(
            "API Version",
            default="v2"
        ),
    }

    connection_form_field_placeholders = {
        "host": "api.example.com",
        "password": "your-api-key",
        "extra__my_custom__api_version": "v2",
    }
```

---

## Connection Security

### Never Hardcode Credentials

```python
# ❌ NEVER DO THIS
@task
def bad_example():
    conn = psycopg2.connect(
        host="prod-db.example.com",
        password="super_secret_123"  # EXPOSED IN CODE
    )

# ✅ Always use connections
@task
def good_example():
    hook = PostgresHook(postgres_conn_id='my_postgres')
    conn = hook.get_conn()
```

### Mask Sensitive Values in Logs

```python
from airflow.utils.log.secrets_masker import mask_secret

@task
def handle_sensitive_data():
    hook = PostgresHook(postgres_conn_id='my_postgres')
    conn = hook.get_connection('my_postgres')

    # Mask in logs
    mask_secret(conn.password)

    # Now password will show as *** in logs
    print(f"Connecting to {conn.host}")
```

### Connection Scoping

Limit connection visibility:

```python
# Connection IDs should be descriptive and scoped
# ✅ Good
'prod_analytics_postgres'
'stage_user_api'
'dev_local_redis'

# ❌ Bad (too generic)
'postgres'
'api'
'db'
```

---

## Azure Integration (Our Infrastructure)

### Azure Key Vault Secrets Backend

```python
# airflow.cfg
[secrets]
backend = airflow.providers.microsoft.azure.secrets.key_vault.AzureKeyVaultBackend
backend_kwargs = {
    "connections_prefix": "airflow-conn",
    "variables_prefix": "airflow-var",
    "vault_url": "https://talent-ai-keyvault.vault.azure.net/"
}

# Authentication via Managed Identity (recommended) or Service Principal
```

### Store Connection in Key Vault

```bash
# Connection as JSON
az keyvault secret set \
  --vault-name talent-ai-keyvault \
  --name airflow-conn-my-postgres \
  --value '{
    "conn_type": "postgres",
    "host": "my-db.postgres.database.azure.com",
    "login": "airflow_user",
    "password": "secret",
    "port": 5432,
    "schema": "airflow_db",
    "extra": {"sslmode": "require"}
  }'
```

### Azure Blob Storage Connection

```python
# Via Managed Identity (recommended)
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

@task
def read_from_blob():
    # Connection configured with managed identity
    hook = WasbHook(wasb_conn_id='azure_blob')
    data = hook.read_file(
        container_name='data',
        blob_name='input/file.csv'
    )
    return data
```

---

## Troubleshooting Connections

### Test Connection via CLI

```bash
# Test a connection
airflow connections test my_postgres

# List all connections
airflow connections list

# Export connection (for debugging only)
airflow connections export --format json /tmp/conns.json
```

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `Connection not found` | Missing connection | Create in UI, env var, or secrets backend |
| `Access denied` | Wrong credentials | Verify in secrets backend |
| `SSL required` | Missing SSL config | Add `sslmode=require` to extras |
| `Timeout` | Network/firewall | Check VNet, NSG rules |

### Debug Connection Lookup

```python
from airflow.hooks.base import BaseHook
import logging

logging.getLogger('airflow.secrets').setLevel(logging.DEBUG)

# Now connection lookups will log which backend was searched
conn = BaseHook.get_connection('my_connection')
```

---

## Connection Templates

### PostgreSQL

```json
{
  "conn_type": "postgres",
  "host": "db.example.com",
  "login": "user",
  "password": "secret",
  "port": 5432,
  "schema": "mydb",
  "extra": {
    "sslmode": "require"
  }
}
```

### HTTP API

```json
{
  "conn_type": "http",
  "host": "api.example.com",
  "port": 443,
  "password": "api-key",
  "extra": {
    "headers": {
      "Authorization": "Bearer {password}",
      "Content-Type": "application/json"
    }
  }
}
```

### Azure Blob Storage

```json
{
  "conn_type": "wasb",
  "login": "storage_account_name",
  "password": "storage_account_key",
  "extra": {
    "sas_token": "optional_sas_token"
  }
}
```

### Redis

```json
{
  "conn_type": "redis",
  "host": "redis.example.com",
  "port": 6379,
  "password": "secret",
  "extra": {
    "db": 0,
    "ssl": true
  }
}
```

---

## Quality Auditor Checks

The Quality Auditor verifies:

1. [ ] No hardcoded credentials in DAG code
2. [ ] Connections use secrets backend in production
3. [ ] Connection IDs are descriptive and scoped
4. [ ] Provider hooks used (not deprecated locations)
5. [ ] Sensitive values masked in logs
