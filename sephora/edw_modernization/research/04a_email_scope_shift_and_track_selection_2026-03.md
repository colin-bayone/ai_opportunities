# 04a - Email: Scope Shift and Track B Selection

**Source:** /sephora/edw_modernization/source/email_3-6-2026_malika.txt, email3_malika_2026-03.txt
**Source Date:** 2026-03-06 through 2026-03 (Post-meeting email thread)
**Document Set:** 04a (Email Thread)
**Pass:** Focused deep dive on scope evolution and Track B selection

---

## 1. Malika's March 6 Scope Shift Email

One day after the Set 04 technical deep dive meeting, Malika sent an email that fundamentally redirected what BayOne would need to demonstrate. The email was addressed to the full team (Zahra, Neha, Colin, Rahul) with Sergey, Maher Burhan, Gariashi, and Andrew on CC. It arrived Friday, March 6, 2026 at 4:46 PM.

### What She Eliminated: Code Translation

Malika opened with a direct statement that code translation alone -- the initial expectation going into the engagement -- was off the table as a demo focus:

> "While the initial expectation was to provide a Cognos report XML and demonstrate code translation to Databricks SQL, we should note that our team is already performing report logic extraction and SQL conversion using our internal enterprise AI tooling and LLM-assisted workflows."

> "As such, code translation alone would not be the primary area we are looking to evaluate."

This is the single most consequential scope statement in the email thread. Sephora's internal team already uses Claude and other LLM-assisted workflows to do code translation. They do not need BayOne to demonstrate that capability. If BayOne had built a demo centered on translating SQL from one dialect to another, it would have shown Sephora something they already do in-house. The demo would have failed before it started.

This aligns with Sergey's statements during the Set 04 meeting about having used Claude for DataStage conversion (achieving 85% accuracy). The Sephora team is not naive about LLM-assisted code transformation -- they have direct, recent experience with it. What they lack, and what they want to evaluate, is the orchestration layer that sits above the translation step.

### What She Wanted: Agent-Driven Orchestration

Malika then listed five specific capabilities she wanted the demo to showcase. These are quoted directly from the email:

1. **"Demonstration of the MCP server or integration layer for Cognos that you previously mentioned"** -- This references Colin's Set 03 and Set 04 presentations about building MCP connectors for legacy systems. Malika is calling out a specific claim Colin made and asking to see it demonstrated.

2. **"Automated extraction of report metadata or XML from Cognos"** -- Not manual export followed by LLM processing, but an agent that reaches into Cognos and extracts what it needs programmatically.

3. **"Agent orchestration across multiple tools (e.g., Cognos, Databricks)"** -- The agent must work across system boundaries, not within a single tool. The value is in bridging the gap between the legacy source (Cognos on SQL Server) and the modern target (Databricks).

4. **"End-to-end workflow automation, where the agent coordinates the extraction, interpretation, and downstream execution steps"** -- The agent is not a helper that does one step while a human handles the rest. It coordinates the full pipeline: extract from source, interpret what was extracted, and execute (or generate) the downstream output.

5. **"How the agent manages tool communication, task sequencing, and dependency handling across the migration process"** -- This is the most technically specific ask. Malika wants to see how the agent decides what to do next, how it passes context between tools, and how it handles dependencies (e.g., a SQL conversion that depends on first extracting the schema, which depends on first connecting to the metadata layer).

### What "End-to-End Agent Orchestration" Means to Sephora

Reading these five capabilities together, Sephora's definition of agent orchestration is precise and operational. They are not asking for a chatbot that answers questions about migration. They are asking for:

- An agent that connects to multiple systems (Cognos, SQL Server, Databricks) through programmatic interfaces (MCP or equivalent)
- An agent that autonomously sequences its own work: first extract, then interpret, then generate output
- An agent that manages dependencies between steps without human intervention at each handoff
- An agent that produces end-to-end results, not intermediate artifacts that require manual assembly

The emphasis on "tool communication" and "dependency handling" suggests that Malika is thinking about this as a workflow engine problem, not a code generation problem. The code generation piece (SQL translation) is already solved in their view. What is not solved is the automation of the surrounding workflow: knowing what to extract, from where, in what order, and how to assemble the pieces into something deployable.

### The ETL Migration Addition

After the five orchestration capabilities, Malika added a second use case that had not been the primary focus during the meeting:

> "Additionally, we would also like to include an ETL migration use case (attached) to understand how the agent handles legacy data pipeline modernization."

She listed four capabilities for this track:

