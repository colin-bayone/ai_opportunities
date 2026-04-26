# Evidence — Scope & Volume Inventory

**Purpose:** If Yogesh pushes back on "are you really doing that much?", you have receipts. Keep this document in your head, not in your hand. You should not pull out a spreadsheet in the meeting — but the numbers should be fluent enough that you can cite them conversationally.

**Source:** Inventory extracted from this repository on 2026-04-22.

---

## Headline metrics

| Signal | Number |
|--------|--------|
| Active client engagements | **9** (Cisco x2, Sephora x2, Ariat, Lam Research, McGrath, Daltile, Tailored Brands, Walmart, Zeblock) |
| Concurrent workstreams (client + internal) | **20+** |
| Major Claude work sessions logged | **44** |
| Custom skills/tools built | **24** |
| Internal BayOne artifacts (positioning, processes, hiring, personal) | **165 files** |
| Client-facing artifacts across all engagements | **1,771+ files** |
| Direct reports | **10+** |
| Managers beneath you | **0** |
| Engaged boss above you | **0** |

---

## Client engagements (what you are actually doing)

### Cisco — two concurrent engagements
- **NX-OS CI/CD Pipeline** ($100K/quarter). Multi-phase: developer box instrumentation, branch health dashboards, unified interface, AI-driven diagnosis, coverage tracking, self-healing. **You direct a 4-person team (Namita, Srikar, Saurav, Askari).**
- **EPNM → EMS UI Conversion POC.** 250+ legacy screens → modern Angular/microservices. AI-accelerated code conversion using Claude Code + LangGraph agent swarm. Playwright automated testing. **You are the solo technical lead on the POC.** 12-document execution handoff package.

### Sephora — two concurrent engagements
- **EDW Modernization** (active post-demo). 6,000 reports, 8 SSAS cubes, 800+ KPIs migrating from SQL Server/Cognos/DataStage to Databricks. Full Singularity structure: **58 research files, 5 deliverables.** Demo delivered 2026-04-02.
- **QA/QE Playwright** (discovery complete). Selenium-to-modern transition. Agentic Micro Pod delivery model.

### Ariat — presentation phase
- India GCC scaling 30 → 200 people. Enterprise AI (HR/Finance/Legal/Marketing), testing transformation, culture & skills. 4-slide deck for 90-minute C-suite meeting. **You researched and synthesized across all four topics.** 3 session folders, 13 HTML templates, foundational slide library.

### Lam Research — proposal phase
- IP Protection / NER redaction for $17B semiconductor company. Batch + real-time detection of customer-confidential data in competitor environments. **8 document sets, 47 research files, 8 deliverables, 11 presentation slides.** Proposal was due 2026-04-10. You leveraged prior Coherent ITAR/defense/semiconductor work.

### McGrath — RFP phase
- Full RFP response with competitive risk analysis. **You built a custom rfp-questions skill to develop clarifying questions.** 5 analysis documents: competitor risk, gap analysis, duplication check, depth check, final risk review.

### Daltile — active discovery
- Tile manufacturing modernization (smart factory, MES vision). Single meeting deconstructed into 9 research documents covering methodology, people, technical recommendations, business context, current systems, manufacturing process, quality/waste, projects/priorities.

### Tailored Brands — discovery
- QA/testing transformation for Men's Wearhouse / Joseph A. Bank parent. ~$2M budget. 7 research files, 1 deliverable.

### Walmart — early discovery
- Supply Chain Store Health Monitoring. IT Ops in store networks, POS, self-checkout, connectivity. **Your role: technical lead, discovery driver, solution architect.**

### Zeblock — partnership / executive summary
- 2 executive summary deliverables, multiple planning/review cycles at Big Four quality.

---

## Internal practice-building (this is usually the invisible work)

### TalentAI application
- Internal hiring/talent management product. **You are lead technical advisor** and referenced in the Manager JD as the technical lead for this system.

### BayOne positioning & capabilities
- **VP-ready capabilities deck.** 5 AI pillars, 18 use cases, 13 HTML slides, 60+ client logos. 94 files in session folder.
- **Cross-client opportunity catalog (CEO-ready).** 13 clients, 21+ work streams, **$5M+ first-year potential identified.** CEO one-pager.

