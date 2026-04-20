# 04f - Saurav Deliverable: WebEx Intelligence Platform Architecture

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/saurav/webex_architecture_light 1.html and webex_arch_clarifications.md
**Source Date:** 2026-04-16 (proposed architecture and clarification questions)
**Document Set:** 04f (supplementary to Set 04, individual team member deliverable)
**Pass:** Full decomposition of Saurav's WebEx architecture proposal and design questions

---

## Overview

Saurav produced two documents: (1) an HTML architecture diagram for a "WebEx Intelligence Platform" showing current state and proposed architecture as a 6-lane horizontal flow, and (2) a markdown file with 10 specific engineering clarification questions about deployment model, token management, and integration paths.

Together, these cover the WebEx side of the engagement (Tasks 1 and 2) at the same depth Namita's work covers the build log side (Task 3).

---

## Current State (3 Components)

| Component | Input | Output | Status |
|-----------|-------|--------|--------|
| Pulse (Naga) | WebEx spaces | Database | Not deployed in NxOS. Service app status unknown. Deployment mechanism unclear. |
| Scribble (Naga) | Audio files | Text output (local Whisper + Pyannote) | Local only. Transcript source unclear. No DB integration. |
| Wall-E (Saurav) | WebEx spaces (webhook) | PostgreSQL | Code on dead Mac. Not deployed. Local Podman only. |

---

## Proposed Architecture (6 Layers)

### Layer 1: Data Sources (Modular)
- WebEx Chats / Spaces: messages, threads, files, rooms and direct spaces
- WebEx Meetings: transcripts via Scribble or built-in WebEx STT
- Future Connectors: email, GitHub, Jira (pluggable)

### Layer 2: Ingestion (Modular)
- **Service App:** OAuth scoped access, read messages permission, poll at configurable interval
- **Pre-processor:** Normalize, deduplicate, clean to LLM-ready format
- **Raw Snapshot:** Original source preserved for replay and reprocessing
- Both processed and raw paths run in parallel

### Layer 3: Storage
- Unified database: raw + processed snapshots
- Indexed for semantic search
- Timestamped history
- Multi-source, multi-use (single DB serves all downstream consumers)

### Layer 4: Access Layer
- MCP Server with user token baked in
- Search and query tools
- Context-aware retrieval
- Exposes DB to agents

### Layer 5: Application (Modular)
- Agentic WebEx App: action item extraction, meeting summaries, compliance monitoring, chat Q&A and analysis
- Swappable per use case (same DB + MCP, different application)

### Layer 6: Auth / User
- OAuth 2.0 user-level access control
- Data isolation per user (no blanket bot access)
- User access via WebEx interface or direct agent UI

---

## Key Design Principles

1. **Modularity:** Add new data source without touching downstream layers. Swap the agentic app while keeping same DB + MCP.
2. **Pulse integration shortcut:** If Pulse is already a deployed service app with a registered access token, skip the ingestion layer entirely and wire MCP onto their existing DB.
3. **Unified storage:** One database serves all consumers, avoiding the per-user duplication problem identified in Set 04's architecture discussion.

---

## Clarification Questions (10 Items)

### Architectural Questions (1-5)

1. **Polling vs webhooks:** Wall-E used webhooks (event-driven, no delay). The proposed Service App uses polling. Was polling a deliberate choice (simpler, no public endpoint needed on ADS), or should webhooks be an option?
2. **Pre-process vs raw:** Proposal saves both raw snapshot and processed output. Confirmed approach, or should raw only be stored with lazy processing on read?
3. **MCP user token scope:** Per-user deployment = token baked in per container (simple). Shared deployment = tokens must be session-scoped via OAuth. Which deployment model is confirmed?
4. **Scribble integration path:** Does Scribble output feed the same DB as the chat pipeline, or a separate branch? Depends on whether Scribble has a service layer or is still local-only.
5. **First use case for demo:** Any specific first use case to call out (meeting action items, space Q&A)? Helps frame the architecture concretely.

### Deployment Model Questions (6-10)

6. **Per-user vs shared:** Per-user = each user deploys own stack on ADS (simple, isolated, redundant scraping). Shared = one DB per space, session-scoped tokens (efficient, more complex auth). Which model does Srinivas expect? Or start per-user and evolve?
7. **Singular DB with user-scoped access:** Proposed: one shared DB, access enforced at MCP/tool layer via per-user OAuth tokens. Each MCP instance only returns rows the user's token has access to. Confirmed direction?
8. **Token security in MCP:** OAuth token stored server-side in MCP session, never in conversation context. Is there a preferred secret store for ADS deployments (Vault, env vars, Cisco-specific)?
9. **Plugin/module selection UX:** User picks data source from pre-built options, corresponding connector/MCP module is added, OAuth flow, ready to use. Who maintains the module registry?
10. **Pulse/Scribble as ADS Podman containers:** If already being built as ADS-deployable containers, the most efficient path is building the MCP on top of their existing DB output. Need confirmation from Naga on deployment target.

---

## Significance

This architecture proposal demonstrates that the team has thought through the full stack from data source to user-facing application, with specific attention to the deployment constraints of Cisco's ADS infrastructure, the OAuth/token security model, and the modularity requirements Srinivas has emphasized. The clarification questions show implementation-level thinking, not just box-and-arrow design.