1. **"Parse DataStage job XML, SQL Server DDL, stored procedures, and views"** -- The input artifacts are DataStage job definitions (XML format), plus the SQL Server objects they reference (DDL for table creation, stored procedures for transformation logic, and views for data access patterns).

2. **"Extract transformation logic and business rules"** -- Not just translate syntax, but understand what the code does. A stored procedure may implement business rules (e.g., inventory aggregation thresholds, date range filters, product category mappings) that must be preserved in the migrated output.

3. **"Map those patterns to Spark-based transformations"** -- The extracted logic must be mapped to Spark-compatible equivalents. This is not a one-to-one syntax swap; DataStage transformation patterns (e.g., sequential stage processing, hash partitioning, reject links) have different idioms in Spark.

4. **"Generate Databricks-compatible pipelines (Spark SQL / Scala) along with supporting deployment artifacts and documentation"** -- The output includes both the transformation code (Spark SQL or Scala) and the deployment artifacts (configuration files, pipeline definitions) plus documentation.

Note that Malika's email specified "Spark SQL / Scala" as the output format. This directly conflicted with what Sergey said during the Set 04 meeting, where he explained that the target output should be YAML configuration files for the existing AggregationApplication framework, not Scala code. Colin caught this discrepancy and raised it explicitly in his March 9 response.

### The "Your Setup" Instruction

Malika closed the scope section with a logistical directive:

> "It may be easier if the demo is performed using your setup as the goal of this evaluation is to understand how the agent could coordinate multiple tools and automate the migration workflow, rather than focusing only on isolated code conversion."

This confirms the disconnected approach agreed upon in the Set 04 meeting. BayOne should build and run the demo on their own infrastructure. Sephora's goal is to evaluate the orchestration capability, not to integrate with their environment during the demo phase. This also eliminates the security review blocker that Malika and Sergey raised during the meeting (Sephora's security team had previously blocked an MCP server attempt).

---

## 2. Colin's March 9 Response: Track A vs Track B

Colin responded on Monday, March 9, 2026 at 6:55 PM. The email went to Malika, Gariashi, and Andrew (the three Sephora decision-makers), with Sergey, Zahra, Neha, Rahul, Maher Burhan, and Saurav Kumar Mishra on CC.

### Acknowledging the Scope Shift

Colin opened by naming the shift directly:

> "I want to make sure we're on the same page before we start building anything because it looks like a few things have shifted from the call last week."

> "The demo scope we landed on during the call was Cognos lift-and-shift with agent-based orchestration and MCP integration. DataStage came up towards the end as an interesting area but wasn't the primary focus. It sounds like your team has been thinking more about this since then and is now leaning towards ETL migration/DataStage as the lead use case."

This is Colin establishing the record: the Set 04 meeting concluded with Cognos as the primary track and DataStage as a secondary/optional track. Malika's email reversed that priority. Colin did not resist the shift -- he acknowledged it and structured the response around it.

### The Scoping Constraint

Colin set a clear boundary on demo scope:

> "For the demo, we'd build out one of the two tracks to demonstrate the capability, as covering both would extend into paid engagement territory."

This is a deliberate scoping decision. BayOne would demonstrate one track as a free proof-of-concept. If Sephora wanted both tracks, that would require a paid engagement. He framed it positively by noting that "both tracks are extensions of the same underlying architecture" -- the same agent orchestration patterns apply to either use case, so demonstrating one proves the capability for both.

### Track A: Cognos MCP Demo

Colin described Track A with three capabilities:

1. **MCP connector for Cognos** that extracts report metadata and SQL programmatically
2. **Agent-based conversion with orchestration** from Cognos/SQL Server to Databricks-compatible output
3. **Remapping to the target schema**

He then flagged a critical limitation:

> "One thing to flag on this track A is that we can build the MCP connector, but live demonstration for MCP requires access to your Cognos environment. Cognos is proprietary and there's no way for us to spin one up independently. Without that access, we'd demonstrate the full workflow using exported report XML. In production, the MCP connector would replace those manual exports."

This is an honest constraint disclosure. The MCP connector -- the thing Malika specifically asked to see demonstrated -- cannot be shown working live unless BayOne has access to an actual Cognos instance. Cognos is proprietary IBM software. There is no free tier, no open-source alternative, no way to stand up a test instance without a license. Without environment access, Track A would demonstrate the full conversion workflow but with the MCP piece shown as an architecture diagram and code walkthrough rather than a live connection.

Given that Malika's first listed capability was "Demonstration of the MCP server or integration layer for Cognos," this limitation directly undercut the primary ask for Track A.

