# Celery Docker Patterns Reference

Reference for Claude Code. Celery containerization best practices.

---

## TalentAI Project Architecture (IMPORTANT)

**In the TalentAI project, Celery does NOT run in Docker containers for local development.**

| Component | Location | Started By |
|-----------|----------|------------|
| Celery Worker | Local (host) | `run.py` (background process) |
| Celery Beat | Local (host) | `run.py` (background process) |
| Redis | Docker | `docker-compose.yml` |
| Flower | Docker (optional) | `--profile flower` |

**For TalentAI-specific Celery documentation, see:** `docs/CELERY_AND_FLOWER_GUIDE.md`

The patterns below are **generic Docker best practices** for reference when containerizing Celery in production or other projects.

---

## Core Principle: Separate Containers

**ALWAYS** run Celery components in separate containers:
- Django/Flask web app
- Celery worker(s)
- Celery beat (EXACTLY 1 replica)
- Flower (optional monitoring)

**NEVER** use `-B` flag in production (embeds beat in worker).

## Local Development Compose

```yaml
# compose.yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started

  db:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Flower only when needed (profile)
  flower:
    build: .
    command: celery -A config flower --port=5555
    volumes:
      - .:/app
    ports:
      - "5555:5555"
    env_file:
      - .env
    depends_on:
      - redis
    profiles:
      - celery

volumes:
  postgres_data:
```

## Note: Local Celery Workers (TalentAI)

**TalentAI uses `run.py` to automatically start Celery worker and beat as local host processes.**

```bash
# TalentAI local development
poetry run python run.py
# Celery worker and beat start automatically when prompted
# Logs: logs/celery-worker.log and logs/celery-beat.log
```

For full details, see `docs/CELERY_AND_FLOWER_GUIDE.md`.

**Generic pattern for other projects:**

```bash
#!/bin/bash
# start_celery.sh - Run in separate terminal

# Start worker
celery -A config worker -l INFO &

# Start beat
celery -A config beat -l INFO &

# Wait for all background jobs
wait
```

## Production Compose (Reference)

```yaml
# compose.prod.yaml
services:
  web:
    image: ${REGISTRY}/app:${TAG}
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
    env_file:
      - .env.prod
    expose:
      - "8000"
    depends_on:
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      replicas: 2

  celery_worker:
    image: ${REGISTRY}/app:${TAG}
    command: celery -A config worker -l INFO -c ${CELERY_CONCURRENCY:-4}
    env_file:
      - .env.prod
    depends_on:
      - redis
    deploy:
      replicas: 2
      resources:
        limits:
          memory: 512M

  celery_beat:
    image: ${REGISTRY}/app:${TAG}
    command: celery -A config beat -l INFO --pidfile=/tmp/celerybeat.pid
    env_file:
      - .env.prod
    depends_on:
      - redis
    deploy:
      replicas: 1  # CRITICAL: Must be exactly 1

  flower:
    image: ${REGISTRY}/app:${TAG}
    command: celery -A config flower --port=5555
    env_file:
      - .env.prod
    ports:
      - "5555:5555"
    depends_on:
      - redis
    profiles:
      - monitoring
```

## Dedicated Dockerfiles

### Dockerfile.worker
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create celery user
RUN groupadd -r celery && useradd -r -g celery celery

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=celery:celery . .

USER celery

# Default concurrency via env var
ENV CELERY_CONCURRENCY=4

CMD ["sh", "-c", "celery -A config worker -l INFO -c ${CELERY_CONCURRENCY}"]
```

### Dockerfile.beat
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r celery && useradd -r -g celery celery

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=celery:celery . .

USER celery

# Remove stale PID file on start
CMD ["sh", "-c", "rm -f /tmp/celerybeat.pid && celery -A config beat -l INFO --pidfile=/tmp/celerybeat.pid"]
```

## Entrypoint Scripts

### Worker Entrypoint
```bash
#!/bin/bash
# entrypoint-worker.sh
set -e

# Wait for dependencies
echo "Waiting for Redis..."
while ! nc -z ${REDIS_HOST:-redis} ${REDIS_PORT:-6379}; do
    sleep 1
done
echo "Redis ready!"

echo "Waiting for PostgreSQL..."
while ! nc -z ${DB_HOST:-db} ${DB_PORT:-5432}; do
    sleep 1
done
echo "PostgreSQL ready!"

exec celery -A config worker -l ${LOG_LEVEL:-INFO} -c ${CELERY_CONCURRENCY:-4}
```

