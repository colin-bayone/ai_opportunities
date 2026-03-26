---
name: docker-diagnostics
description: Comprehensive Docker environment analysis and health checking. Use when checking Docker setup, troubleshooting issues, or verifying the environment is working properly.
---

# Docker Diagnostics Agent

Performs comprehensive Docker environment analysis.

## When to Use

- User asks to check Docker setup
- Troubleshooting Docker issues
- Verifying environment before starting work
- User reports Docker errors or unexpected behavior

## Workflow

1. **Run diagnostics script**:
   ```bash
   python .claude/skills/docker-expert-skill/scripts/docker_diagnostics.py
   ```

2. **Check Docker/Compose versions**:
   ```bash
   docker version
   docker compose version
   ```

3. **Verify BuildKit status**:
   ```bash
   docker info | grep -i buildkit
   ```

4. **List running containers**:
   ```bash
   docker ps
   docker compose ps
   ```

5. **Check disk usage**:
   ```bash
   docker system df
   ```

6. **Validate compose file** (if present):
   ```bash
   python .claude/skills/docker-expert-skill/scripts/compose_validator.py
   ```

## Report Format

Provide summary of:
- Docker Engine version
- Docker Compose version (confirm v2)
- BuildKit enabled/disabled
- Running containers count
- Disk usage (images, containers, volumes)
- Any compose file issues found

## Red Flags to Highlight

- Docker Compose v1 (hyphenated `docker-compose`)
- BuildKit not enabled
- Dangling images consuming space
- Containers in unhealthy state
- Compose file with deprecated `version:` key

## Follow-up Actions

After diagnostics, offer:
- Fix any issues found
- Run dockerfile-optimizer if image issues
- Run docker-compose-builder if no compose file
