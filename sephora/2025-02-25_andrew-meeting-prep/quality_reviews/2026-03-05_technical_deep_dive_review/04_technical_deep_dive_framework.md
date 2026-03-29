# EDW Modernization
## Technical Deep Dive: Agent-Assisted Acceleration
### March 2026

---

## Our Understanding

Sephora is executing a three-year EDW re-engineering program, transitioning from SQL Server, IBM Cognos, and IBM DataStage to Databricks. The emphasis is on **re-engineering** rather than migration - this is not a lift-and-shift but a complete rebuild of data pipelines and reporting assets for a modern architecture.

The Finance track is underway and making progress, with work continuing through the end of this year. The patterns established in Finance will inform the approach for Merchandising, Supply Chain, and subsequent domains.

### Scale

| Asset | Volume |
|-------|--------|
| Cognos Reports | 6,000+ |
| SSAS Cubes | 8 |
| KPIs | 800+ |
| Dimensions | 300 |
| Source Systems | 20+ |

### Legacy Environment

The current systems include older but stable versions of Cognos (10.2/10.3 era) and DataStage, running on-premises. This is advantageous from an integration perspective - mature, well-documented systems with multiple established integration paths.

**Cognos integration options:**
- IBM Cognos SDK (Java/.NET) providing full access to the BI Bus API and Content Manager
- Content Store database (SQL Server/Oracle) containing all report definitions and metadata
- Report specifications exportable as XML documents
- Content Administration deployment exports for bulk extraction

**DataStage integration options:**
- dsjob command-line interface for job management and XML report generation
- dsexport utility for exporting job definitions directly to XML format
- Native XML storage format for job definitions

These are not theoretical - they are documented, supported integration methods that have been used for years in enterprise environments.

### Current AI Usage

The team has already achieved approximately 30% efficiency gains using AI tools like Claude for SQL transformation. However, the current workflow is manual: open a report, extract the SQL, run it through AI, validate the output, and deploy. Each step requires human intervention.

The aspiration is to move from this piecemeal approach to an orchestrated agent workflow that can run multiple steps in parallel with minimal human intervention.

### The Semantic Layer Goal

A common semantic layer is being established across all reporting tools - Cognos, ThoughtSpot, and any future BI tools. The goal is tool agnosticism: point any reporting tool at the same dataset and get consistent KPIs. No more "my number versus your number" disputes between reports.

### The Core Constraint

SME bandwidth remains the bottleneck. The same experts needed to keep production systems running are also needed to validate re-engineering work. AI acceleration is valuable to the extent it reduces this burden - surfacing decisions that need human judgment while automating the mechanical work.

---

## Key Technical Challenges

### Challenge 1: SSAS to Databricks Transition

The eight SSAS cubes currently feed Excel pivot tables that business users rely on heavily. The drag-and-drop KPI experience in Excel is deeply embedded in workflows. Moving to Databricks while preserving this Excel experience is a significant change management challenge.

The current approach exposes aggregated data through ThoughtSpot, but this requires users to learn a new interface. Retaining the familiar Excel experience while pointing to Databricks backends would minimize disruption.

**Potential approach:** Custom Excel connectivity to Databricks, similar to how Hyperion environments have addressed this challenge. This is infrastructure work rather than AI work, but critical to the overall program success.

### Challenge 2: Cognos Report Re-engineering Automation

Today's workflow for each Cognos report:
1. Manually open the report in Cognos
2. Extract the embedded SQL
3. Run the SQL through AI for transformation
4. Validate the Databricks-compatible output
5. Deploy and test

At 6,000+ reports, this manual process creates a years-long timeline even with AI assistance. The goal is an agent that can integrate directly with Cognos, read report definitions programmatically, and orchestrate the re-engineering workflow end-to-end.

### Challenge 3: DataStage Pipeline Migration

DataStage jobs contain embedded business logic spread across XML job definitions. The same manual pattern applies: extract XML, feed to AI, validate, deploy to Databricks pipelines. Automating this integration would enable parallel processing of hundreds of jobs rather than sequential manual handling.

