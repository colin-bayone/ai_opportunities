# Tools & Vendors - Technology Landscape

## Current Technology Stack (Legacy)

### Data Layer
| Component | Technology | Age | Notes |
|-----------|------------|-----|-------|
| Database | SQL Server | 15-20 years | On-premise, mature |
| Data Warehouse | Enterprise Data Warehouse (EDW) | 15-20 years | Central repository |
| ETL | IBM DataStage | Legacy | Pipeline orchestration |

### Reporting Layer
| Component | Technology | Age | Notes |
|-----------|------------|-----|-------|
| Primary BI | IBM Cognos | 15-20 years | Thousands of reports |
| OLAP | SSAS Cubes | Legacy | 8 cubes identified |
| User Interface | Excel + Cube connections | Ongoing | Business user tool |

### Key Quote on Legacy
> "Cognos, there are actually like 15, 20 years back, something might have been implemented. So the queries are actually like very deep inside the code."
> — Mani, Meeting 1

---

## Target Technology Stack (Modern)

### Data Platform
| Component | Technology | Status | Notes |
|-----------|------------|--------|-------|
| **Primary Platform** | Databricks | Target | Lakehouse architecture |
| **Cloud** | Microsoft Azure | Infrastructure | Microsoft at governance table |

### Reporting Layer (Future)
| Component | Technology | Status | Priority |
|-----------|------------|--------|----------|
| ThoughtSpot | Under consideration | Future | Low - not pursuing now |
| Tableau | Under consideration | Future | Low - not pursuing now |
| Cognos | Retained | Current strategy | High - minimize disruption |

### Key Quote on Target
> "There is a desire to move to ThoughtSpot or Tableau, but that's not something that we are pursuing right now."
> — Mani, Meeting 2

---

## Vendor Relationships

### Databricks
| Aspect | Detail | Source |
|--------|--------|--------|
| **Role** | Primary platform partner | Mani, Meeting 2 |
| **Governance** | "Has seat at the table" | Mani, Meeting 2 |
| **Accelerators** | Providing migration accelerators | Mani, Meeting 2 |
| **AI Tools** | Offering AI-oriented tools | Mani, Meeting 1 |
| **Competition** | "Already asked Databricks for recommendations" | Mani, Meeting 1 |

**Implication:** Databricks is incumbent with strong position. BayOne must complement, not compete.

### Microsoft
| Aspect | Detail | Source |
|--------|--------|--------|
| **Role** | Cloud platform provider | Mani, Meeting 2 |
| **Governance** | "Has seat at the table" | Mani, Meeting 2 |
| **Integration** | Azure infrastructure | Implied |

### Databricks Partners
| Aspect | Detail | Source |
|--------|--------|--------|
| **Role** | Accelerator providers | Mani, Meeting 2 |
| **Tools** | Various specialized tools | Mani, Meeting 2 |
| **Status** | Being evaluated | Mani, Meeting 2 |

---

## AI/Automation Tools in Use

### Confirmed Tools
| Tool | Type | Status | Source |
|------|------|--------|--------|
| **Lutra** | AI/Automation | In use | Mani, Meeting 2 |
| **Flow** | AI/Automation | In use | Mani, Meeting 2 |
| **Databricks AI tools** | Platform-native | Evaluating | Mani, Meetings 1 & 2 |

### Unknown Details
- What specifically Lutra does for them
- What specifically Flow does for them
- Satisfaction level with these tools
- Gaps these tools don't address

### Questions for Grishi/Andrew
1. What's working well with Lutra?
2. What's working well with Flow?
3. What gaps do these tools leave?
4. What's Databricks proposing for AI specifically?

---

## Tool Evaluation Process

### How They Assess Tools
> "Each tool has its own strength. Now, the team is assessing... the last couple of months, which particular tool is good and for what, and the pattern has been established."
> — Mani, Meeting 2

### Tool Selection Criteria (Implied)
| Criterion | Evidence |
|-----------|----------|
| Fit for specific use case | "Someone for Cognos, someone for SQL Server" |
| Speed of results | Timeline pressure |
| Integration capability | Work with existing stack |
| Team adoption | Practical usability |

### Who Makes Tool Decisions
- Core governance table
- Databricks influence
- Grishi/team hands-on evaluation
- Mani strategic oversight

---

## Vendor/Tool Landscape Map

```
                    PLATFORM LAYER
    ┌─────────────────────────────────────────────┐
    │                 Databricks                   │
    │              (Primary Target)                │
    │                     │                        │
    │    ┌────────────────┼────────────────┐      │
    │    │                │                │      │
    │ Databricks    Databricks      Partner       │
    │ Native AI     Accelerators    Accelerators  │
    └─────────────────────────────────────────────┘
                          │
                    CLOUD LAYER
    ┌─────────────────────────────────────────────┐
    │              Microsoft Azure                 │
    └─────────────────────────────────────────────┘
                          │
                  AUTOMATION LAYER
    ┌─────────────────────────────────────────────┐
    │     Lutra         │         Flow            │
    │   (In Use)        │       (In Use)          │
    └─────────────────────────────────────────────┘
                          │
                   LEGACY LAYER
    ┌─────────────────────────────────────────────┐
    │  SQL Server  │  Cognos  │  DataStage │ SSAS │
    │  (Source)    │ (Retained)│  (Migrate) │(TBD) │
    └─────────────────────────────────────────────┘
```

---

## BayOne Tool Positioning

### Where We Fit
| Layer | BayOne Role | Competition |
|-------|-------------|-------------|
| Platform | Work with Databricks (not replace) | Databricks-native tools |
| AI/Automation | Complement Lutra/Flow | Lutra, Flow, Databricks AI |
| Analysis | Code/pattern analysis tools | Partner accelerators |
| Methodology | Process and expertise | Internal team |

### Differentiation Strategy
| Aspect | BayOne Approach | Why Different |
|--------|-----------------|---------------|
| Tool-agnostic | Work with their tools | Not locked to platform |
| Experience-based | Know the pitfalls | Not just tool vendors |
| Hybrid AI | Deterministic + GenAI | More reliable than pure AI |
| Consulting | Methodology included | Not just tool license |

### Key Colin Quote
> "We can work with existing AI strategy (avoiding silos)"
> — Colin, Meeting 2

---

## Technology Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Databricks captures AI work | Medium | High | Position as complementary |
| Tool fragmentation | Medium | Medium | Offer unified methodology |
| Tool doesn't fit use case | Low | Medium | Flexible approach |
| Integration complexity | Medium | Medium | Experience with integrations |

---

## Questions for Technical Discovery

### About Current Tools
1. What's the full inventory of tools being used?
2. What's working well? What's frustrating?
3. Where are the gaps?
4. How do tools integrate (or not)?

### About Databricks Specifically
5. What AI capabilities is Databricks proposing?
6. What's covered by Databricks contract?
7. What's the relationship like?
8. Are they meeting expectations?

### About New Tools
9. What's the process for introducing new tools?
10. Who needs to approve?
11. What security/compliance requirements exist?
12. How long does procurement take?

---

## Tool Integration Opportunities

### For Proposal
- Show how BayOne tools/methods integrate with Lutra/Flow
- Demonstrate Databricks compatibility
- Emphasize methodology that works across tools
- Offer to work with whatever they have

### Value Proposition
> Not another tool to manage — a methodology that makes your existing tools more effective
