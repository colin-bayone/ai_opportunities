# Context Discovery

## Project Overview

This is a consulting engagement between BayOne Solutions and Sephora regarding their Enterprise Data Warehouse (EDW) modernization program. Sephora is executing a three-year re-engineering initiative to transition from SQL Server, IBM Cognos, and IBM DataStage to Databricks.

**Key project characteristics:**
- Re-engineering (not lift-and-shift migration)
- 6,000+ Cognos reports, 8 SSAS cubes, 800+ KPIs
- Finance track underway, Merchandising and Supply Chain to follow
- Goal: Agent-assisted acceleration to compress timeline

## Key People

### BayOne Solutions
| Name | Role |
|------|------|
| Colin Moore | Director of AI, Technical Lead |
| Neha Malhotra | VP of Growth and Customer Success |
| Zahra Syed | Sales |
| Rahul Bobbili | President |
| Amit | Delivery |

### Sephora
| Name | Role |
|------|------|
| Vlad | CIO (Mani's boss) |
| Mani Soundararajan | VP, Data & Analytics (Decision Maker) |
| Andrew Ho | Sr. Director, Data & Analytics (Vision Owner) |
| Gariashi Chakrabarty | Director, Data Engineering / BI & Analytics (Technical Gatekeeper) |
| Maher Burhan | Enterprise Architect (Consultant) |
| Sergey Shtypuliak | SME - IBM Tools (Cognos, DataStage), Consultant |
| Itisha Singh | Data & Analytics |

### Organizational Hierarchy
```
Vlad (CIO)
  └── Mani Soundararajan (VP)
        ├── Andrew Ho (Sr. Director)
        └── Gariashi Chakrabarty (Director)
              └── Sergey Shtypuliak (SME - Consultant)
        └── Maher Burhan (Enterprise Architect - Consultant)
```

## Relevant Systems/Tools

| System | Context |
|--------|---------|
| IBM Cognos (10.2/10.3) | Legacy reporting tool, on-premises |
| IBM DataStage | Legacy ETL/pipeline tool, on-premises |
| SQL Server | EDW database, on-premises |
| Databricks | Target platform, already mature for non-EDW workloads |
| ThoughtSpot | BI tool for aggregated data exposure |
| SSAS (SQL Server Analysis Services) | 8 cubes feeding Excel pivot tables |
| Framework Manager Model | Cognos metadata layer for SQL generation |
| MCP (Model Context Protocol) | Agent connector architecture |
| Claude | AI tool currently used manually for SQL transformation |

## Meeting Context

This is Meeting 4 in the Sephora engagement series:
1. **Meeting 1** (Mani - Strategic): Initial discovery, 3-year roadmap shared
2. **Meeting 2** (Mani + Colin - Proposal): Credibility established, three-tier proposal requested
3. **Meeting 3** (Andrew/Gariashi - Technical): Pain points identified, agent swarm vision discussed
4. **Meeting 4** (Technical Deep Dive): This meeting - scoping demo/POC with architects

## Previous Deliverables

- `03_edw_acceleration_framework.html` - Previous technical framework document
- `04_technical_deep_dive_framework.html` - Screen-share document prepared for this meeting
- Meeting 3 analysis documents in `meetings/03_andrew_grishi_meeting1/`