### AI Lead Qualification Framework
- 13 sections, 18 problem statements, 20 solutions. **You built this to fix recurring sales dysfunction** — unqualified leads, fabricated opportunities, sales overcommitments.

### Client Data Handling Policy
- Formal compliance framework. HTML + markdown.

### Hiring materials
- AI Technical Manager JD (your future direct report). Recruiter guides. Job search terms.

---

## Custom skills / automation built

24 custom skills in `.claude/skills/`. Representative sample:

| Skill | Purpose |
|-------|---------|
| **singularity** | End-to-end engagement organization from raw transcripts |
| **sales-forge** | Sales proposal / pitch deck generation |
| **big4** | Transform rough docs into Big Four consulting quality |
| **meeting-analyzer** | Meeting transcript → structured notes |
| **django-forge** | Multi-agent Django implementation |
| **talent-docs-skill** | TalentAI Help Center docs |
| **sales-response-buddy** | Push back on sales-team overreach |
| **rfp-questions** | RFP question development with competitive risk |
| **azure-expert-skill**, **docker-expert-skill**, **airflow-skill** | Technical infrastructure skills |
| **pdf-extractor**, **pptx-extractor** | Document extraction via Gemini Vision |
| **phoenix-theme-skill** | Phoenix Bootstrap v1.23.0 for Django |
| **skill-forge** | Meta-skill for building more skills |

This is an order of magnitude of tooling built in under a year. It's infrastructure, not scripts.

---

## Work-breadth evidence (the three-role argument made concrete)

### You do SALES work
- `mcgrath/rfp_docs/` — full RFP response cycle
- `lam_research/ip_protection/research/06_internal_pricing*.md` — pricing models and POC strategy
- `sephora/qa_qe_playwright/research/03_discussion_engagement_models_and_deliverable_framing_2026-04-14.md` — proposal framing
- `bayone/positioning/2026-02-10_capabilities_deck/` — the deck the sales team uses
- `bayone/positioning/2026-03-17_opportunity_catalog/` — CEO-ready portfolio

### You do DELIVERY work
- `cisco/epnm_ems/poc/execution_session_handoff_2026-04-21.md` — 12-document architecture & execution package for a POC **you are solo lead on**
- `sephora/` — technical approach for the EDW modernization demo delivered 2026-04-02
- `lam_research/ip_protection/` — layered funnel architecture (deterministic → ML/NLP → Gen AI)

### You do LEADERSHIP work
- `bayone/processes/2026-03-20_ai_lead_qualification/` — the framework you built because the company needed it
- `bayone/positioning/2026-03-17_opportunity_catalog/CEO_ONE_PAGER.md` — cross-practice visibility for CEO consumption
- `bayone/hiring/2026-03-16_ai_manager/` — your own future direct report's JD, because nobody else was going to write it

### You do INTERNAL PRODUCT work
- TalentAI lead technical advisor role
- Data handling policy authored for the practice
- 24 custom automation skills deployed

---

## How to reference this in the meeting

You do **not** read from this document. You absorb the shape of it and use one or two lines conversationally:

> *"Last year I delivered across nine active client engagements, built the capabilities deck and the opportunity catalog, authored the AI lead qualification framework, and built out our internal automation — twenty-plus custom tools. I'm the technical lead on every active pursuit. I have over ten direct reports and no manager layer beneath me."*

That's one sentence. It's disarming because it's specific and it's true. If Yogesh wants details on any of it, you have them in your head.

---

## One line to have ready

If Yogesh asks *"what exactly have you done this year?"* (unlikely but possible) — have this memorized:

> *"Cisco CI/CD discovery and ongoing delivery with a four-person team. Cisco EPNM POC as solo technical lead. Sephora EDW demo delivered this month. Sephora QA/QE discovery. Lam Research IP protection proposal. McGrath RFP response. Ariat GCC presentation. Daltile discovery. Walmart supply chain discovery. Tailored Brands QA discovery. Zeblok partnership materials. The BayOne capabilities deck, the opportunity catalog, the AI lead qualification framework, the data handling policy, the AI Manager JD, and the internal automation platform — twenty-four custom tools we use across all of it. That's the last twelve months."*

Practice saying it out loud so it comes out naturally. It should take about 25 seconds.