**Prerequisites for Track A:**
- Cognos report XML (exported)
- Target Databricks schema

### Track B: ETL/DataStage Demo

Colin described Track B as the one aligned with Malika's email, with four capabilities:

1. **Parsing DataStage job XML** and extracting transformation logic
2. **Interpreting SQL Server stored procedures and views**
3. **Agent orchestration across parsing, interpretation, and generation steps**
4. **Generating output compatible with the existing framework**

Colin noted that BayOne already had most of the materials needed for Track B:

> "We already have the DataStage XML, stored procs, views, and examples of your target YAML and Scala framework."

This is because Sergey had already shared a folder of ETL artifacts either during or shortly after the Set 04 meeting. The one missing piece was Databricks source table schemas:

> "The one item we'd still need for track B is Databricks source table schemas for tables like edwlib_whintr, smt_location, and smt_product. We have the legacy SQL Server DDL but need to know what those source tables look like on your Databricks side to generate accurate output."

### The YAML vs Scala Question

Colin raised the output format discrepancy directly:

> "On the call, Sergey explained that your team already has the AggregationApplication framework in place and that developers prefer to work with YAML configuration files rather than writing Scala directly. Your email referenced Spark SQL / Scala as the expected output. Could you confirm which direction your team is aligned on?"

This question captures a genuine ambiguity from the Set 04 meeting. Sergey was emphatic that the output should be YAML configuration files, not code. He described Claude's notebook-style output as "spaghetti code" that would be "a nightmare to debug." But Malika's March 6 email listed "Spark SQL / Scala" as the expected output. These two statements appeared contradictory, and Colin needed resolution before building anything.

### Colin's Implicit Recommendation

While Colin presented both tracks neutrally, the structure of the email subtly favored Track B:

- Track A had a flagged limitation (no live MCP demo without Cognos access)
- Track B was described as the one that "aligns with Malika's email"
- Track B already had most materials in hand
- Track B needed only one additional artifact (Databricks schemas)
- Colin closed with: "It looked like the ETL track B is the one of interest here but wanted to confirm as it was different than on the call."

He was reading the room correctly. Malika's email had spent more words on the ETL use case, added it explicitly as a new scope item, and attached supporting materials. The Cognos orchestration capabilities she listed (items 1-5) were important but aspirational -- Track A could only partially deliver on them without environment access.

---

## 3. Malika's Final Reply: Track B Selected

Malika's reply (undated in the source, but following Colin's March 9 email) confirmed Track B and resolved every open question.

### Track B Selection

> "After discussing internally with the team, we'd like to move forward with Track B (ETL/DataStage Demo) for the demonstration."

The selection was made after internal discussion, not by Malika alone. "The team" implies Andrew, Gariashi, and likely Sergey were consulted. The reasoning is implicit but clear from the email thread:

1. **Track B had no infrastructure blockers.** Track A's MCP limitation meant the demo could not show a live Cognos connection. Track B required no live environment access at all -- it works entirely from exported artifacts.
2. **Track B materials were already available.** Sergey had already shared the DataStage XML, stored procedures, views, and the ETL Migration Use Cases description document.
3. **Track B was the new scope item.** Malika herself introduced the ETL use case in her March 6 email. Selecting Track B validated the scope shift her team initiated.
4. **Track B addressed the harder operational problem.** Converting DataStage jobs to the YAML framework is a repeatable pattern across thousands of jobs. The Cognos conversion (Track A) was also important, but the DataStage migration represented higher volume and more immediate operational need.

### Output Format Resolution: Both Spark SQL AND YAML

Malika resolved the YAML vs Scala question definitively:

> "The expectation is that the generated output should include both components:
> - Spark SQL transformations where the core transformation logic is implemented
> - YAML configuration and deployment artifacts that integrate with the existing AggregationApplication framework"

She then explained the architecture that makes both necessary:

> "In our current framework, the business logic sits within the Spark SQL layer, while the pipeline configuration and deployment setup are managed through YAML files, so both pieces are required for the migrated pipeline to be executable."

This resolves the apparent contradiction between Sergey's YAML emphasis and Malika's Spark SQL/Scala reference. They were not describing competing approaches -- they were describing two layers of the same system:

- **Layer 1: Business logic (Spark SQL).** The actual transformation queries -- the joins, aggregations, filters, and calculations that implement the business rules from the legacy stored procedures. This is where the DataStage logic lands after conversion. It is Spark SQL, not Scala (Malika did not mention Scala in her final reply, effectively dropping that from the equation).

