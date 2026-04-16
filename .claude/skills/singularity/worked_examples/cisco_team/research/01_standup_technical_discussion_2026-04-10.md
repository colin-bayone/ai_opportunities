# 01 - Standup: Technical Discussion and Architecture Insights

**Source:** /cisco/cicd/team/source/internal_standup_2026-04-10.txt (supplemented by Namita's build log analysis document)
**Source Date:** 2026-04-10 (Friday standup, pre-Srinivas meeting)
**Document Set:** 01 (First team sub-singularity set)
**Pass:** Technical findings, architecture approach, tool evaluation

---

## Build System Landscape

### Two Build Automation Tools

The Cisco NX-OS platform operates on two distinct build systems, which is itself a significant finding -- having different build systems for dev and prod represents substantial technical debt.

1. **Gmake (Legacy)**
   - Used to build the **nx_main** repo (production branch)
   - Cisco is actively moving away from Gmake
   - Old repos continue to be built with Gmake
   - Represents the production build pipeline

2. **Bazel (Current)**
   - Used to build the **nx_dev** repo (development branch)
   - The direction Cisco is heading for all builds
   - Justin explicitly recommended the team focus on Bazel, stating Gmake logs will become outdated
   - Bazel has a finite, documentable set of possible error codes -- this is architecturally significant (see Tiered Approach below)

### Colin's Observation on Build System Divergence

Colin flagged that running different build systems for dev (Bazel) vs. prod (Gmake) is "honestly kind of crazy" and likely represents significant code debt Cisco wants to resolve. He suggested the team could offer Gmake-to-Bazel conversion as a code modernization effort -- a natural expansion opportunity that could be raised with Srinivas if the team is prepared to discuss it.

---

## Log Infrastructure

### Storage and Access

- **Storage medium:** NFS (Network File System)
- **NFS location:** `/auto/ins-bld-tools/branches/nx_main/nexus/togs/`
- **Access method:** ADS (Application Development Server) machines only -- no Kafka, no alternative storage paths
- **Access types:**
  - Temporary ADS access: 4-week window, used for testing (Namita received approval morning of standup)
  - Permanent ADS alias machine: Requires tenant configuration under DCN Switching in managecisco.com (tenant not yet available to team; support engagement ongoing)
- **Access is individual**, not team-wide -- each person must apply separately

### Retention Policy

- **Failed build logs:** Retained approximately 3-5 days, then deleted
- **Official nightly build logs:** Retained for up to 5 years
- **User/developer build logs:** Temporary, limited retention

### Log Characteristics

- **Size:** 300K to 500K lines per individual log file
- **Files per build:** 12-15 log files generated from a single Bazel build
- **Build duration:** Some builds run 1.5 to 2 hours; others can scale to 6-8 hours
- **Build queue:** Approximately 200 builds in queue at any given time, with manual priority selection
- **Build portal metadata** (stored in MySQL): Build number, build date, expiry date, LOC changes (insertions/modifications/deletions), pass/fail status, sanity check count, comments, and committer

### Log File Structure -- Open Questions

Saurav raised critical questions about log file organization that remain unanswered:
- Are the 12-15 files generated consistently for every build, or does the count vary by build scope?
- Are files divided by build stage, by log type (auth, network, etc.), or by some other scheme?
- The team does not yet have direct visibility into the file structure -- this requires ADS access to confirm

---

## Justin's Existing Workflow (Build Log Analysis)

### What Justin Built

Per Namita's account and her supplementary document, Justin's existing workflow operates as follows:

1. **Python script** extracts errors from build logs -- but only a subset ("top few," "initial ones," not comprehensive)
2. Extracted errors are passed to an **LLM** for analysis
3. The LLM **generates a summary** and lists approximately 10-50 errors
4. The LLM **suggests code fixes** and applies them automatically to a separate workspace
5. A **build verification step** runs to confirm the fixes resolve the errors
6. There is potential (not yet implemented) to **automate PR creation** for verified fixes to official builds

Justin showed Namita a "prune.error" file containing the error summary output. He did not demonstrate the Python script itself or the full end-to-end pipeline live. The script and related code exist in a PR on the Cisco internal GitHub: `https://wwwwin-github.cisco.com/DCN/tools/pull/642`.

### Colin's Critique: POC, Not Production

Colin was explicit that Justin's work, while valuable as a proof of concept, is not production-ready. Specific gaps identified:

1. **Incomplete error extraction:** The Python script captures only a subset of errors. Colin noted: "You could have 100 errors and they could all be high severity, and if you only fix the top five, you're going to fail again."

2. **No structured error storage:** Errors are likely not being persisted. Colin assessed: "How is it storing the errors? It's probably not. It's probably just running some script and then calling a language model with the top three or top N errors."

3. **Missing guardrails and governance:** No human-in-the-loop approval process. No rules about what the LLM is allowed to modify. Saurav pointed out: "What exactly the LLM has access to in that workspace? What type of context we are passing with the error message?" Colin described it as "the very scary version" -- "they've essentially just made Cursor" without proper scaffolding.

4. **No tool calling or structured interaction:** The LLM interaction is a simple prompt-response pattern, not an agentic workflow with tool calling, validation loops, or structured outputs.

5. **No validation framework:** Saurav asked whether they have a working POC with passing builds and how they measure success. Namita confirmed Justin did not provide information about validation methodology.

6. **Log slicing problem unsolved:** Colin identified that even the initial regex/pattern matching step has an unsolved problem -- after finding an error, how do you determine where the relevant log snippet begins and ends? This is likely why errors aren't stored in MySQL: "not just because they're long, but because they weren't sure how to slice up the log after it was created."

### Strategic Framing for Srinivas

Colin framed the approach to Srinivas carefully: acknowledge Justin's work as a valuable POC, then demonstrate what production looks like. Key quote: "Divakar and his team, I appreciate what they did, but that was the POC. We're going to show you what production looks like."

---

## Colin's Three-Tier Architecture Approach

Colin outlined his standard approach for classification/detection problems, applied to build log error analysis:

### Tier 1: Rule-Based / Deterministic

- Regex pattern matching against known error codes
- Bazel has a **finite number of possible errors** documented in its official docs
- Colin proposed: scrape Bazel documentation to extract all possible error codes, run the scraper weekly to detect new error codes from releases
- "It's actually possible to do this entire thing without even using AI at all" for Tier 1 detection
- This tier alone would outperform Justin's current Python script approach

### Tier 2: NLP/ML (Smaller Models)

- For errors that require more than simple pattern matching
- Not mandatory for every error -- only applied where Tier 1 is insufficient
- Handles cases where log content is ambiguous or requires contextual understanding
- Acts as a second gate in the classification pipeline

### Tier 3: LLM (Complex Cases)

- Reserved for genuinely complex errors requiring reasoning
- Where the LLM comes in for suggesting and applying fixes
- Should have proper guardrails, tool calling, and human approval mechanisms
- The fix suggestion and application workflow that Justin prototyped belongs here, but with proper scaffolding

### Key Principle

Colin emphasized engineering pragmatism: "Sometimes people make these problems harder than they are." The approach starts with the simplest effective solution and escalates only when necessary. Each tier handles the errors it is best suited for, avoiding the cost and risk of sending everything to an LLM.

---

## Log Sampling Strategy

Colin provided specific methodological advice for initial log analysis:

### Temporal Sampling Approach

Select logs from three time periods:
1. **Oldest available** logs
2. **Midpoint** of the system's operational history
3. **Newest** logs

### Purpose: Detect Format Changes

- Log formats may change at major version boundaries of the build tool
- If format changed (e.g., hypothetically in 2015, 2020, 2025), each era may need its own processing workflow
- Historical format variants are one-time efforts -- "you don't need to build a complete workflow that goes and solves every possible variation of every possible log"
- After identifying change points, the ongoing processing workflow only needs to handle the current format

### Source of Truth Verification

Colin emphasized verifying whether logs have been modified from their original form:

- "What is your real source of truth here? Have the logs in any way been modified from the original creator of the log?"
- Teams sometimes build custom layers that truncate, trim, or selectively include fields
- If logs are pre-processed before the team sees them, the finite-error-set assumption may not hold: "we might have more systems feeding into this than we expect"
- User-facing logs (developer builds) may contain different errors than production logs (nightly builds) -- these should be analyzed separately

### Practical Advice on Log Collection

Given the 3-5 day retention for failed builds, Colin recommended:
- Go to the NFS location daily and grab a few new log files
- Accumulate approximately one week of data to assess diversity of file types and formats
- Do not be intimidated by log size -- the first step is chunking them into structured format, similar to a RAG pipeline

---

## WebEx Scraper / Communication Tools

### Naga's Existing Tools

Srikar reported on his meeting with Naga, who showed two tools he built, both housed in the DeepSight repos:

#### Pulse (WebEx Chat Scraper)
- Scrapes/extracts data from WebEx chat
- Built 2-3 months ago
- No commits or updates in approximately 2 months
- **No defined end use case** -- Naga "didn't have any clear vision on where to go from there"
- Naga expressed aspirations to expand beyond WebEx to email, GitHub, Splunk, and other platforms

#### Scribble (Audio-to-Text Transcription)
- Converts audio files to text using **Whisper** and **Pannote**
- Naga claims Whisper produces more accurate transcription than native WebEx transcription
- More recent activity -- commits approximately 1-2 weeks ago
- Srikar noted Scribble is intended as a general audio-to-text tool, not WebEx-specific
- Both tools are designed to be independently deployable on any ADS server

### Colin and Saurav's Assessment

Both Colin and Saurav questioned the fundamental value proposition:

1. **Pulse:** Saurav's critique was direct: "What does it do for me? Scrape my messages and save it to the DB? Then what?" There is no downstream workflow, no analysis, no actionable output.

2. **Scribble:** Colin questioned why a custom transcription solution is needed when WebEx already provides native transcription. The improvement from Whisper may not justify the additional API cost and maintenance. Saurav noted that WebEx transcription quality is actually good -- most errors are limited to proper names, which can be solved with a glossary/lookup table approach rather than a separate transcription pipeline.

3. **Scope creep concern:** Naga mentioned expanding to email, GitHub, and other platforms. Colin flagged this as premature: "If it doesn't even work for the WebEx meetings for scraping for Pulse, what's the point?" Srinivas's original scope assignment was WebEx first, meetings second.

### Colin's POC Assessment

Colin applied the same POC framework as with Justin's work: "If people aren't using them, they're POCs. That's my rule of thumb. If it's used in production and people depend on it for business, then it's not a POC."

### Political Dynamics with Naga

Similar to the Divakar situation on build logs, Naga's scope and ownership is unclear. Colin diagnosed the likely cause: "Someone who's important in the organization mention something in passing to someone who's usually earlier in their career and very eager." Naga likely started building without a formal project scope or objective. The team needs Srinivas to clarify scope and ownership without antagonizing Naga's team.

---

## Saurav's Volley Bot (WebEx SDK Implementation)

### What Saurav Built

Saurav demonstrated a working WebEx bot called **Volley** built using the **WebEx SDK**:

- **Architecture:** WebEx bot + personal user token for extended access + PostgreSQL backend (Dockerized PG image)
- **Functionality demonstrated:**
  - Ping/health check
  - On-demand chat scraping: scrapes all messages in a WebEx space and stores them in PostgreSQL
  - Report generation: breakdown of messages by human vs. bot, total people count, message categorization
  - Transcript retrieval: pulls stored messages from the database for display
  - Filtering: ability to exclude bot messages, filter by user, filter by room
  - Webhook support: real-time event processing capability
- **Permissions model:** Bot-level access only sees messages where it is @mentioned; user token access enables full chat history. Granular permissions available -- restrict to specific rooms, specific users, specific chats
- **Multi-room capable:** Can scrape different rooms/channels individually or in parallel

### WebEx Developer Platform Assessment

Saurav shared his assessment of the WebEx developer ecosystem:
- Well-documented APIs with examples, sandboxes, and dev community
- App types available: Integration, Bot, User, **Agentic App** (MCP server registration), Service/org-wide bot
- Personal tokens available for development
- Saurav rated WebEx development experience as "100 times better than Teams"
- Created reference documents with verified endpoints, methods, and parameters -- shared with the team

### Relevance to Naga's Work

Saurav's Volley bot appears to replicate and potentially exceed what Naga built with Pulse, constructed in a fraction of the time. This validates both the feasibility of the WebEx scraping task and the team's ability to deliver quickly. Colin noted: "That's already close to something that he wanted. So very fast."

### Agentic App Capability

Saurav highlighted the WebEx **Agentic App** type, which supports MCP server registration. This is directly relevant to Naga's aspirations about multi-platform integration -- rather than building custom scrapers for each platform, MCP servers could be registered as tool providers for a WebEx-based agent. This was not explored by Naga's team.

---

## Architecture Decision Status

### Explicitly Preliminary

Colin was deliberate about not rushing architectural commitments:

- "We don't want to rush into it, but at the same time we can give something as a kind of a high level overview"
- Architectural diagrams will be created collaboratively next week using the team's presentation tooling
- Divakar expects an architecture document -- Colin noted Divakar "is not an AI person, he's a build person," so the document should be pitched accordingly
- Rearchitecture assessment should be deferred until the team has reviewed existing code: "Saying it like that will keep you out of the crosshairs"

### Questions for Srinivas (Prepared During Standup)

The team prepared these items for the Srinivas meeting later that day:

1. **Divakar conflict:** Divakar was unaware the team was assigned build log analysis work and perceived it as duplicating his team's effort. Request: Srinivas to clarify ownership and collaboration model.

2. **Gmake vs. Bazel scope:** Justin recommended Bazel-only focus. Does Srinivas want the team to also handle Gmake? Ancillary offer: Gmake-to-Bazel conversion assistance as a code modernization effort.

3. **Scribble justification:** Why build custom audio-to-text when WebEx provides native transcription? Are there non-WebEx audio sources that justify Scribble's existence?

4. **WebEx scraper scope:** Srinivas originally scoped WebEx + meetings. Naga mentioned email, GitHub, Splunk, etc. What is the immediate scope? What is the eventual scope? The answer determines whether the current architecture needs to be connector-friendly from the start.

5. **DeepSight repo access:** Pulse and Scribble repos are under DeepSight; access requires Srinivas's authorization.

6. **Build optimization opportunity:** Builds taking 6-8 hours with a queue of 200 and manual priority selection. Is build optimization in scope? Silent failures in the pipeline suggest Airflow/orchestration issues worth investigating.

---

## Key Technical Insights Summary

| Topic | Finding | Implication |
|-------|---------|-------------|
| Bazel error codes | Finite, documentable set from official docs | Tier 1 deterministic approach is viable for majority of error detection |
| Log size | 300K-500K lines, 12-15 files per build | Chunking/structured parsing is prerequisite; do not send raw to LLM |
| Log retention | 3-5 days for failed builds | Must collect samples proactively; cannot do historical analysis on failures |
| Justin's workflow | POC-level: partial extraction, no storage, no guardrails | Clear opportunity to demonstrate production-grade approach |
| Naga's tools | No defined end use case, no downstream workflow | Need Srinivas to define scope before building on top |
| WebEx SDK | Rich API, bot + agentic app types, MCP support | Strong foundation for properly architected solution |
| Build systems | Different systems for dev (Bazel) vs. prod (Gmake) | Technical debt; potential code modernization opportunity |
| Build queue | ~200 builds, manual priority, 6-8 hour durations | Pipeline optimization is a natural expansion area |
