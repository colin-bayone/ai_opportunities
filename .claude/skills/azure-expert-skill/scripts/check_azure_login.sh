#!/bin/bash
# check_azure_login.sh - Verify Azure CLI authentication status
# Usage: ./check_azure_login.sh
# Returns: 0 if logged in, 1 if not logged in

set -e

echo "Checking Azure CLI authentication..."
echo ""

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "ERROR: Azure CLI is not installed."
    echo ""
    echo "Install Azure CLI:"
    echo "  curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash"
    echo ""
    exit 1
fi

# Check if logged in
ACCOUNT_INFO=$(az account show 2>/dev/null || true)

if [ -z "$ACCOUNT_INFO" ]; then
    echo "NOT LOGGED IN"
    echo ""
    echo "To log in, run:"
    echo "  az login"
    echo ""
    echo "For service principal authentication:"
    echo "  az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>"
    echo ""
    exit 1
fi

# Extract account details
SUBSCRIPTION_NAME=$(echo "$ACCOUNT_INFO" | grep -o '"name": "[^"]*"' | head -1 | cut -d'"' -f4)
SUBSCRIPTION_ID=$(echo "$ACCOUNT_INFO" | grep -o '"id": "[^"]*"' | head -1 | cut -d'"' -f4)
TENANT_ID=$(echo "$ACCOUNT_INFO" | grep -o '"tenantId": "[^"]*"' | cut -d'"' -f4)
USER_NAME=$(echo "$ACCOUNT_INFO" | grep -o '"name": "[^"]*"' | tail -1 | cut -d'"' -f4)
USER_TYPE=$(echo "$ACCOUNT_INFO" | grep -o '"type": "[^"]*"' | tail -1 | cut -d'"' -f4)

echo "LOGGED IN"
echo ""
echo "Account Details:"
echo "  Subscription: $SUBSCRIPTION_NAME"
echo "  Subscription ID: $SUBSCRIPTION_ID"
echo "  Tenant ID: $TENANT_ID"
echo "  User: $USER_NAME"
echo "  Auth Type: $USER_TYPE"
echo ""

# Check Azure CLI version
AZ_VERSION=$(az version --query '"azure-cli"' -o tsv 2>/dev/null || echo "unknown")
echo "Azure CLI Version: $AZ_VERSION"
echo ""

# List available subscriptions
echo "Available Subscriptions:"
az account list --query "[].{Name:name, ID:id, IsDefault:isDefault}" --output table 2>/dev/null || echo "  Unable to list subscriptions"
echo ""

exit 0
