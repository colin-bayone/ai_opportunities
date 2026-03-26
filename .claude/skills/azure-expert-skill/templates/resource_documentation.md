# {Resource Name} Configuration

**Generated:** {YYYY-MM-DD HH:MM:SS}
**Last Updated:** {YYYY-MM-DD HH:MM:SS}
**Agent:** azure-config-exporter
**Session:** {session_folder_name}
**Format:** Markdown

---

## Overview

| Property | Value |
|----------|-------|
| **Name** | {resource_name} |
| **Type** | {resource_type} |
| **Resource Group** | {resource_group} |
| **Location** | {location} |
| **Subscription** | {subscription_name} |
| **Resource ID** | {resource_id} |

---

## Status

| Property | Value |
|----------|-------|
| **Provisioning State** | {Succeeded/Failed/InProgress} |
| **Runtime Status** | {Running/Stopped/etc} |
| **Last Modified** | {timestamp} |

---

## Configuration

### Basic Settings

| Setting | Value | Description |
|---------|-------|-------------|
| {setting_name} | {value} | {description} |

### Advanced Settings

{Detailed configuration based on resource type}

---

## Scaling Configuration

| Property | Value |
|----------|-------|
| **Min Instances** | {min} |
| **Max Instances** | {max} |
| **Scale Rules** | {rules} |

---

## Network Configuration

| Property | Value |
|----------|-------|
| **VNet Integration** | {Yes/No} |
| **Subnet** | {subnet_name or N/A} |
| **Private Endpoint** | {Yes/No} |
| **Public Access** | {Enabled/Disabled} |

---

## Security

### Authentication

| Property | Value |
|----------|-------|
| **Auth Type** | {System Managed Identity/User Assigned/etc} |
| **Identity** | {identity_name or N/A} |

### Secrets (Names Only)

| Secret Name | Source | Description |
|-------------|--------|-------------|
| {secret_name} | Key Vault | {description} |

**Note:** Secret values are NOT included for security.

---

## Environment Variables

| Name | Value/Source | Sensitive |
|------|--------------|-----------|
| {env_name} | {value or "Secret Reference"} | {Yes/No} |

---

## Dependencies

### Depends On

| Resource | Type | Purpose |
|----------|------|---------|
| {resource_name} | {type} | {why it's needed} |

### Depended By

| Resource | Type | Purpose |
|----------|------|---------|
| {resource_name} | {type} | {why it depends on this} |

---

## Tags

| Tag | Value |
|-----|-------|
| {tag_key} | {tag_value} |

---

## For Production Deployment

To recreate this resource in production:

1. **Naming:** Update `{stage}` to `{prod}` in resource name
2. **Resource Group:** Use production resource group
3. **VNet:** Reference production VNet/subnet
4. **Key Vault:** Reference production Key Vault secrets
5. **Scaling:** Review and adjust for production load
6. **Monitoring:** Ensure alerts are configured

### Key Differences for Production

| Setting | Stage Value | Recommended Prod Value |
|---------|-------------|----------------------|
| {setting} | {stage_value} | {prod_recommendation} |

---

## Raw Export Location

Full JSON export available at:
`{session_folder}/exports/{resource_type}_{resource_name}_{timestamp}.json`

---

## Appendix

### CLI Commands Used

```bash
# Get full configuration
az {service} show -n {name} -g {rg} --output json

# Additional commands...
```

### Generation Notes

- {Any notes about how this document was generated}
- {Any caveats or limitations}
