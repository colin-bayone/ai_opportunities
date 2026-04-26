---
name: fido
description: |
  Fetch It, Deliver Output — retrieve Microsoft Teams meeting transcripts via Graph API and save as local files.
  WHEN to use: User asks to grab/fetch/get meeting transcripts, list meetings,
  find meetings with a person, search by meeting name, check upcoming calendar,
  get meeting stats, or retrieve transcripts from a date range.
  WHEN NOT to use: Summarizing transcripts, Django app transcript features, non-Microsoft meetings.
hooks:
  Stop:
    - hooks:
        - type: command
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/fido/scripts/fido-workflow.py"
          timeout: 10000
          statusMessage: "Checking FIDO workflow compliance..."
---

# FIDO — Fetch It, Deliver Output

Retrieve Microsoft Teams meeting transcripts via Graph API. Standalone — no Django, no database.

## Hard Rules

1. **Check dependencies first.** Run `python3 {baseDir}/scripts/check_deps.py` before any operation. If it fails, tell user to run `pip install -r {baseDir}/scripts/requirements.txt`.
2. **Check auth before any API call.** Run `python3 {baseDir}/scripts/main.py check-auth --env-file <path>`. If it fails, guide user through auth setup.
3. **Never store secrets in skill files.** API keys, tokens, and credentials live ONLY in the user's .env file and token_cache.json. No exceptions.
4. **Ask, don't churn.** If a person's email is unknown, ASK the user. If a meeting can't be found, REPORT what was searched and ask for clarification. Never guess.
5. **Smart timing for missing transcripts.** When no transcript is found, check how long ago the meeting ended:
   - < 30 min ago: "Transcript may still be processing. Try again in 15-20 minutes."
   - 30-90 min ago: "Not yet available. If transcription was enabled, try again shortly."
   - > 90 min ago: "Transcription was likely not enabled for this meeting."
6. **Scripts run with python3, never poetry.** All invocations use `python3`, not `poetry run`.
7. **Save contacts after resolution.** When a new person/email is resolved, save to contacts.json immediately.
8. **Number same-day meetings.** Multiple meetings on the same day with the same person get `_01`, `_02`, etc. ordered chronologically.
9. **Env file location must be provided by user.** Always ask the user where their .env file is. Never assume a location.
10. **Token cache and contacts must be gitignored.** Warn user if these files could be tracked by git.
11. **Never make changes without user approval.** Do not decide on a "simpler path" and act on it. When there are options (auth flows, config changes, troubleshooting approaches), present all options to the user and let them choose. You do not get to make these decisions.
12. **Troubleshoot auth failures using the reference doc.** When auth fails, read `{baseDir}/references/auth_troubleshooting.md` and walk the user through their options. Do not guess at fixes.
13. **Deduplication.** Already-downloaded transcripts are skipped automatically. Do not re-fetch unless user explicitly asks.

## Prerequisites

### Step 1: Check Dependencies

```bash
python3 {baseDir}/scripts/check_deps.py
```

If missing packages, tell the user:
```bash
pip install -r {baseDir}/scripts/requirements.txt
```

### Step 2: Environment File

Ask the user for the path to their `.env` file. Required variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `MICROSOFT_CLIENT_ID` | Azure app registration client ID | Yes |
| `MICROSOFT_CLIENT_SECRET` (or `MICROSOFT_SECRET`) | Azure app registration secret | Yes |
| `AZURE_TENANT_ID` | Azure AD tenant ID | Yes |
| `GRAPH_API_SCOPES` | Comma-separated scopes | No (defaults provided) |
| `MICROSOFT_USER_ID` | Azure AD user object ID (client credentials only) | Only for client creds |
| `DEFAULT_SEARCH_DAYS` | How far back to search | No (default: 30) |

Show them the template at `{baseDir}/.env.example` if they need to create one.

### Step 3: Authentication

One-time setup — device code flow (recommended):

```bash
python3 {baseDir}/scripts/auth_bootstrap.py --env-file /path/to/.env
```

Prints a URL and code. User opens URL in their Windows browser and enters the code.
Token cached to `claude/meeting_transcripts/token_cache.json`. Valid for ~90 days.

Requires "Allow public client flows" = Yes in Azure Portal > App Registration > Authentication.

For client credentials flow (fully unattended, requires admin setup):
```bash
python3 {baseDir}/scripts/auth_bootstrap.py --env-file /path/to/.env --client-credentials
```

## Operations

### Fetch Transcripts with a Specific Person

```bash
python3 {baseDir}/scripts/main.py fetch \
  --env-file /path/to/.env \
  --person "email@example.com" \
  --start-date 2026-04-01 \
  --end-date 2026-04-16
```

Fetch the most recent meeting only:
```bash
python3 {baseDir}/scripts/main.py fetch \
  --env-file /path/to/.env \
  --person "email@example.com" \
  --last
```

**Exclusive mode** — only 1:1 meetings (no group meetings):
```bash
python3 {baseDir}/scripts/main.py fetch \
  --env-file /path/to/.env \
  --person "Shalini" \
  --exclusive \
  --start-date 2025-12-01 --end-date 2026-04-16
```

`--only` is shorthand for `--exclusive`. `--inclusive` is the default (any meeting where the person is an attendee, even group meetings).

The `--person` flag accepts an email address OR a name from the contacts glossary.

### Fetch ALL Transcripts in a Date Range

No `--person` flag = fetch all meetings with transcripts:

