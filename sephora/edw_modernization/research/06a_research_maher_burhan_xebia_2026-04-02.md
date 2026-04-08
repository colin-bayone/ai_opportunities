# 06a - Research: Maher Burhan and Xebia Assessment

**Source:** LinkedIn profile, web research, engagement email thread (Set 04a)
**Date:** 2026-04-02
**Document Set:** 06a (Supplementary to Set 06, pre-demo intelligence)
**Context:** Maher Burhan was added to the demo call by Andrew and Grishi. This document assesses who he is, what Xebia does, and what this means for the demo.

---

## Who Is Maher Burhan

- **Current role:** Senior Architect at Xebia, embedded at Sephora as "Enterprise Architect for Sephora Data Platform"
- **Start at Xebia:** May 2025 (approximately 1 year)
- **Location:** Ontario, Canada (remote)
- **Prior to Xebia:** GlobalLogic (Senior Solution/Technology Architect, 11 months), with Databricks Unity Catalog and SAP S/4HANA integration experience
- **Deep background:** 8 years at IBM (Software Engineer Service Consultant), CBSA for 12+ years (enterprise integration), Innovapost (Technical Solutions Architect)
- **Key specialties:** Java, J2EE, .NET, DB2, Oracle, SQL Server, Teradata, Netezza, **IBM Cognos**, data modeling, data warehouse design

**This is the same person as "Meher" / "my hair" from the Set 04 transcript and "Maher.Burhan@sephora.com" on the email CC lines.** He has been involved since the technical deep dive. He is not new to the engagement.

### What He Knows About BayOne

