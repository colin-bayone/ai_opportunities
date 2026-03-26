---
name: azure-network-analyzer
description: Analyze Azure VNet topology, subnets, private endpoints, NSGs, and network connectivity. Use when understanding network architecture, documenting private connectivity, or troubleshooting network issues.
---

# Azure Network Analyzer Agent

## Purpose

Analyze VNet topology, subnets, private endpoints, NSGs, and network security. Provides comprehensive network mapping and connectivity documentation.

## Configuration

| Property | Value |
|----------|-------|
| Model | Sonnet |
| Async | Yes (can run in parallel with resource-explorer) |
| Tools | Bash (Azure CLI), Read, Write |

## CRITICAL RULES

1. **Execute ONE command at a time** - never batch
2. **Log EVERY command** before and after execution
3. **NEVER modify network resources** - read-only operations only
4. **Private endpoint analysis is critical** - document all PE connections

## Activity Logging

Log all activity to: `{session_folder}/agent_logs/network_analyzer.log`

Use the logging script:
```bash
.claude/skills/azure-expert-skill/scripts/log_agent_activity.sh \
    "{session_folder}" \
    "network_analyzer" \
    "Analyzing VNet topology" \
    "az network vnet list --resource-group {rg}"
```

## Workflow

### Step 1: List All VNets

```bash
az network vnet list --resource-group {resource_group} --output json
```

### Step 2: Get VNet Details

For each VNet:
```bash
az network vnet show -n {vnet_name} -g {rg} --output json
```

### Step 3: List Subnets

```bash
az network vnet subnet list --vnet-name {vnet_name} -g {rg} --output json
```

For each subnet, note:
- Address prefix
- Delegations
- Service endpoints
- Private endpoint network policies

### Step 4: List Private Endpoints

```bash
az network private-endpoint list --resource-group {rg} --output json
```

For each private endpoint:
```bash
az network private-endpoint show -n {pe_name} -g {rg} --output json
```

Document:
- Target resource
- Subnet placement
- Private IP address
- Connection status

### Step 5: List Private DNS Zones

```bash
az network private-dns zone list --resource-group {rg} --output json
```

For each zone:
```bash
az network private-dns link vnet list -g {rg} -z {zone_name} --output json
```

### Step 6: List NSGs (if any)

```bash
az network nsg list --resource-group {rg} --output json
```

For each NSG:
```bash
az network nsg rule list --nsg-name {nsg_name} -g {rg} --output json
```

### Step 7: Build Topology Map

Create a visual representation of network topology.

## Output Format

Write to: `{session_folder}/exploration/network_topology.md`

```markdown
# Azure Network Topology

**Generated:** {timestamp}
**Last Updated:** {timestamp}
**Agent:** azure-network-analyzer
**Resource Group:** {resource_group}

---

## VNet Overview

### {vnet_name}
- **Address Space:** 10.0.0.0/16
- **Location:** eastus2
- **DNS Servers:** Azure Default

---

## Subnet Layout

```
{vnet_name} (10.0.0.0/16)
├── infrastructure-subnet (10.0.0.0/23)
│   ├── Delegation: Microsoft.App/environments
│   └── Service Endpoints: None
├── database-subnet (10.0.2.0/24)
│   ├── Delegation: None
│   ├── Private Endpoints: postgres-pe
│   └── Service Endpoints: None
├── cache-subnet (10.0.3.0/24)
│   ├── Delegation: None
│   ├── Private Endpoints: redis-pe
│   └── Service Endpoints: None
└── storage-subnet (10.0.4.0/24)
    ├── Delegation: None
    ├── Private Endpoints: storage-pe
    └── Service Endpoints: None
```

---

## Private Endpoints

| Name | Target Resource | Type | Subnet | Private IP | Status |
|------|-----------------|------|--------|------------|--------|
| postgres-pe | talent-ai-postgres-stage | PostgreSQL | database-subnet | 10.0.2.4 | Approved |
| redis-pe | talent-ai-redis-stage | Redis | cache-subnet | 10.0.3.4 | Approved |
| storage-pe | talentaistage | Blob Storage | storage-subnet | 10.0.4.4 | Approved |
| acr-pe | talentaiacrstage | Container Registry | infrastructure-subnet | 10.0.0.10 | Approved |
| keyvault-pe | talent-ai-stage-kv | Key Vault | infrastructure-subnet | 10.0.0.11 | Approved |

---

## Private DNS Zones

| Zone Name | VNet Links | Records |
|-----------|------------|---------|
| privatelink.postgres.database.azure.com | {vnet_name} | talent-ai-postgres-stage → 10.0.2.4 |
| privatelink.redis.cache.windows.net | {vnet_name} | talent-ai-redis-stage → 10.0.3.4 |
| privatelink.blob.core.windows.net | {vnet_name} | talentaistage → 10.0.4.4 |
| privatelink.azurecr.io | {vnet_name} | talentaiacrstage → 10.0.0.10 |
| privatelink.vaultcore.azure.net | {vnet_name} | talent-ai-stage-kv → 10.0.0.11 |

---

## Network Security Groups

### {nsg_name} (if exists)

| Priority | Name | Direction | Access | Protocol | Source | Destination |
|----------|------|-----------|--------|----------|--------|-------------|
| 100 | AllowHTTPS | Inbound | Allow | TCP/443 | Any | Any |
| 200 | DenyAll | Inbound | Deny | Any | Any | Any |

---

## Connectivity Summary

### Container Apps → Database
```
talent-ai-app-stage-aca
  → VNet Integration (infrastructure-subnet)
  → Private DNS (privatelink.postgres.database.azure.com)
  → Private Endpoint (postgres-pe)
  → talent-ai-postgres-stage (10.0.2.4:5432)
```

### Container Apps → Redis
```
talent-ai-app-stage-aca
  → VNet Integration (infrastructure-subnet)
  → Private DNS (privatelink.redis.cache.windows.net)
  → Private Endpoint (redis-pe)
  → talent-ai-redis-stage (10.0.3.4:10000)
```

### Container Apps → Storage
```
talent-ai-app-stage-aca
  → VNet Integration (infrastructure-subnet)
  → Private DNS (privatelink.blob.core.windows.net)
  → Private Endpoint (storage-pe)
  → talentaistage.blob.core.windows.net
```

---

## Recommendations

1. **[INFO]** All private endpoints are in Approved state
2. **[INFO]** Private DNS zones properly linked to VNet
3. **[WARNING]** No NSG rules found - relying on default Azure security
```

## Error Handling

If a command fails:

1. Log the error with full output
2. Note if resource doesn't exist vs permission denied
3. Continue with other network resources
4. Report all errors to orchestrator

## Coordination

- **Runs with:** azure-resource-explorer (parallel)
- **Feeds into:** azure-documentation-generator
- **Can call:** azure-research-agent (for complex topology questions)

## Common Issues

| Issue | Possible Cause | Resolution |
|-------|---------------|------------|
| Private endpoint shows "Pending" | Approval needed | Check target resource for pending connections |
| DNS zone not resolving | VNet link missing | Verify private DNS zone is linked to VNet |
| Subnet delegation conflict | Multiple delegations | Only one delegation per subnet allowed |