---

## Agent Orchestration Approach

### Design Philosophy

Agent swarms work best when modeled after real-world team structures. If we imagine this work being done without AI, what roles would exist? Each role becomes an agent with a specific responsibility.

The key principle: **agents work better when they're more specific**. Rather than one "reports agent" trying to do everything, a swarm might include:
- A report metadata extraction agent
- A SQL parsing agent
- A transformation validation agent
- A deployment preparation agent

Each agent does one thing well, and orchestration coordinates their work.

### Keeping Humans in the Loop

Agent automation does not mean humans disappear. The goal is to shift human effort from mechanical tasks to judgment calls:

- Agents handle: extraction, transformation, pattern matching, validation checks
- Humans handle: business logic verification, edge case decisions, final approval

Reports can be generated throughout the workflow to keep humans aware of progress and flag items that need attention, rather than operating as a black box.

---

## Schema Mapping Methodology

Schema mapping between SQL Server EDW and Databricks is not a one-to-one exercise. Three tables in EDW might become one table in Databricks, or vice versa. The complexity of these transformations makes pure AI approaches unreliable - feeding schemas into an LLM and hoping for accurate mappings produces inconsistent results that still require extensive manual review.

A structured framework approach addresses this differently.

### Deterministic Foundation First

Before AI touches anything, establish certainty where certainty is possible:

**Phase 1: Structural Discovery (No AI)**
- Enumerate all tables, views, and schemas in both environments
- Map data types, column names, and relationships
- Create a reliable baseline that AI can reference without hallucination risk

**Phase 2: Rule-Based Mapping (No AI)**
- Exact column name matches
- Tables with identical structures
- Known migration patterns from earlier tracks

This typically resolves 30-40% of mappings with near-perfect certainty. These become anchor points that AI cannot contradict.

**Phase 3: AI-Assisted Mapping**

AI handles the remaining ambiguous cases:
- Semantic similarity between column names
- Data type compatibility analysis
- Sample value pattern matching
- Contextual clues from related tables

### Confidence-Based Routing

Not all mappings require the same level of attention. Each mapping receives a confidence score - but confidence is not AI guessing. It's pattern recognition based on human feedback.

**How confidence builds:**
- When a human approves an AI-suggested mapping, that approval is stored with full context
- The next time the system encounters a structurally similar situation, it recognizes the pattern
- If the same pattern has been approved multiple times, confidence is high
- Each human approval reinforces the system's understanding

This creates a feedback loop. Early in the process, more items require human review. As approvals accumulate, the system learns what "correct" looks like for this specific environment. High confidence means humans have already validated this type of change repeatedly.

**Routing based on confidence:**
- **High confidence:** Pattern matches multiple prior approvals - auto-proceed
- **Medium confidence:** Similar to approved patterns but with variations - flagged for quick verification
- **Low confidence:** No matching patterns or conflicting signals - routed to SME for judgment

Human effort concentrates on genuinely novel cases rather than re-approving the same patterns.

### Persistent Knowledge Graph

In a typical AI workflow, each mapping is independent - insights from one report don't inform the next. A structured approach maintains a central knowledge graph that accumulates learnings:

- Patterns discovered in Finance track carry forward to Merchandising
- Entity relationships learned once are applied everywhere
- Edge cases and exceptions are remembered, not re-discovered

Accuracy improves over time as the system processes more assets.

### Validation and Guardrails

Before any mapping reaches human review, it passes through validation that checks for:
- Internal consistency (does this mapping contradict other mappings?)
- Pattern compliance (does this follow established conventions?)
- Completeness (are there obvious gaps?)

Obvious errors are caught and corrected before consuming human attention.

**Failure handling:**
- If validation fails, the system retries with adjusted parameters
- If retries continue to fail, the item is escalated to human review - not retried indefinitely
- All failures are logged with full context so patterns of failure can be identified and addressed
- Humans always have visibility into what's being processed and can intervene at any point

The goal is automation with guardrails, not a black box. Items that the system cannot resolve confidently become human decisions rather than pipeline blockers.

