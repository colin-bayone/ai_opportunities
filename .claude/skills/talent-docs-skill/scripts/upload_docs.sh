#!/bin/bash
# Upload documentation files to Azure Blob Storage
#
# Usage:
#   ./upload_docs.sh <local_path> [blob_path]
#
# Examples:
#   ./upload_docs.sh welcome.md getting-started/welcome.md
#   ./upload_docs.sh _nav.yaml _nav.yaml
#   ./upload_docs.sh ./docs-content/  # Upload entire directory

set -e

# Check for Azure CLI
if ! command -v az &> /dev/null; then
    echo "Error: Azure CLI (az) not found. Please install it first."
    exit 1
fi

# Container name
CONTAINER="docs"

# Get storage account from environment or .env file
if [ -z "$AZURE_STORAGE_ACCOUNT_NAME" ]; then
    # Try to load from .env.local
    if [ -f ".env.local" ]; then
        export $(grep AZURE_STORAGE_ACCOUNT_NAME .env.local | xargs)
    fi
fi

if [ -z "$AZURE_STORAGE_ACCOUNT_NAME" ]; then
    echo "Error: AZURE_STORAGE_ACCOUNT_NAME not set"
    echo "Set it in environment or .env.local file"
    exit 1
fi

LOCAL_PATH="$1"
BLOB_PATH="$2"

if [ -z "$LOCAL_PATH" ]; then
    echo "Usage: $0 <local_path> [blob_path]"
    echo ""
    echo "Examples:"
    echo "  $0 welcome.md getting-started/welcome.md"
    echo "  $0 _nav.yaml _nav.yaml"
    echo "  $0 ./docs-content/  # Upload directory"
    exit 1
fi

# Check if local path exists
if [ ! -e "$LOCAL_PATH" ]; then
    echo "Error: $LOCAL_PATH does not exist"
    exit 1
fi

# Upload single file or directory
if [ -d "$LOCAL_PATH" ]; then
    echo "Uploading directory: $LOCAL_PATH"
    az storage blob upload-batch \
        --account-name "$AZURE_STORAGE_ACCOUNT_NAME" \
        --destination "$CONTAINER" \
        --source "$LOCAL_PATH" \
        --overwrite
    echo "Directory uploaded successfully"
else
    # Single file - use blob path or derive from local path
    if [ -z "$BLOB_PATH" ]; then
        BLOB_PATH=$(basename "$LOCAL_PATH")
    fi

    echo "Uploading: $LOCAL_PATH → $CONTAINER/$BLOB_PATH"
    az storage blob upload \
        --account-name "$AZURE_STORAGE_ACCOUNT_NAME" \
        --container-name "$CONTAINER" \
        --name "$BLOB_PATH" \
        --file "$LOCAL_PATH" \
        --overwrite
    echo "File uploaded successfully"
fi

echo ""
echo "View at: /docs/${BLOB_PATH%.md}/"
