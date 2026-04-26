# Presentation Topic Assignments — Srinivas Meeting, April 17

**Purpose:** Map primer sections to team presenters based on who did the work.
**Reference document:** `cisco/cicd/deliverables/srinivas_primer_2026-04-16.html`

---

## Topic Tree

```
Srinivas Meeting Presentation (April 17)
│
├── Opening & Framing ─────────────────── COLIN
│   └── Connect the week's work to the PR-unblocking goal
│
├── Section 01 · Pain Point Analysis ─── SRIKAR
│   ├── NxOS CI workflow scrape (4,200+ messages, 3 years)
│   ├── 25-category taxonomy
│   ├── Response time and coverage findings
│   └── Recommendation: target Question/Help Request first
│
├── Section 02 · Build Log Infrastructure ─ NAMITA
│   ├── Meetings with Justin Joseph (April 8, 9)
│   ├── CI vs CD path discovery (NFS structure, retention)
│   ├── 13 Bazel error log types, 40+ files per build
│   └── Review of PR #642 automation pipeline + limitations
│
├── Section 03 · Proposed Architecture ── NAMITA
│   ├── 6-block pipeline walkthrough (B1 → B6)
│   ├── Three-tier classification cascade
│   ├── Error Catalog Service (replaces Bazel docs scraper)
│   └── Feedback loop and human review gate
│
├── Section 04 · WebEx Integration
│   ├── Chat scraping (Wall-E bot) ────── SAURAV
│   │   └── Architecture, deployment, Podman
│   ├── Meeting recording extraction ──── SRIKAR
│   │   ├── API endpoint findings
│   │   └── Owner-only constraint
│   ├── WebEx platform architecture ───── SAURAV
│   │   ├── 6-layer design
│   │   └── Current-state comparison
│   └── Open design questions ─────────── SAURAV
│       └── Deployment model, polling vs webhooks, token security
│
├── Section 05 · Scope Alignment ──────── COLIN
│   ├── Nexus T overlap (Rui Guo)
│   └── Pulse / Scribble scope shift (Naga)
│
├── Section 06 · Open Questions ───────── COLIN
│   └── Facilitates discussion, pulls in team members as topics come up
│
└── Section 07 · Access Items ─────────── NAMITA + COLIN
    ├── DeepSight access (Colin)
    ├── Pulse/Scribble repos (Srikar has context too)
    └── Permanent ADS machine (Namita)
```

---

## Assignments by Person

### Colin Moore
**Role in meeting:** Runs the meeting, frames the overall narrative, handles strategic/sensitive topics.

**Primary sections:**
- Opening and framing (connect all work to PR-unblocking goal)
- Section 05: Scope Alignment (Rui Guo / Nexus T + Naga / Pulse-Scribble)
- Section 06: Open Questions (facilitate discussion)
- Section 07: Access items at the strategic level (DeepSight 4-week gap, overall pattern)

**Why Colin owns these:** Scope alignment touches directly on other Cisco engineers' work and needs to be raised neutrally by the project lead. Access escalation is Colin's ongoing workstream with Anand.

---

### Namita Mane
**Role in meeting:** Build log track expert. Handles Sections 02 and 03 end to end.

**Primary sections:**
- Section 02: Build Log Infrastructure
- Section 03: Proposed Architecture (build log pipeline)
- Section 07: Permanent ADS machine access item

**What she's bringing:**
- Discovery from two Justin Joseph sessions (April 8, April 9)
- Current-state architecture diagram with annotated limitations
- Log Type Mapping document (CI vs CD paths, retention, 13 error log types)
- The proposed 7-block pipeline (now the corrected Mermaid TB version)
- Build Log Analysis Updates PDF (April 10)
- Code-level review of Justin's PR #642 automation pipeline

**Key talking points:**
- The Bazel workflow is the stronger foundation (not Gmake)
- Justin's pipeline is a POC with 7 specific gaps identified
- Star schema storage addresses the traceability gap
- Three-tier cascade is mutually exclusive (each error caught at one tier)
- Error Catalog Service replaces brittle docs scraping

---

### Srikar Madarapu
**Role in meeting:** Pain point analysis lead and meeting recording track. Handles Section 01 and part of Section 04.

**Primary sections:**
- Section 01: Pain Point Analysis (full section)
- Section 04: Meeting recording extraction (one card in WebEx section)

**What he's bringing:**
- NxOS CI workflow chat scrape (4,200+ messages, April 2023 through March 2026)
- 25-category taxonomy with distribution analysis
- Response time statistics by category
- Charts: category distribution, response time by resolvable category, weekly trend
- WebEx recording extraction tool (transcripts, summaries, action items, audio)
- Discovery of the WebEx API owner-only constraint
- April 16 in-person meeting with Naga (scope shift context, but Colin handles the narrative)

