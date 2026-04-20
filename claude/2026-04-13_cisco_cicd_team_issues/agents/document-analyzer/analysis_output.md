# Document Analysis: Internal Team Meeting 2026-04-13

**Source:** internal_team_meet_4-13-2026.txt
**Meeting Date:** 2026-04-13 (Sunday)
**Duration:** ~1h 22m
**Attendees:** Colin Moore, Saurav Kumar Mishra, Srikar Madarapu, Namita Ravikiran Mane, Vaishali Sonawane

## Meeting Context

Internal BayOne team standup covering progress since Friday's Srinivas client meeting. Two workstreams: WebEx/Scribble (Saurav + Srikar) and Build Log Analysis (Namita + Vaishali). Meeting focused on debrief from Srinivas call, access blockers, and planning this week's deliverables for Friday.

## Transcription Notes

- "Bay One" / "Bay 1" / "P1" = BayOne Solutions
- "Basel" = Bazel (build system)
- "Sterni Bus" / "Singh" = Srinivas
- "Deepak" = likely Diwali/weekend, not a person in some contexts
- "Imperma" / "Imran" = Anupma (Cisco stakeholder)
- "Deep site" / "Deepak Site" = DeepSite (Cisco internal platform)
- "ADS" = Aurora Development Server (Cisco internal VM system)
- "Codex" / "Codecs" = likely refers to Cisco approved coding tools
- "A2G" = access-to-GitHub group at Cisco
- "DCN" = Cisco network switching tenant

## Actionable Topics Identified

### Topic 1: Cisco Tool Access Requests
**Priority:** HIGH (blocking other work)
**Owner area:** All team (except Vaishali)
- Request Codecs and GitHub Copilot via appstore.cisco.com
- Request Docker Desktop access (requires admin approval)
- Podman available without request (already used by Saurav)
- Complete Cisco GitHub access: get A2G group, then ping Justin for repo-level access
- Namita is the only person who succeeded at GitHub access; she needs to teach others

### Topic 2: BayOne GitHub Account Setup
**Priority:** HIGH (blocks issue assignment workflow)
**Owner area:** Namita (hasn't created yet), verify Srikar (just created)
- Colin needs everyone on BayOne GitHub to start assigning weekly tasks
- Colin will send issue links in Teams chat for tomorrow

### Topic 3: WebEx SDK Architecture Investigation
**Priority:** MEDIUM-HIGH
**Owner area:** Saurav, Srikar
- Determine what Naga and Justin have already built for WebEx integration
- Understand: service apps vs bots vs integrations vs agentic apps vs OAuth
- Avoid duplicating existing work before demoing to Srinivas
- Saurav identified need for service layer approach: scraper to DB, then MCP, then app/bot
- Need to consider: data isolation (OAuth per user vs bot token), file handling in chats
- Colin directive: record meetings with Naga/Justin, build architecture diagrams of current state AND proposed future state

### Topic 4: Scribble vs WebEx Transcription A/B Testing
**Priority:** MEDIUM-HIGH
**Owner area:** Srikar, Saurav
- Multi-tier comparison framework:
  1. Raw transcription quality (out-of-box Wispr vs out-of-box WebEx)
  2. Downstream AI usability (does the quality difference matter for LLM processing?)
  3. Prompt engineering compensation (glossary/term lookup table to improve WebEx quality)
  4. Cost and scale analysis (compute needed, concurrency, hosting model)
- Quick start: request Friday's call transcript from Naga's Scribble, compare with WebEx transcript of same meeting
- Key finding from Srikar: Scribble/Wispr is just a local Python script, not integrated into any system
- Colin coaching: present findings diplomatically; show current-state vs proposed-state architecture, let smart people draw conclusions

### Topic 5: Cisco Bot Compliance Policy
**Priority:** MEDIUM
**Owner area:** Saurav
- IT flagged Saurav's deployed bot as non-compliant
- Bot policy requires registration with Cisco org, thorough review
- Group size policy: bots cannot serve groups >100 people (NXOI group has 300+)
- Need to check with Naga/Justin if they already have provisioned bot access tokens
- Colin: raise to Srinivas as "help us navigate this" rather than trying to solve alone

### Topic 6: Build Log Mapping and Sample Collection
**Priority:** HIGH
**Owner area:** Namita (Vaishali async support)
- Map all available log types on ADS machine (not just Bazel)
- CI logs: Bazel (focus) - Gmake excluded per Srinivas directive
- CD logs: nightly builds - Justin has not shown this yet, need to investigate
- Determine: composite vs individual log files, sources, consistency
- Observation period: collect samples over multiple days (even passing logs are valuable)
- Automation: write script to collect logs rather than manual daily downloads
- Priority: get read-only access to NFS server with production (main) build logs
- Structure collected logs in folders: date, build type (nightly/user), source

### Topic 7: Build Log Data Model Design
**Priority:** MEDIUM
**Owner area:** Namita
- Star schema recommended for enabling downstream agentic AI
- Think about what to persist vs what to query live via MCP/git
- Key identifiers: SHA hashes (commits, PRs)
- Git lineage can be queried real-time rather than stored
- Consider: PR traceability, commit-level transparency (Cisco wants this)
- Colin will hold architecture working session with Namita + Vaishali this week

### Topic 8: Documentation Deliverables for Friday Srinivas Meeting
**Priority:** HIGH
**Owner area:** Both teams + Colin
- Architecture documentation: Colin will work with each sub-team
  - WebEx/Scribble architecture (Saurav + Srikar + Colin)
  - Build log analysis architecture (Namita + Vaishali + Colin)
- Presentations: Singularity training happening later today, each team will own their own slides going forward
- Key tone: current-state diagrams alongside proposed future-state, diplomatic framing

### Topic 9: Access Blocker Escalation Process
**Priority:** HIGH (process item)
**Owner area:** All team, Colin escalates
- Try to resolve access issues by Tuesday
- If still blocked after Tuesday, flag to Colin
- Colin escalates to Srinivas by Wednesday at latest
- Srinivas asked for early-in-week problem reports so he can help

### Topic 10: Document Podman Setup as Docker Alternative
**Priority:** LOW-MEDIUM
**Owner area:** Saurav
- Saurav already working: pulled PG17 image from AWS ECR (no Docker Hub auth needed), loaded into Podman
- All Docker commands map 1:1 to Podman commands
- Useful for entire team as local dev environment workaround
- Colin: show others how to do this

## Suggested Issue Grouping (for GitHub)

These could be grouped as ~8-10 issues rather than 10 individual topics. Topics 1, 2, and 9 are administrative/process and may be better as a single "access and setup" issue. Topics 3 and 4 are closely related (both WebEx/Scribble workstream). Topics 6 and 7 are part of the same build log workstream but distinct enough to separate.
