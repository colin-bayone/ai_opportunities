# Session Summary: 2026-02-26_sephora-hiring

## Client/Opportunity
**Sephora** — ML/Data Engineering hiring initiative. Hiring manager: Ravi. Fortune 500 company.

## Purpose
Create three targeted job descriptions from Ravi's original Senior ML Engineer JD by splitting one broad "unicorn" role into specialized tracks: ML Engineer (75% ML / 25% light data eng), Data Engineer (75% data / 25% MLOps), and Senior ML/Data Engineer (full-stack unicorn). Also includes recruiter feedback for a candidate interview (Anushree Joshi).

## File Tree
```
2026-02-26_sephora-hiring/
  00_jd_creation_plan.md                        (9.4K)  Master plan: strategic overview, 3-role split rationale,
                                                        8-phase execution plan, technical requirements per JD,
                                                        golden rules (stage before approve, never edit originals),
                                                        open questions for Colin (titles, experience, degrees).
                                                        Source: sephora/ravi/ravi-ml-jd.txt + jd_ai_engineer_sephora.md
  01_skill_classifications.md                   (9.5K)  Requirements matrix: must-have vs nice-to-have for each
                                                        role across 10+ skill categories (Languages, ML/Deep
                                                        Learning, MLOps, Data Engineering, Cloud Infrastructure,
                                                        DevOps, Soft Skills). Universal: AI pair programming
                                                        proficiency + university degree. Recommendations for
                                                        unicorn elevation (Scala, model optimization, Spark,
                                                        Kafka, Kubernetes).
  candidate_guide/
    anushree_joshi_recruiter_feedback.md         (5.5K)  Interview feedback for Senior AI Solutions Engineer
                                                        candidate. Recommendation: ADVANCE. Standout: MCP
                                                        expertise (embedding-based matching for 100+ tool
                                                        server), log classification as traditional ML not LLM,
                                                        document processing (PDFs, tables), retrieval
                                                        improvements (hybrid matching, cross-encoder, query
                                                        expansion), AI tooling (Cursor). 9 strengths listed.
                                                        1 minor concern (abstract state management).
    anushree_joshi_recruiter_feedback.html       (14K)   BayOne-branded HTML version — purple gradient header,
                                                        Inter font, print-optimized, icon-styled strengths,
                                                        gradient "Bottom Line" box.
  staging/
    jd_ml_engineer_additions.md                 (7.1K)  Proposed additions for ML Engineer JD: title change
                                                        ("AI Engineer" -> "ML Engineer"), Position Overview
                                                        rewrite, restructured responsibilities (50% ML Dev,
                                                        30% MLOps, 20% Team Collab), Required Qualifications
                                                        (Education, ML/DL, SWE, Cloud, AI Dev, Working Style),
                                                        Preferred Qualifications, closing statement.
                                                        Status: AWAITING APPROVAL.
    jd_ml_engineer_removals.md                  (7.3K)  9 sections inherited from AI Engineer JD requiring
                                                        removal for ML Engineer role: Position Overview,
                                                        AI-Assisted Development, Agent & Skill Development
                                                        (Claude Code specific), etc. Each with current text
                                                        and removal rationale. Status: AWAITING APPROVAL.
    jd_ml_engineer_repetition_fixes.md          (6.9K)  Addresses "ML" overuse (30+ occurrences). Strategy:
                                                        spell out in title, keep in headers, drop qualifier
                                                        in body. Before/after comparisons. Reduces "ML" from
                                                        ~30 to ~6 occurrences. Status: AWAITING APPROVAL.
```

## Key Deliverables
1. **JD creation plan** — 3-role split strategy from 1 unicorn role
2. **Skill classifications matrix** — complete must-have/nice-to-have by role
3. **Recruiter feedback** (md + HTML) — Anushree Joshi evaluation with 9 strengths
4. **ML Engineer JD staged changes** — 3 files (additions, removals, repetition fixes) awaiting approval
5. **Workflow methodology** — golden rules: never edit originals, stage all changes, require explicit approval

## Cross-References
- **Source JD:** `sephora/ravi/ravi-ml-jd.txt` and `sephora/ravi/job_descriptions/jd_ai_engineer_sephora.md`
- **Output target:** `sephora/ravi/job_descriptions/` for final JDs + HTML versions
- **Cisco JD variant:** `2026-02-02_resource-planning/deliverables/jd_ai_engineer_sephora.md` (earlier version)

## Suggested Home
`sephora/` — Sephora hiring work for Ravi's team.

## Summary Statistics
- **Total files:** 7 (5 markdown, 1 HTML, 1 plan)
- **Total size:** ~60 KB
- **JDs planned:** 3 (ML Engineer, Data Engineer, Unicorn)
- **JDs in staging:** 1 of 3 (ML Engineer, Phases 3-5 pending)
- **Candidate evaluated:** 1 (Anushree Joshi — recommend advance)
