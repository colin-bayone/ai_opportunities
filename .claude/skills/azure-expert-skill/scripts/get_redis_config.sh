#!/bin/bash
# get_redis_config.sh - Export Azure Redis configuration
# Usage: ./get_redis_config.sh "<redis_name>" "<resource_group>" "<session_folder>"
# Example: ./get_redis_config.sh "talent-ai-redis-stage" "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

REDIS_NAME="${1}"
RESOURCE_GROUP="${2}"
SESSION_FOLDER="${3:-.}"

if [ -z "$REDIS_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Redis name and resource group required"
    echo "Usage: ./get_redis_config.sh <redis_name> <resource_group> [session_folder]"
    exit 1
fi

echo "Exporting Azure Redis configuration: $REDIS_NAME"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# Full configuration
FULL_CONFIG_FILE="$SESSION_FOLDER/exports/redis_${REDIS_NAME}_full_${TIMESTAMP}.json"
echo "Fetching full configuration..."
az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --output json > "$FULL_CONFIG_FILE"
echo "  Saved: $FULL_CONFIG_FILE"

# Firewall rules (if any)
FIREWALL_FILE="$SESSION_FOLDER/exports/redis_${REDIS_NAME}_firewall_${TIMESTAMP}.json"
echo "Fetching firewall rules..."
az redis firewall-rules list -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --output json > "$FIREWALL_FILE" 2>/dev/null || echo "[]" > "$FIREWALL_FILE"
echo "  Saved: $FIREWALL_FILE"

# Summary
echo ""
echo "Redis Cache Summary:"
echo "===================="

LOCATION=$(cat "$FULL_CONFIG_FILE" | grep -o '"location": "[^"]*"' | head -1 | cut -d'"' -f4)
SKU=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "sku.name" -o tsv 2>/dev/null || echo "Unknown")
FAMILY=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "sku.family" -o tsv 2>/dev/null || echo "Unknown")
CAPACITY=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "sku.capacity" -o tsv 2>/dev/null || echo "Unknown")
STATE=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "provisioningState" -o tsv 2>/dev/null || echo "Unknown")
HOSTNAME=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "hostName" -o tsv 2>/dev/null || echo "Unknown")
PORT=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "port" -o tsv 2>/dev/null || echo "Unknown")
SSL_PORT=$(az redis show -n "$REDIS_NAME" -g "$RESOURCE_GROUP" --query "sslPort" -o tsv 2>/dev/null || echo "Unknown")

echo "  Location: $LOCATION"
echo "  SKU: $SKU $FAMILY $CAPACITY"
echo "  State: $STATE"
echo "  Hostname: $HOSTNAME"
echo "  Port: $PORT"
echo "  SSL Port: $SSL_PORT"
echo ""

# Check for private endpoint
echo "Checking for private endpoint..."
PE_COUNT=$(az network private-endpoint list -g "$RESOURCE_GROUP" --query "[?contains(privateLinkServiceConnections[0].privateLinkServiceId, '$REDIS_NAME')].name" -o tsv 2>/dev/null | wc -l || echo "0")
if [ "$PE_COUNT" -gt 0 ]; then
    echo "  Private Endpoint: Yes"
else
    echo "  Private Endpoint: No (public access)"
fi

echo ""
echo "NOTE: Redis access keys are NOT exported for security reasons."
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
