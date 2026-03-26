#!/bin/bash
# get_keyvault_secrets_list.sh - List Key Vault secrets (NAMES ONLY - never values)
# Usage: ./get_keyvault_secrets_list.sh "<keyvault_name>" "<resource_group>" "<session_folder>"
# Example: ./get_keyvault_secrets_list.sh "talent-ai-stage-kv" "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

KEYVAULT_NAME="${1}"
RESOURCE_GROUP="${2}"
SESSION_FOLDER="${3:-.}"

if [ -z "$KEYVAULT_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Key Vault name and resource group required"
    echo "Usage: ./get_keyvault_secrets_list.sh <keyvault_name> <resource_group> [session_folder]"
    exit 1
fi

echo "SECURITY NOTE: This script only exports SECRET NAMES, never actual values."
echo ""
echo "Listing Key Vault secrets for: $KEYVAULT_NAME"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# Key Vault configuration
KV_CONFIG_FILE="$SESSION_FOLDER/exports/keyvault_${KEYVAULT_NAME}_config_${TIMESTAMP}.json"
echo "Fetching Key Vault configuration..."
az keyvault show -n "$KEYVAULT_NAME" -g "$RESOURCE_GROUP" --output json > "$KV_CONFIG_FILE"
echo "  Saved: $KV_CONFIG_FILE"

# Secret names only
SECRETS_FILE="$SESSION_FOLDER/exports/keyvault_${KEYVAULT_NAME}_secret_names_${TIMESTAMP}.json"
echo "Fetching secret names (NOT values)..."
az keyvault secret list --vault-name "$KEYVAULT_NAME" --query "[].{name:name, enabled:attributes.enabled, created:attributes.created, updated:attributes.updated}" --output json > "$SECRETS_FILE"
echo "  Saved: $SECRETS_FILE"

# Access policies
POLICIES_FILE="$SESSION_FOLDER/exports/keyvault_${KEYVAULT_NAME}_policies_${TIMESTAMP}.json"
echo "Fetching access policies..."
az keyvault show -n "$KEYVAULT_NAME" -g "$RESOURCE_GROUP" --query "properties.accessPolicies" --output json > "$POLICIES_FILE"
echo "  Saved: $POLICIES_FILE"

# Network rules
NETWORK_FILE="$SESSION_FOLDER/exports/keyvault_${KEYVAULT_NAME}_network_${TIMESTAMP}.json"
echo "Fetching network configuration..."
az keyvault show -n "$KEYVAULT_NAME" -g "$RESOURCE_GROUP" --query "properties.networkAcls" --output json > "$NETWORK_FILE"
echo "  Saved: $NETWORK_FILE"

# Summary
echo ""
echo "Key Vault Summary:"
echo "=================="

LOCATION=$(cat "$KV_CONFIG_FILE" | grep -o '"location": "[^"]*"' | head -1 | cut -d'"' -f4)
SKU=$(az keyvault show -n "$KEYVAULT_NAME" -g "$RESOURCE_GROUP" --query "properties.sku.name" -o tsv 2>/dev/null || echo "Unknown")
SECRET_COUNT=$(az keyvault secret list --vault-name "$KEYVAULT_NAME" --query "length(@)" -o tsv 2>/dev/null || echo "0")

echo "  Location: $LOCATION"
echo "  SKU: $SKU"
echo "  Secrets Count: $SECRET_COUNT"
echo ""

echo "Secret Names:"
az keyvault secret list --vault-name "$KEYVAULT_NAME" --query "[].name" -o tsv 2>/dev/null | while read name; do
    echo "  - $name"
done

echo ""
echo "NOTE: Secret values are NOT exported for security reasons."
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
