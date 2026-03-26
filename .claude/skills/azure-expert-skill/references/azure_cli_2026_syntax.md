# Azure CLI 2026 Syntax Reference

**Last Updated:** 2026-01-06
**Source:** [Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/)

---

## Modern Azure CLI Best Practices

### Always Use

1. **`az` commands (not `azure`)**
   - `az resource list` (correct)
   - `azure resource list` (deprecated)

2. **JSON output for scripts**
   ```bash
   az resource list --output json
   ```

3. **JMESPath queries for filtering**
   ```bash
   az containerapp list --query "[?name.contains(@, 'stage')]"
   ```

4. **`@-` for piping IDs**
   ```bash
   az vm list --query "[].id" -o tsv | az vm start --ids @-
   ```

5. **`--no-wait` for async operations**
   ```bash
   az containerapp create ... --no-wait
   ```

### Avoid

1. **Deprecated `--repo` flag** - work from repo directory
2. **JSON blobs as arguments** - use `@file.json` syntax
3. **`docker-compose` (hyphenated)** - use `docker compose`

---

## Container Apps Commands

### List all Container Apps
```bash
az containerapp list --resource-group {rg} --output json
```

### Show Container App details
```bash
az containerapp show -n {name} -g {rg} --output json
```

### Get logs
```bash
# System logs
az containerapp logs show -n {name} -g {rg} --type system --tail 100

# Console logs (app output)
az containerapp logs show -n {name} -g {rg} --type console --tail 100
```

### Get replicas
```bash
az containerapp replica list -n {name} -g {rg} --output table
```

### Execute command in container
```bash
az containerapp exec -n {name} -g {rg} --command "/bin/bash"
```

### Update image
```bash
az containerapp update -n {name} -g {rg} --image {acr}.azurecr.io/{image}:{tag}
```

---

## PostgreSQL Flexible Server Commands

### Show server
```bash
az postgres flexible-server show -n {name} -g {rg} --output json
```

### List databases
```bash
az postgres flexible-server db list -g {rg} -s {name} --output json
```

### List firewall rules
```bash
az postgres flexible-server firewall-rule list -g {rg} -s {name}
```

### Check connectivity
```bash
az postgres flexible-server show-connection-string -s {name}
```

---

## Redis Commands

### Show cache
```bash
az redis show -n {name} -g {rg} --output json
```

### List firewall rules
```bash
az redis firewall-rules list -n {name} -g {rg} --output json
```

### Note: Azure Managed Redis uses port 10000 (not 6379)

---

## Network Commands

### List VNets
```bash
az network vnet list --resource-group {rg} --output json
```

### Show VNet details
```bash
az network vnet show -n {name} -g {rg} --output json
```

### List subnets
```bash
az network vnet subnet list --vnet-name {vnet} -g {rg} --output json
```

### List private endpoints
```bash
az network private-endpoint list --resource-group {rg} --output json
```

### Show private endpoint
```bash
az network private-endpoint show -n {name} -g {rg} --output json
```

### List private DNS zones
```bash
az network private-dns zone list --resource-group {rg} --output json
```

---

## Storage Commands

### Show account
```bash
az storage account show -n {name} -g {rg} --output json
```

### List containers
```bash
az storage container list --account-name {name} --auth-mode login --output json
```

### Network rules
```bash
az storage account network-rule list -n {name} -g {rg} --output json
```

---

## Key Vault Commands

### Show vault
```bash
az keyvault show -n {name} -g {rg} --output json
```

### List secrets (NAMES ONLY)
```bash
az keyvault secret list --vault-name {name} --query "[].name" --output json
```

### Get access policies
```bash
az keyvault show -n {name} -g {rg} --query "properties.accessPolicies"
```

---

## Resource Group Commands

### List all resources
```bash
az resource list --resource-group {rg} --output json
```

### Export ARM template
```bash
az group export --name {rg} --output json > template.json
```

### Show resource
```bash
az resource show --ids {resource_id} --output json
```

---

## Output Formats

| Format | Use Case |
|--------|----------|
| `--output json` | Scripts, parsing |
| `--output table` | Human readable |
| `--output tsv` | Piping to other commands |
| `--output yaml` | Configuration files |
| `--output none` | Suppress output |

---

## JMESPath Query Examples

### Filter by name
```bash
--query "[?name=='myapp']"
```

### Select specific fields
```bash
--query "[].{Name:name, Location:location}"
```

### Filter and select
```bash
--query "[?provisioningState=='Succeeded'].name"
```

### Count items
```bash
--query "length(@)"
```

---

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `AZURE_CONFIG_DIR` | Isolate config for concurrent scripts |
| `AZURE_DEFAULTS_GROUP` | Default resource group |
| `AZURE_DEFAULTS_LOCATION` | Default region |

---

## Common Gotchas

1. **Container Apps in Consumption plan** have no persistent storage
2. **PostgreSQL Flexible Server** private access requires VNet integration
3. **Redis Enterprise** uses port 10000, not 6379
4. **Key Vault** soft-delete is enabled by default (90 days retention)
5. **Private endpoints** can take several minutes for DNS propagation
