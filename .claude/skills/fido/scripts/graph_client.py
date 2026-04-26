"""
Standalone Microsoft Graph API client with MSAL token management.
No Django dependencies. Uses python-dotenv for configuration.

Supports two auth modes:
  1. Device code flow (delegated permissions, uses /me/ endpoints)
  2. Client credentials flow (application permissions, uses /users/{id}/ endpoints)
"""

import json
import logging
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import msal
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Default output directory relative to project root
DEFAULT_OUTPUT_DIR = "claude/meeting_transcripts"

# Default Graph API scopes for device code flow
DEFAULT_SCOPES = [
    "User.Read",
    "Calendars.Read",
    "OnlineMeetings.Read",
    "OnlineMeetingTranscript.Read.All",
    "offline_access",
]

# Refresh token default lifetime (days) - actual varies by tenant policy
REFRESH_TOKEN_DEFAULT_LIFETIME_DAYS = 90
REFRESH_TOKEN_WARNING_DAYS = 7

GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"


class AuthError(Exception):
    """Raised when authentication fails."""
    pass


class GraphAPIError(Exception):
    """Raised when a Graph API call fails."""
    def __init__(self, message, status_code=None, error_code=None):
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


def get_output_dir(env_file: str = None) -> Path:
    """Get the output directory path."""
    if env_file:
        load_dotenv(env_file)
    output = os.getenv("OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return Path(output)


def get_token_cache_path(env_file: str = None) -> Path:
    """Get token cache file path."""
    return get_output_dir(env_file) / "token_cache.json"


def get_token_metadata_path(env_file: str = None) -> Path:
    """Get token metadata file path."""
    return get_output_dir(env_file) / "token_metadata.json"


def _load_env(env_file: str) -> dict:
    """Load and validate environment variables."""
    load_dotenv(env_file, override=True)

    config = {
        "client_id": os.getenv("MICROSOFT_CLIENT_ID", ""),
        "client_secret": os.getenv("MICROSOFT_CLIENT_SECRET", "") or os.getenv("MICROSOFT_SECRET", ""),
        "tenant_id": os.getenv("AZURE_TENANT_ID", ""),
        "user_id": os.getenv("MICROSOFT_USER_ID", ""),
        "scopes": [],
        "default_search_days": int(os.getenv("DEFAULT_SEARCH_DAYS", "30")),
    }

    scopes_env = os.getenv("GRAPH_API_SCOPES", "")
    if scopes_env:
        config["scopes"] = [s.strip() for s in scopes_env.split(",") if s.strip()]
    else:
        config["scopes"] = DEFAULT_SCOPES

    return config


def _validate_config(config: dict, require_user_id: bool = False) -> list[str]:
    """Validate required config values. Returns list of error messages."""
    errors = []
    if not config["client_id"]:
        errors.append("MICROSOFT_CLIENT_ID is missing")
    if not config["client_secret"]:
        errors.append("MICROSOFT_CLIENT_SECRET is missing")
    if not config["tenant_id"]:
        errors.append("AZURE_TENANT_ID is missing")
    if require_user_id and not config["user_id"]:
        errors.append("MICROSOFT_USER_ID is required for client credentials flow")
    return errors


def _load_token_cache(cache_path: Path) -> msal.SerializableTokenCache:
    """Load MSAL token cache from file."""
    cache = msal.SerializableTokenCache()
    if cache_path.exists():
        cache.deserialize(cache_path.read_text())
    return cache


def _save_token_cache(cache: msal.SerializableTokenCache, cache_path: Path):
    """Persist MSAL token cache to file."""
    if cache.has_state_changed:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(cache.serialize())


def _load_token_metadata(meta_path: Path) -> dict:
    """Load token metadata (auth timestamps, expiry info)."""
    if meta_path.exists():
        try:
            return json.loads(meta_path.read_text())
        except json.JSONDecodeError:
            pass
    return {}


def _save_token_metadata(meta_path: Path, metadata: dict):
    """Save token metadata."""
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(metadata, indent=2))


