# Context Discovery

## Project Overview

BayOne Solutions is pursuing a strategic engagement with Sephora for their Enterprise Data Warehouse (EDW) modernization program. This is a 3-year, multi-track initiative to re-engineer (not migrate) ~6,000+ legacy reports, 8 SSAS cubes, 800+ KPIs from SQL Server/IBM Cognos/DataStage to Databricks.

BayOne's positioning: AI-powered acceleration of the EDW modernization through agent swarms, pattern detection, automated code transformation, and semantic layer formation.

## Key People

### Sephora
| Person | Role | Notes |
|--------|------|-------|
| **Mani Soundararajan** | VP, Marketing Tech, Personalization, Data/AI, Enterprise Reporting | Key decision-maker, wants proposal-led conversations |
| **Andrew Ho** | Sr. Director, Influencer/Media/Marketing AI, Enterprise Reporting | Reports to Mani, owns semantic layer strategy |
| **Grishi Chakraborty** | Director, Data Engineering / BI & Analytics | Reports to Andrew, ground truth on technical execution |
| **Mahair** | Enterprise Architect (under Grishi) | Technical architecture lead for migration |
| **Ram** | Director, Acquisition & Retention | Under Mani, actively hiring |
| **Rizwan Khan** | Director, CRM & Personalization | Under Mani, Q1 2026 hiring |

### BayOne
| Person | Role | Notes |
|--------|------|-------|
| **Colin Moore** | Director of AI | Technical lead, prior CTO at Coherent with similar migration experience |
| **Zahra Syed** | Director, Strategic Accounts | Sales lead, primary relationship manager |
| **Neha Malhotra** | Head of Recruiting, Enterprise | Handles candidate submissions |

## Meeting Progression

1. **Meeting 1 (Mani + Zahra/Neha):** Initial discovery, Mani shared roadmap and pain points
2. **Meeting 2 (Mani + Colin/Zahra/Neha):** Colin presented AI acceleration ideas, Mani requested 3-tier proposal
3. **Meeting 3 (Andrew/Grishi + Colin/Zahra/Neha):** THIS MEETING - Technical deep dive with execution team

## Relevant Systems/Tools

### Current State (Legacy)
- IBM Cognos (reporting) - very old version (10.2/10.3)
- SQL Server (EDW)
- SSAS Cubes (8 cubes, Excel pivot table interface)
- IBM DataStage (ETL) - not latest version
- All on-prem

### Target State
- Databricks (lakehouse)
- Tableau / ThoughtSpot (BI)
- Databricks pipelines (ETL)
- Common semantic layer

### AI Tools Already in Use/Evaluation
- Claude (30% efficiency gain on SQL transformation)
- Lutra, Flow (AI-assisted automation)
- Databricks accelerators
- Azure AI Foundry mentioned

## Key Pain Points Identified (Prior Meetings)

1. **SSAS to Databricks connector** - No native connector, business loves Excel pivot tables
2. **Manual agent workflow** - Using Claude but process is: open report → extract SQL → run AI → validate → deploy
3. **Scale** - 6,000+ reports, can't do report-by-report
4. **SME bandwidth** - Same people running production AND validating modernization

## What BayOne Has Presented

- EDW Acceleration Framework (8 AI capabilities)
- Discovery Discussion Guide
- Colin's experience with similar Snowflake migration at Coherent
