# Webex Recording Extraction (Transcript, Summary, Action Items)

## Purpose
This document captures the process to extract recording artifacts from Webex, including what worked, what failed, and operational limitations.

## Scope
- Script: `webex/extract_webex_recording.py`
- Supported flows:
  - `list`: list recordings accessible to the token
  - `extract`: create a folder named with the recording ID and save artifacts

## End-to-End Flow Followed
1. Set `WEBEX_ACCESS_TOKEN` in shell.
2. Validate token identity using `/v1/people/me`.
3. Pick a recording ID from list output.
4. Run extract command:
   - Create folder `<recording_id>/`
   - Save `transcript.txt` — fetched from `meetingTranscripts` `txtDownloadLink`
   - Save `summary.txt` — fetched from `meetingSummaries` (HTML stripped to plain text)
   - Save `action_items.txt` — extracted from the `actionItems` field of the summary response
   - Download media as `audio.<ext>` when URL is available
5. Review missing artifacts output (`not found`) and decide fallback path.

## Commands Used
```bash
export WEBEX_ACCESS_TOKEN="<token>"

# List recordings
.venv/bin/python webex/extract_webex_recording.py list

# Extract artifacts for a recording
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <recording_id>
# Skip audio download (faster):
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <recording_id> --skip-audio
# Custom output directory:
.venv/bin/python webex/extract_webex_recording.py extract --recording-id <recording_id> --output-dir ./recordings
```

## API Endpoints Used
| Artifact | Endpoint | Notes |
|---|---|---|
| Recording metadata | `GET /v1/recordings/{id}` | Contains `meetingId` used for all downstream queries |
| Transcript download | `GET /v1/meetingTranscripts?recordingId=...` → `txtDownloadLink` | Items include a ready-to-fetch plain-text URL |
| Summary | `GET /v1/meetingSummaries?meetingId=...` | Requires `meetingId`, not `recordingId`; content is HTML, stripped to plain text |
| Action items | `actionItems` field on the summary response item | Empty list when Webex AI found none |

## What Worked
- Transcript extraction via `meetingTranscripts` `txtDownloadLink` (fetched as plain text with auth).
- Summary extraction from `meetingSummaries` — `notes.content` HTML field stripped to readable plain text.
- Action items from the `actionItems` field on the summary item.
- `meetingId` auto-detected from recording metadata — no need to pass `--meeting-id` manually.
- Audio download via Webex temporary direct download links (`temporaryDirectDownloadLinks`).
- One folder per recording ID, all artifacts written atomically.

## Challenges Faced
1. **Transcript file contained a raw URL instead of text**
   - Recording metadata includes a `transcript` field that is a pre-signed download URL, not the transcript text.
   - Fix: `normalize_text_payload` now skips strings that start with `http://`/`https://`; URLs are fetched separately via `discover_text_urls` → `fetch_resource`.

2. **Summary not found despite being available**
   - `meetingSummaries` returns HTTP 400 when queried with `recordingId`; it requires `meetingId`.
   - Fix: `meetingId` is now automatically extracted from the recording metadata and used for all summary/transcript queries.

3. **Summary response items not scanned individually**
   - API responses are collections (`{"items": [...]}`); the extractors only saw the wrapper object, not the individual items.
   - Fix: each item in `items` is now appended to `sources_to_scan` individually.

4. **Summary content is HTML**
   - `meetingSummaries` returns `notes.content` as an HTML string.
   - Fix: `extract_summary` now detects `notes.content`, strips HTML tags using `html.parser`, and converts block elements to newlines.

5. **Public recording link vs API identity mismatch**
   - Password-protected `ldr.php` links allow viewer access but do not grant API artifact access.
   - API access requires the host owner token (or an admin token with org-wide scope).

6. **Empty recordings list with valid token**
   - `/v1/recordings` returns empty when the token user does not own the recording.
   - Use the host's own access token, or an admin token.

## Key Limitations
- Summary and action items require Webex AI to have processed the recording. Short or older meetings may have no AI artifacts.
- Link + password alone is not a reliable source for structured transcript/summary/action-items via API.
- Recording visibility is constrained by token user permissions (host or admin required).
- Transcript availability depends on whether Webex transcription was enabled for the meeting.