def _update_token_metadata(env_file: str, auth_method: str):
    """Record authentication timestamp and method."""
    meta_path = get_token_metadata_path(env_file)
    metadata = _load_token_metadata(meta_path)
    now = datetime.now(timezone.utc).isoformat()
    metadata["last_authenticated"] = now
    metadata["auth_method"] = auth_method
    metadata["refresh_token_expires_estimate"] = (
        datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_DEFAULT_LIFETIME_DAYS)
    ).isoformat()
    _save_token_metadata(meta_path, metadata)


def check_auth_status(env_file: str) -> dict:
    """
    Check current authentication status.

    Returns dict with:
      - authenticated: bool
      - auth_method: str
      - last_authenticated: str (ISO timestamp)
      - refresh_token_expires: str (ISO timestamp estimate)
      - days_until_expiry: int
      - needs_reauth: bool
      - warning: str (if approaching expiry)
      - error: str (if there's a problem)
    """
    config = _load_env(env_file)
    errors = _validate_config(config)
    if errors:
        return {"authenticated": False, "error": f"Config errors: {'; '.join(errors)}"}

    cache_path = get_token_cache_path(env_file)
    meta_path = get_token_metadata_path(env_file)

    if not cache_path.exists():
        return {
            "authenticated": False,
            "error": "No token cache found. Run auth_bootstrap.py to authenticate.",
        }

    metadata = _load_token_metadata(meta_path)
    if not metadata.get("last_authenticated"):
        return {
            "authenticated": False,
            "error": "Token cache exists but no auth metadata. Re-run auth_bootstrap.py.",
        }

    result = {
        "authenticated": True,
        "auth_method": metadata.get("auth_method", "unknown"),
        "last_authenticated": metadata["last_authenticated"],
    }

    # Check refresh token expiry estimate
    expires_str = metadata.get("refresh_token_expires_estimate")
    if expires_str:
        try:
            expires_at = datetime.fromisoformat(expires_str)
            now = datetime.now(timezone.utc)
            days_left = (expires_at - now).days

            result["refresh_token_expires"] = expires_str
            result["days_until_expiry"] = days_left
            result["needs_reauth"] = days_left <= 0

            if days_left <= 0:
                result["error"] = (
                    "Refresh token has likely expired. Re-run auth_bootstrap.py."
                )
                result["authenticated"] = False
            elif days_left <= REFRESH_TOKEN_WARNING_DAYS:
                result["warning"] = (
                    f"Refresh token expires in ~{days_left} days. "
                    "Consider re-authenticating soon."
                )
        except (ValueError, TypeError):
            pass

    # Try to actually acquire a token silently to verify
    cache = _load_token_cache(cache_path)
    authority = f"https://login.microsoftonline.com/{config['tenant_id']}"

    if metadata.get("auth_method") == "client_credentials":
        app = msal.ConfidentialClientApplication(
            client_id=config["client_id"],
            client_credential=config["client_secret"],
            authority=authority,
            token_cache=cache,
        )
        token_result = app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )
    else:
        app = msal.PublicClientApplication(
            client_id=config["client_id"],
            authority=authority,
            token_cache=cache,
        )
        accounts = app.get_accounts()
        if not accounts:
            result["authenticated"] = False
            result["error"] = "No cached accounts found. Re-run auth_bootstrap.py."
            return result

        # Filter to delegated scopes only (exclude reserved OIDC scopes)
        delegated_scopes = [
            s for s in config["scopes"]
            if s.lower() not in ("offline_access", "openid", "profile", "email")
        ]
        token_result = app.acquire_token_silent(
            scopes=delegated_scopes, account=accounts[0]
        )

    if token_result and "access_token" in token_result:
        _save_token_cache(cache, cache_path)
        result["token_valid"] = True
    else:
        error_desc = ""
        if token_result:
            error_desc = token_result.get("error_description", token_result.get("error", ""))
        result["token_valid"] = False
        result["error"] = f"Token acquisition failed: {error_desc}. Re-run auth_bootstrap.py."
        result["authenticated"] = False

    return result


