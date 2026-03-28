# Session Summary: 2026-02-04_recruiter-guides

## Client/Opportunity
**Cisco Systems** — NX-OS CI/CD Pipeline Modernization (Recruiter Guides Quality Review & Correction Track)

## Purpose
Quality review and systematic correction of recruiter guides for 4 key hiring roles supporting Cisco's CI/CD pipeline modernization. A prior Claude session had produced recruiter guides with significant structural and content problems (unusable search strings, incorrect skill classifications, missing evaluation criteria). This session documented the problems in detail, created comprehensive research references, and produced one corrected draft guide as the template for the remaining three.

---

## Files

### Review Feedback Documents (review_feedback/)

- **`HANDOFF_READ_IMMEDIATELY.md`** (2.5K) — Urgent handoff directive. Instructs next session to read critical feedback before proceeding. Contains executive summary of key issues: AI pair programming as must-have vs. signal, Copilot/Claude Code distinction, tiered search strings, weak/good answer indicators. Also notes final update required to add CrewAI to Agentic AI Engineer guide after all 4 guides are approved.

- **`00_read_this_first.md`** (1.9K) — Overview explaining what a separate Claude session found wrong with the recruiter guides. Provides reading order for review_feedback materials and emphasizes that the first two guides (Senior AI Solutions Engineer, Automation Engineer) require multiple rounds of correction. Structures next session's approach: one-at-a-time review, validation checklist required, no proceeding to remaining guides until first two approved.

- **`01_critical_feedback.md`** (11K) — The core quality critique document. Details three major problem categories:
  1. **Unusable search strings** — Agentic AI Engineer Layer 1 included "AI agent" which matches customer service agents, insurance agents, real estate agents (massive noise); AI Engineer Layer 1 lacked AI pair programming filter and CI/CD context; included experimental frameworks (AutoGPT, BabyAGI) that surface hobbyists not production engineers.
  2. **AI pair programming incorrectly classified** — Listed under "Strong Signals" when it's a "MUST-HAVE" requirement per the JD. Explicit distinction: Copilot (autocomplete) is NOT equivalent to Claude Code/Cursor (agentic AI tools that write/edit code autonomously).
  3. **Arbitrary company lists as "Target Backgrounds"** — Listed specific companies (Adept, Cognition, "AIOps platforms") providing zero actionable guidance to non-technical recruiters. Replaced with concrete pattern guidance (company 100+ employees, built autonomous systems, production environment experience).

  Provides specific examples of correct formatting for screening questions with weak/good answer indicators. Notes missing Cisco project context (Apache Airflow, Jenkins, Bazel, pgvector+PostgreSQL, Grafana) that should appear in Nice-to-Have and keywords.

- **`02_validation_checklist.md`** (8.6K) — 11-section mandatory checklist for validating every recruiter guide before presenting for review:
  1. **Document structure** — Header with location/status/focus, Teams transcription note, two-column grid layout
  2. **Must-Have Skills** — Plain-language explanations, explicit AI pair programming requirement distinguishing agentic tools (Claude Code/Cursor) from autocomplete (Copilot alone)
  3. **Nice-to-Have Background** — Clearly distinguished from must-haves, includes Cisco tech stack items (Airflow, Jenkins, Grafana, Bazel)
  4. **Strong Signals** — Observable by non-technical recruiter only, no technical evaluation required
  5. **Warning Signs** — Including "Doesn't use AI coding tools" and "Vague about personal contribution"
  6. **Screening Questions** — Minimum 5, each with 2-4 sentence WEAK ANSWER and GOOD ANSWER indicators observable without technical knowledge
  7. **LinkedIn Search Strings** — Mandatory tiered structure (Layer 1 Narrow / Layer 2 Broader / Layer 3 Widest), with clear escalation guidance ("Start with Layer 1. If fewer than 20 results, try Layer 2..."), Communication Filter, AI Tools Filter, validation by actual LinkedIn testing
  8. **Synonym Groups** — Explaining WHY terms are related
  9. **Tech Stack Keywords** — Must-Have and Nice-to-Have tiers displayed as tags
  10. **What to Look for in Work History** — NO arbitrary company names, NO VC jargon, actionable guidance with brief WHY
  11. **Final Review** — Complete read-through as non-technical recruiter

