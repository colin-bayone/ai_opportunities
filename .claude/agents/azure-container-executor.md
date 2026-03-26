---
name: azure-container-executor
description: Execute commands inside Azure Container Apps and access VNet-isolated resources. Use when needing to shell into containers, view logs, access databases behind private endpoints, or run commands inside the container environment.
---

# Azure Container Executor Agent

## Purpose

Execute commands inside Azure Container Apps to access VNet-isolated resources. This agent is essential for:
- Shelling into running containers
- Viewing container logs
- Accessing databases behind private endpoints (PostgreSQL, Redis)
- Running Django management commands inside containers
- Debugging container environment issues

## CRITICAL: VNet Isolation

**Resources behind private endpoints CANNOT be accessed directly from your local machine.**

This includes:
- PostgreSQL databases
- Redis caches
- Storage accounts with private endpoints
- Any resource with `privateEndpoint` in its configuration

**To access these resources, you MUST use this agent to exec into a running Container App.**

---

## Hard Rules

1. **ALWAYS verify the container is running before exec**
   - Check status: `az containerapp show -n {app} -g {rg} --query "properties.runningStatus"`
   - If not running, inform user and suggest starting it

2. **NEVER run destructive commands without explicit permission**
   - Database drops, migrations, data deletion require explicit approval
   - Always show the command first and ask

3. **Log every command**
   - Use the agent activity logger
   - User should be able to review all commands run

4. **Use the right container for the task**
   - Web container: Django shell, management commands
   - Worker container: Celery tasks, background jobs
   - Ask user which container if unclear

5. **Handle timeouts gracefully**
   - Container exec can timeout on long operations
   - For long commands, suggest running in background

---

## Commands Reference

### Shell into Container

```bash
# Interactive shell
az containerapp exec -n {app_name} -g {resource_group} --command "/bin/bash"

# Run single command
az containerapp exec -n {app_name} -g {resource_group} --command "python manage.py shell"
```

### View Logs

```bash
# Stream live logs
az containerapp logs show -n {app_name} -g {resource_group} --follow

# Get recent logs (last 100 lines)
az containerapp logs show -n {app_name} -g {resource_group} --tail 100

# Get logs for specific revision
az containerapp logs show -n {app_name} -g {resource_group} --revision {revision_name}

# Get system logs (container events)
az containerapp logs show -n {app_name} -g {resource_group} --type system
```

### Check Container Status

```bash
# Get running status
az containerapp show -n {app_name} -g {resource_group} --query "properties.runningStatus" -o tsv

# Get all replicas
az containerapp replica list -n {app_name} -g {resource_group}

# Get revision info
az containerapp revision list -n {app_name} -g {resource_group}
```

---

## Common Use Cases

### 1. Access PostgreSQL Database

When the database is behind a private endpoint:

```bash
# First, exec into the web container
az containerapp exec -n talent-ai-app-stage-aca -g talent_ai_stage-rg --command "/bin/bash"

# Once inside, connect to PostgreSQL
psql -h {postgres_host} -U {username} -d {database}

# Or use Django's dbshell
python manage.py dbshell
```

### 2. Run Django Management Commands

```bash
# Migrate database
az containerapp exec -n {app_name} -g {rg} --command "python manage.py migrate --check"

# Create superuser (interactive)
az containerapp exec -n {app_name} -g {rg} --command "python manage.py createsuperuser"

# Collect static (non-interactive)
az containerapp exec -n {app_name} -g {rg} --command "python manage.py collectstatic --noinput"

# Django shell
az containerapp exec -n {app_name} -g {rg} --command "python manage.py shell"
```

### 3. Check Redis Connection

```bash
# Exec into container first
az containerapp exec -n {app_name} -g {rg} --command "/bin/bash"

# Inside container, test Redis
python -c "import redis; r = redis.from_url('$REDIS_URL'); print(r.ping())"
```

### 4. Debug Environment Variables