**Key talking points:**
- 66% of help requests get no response
- Bug/Error and Test Failure threads wait 4-5 hours for first response
- Explicit blockers get resolved fast (12 minutes) but most issues aren't flagged
- Channel volume has tripled over three years — manual triage is not scaling
- Meeting API works for meeting owners only; affects Task 2 automation

---

### Saurav Kumar Mishra
**Role in meeting:** WebEx architecture and chat scraping. Handles most of Section 04.

**Primary sections:**
- Section 04: Chat scraping (Wall-E)
- Section 04: WebEx Intelligence Platform architecture (6 layers)
- Section 04: Open design questions

**What he's bringing:**
- Wall-E bot (WebEx scraper prototype, built on WebEx SDK + PostgreSQL)
- WebEx Intelligence Platform architecture (Data Sources → Ingestion → Storage → MCP → Application + Auth)
- 10 engineering clarification questions
- Understanding of OAuth token security patterns, Podman deployment, Pulse integration shortcut

**Key talking points:**
- Modular design enables swapping applications while keeping DB + MCP intact
- If Pulse is already an ADS-deployable container, MCP can wire on top of its DB
- Deployment model (per-user vs shared) is a fundamental decision
- Token security in shared deployments needs direction

**Logistical note:** Saurav's Cisco MacBook is currently offline (hardware failure INC10796337 from April 14). Wall-E code is on the dead laptop. He is presenting from his BayOne machine. The hardware situation should NOT be discussed in the Srinivas meeting.

---

### Vaishali Sonawane
**Role in meeting:** Attend and observe. No assigned presenting topic.

**Why:** Still onboarding. Hardware not yet provisioned. Limited exposure to the active work streams.

**Recommendation:** Have her attend the meeting to build context. She can shadow whichever topic she finds most aligned with her interests, with a view toward taking an active role in the next cycle.

---

## Summary Table

| Section | Presenter | Backup | Key Deliverables Referenced |
|---------|-----------|--------|----------------------------|
| Opening / Framing | Colin | — | Primer cover + summary |
| 01 Pain Point Analysis | Srikar | Colin | 3 charts, category taxonomy, response time stats |
| 02 Build Log Infrastructure | Namita | Srikar | Log Type Mapping, PR #642 review |
| 03 Proposed Architecture | Namita | Colin | architecture_diagram.png, block-by-block notes |
| 04 WebEx — Chat scraping | Saurav | Srikar | Wall-E bot architecture |
| 04 WebEx — Recording extraction | Srikar | Saurav | WebEx API findings, owner-only constraint |
| 04 WebEx — Platform architecture | Saurav | — | 6-layer vertical diagram |
| 04 WebEx — Design questions | Saurav | Colin | 5 question cards |
| 05 Scope Alignment | Colin | Srikar (Naga context) | Rui/Nexus T, Naga/Pulse-Scribble |
| 06 Open Questions | Colin | All | Discussion facilitation |
| 07 Access Items | Namita (ADS) + Colin (DeepSight, Pulse/Scribble) | Srikar (repos) | Blockers table |

---

## Meeting Flow Suggestion (Working Draft)

This is one possible running order. Final sequencing to be decided by Colin:

1. **Colin opens** (2-3 min): Acknowledge Srinivas's request, frame the week's work around the PR-unblocking goal he articulated on April 10.
2. **Pain point analysis** (Srikar, 5-7 min): Present the data, land the 66% gap finding.
3. **Build log discovery** (Namita, 5 min): What we learned from Justin about the infrastructure.
4. **Build log architecture** (Namita, 7-10 min): Walk through the proposed pipeline. This is the biggest technical block.
5. **WebEx integration** (Srikar + Saurav, 5-7 min total): Split between the three WebEx subtopics.
6. **Colin brings up scope alignment** (3-5 min): Raise Nexus T and Pulse/Scribble scope questions directly.
7. **Open questions and discussion** (Colin leads, remaining time): Work through the four technical questions and any Srinivas raises.
8. **Access items** (Namita + Colin, closing): Flag the outstanding blockers and confirm next steps.

---

## Notes for Team Prep Meeting

- Each presenter should know their section cold. Srinivas will interrupt and probe.
- When he asks a technical detail beyond a presenter's prep, defer to the primer or say "we'll follow up" rather than guessing.
- No individual names of other Cisco engineers unless Colin has already raised them (Rui, Naga only in Section 05).
- No internal team dynamics. No tool attribution (Claude / Copilot). No hardware failure mentions.
- If Srinivas asks about something not covered in the primer, flag it honestly as an open item rather than inventing.