- **`03_search_string_reference.md`** (9.8K) — Properly constructed, tested LinkedIn search string patterns for all 4 roles. Details Boolean search construction rules (AND = both required, OR = either, NOT = exclude, parentheses group, quotes for exact phrases).
  - **Senior AI Solutions Engineer Layer 1:** `("AI engineer" OR "ML engineer" OR "LLM engineer") AND Python AND (LangChain OR LangGraph OR "RAG" OR "retrieval augmented") AND (production OR shipped OR deployed)` — expecting 50-200 profiles
  - **Automation Engineer Layer 1:** `("Apache Airflow" OR Airflow) AND Jenkins AND Python AND (integration OR automation OR pipeline OR built OR developed)` — expecting 30-150 profiles
  - **AI Engineer Layer 1:** `("AI engineer" OR "LLM engineer" OR "ML engineer") AND Python AND (LangChain OR LangGraph OR "RAG" OR "retrieval") AND (chat OR conversational OR dashboard) AND (production OR shipped)` — expecting 30-100 profiles
  - **Agentic AI Engineer Layer 1:** `("AI engineer" OR "ML engineer" OR "platform engineer" OR SRE) AND Python AND (autonomous OR "self-healing" OR "auto-remediation" OR "automated recovery" OR "incident automation") AND (production OR deployed)` — expecting 20-80 profiles

  All roles include optional filters: Communication Filter (for client-facing roles), AI Tools Filter (`AND ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI")`), Offshore Location Filter. Framework guidance: LangGraph and CrewAI are legitimate production frameworks; AutoGPT/BabyAGI are experimental toys to avoid.

### Planning Documents (planning/)

