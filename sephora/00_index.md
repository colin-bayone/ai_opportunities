# Sephora EDW Modernization - Documentation Index

*BayOne Solutions Engagement*
*Last updated: February 12, 2026*

---

## Quick Links

### Core Understanding
- [Project Overview](project/00_project_overview.md) - What the project is, migration path, current state
- [Key Terms & Glossary](project/01_glossary.md) - SSAS, Cognos, DataStage, Databricks, etc.
- [Scope and Scale](project/03_scope_and_scale.md) - Quantified scope: 6,000 reports, 8 cubes, 800+ KPIs

### Problem Analysis
- [Pain Points & Opportunities](project/02_pain_points.md) - SSAS blocker, ETL conversion, embedded SQL, data mapping

### People
- [Stakeholder Directory](stakeholders/00_people_directory.md) - Who's who at Sephora and BayOne

### Strategy & Planning
- [BayOne Positioning](planning/00_bayone_positioning.md) - How we position ourselves, two-track model
- [Open Questions](planning/01_open_questions.md) - Gaps to fill, questions to answer

### Timeline
- [Engagement History](project/04_engagement_timeline.md) - Chronological record of interactions

### Source Materials
- [context/email1.txt](context/email1.txt) - Full email thread Dec 2025 - Feb 2026
- [context/email2.txt](context/email2.txt) - Zahra's internal planning email

---

## Folder Structure

```
sephora/
├── 00_index.md              ← You are here
├── context/                 ← Source documents (emails, transcripts)
│   ├── email1.txt
│   └── email2.txt
├── project/                 ← Current state documents
│   ├── 00_project_overview.md
│   ├── 01_glossary.md
│   ├── 02_pain_points.md
│   ├── 03_scope_and_scale.md
│   └── 04_engagement_timeline.md
├── planning/                ← Strategy and approach
│   ├── 00_bayone_positioning.md
│   └── 01_open_questions.md
├── stakeholders/            ← People and relationships
│   └── 00_people_directory.md
└── research/                ← Investigation materials (empty for now)
```

---

## Key Numbers at a Glance

| Metric | Value |
|--------|-------|
| Reports to migrate | ~6,000 (15-20 years legacy) |
| SSAS Cubes | 8 |
| KPIs | 800+ |
| Dimensions | 300 |
| Source systems | 20+ |
| EDW age | ~20 years |
| Timeline | 2026-2028 (possibly 2027 with AI acceleration) |
| Rate strategy | $105-115/hr ($120+ on-site only) |

---

## Key People at a Glance

**Sephora (Mani's Org):**
- **Vlad** - CIO (executive sponsor)
- **Mani Soundararajan** - VP (key decision-maker, wants proposal-led conversations)
- **Ram** - Acquisition & Retention (reports to Mani, actively hiring)
- **Andrew Ho** - Sr. Director, Influencer/Media/Marketing AI (reports to Mani, actively hiring)
- **Rizwan Khan** - CRM & Marketing Personalization (reports to Mani, hiring late Q1)
- **Grishi Chakraborty** - Director, Data Eng/BI (reports to Andrew, actively hiring)
- **Ravi** - Engineer (Colin lunch today)

**Domain Leaders (Decentralization):**
- **David/Natalia** - Stores (Model 1)
- **Rajesh** - E-commerce/Omni (Model 2)

**BayOne:**
- **Colin Moore** - Director of AI (technical lead)
- **Zahra Syed** - Director, Strategic Accounts (sales lead, had key roadmap conversation)
- **Neha Malhotra** - Head of Recruiting (staffing track)

---

## Current Status

**Phase:** Discovery & Positioning (Nearing Completion) → Proposal Development (Starting)

**Today (Feb 12, 2026):**
- Colin meeting with Mani (VP) - **proposal-led conversation expected**
- Colin lunch with Ravi (Engineer)

**Key Strategic Insight:**
> *"If someone comes with groundwork done and a proposal — that would be very productive."* - Mani

**They want:** Proposal-led, not discovery. They are **not locked into Databricks** AI tools yet.

**Next Steps:**
1. ~~Clarify staffing vs. solutions~~ **DONE** - both active
2. ~~Identify decision authority~~ **DONE** - Mani is key
3. Prepare 1-page POV: AI-Assisted EDW Modernization Framework
4. Get sample reports from Grishi
5. Define pilot scope (Finance - Business Planning suggested)

---

## Open Questions (Priority)

**Answered:**
- Do they want AI help? → **YES, explicitly**
- Proposal or discovery? → **Proposal-led**
- Locked into Databricks? → **NO, still experimenting**

**Remaining:**
1. What AI POCs have they already done?
2. What is Databricks proposing?
3. Budget authority for solutions engagement?
4. Sample reports across complexity levels?

See [Open Questions](planning/01_open_questions.md) for full list.
