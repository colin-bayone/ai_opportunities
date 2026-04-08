# Sephora EDW Modernization - Org Chart

**Last Updated:** 2026-04-02 (after processing Sets 01-07)

---

## Sephora (Client)

### Mani
- **Title:** VP, Marketing & Enterprise Analytics
- **Reports to:** Unknown (executive level)
- **Direct reports:** Andrew Ho, Ram, Rizwan
- **Engagement role:** Executive sponsor. Set the ground rules ("come with a proposal, not blank-slate discovery"). Has final approval on vendor selection.
- **Key intel:** Visited in person by Colin at Sephora HQ (March 2026). Told BayOne that Sephora must select a vendor by end of April 2026. Has told all other vendors no.
- **Key asks:** Three engagement options, show BayOne's investment/skin in the game, flexibility in staffing models.
- **Sentiment:** Warm, supportive, wants BayOne to succeed. Validated Colin's approach ("Your approach, all looks good").
- **First appeared:** Set 01

### Andrew Ho
- **Title:** Director, Enterprise Reporting (reports to Mani)
- **Direct reports:** Grishi
- **Engagement role:** Strategic decision-maker between Mani and the technical team. Articulated the multi-agent orchestration vision independently. Transparent about talking to other vendors (Set 03). Manages the meeting flow.
- **Key concern:** "I just want to make sure the wild thinking is not wild, it's real, it can be done."
- **Sentiment:** Direct, strategic, transparent. Impressed by Colin's technical depth but wants proof.
- **First appeared:** Set 03

### Grishi (Gariashi Chakrabarty)
- **Title:** Director, Data Engineering, BI and Analytics (reports to Andrew Ho)
- **Engagement role:** Execution owner for the EDW modernization. Her team is doing the manual migration work today. Already using Claude for SQL conversion (~30% efficiency gain). Has an enterprise architect (Malika) reporting to her.
- **Key concern:** "I just want to see that you guys have done something like this, that you've created agents capable of doing these kind of things."
- **Sentiment:** Technical, detail-oriented, hands-on. Skeptical until she sees it working.
- **First appeared:** Set 03

### Malika Seth
- **Email:** Malika.Seth@sephora.com
- **Title:** Enterprise Architect (reports to Grishi)
- **Engagement role:** Primary technical contact via email. Proposed the disconnected demo approach (share XML + schema, skip security). Selected Track B. Clarified output format (both Spark SQL AND YAML). Provided Databricks source table schemas.
- **Sentiment:** Professional, precise, solution-oriented. Her emails are well-structured with clear asks.
- **First appeared:** Set 04 (on call), Set 04a (email)

### Sergey Shtypuliak
- **Email:** Sergey.Shtypuliak@sephora.com
- **Title:** Consultant / Senior Developer, IBM Tools SME (10-15 years)
- **Engagement role:** The most consequential technical voice. Explained the AggregationApplication framework: no Scala code, just YAML configs (3 per job: pipeline YAML, deployment YAML, create.HQL). Thousands of jobs in production. Critiqued Claude's "spaghetti code" notebooks. His guidance directly shaped the demo output format.
- **Key quote:** "No need to create new framework. No need to write Scala code. Just create config files."
- **Sentiment:** Pragmatic, experienced, slightly skeptical. "It's easy said than done."
- **First appeared:** Set 04

### Vishal Sharma
- **Title:** Consultant (likely Databricks/data engineering specialist)
- **Engagement history:** First appeared at the demo meeting (Set 07). Not present in any prior meetings or email threads.
- **Key concerns:** Platform portability ("we want to run this fully in our environment without your system"), ADF as alternative orchestration, XML parsing comprehensiveness for all DataStage components, data reconciliation
- **Tone:** Cautious, practical. Focused on self-sufficiency and avoiding vendor lock-in.
- **Note:** Need to determine his exact role and employer. May be another embedded consultant like Maher.
- **First appeared:** Set 07