```bash
python3 {baseDir}/scripts/main.py fetch \
  --env-file /path/to/.env \
  --start-date 2026-04-10 \
  --end-date 2026-04-16
```

### Search Meetings by Name

Find meetings by subject, then optionally fetch a transcript:

```bash
# Search only (shows results, no fetch)
python3 {baseDir}/scripts/main.py search \
  --env-file /path/to/.env \
  --query "Cisco Team Sync" \
  --start-date 2026-04-16 --end-date 2026-04-16

# Search and fetch transcript
python3 {baseDir}/scripts/main.py search \
  --env-file /path/to/.env \
  --query "Sprint Review" \
  --start-date 2026-04-01 --end-date 2026-04-16 \
  --fetch
```

When `--fetch` is used: if one match, auto-selects it. If multiple, prompts user to choose.
Search results show subject, date/time, duration, attendees, and online status.
**Present results to the user first** — do not auto-fetch without `--fetch`.

### List Meetings

Returns a formatted table of meetings — subjects, attendees, times, durations:

```bash
python3 {baseDir}/scripts/main.py list \
  --env-file /path/to/.env \
  --start-date 2026-04-10 \
  --end-date 2026-04-16
```

**Export to file:**
```bash
# Save as CSV
python3 {baseDir}/scripts/main.py list \
  --env-file /path/to/.env \
  --start-date 2026-04-10 --end-date 2026-04-16 \
  --save --format csv

# Save as markdown
python3 {baseDir}/scripts/main.py list \
  --env-file /path/to/.env \
  --start-date 2026-04-10 --end-date 2026-04-16 \
  --save --format md
```

Files saved to `claude/meeting_transcripts/exports/`.

### Meeting Statistics

Summary stats for a date range — meeting count, hours, top attendees, day-of-week breakdown:

```bash
python3 {baseDir}/scripts/main.py stats \
  --env-file /path/to/.env \
  --start-date 2026-03-17 \
  --end-date 2026-04-16
```

Default range is last 30 days if no dates specified.

### Upcoming Meetings (Calendar Overview)

"What's on my calendar?" — grouped by day with attendees and online status:

```bash
# Next 7 days (default)
python3 {baseDir}/scripts/main.py upcoming --env-file /path/to/.env

# Next 3 days
python3 {baseDir}/scripts/main.py upcoming --env-file /path/to/.env --days 3
```

### Contact Management

```bash
# Look up a person by name
python3 {baseDir}/scripts/main.py contacts --lookup "Ambar"

# Add a new contact
python3 {baseDir}/scripts/main.py contacts --add "Ambar Singh" "ambar@bayone.com"

# List all saved contacts
python3 {baseDir}/scripts/main.py contacts --list
```

### Check Authentication Status

```bash
python3 {baseDir}/scripts/main.py check-auth --env-file /path/to/.env
```

Reports: auth method, last authenticated, days until refresh token expiry, whether token acquisition works.

## Output Structure

All output at `claude/meeting_transcripts/` from the project root:

```
claude/meeting_transcripts/
├── contacts.json                          # Name-to-email glossary
├── token_cache.json                       # MSAL token cache (gitignored)
├── token_metadata.json                    # Auth timestamps, user email, expiry
├── exports/                               # Exported meeting lists
│   └── 2026-04-14_to_2026-04-16_meetings.csv
├── shalini/                               # Person-based folder
│   ├── 2025-12-09/                        # Date subfolder
│   │   ├── shalini-and-colin-weekly-11_01.txt
│   │   ├── shalini-and-colin-weekly-11_01.vtt
│   │   └── shalini-and-colin-weekly-11_01_meta.json
│   └── 2025-12-16/
│       └── ...
└── cisco-team-sync/                       # Subject-based folder (no person filter)
    └── 2026-04-16/
        └── cisco-team-sync_01.txt
```

## Handling User Requests

When the user asks for transcripts:

1. **Check prerequisites** — Run check_deps.py. Ask for env file path. Run check-auth.
2. **Resolve person** — If user said a name, check contacts.json. If not found, ask for email. Save new contact.
3. **Determine date range** — Parse natural language: "last week", "today", "yesterday", "April 1-15". Default: last 30 days for `--last` queries.
4. **Choose the right command:**
   - "Grab meetings with X" → `fetch --person X`
   - "Find the meeting called Y" → `search --query Y`
   - "What's on my calendar?" → `upcoming`
   - "How many meetings this month?" → `stats`
   - "List everything from last week" → `list --start-date --end-date`
5. **Report results** — Tell user what was found. Present tables/stats in chat.
6. **Handle failures gracefully** — Apply smart timing rules. Report clearly. Ask user what to do next.

## References

- `{baseDir}/references/auth_troubleshooting.md` — Auth flows, common errors, delegated vs application permissions, WSL2 considerations, token lifecycle

## Script Reference

| Script | Purpose |
|--------|---------|
| `check_deps.py` | Verify pip dependencies are installed |
| `auth_bootstrap.py` | One-time interactive authentication |
| `graph_client.py` | Standalone Graph API client with MSAL token management |
| `calendar_search.py` | Find meetings by person, date, subject. Stats and formatting. |
| `transcript_fetcher.py` | Fetch VTT transcripts from Teams, date-match for recurring meetings |
| `vtt_parser.py` | Parse VTT subtitle format into structured utterances |
| `transcript_formatter.py` | Format parsed transcript to readable text/markdown |
| `contacts.py` | Name-to-email glossary management |
| `main.py` | CLI orchestrator: fetch, search, list, stats, upcoming, contacts, check-auth |
