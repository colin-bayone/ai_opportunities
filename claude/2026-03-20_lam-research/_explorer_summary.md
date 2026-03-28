# Session Summary: 2026-03-20_lam-research

## Client/Opportunity
**Lam Research** — $17B+ semiconductor company. IP protection: detecting/redacting customer-confidential information in unstructured data to enable cross-customer knowledge sharing. Contact: Bradley Estes (Managing Director, Knowledge & Advanced Services).

## Purpose
Blockchain-style discovery documentation for Lam Research engagement. Three analytical sets: pre-call prep (Set 01), discovery call decomposition (Set 02), and internal debrief (Set 02a). Covers problem understanding, technical use cases, infrastructure landscape, and engagement strategy.

## File Tree
```
2026-03-20_lam-research/
  org_chart.md                                  (var)   Living people map — Brad (room controller, decision
                                                        maker), Mikhail (problem presenter, Head of Product),
                                                        Pat/Pratik (supporting), Daniel (technical lead),
                                                        Jason Callahan (CISO). BayOne: Colin, Anuj (VP Sales).
  planning/
    session_handoff_2026-03-20.md                (var)   End-of-session handoff, file inventory, next steps
    skill_notes.md                              (var)   Best practices for future meeting-decomposition skill

  research/
    00_methodology_2026-03-20.md                (var)   Blockchain-style approach: append-only, numbered,
                                                        bridge documents, dual people-tracking

    Set 01 — Pre-Call Prep (6 files):
    01_call_prep_situational_context_2026-03-12.md    Company profile, why IP protection is existential
    01_call_prep_discovery_strategy_2026-03-12.md     8-category question bank, signals to listen for
    01_call_prep_technical_reference_2026-03-12.md    Microsoft stack (Sentinel/Purview/Content Safety)
    01_call_prep_people_2026-03-12.md                 Pre-call people intelligence
    01_call_prep_summary_2026-03-12.md                Set 01 summary, 4 working hypotheses

    Bridge:
    01-02_changes_2026-03-12.md                       Pre-call vs actual: validated/invalidated/superseded

    Set 02 — Discovery Call (8 files):
    02_meeting_people_2026-03-12.md                   Who was there, relationship dynamics
    02_meeting_topic_map_2026-03-12.md                9 major topics, proposed deep-dive structure
    02_meeting_technical_use_cases_2026-03-12.md      2 use cases: (1) batch redaction for self-help search,
                                                      (2) real-time detection for escalation. Performance:
                                                      2-5 sec detection, <1% false positive.
    02_meeting_what_was_tried_2026-03-12.md           Transformers/SpaCy/Azure AI all ~20% false positive,
                                                      fine-tuned to 17%. 1,000+ hour labeling paused.
                                                      Colin: "prior approaches fundamentally wrong."
    02_meeting_infrastructure_and_access_2026-03-12.md  On-prem + cloud, LamGPT, Copilot, 6+ search systems,
                                                      no unified data lake, IAM ~2 years in.
    02_meeting_business_opportunity_2026-03-12.md     Brad's ownership, engagement prefs (rapid prototyping),
                                                      ROI framing, deal signals
    02_meeting_speaker_dynamics_2026-03-12.md         Brad (controller), Mikhail (precise), Colin (strengths:
                                                      20%/ChatGPT diagnosis; weaknesses: verbosity)
    02_meeting_summary_2026-03-12.md                  Set 02 summary

    Set 02a — Internal Debrief (4 files):
    02a_debrief_people_2026-03-12.md                  Candid takes: Brad (manage him), Mikhail (lacks depth),
                                                      Pat (awesome). Anuj Sehgal introduced.
    02a_debrief_internal_assessment_2026-03-12.md     Colin: "AI 101, RAG chatbot, easy work." Anuj: "start
                                                      small, embed, scale." Lam has no in-house AI expert.
    02a_debrief_action_items_2026-03-12.md            Email Pradeep/Pat, two paths (A: specifics, B: synthetic).
                                                      Phase-based proposal. Sales workshop 3/24-3/27.
    02a_debrief_summary_2026-03-12.md                 Core read: "astonishment at unsophistication"

  source/
    lam_call_prep (1).txt                       (var)   Raw pre-call prep document
    lam_meeting_3122026.txt                     (var)   Raw discovery call transcript
    anuj_and_colin_after_call1.txt              (var)   Raw post-call debrief (candid, unfiltered)

  decisions/                                    (empty)
  progress/                                     (empty)
```

## Key Deliverables
1. **3-set blockchain-style decomposition** — 18+ research files preserving discovery arc
2. **Bridge document** (01-02) — tracks hypothesis validation/invalidation
3. **Dual documentation** — diplomatic meeting notes (Set 02) + candid internal assessment (Set 02a)
4. **Living org chart** — updated per meeting with sentiment and dynamics
5. **Technical use case analysis** — 2 use cases with performance requirements

## Lam Research Context
- **Problem:** Customer-confidential data in unstructured knowledge base prevents cross-customer sharing
- **Prior attempts:** Transformers, SpaCy, Azure AI (all ~20% false positive), fine-tuned to 17%, 1,000+ hour labeling paused
- **Colin's assessment:** Prior approaches wrong. Needs curated dictionaries + fuzzy matching, not ML.
- **Phase strategy:** Phase 1 MVP on 2 fields (customer name, file name), Phase 2 expansion, Phase 3 scale
- **Competitors:** Deloitte, Capgemini, Accenture
- **Key advantage:** Lam has no in-house AI expert; BayOne fills gap

## Cross-References
- **QA review:** `2026-03-20_big4_lam_problem_restatement` (#25) — quality audit of deliverable
- **Opportunity catalog:** `2026-03-17_opportunity_catalog/research/06_lam_research.md`
- **Deliverables location:** `cisco_projects/cicd/claude/2026-03-20_lam-research/deliverables/`
- **People:** Brad Estes, Mikhail Krivenko, Daniel, Pat/Pratik, Jason Callahan (CISO); BayOne: Colin, Anuj

## Suggested Home
New `lam_research/` directory — major new client engagement.

## Summary Statistics
- **Total files:** ~42
- **Document sets:** 3 (pre-call, discovery call, debrief)
- **Detail files per set:** 5-7 + summary
- **Key people identified:** 12 (7 Lam + 5 BayOne)
- **Prior approaches documented:** 5
- **Use cases identified:** 2
- **Hypotheses tested:** 4 (1 invalidated, 1 validated, 1 superseded, 1 open)
- **Competitors identified:** 3
