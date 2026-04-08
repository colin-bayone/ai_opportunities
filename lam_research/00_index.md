# Lam Research — Engagement Index

*BayOne Solutions*
*Last updated: 2026-04-08*

---

## Active Project

### [IP Protection](ip_protection/)
- **Status:** Proposal phase — proposal due by April 10, decision expected ~April 17
- **Structure:** Full Singularity (8 document sets, 47 research files, 8 deliverables, 11 presentation slides)
- **Application:** Escalation Solver (homegrown escalation management platform)
- **Problem:** Customer-confidential data in knowledge base prevents cross-customer sharing. Customers are competitors (semiconductor fabs).
- **Key contacts:** Bradley Estes (Managing Director, decision-maker), Mikhail Krivenko (Head of Product, technical driver), Daniel Harrison (Director of Engineering, GFSO)
- **BayOne team:** Colin Moore (technical lead), Anuj Sehgal (relationship), Pratik Sharda / Amit Grover (technical support)
- **Start here:** `ip_protection/research/00_methodology_2026-04-06.md`, then summaries in order

**Company:** Lam Research ($17B+ revenue, ~17,000 employees, wafer fabrication equipment)

---

## Quick Context

- **Two use cases:** (1) Batch redaction for self-help search, (2) Real-time detection for escalation entry point
- **Prior attempts:** 18 months of work, Transformers/SpaCy/Azure AI, 21% false positive (reduced to 17%), no golden set created
- **BayOne approach:** Layered funnel (deterministic -> ML/NLP -> Gen AI), ground truth first, linear not parallel
- **POC scope:** Five free-text fields, two entity types (customer name, fab ID) on Escalation Solver
- **Key advantage:** Lam has no in-house AI expertise. Colin built similar systems at Coherent (semiconductor/defense ITAR).

---

## Archive

Pre-Singularity content preserved in [`archive/`](archive/). This includes:

| Folder | Contents |
|--------|----------|
| `context/` | 3 original source transcripts (March 12). Duplicated in ip_protection/source/ and ip_protection/archive/. |
| `project/` | 29 files of pre-Singularity research (sets 01-03) and Big Four quality review. Superseded by ip_protection/research/. |
| `planning_legacy/` | Session handoff from March 20 and skill notes. Copied to ip_protection/planning/ before archiving. |
| `deliverables_legacy/` | March 12 deliverables (problem restatement, preliminary approach, information request, email draft). Copied to ip_protection/deliverables/ with dated filenames before archiving. |
| `org_chart.md` | Older version. ip_protection/org_chart.md is authoritative. |

---

## Reorganization Log

**2026-04-08:** Consolidated using Singularity Reorganization Guide.
- Validated ip_protection/ Singularity structure (all research checks pass)
- Moved March 12 deliverables into ip_protection/deliverables/ with dated filenames
- Moved internal meeting summary from deliverables/ to planning/ (not client-facing)
- Copied session handoff and skill notes into ip_protection/planning/
- Wrote fresh session handoff reflecting April 6 state
- Archived all top-level legacy content
