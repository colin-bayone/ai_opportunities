# 01 - Standup: Action Items and Assignments

**Source:** /cisco/cicd/team/source/internal_standup_2026-04-10.txt
**Source Date:** 2026-04-10 (Friday standup, pre-Srinivas meeting)
**Document Set:** 01 (First team sub-singularity set)
**Pass:** Action items, assignments, progress tracking

---

## Three Srinivas-Assigned Tasks (from 2026-04-02)

### Task 1: WebEx Space Scraper (Pulse)

**Assigned investigation:** Srikar
**Cisco contact:** Naga (built the existing tool)
**Status:** Discovery complete; working prototype built independently by Saurav

- Srikar met with Naga, who showed two existing Deepsight repos: **Pulse** (WebEx space scraper) and **Scribble** (audio transcription via Whisper/Pannote)
- Pulse currently scrapes WebEx messages for a single user and stores them, but has no defined end-use case or downstream workflow
- Naga built these 2-3 months ago; Pulse has not been updated since; Scribble had minor updates 1-2 weeks ago
- Naga expanded scope beyond Srinivas's original ask, suggesting integration with email, GitHub, Splunk, and other platforms -- team flagged this as scope creep to clarify with Srinivas
- Naga was unclear on the full scope and end goal; Colin characterized both tools as POCs without a production plan
- **Saurav independently built a working WebEx bot ("Volley")** using the WebEx SDK that scrapes space messages and stores them in a Postgres database via Docker. Demonstrated live: scrapes messages, stores structured data, reports message counts by human vs. bot, supports per-room scraping, and has granular permission controls
- Saurav also created reference documents with verified WebEx API endpoints, methods, and parameters (shared with team)
- Both Pulse and Scribble repos are under Deepsight; access requires Srinivas approval

### Task 2: Meeting Recording Transcriber (Scribble)

**Assigned investigation:** Srikar
**Cisco contact:** Naga
**Status:** Discovery complete; approach questioned

- Scribble converts audio files to transcription using Whisper and Pannote
- Team raised the question: why build custom transcription when WebEx already provides built-in meeting transcripts via its API?
- Srikar noted Naga claimed Whisper produces more accurate transcription than native WebEx
- Colin and Saurav countered that transcription accuracy issues are primarily names/proper nouns, solvable with a glossary/lookup table approach rather than a separate transcription pipeline
- **Key question for Srinivas:** Is there audio outside of WebEx meetings that justifies a standalone transcription tool? If not, pulling existing WebEx transcripts via API is cheaper and simpler
- Naga was not clear on whether this is scoped only to WebEx or to arbitrary audio sources

### Task 3: Build Log Analysis (with Justin Joseph)

**Assigned investigation:** Namita and Srikar
**Cisco contacts:** Justin Joseph, Divakar
**Status:** Access partially granted; discovery well advanced

- Two calls completed: one with Justin alone, one with Divakar and Justin together
- **Build systems identified:** Gmake (older, used for production/NX-main repo) and Bazel (newer, used for dev/NX-dev repo). Divakar recommended focusing on Bazel only since Gmake is being phased out
- Logs are stored on ADS machines via NFS (not in a database); MySQL DB stores only build metadata (build number, date, status)
- Justin's existing workflow: Python script extracts a subset of errors from logs, passes them to an LLM for summary, LLM suggests fixes, fixes are applied to PR, then build verification runs
- Team identified significant limitations in Justin's approach: script only extracts top-level errors (not comprehensive), no structured storage of errors, no guardrails or tool-calling on the LLM, no validation framework, unclear how LLM applies fixes (no harness/scaffolding)
- Log files are large (50K to 500K lines) with 12+ log files generated per build; builds take 1.5 to 6+ hours; ~200 builds in queue at any time
- **Divakar conflict:** Divakar was initially reluctant to engage, stating this work conflicted with his team's existing work. After Namita explained the collaborative intent, he opened up. Colin directed the team to raise this with Srinivas directly: "Divakar didn't know we were working on this and felt it was duplicating his team's work. Please advise."
- Colin's proposed approach: three-tier architecture (1) deterministic rule-based matching/regex, (2) NLP/ML smaller models as a second gate where needed, (3) LLM for complex analysis. Noted that Bazel has a finite set of possible errors documented in official docs, making much of this solvable without AI

---

## Completed This Week

