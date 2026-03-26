#!/bin/bash
# get_storage_config.sh - Export Azure Storage Account configuration
# Usage: ./get_storage_config.sh "<storage_name>" "<resource_group>" "<session_folder>"
# Example: ./get_storage_config.sh "talentaistage" "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

STORAGE_NAME="${1}"
RESOURCE_GROUP="${2}"
SESSION_FOLDER="${3:-.}"

if [ -z "$STORAGE_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Storage account name and resource group required"
    echo "Usage: ./get_storage_config.sh <storage_name> <resource_group> [session_folder]"
    exit 1
fi

echo "Exporting Azure Storage Account configuration: $STORAGE_NAME"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# Full configuration
FULL_CONFIG_FILE="$SESSION_FOLDER/exports/storage_${STORAGE_NAME}_full_${TIMESTAMP}.json"
echo "Fetching full configuration..."
az storage account show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --output json > "$FULL_CONFIG_FILE"
echo "  Saved: $FULL_CONFIG_FILE"

# Network rules
NETWORK_FILE="$SESSION_FOLDER/exports/storage_${STORAGE_NAME}_network_${TIMESTAMP}.json"
echo "Fetching network rules..."
az storage account network-rule list -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --output json > "$NETWORK_FILE" 2>/dev/null || echo "{}" > "$NETWORK_FILE"
echo "  Saved: $NETWORK_FILE"

# Blob service properties
BLOB_PROPS_FILE="$SESSION_FOLDER/exports/storage_${STORAGE_NAME}_blob_props_${TIMESTAMP}.json"
echo "Fetching blob service properties..."
az storage account blob-service-properties show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --output json > "$BLOB_PROPS_FILE" 2>/dev/null || echo "{}" > "$BLOB_PROPS_FILE"
echo "  Saved: $BLOB_PROPS_FILE"

# Container list (requires auth)
CONTAINERS_FILE="$SESSION_FOLDER/exports/storage_${STORAGE_NAME}_containers_${TIMESTAMP}.json"
echo "Fetching container list..."
az storage container list --account-name "$STORAGE_NAME" --auth-mode login --output json > "$CONTAINERS_FILE" 2>/dev/null || echo "[]" > "$CONTAINERS_FILE"
echo "  Saved: $CONTAINERS_FILE"

# Summary
echo ""
echo "Storage Account Summary:"
echo "========================"

LOCATION=$(cat "$FULL_CONFIG_FILE" | grep -o '"location": "[^"]*"' | head -1 | cut -d'"' -f4)
SKU=$(az storage account show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --query "sku.name" -o tsv 2>/dev/null || echo "Unknown")
KIND=$(az storage account show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --query "kind" -o tsv 2>/dev/null || echo "Unknown")
ACCESS_TIER=$(az storage account show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --query "accessTier" -o tsv 2>/dev/null || echo "Unknown")
STATE=$(az storage account show -n "$STORAGE_NAME" -g "$RESOURCE_GROUP" --query "provisioningState" -o tsv 2>/dev/null || echo "Unknown")

echo "  Location: $LOCATION"
echo "  SKU: $SKU"
echo "  Kind: $KIND"
echo "  Access Tier: $ACCESS_TIER"
echo "  State: $STATE"
echo ""

# Container count
CONTAINER_COUNT=$(cat "$CONTAINERS_FILE" | grep -c '"name":' || echo "0")
echo "  Containers: $CONTAINER_COUNT"

if [ "$CONTAINER_COUNT" -gt 0 ]; then
    echo "  Container Names:"
    cat "$CONTAINERS_FILE" | grep '"name":' | cut -d'"' -f4 | while read name; do
        echo "    - $name"
    done
fi

echo ""
echo "NOTE: Storage access keys are NOT exported for security reasons."
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
