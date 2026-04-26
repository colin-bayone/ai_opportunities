#!/usr/bin/env python3
"""
One-time authentication bootstrap for meeting transcript skill.

Supports two auth flows:
  1. Device code flow (default) — user enters code in browser
  2. Client credentials flow — fully unattended

Usage:
    # Device code flow (recommended for WSL2 — just copy URL to Windows browser)
    python3 auth_bootstrap.py --env-file /path/to/.env

    # Client credentials flow
    python3 auth_bootstrap.py --env-file /path/to/.env --client-credentials
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import msal
from dotenv import load_dotenv

# Import from sibling module
sys.path.insert(0, str(Path(__file__).parent))
from graph_client import (
    _load_env,
    _validate_config,
    _load_token_cache,
    _save_token_cache,
    _update_token_metadata,
    get_token_cache_path,
    get_output_dir,
    DEFAULT_SCOPES,
    GRAPH_BASE_URL,
)


def device_code_flow(env_file: str) -> bool:
    """
    Authenticate using device code flow.
    Prints URL and code for user to enter in any browser.

    Requires "Allow public client flows" = Yes in Azure Portal:
      App Registration > Authentication > Allow public client flows > Yes
    """
    config = _load_env(env_file)
    errors = _validate_config(config)
    if errors:
        print(f"Configuration errors:\n  " + "\n  ".join(errors))
        return False

    authority = f"https://login.microsoftonline.com/{config['tenant_id']}"
    cache_path = get_token_cache_path(env_file)
    cache = _load_token_cache(cache_path)

    app = msal.PublicClientApplication(
        client_id=config["client_id"],
        authority=authority,
        token_cache=cache,
    )

    # Filter scopes (exclude reserved OIDC scopes MSAL handles automatically)
    scopes = [
        s for s in config["scopes"]
        if s.lower() not in ("offline_access", "openid", "profile", "email")
    ]

    flow = app.initiate_device_flow(scopes=scopes)

    if "user_code" not in flow:
        error = flow.get('error_description', 'Unknown error')
        if 'AADSTS7000218' in str(error):
            print("ERROR: Azure app requires 'Allow public client flows' to be enabled.")
            print("  Go to Azure Portal > App Registration > Authentication")
            print("  Set 'Allow public client flows' to Yes, then try again.")
        else:
            print(f"Failed to initiate device code flow: {error}")
        return False

    print("\n" + "=" * 60)
    print("AUTHENTICATION REQUIRED")
    print("=" * 60)
    print()
    print(flow["message"])
    print()
    print("NOTE: Copy the URL above and open it in your Windows browser.")
    print("      (WSL2 cannot open a browser directly)")
    print()
    print("Waiting for you to complete sign-in...")
    print("=" * 60)

    result = app.acquire_token_by_device_flow(flow)

    if "access_token" in result:
        _save_token_cache(cache, cache_path)
        _update_token_metadata(env_file, "device_code")

        print("\nAuthentication successful!")
        print(f"  Token cached to: {cache_path}")

        # Verify by calling /me and store user email in metadata
        import requests
        headers = {"Authorization": f"Bearer {result['access_token']}"}
        me_response = requests.get(f"{GRAPH_BASE_URL}/me", headers=headers, timeout=10)
        if me_response.status_code == 200:
            user_data = me_response.json()
            user_email = user_data.get('mail', user_data.get('userPrincipalName', ''))
            print(f"  Authenticated as: {user_data.get('displayName', 'Unknown')}")
            print(f"  Email: {user_email}")

            # Save email to token metadata for exclusive mode
            meta_path = get_token_metadata_path(env_file)
            from graph_client import _load_token_metadata, _save_token_metadata
            metadata = _load_token_metadata(meta_path)
            metadata["user_email"] = user_email.lower()
            metadata["user_display_name"] = user_data.get('displayName', '')
            _save_token_metadata(meta_path, metadata)
        else:
            print(f"  (Could not verify user identity: {me_response.status_code})")

        return True
    else:
        error = result.get("error_description", result.get("error", "Unknown error"))
        print(f"\nAuthentication failed: {error}")
        return False


def client_credentials_flow(env_file: str) -> bool:
    """
    Authenticate using client credentials (application permissions).
    Fully unattended — no browser interaction.
    """
    config = _load_env(env_file)
    errors = _validate_config(config, require_user_id=True)
    if errors:
        print(f"Configuration errors:\n  " + "\n  ".join(errors))
        return False

    authority = f"https://login.microsoftonline.com/{config['tenant_id']}"
    cache_path = get_token_cache_path(env_file)
    cache = _load_token_cache(cache_path)

    app = msal.ConfidentialClientApplication(
        client_id=config["client_id"],
        client_credential=config["client_secret"],
        authority=authority,
        token_cache=cache,
    )

    result = app.acquire_token_for_client(
        scopes=["https://graph.microsoft.com/.default"]
    )

    if "access_token" in result:
        _save_token_cache(cache, cache_path)
        _update_token_metadata(env_file, "client_credentials")

        print("Authentication successful (client credentials)!")
        print(f"  Token cached to: {cache_path}")
        print(f"  User ID: {config['user_id']}")
        print()
        print("NOTE: For transcript access, ensure Application Access Policy is configured.")
        print("      This requires a Teams admin to run PowerShell on Windows:")
        print(f"      New-CsApplicationAccessPolicy -Identity TranscriptPolicy -AppIds \"{config['client_id']}\"")
        print(f"      Grant-CsApplicationAccessPolicy -PolicyName TranscriptPolicy -Identity \"{config['user_id']}\"")

        return True
    else:
        error = result.get("error_description", result.get("error", "Unknown error"))
        print(f"Authentication failed: {error}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Authenticate with Microsoft Graph API for meeting transcripts"
    )
    parser.add_argument(
        "--env-file", required=True,
        help="Path to .env file with Azure credentials"
    )
    parser.add_argument(
        "--client-credentials", action="store_true",
        help="Use client credentials flow (application permissions) instead of device code"
    )

    args = parser.parse_args()

    if not os.path.exists(args.env_file):
        print(f"ERROR: .env file not found: {args.env_file}")
        print(f"See .claude/skills/meeting-transcript-skill/.env.example for the template.")
        sys.exit(1)

    if args.client_credentials:
        success = client_credentials_flow(args.env_file)
    else:
        success = device_code_flow(args.env_file)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
