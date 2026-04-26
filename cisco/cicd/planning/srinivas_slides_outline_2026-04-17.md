# Srinivas Meeting Deck — Slide Outline

**Meeting date:** 2026-04-17 (Friday)
**Audience:** Srinivas Pitta, Director of Engineering, Cisco CNG
**Output:** `cisco/cicd/presentations/srinivas_status_2026-04-17/`
**Source material:** `cisco/cicd/deliverables/srinivas_primer_2026-04-16.html` (approved)
**Prior deck:** `cisco/cicd/presentations/srinivas_status_2026-04-10/` (previous Friday's deck, 8 slides, felt disorganized to navigate)

---

## Guiding Principles for This Deck

1. **Lead with Srinivas's problem, then evidence, then architecture, then ask.** His April 10 framing (PR through 45 checks, where did it fail, how do we unblock) anchors the deck.
2. **Every slide's title previews its answer.** Srinivas drives by his own agenda. When he asks "show me the pain points," the pain point slide is titled for that. No guessing where content lives.
3. **No task-by-task status slide.** The prior "Assigned Items Status" slide felt like a timesheet; he skipped past it. Progress is conveyed through the evidence and architecture, not through status cards.
4. **Evidence before architecture.** Pain point data grounds the recommendation. Architecture makes sense because the data justifies it.
5. **End with a clear ask.** What we want him to decide or direct today. Not "next steps for us" (internal-facing) but "items requiring your input" (his-facing).
6. **Rules strictly applied:** no em dashes, no direct quotes, no individual names in slide body text (frame as "the team" or "an existing engineering effort"), diplomatic framing on scope issues, 16:10 aspect, navigation on every slide, bullet formatting in every card.

---

## Slide List

### 00_title.html — Title
- **Layout:** Dark full-bleed title (matches prior deck's title pattern).
- **Title:** "Pipeline Intelligence: Progress and Open Items"
- **Subtitle:** "Pain point analysis, proposed architecture, and decisions needed"
- **Presenter credit:** Colin Moore, Director of AI, BayOne Solutions (presenter credit is allowed on title and closing only)
- **Date:** April 17, 2026
- **Nav:** prev disabled, next → 01, home → 00

### 01_problem_and_agenda.html — Problem + Agenda
- **Layout:** Split panel.
  - **Left (dark gradient panel, ~40%):** Definition-bar style framing of the problem. Label: "The Problem." Content paraphrases Srinivas's April 10 framing (organizationally, not quoted): engineers raise PRs that traverse a 45-check pipeline, failures emerge with unclear cause and location, manual triage absorbs engineering time, the goal is AI-assisted reasoning about where a PR is stuck and how to unblock it.
  - **Right (light, ~60%):** Agenda card-list with 5 items in gradient progression. Each is a single line: (1) Pain point analysis, (2) Proposed build log architecture, (3) WebEx integration, (4) Scope alignment, (5) Access items and decisions requested.
- **Why this slide:** Opens by reflecting his own framing back. When he asks "what's the problem?" the first slide already answers it. When he asks "what are we covering?" the agenda is right there.
- **Nav:** prev → 00, next → 02, home → 00

### 02_pain_point_analysis.html — Pain Point Analysis: Findings
- **Layout:** Definition bar + two-column layout (chart image left, findings cards right) + takeaway bar.
- **Definition bar:** Label "Evidence from the NxOS CI Workflow." Title "Pain Point Analysis." Description: "Over 4,200 messages across three years, categorized into 25 types, approximately 3,000 actionable technical threads. The data grounds the prioritization decisions that follow."
- **Left column:** Embedded `category_distribution.png` chart (~50% width). Caption strip beneath.
- **Right column:** Four finding cards, each with a bold lead + one supporting detail bullet:
  1. Two-thirds of help requests receive no reply. Question and help requests are the highest-volume category and have 34% response coverage.
  2. Build failures wait four to five hours for first acknowledgment. Bug and test failure threads average 263 to 321 minutes to a first response.
  3. Explicit blockers resolve in minutes. Threads flagged as blockers average 12 minute first response, showing the organization responds when urgency is communicated. The gap is identification.
  4. Channel volume has tripled over three years. Weekly message volume has grown from 20 to 40 in 2023 to 60 to 120 in 2026. Manual triage is not scaling.
- **Takeaway bar:** "The highest-impact first target for AI-driven triage is the question and help request category. Highest volume, lowest response coverage, longest average wait."
- **Nav:** prev → 01, next → 02a, home → 00

### 02a_pain_point_charts.html — Pain Point Analysis: Detail Charts
- **Layout:** Definition bar + two embedded charts stacked vertically, plus a short connection strip.
- **Definition bar:** Label "Detail Views." Title "Response Time and Volume Over Time." Description: "Supporting charts for the findings on the prior slide."
- **Chart 1 (top):** `avg_response_time.png` with caption explaining the spread from blockers (12 min) to help requests (440 min average).
- **Chart 2 (bottom):** `weekly_trend.png` with caption explaining the roughly 3x growth in weekly volume over the measurement period.
- **Connection strip (small dark bar at bottom):** "These patterns shaped the proposed architecture on the next slide."
- **Nav:** prev → 02, next → 03, home → 00
- **Note:** This is a second pain-point slide because the three charts are each distinct evidence. Splitting protects density on slide 02 and gives Srinivas a clean visual to reference if he drills in. If Colin prefers to collapse into one slide, we can cut.

### 03_build_log_architecture.html — Proposed Build Log Architecture
- **Layout:** Definition bar + large embedded diagram + compact "pending decisions" strip at bottom.
- **Definition bar:** Label "Build Log Track." Title "Proposed End-to-End Architecture." Description: "Initial thinking grounded in the pain point data and the infrastructure review. Several decisions remain pending, called out below."
- **Diagram:** `architecture_diagram.png` embedded at full width inside the slide content area. Same image already approved for the primer (corrected Mermaid TB rendering with Airflow banner above).
- **Principle callout strip (dark bar):** "Simplest first, always. Deterministic regex precedes ML precedes LLM. Inverted pyramid cascade, mutually exclusive per error."
- **Pending decisions strip (compact 4-item list, labeled):** Ingestion mode (batched vs event), Error Catalog scoping, ML model training data availability, CI vs CD differentiation.
- **Nav:** prev → 02a, next → 04, home → 00
- **Note:** This slide has the architecture diagram as its hero. No separate "discovery findings" slide for build log infrastructure in this deck, because the primer's Section 02 material is setup for the architecture and doesn't need its own slide. If Srinivas asks about the current state or the PR #642 limitations, we verbally reference the primer document (which he will have).

### 04_webex_integration.html — WebEx Integration
- **Layout:** Definition bar + two-card grid + takeaway bar.
- **Definition bar:** Label "WebEx Track." Title "Integration Progress and Proposed Architecture." Description: "Two capabilities built and deployed, with a design for unified WebEx intelligence."
- **Card 1 — Current Capabilities Built:**
  - Chat scraper deployed, capturing structured message history (timestamp, author, thread parent, files) into PostgreSQL.
  - Meeting recording extractor built, retrieves transcripts, summaries, action items, and audio via the WebEx API.
  - Chat scraper was the instrument for the pain point analysis on slide 02.
  - API constraint identified: recording and transcript extraction via API requires the meeting owner's credentials.
- **Card 2 — Proposed Unified Architecture:**
  - Five layer design: data sources, ingestion, unified storage, MCP access layer, agentic application. Auth layer attached to MCP.
  - Modular: new data sources can be added without touching downstream layers.
  - The agentic application is swappable per use case.
  - Supports per-user token scoping on MCP.
- **Takeaway bar:** "Chat scraping already produced the pain point evidence on slide 02. Remaining decisions center on deployment model (per-user vs shared) and whether to build on existing internal tools."
- **Nav:** prev → 03, next → 05, home → 00
- **Note:** Does not include the 6-layer diagram from the primer. Instead, cards summarize the layers verbally. The full diagram is in the primer document for Srinivas to reference after the meeting. Keeping this slide tight because his April 10 engagement with WebEx was minimal compared to the build log track.

### 05_scope_alignment.html — Scope Alignment Needed
- **Layout:** Definition bar + two-card grid + takeaway bar.
- **Definition bar:** Label "Items Requiring Direction." Title "Scope Alignment Needed." Description: "Two areas of scope overlap have surfaced that benefit from clarification before the team commits further."
- **Card 1 — Build Log Analysis Overlap:**
  - A separate engineering effort on build failure analysis using a GPT-based auto-triage agent was identified in the NxOS CI workflow space.
  - This sits alongside the existing automation pipeline reviewed in PR #642 and alongside the team's own work.
  - Three parallel efforts now touch build failure analysis.
  - Guidance requested on how they relate and whether the team should build on, collaborate with, or solve a different slice.
- **Card 2 — WebEx Scope Direction:**
  - The original direction was to evaluate and build on existing internal WebEx tooling.
  - In a conversation on April 16, the engineer who owns that tooling indicated the expectation has shifted toward CI/CD pipeline integration.
  - Guidance requested on whether to continue pursuing the internal tooling path or to redirect effort toward the CI/CD pipeline integration directly.
- **Takeaway bar:** "Both items are about pointing the effort in the right direction. The team is ready to move quickly once the boundaries are confirmed."
- **Nav:** prev → 04, next → 06, home → 00
- **Note:** Names (Rui, Naga) do not appear in slide text per the design language rule. Framed as "separate engineering effort," "the engineer who owns that tooling," etc.

### 06_access_items.html — Access Items Requiring Action
- **Layout:** Three-column status grid (matches the prior deck's 05_access_status.html pattern and the gold standard). Takeaway bar.
- **Definition bar:** Label "Infrastructure Dependencies." Title "Access Items Requiring Action." Description: "Three access items remain outstanding. Each has been requested previously."
- **Column 1 — DeepSight platform access.** First requested approximately four weeks ago. Current status: no access. Needs a direct grant from the platform owner.
- **Column 2 — Internal WebEx tooling repositories.** First requested April 9. Repository links not yet provided. There is naming confusion in the repository index. Needs direction to the owner to share exact links and grant access.
- **Column 3 — Permanent ADS machine.** Tenant requested April 3, bundle requested April 11. Tenant approved but not reflected in the provisioning portal. Needs follow-up on the portal issue.
- **Takeaway bar:** "The team has temporary ADS access enabling current work. Permanent access is needed for sustained development."
- **Nav:** prev → 05, next → 07, home → 00

### 07_decisions_requested.html — Decisions Requested Today
- **Layout:** Definition bar + numbered list of decision cards (4 items), with a closing takeaway bar.
- **Definition bar:** Label "Closing Ask." Title "Decisions Requested Today." Description: "Items where the team would benefit from direction before the next working cycle."
- **Decision 1 — WebEx scope.** Focus on the NxOS CI workflow channel specifically, or generalize to the broader set of WebEx spaces?
- **Decision 2 — Fix delivery preference.** When AI generates a build fix, deliver via comment on the existing PR, a new PR with the fix, or another channel? Current workflow is email; the proposed architecture uses PR with human review.
- **Decision 3 — Tier 2 ML training data.** Does the team have access to labeled datasets of past build errors and resolutions? If not, should Tier 2 begin with pre-trained models or unsupervised approaches?
- **Decision 4 — Batch vs realtime ingestion.** For CI builds where developers are waiting, is near-realtime expected? For CD nightly builds, is a 15 to 30 minute batch cycle acceptable?
- **Takeaway bar (closing):** "The team is ready to move quickly on each of these once direction is confirmed."
- **Nav:** prev → 06, next disabled, home → 00
- **Note:** This is the closing slide. No separate "closing / thank you" slide because the ask itself is the close and it respects Srinivas's preference for directional conversations over ceremony.

---

## Summary Table

| # | Filename | Layout | Purpose |
|---|----------|--------|---------|
| 00 | `00_title.html` | Dark full-bleed | Title and presenter |
| 01 | `01_problem_and_agenda.html` | Split panel | Reflect Srinivas's problem framing, preview agenda |
| 02 | `02_pain_point_analysis.html` | Def bar + chart + cards + takeaway | Headline evidence |
| 02a | `02a_pain_point_charts.html` | Def bar + 2 charts + connection strip | Supporting charts |
| 03 | `03_build_log_architecture.html` | Def bar + diagram + decisions strip | Proposed architecture (the recommendation) |
| 04 | `04_webex_integration.html` | Def bar + 2 cards + takeaway | WebEx progress and design |
| 05 | `05_scope_alignment.html` | Def bar + 2 cards + takeaway | The critical alignment ask |
| 06 | `06_access_items.html` | 3-column status grid + takeaway | Specific unblocks needed |
| 07 | `07_decisions_requested.html` | Def bar + 4 decision cards + closing takeaway | The explicit decisions ask |

Total: 9 slides (1 title + 8 content).

---

## Colin's Approvals (2026-04-17)

1. **Output path:** `cisco/cicd/presentations/srinivas_status_2026-04-17/` — confirmed.
2. **Split pain point into two slides (02 + 02a):** Yes.
3. **Give architectures their own individual slides:** Yes. Build log split into current state (03) + proposed architecture (03a). WebEx split into current state (04) + proposed architecture (04a).
4. **Dedicated WebEx architecture slide:** Yes.
5. **Closing/thank-you slide:** No. End on decisions ask.
6. **Visual anchor on agenda panel:** Yes. Each agenda item gets a Font Awesome icon.
7. **Include images from Srikar and others:** Yes. Using the three primer-approved charts (`category_distribution.png`, `avg_response_time.png`, `weekly_trend.png` from Srikar) plus the build log architecture diagram (`architecture_diagram.png` from Namita/corrected version).

## Final Slide List (11 slides)

1. `00_title.html` — Title
2. `01_problem_and_agenda.html` — Problem + Agenda (with icons)
3. `02_pain_point_findings.html` — Pain Point Analysis: Findings (chart left, cards right)
4. `02a_pain_point_charts.html` — Pain Point Analysis: Response Time and Volume Detail
5. `03_build_log_current_state.html` — Build Log Track: Infrastructure and Existing Automation
6. `03a_build_log_architecture.html` — Build Log Track: Proposed Architecture
7. `04_webex_current_state.html` — WebEx Track: Current Capabilities and Constraints
8. `04a_webex_architecture.html` — WebEx Track: Proposed Unified Architecture
9. `05_scope_alignment.html` — Scope Alignment Needed
10. `06_access_items.html` — Access Items Requiring Action
11. `07_decisions_requested.html` — Decisions Requested Today
