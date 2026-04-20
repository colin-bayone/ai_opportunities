# 02d - Srikar Deliverable: WebEx Recording Extraction (Technical Reference)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/srikar/WEBEX_REC_EXTRACTION.md
**Source Date:** 2026-04-15 (correlates with Srikar's 9:54 PM chat message about WebEx API owner-only limitation)
**Document Set:** 02d (supplementary to Set 02, individual team member deliverable)
**Pass:** Full decomposition of Srikar's WebEx recording extraction tool and API findings

---

## Document Overview

Srikar built and tested a Python script (`webex/extract_webex_recording.py`) that extracts four artifact types from WebEx meeting recordings: transcripts, summaries, action items, and audio. The document catalogs the end-to-end flow, API endpoints, what worked, 6 specific technical challenges encountered and resolved, and key limitations.

This work directly relates to Task 2 (Meeting Recording Transcriber) assigned by Srinivas on 4/2. While Saurav focused on Task 1 (WebEx Space Scraper/Wall-E), Srikar has been independently exploring the Task 2 space — specifically the API-driven extraction path that would complement or replace Naga's Scribble tool.

---

## The Script: `extract_webex_recording.py`

### Supported Commands

| Command | Purpose |
|---------|---------|
| `list` | List all recordings accessible to the current token |
| `extract` | Create a folder per recording and save all available artifacts |

### Extraction Flow

1. Set `WEBEX_ACCESS_TOKEN` environment variable
2. Validate token identity via `/v1/people/me`
3. Select a recording ID from list output
4. Extract command creates `<recording_id>/` folder and saves:
   - `transcript.txt` — from `meetingTranscripts` API, fetched via `txtDownloadLink`
   - `summary.txt` — from `meetingSummaries` API, HTML stripped to plain text
   - `action_items.txt` — from `actionItems` field in the summary response
   - `audio.<ext>` — from `temporaryDirectDownloadLinks` (optional, can skip with `--skip-audio`)
5. Review "not found" output for missing artifacts and decide fallback

### Command Examples

```bash
# List recordings
.venv/bin/python webex/extract_webex_recording.py list

# Full extraction
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <id>

# Skip audio (faster)
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <id> --skip-audio

# Custom output directory
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <id> --output-dir ./recordings
```

---

## API Endpoints Documented

| Artifact | Endpoint | Key Notes |
|----------|----------|-----------|
| Recording metadata | `GET /v1/recordings/{id}` | Returns `meetingId` used for all downstream queries |
| Transcript | `GET /v1/meetingTranscripts?recordingId=...` | Items include `txtDownloadLink` — a pre-signed URL for plain text download |
| Summary | `GET /v1/meetingSummaries?meetingId=...` | **Requires `meetingId`, not `recordingId`**. Content is HTML in `notes.content` field. |
| Action items | `actionItems` field on summary response | Empty list when WebEx AI found no action items |

**Critical API quirk:** The summary endpoint (`meetingSummaries`) rejects `recordingId` as a query parameter (returns HTTP 400). It requires `meetingId`, which must be extracted from the recording metadata response first. This is a non-obvious two-step dependency: recording → meetingId → summary.

---

## Technical Challenges and Resolutions (6 Items)

### 1. Transcript Field Contains a URL, Not Text

**Problem:** The recording metadata includes a `transcript` field that contains a pre-signed download URL, not the actual transcript text. Naively saving this field produces a file containing a URL.

**Resolution:** `normalize_text_payload()` now detects strings starting with `http://`/`https://` and skips them. URLs are fetched separately via `discover_text_urls()` → `fetch_resource()`.

### 2. Summary Endpoint Requires meetingId, Not recordingId

**Problem:** `meetingSummaries` returns HTTP 400 when queried with `recordingId`. The API documentation was not clear about this requirement.

**Resolution:** `meetingId` is automatically extracted from the recording metadata response and used for all summary/transcript queries.

### 3. API Response Collection Structure Not Parsed Correctly

**Problem:** API responses return collections (`{"items": [...]}`) but the initial implementation only saw the wrapper object, not the individual items inside.

**Resolution:** Each item in the `items` array is now appended to `sources_to_scan` individually.

### 4. Summary Content Is HTML, Not Plain Text

**Problem:** `meetingSummaries` returns the `notes.content` field as an HTML string, not plain text.

**Resolution:** `extract_summary()` detects `notes.content`, strips HTML tags using `html.parser`, and converts block elements to newlines for readable output.

### 5. Public Recording Link Does Not Grant API Access

**Problem:** Password-protected `ldr.php` links (like the DeepSight training video shared on 4/1) allow a viewer to watch the recording but do not grant API artifact access. The API requires the host owner's token or an admin token with org-wide scope.

**Resolution:** This is a fundamental limitation, not a bug. Must use the host's own access token.

### 6. Empty Recordings List Despite Valid Token

**Problem:** `/v1/recordings` returns an empty list when the token user does not own the recording. The token is valid (identity check passes) but has no recordings to list.

**Resolution:** Use the host's own access token, or an admin token with broader scope.

---

## Key Limitations

1. **Owner-only access.** Summary, action items, and transcripts require the meeting host's token or an org-admin token. A regular participant cannot extract these artifacts. This confirms Srikar's 4/15 chat message: "Using Webex API only owner of the meeting using access token can extract the recording, summary, action items, Transcript."

2. **WebEx AI dependency.** Summary and action items require WebEx AI to have processed the recording. Short meetings or older recordings may have no AI artifacts. There is no way to trigger AI processing after the fact.

3. **Transcription must be enabled.** Transcript availability depends on whether WebEx transcription was enabled for the meeting. If it was not turned on, there is no transcript to extract.

4. **Password-protected links are not API-equivalent.** Having a recording link and password (like the DeepSight training video) does not enable API extraction. The API enforces ownership/admin permissions independently from link-based sharing.

---

## Implications for Task 2 and the Scribble Question

### API Path (Srikar's Approach)
- **Works when:** You own the meeting or have admin access
- **Produces:** Transcript, summary, action items, audio — structured and ready to use
- **Fails when:** You are not the meeting owner and do not have admin scope

### Scribble Path (Naga's Approach)
- **Works when:** You have the audio file, regardless of who owns the meeting
- **Produces:** Transcript only (via Whisper/Pyannote)
- **Fails when:** No audio file available

### Comparison

| Dimension | WebEx API (Srikar) | Scribble (Naga) |
|-----------|-------------------|-----------------|
| Transcript | Yes (if transcription was enabled) | Yes (from any audio file) |
| Summary | Yes (if WebEx AI processed it) | No |
| Action items | Yes (if WebEx AI processed it) | No |
| Audio download | Yes | N/A (requires audio as input) |
| Access constraint | Owner/admin token required | Audio file access required |
| Processing latency | Immediate (already processed by WebEx) | Requires Whisper/Pyannote processing time |
| Setup complexity | Token management, API integration | Audio pipeline, model hosting |

### Strategic Implication

The two approaches are complementary, not competing:
- **For team's own meetings:** Use the API path. The meeting organizer's token can extract all artifacts immediately. This is what Colin directed on 4/16 ("manual transcript download available now").
- **For other people's meetings:** The API path fails (owner-only). Scribble can work if the audio file is obtainable through other means.
- **For automation at scale:** A service account with admin scope could theoretically extract from any meeting, but this requires Cisco IT to provision such an account. Whether this is achievable is an open question for Srinivas.

This analysis gives the team a data-driven position for the Srinivas discussion about Task 2 scope: both tools have a role, but the use cases are different. The question for Srinivas is whether the automation target is "our own meetings" (API is sufficient) or "any meeting in the CI/CD team space" (may need admin scope or Scribble as fallback).

---

## Connection to Saurav's Wall-E Bot

Srikar's recording extraction tool and Saurav's Wall-E bot address different WebEx data types:

| Data Type | Tool | Status |
|-----------|------|--------|
| WebEx space messages (chat) | Wall-E (Saurav) | Working, deployed |
| WebEx meeting recordings (audio, transcript, summary) | extract_webex_recording.py (Srikar) | Working, tested |

Together, they cover the two primary WebEx data sources. If combined into a unified pipeline, the team could offer: chat scraping + meeting transcript extraction + summary/action item extraction as a complete WebEx intelligence layer.