| Item | Who | Details |
|------|-----|---------|
| Two discovery calls with Justin and Divakar | Namita, Srikar | Gathered build system details, log locations, Justin's existing workflow |
| Discovery call with Naga | Srikar | Learned about Pulse and Scribble tools in Deepsight |
| Written notes document on log analysis findings | Namita | Created document summarizing Justin/Divakar meetings (to be shared in team chat) |
| Working WebEx bot ("Volley") with scraper | Saurav | Functional bot scraping WebEx spaces, storing in Postgres, with reporting commands |
| WebEx API reference documents | Saurav | Verified endpoints, methods, parameters documented and shared with team |
| WebEx developer portal research | Saurav | Explored bot types, agentic apps, MCP server registration, permission models |
| ADS temporary access request | Namita | Requested and granted (confirmed morning of 4/10) -- four-week temporary access |
| GitHub repo access request (NX-dev) | Namita | Requested and granted (confirmed morning of 4/10) -- needs verification |
| ADS permanent machine bundle request | Namita | Requested and granted (confirmed morning of 4/10) -- still needs DCN Switching tenant |
| Training course access request | Namita | Raised; awaiting response |

---

## Still In Progress

| Item | Who | Status | Next Step |
|------|-----|--------|-----------|
| Verify ADS temporary access works | Namita | Access granted today | Test access to NFS log location today |
| Verify GitHub repo access works | Namita | Email confirmed access granted | Log in and confirm access, review Justin's PR and Python scripts |
| DCN Switching tenant for permanent ADS | Namita | Tenant not available; chatbot support query sent | Follow up with support; needed for permanent ADS machine request |
| Deepsight repo access (Pulse/Scribble) | Srikar | Requires Srinivas approval | Ask Srinivas in today's meeting |
| ADS access for Saurav/offshore team | Saurav | Not yet requested | Individual access requests needed (access is per-person, not team-wide) |
| Review Justin's pull request and code | Namita | Blocked on GitHub access verification | Assess what the Python script actually does, quality of output, whether builds pass after fixes |
| Collect sample log files from NFS | Namita, Srikar | Blocked on ADS access verification | Grab logs from different time periods (old, mid, recent) to check for format changes |
| Training course enrollment | Team | Access request pending | Awaiting response |
| Vaishali onboarding deep-dive | Colin, Vaishali | Scheduled | Monday session to bring Vaishali fully into the project |
| BayOne laptop delivery for Srikar/Namita | Colin (via RIT) | Overdue by 1+ month | Colin escalating; expected delivery next week |

---

## Items to Raise with Srinivas Today

### 1. Divakar Conflict on Build Log Analysis
- **Framing:** "We had productive meetings with Justin and Divakar. Divakar wasn't aware we were assigned to this and felt it duplicated his team's work. Please advise on how you'd like us to proceed."
- **Do not** frame it as adversarial; present it as a request for guidance
- Raise this early in the conversation, not buried at the end

### 2. Scope Clarification for WebEx Scraper and Transcriber
- Naga expanded scope beyond what Srinivas originally assigned (adding email, GitHub, Splunk, etc.)
- **Ask Srinivas:** Should we focus on WebEx only as originally scoped, or does he want the broader integration? Recommend starting with WebEx, expanding later once it works
- **Ask Srinivas:** Do they have audio sources outside WebEx that justify a standalone transcription tool (Scribble), or should we use the existing WebEx transcript API?

### 3. Demonstrate Progress on WebEx Scraper
- Saurav's Volley bot is a working prototype ready for informal demo
- Be prepared for Srinivas to ask: How was it built? What API/MCP was used? What is the plan for next steps beyond exploration?

### 4. Architecture Document for Build Log Analysis
- Divakar is expecting an architectural approach from the team
- Colin will help the team build this together next week using existing tooling
- For today: mention that the team will come back with a formal architecture assessment after accessing and reviewing the actual logs and code

### 5. Gmake vs. Bazel Focus
- Share Divakar's recommendation to focus on Bazel only
- Optionally offer: if Cisco wants help with Gmake-to-Bazel migration/conversion, that is something the team can assist with (code modernization)

### 6. Build Queue and Silent Failures
- Srikar observed ~200 builds in queue with 3-4 day processing delays
- Some builds silently fail (expected 1.5 hours, run 6+ hours with no notification)
- Manual priority selection and manual restarts happening via WebEx space threads
- Potential opportunities: build queue optimization, automated retrigger pipeline, investigative tooling for silent pipeline failures

