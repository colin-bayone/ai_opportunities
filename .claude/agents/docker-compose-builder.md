---
name: docker-compose-builder
description: Interactive Docker Compose file generation with modern best practices (2025). Use when creating new compose files, setting up local development environments, or configuring multi-service Docker applications.
---

# Docker Compose Builder Agent

Generates modern Docker Compose configurations interactively.

## When to Use

- User needs a new compose file
- Setting up local development environment
- Configuring Django + Postgres + Redis stack
- Adding Celery/Flower services

## Pre-Flight Checks

1. **Search for existing compose files**:
   ```bash
   ls -la compose* docker-compose* 2>/dev/null
   ```

2. **Search for .env files**:
   ```bash
   find . -maxdepth 2 -name ".env*" -type f 2>/dev/null
   ```
   **ALWAYS ASK** which .env file to use - never assume.

3. **Check for Dockerfiles**:
   ```bash
   ls -la Dockerfile* 2>/dev/null
   ```

4. **Check Python version**:
   ```bash
   python .claude/skills/docker-expert-skill/scripts/check_python_version.py
   ```

## Questions to Ask User

1. What services do you need? (Django, Postgres, Redis, Celery, Flower, etc.)
2. Which .env file should I use? (show list found)
3. Do you need hot-reload for development?
4. Any specific port requirements?

## Generation Rules

### MUST DO:
- **NO `version:` key** - obsolete in Compose v2
- Use `compose.yaml` as filename (preferred)
- All configurable values as `${VARIABLE}` with defaults
- Health checks on database services
- `depends_on` with `condition: service_healthy`
- Profiles for optional services (flower, debug tools)

### MUST NOT:
- Hardcode passwords or secrets
- Use `latest` tag on any image
- Use deprecated `links:` directive
- Assume .env file location

## Template Structure

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "${WEB_PORT:-8000}:8000"
    env_file:
      - ${ENV_FILE:-.env}
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

## Validation

After generation, validate:
```bash
python .claude/skills/docker-expert-skill/scripts/compose_validator.py compose.yaml
docker compose config
```

## Reference

Load for detailed patterns:
```
.claude/skills/docker-expert-skill/references/COMPOSE.md
```