### Maher Burhan
- **Email:** Maher.Burhan@sephora.com
- **Employer:** Xebia (Senior Architect), embedded at Sephora since May 2025
- **Sephora role:** Enterprise Architect for Sephora Data Platform
- **Background:** 8 years at IBM, deep Cognos and data warehouse expertise, Java/.NET, Databricks Unity Catalog (from GlobalLogic), 12+ years enterprise integration at CBSA
- **Engagement history:** Present on Set 04 call (suggested disconnected demo approach), CC on Set 04a emails, added to demo call by Andrew/Grishi
- **Demo role:** Trusted technical assessor. Will evaluate BayOne's approach with expert-level understanding. His employer (Xebia) has a directly competing "Agentic Data Pipeline Migrator" product, though Maher is embedded as a consultant, not pitching.
- **Note:** This is "Meher" / "my hair" from the transcripts. Separate person from Malika.
- **First appeared:** Set 04. Profile researched in Set 06a.

### Ram
- **Title:** Reports to Mani directly
- **Owns:** Top funnel (acquisition, retention, digital ads, TV, social media, post-purchase)
- **Status:** Actively hiring. Was traveling to India.
- **Relevance:** Potential future BayOne staffing opportunity, not directly involved in EDW.
- **First appeared:** Set 01

### Rizwan
- **Title:** Reports to Mani directly, based in Chicago
- **Owns:** CRM, personalization, marketing orchestration
- **Status:** Ramping down, may open positions late Q1 2026.
- **Relevance:** Potential future staffing, not directly involved in EDW.
- **First appeared:** Set 01

### David
- **Title:** Peer to Mani, owns Stores
- **Relevance:** Taking over stores-specific reports. Model 1 in the org restructure.
- **First appeared:** Set 01

### Rajesh
- **Title:** Owns e-commerce
- **Relevance:** Model 2 in the org restructure. Dinesh (digital personalization) reports to him.
- **First appeared:** Set 01

### Kalyan
- **Title:** Owns supply chain, merchandising
- **Relevance:** Still on legacy technologies. Last to transition. Potential future target for BayOne pilot.
- **First appeared:** Set 01

---

## BayOne (Our Team)

### Colin Moore
- **Title:** Director of AI
- **Engagement role:** Engagement lead, solution architect, demo presenter, client relationship owner
- **Key actions:** Led all 4 client meetings, presented AI-assisted EDW approach, did Cognos SDK homework, positioned the three-tier engagement model, visited Sephora HQ in person, giving the demo today (April 2, 2026 at 6:00 PM ET)
- **Prior experience:** Same type of EDW modernization at Coherent Corp (40K employees, $1.6B revenue, SSAS/SSRS to Snowflake)

### Saurav Kumar Mishra
- **Title:** Engineer / Developer
- **Engagement role:** Built the entire demo: LangGraph pipeline, Django dashboard, all agent architecture (orchestrator, gates, parsers, mappers, generators, validation, auto-fix, knowledge base). Ran 40-50+ test iterations.
- **Availability:** May join demo at 3:30 AM his time. Not guaranteed. Colin recording either way.

### Zahra Syed
- **Title:** Director, Strategic Accounts
- **Engagement role:** Account management, relationship owner, coordinated all meetings. Wrote the internal stakeholder mapping strategy that set up successful meetings. Present on all calls.

### Neha Malhotra
- **Title:** VP of Growth and Customer Success / Head of Recruiting
- **Engagement role:** Early discovery (gathered initial requirements from Grishi), coordinated introductions, present on client calls, weekly in-person presence at Sephora.
- **Key contribution:** The 10-section requirements document (Set 04a) that started the engagement.

---

## Vendor Landscape

- **All other vendors dismissed** as of March 2026 (learned in person at Sephora HQ)
- **Budget lock-in deadline:** End of April 2026
- **BayOne is the sole remaining candidate**
- Previously mentioned: Palantir as the expensive commercial ceiling (Colin, Set 03), Databricks as a trusted partner already at the table
- Andrew was transparent about multiple vendor conversations in Set 03; by Set 05 all were eliminated

---

## Engagement Decision Chain

```
Mani (approves vendor, budget)
  └── Andrew Ho (strategic decision on approach)
        └── Grishi (execution decision, team impact)
              ├── Malika (architecture, materials, technical contact)
              └── Sergey (framework requirements, output format)
```
