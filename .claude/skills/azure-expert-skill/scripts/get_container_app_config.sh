#!/bin/bash
# get_container_app_config.sh - Export Container App configuration
# Usage: ./get_container_app_config.sh "<app_name>" "<resource_group>" "<session_folder>"
# Example: ./get_container_app_config.sh "talent-ai-app-stage-aca" "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

APP_NAME="${1}"
RESOURCE_GROUP="${2}"
SESSION_FOLDER="${3:-.}"

if [ -z "$APP_NAME" ] || [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: App name and resource group required"
    echo "Usage: ./get_container_app_config.sh <app_name> <resource_group> [session_folder]"
    exit 1
fi

echo "Exporting Container App configuration: $APP_NAME"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# Full configuration
FULL_CONFIG_FILE="$SESSION_FOLDER/exports/containerapp_${APP_NAME}_full_${TIMESTAMP}.json"
echo "Fetching full configuration..."
az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" --output json > "$FULL_CONFIG_FILE"
echo "  Saved: $FULL_CONFIG_FILE"

# Environment variables (non-secret only)
ENV_FILE="$SESSION_FOLDER/exports/containerapp_${APP_NAME}_env_${TIMESTAMP}.json"
echo "Fetching environment variables..."
az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" \
    --query "properties.template.containers[0].env" --output json > "$ENV_FILE"
echo "  Saved: $ENV_FILE"

# Scaling configuration
SCALE_FILE="$SESSION_FOLDER/exports/containerapp_${APP_NAME}_scale_${TIMESTAMP}.json"
echo "Fetching scaling configuration..."
az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" \
    --query "properties.template.scale" --output json > "$SCALE_FILE"
echo "  Saved: $SCALE_FILE"

# Ingress configuration
INGRESS_FILE="$SESSION_FOLDER/exports/containerapp_${APP_NAME}_ingress_${TIMESTAMP}.json"
echo "Fetching ingress configuration..."
az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" \
    --query "properties.configuration.ingress" --output json > "$INGRESS_FILE"
echo "  Saved: $INGRESS_FILE"

# Secret names only (NEVER export actual secret values)
SECRETS_FILE="$SESSION_FOLDER/exports/containerapp_${APP_NAME}_secret_names_${TIMESTAMP}.json"
echo "Fetching secret names (not values)..."
az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" \
    --query "properties.configuration.secrets[].name" --output json > "$SECRETS_FILE"
echo "  Saved: $SECRETS_FILE"

# Quick summary
echo ""
echo "Configuration Summary:"
echo "====================="

# Get key properties
LOCATION=$(cat "$FULL_CONFIG_FILE" | grep -o '"location": "[^"]*"' | head -1 | cut -d'"' -f4)
STATUS=$(az containerapp show -n "$APP_NAME" -g "$RESOURCE_GROUP" --query "properties.provisioningState" -o tsv 2>/dev/null || echo "Unknown")
IMAGE=$(cat "$FULL_CONFIG_FILE" | grep -o '"image": "[^"]*"' | head -1 | cut -d'"' -f4)

echo "  Location: $LOCATION"
echo "  Status: $STATUS"
echo "  Image: $IMAGE"

echo ""
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
