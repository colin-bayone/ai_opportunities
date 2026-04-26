# Internal Week Tracker — Apr 27 to May 1, 2026

**Audience:** Internal BayOne (Colin + Claude). Never shared with Cisco.
**Pattern:** One of these per week. Running document — append progress notes throughout the week. End-of-week snapshot fills in the status column on Friday.
**Source rules:** Exclusion rules at `claude/2026-04-26_cisco_cicd_week_planning/10_exclusion_rules.md` apply.

---

## 1. Friday May 1 deployment target (what we are marching toward)

Per Srinivas's Apr 24 sync. The Friday demo to Srinivas is the contract-renewal-window measurement point. Hard deadline; should land earlier in the week if possible.

**The deliverable:**
- CI/CD application running on ADS (Temp ADS acceptable; Permanent ADS preferred if it lands)
- CAT MCP plugged into the backend as the dynamic-answer path
- Static FAQ entries from existing answer data wired into the chat interface
- Both static and dynamic routes feeding the same chat user interface
- WebEx bot deployed on the NX-OS CI pipeline sharing the same backend (Service-Application-Platform-style backend with two pluggable frontends)
- LLM via circuit API initially (Saurav already has token; others to acquire via the API Enabler Bot path Saurav documented Apr 23)
- All skills committed to the main CI/CD repository

**Acceptable Friday outcome if Permanent ADS does not land:** Temp ADS deployment with everything above running, clearly portable to Permanent ADS, with explicit communication that we are still working on the permanent-ADS sort-out.

---

## 2. Per-target dependency map

Every target above broken into its prerequisites and the upstream blockers. This is the part the master list (file 02) does not give us — it lists items, this maps them.

### Target A — CI/CD app shell running on Temp ADS

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| Anupma's Cisco-side CI/CD app deployment lands by Monday | Committed by Srinivas Friday Apr 24; not confirmed | Cisco (Anupma) |
| Fallback: BayOne stands up the app shell directly on Temp ADS | Ready to execute | BayOne if Cisco slips |
| Temp ADS is RHEL8-compatible | Confirmed Friday Apr 24 (Srikar) | None |
| CN-SJC-STANDALONE bundle membership | Requested Friday Apr 24 by Srikar; Srinivas warned 4-6+ hour window | Cisco (provisioning) |

### Target B — Static FAQ wired into the chat interface

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| Static FAQ source data extracted from existing answers-by-the-user data | Not started | BayOne |
| Static-vs-dynamic routing logic in the chat backend | Not started; dependent on Target A | BayOne |

