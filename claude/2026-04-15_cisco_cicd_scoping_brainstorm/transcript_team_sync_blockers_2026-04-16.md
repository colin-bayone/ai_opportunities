# Team Sync — Blockers and Access Status (April 16, 2026)

**Source:** cisco-team-sync_4-16-2026.txt.txt
**Date:** 2026-04-16 (Wednesday team sync, Colin + Srikar + Namita + Saurav + Vaishali)

---

## Colin's Opening Frame

Colin set the purpose explicitly: this meeting is about documenting blockers for an email to Anand and Srinivas. He stated the team's velocity is "primarily gated by not technology or complexity or things being difficult, but pretty much by access." Four weeks into the project, they still do not have access to DeepSight.

Colin wants to give Cisco an ultimatum: provide a list of what should be done, pick a date by which Cisco resolves all access, and stop telling BayOne to talk to 30 different people and put in 30 different requests.

---

## Blocker Inventory (Updated April 16)

### 1. Pulse and Scribble Repo Access
- **Status:** Still blocked.
- **Timeline:** Srikar first met Naga on April 9. Asked for access. Naga said to go through Srinivas. Srikar reached out to Srinivas on April 15. Srinivas asked why they need "Scrubber" (name confusion between Scribble and a different repo called Scrubber in the DeepSight org). Srikar went back to Naga for the correct repo links. Naga has not responded.
- **Root cause:** Verbal instructions with no repo links, no documentation, similar naming (Scribble vs. Scrubber), no clear owner.
- **Colin's comment:** "We should have been able to assume that Scribble would have presumably been at the same place as the other applications in the same repo. But it wasn't." Called it "an impossible way to work" to have Srinivas mention a project name and then have BayOne hunt down the repo owner and link.

### 2. Permanent ADS Machine
- **Status:** Still blocked. Two separate sub-items:
  - **Tenant ID (DCN Switching):** Requested approximately two weeks ago (early April). Mahavir said he approved it, but the tenant is still not visible to Namita.
  - **Standalone bundle:** Requested last Friday (April 11). No response.
- **Impact:** Without permanent ADS, all work is on temporary 4-week machines that expire. Colin: "That's a non-starter for me. It's like you have a Git repository that disappears every four weeks."

### 3. DeepSight Platform Access
- **Status:** Still not accessible after 4 weeks. Colin raised this with Srinivas on April 15, who acknowledged and said his team is wrapping up compose files.
- **Colin's comment:** "It is Thursday of the following week and we still don't have access to DeepSight. This is now 4 weeks into the project and we still don't have access to the thing that Srinivas himself is the owner of."

### 4. Saurav's Laptop
- **Status:** Loaner picked up. It is a heavily used older M1 with non-functional and sticky keys. Saurav is doing full setup from scratch. Two weeks of work lost from the original device.

### 5. WebEx API Limitation (Meeting Transcripts)
- **Status:** Srikar discovered that accessing other people's meeting transcripts via API requires an org-level token. Individual tokens only give access to meetings the user created. This is a structural limitation for the transcription work.
- **Workaround:** Manual download from meeting link is possible but does not scale.
- **Resolution needed:** Cisco needs to provide org-level or manager-level access tokens, or a service app with proper scope permissions.

### 6. No Documentation Anywhere
- **Status:** Ongoing. Saurav noted that none of the repos have any kind of documentation. No README, no architecture docs, no quickstart. Cisco does not use Mermaid or any formal architecture tooling. Justin confirmed they only use PowerPoint for architecture diagrams.
- **Impact:** Every new repo requires diving in blind to understand what it does before work can begin.

### 7. Three Separate GitHub Enterprise Servers
- **Status:** Confirmed. Cisco has at least three different GitHub Enterprise instances. Each requires separate access requests, multiplying the access burden.

---

## Major Open Question: Rui Guo and Duplicate Work

