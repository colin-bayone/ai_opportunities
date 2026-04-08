# 01 - Meeting: EDW Modernization Project

**Source:** /sephora/edw_modernization/source/mani_meeting1_2026-02_formatted.txt
**Source Date:** 2026-02 (Initial Discovery Call with Mani)
**Document Set:** 01 (Mani Meeting 1)
**Pass:** Focused deep dive on EDW Modernization opportunity

---

## 1. Project Overview

Mani described a major initiative called **EDW Modernization** — a multi-year effort to move Sephora's entire enterprise data warehouse and reporting ecosystem from legacy technologies to a modern platform. This is positioned as one of the most significant projects in his portfolio for 2026 and beyond.

**Key statement (line 64):** "We're starting a big project called EDW Modernization."

**Key statement (line 66-67):** "This project is to move from all legacy technologies into modern technologies."

**Key statement (line 68):** "We're going to be re-engineering all the reports that we have done over the past 15, 20 years."

---

## 2. Legacy Systems Being Replaced

### IBM Cognos
- Primary legacy reporting tool referenced throughout the discussion
- Contains reports built over 15-20 years
- Mani described the Cognos codebase as deeply embedded and difficult to untangle: "If you look at Cognos, there are actually like 15, 20 years back, actually like something might have been implemented. So the queries are actually like very deep inside the code." (lines 185-186)
- Manual analysis of the Cognos codebase would "take years" even to finish, let alone start (lines 187-188)
- **Not fully going away** — in some areas, Cognos will continue as the reporting front-end but will be re-pointed to the new data platform instead of the old database (line 74)

### SQL Server
- Legacy database platform underpinning the current reporting environment
- Being replaced by Databricks as the data platform
- Explicitly named alongside Cognos as the technologies being moved away from (lines 71, 163, 174)

### Other Legacy Technologies
- Mani referenced "old legacy technologies" broadly (line 71) and mentioned that the supply chain and merchandising areas "still have legacy technologies" (line 59), which is why those departments are being modernized later
- The exact inventory of all legacy systems was not enumerated, but Mani characterized it as "very old technologies" with deep technical debt (line 85)

---

## 3. Modern Target Systems

### Databricks
- **Primary data platform** for the modernized environment
- Databricks is already actively partnering with Sephora on this initiative (line 194): "We have also asked Databricks to come with recommendations."
- Mani's team is "experimenting, partnering with Databricks saying like, what is the right tool to use?" (line 175)
- Databricks is also developing AI-oriented tools that could assist with the migration (line 183)

### Tableau
- Named as one of the potential reporting/visualization targets for certain areas (line 73)
- The determination of which reports go to Tableau versus other tools appears to be area-dependent

### ThoughtSpot
- Named alongside Tableau as another potential reporting/analytics front-end (line 73)
- Again, deployment appears to vary by business area

### Cognos (Retained, Re-platformed)
- In some areas, Cognos will be kept as the reporting layer (line 74)
- However, the underlying data source will shift from the old database (SQL Server) to the new data platform (Databricks)
- This represents a pragmatic middle ground — not every report gets a full front-end migration, but all reports move to the modern data foundation

---

## 4. Scale of the Effort

### Report Volume
- **Thousands of reports** accumulated over 15-20 years (line 69): "We have about seven — like thousands of reports, basically."
- Mani explicitly stated he does not have an exact count (line 70): "Don't have an exact [number]."
- Reports span every business area: finance, supply chain, stores, e-commerce, and more (lines 199-200)

### Organizational Breadth
- Reports are "scattered" across the entire organization (line 202)
- Reports exist for finance, supply chain, stores, and other departments (lines 200-201)
- Each department has its own set of reports that must be assessed and migrated

### Technical Depth
- 15-20 years of accumulated code and queries in legacy systems (lines 68-69, 185)
- Cognos queries are "very deep inside the code" — deeply embedded business logic (line 186)
- Manual review of the codebase would take an impractical amount of time (lines 187-188)

---

## 5. Timeline and Phases

### Overall Duration
- **Three-year project** as currently planned (line 75): "This one will be a three-year project."
- Current plan extends through **2028** (line 81)
- Aspiration to compress the timeline — finish by **2027** or **early 2028** (line 83): "We're trying to see how we can possibly do it in 2027 or maybe finish it off by early 2028."

### Year One (2026)
- Project has **already started** as of the meeting date (line 76): "We already started, by the way."
- Grishi and Andrew Ho have been involved from the Sephora side; BayOne's Zara has been engaged from a sourcing perspective (lines 77-78)

### Department-by-Department Rollout
- The migration is **not** being done as one centralized effort — it is proceeding **department by department** (line 203): "We are taking department by department."
- This is the primary reason for the three-year timeline (line 203): "That's why it is like right now the plan is like three-year initiative because we are taking like department by department."

### Phase 1: Finance Department
- **Finance is the first department** being migrated (line 203): "We're taking finance department first and that's the first department we have taken."
- Within finance, they are starting with **Business Planning** specifically (line 205): "Finance department, we're not taking all the reports. Finance department, Business Planning is something we are taking first."
- **Accounting will come later** within the finance migration (line 205): "Accounting we'll take later."
- This sub-division approach (taking subdivisions within departments, not entire departments at once) is the operating model (line 206)

