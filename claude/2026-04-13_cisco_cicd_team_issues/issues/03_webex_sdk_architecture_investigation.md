## Investigate WebEx SDK Architecture and Existing Cisco Implementations

### Description

Before building or demoing anything to Srinivas, the team needs to understand what Naga and Justin have already built for WebEx integration (Pulse and Scribble) and evaluate the current state against production requirements. This prevents duplicating existing work and positions the team to make informed architectural recommendations.

### Background

From meetings with Naga (week of 2026-04-07):
- **Pulse:** WebEx chat scraper that extracts messages and stores them in a database. Built 2-3 months ago with no updates since. No clear end-use case defined. Naga mentioned aspirations to expand to email, GitHub, and other platforms, but no concrete plan exists.
- **Scribble:** Audio-to-text transcription using Whisper and PanNote. Runs as a local Python script on a developer's machine. Not integrated into any system or deployed as a service. Last updated 1-2 weeks ago.
- Both are in DeepSite repos (access requires Srinivas approval).

From Saurav's independent exploration:
- WebEx developer portal offers multiple integration types: bots, service apps, integrations, agentic apps, OAuth flows
- Saurav has built a working bot (Volley) that scrapes WebEx messages into a Postgres DB with webhook support
- WebEx API is well-documented with sandboxes, samples, and a developer community
- Bot token vs user token distinction matters for privacy (bots only see messages where they are mentioned; user tokens access full chat history)

### Tasks

- [ ] Schedule meeting with Naga to review Pulse and Scribble codebases (once DeepSite repo access is granted)
- [ ] Record the meeting for documentation purposes
- [ ] Evaluate Pulse: What data does it extract? How is it stored? Is there an API or service layer? What is the data model?
- [ ] Evaluate Scribble: Is it just a Whisper wrapper script? Does it have any integration points? How is it deployed?
- [ ] Check with Naga and Justin: Do they already have provisioned bot access tokens or registered applications with Cisco IT?
- [ ] Document current-state architecture diagram for both Pulse and Scribble
- [ ] Identify gaps between current POC state and production requirements (service layer, OAuth, data isolation, scale)
- [ ] Determine which WebEx integration type is appropriate for the use case (service app vs bot vs agentic app)

### Key Considerations

- **Data isolation:** If using bot tokens, the bot only sees messages where it is tagged. If using user tokens, it accesses all chats that user has access to. A service-layer approach with OAuth per user is preferred for production to prevent data cross-contamination.
- **File handling:** WebEx chats contain shared files, not just messages. Determine whether file contents need to be scraped or just tracked by ID.
- **Do not demo to Srinivas before understanding what already exists.** If the team demos something that duplicates Naga's work, it creates a bad impression.
- **Frame existing Cisco work as POCs.** If Pulse and Scribble are not deployed, not integrated, and not used in production, they are POCs regardless of what the builders call them. Present this diplomatically through architecture diagrams, not verbal criticism.

### Acceptance Criteria

- [ ] Both Pulse and Scribble codebases reviewed (or verbal understanding documented if access is delayed)
- [ ] Current-state architecture diagram created for each
- [ ] Gap analysis completed: what exists vs what production requires
- [ ] Recommendation on integration type documented