class GraphClient:
    """
    Standalone Microsoft Graph API client.

    Usage:
        client = GraphClient(env_file="/path/to/.env")
        events = client.get("/me/calendarView", params={...})
    """

    def __init__(self, env_file: str, auth_method: str = None):
        """
        Initialize Graph client.

        Args:
            env_file: Path to .env file with credentials
            auth_method: "device_code" or "client_credentials".
                         Auto-detected from token_metadata.json if not specified.
        """
        self.env_file = env_file
        self.config = _load_env(env_file)

        # Determine auth method
        if auth_method:
            self.auth_method = auth_method
        else:
            meta_path = get_token_metadata_path(env_file)
            metadata = _load_token_metadata(meta_path)
            self.auth_method = metadata.get("auth_method", "device_code")

        self.cache_path = get_token_cache_path(env_file)
        self.cache = _load_token_cache(self.cache_path)

        authority = f"https://login.microsoftonline.com/{self.config['tenant_id']}"

        if self.auth_method == "client_credentials":
            self.app = msal.ConfidentialClientApplication(
                client_id=self.config["client_id"],
                client_credential=self.config["client_secret"],
                authority=authority,
                token_cache=self.cache,
            )
            self.user_id = self.config["user_id"]
        else:
            self.app = msal.PublicClientApplication(
                client_id=self.config["client_id"],
                authority=authority,
                token_cache=self.cache,
            )
            self.user_id = None

        self._access_token = None

    def _get_token(self, force_refresh: bool = False) -> str:
        """Acquire a valid access token."""
        if self.auth_method == "client_credentials":
            result = self.app.acquire_token_for_client(
                scopes=["https://graph.microsoft.com/.default"]
            )
        else:
            accounts = self.app.get_accounts()
            if not accounts:
                raise AuthError(
                    "No cached accounts. Run auth_bootstrap.py to authenticate."
                )
            delegated_scopes = [
                s for s in self.config["scopes"]
                if s.lower() not in ("offline_access", "openid", "profile", "email")
            ]
            result = self.app.acquire_token_silent(
                scopes=delegated_scopes,
                account=accounts[0],
                force_refresh=force_refresh,
            )

        if not result or "access_token" not in result:
            error_msg = ""
            if result:
                error_msg = result.get("error_description", result.get("error", ""))
            raise AuthError(
                f"Failed to acquire token: {error_msg}. Re-run auth_bootstrap.py."
            )

        self._access_token = result["access_token"]
        _save_token_cache(self.cache, self.cache_path)
        return self._access_token

    def _get_endpoint_prefix(self) -> str:
        """Get the endpoint prefix based on auth method."""
        if self.auth_method == "client_credentials":
            if not self.user_id:
                raise AuthError("MICROSOFT_USER_ID required for client credentials flow.")
            return f"/users/{self.user_id}"
        return "/me"

    def get(self, endpoint: str, params: dict = None,
            return_binary: bool = False, max_retries: int = 3) -> dict:
        """
        Make a GET request to Graph API.

        Args:
            endpoint: API endpoint (e.g., "/me/calendarView")
            params: Query parameters
            return_binary: Return raw bytes instead of JSON
            max_retries: Max retry attempts on 401

        Returns:
            Dict with 'success', 'data', and optionally 'error'
        """
        token = self._get_token()

        for attempt in range(max_retries):
            try:
                headers = {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                }
                if return_binary:
                    headers.pop("Content-Type", None)

                url = f"{GRAPH_BASE_URL}{endpoint}"
                response = requests.get(url, headers=headers, params=params, timeout=30)

                if response.status_code == 401 and attempt < max_retries - 1:
                    logger.info("Got 401, refreshing token (attempt %d)", attempt + 1)
                    token = self._get_token(force_refresh=True)
                    continue

                if response.status_code >= 400:
                    try:
                        error_data = response.json()
                        error_msg = error_data.get("error", {}).get("message", response.text)
                        error_code = error_data.get("error", {}).get("code", "")
                    except (json.JSONDecodeError, ValueError):
                        error_msg = response.text
                        error_code = ""

                    return {
                        "success": False,
                        "error": error_msg,
                        "error_code": error_code,
                        "status_code": response.status_code,
                    }

                if return_binary:
                    return {"success": True, "data": response.content}
                else:
                    return {"success": True, "data": response.json()}

            except requests.Timeout:
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return {"success": False, "error": "Request timed out", "error_code": "TIMEOUT"}
            except requests.ConnectionError as e:
                return {"success": False, "error": f"Connection error: {e}", "error_code": "CONNECTION"}

        return {"success": False, "error": "Max retries exceeded", "error_code": "MAX_RETRIES"}