- **`00_handoff_to_next_session.md`** (4.1K) — Analysis of what went wrong in prior session and lessons learned. States the prior session was "lazy" and made factual errors: called LangChain/LangGraph synonyms (they're completely different — LangChain is general orchestration, LangGraph is stateful agent graphs), removed confirmed stack items (PostgreSQL), added irrelevant frameworks (BabyAGI). Lists three completed research documents and describes the research pattern to replicate for each role. Confirms full tech stack: PostgreSQL+pgvector, Apache Airflow, Jenkins, Bazel, Claude API, OpenAI API, LangChain, LangGraph, Python, FastAPI or Django, Grafana, on-prem deployment.

  **Key learnings documented:**
  - LangChain != LangGraph (fundamentally different tools)
  - Senior != Depth (LangSmith/LangFuse signal depth, not seniority)
  - Production = business relies on it (not POC)
  - RAG/pgVector are table stakes for senior AI engineer in 2026
  - Industries > Companies for targeting
  - Tiered searching with AND/OR structure
  - Don't pad with irrelevant frameworks

### Research Documents (research/)

- **`01_ai_engineer_landscape_2026.md`** (5.0K) — Comprehensive market context for AI engineer hiring. Covers:
  - **Skill differentiation by level:** Junior L3 ($120K-$180K) needs mentorship; Mid-level L4 ($180K-$280K) independent feature owners; Senior L5+ ($280K-$400K) distinguished by demonstrated project outcomes, custom architectures, 10-100x performance. Critical insight: "Most ML specialists can't deploy. Most software engineers don't understand ML."
  - **LLM Ecosystem:** LangChain (general-purpose orchestration, ~10ms overhead), LangGraph (stateful multi-agent with native cycle support), LlamaIndex (data-centric RAG, ~6ms overhead). "Power Move": Use LlamaIndex for data + LangChain for orchestration + LangGraph for agents.
  - **Observability tools signal depth:** LangSmith (zero overhead, closed source), Langfuse (open-source, 19K GitHub stars, ~15% overhead), W&B Weave (ecosystem lock-in)
  - **Vector databases:** Pinecone (managed/serverless/enterprise), Qdrant (high-performance Rust), Weaviate (hybrid search), Chroma (prototyping only), pgvector (for Postgres shops)
  - **Production vs. POC signals:** 80% of enterprises experiment, 5% successfully deploy. POC engineers discuss Jupyter, accuracy, clean data, metrics. Production engineers discuss drift detection, latency, cost per task, observability, async, containerization, token economics.
  - **Market data:** AI/ML jobs growing from 10% to 50% of tech market (2023-2025), AI Engineer roles 300% faster growth than traditional software, average salary $206K (up $50K YoY, +18.7%), LLM fine-tuning commands +47% premium

- **`02_recruiter_search_strategies.md`** (5.1K) — Boolean search guidance for non-technical recruiters. Covers LinkedIn limitations (2,000 character limits, 1,000 results max, no wildcard), synonym expansion strategies (single dash multiplies results 25x), signal vs. noise analysis (high false positives from generic terms like "AI" alone), tiered searching structure (Layer 1 must-have core all ANDs, Layer 2 adds framework, Layer 3 broadens titles/skills), decision tree workflow, and what non-technical recruiters need (one-page tech cheat sheet, what role does in plain English, key skill translations, red/green flags). 2026 trend: AI-powered search replacing Boolean, reduces sourcing time 70%+.

- **`03_cisco_project_context.md`** (5.0K) — Cisco-specific technical and organizational context for recruiting.
  - **Confirmed stack:** Apache Airflow, Jenkins, Bazel, GitHub, PostgreSQL+pgvector, Grafana, Python, on-prem only, Claude API, OpenAI API (external calls, not self-hosted)
  - **Cisco-specific tools:** CAT (Commit Approval Tool), CDT (Context Driven Testing, 2+ years live), pyATS (Cisco test automation), DevX (developer platform)
  - **Scale:** 39+ validation gates before merge, NX-OS multi-stage pipeline
  - **6 Capability Areas:** (A) Developer Box visibility, (B) Gate Failures / AI diagnosis, (C) Cross-Pipeline Visibility / unified chat + dashboard, (D) Coverage Confirmation per PR, (E) Self-Healing / autonomous corrective actions (DEFERRED), (F) Branch Health dashboards
  - **Current priorities:** A and F
  - **Target metric:** 20-30% reduction in average PR merge time
  - **Role differentiation:** Senior AI Solutions Engineer (60% AI dev / 25% client interface / YES client-facing), Automation Engineer (60% CI/CD / YES client-facing with CI/CD teams), AI Engineer (65% AI features / NO client-facing, works under Senior), Agentic AI Engineer (45% autonomous systems / NO client-facing)
  - **Constraints affecting hiring:** On-prem reality (no cloud AI services, security constraints, incomplete docs, complex approvals) — candidates must have production systems experience not research, comfortable with enterprise bureaucracy

### Drafts (drafts/)

- **`automation_engineer_recruiter_guide.md`** (7.1K) — Complete corrected draft recruiter guide for the Automation Engineer role (on-site San Jose, CI/CD + integration focus). Demonstrates the proper format with all 11 checklist sections implemented:
  - **Must-Have Skills:** 4+ years software engineering / 3+ CI/CD, Apache Airflow (build DAGs not just use dashboards), Jenkins (configure pipelines not just click run), Python backend, SQL/PostgreSQL, integration experience, strong communicator
  - **Nice-to-Have:** Bazel, Grafana, GitHub APIs/webhooks, on-prem deployment, platform engineering, legacy systems
  - **5 Screening Questions** with weak/good indicators (e.g., "Describe an Airflow DAG you built" — Weak: vague, can't explain rationale; Good: specific workflow details, explains why Airflow vs alternatives)
  - **Tiered search strings:** Layer 1 (`Airflow AND Jenkins AND Python AND built`), Layer 2 (expanded titles), Layer 3 (broadest net)
  - **Synonym Groups:** Workflow Orchestration (Airflow/Prefect/Dagster/Luigi/Argo/Temporal), CI/CD Systems (Jenkins/GitHub Actions/GitLab CI/CircleCI/BuildKite), Build Systems (Bazel/Gradle/Buck/Pants/Make)
  - **Work History guidance:** Company 100+ (scale for CI/CD complexity), built not just used automation, integration/platform team, legacy/messy system experience

---

## What Went Wrong with Prior Guides

The initial recruiter guides had three systematic problem categories:

1. **Unusable Search Strings** — Agentic AI Engineer Layer 1 included "AI agent" matching customer service / insurance / real estate agents (massive noise). Included experimental frameworks (AutoGPT, BabyAGI) surfacing hobbyists. Missing CI/CD context despite role being "build self-healing systems for Jenkins and Airflow pipelines." No tiering structure. No AI pair programming filter.

2. **Incorrect Skill Classification** — AI pair programming listed under "Strong Signals" when JD says "expected" (required). Treated Copilot (autocomplete) as equivalent to Claude Code/Cursor (agentic AI that writes/edits code autonomously). Fundamentally wrong classification.

3. **Arbitrary Company Lists** — Listed specific companies as "target backgrounds" (Adept, Cognition, "AIOps platforms") providing zero actionable guidance for non-technical recruiters. Should have been replaced with concrete patterns (company 100+ employees, built autonomous systems, production environment).

---

## The 4 Roles

| Role | Location | Mix | Client-Facing | Key Must-Haves |
|------|----------|-----|---------------|----------------|
| Senior AI Solutions Engineer | On-site San Jose | 60% AI / 25% client | YES | 5+ yrs AI/ML, 3+ yrs production AI, LLM architecture, LangChain/LangGraph, RAG, AI pair programming |
| Automation Engineer | On-site San Jose | 60% CI/CD / 20% backend | YES | 4+ yrs SWE, 3+ CI/CD, Airflow DAGs, Jenkins pipelines, Python, SQL/PostgreSQL, integration |
| AI Engineer | Offshore | 65% AI / 20% dashboard | NO | 4+ yrs SWE, 2+ AI/ML, LangChain/LangGraph, chat interfaces, FastAPI/Django, React/Vue |
| Agentic AI Engineer | Offshore | 45% autonomous / 35% agent | NO | 4+ yrs SWE, 2+ production AI, autonomous systems, LLM APIs, tool calling, safety/governance |

---

## Cross-References

### Parent Session
- **`2026-02-02_resource-planning`** — Comprehensive Cisco resource planning session that produced the job descriptions, team structure, quarterly phasing, and recruiter guides that this session reviews and corrects.

### Cisco-Specific Context
- **Tech Stack:** Apache Airflow, Jenkins, Bazel, PostgreSQL+pgvector, Grafana, Python, Claude API, OpenAI API, FastAPI or Django, on-prem only
- **People:** VP Arun (executive sponsor), Srini/Srinivas (senior engineering manager), Anand (director), Divakar/Diwakar (engineering lead)
- **Scale:** 39+ validation gates, NX-OS multi-stage pipeline
- **Deliverables referenced:** Recruiter guides at `/deliverables/job_descriptions/recruiter_guides/` within `2026-02-02_resource-planning`

### BayOne Internal
- Colin Moore (Director of AI), Rahul (President), Amit (Delivery), Zahra (Sales)

## Suggested Home

**Primary:** `cisco/` — This is entirely Cisco hiring/recruiting work. The deliverables belong with the Cisco project; the research materials (AI engineer landscape, search strategies) have some reuse value across clients but are Cisco-contextualized.

**Relationship:** This session is a direct follow-up to `2026-02-02_resource-planning` and its recruiter guide outputs.

---

## Summary Statistics

- **Total files:** 11 across 4 directories (review_feedback, planning, research, drafts)
- **Total content:** ~18,000+ words across all documents
- **Review feedback:** 5 documents (33.8K combined)
- **Planning:** 1 document (4.1K)
- **Research:** 3 foundational references (15.1K combined)
- **Drafts:** 1 completed corrected guide (7.1K)
- **Roles covered:** 4 (Senior AI Solutions Engineer, Automation Engineer, AI Engineer, Agentic AI Engineer)
- **Guides completed:** 1 of 4 (Automation Engineer draft)
- **Pending work:** Senior AI Solutions Engineer, AI Engineer, and Agentic AI Engineer guides need correction following same validated pattern
- **Critical path:** Fix guides one-at-a-time, validate each against 11-section checklist before proceeding to next
