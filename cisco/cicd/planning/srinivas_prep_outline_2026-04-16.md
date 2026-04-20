# Srinivas Meeting Prep — Outline for Discussion

**Date:** 2026-04-16 (for meeting on 2026-04-17)
**Status:** DRAFT — awaiting Colin's input

---

## What Srinivas Asked For

"What the team learned and any open questions you might have" — so he can structure tomorrow's meeting productively.

## What Was Shared Last Time (April 6 Team Briefing)

The last deliverable was based on the Set 10 meeting (4/2-3). It covered:
- New Cisco contacts (Anupma, Justin, Naga)
- GitHub MFA blocker (single highest priority at the time)
- First tasks overview (3 tasks, high-level)
- Design constraints (modular, reusable, optimize inference costs)
- MCP integration pattern
- Database landscape (MySQL, MongoDB, Cassandra)
- CI pipeline co-ownership (Anupma/DevEx)

**Key difference since then:** The team has now had the 4/10 Srinivas meeting, met with Justin (twice), met with Naga, gotten partial access, and done substantial independent work. The tone should shift from "here is what we are getting started on" to "here is what we learned, what we built, and what we need from you."

---

## Proposed Structure for the Prep Document

### Section 1: What We Learned — Build Log Analysis (Task 3)

This is where the team has made the most progress. Namita's work is the backbone.

**Technical understanding gained:**
- Two build systems: Gmake (nx_main, legacy) and Bazel (nx_dev, current). Focus is Bazel per Justin.
- CI builds (developer PRs) vs CD builds (nightly). Different NFS paths, different retention policies.
- CD path: `/auto/ins-bld-tools/branches/{branch}/nexus/logs/{tag}` — predictable, 5-year retention for failures.
- CI path: `/auto/paw-sjc-scratch/paw-logs/{uuid}/NXOS Build/build` — UUID-based, 3-5 day retention, deleted at merge for successes.
- 13 distinct Bazel error log types organized per image/stage (nxos64, nxos64_msx, linecardimages, etc.)
- `build_log.html` exists for CD builds as a triage entry point. CI builds lack this.
- 40+ log files per build in flat directory structure.
- Justin's existing workflow: `analyze_and_fix_build.py` → routes to make or Bazel path → error extraction → Codex → verification builds (3 retries) → email.

**Architecture analysis (from code review of PR #642):**
- 7 specific limitations identified in Justin's pipeline: subset error extraction, no persistence, no traceability, make retries all targets, unused error_output parameter, hard-coded paths, tag selection sort bug.
- Bazel workflow is better engineered than Make workflow (tracks remaining targets, uses structured JSON, maintains attempt history).

**Open questions for Srinivas (Task 3):**
- What is the relationship between our work and Rui Guo's Nexus T agent? (GPT 5.4 failure analysis, already deployed — three-way overlap with Justin and BayOne)
- For CI builds: batch processing or real-time? (CI developers are waiting; CD is nightly)
- Fix delivery: comment on PR, auto-create new PR, or email? (Justin says new PR; team thinks comment is better)
- Do they have labeled datasets for training ML models, or should we use pre-trained?

### Section 2: What We Learned — WebEx Scraping (Task 1)

**Technical understanding gained:**
- Built and deployed a working WebEx scraper (Wall-E bot) into the team space on 4/10. Demonstrated: full room scrape (45 messages), activity reports, structured transcript export with 8-field schema, PostgreSQL storage, deduplication.
- Identified that Naga's Pulse has been stalled 2-3 months with no architecture documentation and no clear end goal.
- Scraped 6,500 messages from the NxOS CI workflow channel (318 members). Data being categorized to identify top user pain points.
- WebEx API limitation: only meeting owners can extract recordings/transcripts via API. Impacts Task 2 automation.

**Open questions for Srinivas (Task 1):**
- Pulse/Scribble repo access: Naga has not provided repo links despite multiple requests (4/9, 4/15, 4/16). Naming confusion — Scribble appears as "Scrubber" in GitHub. Need Srinivas to direct Naga.
- Scope clarity: Is the WebEx scraping just for the NxOS CI workflow space, or should it be generalized for 40+ spaces?
- Srinivas said "scraping is just a one day job" — does the pain point analysis and categorization align with his vision?

### Section 3: What We Learned — Meeting Transcriber (Task 2)

**Technical understanding gained:**
- Built a working WebEx recording extraction tool: extracts transcripts, summaries, action items, and audio from any meeting where the user is the owner.
- Discovered the owner-only API limitation. This is the core architectural constraint.
- Evaluated Scribble vs API approach: API gives transcript + summary + action items (but owner-only). Scribble gives transcript only (but from any audio file). Complementary, not competing.

**Open question for Srinivas (Task 2):**
- Is the automation target "our own meetings" (API is sufficient) or "any meeting across the team" (needs admin scope or Scribble as fallback)?

### Section 4: Access Blockers Requiring Srinivas

This is Colin's escalation. The team's velocity is gated by access, not by technical complexity.

| Blocker | First Requested | Status | What We Need |
|---------|----------------|--------|-------------|
| DeepSight platform access | ~March 2026 | No access after 4 weeks | Srinivas is the owner — direct access grant |
| Pulse/Scribble repos | April 9 | Naga unresponsive, naming confusion | Srinivas to direct Naga or provide links |
| Permanent ADS machine | ~April 3 (tenant), April 11 (bundle) | Tenant approved but not reflected; bundle pending | Srinivas to escalate with Cisco IT |
| Rui Guo / Nexus T overlap | Discovered April 16 | Unknown scope boundary | Srinivas to clarify BayOne vs Rui's role |

### Section 5: Architecture Recommendations (If Appropriate for This Meeting)

**Depends on Colin's judgment** whether to include architecture in this primer or save for a separate session. If included:

- Unified data layer instead of per-user deployment
- GitHub Issues for bug tracking instead of WebEx chat
- Auto-documentation on commit/PR hooks
- Security: access control, authorization, guardrails for AI actions
- Processing modes: real-time for CI, batched for CD, Airflow polling as middle ground

---

## Format Considerations

- **Srinivas asked for a primer, not a full deliverable.** He wants to prep the meeting, not read a 20-page document.
- **The last deliverable was a polished HTML document.** This one could be lighter — markdown is probably sufficient for a primer. HTML if Colin wants to impress.
- **No quoting anyone.** Everything must be paraphrased as team knowledge, not attributed to individuals.
- **Chronology matters.** 4/7 briefing → 4/10 Srinivas meeting → 4/10-4/16 team work → 4/16 this prep.

---

## Open Items for Colin

1. Does the Rui Guo/Nexus T scope conflict go to Srinivas in this primer, or does Colin want to raise it verbally in the meeting?
2. Should architecture recommendations be included or saved for a separate session?
3. Should Namita's architecture diagrams be included (they are impressive and show depth of understanding)?
4. How much detail on blockers? Timeline-with-dates level or just the list?
5. Markdown or HTML for the primer format?