### Beat Entrypoint
```bash
#!/bin/bash
# entrypoint-beat.sh
set -e

# Remove stale PID file
rm -f /tmp/celerybeat.pid

# Wait for Redis
while ! nc -z ${REDIS_HOST:-redis} ${REDIS_PORT:-6379}; do
    sleep 1
done

exec celery -A config beat -l ${LOG_LEVEL:-INFO} --pidfile=/tmp/celerybeat.pid
```

## Environment Variables

### Required
```bash
# Broker
CELERY_BROKER_URL=redis://redis:6379/0

# Result backend (optional but recommended)
CELERY_RESULT_BACKEND=redis://redis:6379/1
```

### Optional Configuration
```bash
# Worker settings
CELERY_CONCURRENCY=4
CELERY_PREFETCH_MULTIPLIER=4
CELERY_MAX_TASKS_PER_CHILD=1000

# Task settings
CELERY_TASK_ACKS_LATE=true
CELERY_TASK_REJECT_ON_WORKER_LOST=true

# Beat settings (database scheduler)
CELERY_BEAT_SCHEDULER=django_celery_beat.schedulers:DatabaseScheduler

# Logging
LOG_LEVEL=INFO
```

## Django Celery Configuration

```python
# config/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

```python
# config/settings/base.py
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_WORKER_HIJACK_ROOT_LOGGER = False

# Beat schedule
CELERY_BEAT_SCHEDULE = {
    "example-task": {
        "task": "myapp.tasks.example_task",
        "schedule": 60.0,  # Every 60 seconds
    },
}
```

## Health Checks for Celery

### Worker Health Check
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD celery -A config inspect ping -d celery@$HOSTNAME || exit 1
```

### Beat Health Check (file-based)
```dockerfile
# Beat writes heartbeat file
HEALTHCHECK --interval=60s --timeout=10s --retries=3 \
    CMD test $(find /tmp/celerybeat-heartbeat -mmin -2 2>/dev/null) || exit 1
```

Beat task to write heartbeat:
```python
@app.task
def celery_beat_heartbeat():
    Path("/tmp/celerybeat-heartbeat").touch()
```

## Scaling Patterns

### Horizontal Scaling (Compose)
```bash
docker compose up --scale celery_worker=4
```

### Queue-Based Scaling
```yaml
services:
  worker_default:
    image: myapp:latest
    command: celery -A config worker -Q default -c 4

  worker_high_priority:
    image: myapp:latest
    command: celery -A config worker -Q high_priority -c 2

  worker_cpu_intensive:
    image: myapp:latest
    command: celery -A config worker -Q cpu_intensive -c 1
    deploy:
      resources:
        limits:
          cpus: "2.0"
```

## Common Issues

### PID File Errors
```bash
# Beat: "celerybeat.pid already exists"
# Solution: Remove on startup
rm -f /tmp/celerybeat.pid
```

### Worker Already Running
```bash
# Check for zombie processes
celery -A config status
celery -A config inspect active
```

### Tasks Running Multiple Times
- **Cause**: Multiple beat instances
- **Solution**: Ensure beat replicas = 1

### Memory Leaks
```python
# config/settings.py
CELERY_WORKER_MAX_TASKS_PER_CHILD = 1000  # Restart worker after N tasks
```

## Monitoring with Flower

```yaml
flower:
  image: mher/flower:2.0
  command: celery --broker=${CELERY_BROKER_URL} flower --port=5555
  ports:
    - "5555:5555"
  environment:
    - CELERY_BROKER_URL=${CELERY_BROKER_URL}
    - FLOWER_BASIC_AUTH=${FLOWER_USER}:${FLOWER_PASSWORD}
```

## Azure Redis Cache Configuration

```bash
# SSL required for Azure Redis
CELERY_BROKER_URL=rediss://:password@myredis.redis.cache.windows.net:6380/0?ssl_cert_reqs=required
CELERY_RESULT_BACKEND=rediss://:password@myredis.redis.cache.windows.net:6380/1?ssl_cert_reqs=required

# Connection pool settings for Azure
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP=true
CELERY_BROKER_CONNECTION_MAX_RETRIES=10
```
