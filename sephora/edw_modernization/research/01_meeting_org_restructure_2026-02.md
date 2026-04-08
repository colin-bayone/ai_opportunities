# 01 - Meeting: Organizational Restructure and Operating Models

**Source:** /sephora/edw_modernization/source/mani_meeting1_2026-02_formatted.txt
**Source Date:** 2026-02 (Initial Discovery Call with Mani)
**Document Set:** 01 (Mani Meeting 1)
**Pass:** Focused deep dive on org restructure and team transition models

---

## What Is Happening: "Democratizing Reports"

Mani described a fundamental restructuring of how enterprise-wide reports and analytics are handled at Sephora. Today, one central team (Mani's team) handles all enterprise-wide reports. Starting in 2026, that is changing.

**The core idea:** Reports will become the responsibility of each domain engineering team rather than a central team. As Mani put it, domain teams "know their business, they know their project" and "report is just actually reporting what they have done. So it doesn't have to be done by another separate team" (lines 22-24).

**What "democratizing" means in practice:**
- **Data** has already begun to be democratized (decentralized to domain teams). This journey started before this meeting.
- **Reports** are now following the same path. As domain engineering teams (stores, e-commerce, supply chain) execute their own projects and use cases, reports will be built as part of those projects instead of being routed to Mani's central team.
- Previously, when a domain team completed a project, report requests would "come to Mani's team." That handoff is being eliminated.

**What Mani's team becomes:** A "lean core platform" team focused on:
- Establishing frameworks and governance ("what's the right tool to use?")
- Reviewing whether data is flowing correctly into reports
- Providing subject matter expertise when domain teams need it
- Setting standards rather than executing individual report builds

This is not an overnight change. Mani explicitly said "it won't happen immediately in 2026, but that's a journey that we are starting with" (line 25). The transition is being tested through "two, three forms of experiment" — the three operating models described below.

---

## The Three Operating Models

Mani described three distinct models being used simultaneously to transition reports responsibility from his central team to domain engineering teams. Each model represents a different level of autonomy for the receiving domain and a different role for Mani's people (particularly Grishi).

### Model 1: David / Stores (Most Autonomous)

**Domain:** Retail stores
**Hiring managers:** David and Natalia
**Grishi's role:** Subject matter expert and interview panelist — not the hiring manager
**Transition timeline:** Approximately one year to reach stability

**How it works:**
- David's team is already taking on stores-specific reports projects (line 27-28: "David's team is already taking reports, projects for... retail stores and all that").
- "Full delivery will be taken by them" — David's team owns the end-to-end delivery of stores reports.
- Mani's people (specifically Andrew Ho and Grishi) participate only "as subject matter experts" who "will get involved if they need and where they need" (line 29).
- For hiring, David and Natalia are the hiring managers. Grishi sits on the interview panel to ensure technical quality, but she does not own the headcount decisions.
- Mani's team provides the governance layer: framework definition, tool selection guidance, data quality reviews, and standards compliance.

**Key detail:** This model gives the domain team the most independence. David's team hires, delivers, and operates. Mani's team only advises and governs. This is the target end-state for all domains.

**Why stores goes first:** Stores is already on modern technology (line 60: "for stores and .com, we are already like in the modern technology"), which makes the transition feasible now.

### Model 2: Rajesh / E-commerce (Transitional)

**Domain:** E-commerce (starting with omnichannel order fulfillment — BOPIS/same-day delivery)
**Hiring manager:** Grishi (initially)
**Execution:** Engineers work on projects in Rajesh's domain
**Transition timeline:** Six months to evaluate, then full transition (target: June/July 2026)

**How it works:**
- Grishi is the hiring manager — she sources and hires the engineers (line 35-37: "the team of engineers will be reporting to Grishi... Grishi will still be working with you, for example, to source the team members, to hire the engineers").
- The hired engineers execute projects within Rajesh's organization. They are "in Rajesh's spots" and "responsible for the project delivery" (lines 38-39).
- This creates a split-reporting structure: engineers report to Grishi administratively but deliver work for Rajesh's e-commerce domain.
- The starting scope is omnichannel order fulfillment — specifically scenarios where orders are received online and transitioned to stores for same-day delivery or buy-online-pickup-in-store (BOPIS) (lines 33-34).

**The six-month evaluation gate:**
- Around June/July 2026, leadership will evaluate whether this model is working successfully.
- If it is, "these team members will be fully transitioned to Rajesh's org" (line 41) — meaning Grishi would no longer be the hiring manager and the engineers would move entirely under Rajesh.
- At that point, this model would converge with Model 1 (full domain ownership).

**Why the intermediate step:** Unlike stores, Rajesh's e-commerce domain is not yet set up to hire and manage reports engineers independently. Grishi acts as a bridge — she provides hiring expertise and technical vetting while the domain builds capacity. The six-month trial de-risks the transition.

### Model 3: Kalyan / Supply Chain (Status Quo)

**Domain:** Supply chain, merchandising
**Hiring manager:** Grishi
**Delivery owner:** Grishi
**Transition timeline:** After Models 1 and 2 are proven successful

**How it works:**
- This is a continuation of how things have been done "this year and the last year" (line 51).
- Both delivery and hiring remain under Grishi's responsibility (line 55: "both the delivery and hiring and engineers will be in Grishi's responsibility").
- There is no split reporting and no domain team taking ownership yet.

**Why supply chain is last:** Mani was explicit — "in Kalyan's area, like, for supply chain merchandising, we still have legacy technologies" (line 59). The legacy stack (IBM Cognos, SQL Server — referenced elsewhere in the conversation) makes it impractical to democratize reports until the underlying platform is modernized.

**Sequencing logic:** "Once the first two models are kind of like good and successful, then we will start doing the same thing for Kalyan's area also" (line 57). Supply chain will not begin transitioning until both stores (Model 1) and e-commerce (Model 2) have been validated.

---

## Model Comparison Matrix

| Dimension | Model 1 (Stores) | Model 2 (E-commerce) | Model 3 (Supply Chain) |
|---|---|---|---|
| **Domain owner** | David | Rajesh | Kalyan |
| **Who hires** | David & Natalia | Grishi (initially) | Grishi |
| **Who delivers** | David's team | Engineers in Rajesh's org | Grishi's team |
| **Grishi's role** | SME, interview panelist | Hiring manager (temporary) | Hiring manager + delivery owner |
| **Mani's team role** | Governance, framework, on-call SME | Governance + hiring bridge | Full ownership (current state) |
| **Technology readiness** | Modern stack | Modern stack | Legacy (Cognos, SQL Server) |
| **Timeline to full transition** | ~1 year (stability by early 2027) | ~6 months evaluation, then transition (mid-2026) | After Models 1 & 2 succeed |
| **Autonomy level** | High | Medium (growing) | Low (unchanged) |

---

## Transition Sequencing and Rationale

The three models are not random experiments. They represent a deliberate sequencing strategy:

1. **Technology readiness determines eligibility.** Stores and e-commerce are on modern technology stacks. Supply chain is still on legacy (Cognos, SQL Server). You cannot democratize reports that run on technology the receiving domain team has never worked with. The EDW Modernization project (3-year, starting 2026) will eventually bring supply chain onto modern platforms, at which point Model 3 can begin transitioning.

2. **Each model is a progressively lower-risk experiment.** Model 1 (stores) gives the most autonomy because David's team is already closest to self-sufficiency. Model 2 (e-commerce) uses Grishi as a bridge because Rajesh's team needs more ramp-up time. Model 3 (supply chain) stays unchanged because it is not ready on any dimension.

3. **Learnings flow forward.** Mani explicitly said the team will "take those learnings" from the first six months of Model 2 before deciding on full transition (line 41). The same pattern applies to Model 3 — it will not start until Models 1 and 2 are validated.

4. **The end state is the same for all three.** Every domain eventually owns its own reports delivery and hiring, with Mani's team providing only governance, frameworks, and on-demand SME support. The three models differ only in how quickly each domain reaches that end state.

---

## What Mani's Team Retains

Regardless of which model applies, Mani's central team keeps a set of platform-level responsibilities:

- **Framework definition:** "My team is establishing like a framework and governance" (line 29) — what tools should be used, what standards reports must meet.
- **Tool selection governance:** "What's the right tool to use?" (line 29) — Mani's team decides whether a given report should use Tableau, ThoughtSpot, Cognos, or Databricks native tooling.
- **Data quality reviews:** Reviewing "if they've implemented like... data is coming in correctly or not" (line 30) — validation that reports built by domain teams are consuming data correctly.
- **Subject matter expertise:** Available on-call when domain teams need help ("they will get involved if they need and where they need" — line 29).
- **Standards and governance:** The "kinds of reviews and support" role (line 31) — ensuring consistency across domains even as execution is distributed.

This is the "lean core platform team" Mani described — a center of excellence that sets standards and provides expert support rather than executing every report.

---

## Implications for BayOne

### Direct Hiring Implications

The restructure creates multiple parallel hiring streams, each with different engagement models:

- **For stores (Model 1):** David and Natalia are the hiring managers. BayOne's sourcing conversations should go through them, with Grishi participating in technical interviews. The talent needs here are for reports/analytics engineers who can work on the modern stack.
- **For e-commerce (Model 2):** Grishi is currently the hiring manager. BayOne already has a relationship with Grishi (she had candidates in pipeline that were put on hold). As this model matures and engineers transition to Rajesh's org, the hiring manager relationship may shift.
- **For supply chain (Model 3):** Grishi remains the single point of contact for both hiring and delivery. This is the existing model BayOne already operates in.

### Strategic Observations

1. **Multiplied points of contact.** The democratization creates more hiring managers to engage with. Instead of one central team making all reports hiring decisions, there will eventually be hiring managers in each domain. BayOne needs to build relationships with David, Natalia, and eventually Rajesh's team in addition to Grishi.

2. **Grishi's role is pivotal but changing.** Today, Grishi is central to almost all reports hiring. As Model 1 matures and Model 2 transitions, her direct hiring authority shrinks. However, her SME/governance role means she retains influence over technical standards and interview quality across all domains. Maintaining the relationship with Grishi remains important regardless of her formal title.

3. **EDW Modernization is the enabler.** The three-year EDW Modernization project (moving from Cognos/SQL Server to Databricks/Tableau/ThoughtSpot) is what will eventually make Model 3 possible. It is also the largest project on Mani's 2026 roadmap. BayOne's engagement with EDW Modernization directly accelerates the overall restructure timeline.

4. **The governance layer is a potential AI opportunity.** Mani's retained responsibilities — framework definition, tool selection, data quality reviews — are exactly the kinds of functions where AI tooling could add value. Automated data quality checks, standardized report templates, or AI-assisted governance reviews align directly with what the lean platform team needs to scale across multiple domains without growing headcount.

5. **Timeline awareness matters for staffing.** The six-month evaluation gate for Model 2 (June/July 2026) and the one-year stability target for Model 1 (early 2027) are inflection points. If these transitions succeed, there will be a surge of hiring within domain teams as they take over full ownership. BayOne should be positioned to fill those roles when the gates are passed.

---

## Key Quotes (Cleaned from Speech-to-Text)

> "Enterprise-wide reports is currently handled by one central team, which is my team at this time, but starting 2026 we're kind of democratizing that." (line 16)

> "My team will become a lean team, which is like a core reports platform kind of a team." (line 17)

> "They know their business, they know their project... report is just actually reporting what they have done. So it doesn't have to be done by another separate team." (lines 22-24)

> "In Kalyan's area, for supply chain merchandising, we still have legacy technologies. Whereas for stores and .com, we are already in the modern technology." (lines 59-60)

> "Once the first two models are kind of good and successful, then we will start doing the same thing for Kalyan's area also." (line 57)

> "My team is establishing a framework and governance... what's the right tool to use? ...Those kinds of reviews and support is what we'll be doing." (lines 29-31)
