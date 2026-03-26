# Docker Expert Skill - Installation & Usage

## Installation

### Skill Files
Copy the skill folder to your Claude skills directory:

```bash
# Copy skill to Claude Code skills location
cp -r docker-skill ~/.claude/skills/docker-expert-skill

# Or for project-specific
cp -r docker-skill /path/to/your/project/.claude/skills/docker-expert-skill
```

### Agent Files
Copy individual agent files to your Claude agents directory:

```bash
# Copy agents to Claude Code agents location
cp docker-skill/agents/*.md ~/.claude/agents/

# Or for project-specific
cp docker-skill/agents/*.md /path/to/your/project/.claude/agents/
```

### Create Scratchpad Directory
```bash
mkdir -p .claude/docker/scratchpad
echo ".claude/" >> .gitignore
```

## Expected Directory Structure (Claude Code)

```
your-project/
├── .claude/
│   ├── skills/
│   │   └── docker-expert-skill/
│   │       ├── SKILL.md
│   │       ├── references/
│   │       │   ├── COMMANDS.md
│   │       │   ├── DOCKERFILE.md
│   │       │   ├── COMPOSE.md
│   │       │   ├── BUILDKIT.md
│   │       │   ├── AZURE.md
│   │       │   └── CELERY.md
│   │       └── scripts/
│   │           ├── docker_diagnostics.py
│   │           ├── image_analyzer.py
│   │           ├── check_python_version.py
│   │           └── compose_validator.py
│   ├── agents/
│   │   ├── docker-diagnostics.md
│   │   ├── docker-compose-builder.md
│   │   ├── dockerfile-optimizer.md
│   │   ├── azure-container-prep.md
│   │   └── docker-explainer.md
│   └── docker/
│       └── scratchpad/
│           └── (ephemeral scripts & todo lists)
└── ... your project files
```

## Key Features

### Modern Docker Syntax (2025)
- Uses `docker compose` (v2) not `docker-compose` (v1)
- No `version:` key in compose files
- BuildKit features (cache mounts, secrets, heredocs)
- Specific image tags (never `latest`)

### Django/Celery Stack Support
- Multi-stage Dockerfiles
- Separate containers for web, worker, beat
- Local dev with hot-reload
- Production with Gunicorn

### Azure Container Apps Ready
- Production Dockerfile patterns
- ACR push workflows
- Health check endpoints
- Key Vault integration patterns

### Safety First
- Never destructive without confirmation
- Always narrates actions before execution
- Thorough RCA before simplification
- Environment variable discovery

## Subagents

1. **docker-diagnostics**: Environment health checks
2. **docker-compose-builder**: Interactive compose file generation
3. **dockerfile-optimizer**: Image size and build optimization
4. **azure-container-prep**: Production deployment preparation
5. **docker-explainer**: Research and explain Docker concepts

## Usage Examples

### "Create a compose file for Django with Postgres and Redis"
→ Triggers docker-compose-builder subagent

### "Why is my Docker image 2GB?"
→ Triggers dockerfile-optimizer subagent

### "Prepare this project for Azure Container Apps"
→ Triggers azure-container-prep subagent

### "What's the difference between COPY and ADD?"
→ Triggers docker-explainer subagent

## Scratchpad Location

The skill creates helper scripts in:
```
.claude/docker/scratchpad/
```

Add this to your `.gitignore`:
```
.claude/
```

## Environment Variables

The skill will:
1. Search for `.env*` files in project root
2. ASK which file to use (never assumes)
3. Use variable substitution in all generated files

## Related to Your Projects

Given your work on TalentAI and Issue #385, this skill is particularly useful for:
- Continuing Docker optimization for the 1.14GB production image
- Setting up Celery containers for the resume processing pipeline
- Deploying to Azure Container Apps with Presidio, spaCy, and PDF processing