---

## Tool Integration Strategy

### MCP for Reliable Connections

Agents need to interact with actual systems - Cognos, DataStage, SQL Server, Databricks. Rather than having agents figure out how to connect each time, MCP (Model Context Protocol) provides stable, reliable interfaces.

With MCP:
- Connection logic is defined once and reused
- Agents call consistent functions rather than improvising
- Error handling is standardized
- Testing becomes deterministic

This is particularly important for legacy systems where connection patterns might be non-obvious.

### Building on Existing Infrastructure

Any agent development should use existing enterprise infrastructure:
- Enterprise AI accounts (Claude, Azure AI Foundry, Vertex AI)
- Existing cloud environments (Azure, GCP)
- Current security and compliance frameworks

This avoids introducing new tools that create ongoing maintenance burden. When the re-engineering program completes, there should be capability gained, not dependency created.

Azure AI Foundry models, for example, are significantly cheaper than commercial API equivalents while meeting the same enterprise security standards as other Azure services.

---

## Acceleration Capabilities

### Report Similarity Clustering

Analyze Cognos report metadata to group reports by structural similarity. Reports sharing data sources and query patterns can be re-engineered together as batches. The system learns from each report processed, building a knowledge graph that makes subsequent reports faster to handle.

### Business Logic Extraction

Parse report definitions and embedded SQL to create a readable catalog of calculations, filters, and business rules. Twenty years of accumulated logic becomes visible and documented, accelerating SME review and reducing the risk of losing critical rules.

### Dependency Mapping

Trace relationships between tables, views, reports, and cubes to create a complete dependency graph. Before touching any source, see exactly what downstream assets are affected. This prevents mid-project surprises from unexpected dependencies.

### KPI Lineage Tracing

Map the 800+ KPIs back to their source calculations across reports, cubes, and pipelines. Identify where the same KPI is calculated differently in different places. Standardizing KPI definitions is prerequisite to a clean semantic layer.

### Change Impact Analysis

Before making changes to source systems or transformation logic, simulate downstream impact across the entire reporting portfolio. Make changes with confidence rather than discovering broken reports after deployment.

### Documentation Generation

Generate documentation for undocumented stored procedures, DataStage jobs, and report logic. Institutional knowledge embedded in code becomes explicit and reviewable - valuable for onboarding and SME validation.

### Consolidation Detection

Identify reports with nearly identical functions and minor variations. Organizations accumulate redundant reports over time. Surfacing consolidation opportunities reduces the total volume requiring re-engineering.

---

## Implementation Approach

### Start Small, Prove Value

Rather than proposing a large engagement upfront, a focused proof-of-concept on representative samples demonstrates feasibility with actual systems. A handful of Cognos reports and DataStage jobs is enough to show:

- Agent integration with legacy systems works
- The orchestration pattern handles real complexity
- Output quality meets validation requirements

### Build on Your Infrastructure

Development happens within existing security and compliance frameworks. This might mean:
- Using client-issued hardware with standard images
- Working through VPN and approved access methods
- Leveraging existing enterprise AI accounts
- Deploying to existing cloud environments

No new tools to evaluate, license, or maintain long-term.

### Scale Based on Results

Once the proof-of-concept validates the approach, the same patterns scale to larger batches. The work to process 100 reports is not dramatically different from processing 1,000 once the foundation is established.

---

## Discussion Topics

1. **Architecture Deep Dive** - How is the Databricks environment structured? What tools have been selected for pipelines? How is the semantic layer being implemented?

2. **Representative Samples** - What would a good cross-section of reports and jobs look like for a proof-of-concept? What represents the range of complexity?

3. **Integration Points** - What access methods exist for Cognos and DataStage in the current environment? Are staging servers available for experimentation without production impact?

4. **Priority Ranking** - Of the challenges discussed, which would deliver the most value if solved first? Where is the team spending the most manual effort today?

5. **Success Criteria** - What would a successful proof-of-concept need to demonstrate to build confidence in a larger engagement?

---

*BayOne Solutions*
