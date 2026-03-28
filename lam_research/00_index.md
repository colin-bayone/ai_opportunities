# Lam Research — AI Opportunities

**Company:** Lam Research ($17B+ revenue, ~17,000 employees, wafer fabrication equipment)
**Opportunity:** IP Protection — detecting/redacting customer-confidential information in unstructured data to enable cross-customer knowledge sharing
**Primary Contact:** Bradley Estes (Managing Director, Knowledge & Advanced Services)
**BayOne Sales:** Anuj Sehgal (VP of Sales)
**Status:** Discovery complete (March 12, 2026), problem restatement delivered, follow-up pending

## Directory Structure

```
lam_research/
  org_chart.md                                  Living people map (updated per meeting)
  context/
    2026-03-12_source_transcripts/              3 raw transcripts:
      lam_call_prep (1).txt                       Pre-call prep document
      lam_meeting_3122026.txt                     Discovery call transcript
      anuj_and_colin_after_call1.txt              Post-call debrief (candid, unfiltered)
  project/
    2026-03-12_research/                        Blockchain-style research (append-only, numbered)
      00_methodology_2026-03-20.md                Documentation methodology
      01-02_changes_2026-03-12.md                 Bridge: hypothesis validation/invalidation
      set_01_call_prep/                           5 files: company profile, question bank, tech ref, people, summary
      set_02_discovery_call/                      8 files: people, topic map, use cases, infrastructure, dynamics, etc.
      set_02a_debrief/                            4 files: candid takes, internal assessment, action items, summary
      set_03_discussion/                          7 files: technical approach (3 rounds), strategy, open needs, clarifications
    2026-03-20_quality_review/                  Big Four QA of problem restatement deliverable
      critique.md                                 19/19 compliance checks passed, 2 minor phrasing fixes
      source_analysis.md                          All claims verified against transcripts
  planning/
    2026-03-20_session/                         Session handoff + skill notes
  deliverables/
    2026-03-12_discovery_call/                  Client-facing outputs
      problem_restatement.md / .html              Core deliverable: 9-section problem understanding
      preliminary_approach.md / .html             Technical approach options
      information_request.md / .html              Specific asks for Lam team
      followup_email_draft.md                     Email draft for next steps
      README.md                                   Deliverable context/navigation
```

## Source Session Folders (in `claude/`, marked _MIGRATED)

| Session | Content Migrated To | Status |
|---------|-------------------|--------|
| `claude/2026-03-20_lam-research` | All content (context, research, planning, deliverables) | Migrated 2026-03-28 |
| `claude/2026-03-20_big4_lam_problem_restatement` | project/2026-03-20_quality_review/ | Migrated 2026-03-28 |

## Problem Context

- **The Problem:** Customer-confidential data in knowledge base prevents cross-customer sharing. Customers are competitors (semiconductor fabs).
- **Prior Attempts:** Transformers, SpaCy, Azure AI (all ~20% false positive), fine-tuned to 17%. 1,000+ hour labeling exercise paused.
- **Colin's Assessment:** Prior approaches fundamentally wrong. Needs curated dictionaries + fuzzy matching, not ML.
- **Two Use Cases:** (1) Batch redaction for self-help search, (2) Real-time detection for escalation entry point
- **Phase Strategy:** Phase 1 MVP on 2 fields (customer name, file name) -> Phase 2 expansion -> Phase 3 scale
- **Competitors:** Deloitte, Capgemini, Accenture
- **Key Advantage:** Lam has no in-house AI expert. Colin built similar systems at Coherent (semiconductor/defense ITAR).

## Key People

| Person | Role | Notes |
|--------|------|-------|
| Bradley Estes | Managing Director, Knowledge & Advanced Services | Decision maker, room controller |
| Mikhail Krivenko | Head of Product | Problem presenter, precise but honest about limits |
| Daniel | Technical Lead | Key for follow-up technical discussion |
| Pat/Pratik | Supporting | "Awesome" per Colin |
| Jason Callahan | CISO | Security context |
| Anuj Sehgal | BayOne VP of Sales | Deal driver, "start small, embed, scale" strategy |