### 7. Access Requests
- Request Srinivas grant access to Deepsight repos (Pulse and Scribble) for the team
- Confirm that individual access requests are the correct process (no team-wide provisioning)

---

## New Action Items Assigned During This Standup

| # | Action | Owner | Due/Timeline | Notes |
|---|--------|-------|-------------|-------|
| 1 | Test ADS temporary access and verify NFS log location is reachable | Namita | Today (4/10) | Access was confirmed this morning |
| 2 | Verify GitHub repo access and review Justin's PR/Python scripts | Namita | Today/Monday | Focus on: what output is generated, quality, whether builds pass after fixes, validation approach |
| 3 | Follow up with support on DCN Switching tenant for permanent ADS machine | Namita | Next week | Bundle request is approved; tenant is the blocker |
| 4 | Share written notes document in team chat | Namita | Today (4/10) | Colin has not received it yet (no Cisco laptop) |
| 5 | Collect sample log files from NFS across time periods (oldest, middle, newest) | Namita, Srikar | Once ADS access verified | Check for log format variations over time |
| 6 | Request Deepsight repo access from Srinivas | Srikar | Today (Srinivas meeting) | Pulse and Scribble repos |
| 7 | Prepare to answer Srinivas's questions about Volley bot implementation | Saurav | Today (before Srinivas meeting) | How built, what API used, next steps beyond exploration |
| 8 | Raise Divakar conflict with Srinivas | Namita or Colin | Today (Srinivas meeting) | Use agreed framing; raise early in conversation |
| 9 | Ask Srinivas to clarify scope for WebEx/transcription tasks | Srikar or Colin | Today (Srinivas meeting) | WebEx only vs. multi-platform; Scribble vs. native WebEx transcripts |
| 10 | Build architecture document for log analysis approach | Colin + team | Next week | Colin to show team how to create using existing tools; three-tier approach |
| 11 | Vaishali onboarding deep-dive session | Colin, Vaishali | Monday (4/13) | Full project orientation |
| 12 | Resolve BayOne laptop delivery for Srikar and Namita | Colin (via RIT) | Next week | Over a month overdue; Colin escalating |
| 13 | Build a Claude Code skill/reference for WebEx API | Saurav, Colin | Future | Reusable reference from Saurav's research and verified endpoints |
| 14 | Investigate build queue optimization and silent failure detection | Team | Future (after scope confirmed) | Potential new project areas; get Srinivas read first |
| 15 | File individual access requests for offshore team members | Saurav, Vaishali | Next week | Access is per-person; cannot be provisioned team-wide |
| 16 | Add team members to Srinivas's weekly meeting invite | Colin | Today (4/10) | Meeting invite currently only lists Colin; Colin pinging Srinivas to add everyone |

---

## Meeting Structure Established

Colin laid out a recurring Friday standup format (pre-Srinivas meeting):
1. **General updates** from Colin (project-level news, team changes)
2. **Team round-robin** -- one person per sub-team gives high-level update (what was done, current work, blockers)
3. **Next week planning** and demo/assistance requests
4. **Srinivas meeting prep** -- formalize talking points and agenda for the weekly Srinivas meeting that follows ~1 hour later

Colin noted that future meetings will include prepared presentations built using internal tooling (no manual effort from the team). Starting next week, a formal written agenda will be distributed.

---

## Key Context Notes

- **New team member:** A new person is joining the project (unnamed; announced by Colin as a general update)
- **Vaishali** is new to the team; following along but not yet fully onboarded. She completed some early prep work that gives her a head start
- **Team sub-structure:** Two temporary sub-teams: (1) Srikar + Namita (on-site at Cisco), (2) Saurav + Vaishali (offshore)
- **Srinivas meeting timing:** Occurs ~2 hours after the Friday standup; Saurav and Vaishali invited but not required (late Friday for India time)
- **Competitive pressure:** Cisco/Srinivas frustrated with other vendors being slow to deliver despite AI claims; speed of delivery is a key differentiator for BayOne
- **Political dynamics:** Both Divakar (build log analysis) and Naga (WebEx/transcription) have existing ownership feelings over their work. Colin coached the team to acknowledge existing work, avoid directly criticizing, frame feedback as engineering rationale, and let Srinivas make decisions on scope and collaboration model