### Later Phases: Supply Chain and Merchandising
- Supply chain and merchandising areas are explicitly deferred because they "still have legacy technologies" (line 59)
- In contrast, stores and e-commerce (.com) are "already in the modern technology" (line 60), making them easier candidates for the reports democratization model
- The implication is that supply chain/merchandising reports migration will happen in later phases after the foundational departments are done

---

## 6. AI as a Migration Accelerator

Mani expressed significant interest in using AI to speed up the EDW modernization, citing two distinct use cases:

### Use Case 1: Batch Processing Reports (Instead of One-by-One)
- **The problem:** If the team migrates reports one at a time, the project will take too long (line 176): "If we go report by report, that actually like people — it will take a long time for us."
- **The aspiration:** Use AI or tooling to process multiple reports simultaneously (lines 177-178): "Can we do something like maybe if we do this, we can finish off three reports at one shot... we can finish off like six reports at one shot, so we can expedite the delivery."
- This is about **throughput acceleration** — grouping similar reports and migrating them in batches rather than treating each as a unique project

### Use Case 2: Codebase Analysis and Discovery
- **The problem:** The Cognos codebase is 15-20 years old with deeply embedded queries that would take years for humans to fully audit (lines 185-188)
- **The aspiration:** AI tools that can analyze the legacy codebase and proactively identify issues, dependencies, and migration considerations (lines 189-192): "Look at the codebase... AI would itself would kind of proactively come and tell us — these things are actually like something to watch out for. This is what you can take."
- Mani wants AI to "analyze the codebase and then say, okay, these are all the places for us to mind for" (line 192)
- This is about **automated code archaeology** — using AI to map and assess the legacy landscape before and during migration

### Databricks Partnership on AI Tooling
- Databricks is "already coming up with AI-oriented tools" relevant to this effort (line 183)
- Sephora has "asked Databricks to come with recommendations" on AI-assisted migration approaches (line 194)
- This creates a competitive dynamic — BayOne would need to bring something differentiated beyond what Databricks is already offering natively

---

## 7. Reports Democratization (Structural Context for EDW Modernization)

The EDW modernization is happening in parallel with a broader organizational shift in how reports are owned and delivered. This context is important because it affects who will be consuming the modernized reports and what governance model applies.

