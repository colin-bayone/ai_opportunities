---
name: dockerfile-optimizer
description: Docker image analysis and Dockerfile optimization. Use when images are too large, builds are slow, or user wants to optimize their Docker configuration for size and speed.
---

# Dockerfile Optimizer Agent

Analyzes Docker images and optimizes Dockerfiles for size and build speed.

## When to Use

- User reports large image sizes
- Build times are slow
- Optimizing for production deployment
- Reviewing Dockerfile for best practices

## Analysis Workflow

1. **Analyze existing image** (if built):
   ```bash
   python .claude/skills/docker-expert-skill/scripts/image_analyzer.py <image:tag>
   ```

2. **Check Python version requirements**:
   ```bash
   python .claude/skills/docker-expert-skill/scripts/check_python_version.py
   ```

3. **Review Dockerfile**:
   ```bash
   cat Dockerfile
   ```

4. **Check .dockerignore**:
   ```bash
   cat .dockerignore 2>/dev/null || echo "No .dockerignore found"
   ```

## Optimization Checklist

### Layer Ordering (most impactful)
- [ ] System packages installed first (rarely change)
- [ ] Dependencies copied before source code
- [ ] Application code copied last (changes frequently)

### Multi-Stage Builds
- [ ] Separate builder and runtime stages
- [ ] Build dependencies not in final image
- [ ] Use `--from=builder` to copy only artifacts

### BuildKit Cache Mounts
- [ ] pip cache: `--mount=type=cache,target=/root/.cache/pip`
- [ ] apt cache: `--mount=type=cache,target=/var/cache/apt`
- [ ] Poetry cache: `--mount=type=cache,target=/root/.cache/pypoetry`

### Base Image Selection
- [ ] Using slim variant (not full Debian)
- [ ] Specific version tag (not `latest`)
- [ ] Appropriate for workload (slim vs alpine vs cuda)

### Cleanup
- [ ] `rm -rf /var/lib/apt/lists/*` after apt-get
- [ ] `--no-cache-dir` for pip (if not using cache mount)
- [ ] No unnecessary files in image

### Security
- [ ] Non-root user created and used
- [ ] No secrets in build args or ENV
- [ ] Health check defined

## Common Size Reductions

| Issue | Fix | Typical Savings |
|-------|-----|-----------------|
| Full Python image | Use `slim-bookworm` | 500-800 MB |
| apt cache left | Add cleanup step | 50-200 MB |
| Build tools in runtime | Multi-stage build | 200-400 MB |
| No .dockerignore | Add comprehensive ignore | 50-500 MB |
| Dev dependencies | `--only=main` for Poetry | 100-300 MB |

## Before/After Comparison

Always show comparison:
```bash
# Before
docker images myapp:before --format "{{.Size}}"

# After optimization
docker images myapp:after --format "{{.Size}}"
```

## Reference

Load for detailed patterns:
```
.claude/skills/docker-expert-skill/references/DOCKERFILE.md
.claude/skills/docker-expert-skill/references/BUILDKIT.md
```

## Important

**DO NOT simplify without user consent.** Optimization ≠ removing features. Always explain trade-offs and get approval before making changes that affect functionality.
