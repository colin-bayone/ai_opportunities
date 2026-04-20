# WebEx Architecture — Clarification Questions

## Original Design Questions

1. **Polling vs Webhooks**
   The Service App currently shows "poll at interval X". Wall-e used webhooks which are more efficient (event-driven, no delay). Was polling a deliberate choice (simpler, no public endpoint needed on ADS), or should webhooks be an option depending on deployment context?

2. **Pre-process vs Raw — both or one?**
   Current proposal saves both raw snapshot and processed output. Is this the confirmed approach, or should we save raw only and process lazily on read? Storing both adds storage overhead but makes reprocessing easier without re-scraping.

3. **MCP user token "baked in" — per-instance or session-scoped?**
   If deployed locally per-user on ADS, each user's MCP container holds their own token — straightforward and safe. If it becomes a shared team deployment, tokens need to be session-scoped (OAuth → server-side session → filtered queries). Which deployment model is confirmed?

4. **Scribble integration path**
   Is Scribble output (transcripts) meant to feed the same DB as the chat pipeline, or a separate branch/DB? Answer depends on whether Scribble has a service layer writing to a DB or if it's still local-only output.

5. **Agentic app — first use case for Friday**
   Any specific first use case to call out for Srinivas (e.g., "meeting action item extraction", "space Q&A")? Helps frame the demo scope and makes the architecture concrete rather than generic.

---

## Deployment Model Questions (from architecture discussion)

6. **Per-user local deployment vs shared team deployment**
   Srinivas's ask is for local deployment (ADS per-user, like DeepSight). Two models are possible:
   - **Per-user**: each user deploys their own stack (scraper + DB + MCP) on ADS. Token baked into their own container. Simple, isolated, but redundant scraping of the same spaces.
   - **Shared team**: one shared DB (scrape once per space), MCP server uses session-scoped tokens to filter queries per user. More efficient, but more complex auth layer.
   
   Which model does Srinivas expect? Or is the per-user model a starting point that evolves to shared?

7. **Singular DB with user-scoped access — confirmed direction?**
   Proposal is: one shared DB per deployment, access enforced at MCP/tool layer via per-user OAuth tokens (not at storage layer). Each user's MCP only returns rows their token has access to. Is this the agreed approach to avoid redundant scraping?

8. **Token security in MCP — implementation approach**
   Agreed the safe pattern is: OAuth token stored server-side in MCP session (never in conversation context), bot calls tools with query only, MCP resolves token internally. 
   - Is there a preferred secret store for ADS deployments (e.g., Vault, env vars, Cisco-specific secret manager)?
   - Should the OAuth consent flow be triggered from within the WebEx agentic app UI, or a separate web flow?

9. **Plug-in / module selection UX**
   Proposal: user picks data source (chats, meetings, etc.) from pre-built options → corresponding connector/MCP module is added → OAuth flow → ready to use.
   - Who manages the module registry (pre-built options)? Is this a Bayone-maintained catalogue or something Cisco controls?
   - Should users be able to combine multiple data sources into one agentic app, or one source per app instance?

10. **Pulse / Scribble as ADS Podman containers — confirmed?**
    If Pulse and Scribble are already being built as ADS-deployable containers, we may not need to rebuild the ingestion layer — just build the MCP on top of their DB output. This is the most efficient integration path. Need to confirm with Naga/Justin whether this is their intended deployment target.