- He was on the Set 04 technical deep dive call where Colin presented the agent architecture, MCP approach, and mapping methodology
- He was on the email CC for all of Set 04a (Malika's scope shift, Colin's Track A/B response, Malika's Track B selection)
- He suggested the disconnected approach in Set 04 (share XML, skip security) that made the demo feasible
- He has Cognos expertise and can assess BayOne's MCP claims with authority
- He has Databricks experience (Unity Catalog from GlobalLogic) and can assess output quality

---

## Who Is Xebia

**Company:** Global AI-first consulting, software engineering, and training company
**Size:** 1,001-5,000 employees, 6,199 LinkedIn members
**HQ:** Atlanta, Georgia
**Delivery model:** Client-facing teams in US/Europe, nearshore in Poland/Latin America, offshore hub in India

### Xebia's Databricks Relationship

- **Databricks Elite Consulting Partner** (highest tier)
- **Databricks Gold Partner** (achieved March 2026)
- 60+ certified data experts, Databricks Solution Architect Champions
- End-to-end Databricks services: advisory, data engineering, migrations, Lakehouse optimization, training

### Xebia's Sephora Relationship

- Maher Burhan is embedded as Enterprise Architect for Sephora Data Platform
- Manbir Paul (VP of Engineering, Data Insights and Marketing at Sephora) participated as a guest panelist at a Xebia fireside chat at Gartner
- Xebia appears to have an established consulting presence at Sephora beyond just Maher

---

## THE CRITICAL FINDING: Xebia Has a Directly Competing Product

### Xebia Agentic Data Pipeline Migrator

Xebia has built a product called the **Agentic Data Pipeline Migrator** that does almost exactly what BayOne's demo does:

- **Multi-agent architecture** with specialized agents for orchestration, analysis, translation, validation, generation, and visualization
- **Automatically converts entire SQL and ETL codebases** from legacy systems into Databricks-ready workflows
- **Supports 7 SQL platforms:** Redshift, Databricks, Snowflake, BigQuery, Postgres, MySQL, and SQL Server
- **Translates SQL dialects, resolves macros, validates schemas, assembles projects**
- **Graceful error handling:** skips non-translatable code with comments rather than halting
- **Produces auditable reports** preserving logic, lineage, and performance
- **Claims to complete in hours what once required weeks**

This is listed on Xebia's website as a product/solution, featured on the Databricks blog as a GenAI Partner Accelerator, and promoted on LinkedIn.

### How It Compares to BayOne's Demo

| Aspect | BayOne Demo | Xebia Agentic Migrator |
|--------|-------------|----------------------|
| Architecture | Multi-agent with LangGraph, custom gates | Multi-agent (details unknown) |
| Target | Databricks (Spark SQL + YAML configs) | Databricks (and 6 other platforms) |
| Source support | DataStage XML, SQL Server (Sephora-specific) | 7 SQL platforms (generic) |
| Output format | Sephora's AggregationApplication framework (YAML) | Databricks-ready workflows (generic) |
| Customization | Built specifically for Sephora's data and framework | Product/accelerator (likely needs customization) |
| Validation | Deterministic gates + LLM checks + human-in-the-loop | Auditable reports, graceful error handling |
| Cognos support | MCP connector architecture (designed but not demoed) | Not mentioned |
| Knowledge base | Learns from approved patterns | Not mentioned |
| Maturity | PoC built in 2 weeks | Appears to be a shipping product |

---

## What This Means for the Demo

### Most Likely Scenario

Maher is on the call as **Sephora's trusted technical assessor**. Andrew and Grishi do not have deep AI/agent architecture expertise. Maher does, both from his own background and from working at a company that builds exactly this type of tool. He is there to:

1. Assess whether BayOne's approach is technically sound
2. Compare it (mentally or explicitly) against what Xebia could offer
3. Ask pointed technical questions that Andrew and Grishi would not know to ask
4. Advise Andrew and Grishi on whether to proceed

### He Is NOT Likely a Competitive Threat (But Be Aware)

- All other vendors were dismissed (Set 05). If Xebia were competing, they would have been in the running already.
- Maher is embedded as a consultant at Sephora, not pitching Xebia's services. His role is "Enterprise Architect for Sephora Data Platform," not "sales."
- He was collaborative in Set 04, not adversarial. He helped make the demo feasible with the disconnected approach.
- However, he works for a company with a directly competing product. He knows what good looks like in this space. The bar is higher with him in the room.

### What He Will Likely Probe

Based on his background and Xebia's product:

1. **Scalability:** "You showed one pipeline. How does this work across hundreds of different pipeline types?" (Xebia's product handles 7 SQL platforms generically)
2. **Error handling at scale:** "What happens when the agent encounters something it cannot translate?" (Xebia's product skips and marks with comments)
3. **Auditability and lineage:** "Can you trace every transformation back to its source?" (Xebia emphasizes "fully auditable reports preserving logic, lineage, and performance")
4. **Cognos specifics:** He has deep Cognos expertise. If MCP comes up, he can assess the claim technically.
5. **Framework fit:** He knows Sephora's data platform architecture. He will assess whether the output truly fits.
6. **Build vs buy:** Whether Sephora should use BayOne's custom approach or a product like Xebia's own migrator (though he may not raise this explicitly given his consultant role)

---

## How to Handle This in the Demo

### Do

- **Acknowledge him warmly.** He has been part of this from Set 04. He is not a stranger. "Good to see you again, Maher."
- **Lean into what differentiates BayOne from a generic product.** The output is built specifically for Sephora's AggregationApplication framework (YAML configs, not generic Databricks code). A generic migrator would produce notebooks or raw SQL that does not fit their existing support model. Sergey was explicit about this.
- **Emphasize the knowledge base learning.** Generic products do not learn from Sephora's specific patterns and approved decisions. BayOne's pipeline does.
- **Emphasize human-in-the-loop with surgical auto-fix.** This is not a black-box "run and pray" migration. The review step, the confidence scoring, and the auto-fix are about transparency and control.
- **Be technically precise.** Maher will notice handwaving. Use specific terms: deterministic gates, sqlglot for AST parsing, source grounding checks, dependency graph for stage generation.

### Do Not

- **Do not mention Xebia or their product.** Do not acknowledge the competitive overlap. Let Maher draw his own conclusions.
- **Do not position this as a "product."** This is a custom solution. That is the differentiation. A product approach is what Xebia sells.
- **Do not oversimplify the technical architecture.** Maher will see through it. Be ready to go deep if he asks.
- **Do not be defensive if he asks hard questions.** He is doing his job. Treat his questions as validation opportunities.

---

## Updated Org Chart Entry

### Maher Burhan
- **Email:** Maher.Burhan@sephora.com
- **Employer:** Xebia (Senior Architect), embedded at Sephora
- **Sephora role:** Enterprise Architect for Sephora Data Platform
- **Background:** 8 years IBM, deep Cognos expertise, Java/.NET, Databricks Unity Catalog experience
- **Engagement history:** Present on Set 04 call, CC on Set 04a emails, suggested the disconnected demo approach
- **Employer context:** Xebia is a Databricks Elite Partner with a directly competing "Agentic Data Pipeline Migrator" product
- **Demo role:** Trusted technical assessor for Andrew and Grishi. Will evaluate BayOne's approach with expert-level understanding of the space.

---

## Sources

- [Xebia Agentic Data Pipeline Migrator](https://xebia.com/solutions/agentic-data-pipeline-migrator/)
- [Xebia Databricks Elite Partner](https://xebia.com/partners/databricks/)
- [Xebia Databricks Gold Partner Status](https://xebia.com/news/xebia-achieves-databricks-gold-partner-status/)
- [Databricks GenAI Partner Accelerators (includes Xebia)](https://www.databricks.com/blog/introducing-databricks-genai-partner-accelerators-data-engineering-migration)
- [Xebia Modernize E-commerce Data Pipeline blog](https://xebia.com/blog/modernizing-a-global-e-commerce-data-pipeline-with-ai-a-faster-path-to-databricks/)
- [Xebia About](https://xebia.com/about-us/)
