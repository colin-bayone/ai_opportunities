# Azure Common Errors Reference

**Last Updated:** 2026-01-06

This document catalogs common Azure CLI errors and their solutions.

---

## Authentication Errors

### Error: AADSTS700016 - Application not found

**Message:**
```
AADSTS700016: Application with identifier 'xxx' was not found in the directory
```

**Cause:** Service principal doesn't exist or wrong tenant.

**Solution:**
1. Verify tenant ID is correct
2. Verify service principal exists: `az ad sp show --id {app-id}`
3. Re-authenticate: `az login --tenant {tenant-id}`

---

### Error: AADSTS50076 - MFA Required

**Message:**
```
AADSTS50076: Due to a configuration change made by your administrator, you must use multi-factor authentication
```

**Cause:** Conditional Access policy requires MFA.

**Solution:**
1. Use interactive login: `az login`
2. Complete MFA in browser
3. Or use device code flow: `az login --use-device-code`

---

## Resource Errors

### Error: ResourceNotFound

**Message:**
```
(ResourceNotFound) The Resource 'Microsoft.App/containerApps/xxx' was not found
```

**Cause:** Resource doesn't exist or wrong name/resource group.

**Solution:**
1. Verify resource name spelling
2. Verify resource group: `az resource list -g {rg} --query "[].name"`
3. Check if resource was deleted

---

### Error: ResourceGroupNotFound

**Message:**
```
(ResourceGroupNotFound) Resource group 'xxx' could not be found.
```

**Cause:** Resource group doesn't exist.

**Solution:**
1. List resource groups: `az group list --query "[].name"`
2. Check subscription: `az account show`
3. Create if needed: `az group create -n {name} -l {location}`

---

## Network Errors

### Error: PrivateEndpointConnectionNotApproved

**Message:**
```
The private endpoint connection is not approved
```

**Cause:** Private endpoint waiting for manual approval.

**Solution:**
1. Check PE status: `az network private-endpoint show -n {name} -g {rg}`
2. Approve on target resource (Key Vault, Storage, etc.)
3. Or approve via CLI if you have access

---

### Error: SubnetNotFound

**Message:**
```
Subnet 'xxx' not found in virtual network 'yyy'
```

**Cause:** Subnet name incorrect or doesn't exist.

**Solution:**
1. List subnets: `az network vnet subnet list --vnet-name {vnet} -g {rg}`
2. Verify subnet name matches exactly

---

### Error: SubnetIsFull

**Message:**
```
Subnet has no available IP addresses
```

**Cause:** All IPs in subnet CIDR are allocated.

**Solution:**
1. Delete unused resources in subnet
2. Or expand subnet CIDR (may require downtime)
3. Or create new subnet with larger CIDR

---

## Container App Errors

### Error: ContainerAppOperationError - Image Pull Failed

**Message:**
```
Failed to pull image from registry
```

**Cause:** ACR authentication or network issue.

**Solution:**
1. Verify ACR exists: `az acr show -n {acr}`
2. Check managed identity has AcrPull role
3. Verify image tag exists: `az acr repository show-tags -n {acr} --repository {repo}`
4. Check VNet/private endpoint if using private ACR

---

### Error: Container Exited with Code 1

**Message:**
```
Container exited with exit code 1
```

**Cause:** Application crashed on startup.

**Solution:**
1. Check console logs: `az containerapp logs show -n {name} -g {rg} --type console`
2. Check environment variables
3. Verify database connectivity
4. Check if migrations ran

---

## PostgreSQL Errors

### Error: FirewallRuleNotAllowed

**Message:**
```
Cannot create firewall rule. Public network access is disabled
```

**Cause:** Server configured for private access only.

**Solution:**
1. Use private endpoint instead of firewall rules
2. Or enable public access (not recommended for production)

---

### Error: ConnectionRefused

**Message:**
```
connection refused to host xxx on port 5432
```

**Cause:** Network connectivity issue.

**Solution:**
1. Check private endpoint is approved
2. Verify VNet integration
3. Check private DNS zone is linked to VNet
4. Verify container is in same VNet

---

## Redis Errors

### Error: RedisConnectionException

**Message:**
```
Unable to connect to Redis
```

**Cause:** Network or authentication issue.

**Solution:**
1. Verify using correct port (10000 for Enterprise, 6380 for SSL)
2. Check private endpoint status
3. Verify access key from Key Vault
4. Check TLS/SSL settings

---

## Key Vault Errors

### Error: ForbiddenByPolicy

**Message:**
```
Operation is not allowed by the policy
```

**Cause:** Access policy or network ACL blocking access.

**Solution:**
1. Check access policies include your identity
2. Check network ACLs if using private endpoint
3. Verify managed identity has correct permissions

---

### Error: SecretDisabled

**Message:**
```
Secret xxx is currently disabled
```

**Cause:** Secret was disabled.

**Solution:**
1. Enable secret: `az keyvault secret set-attributes --vault-name {vault} -n {secret} --enabled true`

---

## Storage Errors

### Error: AuthorizationPermissionMismatch

**Message:**
```
This request is not authorized to perform this operation
```

**Cause:** RBAC or access key issue.

**Solution:**
1. Check RBAC assignments
2. Verify using `--auth-mode login` for RBAC
3. Or use `--auth-mode key` with valid key

---

## Quota Errors

### Error: QuotaExceeded

**Message:**
```
Operation could not be completed as it results in exceeding quota
```

**Cause:** Subscription quota limit reached.

**Solution:**
1. Check current usage: `az quota usage show`
2. Request quota increase via Azure Portal
3. Or use a different region with available quota

---

## Tips for Debugging

1. **Always check logs first**
   ```bash
   az containerapp logs show -n {name} -g {rg} --type system --tail 100
   ```

2. **Verify resource exists**
   ```bash
   az resource show --ids {resource_id}
   ```

3. **Check provisioning state**
   ```bash
   az resource show --ids {id} --query "properties.provisioningState"
   ```

4. **Activity log for recent errors**
   ```bash
   az monitor activity-log list --resource-group {rg} --start-time {24h_ago}
   ```

5. **Test network connectivity from container**
   ```bash
   az containerapp exec -n {name} -g {rg} --command "nslookup {hostname}"
   ```