### Current State
- One central team (Mani's team) handles enterprise-wide reports and analytics (lines 16-17)
- Data has already begun to be democratized; now reports are following (line 16): "Data is already kind of — we started the journey to democratize. Now on top of data, reports is also getting democratized."

### Target State
- Mani's team becomes a **lean, core platform/governance team** (line 17): "My team will become a lean team, which is like a core, like a reports platform kind of a team."
- Individual domain engineering teams (stores, e-commerce, supply chain) will own their own reporting as part of their project delivery (lines 18, 21-23)
- The rationale: domain teams know their business best — "report is just actually reporting what they have done. So it doesn't have to be done by another separate team" (lines 23-24)

### Three Experimental Models for Transition
Mani described three parallel experiments for how to transition report ownership to domain teams:

**Model 1 — Stores (David's Team):**
- David's team is already taking on stores-related reports and retail project delivery (lines 27-28)
- Andrew Ho and Grishi serve as subject matter experts, available for consultation (line 29)
- Mani's team establishes framework and governance: right tools, data validation, reviews (lines 29-31)
- Transition to stability estimated at approximately one year (line 32)
- David and Natalia are the hiring managers; Grishi sits on interview panels (lines 43-46)

**Model 2 — E-commerce/Omnichannel (Rajesh's Area):**
- Starting with omnichannel order fulfillment use cases — orders transitioning to stores for same-day delivery, buy-online-pickup-in-store (lines 33-34)
- Engineers report to Grishi initially (line 35) but execute projects in Rajesh's area (line 50)
- After a six-month pilot (around June-July 2026), if successful, engineers will fully transition to Rajesh's org (line 41)
- Grishi remains hiring manager during the pilot period (line 50)

**Model 3 — Supply Chain/Merchandising (Kalyan's Area):**
- Continues the current operating model (delivery, hiring, and engineers all under Grishi's responsibility) (lines 51-55)
- Will transition to the decentralized model only after Models 1 and 2 are proven successful (line 57)
- Explicitly deferred because of legacy technology dependencies (lines 59-62)

### Governance Role for Mani's Core Team
- Framework definition and governance (line 29)
- Tool selection standards — "what's the right tool to use?" (line 29)
- Data quality reviews — validating that "data is coming in correctly or not" (line 30)
- Subject matter expertise on demand (line 29)

---

## 8. Challenges, Blockers, and Concerns

### Scale Challenge
- Thousands of reports over 15-20 years make a one-by-one approach infeasible (lines 69, 84, 176)
- The sheer volume is the primary reason the timeline is three years even with a department-by-department approach

### Technical Debt in Legacy Codebase
- Cognos code from 15-20 years ago has queries buried deep inside the codebase (lines 185-186)
- Manual analysis would "take years" — this is described as a genuine blocker, not a nice-to-have concern (lines 187-188): "Forget like the starting, but to finish it, it will take a long time."

### Timeline Pressure
- The plan goes through 2028 but there is pressure to compress to 2027 or early 2028 (lines 81-83)
- This compression aspiration depends on finding ways to accelerate delivery — specifically through AI and batch processing approaches (line 87): "We are hoping that tools like AI will come to help to speed this up."

### Tool Selection Still in Progress
- Mani's team is "still experimenting" on the right tools, specifically in partnership with Databricks (line 175)
- The choice between Tableau, ThoughtSpot, and retained Cognos varies by area and is not yet fully decided (lines 73-74)
- This creates both an opportunity (to influence tool selection) and a risk (decisions may shift as experimentation continues)

### Competitive Positioning Risk
- Databricks is already embedded as a partner and is being asked for AI-related recommendations (line 194)
- Any AI acceleration proposal from BayOne would need to complement or exceed what Databricks is offering natively
- Mani explicitly suggested that any external consultant should "come with groundwork" already done rather than starting from scratch (lines 159-162)

---

## 9. Specific Numbers and Data Points

| Data Point | Value | Source Line |
|---|---|---|
| Years of legacy reports | 15-20 years | 68-69, 185 |
| Approximate report count | "Thousands" (no exact number) | 69-70, 84 |
| Project duration (planned) | 3 years (through 2028) | 75, 81 |
| Compressed target | Finish by 2027 or early 2028 | 83 |
| First department | Finance (Business Planning subdivision first) | 203-205 |
| Model 2 pilot evaluation | ~6 months (June-July 2026) | 41 |
| Stores transition to stability | ~1 year | 32 |
| Project start | Already started as of meeting date (Feb 2026) | 76 |
| Legacy technologies named | IBM Cognos, SQL Server | 71 |
| Modern targets named | Databricks, Tableau, ThoughtSpot | 73 |
| Batch processing aspiration | 3-6 reports at once instead of one-by-one | 177-178 |

---

## 10. BayOne Opportunity Assessment

### Direct Opportunity: AI-Accelerated Migration
Mani explicitly invited a proposal for AI-assisted migration (lines 195-197): "This is something that you can take it back to that person and they can come back with a proposal." The two concrete use cases are:
1. Batch report migration tooling (processing multiple reports simultaneously)
2. AI-driven legacy codebase analysis (automated discovery and assessment of Cognos queries/logic)

### Requirements for Engagement
- Mani set clear expectations for how an external AI consultant should engage (lines 159-162): come prepared with groundwork, talk to the teams first, then present a proposal — not start with "what are you guys doing?"
- This means Colin would need to be briefed on the tech stack, the Cognos codebase structure, and the Databricks target before the initial meeting
- A one-pager or preliminary proposal was discussed as a reasonable first deliverable (line 214)

### Competitive Landscape
- Databricks is already a partner and is developing its own AI migration tools
- BayOne's value would need to be additive — either through proprietary tooling, deeper code archaeology capability, or integration expertise that Databricks does not offer natively

### Hiring Pipeline Connection
- The EDW modernization drives demand for engineers with AI skills (lines 330-331): "We are coming up with completely like agentic coding and AI and all those things. So that's will be a new required skill set."
- Mani asked for two profile types to be pipelined: full-stack engineers, and AI/data processing specialists (lines 341-344)
- This hiring demand is directly tied to the EDW modernization staffing needs

---

## 11. Key Quotes (Verbatim, Corrected for Transcription Errors)

**On project scope:**
> "We're going to be re-engineering all the reports that we have done over the past 15, 20 years." (line 68)

**On legacy complexity:**
> "If you look at Cognos, there are actually like 15, 20 years back, something might have been implemented. So the queries are actually very deep inside the code. If somebody has to go through that manually, it will take years for us to even finish this." (lines 185-188)

**On AI-driven batch processing:**
> "If we go report by report, it will take a long time for us. So we are saying, what would be an easier way, what would be the right way, the efficient way to do this? Instead of going report by report, can we do something like maybe finish off three reports at one shot, finish off six reports at one shot, so we can expedite the delivery." (lines 176-178)

**On AI codebase analysis:**
> "We are looking for AI to come and help to say, okay, look at the codebase... AI would itself proactively come and tell us, these things are something to watch out for. This is what you can take. It will analyze the codebase and then say, okay, these are all the places for us to mind for." (lines 189-192)

**On phased rollout rationale:**
> "We are taking department by department. We're taking finance department first. But then finance department, we're not taking all the reports. Finance department, Business Planning is something we are taking first. Accounting we'll take later." (lines 203-205)

**On timeline compression:**
> "Right now the plan is already going till 2028. But we're trying to see how we can possibly do it in 2027 or maybe finish it off by early 2028." (lines 81-83)

**On expectation for external consultants:**
> "If that person comes with a little bit of groundwork done, instead of coming and asking 'what is this, what are you guys doing?' — if that person can come with groundwork, talking to the teams and then coming with a proposal, that would be great. That would be a very productive discussion." (lines 159-162)
