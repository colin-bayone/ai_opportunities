# Auth Troubleshooting Reference

## Contents

1. [Authentication Flows Overview](#authentication-flows-overview)
2. [Common Errors and Solutions](#common-errors-and-solutions)
3. [Azure App Registration Requirements](#azure-app-registration-requirements)
4. [Delegated vs Application Permissions](#delegated-vs-application-permissions)
5. [WSL2-Specific Considerations](#wsl2-specific-considerations)
6. [Token Lifecycle](#token-lifecycle)

---

## Authentication Flows Overview

This skill supports two authentication flows. Always present both to the user if they're having trouble.

### Device Code Flow (Default — Delegated Permissions)

**How it works:**
1. Script calls `PublicClientApplication.initiate_device_flow()`
2. Prints a URL (`https://microsoft.com/devicelogin`) and a short code
3. User opens the URL in any browser and enters the code
4. User signs in (MFA supported)
5. Script polls Azure AD and receives tokens when sign-in completes

**Requirements:**
- "Allow public client flows" must be enabled in Azure App Registration
- Delegated permissions granted: `User.Read`, `Calendars.Read`, `OnlineMeetings.Read`, `OnlineMeetingTranscript.Read.All`

**Returns:** access_token + refresh_token (cached for ~90 days)

**Endpoints:** Uses `/me/` — acts as the signed-in user

### Client Credentials Flow (Application Permissions)

**How it works:**
1. Script uses `ConfidentialClientApplication.acquire_token_for_client()`
2. Authenticates with client_id + client_secret — no user interaction
3. Gets an app-only token

**Requirements:**
- Application permissions granted and admin-consented
- `MICROSOFT_USER_ID` set in .env (Azure AD user object ID)
- For transcript access: Application Access Policy configured by Teams admin (Windows PowerShell only)

**Returns:** access_token only (no refresh token — re-authenticates with credentials each time)

**Endpoints:** Uses `/users/{user-id}/` — no `/me/` available

---

## Common Errors and Solutions

### AADSTS7000218: "The request body must contain 'client_assertion' or 'client_secret'"

**What it means:** The Azure app registration has a client secret configured, making it a confidential client. The device code flow uses `PublicClientApplication` which doesn't send the secret.

**User options:**
1. **Enable public client flows** (recommended): Azure Portal > App Registration > Authentication > "Allow public client flows" > Yes. This allows the same app to work with both public and confidential flows.
2. **Use client credentials flow instead**: Run `auth_bootstrap.py --client-credentials`. Requires `MICROSOFT_USER_ID` in .env and Application Access Policy setup.
3. **Create a separate public app registration**: Register a new app without a client secret for this skill's device code flow.

### AADSTS65001: "The user or administrator has not consented to use the application"

**What it means:** The required permissions haven't been granted or admin-consented.

**User options:**
1. Go to Azure Portal > App Registration > API Permissions
2. Verify these delegated permissions are listed: `User.Read`, `Calendars.Read`, `OnlineMeetings.Read`, `OnlineMeetingTranscript.Read.All`
3. Click "Grant admin consent for [tenant]" (requires admin role)

### AADSTS50076: "Due to a configuration change made by your administrator..."

**What it means:** Conditional access or MFA policy is blocking the flow.

**User options:**
1. Device code flow supports MFA — the user should be prompted during browser sign-in
2. If still blocked, check with the Azure AD admin about Conditional Access policies
3. Client credentials flow bypasses MFA entirely (app-only auth)

### AADSTS700016: "Application with identifier was not found"

**What it means:** The `MICROSOFT_CLIENT_ID` in the .env file doesn't match any app registration.

**Fix:** Verify the client ID in Azure Portal > App Registrations > Overview > Application (client) ID

### 403 Forbidden on transcript endpoints

**What it means (delegated):** The user may not have the `OnlineMeetingTranscript.Read.All` permission, or transcription wasn't enabled for the meeting.

**What it means (application):** Application Access Policy not configured.

**User options (delegated):**
1. Verify the permission is granted in Azure Portal
2. Verify the user attended the meeting
3. Verify transcription was enabled during the meeting

**User options (application):**
1. A Teams admin must run these PowerShell commands on Windows:
   ```
   New-CsApplicationAccessPolicy -Identity "TranscriptPolicy" -AppIds "your-client-id"
   Grant-CsApplicationAccessPolicy -PolicyName "TranscriptPolicy" -Identity "user-object-id"
   ```
2. Wait up to 30 minutes for the policy to propagate

### Token acquisition failed / No cached accounts

**What it means:** The cached token has expired or been invalidated.

**Fix:** Re-run `auth_bootstrap.py --env-file /path/to/.env` to re-authenticate.

---

## Azure App Registration Requirements

### Required Configuration

**Authentication tab:**
- Platform: Mobile and desktop applications
- Redirect URI: `https://login.microsoftonline.com/common/oauth2/nativeclient`
- Allow public client flows: **Yes** (required for device code flow)

**API Permissions tab (Delegated):**
| Permission | Type | Admin Consent Required |
|-----------|------|----------------------|
| `User.Read` | Delegated | No |
| `Calendars.Read` | Delegated | Depends on tenant |
| `OnlineMeetings.Read` | Delegated | Yes |
| `OnlineMeetingTranscript.Read.All` | Delegated | Yes |

**API Permissions tab (Application — for client credentials flow):**
| Permission | Type | Admin Consent Required |
|-----------|------|----------------------|
| `Calendars.Read` | Application | Yes |
| `OnlineMeetings.Read.All` | Application | Yes |
| `OnlineMeetingTranscript.Read.All` | Application | Yes |
| `User.Read.All` | Application | Yes |

---

## Delegated vs Application Permissions

| Aspect | Delegated | Application |
|--------|-----------|-------------|
| Auth flow | Device code (user signs in) | Client credentials (no user) |
| Acts as | The signed-in user | The application itself |
| Endpoints | `/me/...` | `/users/{user-id}/...` |
| Transcript access | Any meeting user attended | Requires Application Access Policy |
| Non-organizer access | Yes — any meeting attended | Yes — if policy covers the user |
| MFA support | Yes | N/A (no user) |
| Refresh token | Yes (~90 days) | No (re-auth with credentials) |
| Admin setup | Grant permissions | Grant permissions + Access Policy |

### Key insight: Non-organizer transcript access

With delegated `OnlineMeetingTranscript.Read.All`, the user can access transcripts for any meeting they **attended**, not just meetings they organized. The `.All` suffix means "all meetings the user has access to."

---

## WSL2-Specific Considerations

- WSL2 has no native browser — `xdg-open` fails
- Device code flow prints the URL; user must manually copy it to their Windows browser
- The script does NOT attempt to open a browser
- `http://localhost` forwarding works from Windows to WSL2 (since Windows 10 build 1903+) but is not relied upon for this skill
- Application Access Policy PowerShell commands must run from Windows PowerShell or Azure Cloud Shell, not WSL2

---

## Token Lifecycle

### Device Code Flow Tokens

1. **Access token**: Short-lived (~1 hour). MSAL auto-refreshes silently.
2. **Refresh token**: Long-lived (~90 days, tenant policy dependent). Stored in `token_cache.json`.
3. **Token metadata**: `token_metadata.json` tracks `last_authenticated` and estimated expiry.

### Token Persistence

- `token_cache.json` is MSAL's serialized cache. Contains access and refresh tokens.
- After initial auth, all subsequent runs call `acquire_token_silent()` which uses the refresh token — no user interaction needed.
- When the refresh token expires (~90 days), user must re-run `auth_bootstrap.py`.
- The skill proactively warns when expiry is within 7 days.

### Checking Token Status

```bash
python3 main.py check-auth --env-file /path/to/.env
```

Reports: auth method, last authenticated, days until refresh token expiry, whether token acquisition works.
