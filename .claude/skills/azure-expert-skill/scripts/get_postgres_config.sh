#!/bin/bash
# get_postgres_config.sh - Export PostgreSQL Flexible Server configuration
# Usage: ./get_postgres_config.sh "<server_name>" "<resource_group>" "<session_folder>"
# Example: ./get_postgres_config.sh "talent-ai-postgres-stage" "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

SERVER_NAME="${1}"
RESOURCE_GROUP="${2}"
SESSION_FOLDER="${3:-.}"

if [ -z "$SERVER_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Server name and resource group required"
    echo "Usage: ./get_postgres_config.sh <server_name> <resource_group> [session_folder]"
    exit 1
fi

echo "Exporting PostgreSQL Flexible Server configuration: $SERVER_NAME"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# Full configuration
FULL_CONFIG_FILE="$SESSION_FOLDER/exports/postgres_${SERVER_NAME}_full_${TIMESTAMP}.json"
echo "Fetching full configuration..."
az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --output json > "$FULL_CONFIG_FILE"
echo "  Saved: $FULL_CONFIG_FILE"

# Firewall rules
FIREWALL_FILE="$SESSION_FOLDER/exports/postgres_${SERVER_NAME}_firewall_${TIMESTAMP}.json"
echo "Fetching firewall rules..."
az postgres flexible-server firewall-rule list -g "$RESOURCE_GROUP" -s "$SERVER_NAME" --output json > "$FIREWALL_FILE" 2>/dev/null || echo "[]" > "$FIREWALL_FILE"
echo "  Saved: $FIREWALL_FILE"

# Database list
DB_FILE="$SESSION_FOLDER/exports/postgres_${SERVER_NAME}_databases_${TIMESTAMP}.json"
echo "Fetching database list..."
az postgres flexible-server db list -g "$RESOURCE_GROUP" -s "$SERVER_NAME" --output json > "$DB_FILE" 2>/dev/null || echo "[]" > "$DB_FILE"
echo "  Saved: $DB_FILE"

# Summary
echo ""
echo "PostgreSQL Server Summary:"
echo "=========================="

LOCATION=$(cat "$FULL_CONFIG_FILE" | grep -o '"location": "[^"]*"' | head -1 | cut -d'"' -f4)
VERSION=$(az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --query "version" -o tsv 2>/dev/null || echo "Unknown")
SKU=$(az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --query "sku.name" -o tsv 2>/dev/null || echo "Unknown")
STORAGE=$(az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --query "storage.storageSizeGb" -o tsv 2>/dev/null || echo "Unknown")
STATE=$(az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --query "state" -o tsv 2>/dev/null || echo "Unknown")

echo "  Location: $LOCATION"
echo "  Version: PostgreSQL $VERSION"
echo "  SKU: $SKU"
echo "  Storage: ${STORAGE} GB"
echo "  State: $STATE"
echo ""

# Check for private endpoint
PRIVATE_ENDPOINT=$(az postgres flexible-server show -n "$SERVER_NAME" -g "$RESOURCE_GROUP" --query "network.publicNetworkAccess" -o tsv 2>/dev/null || echo "Unknown")
echo "  Public Network Access: $PRIVATE_ENDPOINT"

echo ""
echo "NOTE: Database credentials are NOT exported for security reasons."
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
