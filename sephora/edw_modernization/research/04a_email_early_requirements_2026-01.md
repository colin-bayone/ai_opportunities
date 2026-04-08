# 04a - Email: Early Requirements and Strategic Analysis

**Source:** /sephora/edw_modernization/source/email1_malika.txt
**Source Date:** 2026-01-28 through 2026-02-04 (Internal email thread)
**Document Set:** 04a (Email Thread)
**Pass:** Focused deep dive on initial requirements capture and Colin's strategic assessment

---

## Thread Overview

This email thread contains four messages spanning from December 11, 2025 through February 4, 2026. The thread captures the earliest requirements gathering for the Sephora EDW Modernization engagement, beginning with Zahra Syed's initial introduction of the opportunity and culminating in Neha Malhotra's confirmation of two separate engagement tracks.

**Thread participants:**
- Zahra Syed (Director Strategic Accounts, Enterprise, BayOne Solutions)
- Colin Moore (Director of AI, BayOne Solutions)
- Neha Malhotra (Head of Recruiting, Enterprise, BayOne Solutions)
- Anuj Sehgal (cc'd throughout)

**Sephora stakeholders referenced:**
- Mani Soundararajan — VP overseeing Marketing Tech, Personalization, Data/AI, Enterprise Reporting, and Analytics
- Andrew Ho — Senior Director, Enterprise Reporting
- Grishi Chakraborty — Director of Data Engineering, BI and Analytics (also referred to as "Gariashi" and "Greshey" in the emails due to varying spellings)
- Rizwan Khan — Senior Manager, Data Warehouse
- Ravibas — referenced as the person who handled first-round screening previously

---

## 1. Zahra's Initial Introduction (December 11, 2025)

Zahra Syed's email to Colin establishes the opportunity after a meeting with Mani Soundararajan.

### What Zahra reported from the Mani meeting:
- Sephora is launching a large EDW modernization program starting the following year (2026)
- Thousands of Cognos/SQL Server reports need to be re-engineered and moved to Databricks + Tableau/ThoughtSpot
- Current timeline extends through 2028
- Mani hopes AI can help accelerate the timeline
- Specific AI application areas Mani mentioned: grouping similar reports, analyzing complex SQL inside Cognos, identifying patterns or redundancies, and reducing manual review

### Mani's expectations for a meeting with Colin:
- Not a blank-slate discovery call
- Mani wants Colin to come in with context already gathered
- Prefers a structured point of view or a simple one-pager/idea anchored in what his teams are experiencing

### Key leaders identified:
- Andrew Ho (Senior Director, Enterprise Reporting)
- Grishi Chakraborty (Director, Enterprise Reporting)
- Rizwan Khan (Senior Manager, Data Warehouse)

---

## 2. Colin's Initial Response and Discovery Questions (December 14, 2025)

Colin's response expressed strong enthusiasm for the opportunity, calling it "the strongest one that I have seen so far." He provided eight structured discovery questions and offered strategic context from his own experience.

### Colin's eight discovery questions:

**Question 1 — Report rationalization:**
Has the team done any work to identify which reports are actually used vs. outdated/redundant?

**Question 2 — Nature of the engagement (three sub-options):**
What kind of help are they looking for?
- Option A: Provide AI capabilities to help Sephora's internal team move faster
- Option B: Apply those capabilities directly and deliver a portion of the migrated reports
- Option C: Some combination/hybrid

**Question 3 — Re-engineering scope beyond reports:**
A move like this usually requires re-engineering beyond just migrating reports. Is someone owning that, or is that also an area where they want help? Specifically called out: ETL pipelines, data models, semantic layer, security/RBAC.

**Question 4 — Understanding of current environment:**
How well do they understand their current reporting environment? Any black boxes or pain points they want to address as part of this?

**Question 5 — Motivation for moving off Cognos:**
What pain points caused the move? Cost, capabilities, platform consolidation?

**Question 6 — Timeline concerns:**
2028 is a very long timeline. Where is the time going? Is the bottleneck analysis, rebuilding, testing, or stakeholder sign-off and re-validation?

**Question 7 — Data landscape:**
Number/type of sources, volume, any compliance considerations.

**Question 8 — Sample reports:**
Requested 3-5 sample reports across different complexity levels. Noted that "reports" can mean anything from tabular Excel-style reports to rich interactive executive-level BI dashboards or very granular specialized engineering data reports. Knowing the types is critical to understanding the situation.

### Colin's relevant experience:
Colin stated that part of his old responsibilities at Coherent was leading all BI reporting and migration, noting that BI fell naturally under AI because of the deep ties with data. He asserted that BayOne has real experience doing exactly what Mani wants.

### Colin's recommended approach:
- Start by talking to the people BayOne already has embedded at Sephora under Andrew, Ram, and Grishi
- Build a base of understanding from those conversations
- Then put something together for Mani

---

## 3. Neha's Structured Requirements Dump (January 28, 2026)

Neha's email is the most substantive message in the thread. It is structured as a 10-section requirements capture from a conversation with Grishi (Director of Data Engineering, BI and Analytics). This represents the first detailed requirements dump from the Sephora side.

### Section 1: Core Program Context

- Sephora has a major 3-year transformation program
- Migration path: Legacy SQL / Cognos EDW to Databricks
- The staffing role being hired sits inside this program
- Required skills for the hire:
  - Understand SQL + DataStage ETL
  - Understand Databricks
  - Handle hands-on work + architecture/design
  - Ideally approximately 10 years of experience ("sweet spot") so they are both hands-on and strategic

### Section 2: Day-to-Day Expectations for the Hire

- Lead design and architecture of the migration
- Hands-on work with:
  - ETL re-engineering
  - Data model redesigns
  - Python (as needed)
  - Databricks workloads
- Work across multiple tracks: Finance, Digital/e-commerce, and others
- All tracks are in different phases of migration

### Section 3: AI Usage Expectations

This section contains a clear delineation of what Sephora does and does not want regarding AI.

**What they DO NOT want:**
- ML engineers
- Data scientists

**What they DO want:**
- Someone comfortable using AI-enabled tooling (specifically referenced: CluedIn, Lakehouse AI tools) to:
  - Speed up code generation
  - Assist with data mapping and lineage discovery
  - Reduce manual ETL discovery work
- AI is currently used today to improve:
  - SQL analysis
  - Data mapping
  - Pattern detection
  - Redundancy identification

**Key clarification:** AI usage is strictly for speed and efficiency, not for modeling. This is a tools-and-acceleration play, not a data science engagement.

### Section 4: Current Problem Areas (High-Level Pain Points)

#### Pain Point A: SSAS Cubes Migration Blocker

- SSAS (SQL Server Analysis Services) Cubes sit on top of the legacy EDW
- To move them to Databricks, they need a connector which currently does not exist
- This is described as a "huge challenge" because the business uses:
  - Excel-based cube interfaces
  - Canned reports
  - Ad-hoc drag-and-drop dashboards
- Switching tools completely (e.g., forcing ThoughtSpot, referred to as "Hotspot" in the email) would cause massive change management impact
- What they want help with: a way to keep the same interface/experience while pulling data from Databricks underneath
- Neha flagged this as "one of the biggest AI-assisted opportunity areas"

#### Pain Point B: Re-engineering Thousands of ETL Pipelines

- There are thousands of DataStage ETL pipelines
- Each requires:
  - Extracting logic
  - Re-architecting for Databricks
  - Rebuilding transformations across many tables
- The mapping is not 1:1 between old EDW and Databricks
- Specific example given: one EDW table may become 5 Databricks tables
- AI ask: tooling that helps extract SQL logic and automatically identify tables, dependencies, and lineage

#### Pain Point C: Embedded SQL Inside Cognos

- Some Cognos reports contain embedded SQL
- Those SQL queries may break when moving to Databricks
- They need help:
  - Detecting break points
  - Rewriting SQL for Databricks
  - Optimizing performance

#### Pain Point D: Data Mapping as the Slowest Phase

- Even with AI, engineers still manually validate mappings
- This slows down each migration track
- They want help streamlining this bottleneck

### Section 5: Reporting Landscape Overview

**Tools in use:**
- Cognos
- Tableau
- ThoughtSpot (referred to as "Hotspot" in the email)
- SSAS cubes (Excel-based)
- DataStage (ETL)
- Databricks
- EDW (SQL)

**Report types:**
- Canned / static reports
- Filtering-based custom reports
- Excel-based pivot/analysis tools
- Email reports

### Section 6: What Sephora Has Already Done

- Completed rationalization/analysis of reports (phase 1)
- Migrated some data into Databricks
- Started re-engineering pipeline work in a few tracks
- Used AI tools for mapping proofs of concept (POCs)
- Validated that AI helps, but manual validation is still required

This is significant: Sephora has already done the rationalization work that Colin asked about in his December 14 email. They have also already begun some migration work, meaning this is not a greenfield effort.

### Section 7: What They Want BayOne and Colin's AI Team to Do

This section contains the core "ask" from Sephora:

1. Help identify solutions (AI-assisted + tooling) that remove bottlenecks in:
   - SQL logic extraction
   - Embedded SQL analysis
   - ETL/DataStage code analysis
   - Data mapping automation
   - Dependency discovery
   - Complexity scoring
   - Migration planning

2. Make recommendations for the missing connector between Databricks and SSAS cubes

3. Help accelerate multi-track progress by reducing manual burdens

4. Be a strategic AI partner, not just staffing

### Section 8: Additional Clarifications from Grishi

- Security and access: no major blockers expected
- PII exists but nothing new or unusual
- Approximately 20 source systems feed the EDW
- The EDW is old (approximately 20 years), massive, and hard to scale

### Section 9: Internal Screening Process Preferences

- Grishi wants the same person as last time (Ravibas) to do the first-round screening
- Rates should never be included in candidate submissions
- Submit candidates normally and send rates separately

### Section 10: What Needs to Be Communicated Back

Neha listed what needs to be articulated to Colin and internal leadership:

- The exact bottlenecks Sephora wants help with
- That this is not just staffing — this is AI-led discovery + solution architecture
- The connector problem for SSAS cubes to Databricks
- The massive scope:
  - **6,000 reports**
  - **8 cubes**
  - **800+ KPIs**
  - **300 dimensions**
  - **20+ source systems**
- Where AI can realistically help (and where it cannot)
- What gap Sephora wants BayOne to fill

---

## 4. Colin's Strategic Analysis (January 30, 2026)

Colin's response is a detailed internal strategic analysis. It identifies risks, separates engagement types, diagnoses the real nature of the technical problems described, and flags organizational politics concerns.

### Fundamental Distinction: Staffing vs. Solutions

Colin identified that the ask blends two very different things:

**Track 1 — Staffing:**
- Sephora wants a senior person (10 years, hands-on + architecture) embedded in their program
- That person works under Sephora's direction

**Track 2 — Solutions/Strategic Partnership:**
- They want AI-assisted tooling, recommendations on approach, help removing bottlenecks
- BayOne owns methodology and recommendations

Colin's analysis of why these must be separated:
- The costing is different
- The accountability is different
- Mixing them creates scope confusion
- The two tracks can conflict: if BayOne places someone on Sephora's team, that person works under Sephora's direction; if BayOne is advising on architecture and approach, BayOne owns methodology and recommendations. Those two things can conflict.

Colin asked: Do we have or can we get clarity on whether Sephora sees these as one engagement or two?

### The SSAS Cube "Connector Problem" — Reframed

Colin directly challenged the framing of the SSAS cube issue:

**What Sephora says the problem is:** There is no connector between Databricks and SSAS cubes.

**What Colin says the problem actually is:** This is not a connector problem. Databricks has plenty of mature connectivity (ODBC/JDBC). You can already natively connect Excel, Tableau, and Power BI today.

**Colin's diagnosis:** What they are really saying is "business users are used to SSAS cubes and we don't want to change their experience." This is a change management problem, not a technical one.

**Colin's warning:** Trying to preserve the legacy cube experience while moving to Databricks is going to create long-term maintenance headaches. If they are investing in a 3-year modernization, they should modernize the semantic layer too, not build compatibility shims to keep 20-year-old services alive. He stated: "I'm not sure they have thought it through from a tech strategy angle... it sounds like they are trying to make everyone happy."

### Change Management and Organizational Inertia Warning

Colin drew on his direct experience to warn about the change management challenge:

- There is a massive amount of inertia to overcome among business users in this regard
- He has never seen a half-in, half-out approach work successfully
- Success requires a strong leader internally at Sephora who has real power to enact and force change
- If that person does not have that power or is a "yes-man" to the business users against the greater technical good, BayOne will be in a difficult position because there will be constant churn

### Questioning the Databricks Strategy

Colin raised concerns about the maturity of Sephora's technology strategy:

- They have a 3-year timeline, but it sounds more like a 3-year goal than a 3-year plan
- It appears they are not doing any mid-to-long range tech strategy planning
- He is unclear on why they landed on Databricks in the first place if they are not planning to actually use it
- This tells him either the strategy was half-baked or there is no one with authority to enforce it

### Organizational Politics Flag

Colin explicitly flagged organizational politics:

- His instinct tells him there are organizational politics at play that might be troublesome
- The risk is only manageable if BayOne is aligned with someone who has final decision-making power at Sephora
- He characterized the situation as not necessarily bad (it creates an opportunity for BayOne) but something to go in with eyes open about

### Colin's Three Prerequisites Before Proceeding

Colin recommended getting clarity on three things before diving into a discussion:

1. **Clarity on staffing vs. solutions as separate tracks.** If they cannot be separated, the boundary between them must be clarified.
2. **Understanding of who has decision-making authority on architecture.** This directly relates to the change management and organizational politics concerns.
3. **Understanding why Databricks was selected.** Do they have in-house hands-on experience? Do they have goals beyond the immediate effort to lift and shift the reporting?

### Colin's Overall Assessment

Despite the risks and concerns, Colin was optimistic: "Overall if we can manage to gently force them to lock down on what they want I think there is a lot of juice that can be squeezed here."

---

## 5. Neha's Confirmation and Follow-Up (February 4, 2026)

Neha's response confirms alignment with Colin's analysis and provides updates.

### Confirmed two separate tracks:
- Staffing roles (Data Lead/Architect to re-engineer ETL pipelines for the Cognos to Databricks migration)
- Potential solutions opportunities

### Validated Colin's connector reframing:
Neha acknowledged that Grishi "mostly talked about the connector problem which you feel is a deeper level change management issue."

### Committed to gathering information on Colin's prerequisites:
- Will get more information on who has decision-making authority on the architecture
- Will find out why Databricks was chosen

### New stakeholder identified:
- Andrew Ho is another stakeholder they can meet with to gather more information

### Proposed in-person meeting:
- Suggested Colin come to Sephora to meet Mani (VP) if time permits

---

## 6. Scale Numbers Summary

These numbers appear in Section 10 of Neha's January 28 email and represent the scope of the EDW modernization:

| Metric | Value |
|---|---|
| Total reports | 6,000 |
| SSAS cubes | 8 |
| KPIs | 800+ |
| Dimensions | 300 |
| Source systems | 20+ |
| EDW age | ~20 years |
| Migration timeline | 3 years (through 2028) |
| ETL pipelines | Thousands (DataStage) |
| Migration tracks | Multiple (Finance, Digital/e-comm, others) |

---

## 7. Technology Stack Referenced

**Legacy/Source:**
- SQL Server (EDW)
- Cognos (reporting)
- SSAS Cubes (SQL Server Analysis Services — analytical/pivot layer)
- DataStage (ETL)
- Excel (cube-based interfaces)

**Target/Destination:**
- Databricks (data platform)
- Tableau (reporting)
- ThoughtSpot (reporting, referred to as "Hotspot" in multiple emails)

**AI Tooling Referenced:**
- CluedIn (data management/quality)
- Lakehouse AI tools (Databricks-native)

---

## 8. Analytical Notes

### Evolution of BayOne's Understanding

The thread shows a clear evolution in BayOne's understanding of the opportunity:
- **December 11 (Zahra):** High-level awareness of a reporting modernization program. Framed primarily as a reporting migration with AI acceleration potential.
- **December 14 (Colin):** Structured discovery questions that already anticipate the complexity beyond reporting (ETL, data models, semantic layer, RBAC). Colin immediately recognized this is bigger than a report migration.
- **January 28 (Neha):** Detailed 10-section requirements dump that confirms Colin's instincts and reveals the full technical scope (SSAS cubes, embedded SQL, ETL re-engineering, data mapping bottlenecks).
- **January 30 (Colin):** Strategic analysis that reframes the technical problems as organizational and strategic issues. Identifies the real risks and opportunities.
- **February 4 (Neha):** Confirmation of two tracks and commitment to gather the strategic information Colin requested.

### Gap Between What Sephora Says and What Colin Hears

A recurring pattern in this thread is Colin reading between the lines of what Sephora is communicating:

| What Sephora says | What Colin identifies |
|---|---|
| "We need a connector for SSAS cubes" | Change management problem, not a technical one |
| "3-year transformation program" | A goal, not a plan — no evidence of strategic planning |
| "We chose Databricks" | Unclear rationale; possibly half-baked strategy |
| "We want staffing + AI solutions" | Two fundamentally different engagements being conflated |
| "We want to keep the same interface/experience" | Trying to make everyone happy; avoiding hard decisions |

### What Sephora Has vs. Has Not Done

**Completed:**
- Report rationalization/analysis (phase 1)
- Some data migration into Databricks
- Initial pipeline re-engineering in a few tracks
- AI mapping POCs (validated that AI helps but manual validation still required)

**Not done or unclear:**
- No clear architecture decision-maker identified
- No articulated rationale for Databricks selection
- No plan for the SSAS cube migration path
- No apparent mid-to-long range technology strategy
- No resolution of the change management challenge with business users

### Colin's Implied Opportunity Assessment

Though not stated explicitly as a single list, Colin's analysis implies several distinct opportunities for BayOne:
1. **Staffing placement** — Senior data architect/lead for the migration program
2. **SSAS cube migration strategy** — Solving the semantic layer modernization, which is really a change management + architecture engagement
3. **AI-assisted ETL analysis tooling** — Automated SQL logic extraction, dependency discovery, complexity scoring
4. **Data mapping acceleration** — Reducing the manual validation bottleneck
5. **Technology strategy advisory** — Helping Sephora articulate and enforce their Databricks strategy
6. **Organizational alignment** — Helping ensure decision-making authority exists to execute the modernization
