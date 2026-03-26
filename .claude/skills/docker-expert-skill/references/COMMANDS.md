# Docker Commands Reference (2025)

Quick reference for Claude Code. Modern syntax preferred.

## Critical: Use Modern CLI Syntax

```bash
# CORRECT (Compose v2 - use this)
docker compose up
docker compose down
docker compose build
docker compose logs

# WRONG (deprecated Compose v1)
docker-compose up    # DO NOT USE
```

## Docker Build Commands

### Standard Build
```bash
docker build -t image:tag .
docker build -t image:tag -f Dockerfile.prod .
```

### BuildKit Build (Preferred)
```bash
# Enable BuildKit (default in Docker 23.0+)
DOCKER_BUILDKIT=1 docker build -t image:tag .

# With progress output
docker build --progress=plain -t image:tag .

# No cache (fresh build)
docker build --no-cache -t image:tag .

# Target specific stage
docker build --target production -t image:tag .
```

### Buildx (Multi-platform)
```bash
# Create builder
docker buildx create --name mybuilder --use

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t image:tag .

# Push while building
docker buildx build --push -t registry/image:tag .
```

## Docker Compose Commands

### Core Commands
```bash
docker compose up              # Start services
docker compose up -d           # Start detached
docker compose up --build      # Rebuild before start
docker compose down            # Stop and remove
docker compose down -v         # Also remove volumes
docker compose stop            # Stop without removing
docker compose restart         # Restart services
```

### Build Commands
```bash
docker compose build                    # Build all services
docker compose build --no-cache         # Fresh build
docker compose build --parallel         # Parallel build
docker compose build service_name       # Build specific service
```

### Logs and Debugging
```bash
docker compose logs              # All logs
docker compose logs -f           # Follow logs
docker compose logs service_name # Specific service
docker compose ps                # List containers
docker compose top               # Running processes
docker compose config            # Validate compose file
docker compose config --no-env-resolution  # Show raw config
```

### Exec and Run
```bash
docker compose exec service_name bash      # Shell into running
docker compose run service_name command    # Run one-off command
docker compose run --rm service_name bash  # Remove after exit
```

### Scaling
```bash
docker compose up --scale worker=3    # Scale service
```

## Container Management

### Running Containers
```bash
docker run -d --name name image:tag           # Detached
docker run -it --rm image:tag bash            # Interactive, auto-remove
docker run -p 8000:8000 image:tag             # Port mapping
docker run -v $(pwd):/app image:tag           # Volume mount
docker run --env-file .env image:tag          # Environment file
docker run -e VAR=value image:tag             # Single env var
```

### Container Operations
```bash
docker exec -it container_name bash           # Shell access
docker logs container_name                    # View logs
docker logs -f --tail 100 container_name      # Follow last 100
docker stop container_name                    # Graceful stop
docker kill container_name                    # Force stop
docker rm container_name                      # Remove container
docker rm -f container_name                   # Force remove
```

## Image Management

### Listing
```bash
docker images                     # List images
docker images -a                  # Include intermediates
docker image ls --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

### Analysis
```bash
docker history image:tag          # Layer history
docker inspect image:tag          # Full metadata
docker image inspect image:tag --format='{{.Size}}'
```

### Cleanup
```bash
docker image prune               # Remove dangling
docker image prune -a            # Remove all unused
docker system prune              # Remove all unused data
docker system prune -a --volumes # Full cleanup (DESTRUCTIVE)
```

## Registry Commands

### Docker Hub
```bash
docker login
docker push image:tag
docker pull image:tag
docker tag source:tag target:tag
```

### Azure Container Registry
```bash
az acr login --name registryname
docker tag image:tag registryname.azurecr.io/image:tag
docker push registryname.azurecr.io/image:tag
```

### GitHub Container Registry
```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
docker tag image:tag ghcr.io/owner/image:tag
docker push ghcr.io/owner/image:tag
```

## Volume and Network Commands

### Volumes
```bash
docker volume ls                  # List volumes
docker volume create myvolume     # Create volume
docker volume rm myvolume         # Remove volume
docker volume prune               # Remove unused
```

### Networks
```bash
docker network ls                 # List networks
docker network create mynetwork   # Create network
docker network inspect mynetwork  # Inspect network
docker network prune              # Remove unused
```

## Diagnostic Commands

### System Info
```bash
docker version                    # Docker version
docker info                       # System-wide info
docker system df                  # Disk usage
docker system events              # Real-time events
```

### Container Stats
```bash
docker stats                      # Live resource usage
docker stats container_name       # Specific container
docker top container_name         # Running processes
```

### BuildKit Cache
```bash
docker builder prune              # Clear build cache
docker builder prune -a           # Clear all cache
docker buildx du                  # Cache disk usage
```

## Environment Variable Patterns

### Compose File
```yaml
services:
  web:
    env_file:
      - .env
      - .env.local
    environment:
      - DEBUG=${DEBUG:-false}
      - DATABASE_URL
```

### CLI Patterns
```bash
# Multiple env files
docker compose --env-file .env --env-file .env.local up

# Override file
docker compose -f compose.yaml -f compose.override.yaml up
```

## Important Notes

1. **Always use `docker compose` (space)** - not `docker-compose` (hyphen)
2. **Remove `version:` from compose files** - obsolete in Compose v2
3. **BuildKit is default in Docker 23.0+** - no need to enable manually
4. **Use specific image tags** - never use `latest` in production
5. **Prefer `--rm` for one-off runs** - prevents container accumulation