- **Layer 2: Pipeline configuration (YAML).** The framework orchestration layer that tells the AggregationApplication how to run the Spark SQL transformations -- source table names, connection details, scheduling parameters, dependency chains, and deployment configuration. This is what Sergey described during the Set 04 meeting when he talked about "20, 50 different parameters" and "three YAML files with some configuration inside."

Both layers are required for a migrated pipeline to be executable. A Spark SQL file without the YAML configuration is an orphaned query with no execution context. A YAML configuration without the Spark SQL is a pipeline definition with no business logic. The agent must produce both.

### How This Resolves the YAML vs Scala Question from the Technical Deep Dive

During the Set 04 meeting, the conversation created a false dichotomy:

- Sergey said the target is YAML configuration, not Scala code
- Malika's March 6 email said "Spark SQL / Scala"
- Colin's March 9 email asked for clarification

Malika's final reply establishes that:

1. **The business logic output is Spark SQL** (not Scala, not Python, not Databricks notebooks)
2. **The pipeline configuration output is YAML** (for the AggregationApplication framework)
3. **Both are required** -- they are complementary layers, not alternatives
4. **Scala is out.** Malika's final reply does not mention Scala at all. The "Spark SQL / Scala" phrasing in her March 6 email appears to have been imprecise shorthand. The actual target is Spark SQL for logic plus YAML for configuration.

This also resolves Sergey's critique of Claude's output. When Claude converted DataStage jobs directly, it produced monolithic Databricks notebooks ("spaghetti code"). The correct output is structured: Spark SQL files containing discrete transformation logic, plus YAML files that configure how those transformations execute within the existing framework. The agent must understand this two-layer architecture to produce usable output.

### The Full Expected Output Set

Combining Malika's reply with Sergey's Set 04 meeting statements about the AggregationApplication framework, the complete output for a single migrated DataStage job includes:

1. **Spark SQL transformations** -- The business logic extracted from stored procedures, converted to Spark SQL syntax, with table references remapped from SQL Server to Databricks
2. **YAML configuration files** -- Pipeline configuration for the AggregationApplication framework, containing source table names, connection details, scheduling parameters, and transformation step sequencing
3. **Deployment YAML** -- Deployment artifacts that define how the pipeline is deployed and managed in the Databricks environment
4. **create.HQL** -- Hive Query Language file for table creation/schema definition (referenced in the Set 04 meeting and the 03-04 bridge document as one of the three files per job)

This four-component output structure is what distinguishes an agent-produced migration from a raw LLM code translation. Claude can translate SQL syntax. What it does not do (without orchestration) is produce the full set of deployment-ready artifacts that slot into Sephora's existing production framework.

---

## 4. Materials Provided

Malika confirmed that Sergey had already shared the core artifacts and provided the remaining missing piece.

### Previously Shared by Sergey (Pre-Email Thread)

