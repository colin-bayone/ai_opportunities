# Docker Compose Reference (2025)

Reference for Claude Code. Use Compose v2 syntax exclusively.

## File Naming

Preferred names (in order of detection):
1. `compose.yaml` (preferred)
2. `compose.yml`
3. `docker-compose.yaml`
4. `docker-compose.yml`

Override files:
- `compose.override.yaml` - auto-loaded in development
- `compose.prod.yaml` - explicit production override

## Critical: No Version Key

```yaml
# WRONG - version is obsolete
version: "3.8"
services:
  ...

# CORRECT - no version needed
services:
  ...
```

## Django Development Stack Template

```yaml
# compose.yaml - Local development
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
    ports:
      - "${WEB_PORT:-8000}:8000"
    env_file:
      - .env
    environment:
      - DEBUG=1
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    ports:
      - "${DB_PORT:-5432}:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    ports:
      - "${REDIS_PORT:-6379}:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  flower:
    build:
      context: .
      dockerfile: Dockerfile.dev
    command: celery -A config flower --port=5555
    volumes:
      - .:/app
    ports:
      - "${FLOWER_PORT:-5555}:5555"
    env_file:
      - .env
    depends_on:
      - redis
    profiles:
      - celery

volumes:
  postgres_data:
  redis_data:
  static_volume:
```

## Production Compose Template

```yaml
# compose.prod.yaml
services:
  web:
    image: ${REGISTRY}/web:${TAG:-latest}
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4
    expose:
      - "8000"
    env_file:
      - .env.prod
    environment:
      - DEBUG=0
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      replicas: 2
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
    restart: always

  celery_worker:
    image: ${REGISTRY}/web:${TAG:-latest}
    command: celery -A config worker -l INFO -c 2
    env_file:
      - .env.prod
    depends_on:
      - redis
    deploy:
      replicas: 2
      resources:
        limits:
          memory: 512M
    restart: always

  celery_beat:
    image: ${REGISTRY}/web:${TAG:-latest}
    command: celery -A config beat -l INFO
    env_file:
      - .env.prod
    depends_on:
      - redis
    deploy:
      replicas: 1
    restart: always
```

## Service Configuration Patterns

### Build Configuration

```yaml
services:
  web:
    # Simple build
    build: .
    
    # Full build config
    build:
      context: .
      dockerfile: Dockerfile.prod
      target: production
      args:
        PYTHON_VERSION: "3.11"
      cache_from:
        - type=registry,ref=myregistry/myapp:cache
      cache_to:
        - type=registry,ref=myregistry/myapp:cache,mode=max
```

### Volume Mounts

```yaml
services:
  web:
    volumes:
      # Named volume
      - postgres_data:/var/lib/postgresql/data
      
      # Bind mount (development)
      - .:/app
      
      # Read-only bind mount
      - ./config:/app/config:ro
      
      # Anonymous volume (preserves container data)
      - /app/node_modules
```

### Port Mapping

```yaml
services:
  web:
    # Variable port
    ports:
      - "${WEB_PORT:-8000}:8000"
    
    # Internal only (for reverse proxy)
    expose:
      - "8000"
```

### Dependency Management

```yaml
services:
  web:
    depends_on:
      # Simple dependency
      - redis
      
      # With health check condition
      db:
        condition: service_healthy
      
      # Wait for completion (init containers)
      migrate:
        condition: service_completed_successfully
```

### Health Checks

```yaml
services:
  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Resource Limits

```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 512M
        reservations:
          cpus: "0.25"
          memory: 256M
```

## Environment Variables

### Priority Order (highest to lowest)
1. CLI: `docker compose run -e VAR=value`
2. Shell environment
3. Environment file (env_file)
4. Dockerfile ENV

### Configuration Patterns

```yaml
services:
  web:
    # Load from file
    env_file:
      - .env
      - .env.local
    
    # Override or add specific vars
    environment:
      - DEBUG=${DEBUG:-false}
      - DATABASE_URL
      - SECRET_KEY  # Uses shell value
```

### Variable Substitution

```yaml
services:
  web:
    image: myapp:${TAG:-latest}
    ports:
      - "${PORT:-8000}:8000"
    environment:
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
```

## Profiles

Selectively enable services:

```yaml
services:
  web:
    # Always runs
    build: .

  flower:
    build: .
    profiles:
      - celery
      - monitoring

  debug:
    build: .
    profiles:
      - debug
```

```bash
# Run default services
docker compose up

# Include celery profile
docker compose --profile celery up

# Multiple profiles
docker compose --profile celery --profile monitoring up
```

## Network Configuration

```yaml
services:
  web:
    networks:
      - frontend
      - backend

  db:
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # No external access
```

## Secrets (Development Pattern)

```yaml
services:
  web:
    secrets:
      - db_password
      - api_key

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    environment: API_KEY
```

## Extension Fields (DRY)

```yaml
x-common-env: &common-env
  DEBUG: "${DEBUG:-false}"
  LOG_LEVEL: "${LOG_LEVEL:-INFO}"

x-healthcheck: &healthcheck
  interval: 30s
  timeout: 10s
  retries: 3

services:
  web:
    environment:
      <<: *common-env
      WEB_SPECIFIC: "value"
    healthcheck:
      <<: *healthcheck
      test: ["CMD", "curl", "-f", "http://localhost:8000/health/"]

  worker:
    environment:
      <<: *common-env
      WORKER_SPECIFIC: "value"
```

## Useful Commands Quick Reference

```bash
# Development
docker compose up              # Start
docker compose up -d           # Detached
docker compose up --build      # Rebuild
docker compose logs -f web     # Follow logs
docker compose exec web bash   # Shell access
docker compose down            # Stop

# With profiles
docker compose --profile celery up

# With override file
docker compose -f compose.yaml -f compose.prod.yaml up

# Scaling (use with stateless services)
docker compose up --scale worker=3

# Validation
docker compose config                    # Full resolved config
docker compose config --services         # List services
docker compose config --no-env-resolution # Raw config
```

## Anti-Patterns to Avoid

### DON'T: Hardcode values that should be env vars
```yaml
# BAD
environment:
  - POSTGRES_PASSWORD=mysecretpassword

# GOOD
environment:
  - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

### DON'T: Use latest tag
```yaml
# BAD
image: postgres:latest

# GOOD
image: postgres:16-alpine
```

### DON'T: Mix build and image
```yaml
# BAD - confusing
services:
  web:
    build: .
    image: myapp:latest  # Only use for tagging builds

# GOOD - clear intent
services:
  web:
    build:
      context: .
      tags:
        - myapp:latest
```

### DON'T: Forget depends_on conditions
```yaml
# BAD - might start before DB ready
depends_on:
  - db

# GOOD - waits for healthy
depends_on:
  db:
    condition: service_healthy
```