Colin showed the team the NxOS CI Workflow WebEx channel. He discovered that Rui Guo has already built and is deploying what appears to be a production-grade auto-triage application called "Nexus T" using GPT-5.4. It includes failure analysis, topology views, and a chat agent for failure cases.

Colin's concern: this directly conflicts with BayOne's assigned work, Justin's work, and the CI workflow. Yet Srinivas assigned BayOne to do the same thing.

**Colin's open question for Srinivas:** "What are we doing here? Are we building a duplicate of this? Is this just a POC for a hackathon? Should we be working with Rui directly? How does our work relate to Justin's work relate to Rui's work?"

Saurav's theory: DeepSight is like a hackathon platform. Everyone builds whatever they can. The concern is building something for a month and then being told "we already have something and we're using it."

---

## Architecture Discussion

Colin laid out a three-architecture framework for what to present to Srinivas:

1. **Current state architecture** — What exists right now, grounded in code or defensible sources (not hand-waving). Must be verified before presenting. Credibility loss if wrong.

2. **Problems and recommendations** — Scalability, cost, security issues with the current approach. Specific examples discussed:
   - Per-user deployment model causes duplicate processing (every person scraping the same transcripts independently)
   - No unified data layer means no reusable MCPs or tools
   - No access control or authorization in existing apps (org-level tokens without proper gating)
   - Hosting at scale is impossible with standalone ADS deployments
   - Repos are duplicating tools instead of using shared modules

3. **Future state map** — BayOne's ideal architecture. Both per-application and a master grand vision showing how everything connects with shared modules and unified layers.

### Key Technical Points from the Discussion

- **Dual entry points for log analysis:** Background process watching NFS (proactive, no human needed) plus manual WebEx reports (reactive, cross-referenced against what the system already knows).
- **Batch vs. real-time:** CI should be real-time (developer is waiting). CD can be batched (nightly builds). Middle ground: Airflow polling on a set frequency.
- **WebEx chat is not GitHub Issues:** Colin flagged that bug reports in WebEx have no traceability, can be edited/deleted, and should be converted to GitHub Issues as part of the pipeline.
- **Security gaps:** No authorization checks in existing apps. Org-level tokens without scope gating. No guardrails on AI applying fixes to production code.

### Saurav's Autonomous Agent Proposal

Saurav proposed a fully autonomous approach using Claude Code skills: create specialized skills for different error types, load them into an agent via agent.md, and let it loop autonomously with deterministic scripts inside skills for rule-based patterns, pre/post hooks for validation, and adversarial agent pairs (Codex for fixes, Claude for critique or vice versa).

Colin's response: the idea is good, it is the "million dollar question" of how to pitch it and price it. They need a working example at smaller scale, a deployment model (VS Code plugin?), and a maintenance story before presenting to Srinivas.

---

## WebEx Chat Scraping Progress

Srikar extracted approximately 6,500 messages from the NxOS CI Workflow chat via paginated API. Issues found:
- Connection aborts after ~130 pages
- Duplicate entries detected (same timestamps, same senders, same body text)
- All dates appear to be April 2026, which may or may not be correct (could be 6,500 messages in 6 weeks given the chat volume)
- Needs deduplication by message ID and possibly time-based incremental fetching

Colin will convert the CSV to a Parquet file with parent-child hierarchy, then run categorization and analysis.

---

## Colin's Guidance to the Team

- **Never mention Claude to Cisco.** When in doubt, say Copilot. Colin will handle the explanation.
- **Proactively propose solutions.** Do not wait for Srinivas to tell you what to do. If you see a gap (like no architecture documentation), propose filling it.
- **Don't devalue skills because they're markdown files.** "All code is just text. If skills were that easy to do, then everyone would do them."
- **Frame existing Cisco work as POCs, not failures.** "Divakar and his team, I appreciate what they did, but that was the POC. We're going to show you what production looks like."
- **Come to Srinivas with recommendations, not questions.** "Here is our recommendation. We are the experts here. Do you agree? Do you want us to proceed?"
