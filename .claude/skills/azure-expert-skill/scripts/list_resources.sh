#!/bin/bash
# list_resources.sh - List all resources in an Azure resource group
# Usage: ./list_resources.sh "<resource_group>" "<session_folder>"
# Example: ./list_resources.sh "talent_ai_stage-rg" "claude/2026-01-06_AZURE_staging"

set -e

RESOURCE_GROUP="${1}"
SESSION_FOLDER="${2:-.}"

if [ -z "$RESOURCE_GROUP" ]; then
    echo "Error: Resource group name required"
    echo "Usage: ./list_resources.sh <resource_group> [session_folder]"
    exit 1
fi

echo "Listing resources in: $RESOURCE_GROUP"
echo ""

# Create exports directory if needed
mkdir -p "$SESSION_FOLDER/exports"

# Get timestamp for file naming
TIMESTAMP=$(date '+%Y%m%d_%H%M')

# List all resources and save to JSON
OUTPUT_FILE="$SESSION_FOLDER/exports/raw_resources_${TIMESTAMP}.json"

echo "Fetching resource list..."
az resource list --resource-group "$RESOURCE_GROUP" --output json > "$OUTPUT_FILE"

# Count resources
TOTAL_COUNT=$(cat "$OUTPUT_FILE" | grep -c '"id":' || echo "0")
echo "Total resources found: $TOTAL_COUNT"
echo ""

# Get summary by type
echo "Resources by type:"
echo ""
cat "$OUTPUT_FILE" | grep '"type":' | sort | uniq -c | sort -rn | while read count type; do
    # Clean up the type string
    clean_type=$(echo "$type" | sed 's/"type": "//g' | sed 's/",//g' | sed 's/"//g')
    echo "  $count - $clean_type"
done

echo ""
echo "Raw data saved to: $OUTPUT_FILE"

# Also create a summary table
SUMMARY_FILE="$SESSION_FOLDER/exports/resource_summary_${TIMESTAMP}.txt"
echo "Resource Summary for $RESOURCE_GROUP" > "$SUMMARY_FILE"
echo "Generated: $(date '+%Y-%m-%d %H:%M:%S')" >> "$SUMMARY_FILE"
echo "Total Resources: $TOTAL_COUNT" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"
echo "By Type:" >> "$SUMMARY_FILE"
cat "$OUTPUT_FILE" | grep '"type":' | sort | uniq -c | sort -rn >> "$SUMMARY_FILE"

echo "Summary saved to: $SUMMARY_FILE"
