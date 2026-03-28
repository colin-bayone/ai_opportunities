# Lam Research — AI Opportunities

**Company:** Lam Research ($17B+ revenue, ~17,000 employees, wafer fabrication equipment)
**Opportunity:** IP Protection — detecting/redacting customer-confidential information in unstructured data to enable cross-customer knowledge sharing
**Primary Contact:** Bradley Estes (Managing Director, Knowledge & Advanced Services)
**BayOne Sales:** Anuj Sehgal (VP of Sales)
**Status:** Discovery complete (March 12, 2026), problem restatement delivered, follow-up pending

## Directory Structure

- `context/` — Source materials (call prep, meeting transcripts, debrief recordings)
- `project/` — Structured knowledge (blockchain-style research sets, use case analyses)
- `planning/` — Strategy, session handoffs, skill notes
- `deliverables/` — Client-facing outputs (problem restatement HTML)

## Related Session Folders (in `claude/`)

| Session | Content | Status |
|---------|---------|--------|
| `claude/2026-03-20_lam-research` | Full discovery: 3 analytical sets (prep, call, debrief), 42 files, blockchain-style | Complete |
| `claude/2026-03-20_big4_lam_problem_restatement` | Big Four QA review of problem restatement deliverable | Minor revision needed |

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
