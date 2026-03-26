# BuildKit Features Reference (2025)

Reference for Claude Code. BuildKit is default in Docker 23.0+.

## Enabling BuildKit

### Check Status
```bash
docker info | grep -i buildkit
# Or check version
docker version --format '{{.Server.Version}}'
```

### Enable Methods

#### Docker Desktop (Windows/macOS)
Enabled by default. Verify in Settings → Docker Engine.

#### Linux / WSL2
```bash
# Environment variable (session)
export DOCKER_BUILDKIT=1

# Permanent in daemon.json
# /etc/docker/daemon.json
{
  "features": {
    "buildkit": true
  }
}
```

#### Per-command
```bash
DOCKER_BUILDKIT=1 docker build .
```

#### Docker Compose
```bash
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose build
```

## Syntax Directive

Always include at the top of Dockerfile:
```dockerfile
# syntax=docker/dockerfile:1
```

This enables latest stable syntax features. For specific version:
```dockerfile
# syntax=docker/dockerfile:1.7
```

## Cache Mounts

Persist package manager caches between builds.

### pip
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

### Poetry
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/pypoetry \
    poetry install
```

### apt-get
```dockerfile
# Must disable auto-clean first
RUN rm -f /etc/apt/apt.conf.d/docker-clean

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update && apt-get install -y package-name
```

### npm
```dockerfile
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

### Cache Mount Parameters
```dockerfile
RUN --mount=type=cache,target=/path,\
    id=unique-id,\           # Share cache across stages
    sharing=shared,\         # locked|shared|private
    mode=0755,\              # Permissions
    uid=1000,\               # Owner UID
    gid=1000 \               # Owner GID
    command here
```

## Secret Mounts

Safely use secrets during build without embedding in image.

### Usage
```dockerfile
# Mount secret file
RUN --mount=type=secret,id=mysecret,target=/run/secrets/mysecret \
    cat /run/secrets/mysecret

# As environment variable
RUN --mount=type=secret,id=api_key \
    export API_KEY=$(cat /run/secrets/api_key) && \
    curl -H "Authorization: Bearer $API_KEY" https://api.example.com
```

### Build Command
```bash
docker build --secret id=mysecret,src=./secret.txt .

# From environment
docker build --secret id=api_key,env=API_KEY .
```

### pip with Private Registry
```dockerfile
RUN --mount=type=secret,id=pip_conf,target=/root/.pip/pip.conf \
    pip install -r requirements.txt
```

## SSH Mounts

Forward SSH agent for git operations.

### Usage
```dockerfile
RUN --mount=type=ssh \
    git clone git@github.com:org/private-repo.git
```

### Build Command
```bash
# Forward default SSH agent
docker build --ssh default .

# Specific key
docker build --ssh default=$HOME/.ssh/id_rsa .
```

### Known Hosts
```dockerfile
RUN --mount=type=ssh \
    mkdir -p ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts && \
    git clone git@github.com:org/repo.git
```

## Bind Mounts

Mount files/directories during build.

### Read-only (default)
```dockerfile
RUN --mount=type=bind,source=./data,target=/data \
    process_data /data
```

### From Another Stage
```dockerfile
FROM builder AS data-processor
RUN generate_data > /output/data.json

FROM runtime
RUN --mount=type=bind,from=data-processor,source=/output,target=/data \
    import_data /data/data.json
```

## Tmpfs Mounts

Temporary filesystem for build operations.

```dockerfile
RUN --mount=type=tmpfs,target=/tmp \
    process_with_temp_files
```

## Multi-Stage Build Features

### Named Stages
```dockerfile
FROM python:3.11-slim AS builder
# build stuff

FROM python:3.11-slim AS tester
# test stuff

FROM python:3.11-slim AS production
COPY --from=builder /app/dist /app
```

### Build Specific Stage
```bash
docker build --target builder -t myapp:builder .
docker build --target production -t myapp:latest .
```

### Parallel Building
BuildKit automatically parallelizes independent stages:
```dockerfile
FROM alpine AS stage1
RUN sleep 10 && echo "stage1"

FROM alpine AS stage2
RUN sleep 10 && echo "stage2"

FROM alpine AS final
COPY --from=stage1 /result1 /
COPY --from=stage2 /result2 /
# stage1 and stage2 build in parallel
```

## Heredocs

Multi-line scripts without escaping:

### Basic Heredoc
```dockerfile
RUN <<EOF
apt-get update
apt-get install -y curl
rm -rf /var/lib/apt/lists/*
EOF
```

### With Interpreter
```dockerfile
RUN <<EOF python
import os
print(os.environ.get('HOME'))
EOF
```

### File Creation
```dockerfile
COPY <<EOF /app/config.py
DEBUG = False
SECRET_KEY = 'changeme'
EOF
```

### Multiple Files
```dockerfile
COPY <<config.py <<requirements.txt
DEBUG = True
config.py
flask==2.0
gunicorn==20.0
requirements.txt
```

## Build Arguments

### Declaration and Usage
```dockerfile
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim

ARG BUILD_ENV=production
RUN if [ "$BUILD_ENV" = "development" ]; then \
        pip install pytest; \
    fi
```

### Build Command
```bash
docker build --build-arg PYTHON_VERSION=3.12 --build-arg BUILD_ENV=development .
```

### Predefined ARGs
Available without declaration:
- `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`
- `FTP_PROXY`, `ALL_PROXY`
- `TARGETPLATFORM`, `TARGETOS`, `TARGETARCH`
- `BUILDPLATFORM`, `BUILDOS`, `BUILDARCH`

## Output Options

### Progress Styles
```bash
docker build --progress=auto .    # Default
docker build --progress=plain .   # Full output (CI friendly)
docker build --progress=tty .     # Interactive
```

### Export Types
```bash
# Local tar
docker build --output type=local,dest=./output .

# OCI tar
docker build --output type=oci,dest=./image.tar .

# Direct to registry
docker build --output type=registry .
```

## Remote Cache

### Pull Cache from Registry
```bash
docker build \
  --cache-from type=registry,ref=myregistry/myapp:cache \
  -t myapp:latest .
```

### Push Cache to Registry
```bash
docker build \
  --cache-to type=registry,ref=myregistry/myapp:cache,mode=max \
  --push \
  -t myregistry/myapp:latest .
```

### In Compose
```yaml
services:
  web:
    build:
      context: .
      cache_from:
        - type=registry,ref=myregistry/myapp:cache
      cache_to:
        - type=registry,ref=myregistry/myapp:cache,mode=max
```

## Compression Options

### zstd (faster, better compression)
```bash
docker build --output type=image,compression=zstd .
```

Available: `gzip` (default), `zstd`, `estargz`, `uncompressed`

## Buildx for Multi-Platform

### Setup
```bash
# Create builder
docker buildx create --name multiplatform --use

# Inspect
docker buildx inspect --bootstrap
```

### Build Multi-Platform
```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --push \
  -t myregistry/myapp:latest .
```

### Platform-Specific Logic in Dockerfile
```dockerfile
ARG TARGETARCH

RUN case ${TARGETARCH} in \
        amd64) ARCH="x86_64" ;; \
        arm64) ARCH="aarch64" ;; \
    esac && \
    curl -O https://example.com/binary-${ARCH}
```

## Debugging Builds

### Inspect Build Cache
```bash
docker builder prune --all --dry-run
docker buildx du
```

### Debug Failed Build
```bash
# Get shell in failed stage
docker build --target failed-stage .
docker run -it <image-id> /bin/sh
```

### Verbose Output
```bash
docker build --progress=plain --no-cache .
```
