# 03 - Discussion: Summary

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)

---

## What This Set Covers

A working discussion between Colin and Claude to think through the technical approach, strategy, and deliverables for the Lam Research engagement. Six detail files:

| File | What It Covers |
|------|---------------|
| `03_discussion_technical_approach` | Discard everything Lam tried (intern-level AI projects). Hybrid approach: deterministic matching + AI classification. The entire use case is a RAG chatbot. Ingestion-first philosophy: reject at ingestion instead of detect/redact downstream. Unified control plane architecture. Why their ML failed. Enterprise tools strategy (Purview, Azure AI Foundry). |
| `03_discussion_technical_approach_continued` | Dashboard/metrics as a core control plane feature (usage, governance, business value). Async queue architecture with synchronous UX for classification. Day Zero / Day One terminology for historical data cleanup. The layered architecture: Purview (deterministic) + AI (contextual) + Control Plane (unified interface). The POC gap -- we have nothing to demo without specifics from Lam. |
| `03_discussion_technical_approach_round3` | Document-type-aware processing and known-offender escalation. Full list of questions for the Daniel technical call. Accenture autopsy questions. Competitive positioning: diplomatic but clear, don't name Accenture, frame prior work as "common but brittle pattern." Application-by-application migration doesn't exacerbate the existing governance gap. |
| `03_discussion_open_information_needs` | Consolidated list of everything we still need, organized by: (1) sales team can get without a technical call, (2) requires Daniel technical call, (3) requires hands-on access or document samples. Sequenced action plan with owners and gates. |
| `03_discussion_strategy_and_deliverables` | Dashboard is a fundamental feature, not a differentiator. IT/security stakeholders: work with them, don't question Brad's authority in writing. Agentic AI: solve the use case, don't upsell. The "Gen AI stance" is not real -- it was a drastic overreaction to a bad POC. Two separate deliverables: problem restatement + preliminary approach. |
| `03_discussion_final_clarifications` | Restate using their framing in Doc 1, reframe from authority in Doc 2. Representative sample means failure cases + known good across all data source types, not just documents. The control plane is a project/solution, never a product. Prior work is credibility, not a pre-built offering. Stay laser-focused on Brad's problem statement -- mention future potential only in passing. |

## The Technical Approach in Brief

1. **Discard prior work.** Everything Lam tried was the wrong approach -- custom model training for a problem that is largely deterministic matching plus contextual AI classification.

2. **Hybrid architecture.** Deterministic layer (synonyms lookup, regex, keyword lists via Microsoft Purview) for known patterns with zero false positives. AI layer for contextual classification where patterns can't reach. Unified control plane wraps both into a single interface indistinguishable to end users.

3. **Ingestion-first.** Reject contaminated content at upload rather than detecting/redacting downstream. This eliminates batch redaction as an ongoing operational burden. Historical data gets a one-time cleanup (Day Zero -> Day One), then the system is clean by construction going forward.

4. **Enterprise tools.** Push Lam toward Azure AI Foundry, Microsoft Purview, and managed Azure services. These are solved problems -- don't reinvent the wheel. Option for custom components only where Azure services are cost-prohibitive or insufficient.

5. **Application-by-application migration.** One app at a time. Each migration reduces the remaining workload because data sources are shared across apps. No big bang.

## What's Blocking Progress

Everything is gated by Lam providing specifics:
- **Name one application** (the sales team must get this -- it is not a technical question)
- **Provide representative samples** (failure cases + known good examples from that application's data sources)
- **Schedule the Daniel technical call** (for prior work autopsy, infrastructure details, and organizational reality check)

Without these, we cannot scope a POC, estimate costs, or write a meaningful proposal.

## Deliverable Structure

**Document 1: Problem Restatement** -- Uses Lam's framing (two swim lanes, detection vs. redaction). Pure problem articulation, no solutions. Satisfies Brad's "repeat back" gate.

**Document 2: Preliminary Approach** -- Reframes from authority. Presents the hybrid architecture, ingestion-first philosophy, control plane concept, and enterprise tools strategy. Explicitly framed as preliminary, requiring refinement through discovery with Lam's technical team.

Both documents are needed before the follow-up meeting where Brad expects "approaches with trade-offs."

## State After This Set

BayOne has a clear technical vision and engagement strategy. The ball is with the sales team to extract specifics from Lam (application name, samples, Daniel access). Once those arrive, Colin can build the POC and draft both deliverable documents. The sales workshop (3/24-3/27) is the next in-person opportunity to polish the proposal.