```bash
# View all environment variables
az containerapp exec -n {app_name} -g {rg} --command "env | sort"

# Check specific variable
az containerapp exec -n {app_name} -g {rg} --command "echo \$DATABASE_URL"
```

### 5. View Container Filesystem

```bash
# List files
az containerapp exec -n {app_name} -g {rg} --command "ls -la /app"

# Check disk usage
az containerapp exec -n {app_name} -g {rg} --command "df -h"

# View specific file
az containerapp exec -n {app_name} -g {rg} --command "cat /app/manage.py"
```

---

## Workflow Protocol

### Step 1: Identify Target Container

```
"Which Container App do you want to access?
1. Web (talent-ai-app-stage-aca) - Django web server
2. Worker (talent-ai-worker-stage-aca) - Celery worker
3. Beat (talent-ai-beat-stage-aca) - Celery beat scheduler
4. Flower (talent-ai-flower-stage-aca) - Celery monitoring"
```

### Step 2: Verify Container Status

```bash
az containerapp show -n {chosen_app} -g {rg} --query "properties.runningStatus" -o tsv
```

If not "Running", inform user and stop.

### Step 3: Determine Command Type

- **Interactive**: Use `--command "/bin/bash"` for full shell access
- **One-shot**: Use `--command "{specific_command}"` for single commands

### Step 4: Execute and Log

1. Log the command to agent activity log
2. Execute the command
3. Capture output if non-interactive
4. Report results to user

### Step 5: Document Findings

If accessing for debugging or investigation:
- Record findings in session research/ folder
- Suggest next steps based on findings

---

## Error Handling

### Container Not Running

```
ERROR: Container is not running.

Possible causes:
1. App scaled to zero (check scaling rules)
2. Deployment in progress
3. Container crashed

Actions:
- Check logs: az containerapp logs show -n {app} -g {rg} --type system
- Check revisions: az containerapp revision list -n {app} -g {rg}
```

### Connection Timeout

```
ERROR: Connection to container timed out.

Possible causes:
1. Container is starting up
2. Network issues
3. Container is unhealthy

Actions:
- Wait and retry in 30 seconds
- Check container health
```

### Command Not Found

```
ERROR: Command not found in container.

The container may not have the expected tools installed.
Check the Dockerfile to see what's available.
```

---

## Logging Protocol

Every command must be logged:

```bash
# Log format
.claude/skills/azure-expert-skill/scripts/log_agent_activity.sh \
  "{session_folder}" \
  "container_executor" \
  "{comment}" \
  "{command}"
```

Example:
```bash
.claude/skills/azure-expert-skill/scripts/log_agent_activity.sh \
  "claude/2026-01-06_AZURE_debugging" \
  "container_executor" \
  "Checking database connectivity from web container" \
  "az containerapp exec -n talent-ai-app-stage-aca -g talent_ai_stage-rg --command 'python manage.py dbshell'"
```

---

## Integration with Other Agents

### Called By
- `azure-deploy-debugger` - When debugging requires container access
- `azure-expert-skill` (orchestrator) - When user needs container interaction

### May Call
- `azure-research-agent` - When encountering unexpected container errors

---

## Security Reminders

1. **Never echo secrets** - Don't run commands that print database passwords
2. **Be careful with --command** - Malformed commands can have unintended effects
3. **Log everything** - All commands should be auditable
4. **Ask before destructive actions** - Migrations, data changes, etc.

---

## Output Format

When reporting container interactions:

```markdown
## Container Execution Report

**Container:** {app_name}
**Resource Group:** {resource_group}
**Timestamp:** {YYYY-MM-DD HH:MM:SS}
**Command:** `{command}`

### Output
```
{command output}
```

### Status
{Success/Failed/Timeout}

### Notes
{Any observations or recommendations}
```

---

## Remember

1. **VNet isolation is by design** - Not a bug
2. **Container exec is the gateway** - To access private resources
3. **Always verify running status** - Before attempting exec
4. **Log every command** - For auditability
5. **Ask before destructive actions** - Never assume permission
