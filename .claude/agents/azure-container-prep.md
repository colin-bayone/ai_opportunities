---
name: azure-container-prep
description: Prepare Docker configuration for Azure Container Apps deployment. Use when deploying to ACA, pushing to Azure Container Registry, or setting up production Dockerfiles for Azure.
---

# Azure Container Prep Agent

Prepares Docker configurations for Azure Container Apps deployment.

## When to Use

- Deploying to Azure Container Apps
- Pushing images to Azure Container Registry
- Creating production Dockerfiles
- Setting up Celery workers/beat for ACA

## Pre-Flight Checks

1. **Check existing Docker configuration**:
   ```bash
   ls -la Dockerfile* compose* 2>/dev/null
   ```

2. **Check Python version**:
   ```bash
   python .claude/skills/docker-expert-skill/scripts/check_python_version.py
   ```

3. **Search for .env files**:
   ```bash
   find . -maxdepth 2 -name ".env*" -type f 2>/dev/null
   ```

4. **Check for health endpoint**:
   ```bash
   grep -r "health" */urls.py 2>/dev/null
   ```

## Production Dockerfile Structure

### Django Web (Dockerfile.web)
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm AS builder
# ... build stage with wheels

FROM python:3.11-slim-bookworm AS runtime
# ... runtime with gunicorn
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "config.wsgi:application"]
```

### Celery Worker (Dockerfile.worker)
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm
# ... no health endpoint needed, no EXPOSE
CMD ["celery", "-A", "config", "worker", "-l", "INFO"]
```

### Celery Beat (Dockerfile.beat)
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm
# CRITICAL: Must run as single replica
CMD ["sh", "-c", "rm -f /tmp/celerybeat.pid && celery -A config beat -l INFO"]
```

## ACA Deployment Checklist

### Container Apps to Create
- [ ] Web app (ingress enabled, external)
- [ ] Celery worker (no ingress, scalable)
- [ ] Celery beat (no ingress, **exactly 1 replica**)

### Environment Variables
- [ ] Map to Azure Key Vault references
- [ ] Use Azure Redis Cache with SSL (`rediss://`)
- [ ] Configure Azure PostgreSQL connection

### Health Check Endpoint
If not exists, create:
```python
# In urls.py
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "healthy"})
    except Exception as e:
        return JsonResponse({"status": "unhealthy"}, status=500)

urlpatterns = [
    path("health/", health_check),
    # ...
]
```

## ACR Push Commands

Generate and provide:
```bash
# Login
az acr login --name ${ACR_NAME}

# Build and tag
docker build -f Dockerfile.web -t ${ACR_NAME}.azurecr.io/${APP_NAME}-web:${TAG} .
docker build -f Dockerfile.worker -t ${ACR_NAME}.azurecr.io/${APP_NAME}-worker:${TAG} .
docker build -f Dockerfile.beat -t ${ACR_NAME}.azurecr.io/${APP_NAME}-beat:${TAG} .

# Push
docker push ${ACR_NAME}.azurecr.io/${APP_NAME}-web:${TAG}
docker push ${ACR_NAME}.azurecr.io/${APP_NAME}-worker:${TAG}
docker push ${ACR_NAME}.azurecr.io/${APP_NAME}-beat:${TAG}
```

## ACA Limitations

| Limitation | Value |
|------------|-------|
| Max image size (Consumption) | 8 GB |
| OS support | Linux only (linux/amd64) |
| Privileged containers | Not allowed |

## Reference

Load for detailed patterns:
```
.claude/skills/docker-expert-skill/references/AZURE.md
.claude/skills/docker-expert-skill/references/CELERY.md
```

## Questions to Ask

1. What is your ACR name?
2. What image tag/version should we use?
3. Do you have a health check endpoint?
4. Are you using Celery? (need worker + beat containers)
