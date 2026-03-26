# Dockerfile Best Practices (2025)

Reference for Claude Code. Use these patterns for all Dockerfile generation.

## BuildKit Syntax Header

Always include for BuildKit features:
```dockerfile
# syntax=docker/dockerfile:1
```

## Base Image Selection

### Python Applications
```dockerfile
# Production (small, secure)
FROM python:3.11-slim-bookworm

# AI/ML with CUDA (use specific version, not latest)
FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Alpine (smaller but may have compatibility issues)
FROM python:3.11-alpine
```

### Version Pinning Rules
- **ALWAYS** use specific version tags
- **NEVER** use `latest` tag
- Pin to minor version at minimum: `python:3.11-slim` not `python:3-slim`
- For reproducibility, pin to digest: `python:3.11-slim@sha256:abc123...`

## Layer Ordering Principle

Order instructions by change frequency (least → most):
1. Base image and system packages (rarely change)
2. Dependencies/requirements files
3. Dependency installation
4. Application code (changes frequently)
5. Startup commands

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

# 1. System packages (rarely change)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Copy dependency files first
COPY pyproject.toml poetry.lock ./

# 3. Install dependencies
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction

# 4. Copy application code (changes often)
COPY . .

# 5. Startup
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
```

## BuildKit Cache Mounts

Speed up builds by caching package downloads:

### pip Cache
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

### Poetry Cache
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry \
    poetry install --no-interaction
```

### apt Cache
```dockerfile
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update && apt-get install -y package-name
```

## Multi-Stage Builds

### Python Django Example
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

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy wheels from builder
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# Copy application
COPY --chown=appuser:appuser . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
```

### With Poetry
```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11-slim-bookworm AS builder

ENV POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install poetry==$POETRY_VERSION

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/root/.cache/pypoetry \
    poetry install --only=main --no-root

# ============= RUNTIME =============
FROM python:3.11-slim-bookworm AS runtime

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
```

## Security Best Practices

### Non-Root User
```dockerfile
# Create user early, use late
RUN groupadd -r appuser && useradd -r -g appuser appuser

# ... install dependencies as root ...

# Switch to non-root before copying app code
USER appuser
COPY --chown=appuser:appuser . .
```

### Minimal Permissions
```dockerfile
# Set restrictive permissions
RUN chmod -R 755 /app && \
    chmod -R 750 /app/config
```

### No Secrets in Image
```dockerfile
# WRONG - secrets baked into image
ENV DATABASE_PASSWORD=secret123

# CORRECT - use runtime env vars or secrets
# Pass at runtime: docker run -e DATABASE_PASSWORD=secret
```

### BuildKit Secrets (for build-time secrets)
```dockerfile
RUN --mount=type=secret,id=pip_auth,target=/root/.pip/pip.conf \
    pip install -r requirements.txt
```

Build with: `docker build --secret id=pip_auth,src=./pip.conf .`

## Health Checks

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1
```

For Django:
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD python manage.py check --database default || exit 1
```

## Environment Variables

### Standard Python Env Vars
```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
```

### Django Settings
```dockerfile
ENV DJANGO_SETTINGS_MODULE=config.settings.production
```

## .dockerignore Template

```dockerignore
# Git
.git
.gitignore

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.Python
*.egg-info
.eggs
dist
build
*.egg

# Virtual environments
.venv
venv
ENV

# IDE
.idea
.vscode
*.swp

# Testing
.pytest_cache
.coverage
htmlcov
.tox

# Environment files (IMPORTANT: don't include secrets)
.env
.env.*
!.env.example

# Docker
Dockerfile*
docker-compose*
.docker

# Documentation
docs
*.md
!README.md

# Logs
*.log
logs

# Static files (if collected elsewhere)
staticfiles
media

# Node (if mixed project)
node_modules
```

## Common Anti-Patterns to Avoid

### DON'T: Multiple RUN for related commands
```dockerfile
# BAD
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*

# GOOD
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*
```

### DON'T: Copy everything before installing deps
```dockerfile
# BAD - any code change invalidates cache
COPY . .
RUN pip install -r requirements.txt

# GOOD - only requirements copied first
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### DON'T: Use ADD when COPY works
```dockerfile
# BAD - ADD has magic behavior
ADD . .

# GOOD - explicit
COPY . .

# ADD only when needed for extraction or URLs
ADD archive.tar.gz /app/
```

### DON'T: Use shell form for CMD
```dockerfile
# BAD - runs through shell
CMD python app.py

# GOOD - exec form, proper signal handling
CMD ["python", "app.py"]
```

## Labels for Metadata

```dockerfile
LABEL org.opencontainers.image.title="My App" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.vendor="Company" \
      org.opencontainers.image.source="https://github.com/org/repo"
```