- **DataStage job XML** -- The source job definitions in DataStage's native XML format
- **Stored procedures** -- SQL Server stored procedures referenced by the DataStage jobs
- **Views** -- SQL Server views used as data sources or intermediate transformations
- **ETL Migration Use Cases_description.docx** -- A description document outlining the migration use cases (attached to or shared alongside Malika's March 6 email)
- **Target project structure** -- Examples of the target output format, contained in a shared folder named "Target," showing how the AggregationApplication framework organizes Spark SQL and YAML files
- **Deployment artifacts** -- Examples of the deployment configuration expected for migrated pipelines

### Provided by Malika in the Final Reply

- **Databricks source table schemas** -- This was the one missing item Colin identified in his March 9 email. Malika attached schemas for four specific tables:
  - **edwlib_whintr** -- Referenced by Colin in his March 9 email as one of the tables BayOne needed schema information for
  - **retfl030_skuloc** -- A table name suggesting retail floor / SKU-location data (consistent with Sephora's retail business)
  - **smt_location** -- A table referenced by Colin in his March 9 email; likely store/location master data
  - **smt_product** -- A table referenced by Colin in his March 9 email; likely product master data

These four schemas represent the Databricks-side table definitions that the agent needs to generate accurate Spark SQL. Without them, the agent would know what the legacy SQL Server tables look like (from the DDL) but not what the target Databricks tables look like. The schema mapping between source and target is essential for producing correct joins, column references, and data type handling in the migrated output.

### What This Means for Demo Readiness

After Malika's final reply, BayOne had everything needed to build the Track B demo:

| Artifact | Status | Source |
|----------|--------|--------|
| DataStage job XML | In hand | Sergey's shared folder |
| SQL Server stored procedures | In hand | Sergey's shared folder |
| SQL Server views | In hand | Sergey's shared folder |
| ETL Migration Use Cases description | In hand | Sergey's shared folder |
| Target project structure examples | In hand | Sergey's shared folder ("Target") |
| Deployment artifact examples | In hand | Sergey's shared folder ("Target") |
| Databricks source table schemas | In hand | Malika's final email attachment |
| Legacy SQL Server DDL | In hand | Previously shared |

No outstanding prerequisites remained. The demo build could begin immediately.

---

## 5. The Scope Evolution: From Set 04 to Track B Selection

### What Changed Between the Meeting and the Email Thread

The Set 04 technical deep dive concluded with two co-equal demo tracks:

- **Track 1 (Cognos):** The primary focus during the meeting. Colin presented homework on Cognos SDK/API research and MCP integration. Malika proposed the two-step Cognos demo (lift-and-shift, then remapping). A Finance report was identified as the target.
- **Track 2 (DataStage):** A secondary track introduced late in the meeting. Sergey provided the YAML framework details. Malika said "we probably can have a simple DataStage job that we can share" -- tentative language.

Malika's March 6 email shifted the balance:

- The five orchestration capabilities she listed (MCP server, metadata extraction, multi-tool orchestration, end-to-end workflow, dependency handling) were written as aspirational requirements, not as Track A specifics
- The ETL migration use case was added with four specific, concrete capabilities and attached materials
- The language around ETL was more concrete and actionable than the Cognos language

Colin's March 9 response surfaced the limitation that made Track A weaker: no live MCP demo without Cognos environment access. This was not new information -- the disconnected approach had been agreed in the meeting -- but putting it in writing alongside Track B's readiness made the comparison stark.

Malika's final reply completed the pivot: Track B selected, materials provided, output format clarified.

### What the Scope Shift Reveals About Sephora's Priorities

The scope shift from Cognos-centric to DataStage-centric reflects a deeper strategic calculation by Sephora's team:

1. **Volume.** Sergey described "thousands of jobs running in production" on the AggregationApplication framework. Each DataStage job that can be agent-converted represents a repeatable unit of work. The Cognos report migration, while important, involves a smaller set of reports and a less standardized conversion pattern.

2. **Existing framework advantage.** The YAML-based AggregationApplication framework already exists in production. Migrated DataStage jobs slot into an established operational model with a support team that knows how to maintain them. Cognos report conversion does not have an equivalent standardized target framework.

3. **Measurable baseline.** Sephora's internal team achieved 85% accuracy using Claude directly on DataStage conversion. This gives BayOne a clear benchmark to beat. There is no equivalent baseline for the Cognos track.

4. **Practical readiness.** All DataStage materials were already shared. The Cognos report required coordination with Vlad and selection of a specific Finance report -- additional steps that had not yet been completed.

---

## 6. Summary of Decisions and Open Items Resolved

### Decisions Made in This Email Thread

| Decision | Made By | Implication |
|----------|---------|-------------|
| Code translation alone is not sufficient | Malika (March 6) | BayOne must demonstrate orchestration, not just SQL conversion |
| ETL migration added as a use case | Malika (March 6) | Expanded scope beyond Cognos reports |
| Demo on BayOne's setup, not Sephora's | Malika (March 6) | Disconnected approach confirmed |
| One track for demo, not both | Colin (March 9) | Second track requires paid engagement |
| Track B selected | Malika (final reply) | ETL/DataStage is the demo focus |
| Output is both Spark SQL and YAML | Malika (final reply) | Business logic in Spark SQL, pipeline config in YAML |
| Scala is not the target | Malika (final reply, by omission) | Spark SQL replaces the "Spark SQL / Scala" language |
| All prerequisites satisfied | Malika (final reply) | Databricks schemas were the last missing piece |

### Open Questions Resolved

| Question | Resolution |
|----------|------------|
| Which demo track? | Track B (ETL/DataStage) |
| YAML or Scala output? | Both Spark SQL (business logic) and YAML (pipeline config) -- not Scala |
| What Databricks schemas are needed? | edwlib_whintr, retfl030_skuloc, smt_location, smt_product -- all provided |
| What materials does BayOne still need? | Nothing -- all prerequisites delivered |
| Can the demo proceed without Sephora environment access? | Yes -- confirmed by both sides |

### What Remained Open After This Thread

- The specific demo date (scheduling to be handled separately)
- Whether the Cognos track would be revisited in a paid engagement
- Whether the demo would lead to a formal engagement proposal
- Sephora's internal timeline for vendor selection
