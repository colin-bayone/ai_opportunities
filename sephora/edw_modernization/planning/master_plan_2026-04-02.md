# Master Plan: Sephora EDW Modernization Engagement

**Created:** 2026-04-02
**Status:** In Progress

---

## Session Objective

**Final goal for today:** Colin is fully prepared to deliver the Sephora EDW Modernization demo at 6:00 PM ET on April 2, 2026. He has a complete understanding of the pipeline architecture, a rehearsed demo flow, knows every risk and workaround, has crisp talking points, and can answer any technical question Sephora throws at him.

**How we get there:** Build the complete singularity research library (retroactive + new), then decompose the April 2 Saurav/Colin transcript into a set of actionable demo prep documents that Colin can use as his briefing materials. The codebase exploration rounds out the picture so nothing is left to surprise.

**Why the full library matters for demo prep:** Colin needs to speak fluently about the entire engagement arc, not just today's transcript. The research library gives him command of every meeting, every decision, every technical detail, and every relationship dynamic from the past two months. That depth is what makes a demo feel like a conversation, not a presentation.

---

## Context

This engagement has been active since February 2026. Source materials (transcripts, emails, ETL files) were accumulated across two repos (cisco_projects/cicd and ai_opportunities) without singularity structure. We are now organizing everything properly, processing all sources through the blockchain methodology, and preparing for the demo happening today (April 2, 2026 at 6:00 PM ET).

**Critical business context:** Sephora has dismissed all other vendors. BayOne is the sole remaining candidate. Budget must be locked in by end of April 2026. The demo today is the culminating event.

---

## Phase 1: Engagement Setup

- [x] Create singularity folder structure at `sephora/edw_modernization/`
- [x] Write methodology document (`research/00_methodology_2026-04-02.md`)
- [x] Write initial org chart (`org_chart.md`)
- [x] Copy all source materials to `source/`
- [x] Create this planning file
- [ ] Write skill notes (`planning/skill_notes.md`) after first set is processed

---

## Phase 2: Retroactive Processing (Sets 01-05)

Process all existing source materials through the full singularity workflow. Each set gets: people file, topic map, deep-dive agents, org chart update, bridge document (where applicable), and summary.

### Set 01: Mani Meeting 1 (Initial Discovery)
- **Source:** `source/mani_meeting1_2026-02.txt`
- **Type:** Meeting transcript
- **Priority:** HIGH (foundational context)
- [x] Pass 1: People file
- [x] Pass 1 continued: Topic map (propose files, get user approval)
- [x] Spawn deep-dive agents (5 agents: EDW modernization, org restructure, marketing initiatives, AI opportunities, hiring/rates)
- [x] Write summary

### Set 02: Mani Meeting 2 (Follow-up)
- **Source:** `source/mani_transcript2_formatted.txt`
- **Type:** Meeting transcript
- **Priority:** HIGH
- [x] Pass 1: People file
- [x] Pass 1 continued: Topic map (4 files: Colin's proposal, Mani's corrections/asks, EDW architecture status, engagement next steps)
- [x] Spawn deep-dive agents (4 agents)
- [x] Bridge document (01-02)
- [x] Write summary

### Set 03: Andrew/Grishi Meeting
- **Source:** `source/andrew-girishi-meeting1_formatted.txt`
- **Type:** Meeting transcript
- **Priority:** HIGH
- [x] Pass 1: People file
- [x] Pass 1 continued: Topic map (4 files: pain points/current state, agentic architecture, feasibility concerns, next steps/demo ask)
- [x] Spawn deep-dive agents (4 agents)
- [x] Bridge document (02-03)
- [x] Write summary

