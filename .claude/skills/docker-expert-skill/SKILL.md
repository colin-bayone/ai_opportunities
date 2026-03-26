---
name: docker-expert-skill
description: Modern Docker development and deployment expert (2025). Use for all Docker-related tasks including Dockerfile creation, docker compose configuration, BuildKit optimization, image analysis, troubleshooting, and Azure Container Apps deployment. Covers Django, Celery, AI/ML workloads, and modern ETL stacks. Always uses modern syntax (docker compose v2, BuildKit, no deprecated patterns).
---

# Docker Expert Skill

Expert Docker assistance with 2025 best practices. Supports Django, Celery, AI/ML, and Azure Container Apps deployment.

## Core Principles

1. **Always use modern syntax**: `docker compose` (space), not `docker-compose` (hyphen)
2. **No `version:` key** in compose files - obsolete in Compose v2
3. **Never use `latest` tag** - always pin specific versions
4. **Prefer BuildKit** - explain benefits when introducing features
5. **Environment variables over hardcoding** - search for .env files, ask which to use
6. **Non-destructive by default** - always confirm before destructive operations
7. **Narrate actions** - explain what each command does before executing
8. **Check Python version** from pyproject.toml/Poetry when creating Dockerfiles

## Workflow

### Before Any Docker Task

1. Run diagnostics to understand the current environment:
```bash
python .claude/skills/docker-expert-skill/scripts/docker_diagnostics.py
```

2. Check for existing Docker files:
```bash
ls -la Dockerfile* compose* docker-compose* .dockerignore 2>/dev/null
```

3. If creating Dockerfiles for Python projects, check version requirements:
```bash
python .claude/skills/docker-expert-skill/scripts/check_python_version.py
```

4. Search for .env files and ASK user which one to use:
```bash
ls -la .env* 2>/dev/null
```

## Reference Documents

Load these based on task type:

| Task | Reference |
|------|-----------|
| Docker commands | `.claude/skills/docker-expert-skill/references/COMMANDS.md` |
| Dockerfile creation | `.claude/skills/docker-expert-skill/references/DOCKERFILE.md` |
| Compose files | `.claude/skills/docker-expert-skill/references/COMPOSE.md` |
| BuildKit features | `.claude/skills/docker-expert-skill/references/BUILDKIT.md` |
| Azure deployment | `.claude/skills/docker-expert-skill/references/AZURE.md` |
| Celery containers | `.claude/skills/docker-expert-skill/references/CELERY.md` |

## Common Workflows

### Creating a New Dockerfile

1. Check Python version requirements in project
2. Read `.claude/skills/docker-expert-skill/references/DOCKERFILE.md`
3. Determine if multi-stage build needed (production = yes)
4. Ask about base image preferences if not obvious
5. Include BuildKit syntax header: `# syntax=docker/dockerfile:1`
6. Use cache mounts for pip/poetry
7. Create non-root user for security
8. Add health check

### Creating Compose File

1. Read `.claude/skills/docker-expert-skill/references/COMPOSE.md`
2. Search for .env files, ask which to use
3. NO `version:` key
4. Use variable substitution for all configurable values
5. Add health checks with conditions in depends_on
6. Use profiles for optional services (e.g., flower)

### Troubleshooting

1. Run diagnostics first
2. Check logs: `docker compose logs -f service_name`
3. Inspect container: `docker compose exec service_name bash`
4. Check resource usage: `docker stats`
5. Perform thorough RCA - don't simplify without consent
6. Document findings

### Image Optimization

1. Analyze current image:
```bash
python .claude/skills/docker-expert-skill/scripts/image_analyzer.py image:tag
```

2. Read `.claude/skills/docker-expert-skill/references/DOCKERFILE.md` and `.claude/skills/docker-expert-skill/references/BUILDKIT.md`
3. Apply multi-stage builds
4. Use cache mounts
5. Order layers by change frequency
6. Compare before/after sizes

## Environment Variables Strategy

**Always use environment variables for:**
- Passwords and secrets
- Database connection strings
- Ports
- Feature flags
- Service URLs

**Search for .env files first:**
```bash
find . -maxdepth 2 -name ".env*" -type f 2>/dev/null
```

**Then ask which file to use** - never assume.

## Safety Rules

### NEVER Execute Without Confirmation:
- `docker system prune`
- `docker volume prune`
- `docker image prune -a`
- `docker compose down -v`
- Any command with `--force` or `-f` that removes data
- Removing or replacing running containers in production

### Always Confirm Before:
- Rebuilding images (may take time)
- Scaling services
- Changing network configuration
- Modifying volumes

## Scratchpad Usage

Create helper scripts in `.claude/docker/scratchpad/`:
```bash
mkdir -p .claude/docker/scratchpad
```

Use for:
- Complex diagnostic commands
- Multi-step operations
- Reusable utilities

Keep this directory in `.gitignore`.

## Todo List Management

Maintain a todo list for complex tasks:
```bash
# Create/append to todo
echo "[ ] Task description" >> .claude/docker/scratchpad/TODO.md

# Mark complete
sed -i 's/\[ \] Task/[x] Task/' .claude/docker/scratchpad/TODO.md
```

## BuildKit Explanation (When Introducing)

When suggesting BuildKit features, briefly explain:

> BuildKit is Docker's modern build engine (default since Docker 23.0). It offers:
> - **Parallel builds** for faster multi-stage builds
> - **Cache mounts** to persist package downloads between builds
> - **Secret mounts** for secure credential handling
> - **Better caching** with content-addressed layers
>
> Enable with `DOCKER_BUILDKIT=1` if not default, or add `# syntax=docker/dockerfile:1` to Dockerfile.
>
> Want me to explain more about any specific feature?

## Legacy Syntax Corrections

When encountering legacy patterns, gently correct:

| Legacy | Modern | Note |
|--------|--------|------|
| `docker-compose` | `docker compose` | Compose v2 |
| `version: "3.8"` | (remove entirely) | Obsolete |
| `docker build` | `docker build` or `docker buildx build` | BuildKit auto-enabled |
| `links:` | `depends_on:` + networks | Deprecated |
| `container_name:` with replicas | Remove for scaling | Conflicts with scaling |

## Error Handling

When errors occur:
1. Capture full error output
2. Check logs for context
3. Research root cause thoroughly
4. DO NOT simplify without user consent
5. Propose specific fixes with explanations
6. Test fix in isolation if possible

## Subagent Triggers

Suggest specialized research when:
- User asks "why" about Docker behavior → offer to research
- Encountering unfamiliar error patterns → offer deep dive
- Comparing approaches → offer pros/cons analysis
- Version compatibility questions → offer to check latest docs
