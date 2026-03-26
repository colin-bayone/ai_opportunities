#!/bin/bash
# get_vnet_topology.sh - Map VNet/subnet relationships
# Usage: ./get_vnet_topology.sh "<resource_group>" "<session_folder>"
# Example: ./get_vnet_topology.sh "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

RESOURCE_GROUP="${1}"
SESSION_FOLDER="${2:-.}"

if [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Resource group name required"
    echo "Usage: ./get_vnet_topology.sh <resource_group> [session_folder]"
    exit 1
fi

echo "Mapping VNet topology for: $RESOURCE_GROUP"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# List all VNets
VNET_LIST_FILE="$SESSION_FOLDER/exports/vnets_${TIMESTAMP}.json"
echo "Fetching VNet list..."
az network vnet list --resource-group "$RESOURCE_GROUP" --output json > "$VNET_LIST_FILE"
echo "  Saved: $VNET_LIST_FILE"

# Get VNet names
VNET_NAMES=$(az network vnet list --resource-group "$RESOURCE_GROUP" --query "[].name" -o tsv 2>/dev/null || echo "")

if [ -z "$VNET_NAMES" ]; then
    echo "No VNets found in resource group: $RESOURCE_GROUP"
    exit 0
fi

# For each VNet, get detailed info
for VNET_NAME in $VNET_NAMES; do
    echo ""
    echo "Processing VNet: $VNET_NAME"

    # VNet details
    VNET_DETAIL_FILE="$SESSION_FOLDER/exports/vnet_${VNET_NAME}_detail_${TIMESTAMP}.json"
    az network vnet show -n "$VNET_NAME" -g "$RESOURCE_GROUP" --output json > "$VNET_DETAIL_FILE"
    echo "  VNet details: $VNET_DETAIL_FILE"

    # Subnets
    SUBNET_FILE="$SESSION_FOLDER/exports/vnet_${VNET_NAME}_subnets_${TIMESTAMP}.json"
    az network vnet subnet list --vnet-name "$VNET_NAME" -g "$RESOURCE_GROUP" --output json > "$SUBNET_FILE"
    echo "  Subnets: $SUBNET_FILE"
done

# List all Private Endpoints
PE_FILE="$SESSION_FOLDER/exports/private_endpoints_${TIMESTAMP}.json"
echo ""
echo "Fetching Private Endpoints..."
az network private-endpoint list --resource-group "$RESOURCE_GROUP" --output json > "$PE_FILE"
echo "  Saved: $PE_FILE"

# List all Private DNS Zones
DNS_ZONES_FILE="$SESSION_FOLDER/exports/private_dns_zones_${TIMESTAMP}.json"
echo ""
echo "Fetching Private DNS Zones..."
az network private-dns zone list --resource-group "$RESOURCE_GROUP" --output json > "$DNS_ZONES_FILE" 2>/dev/null || echo "[]" > "$DNS_ZONES_FILE"
echo "  Saved: $DNS_ZONES_FILE"

# Summary
echo ""
echo "VNet Topology Summary:"
echo "====================="

for VNET_NAME in $VNET_NAMES; do
    ADDRESS_SPACE=$(az network vnet show -n "$VNET_NAME" -g "$RESOURCE_GROUP" --query "addressSpace.addressPrefixes[0]" -o tsv 2>/dev/null || echo "Unknown")
    SUBNET_COUNT=$(az network vnet subnet list --vnet-name "$VNET_NAME" -g "$RESOURCE_GROUP" --query "length(@)" -o tsv 2>/dev/null || echo "0")

    echo ""
    echo "VNet: $VNET_NAME"
    echo "  Address Space: $ADDRESS_SPACE"
    echo "  Subnet Count: $SUBNET_COUNT"
    echo "  Subnets:"

    az network vnet subnet list --vnet-name "$VNET_NAME" -g "$RESOURCE_GROUP" \
        --query "[].{Name:name, AddressPrefix:addressPrefix, Delegations:delegations[0].serviceName}" \
        --output table 2>/dev/null | tail -n +3
done

# Private Endpoints summary
PE_COUNT=$(cat "$PE_FILE" | grep -c '"name":' || echo "0")
echo ""
echo "Private Endpoints: $PE_COUNT"
if [ "$PE_COUNT" -gt 0 ]; then
    az network private-endpoint list --resource-group "$RESOURCE_GROUP" \
        --query "[].{Name:name, Subnet:subnet.id, Target:privateLinkServiceConnections[0].privateLinkServiceId}" \
        --output table 2>/dev/null | tail -n +3 | head -20
fi

echo ""
echo "Export complete. Files saved in: $SESSION_FOLDER/exports/"