### Set 04: Technical Deep Dive (Malika, Sergey)
- **Source:** `source/meeting4-technical-deep-dive_formatted.txt`
- **Type:** Meeting transcript
- **Priority:** CRITICAL (this is the meeting where scope was defined)
- [x] Pass 1: People file (Sergey and Malika enter, most consequential new voices)
- [x] Pass 1 continued: Topic map (4 files: Cognos MCP/SDK, Sergey's YAML framework, agent architecture detailed, demo scope/materials)
- [x] Spawn deep-dive agents (4 agents)
- [x] Bridge document (03-04)
- [x] Write summary

### Set 04a: Email Thread (Malika Correspondence)
- **Sources:** `source/email1_malika.txt`, `source/email2_malika.txt`, `source/email3_malika_2026-03.txt`, `source/email_3-6-2026_malika.txt`
- **Type:** Email chain (supplementary to Set 04)
- **Priority:** HIGH (contains Track A/B decision, materials provided, output format clarification)
- [x] Read all emails
- [x] Extract decisions, action items, new information
- [x] Write research docs (3 agents: early requirements, scope shift/Track B selection, Zahra's account strategy)
- [x] Bridge document (04-04a)
- [x] Write summary

### Set 05: Saurav/Colin Debrief (March 30)
- **Source:** `source/saurav_colin_3302026.txt`
- **Type:** Internal debrief
- **Priority:** CRITICAL (contains "all other vendors dismissed" intel, demo status, deployment strategy)
- [x] Pass 1: People file
- [x] Pass 1 continued: Topic map (4 files: competitive intel, demo UI walkthrough, skills alternative, demo timeline)
- [x] Spawn deep-dive agents (4 agents)
- [x] Bridge document (04a-05)
- [x] Write summary

---

## Phase 3: New Transcript Processing (Set 06)

### Set 06: Saurav/Colin Demo Prep (April 2, 2026)
- **Source:** `source/saurav-colin_4-2-2026.txt`
- **Type:** Internal working discussion / debrief
- **Priority:** URGENT (demo is today)
- [x] Pass 1: People file
- [x] Pass 1 continued: Topic map (5 files: pipeline architecture, demo features/UI, demo risks, infrastructure/performance, talking points/strategy)
- [x] Spawn deep-dive agents (5 agents)
- [x] Bridge document (05-06)
- [x] Write summary

**Proposed deep-dive topics for Set 06:**

1. **Pipeline Architecture** - Full walkthrough of orchestrator, gates (G1-G4), parsers (DataStage, SQL, DDL), pattern mapper, SQL/Spark generator, config generation, validation, review/auto-fix cycle. Deterministic vs LLM checks at each stage.

2. **Demo Features and UI** - Dashboard walkthrough, execution log with live spinners, file upload (load demo files), progress bar, collapsible sections, highlight.js code preview, AI review button, download buttons (individual works, zip broken), previous run history, clickable stages.

3. **Demo Risks and Known Issues** - Reject and retry button breaks DAG animation (but backend works fine), zip download not working, pipeline_runs table missing on Colin's DB (Saurav fixing), rendering issue on auto-fix advisory text, duration timer includes human wait time, front end is framework-less ("stick with glue"), configuration dropdowns are non-functional placeholders.

4. **Infrastructure and Performance** - Azure Foundry quotas (75K for Opus and Sonnet, 4X-5X increase requested), concurrency at 4 (hitting 529 errors at higher), Opus for heavy tasks (pattern mapping, SQL generation), Sonnet for lighter tasks, LangSmith for tracing (not real-time but within minutes), LangGraph state management (JSON object built throughout pipeline).

5. **Technical Architecture Deep Dive** - Three-stage parsing in parallel (DataStage parser, SQL interpreter, DDL parser), each uses deterministic + LLM synthesis (SQLGlot + LLM), pattern mapper creates SQL-to-Spark translation dictionary using target examples, SQL generation three-step process (plan stages, dependency graph, generate independent then dependent), max concurrency of 4 for generation, knowledge base learning from approved patterns.

6. **Demo Strategy and Talking Points** - Cognos MCP positioning (Java hook exists, but not for free PoC, getting Cognos access means we already have a contract), auto-fix as "like Claude Code for your pipeline," LangSmith as the technical audience satisfier, demo flow (load files, start pipeline, review gates, click auto-fix, approve, download), Saurav may join at 3:30 AM if awake.

---

## Phase 4: Post-Processing

- [x] Update org chart with all new information from Sets 01-06
- [ ] Write master bridge document covering the full arc (optional, if useful)
- [x] Create session handoff document

---

## Phase 5: Codebase Exploration

- [x] Explore `/home/cmoore/programming/sephora_edw-1/` (parallel agents failed on cross-repo access, completed via direct reads)
- [x] Document: Project structure, tech stack, key files
- [x] Document: LangGraph pipeline implementation details (graph.py, state.py)
- [x] Document: FastAPI API server routes and dashboard
- [x] Document: Agent definitions and model assignments
- [x] Document: Gate logic (deterministic checks + LLM checks via validators.py)
- [x] Document: Configuration and deployment setup
- [x] Write codebase overview document (`planning/codebase_analysis_2026-04-02.md`)

**Why this matters:** The research library captures what was discussed about the system. The codebase exploration captures what was actually built. Together they form the complete picture.

---

## Existing Work to Catalog

The prior meeting analysis work in `sephora/2025-02-25_andrew-meeting-prep/meetings/` contains analysis docs that were produced outside singularity. These should be referenced but not duplicated. Key existing assets:

| Location | Content | Status |
|----------|---------|--------|
| `sephora/2025-02-25_andrew-meeting-prep/meetings/04_technical_deep_dive_meeting1/analysis/` | Meeting breakdown, speaker notes, context discovery, sentiment | Pre-singularity analysis, can reference |
| `sephora/2025-02-25_andrew-meeting-prep/meetings/04_technical_deep_dive_meeting1/research/` | ETL use case analysis, demo feasibility, materials inventory | Pre-singularity research, can reference |
| `sephora/2025-02-25_andrew-meeting-prep/meetings/04_technical_deep_dive_meeting1/scoping/` | Track A (Cognos MCP) and Track B (ETL/DataStage) HTML scoping docs | Deliverables, move reference to deliverables/ |
| `sephora/2025-02-25_andrew-meeting-prep/meetings/04_technical_deep_dive_meeting1/drafts/` | Email drafts (Malika v1-v8, demo followup v1-v2, handoff docs) | Working drafts, reference from research |
| `sephora/context/ETL_use_case/` | Sephora's provided materials (XML, stored procs, views, schemas, target framework) | Source materials, already in context/ |

---

## Open Questions

1. After demo today, what is the next deliverable? Likely a formal proposal with pricing.
2. Should we also process the Mani meeting notes summary (`sephora/context/mani-meeting2-notes.txt`)?
3. Do we need a glossary for this engagement? (DataStage, Cognos, MCP, AggregationApplication framework, etc.)
4. What is the pricing timeline given end-of-April budget deadline?

---

## Notes

- Demo is TODAY, April 2, 2026 at 6:00 PM ET (3:30 AM Saurav's time)
- All file references use the singularity source path (`/sephora/edw_modernization/source/`)
- Bridge documents are written AFTER both adjacent sets exist
- Max 5 parallel agents per wave to avoid overwhelming the system