### Target C — CAT MCP as the dynamic answer path

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| CAT MCP installed in VS Code with 4 tools identified | Done (Srikar, pre-Apr 24) | None |
| OAuth resolved | Done | None |
| Colin sends BayOne user IDs to Anupma | Done Friday Apr 24 (Srikar posted: colmoore@cisco.com, namane@cisco.com, srmadara@cisco.com, sauravmi@cisco.com) | None |
| **Each user logs in to NX GitHub server at least once** (Anupma's hard prerequisite) | **Not confirmed for all four; Anupma pinged twice Friday evening** | **BayOne — every team member, top-of-Monday action** |
| Anupma adds users to NX repo lead-only group | Pending the login prerequisite above | Cisco (Anupma) |
| Git LFS error on NX-OS repo resolved (item 124) | In progress; Justin documentation in hand | BayOne (Srikar) |

### Target D — WebEx bot deployment on NX-OS CI pipeline (shared backend)

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| WebEx bot complete on webex-skills branch | Done | None |
| Podman container build for RHEL8 | Not started | BayOne |
| Bot tested locally | Done | None |
| Bot tested in Podman against Temp ADS | Not started | BayOne |
| Cisco bot compliance / registration (300-user NxOS group) | Open from Set 07; not yet revisited | BayOne (Saurav) |
| Backend designed as Service-Application-Platform style | Not started | BayOne |

### Target E — LLM via circuit API (PoC scope)

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| Saurav has circuit API token (PoC-scope) | Done Apr 23 | None |
| Other team members acquire scope-limited tokens via API Enabler Bot path | Not started | BayOne (Monday) |
| Production-grade key distribution mechanism | NOT a BayOne deliverable for May 1; longer-term Cisco-side ask | Cisco (Srinivas) |

### Target F — All skills committed to main CI/CD repository

| Prerequisite | Status | Blocker / Owner |
|--------------|--------|-----------------|
| Skills inventory documented (3 named so far: Apache eCharts, WebEx bot creation, NX-OS issue categorizer; fourth not yet named) | Partial | BayOne (Colin to name fourth + document) |
| Branch merge: webex-skills branch into main CI/CD repo | Not started | BayOne |
| ds agent init pattern validated | Not started | BayOne |

---

## 3. Policy gate state (governs whether any of the above can start)

- **BayOne Client Data Handling Policy distribution:** Sent Friday Apr 24
- **Signed copies received as of Sunday Apr 26 4:00 PM ET:** 3 of 6
- **Pending:** 3 of 6
- **Working assumption:** all six signatures land Monday morning before any work begins
- **Issue header text (per file 05a, D3):** "Do not begin on this work if you have not submitted the signed policy back to: it's as simple as that."
- **Placement:** All BayOne-internal issues only. Header is the only policy-related content; no policy excerpts, no links, no scope description. Cisco-visible repos contain no policy reference at all.

---

## 4. Carried-forward open items still relevant this week

Filtered from the master list (file 02) to items that touch this week's targets or have movement opportunity.

**Access:**
- DCN Switching tenant for Permanent ADS — Colin owns escalation; Mahaveer Friday outcome unknown, Anand fallback warm
- DeepSight access on Cisco laptop (Srikar) — support ticket open

**Build track:**
- PR-to-PR commit attribution dependency mapping — Bazel command in hand from Justin (Apr 20); executable as soon as NX login completes; this week's stretch target if main targets land early
- Issue categorization skill productionization for real-time insights (admin/manager) — Wednesday MOM directive 2; tied to Target A above

**Saurav-side:**
- Cisco MacBook still in repair (ticket INC10796337) — Saurav working on BayOne hardware; lost-work redo when hardware lands
- MCP endpoint design thinking — ongoing background work

**Coordination:**
- Mahaveer ADS docs and Justin Git LFS docs shared in team chat (item 126) — verify status Monday
- Recurring meetings on calendars (item 73) — verify Monday standup invite stands

---

## 5. Future Goals (out of scope for this week, tracked here so we do not lose them)

- **Regression protection workstream** (Srinivas Apr 24 ask). Not a targeted item this week. Mention possible if asked. Internal note: BayOne can scope this for a future engagement extension once the Friday May 1 demo lands.
- **Production-grade key rotation / lifecycle / vault** (Srinivas Apr 24 raise). Not a BayOne deliverable; advisory only. Three patterns offered Friday (GitHub secrets, Azure Key Vault, Open Web UI). Wait for Srinivas to ask again.
- **Multi-MCP orchestration architecture** (Wednesday MOM directives 3 and 4). The CAT MCP integration this week is one workflow; the multi-MCP orchestrator is a later sequence per Srinivas himself.
- **GitHub Enterprise feature research** (item 120, two-week target from Set 10). Background; revisit when load allows.
- **MCP viewer app for testing external MCPs** (Main Set 13/15 announcement). Cisco-side; consume when it lands.

---

## 6. Risks for the week

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Anupma does not land Cisco CI/CD app deployment by Monday | Moderate | High | Start BayOne fallback Monday afternoon if no Cisco delivery by EOD Monday |
| Team members do not log in to NX GitHub server early Monday | Low if surfaced; high if not | High | Top-of-Monday standup item; Anupma's prerequisite must be cleared by Monday end-of-day Cisco time |
| Mahaveer Permanent ADS does not move | Moderate | Low (Temp ADS is acceptable per Srinivas) | Continue Anand escalation; Temp ADS plan proceeds |
| Policy signatures do not all land Monday | Moderate | High (gate on issue work) | Header on every issue prevents accidental work; Colin pings missing signatories Monday morning |
| RHEL8 Podman compatibility surprise | Low | Moderate | Build and test Podman image early in week; do not save for Thursday |
| Static FAQ data extraction reveals quality issues | Moderate | Moderate | Start extraction Monday; surface quality issues by Tuesday so we have time |
| Srinivas surfaces a new scope ask in chat or Monday meeting | High (pattern) | Variable | "Future Goals" framing already prepared; do not commit on the spot |

---

## 7. Daily progress log (append throughout the week)

### Sunday Apr 26 (planning)
- Internal week tracker created
- Srinivas-facing combined one-pager pending (covers prior-week catch-up + this week)
- Policy gate state: 3 of 6 signed
- Six attachments organized into Singularity source folders (Mahaveer ADS PDF, Srinivas CD impact graph, Srikar Nova-CICD-AI-Assistant repo overview [Cisco-internal parallel project, not BayOne's], Srikar issue responder skills status, commits update PDF, NXOS-CI workflow CSV)
- File 08 chat findings cross-referenced; key clarifications: Anupma is the NX repo provisioner, login prerequisite outstanding, RHEL8 confirmed, CN-SJC-STANDALONE requested Friday, Saurav has circuit token (PoC-scope only)

### Monday Apr 27
*To be filled in*

### Tuesday Apr 28
*To be filled in*

### Wednesday Apr 29
*To be filled in*

### Thursday Apr 30
*To be filled in*

### Friday May 1
*To be filled in*

---

## 8. End-of-week snapshot (fill in Friday May 1)

| Target | Hit / Partial / Missed | Notes |
|--------|------------------------|-------|
| A — CI/CD app shell on ADS | | |
| B — Static FAQ wired | | |
| C — CAT MCP as dynamic path | | |
| D — WebEx bot deployment | | |
| E — LLM via circuit API | | |
| F — All skills on main CI/CD repo | | |

**Overall:** *To be assessed Friday afternoon before the Srinivas sync.*
