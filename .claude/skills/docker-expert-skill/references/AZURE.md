# Azure Container Apps Reference

Reference for Claude Code. Patterns for deploying to Azure Container Apps.

## Architecture Overview

For Django + Celery stack on ACA:
- **Web Container App**: Django API with Gunicorn
- **Celery Worker Container App**: Background task processing
- **Celery Beat Container App**: Task scheduling (single replica)
- **Azure Redis Cache**: Message broker + result backend
- **Azure PostgreSQL**: Database (managed service)
- **Azure Key Vault**: Secrets management

## Production Dockerfile Pattern

### Django API
```dockerfile
# syntax=docker/dockerfile:1

# ============= BUILD STAGE =============
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip wheel --no-cache-dir --wheel-dir=/app/wheels -r requirements.txt

# ============= RUNTIME STAGE =============
FROM python:3.11-slim-bookworm AS runtime

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy and install wheels
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Copy application
COPY --chown=appuser:appuser . .

# Collect static files
RUN python manage.py collectstatic --noinput

USER appuser

EXPOSE 8000

# Health check for ACA
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "2", "config.wsgi:application"]
```

### Celery Worker
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN groupadd -r celery && useradd -r -g celery celery

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=celery:celery . .

USER celery

# Worker command - concurrency set via env var
CMD ["celery", "-A", "config", "worker", "-l", "INFO"]
```

### Celery Beat (Single Replica)
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN groupadd -r celery && useradd -r -g celery celery

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=celery:celery . .

USER celery

# Beat must be single replica
CMD ["celery", "-A", "config", "beat", "-l", "INFO"]
```

## Multi-Dockerfile Project Structure

```
project/
├── Dockerfile              # Development
├── Dockerfile.web          # Production web
├── Dockerfile.worker       # Production celery worker
├── Dockerfile.beat         # Production celery beat
├── compose.yaml            # Local development
├── compose.prod.yaml       # Production reference
├── .dockerignore
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── celery.py
│   └── wsgi.py
└── requirements/
    ├── base.txt
    ├── local.txt
    └── production.txt
```

## ACR Push Workflow

```bash
# Login to ACR
az acr login --name myacr

# Build and tag for ACR
docker build -f Dockerfile.web -t myacr.azurecr.io/myapp-web:v1.0.0 .
docker build -f Dockerfile.worker -t myacr.azurecr.io/myapp-worker:v1.0.0 .
docker build -f Dockerfile.beat -t myacr.azurecr.io/myapp-beat:v1.0.0 .

# Push to ACR
docker push myacr.azurecr.io/myapp-web:v1.0.0
docker push myacr.azurecr.io/myapp-worker:v1.0.0
docker push myacr.azurecr.io/myapp-beat:v1.0.0
```

## Environment Variables for ACA

### Django Settings
```bash
DJANGO_SETTINGS_MODULE=config.settings.production
SECRET_KEY=<from-keyvault>
ALLOWED_HOSTS=myapp.azurecontainerapps.io
DEBUG=0
```

### Database (Azure PostgreSQL)
```bash
DATABASE_URL=postgres://user:pass@server.postgres.database.azure.com:5432/dbname?sslmode=require
# Or individual vars
POSTGRES_HOST=server.postgres.database.azure.com
POSTGRES_DB=myapp
POSTGRES_USER=admin
POSTGRES_PASSWORD=<from-keyvault>
```

### Celery (Azure Redis Cache)
```bash
CELERY_BROKER_URL=rediss://:password@myredis.redis.cache.windows.net:6380/0?ssl_cert_reqs=required
CELERY_RESULT_BACKEND=rediss://:password@myredis.redis.cache.windows.net:6380/1?ssl_cert_reqs=required
```

## ACA Limitations to Know

| Limitation | Value |
|------------|-------|
| Max image size (Consumption) | 8 GB |
| Max containers per app | 10 (sidecars) |
| OS support | Linux only (linux/amd64) |
| Privileged containers | Not allowed |
| Max replicas | 300 |

## Container App Configuration

### Web App (Ingress Enabled)
- **Ingress**: External
- **Target Port**: 8000
- **Min Replicas**: 1
- **Max Replicas**: 10
- **Scale Rule**: HTTP concurrent requests

### Celery Worker (No Ingress)
- **Ingress**: None
- **Min Replicas**: 1
- **Max Replicas**: 5
- **Scale Rule**: Azure Service Bus queue length (or manual)

### Celery Beat (No Ingress, Single Instance)
- **Ingress**: None
- **Min Replicas**: 1
- **Max Replicas**: 1 (CRITICAL - must be exactly 1)

## Health Check Endpoint

Add to Django:
```python
# urls.py
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "healthy"}, status=200)
    except Exception as e:
        return JsonResponse({"status": "unhealthy", "error": str(e)}, status=500)

urlpatterns = [
    path("health/", health_check, name="health_check"),
    # ... other urls
]
```

## Gunicorn Configuration

### Environment-Based Config
```python
# gunicorn.conf.py
import os

bind = "0.0.0.0:8000"
workers = int(os.getenv("GUNICORN_WORKERS", 4))
threads = int(os.getenv("GUNICORN_THREADS", 2))
worker_class = "sync"
worker_tmp_dir = "/dev/shm"
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
preload_app = True
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOG_LEVEL", "info")
```

### Dockerfile CMD
```dockerfile
CMD ["gunicorn", "--config", "gunicorn.conf.py", "config.wsgi:application"]
```

## Static Files Strategy

For ACA, use external storage:

### Azure Blob Storage
```python
# settings/production.py
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
    },
}
AZURE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT")
AZURE_CONTAINER = "static"
STATIC_URL = f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/static/"
```

### WhiteNoise (Simple Alternative)
```python
# settings/production.py
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # After security
    # ... other middleware
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

## Key Vault Integration

### Reference in ACA Environment Variables
```bash
# Format for Key Vault reference
secretref:mykeyvault/secret-name
```

### Azure CLI Setup
```bash
# Create Key Vault
az keyvault create --name mykeyvault --resource-group mygroup

# Add secret
az keyvault secret set --vault-name mykeyvault --name django-secret-key --value "your-secret"

# Grant ACA access via managed identity
az keyvault set-policy --name mykeyvault \
    --object-id <managed-identity-object-id> \
    --secret-permissions get list
```

## Logging Configuration

### Django Settings for ACA
```python
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("LOG_LEVEL", "INFO"),
    },
}
```

## Local Testing for ACA

Test production config locally:
```yaml
# compose.prod-test.yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.web
    environment:
      - DJANGO_SETTINGS_MODULE=config.settings.production
      - DEBUG=0
      - DATABASE_URL=postgres://postgres:postgres@db:5432/myapp
    depends_on:
      - db
      - redis
    ports:
      - "8000:8000"

  worker:
    build:
      context: .
      dockerfile: Dockerfile.worker
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
    depends_on:
      - redis

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=postgres

  redis:
    image: redis:7-alpine
```
