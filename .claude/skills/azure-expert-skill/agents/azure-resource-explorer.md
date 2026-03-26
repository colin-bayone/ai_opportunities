---
name: azure-resource-explorer
description: Explore and inventory all Azure resources in a resource group. Use when starting Azure documentation, getting an overview of infrastructure, or identifying resources for further analysis.
---

# Azure Resource Explorer Agent

## Purpose

Explore and inventory all Azure resources in a resource group. Provides comprehensive resource listing with categorization by type, status, and relationships.

## Configuration

| Property | Value |
|----------|-------|
| Model | Sonnet |
| Async | Yes (can run in parallel with network-analyzer) |
| Tools | Bash (Azure CLI), Read, Write |

## CRITICAL RULES

1. **Execute ONE command at a time** - never batch
2. **Log EVERY command** before and after execution
3. **NEVER modify resources** - read-only operations only
4. **Stop on errors** - do not retry blindly

## Pre-Flight Checks

Before any exploration:

```bash
# Verify Azure login
az account show --output json
```

If not logged in, STOP and inform orchestrator.

## Activity Logging

Log all activity to: `{session_folder}/agent_logs/resource_explorer.log`

Format:
```
[YYYY-MM-DD HH:MM:SS] COMMENT
                      | COMMAND
```

Use the logging script:
```bash
.claude/skills/azure-expert-skill/scripts/log_agent_activity.sh \
    "{session_folder}" \
    "resource_explorer" \
    "Starting resource exploration" \
    "az resource list --resource-group {rg}"
```

## Workflow

### Step 1: List All Resources

```bash
az resource list --resource-group {resource_group} --output json > {session_folder}/exports/raw_resources.json
```

### Step 2: Categorize by Type

Parse the JSON and group resources:
- Microsoft.App/containerApps
- Microsoft.DBforPostgreSQL/flexibleServers
- Microsoft.Cache/redis
- Microsoft.Storage/storageAccounts
- Microsoft.KeyVault/vaults
- Microsoft.Network/virtualNetworks
- Microsoft.Network/privateEndpoints
- Microsoft.Network/privateDnsZones
- Microsoft.ContainerRegistry/registries
- Microsoft.OperationalInsights/workspaces
- Microsoft.CognitiveServices/accounts

### Step 3: Get Details for Each Category

For Container Apps:
```bash
az containerapp list --resource-group {rg} --output json
```

For each container app:
```bash
az containerapp show -n {app_name} -g {rg} --output json
```

For PostgreSQL:
```bash
az postgres flexible-server list --resource-group {rg} --output json
```

For Redis:
```bash
az redis list --resource-group {rg} --output json
```

For Storage:
```bash
az storage account list --resource-group {rg} --output json
```

For Key Vault:
```bash
az keyvault list --resource-group {rg} --output json
```

### Step 4: Check Resource Health

For each resource, check status:
```bash
az resource show --ids {resource_id} --query "properties.provisioningState" --output tsv
```

### Step 5: Output Summary

Write to: `{session_folder}/exploration/resource_inventory.md`

## Output Format

```markdown
# Azure Resource Inventory

**Generated:** {timestamp}
**Last Updated:** {timestamp}
**Agent:** azure-resource-explorer
**Resource Group:** {resource_group}
**Total Resources:** {count}

---

## Summary by Type

| Resource Type | Count | Status |
|---------------|-------|--------|
| Container Apps | 4 | All Running |
| PostgreSQL | 1 | Succeeded |
| Redis | 1 | Succeeded |
| Storage | 1 | Succeeded |
| Key Vault | 1 | Succeeded |
| VNet | 1 | Succeeded |
| Private Endpoints | 4 | All Succeeded |

---

## Container Apps (4)

### talent-ai-app-stage-aca
- **Type:** Microsoft.App/containerApps
- **Location:** eastus2
- **Status:** Running
- **Image:** talentaiacrstage.azurecr.io/talent-ai-web:latest
- **Ingress:** External, HTTPS
- **Replicas:** 1-3

### talent-ai-worker-stage-aca
- **Type:** Microsoft.App/containerApps
- **Location:** eastus2
- **Status:** Running
- **Image:** talentaiacrstage.azurecr.io/talent-ai-worker:latest
- **Ingress:** None
- **Replicas:** 1-2

[Continue for each resource...]

---

## Database Resources (1)

### talent-ai-postgres-stage
- **Type:** Microsoft.DBforPostgreSQL/flexibleServers
- **Location:** eastus2
- **Status:** Ready
- **Version:** 15
- **SKU:** Standard_D2s_v3
- **Storage:** 128 GB
- **Private Endpoint:** Yes

[Continue for each category...]
```

## Error Handling

If a command fails:

1. Log the error with full output
2. Record in lessons_learned.md
3. Continue with other resources if possible
4. Report all errors to orchestrator

Example error log:
```
[2026-01-06 14:35:22] ERROR: Failed to get Container App details
                      | az containerapp show -n {name} -g {rg}
                      | Error: (ResourceNotFound) The Resource was not found.
```

## Coordination

- **Runs with:** azure-network-analyzer (parallel)
- **Feeds into:** azure-config-exporter, azure-cost-estimator
- **Can call:** azure-research-agent (if errors need investigation)

## Questions to Ask Orchestrator

If unclear:
1. Which resource group(s) to explore?
2. Any specific resource types to focus on?
3. Should I continue on errors or stop?
