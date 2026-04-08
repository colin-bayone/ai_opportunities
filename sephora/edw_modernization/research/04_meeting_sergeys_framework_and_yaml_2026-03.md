# 04 - Meeting: Sergey's Framework and YAML Configuration Approach

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive)
**Pass:** Focused deep dive on Sergey's AggregationApplication framework explanation

---

## Context: Who Sergey Is and Why This Input Matters

Sergey is Sephora's senior developer and subject matter expert on all IBM tools (Cognos, DataStage). Andrew introduced him explicitly during this meeting as the team's authority on the legacy stack.

**Key statement from Andrew (lines 132-133):** "We have Sergey, who actually really like our SMB on all our IBM, you know, caught those tools, the data-stage tools. I mean, he knows because he's been really the background behind seeing the developer for us throughout the last 10, 15 years."

Translation: Sergey has been the lead developer behind the IBM Cognos and DataStage environment for 10-15 years. When Sergey speaks about what the framework needs and what acceptable output looks like, he is speaking with the authority of the person who built and maintains the production system. His input is not advisory — it is definitive. Any demo or prototype that does not align with Sergey's stated requirements will be rejected.

Sergey's intervention came late in the meeting (lines 584-609), after approximately an hour of higher-level discussion between Colin, Andrew, Grishi, and Meher about Cognos reports, MCP servers, and agent architecture. When Sergey spoke, he redirected the entire conversation away from Cognos report conversion and toward the DataStage-to-Databricks migration track. His remarks were concise, technical, and prescriptive.

---

## 1. The Existing Databricks Framework: No New Frameworks Needed

### 1a. The Framework Exists and Is Mature

Sergey's central point is that Sephora already has a mature, production-proven framework running on Databricks. The framework is Scala-based (transcribed as "color-based"), but critically, developers do not write Scala code. They write configuration files. The framework handles everything else.

**Key statement (lines 585-588):** "Our goal is to migrate data state jobs to existing framework. So on Databricks, we develop frameworks, color-based [Scala-based], where you don't need to do, let's say, Python development or something. So you just need to do configuration. And we have, let's say, thousands of jobs running in production today, support team aware how to support them and so on."

This statement contains several critical facts:

1. **The goal is migration to an existing framework** — not building a new one, not creating notebooks, not generating Python or Scala code
2. **The framework is Scala-based** — the underlying runtime is Scala, but this is invisible to developers
3. **Developers only write configuration** — no Python, no Scala, no notebook code
4. **Thousands of jobs already running in production** — this is not theoretical; it is the proven production standard
5. **The production support team already knows how to support these jobs** — operational readiness is already established for this framework

### 1b. Explicit Rejection of New Frameworks

**Key statement (lines 589-594):** "So basically, no need to create, let's say, new framework by using some Python or something yeah so everything is there we just need to configure you know and ideally this agent should create all needed configurations."

Sergey was unambiguous: do not create a new framework. Do not generate Python. Do not generate Scala. Everything needed already exists. The only thing the agent needs to produce is configuration files.

**Key statement on the cost of introducing new frameworks (lines 593-594):** "And if we will introduce new framework, you know, it's additional cost for them, they should, you know, learn it, supported, and so on."

This is the production support argument. Sephora has an existing production support team that already knows how to monitor, debug, and maintain jobs running in the current framework. Introducing a new framework means:

- The support team must be trained on the new framework
- New monitoring and logging procedures must be established
- New debugging workflows must be created
- Additional cost is incurred for all of this

Sergey is saying: the framework is not a suggestion. It is a hard constraint. Any output that does not conform to the existing framework creates operational overhead that Sephora will not accept.

---

## 2. The Three Configuration Files Per Job

### 2a. YAML Configuration Structure

**Key statement (lines 602-604):** "Again, main question right now, how to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside. Let's say 20, 50 different parameters like source table name, connection details and so on."

Each job in the framework requires **three YAML files** (or configuration files in YAML format). Sergey did not enumerate all three by name in this meeting, but he specified:

1. **Pipeline YAML** — defines the actual data transformation logic and flow
2. **Deployment YAML** — defines deployment configuration (environment, scheduling, resources)
3. **create.HQL** — the HiveQL file that creates the necessary tables/views in Databricks

The parameters within these YAML files number between **20 and 50** per job. Sergey gave two specific examples of parameter types:

- **Source table name** — where the data is coming from
- **Connection details** — how to connect to the source system

The remaining parameters (up to 50) were not enumerated in this meeting but would include things typical to data pipeline configuration: target table name, catalog, schema, partition columns, write mode, file format, transformation rules, scheduling parameters, retry logic, notification settings, and similar operational configuration.

### 2b. What the Framework Handles Automatically

**Key statement (lines 595):** "But there we have defined logging procedures, file lowers [file flows], and so on."

Translation: The existing framework provides out-of-the-box:

- **Logging procedures** — standardized logging that the production support team monitors
- **File flows** — standardized patterns for data movement (ingestion, staging, output)
- **Support model integration** — because the framework is standardized, the production support team already has established procedures for monitoring, alerting, and debugging

These are not things the agent needs to produce. These are things the framework provides when given proper YAML configuration. This is why Sergey insists on configuration-only output: the framework already solves the hard operational problems (logging, monitoring, error handling, file management). The only thing that varies per job is the configuration.

### 2c. No Code Writing Required — Only Configuration

**Key statement (lines 599-605):** "It's not the complex color [Scala] that we are migrating. Again, no need to write Scala code there at all. So if you talk about aggregation or ingestion, there are no need to do Scala code. So again, main question right now, how to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside... So you don't need to write code itself, just to create config file. It's even simpler than write code."

Sergey made this point with emphasis: for both aggregation pipelines and ingestion pipelines, Scala code is not needed. The framework abstracts all of that away. What the agent must produce is purely declarative configuration — YAML files with parameters. Sergey explicitly called this out as being **simpler than writing code**, which means it should also be simpler for an agent to produce correctly.

---

## 3. Sergey's Critique of Claude's Current Output Quality

### 3a. The "Spaghetti Code" Problem with Notebooks

**Key statement (lines 596-598):** "This is also a problem with lake bridge [Claude]. So we're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of Windows [cells/windows] inside this notebook and how to maintain it I don't I I don't know if it will be nightmare, you know to debug it and so on. Such a problem."

Translation: Sephora has already tried using Claude (transcribed as "lake bridge" or "Lake bridge") for DataStage migration. The results were Databricks notebooks containing what Sergey characterizes as **spaghetti code** — notebooks with hundreds of cells ("windows") that are:

- Unmaintainable
- A nightmare to debug
- Not aligned with the existing framework
- Not supportable by the production support team

This is a direct critique of what happens when an AI tool generates code (Python or Scala in notebook form) rather than configuration. The AI produces something that technically works but is operationally unacceptable because it cannot be maintained, debugged, or supported within the existing framework.

### 3b. The Earlier Attempt Referenced by Meher

**Key statement from Meher (lines 579-582):** "And if you want to extend the demo one of the data stage out and see how did that work on the address because we did that with is the Lake bridge [Claude]. But it was almost like 85% need to do something we can on the deliberate side, convert it to vice part [Spark]. So that's another one. None of we have, we probably can have a simple data stage job that we can share."

Translation: Sephora already attempted using Claude to convert a DataStage job. The result was approximately **85% correct** but still needed significant manual rework. The output needed to be converted to Spark-compatible code. Meher suggested sharing a simple DataStage job for the demo, implying the previous attempt was on something more complex.

This 85% figure is important context: Claude can get most of the way there with raw code generation, but the output does not fit the framework, requires manual rework, and produces unmaintainable notebook code. Sergey's framework approach would eliminate these problems by having the agent produce structured YAML instead of code.

---

## 4. Sergey's Ideal Workflow for Agent Output

### 4a. The Conversion Path: Stored Procedures to SQL to YAML

**Key statement (lines 590-592):** "Let's convert this stored procedure to SQL logic we can say like this spark SQL logic or to Scala but ideally to SQL, to simplify things. Because, you know, stored procedure is basically SQL, so you can just more easily convert it to SQL."

Sergey's preferred conversion path:

1. **Start with the stored procedure** — this is the source artifact from the legacy DataStage/SQL Server environment
2. **Convert to Spark SQL** — not Scala, not Python, but SQL. Stored procedures are already SQL at their core, so this is a language-to-language translation (T-SQL to Spark SQL), which is simpler than a language-to-paradigm translation
3. **Generate YAML configuration files** — the Spark SQL logic becomes one of the parameters in the YAML configuration, and all other operational parameters (source, target, connections, scheduling) are populated in the YAML structure

The key insight here: Sergey explicitly prefers SQL over Scala ("ideally to SQL, to simplify things") because stored procedures are already SQL. Converting SQL to SQL is a tractable problem. Converting SQL to Scala or Python code is a more complex transformation that introduces unnecessary risk and complexity.

### 4b. The Ideal Agent Interaction Model

**Key statement (lines 607-609):** "Let's say if we can ask him [the agent] in the brackets. Ask him, hey man, we have 10 jobs, please convert them, generate YAML files, commit them to packet [repo]. After that, some developer can quickly review that it's good and that's it."

Sergey described his ideal workflow in concrete terms:

1. **Batch input** — give the agent 10 jobs (not one at a time)
2. **Agent converts stored procedures to Spark SQL logic**
3. **Agent generates the YAML configuration files** (all three per job)
4. **Agent commits the files to a repository** (version control)
5. **Developer reviews and approves** — human in the loop only at the review/approval stage, not during generation

This is a pull-request model: the agent does all the conversion and configuration generation work, commits to a branch, and a developer reviews the output before it is merged. The developer is not writing anything — they are reviewing what the agent produced.

### 4c. The Scale Implication

Sergey said "10 jobs" as an example, but the system has thousands of jobs running in production. The ideal workflow scales: if the agent can handle 10, it can handle 100 or 1,000. The developer review step is the bottleneck in this model, not the agent's generation speed.

---

## 5. Ingestion vs. Aggregation Pipelines in the Framework

### 5a. Both Pipeline Types Use the Same Configuration Approach

**Key statement (lines 600-601):** "It's not the complex color [Scala] that we are migrating. Again, no need to write Scala code there at all. So if you talk about aggregation or ingestion, there are no need to do Scala code."

Sergey explicitly called out both pipeline types that exist in the framework:

- **Ingestion pipelines** — move data from source systems into Databricks (raw/landing zone)
- **Aggregation pipelines** — transform and aggregate data within Databricks (business logic layer)

For both types, the same principle applies: no Scala code, no Python code, only YAML configuration. The framework handles the execution for both.

### 5b. Meher's Confirmation of Framework Usage

**Key statement from Meher (lines 628-631):** "We pointed to the framework that Sergey talked me about, and did an aspect to introduce a new ingestion pipeline, source data front, and Oracle database. And it did, you know. It's a cloud [Claude] that's not new stuff yet."

Translation: Meher confirmed that they have already used the framework Sergey described to introduce a new ingestion pipeline sourcing data from an Oracle database. The framework works. They also attempted to use Claude for this, with mixed results ("it's Claude, that's not new stuff yet" — suggesting Claude was not fully effective at producing framework-compatible output).

---

## 6. The Production Support Model as a Hard Constraint

### 6a. Thousands of Jobs as Proof of Maturity

Sergey's reference to "thousands of jobs running in production" (line 588) is not an idle boast. It is a statement of operational fact that carries specific implications:

- **The framework is battle-tested** — it has survived production workloads at scale for years
- **The support team is trained** — monitoring, alerting, and incident response procedures are established
- **Operational tooling is built around it** — logging, file flows, and debugging tools all assume the framework's conventions
- **Adding jobs is a known process** — the operational cost of adding a new job is low because it follows the established pattern

### 6b. Why "New Framework" Is a Non-Starter

Any approach that produces output outside the framework creates a dual-support burden:

1. The support team must continue supporting the thousands of existing framework-based jobs
2. The support team must **also** learn how to support the new-style jobs (notebooks, custom code, etc.)

This is not a technical objection — it is an operational cost objection. Sergey is saying that even if a new approach technically works, the total cost of ownership is higher because of the support overhead. The existing framework eliminates that overhead because the support model is already in place.

---

## 7. What This Means for the Demo and Engagement

### 7a. The Demo Must Produce YAML, Not Code

Sergey's input redefines what "success" looks like for the demo. Before his intervention, the conversation was about Cognos report conversion and MCP servers. After his intervention, there is a second demo track: DataStage job migration that produces YAML configuration files compatible with the existing framework.

The demo must show:

1. **Input:** A DataStage job definition (stored procedure or job definition XML)
2. **Processing:** Conversion of SQL Server T-SQL logic to Spark SQL
3. **Output:** Three YAML configuration files per job, populated with the correct 20-50 parameters
4. **Delivery:** Files committed to a repository for developer review

The demo must NOT show:

- Generated Databricks notebooks
- Python code
- Scala code
- Any output that exists outside the framework's configuration model

### 7b. The Simplicity Argument Favors This Approach

Sergey made an under-appreciated point: generating YAML configuration is **simpler than generating code** (line 605: "It's even simpler than write code"). This is true from the agent's perspective as well:

- YAML files have a fixed, well-defined structure
- Parameters are finite and enumerable (20-50 per job)
- The mapping from stored procedure logic to Spark SQL is a SQL-to-SQL translation
- There is no need to handle complex programming constructs, error handling patterns, or runtime logic — the framework handles all of that

This means the demo is actually more achievable than generating full code would be, while simultaneously being more valuable to Sephora because the output is production-ready.

### 7c. Meher's Suggested Demo Path

**Key statement from Meher (lines 579-582):** Meher suggested sharing a simple DataStage job for the demo. This aligns perfectly with Sergey's framework approach: take a real DataStage job, have the agent convert its stored procedure logic to Spark SQL, generate the three YAML files, and present the result for developer review.

The combination of Meher's practical suggestion and Sergey's technical requirements defines a clear, bounded, and high-value demo scope.

---

## 8. Implied Technical Requirements Not Explicitly Stated

Based on Sergey's description, the following requirements are implied even though not stated verbatim:

### 8a. The Agent Must Know the YAML Schema

To generate YAML files with 20-50 parameters, the agent must have access to the YAML schema or template that the framework expects. This means:

- Example YAML files from existing production jobs should be provided as reference
- The agent must understand which parameters are required vs. optional
- The agent must understand valid values for each parameter (enums, connection string formats, etc.)

### 8b. The Agent Must Understand Spark SQL Dialect

Stored procedures from SQL Server use T-SQL. Spark SQL has different syntax for:

- Window functions
- Date/time operations
- String functions
- Conditional logic (CASE statements are similar, but procedural IF/ELSE is not)
- Temp tables and CTEs
- Data type casting

The agent performing the conversion must handle these dialect differences correctly.

### 8c. The Agent Must Handle the Ingestion/Aggregation Distinction

Different pipeline types likely have different YAML schemas or at least different required parameters. The agent must know whether a given DataStage job maps to an ingestion pipeline or an aggregation pipeline and generate the appropriate YAML variant.

---

## 9. Direct Quotes Index

For reference, the key verbatim quotes from Sergey (with transcription corrections noted in brackets):

| Lines | Quote (corrected) | Significance |
|-------|-------------------|--------------|
| 585-588 | "Our goal is to migrate DataStage jobs to existing framework. So on Databricks, we develop frameworks, Scala-based, where you don't need to do Python development or something. So you just need to do configuration. And we have thousands of jobs running in production today, support team aware how to support them." | Establishes the framework as the mandatory target |
| 589 | "No need to create new framework by using some Python or something. Everything is there, we just need to configure." | Explicit rejection of new framework/code generation |
| 590-592 | "Let's convert this stored procedure to SQL logic, Spark SQL logic or to Scala but ideally to SQL, to simplify things. Because stored procedure is basically SQL, so you can just more easily convert it to SQL." | Defines the preferred conversion path |
| 593-594 | "If we will introduce new framework, it's additional cost for them [support team], they should learn it, support it, and so on." | The production support cost argument |
| 595 | "We have defined logging procedures, file flows, and so on." | Framework provides operational infrastructure |
| 596-598 | "This is also a problem with Claude. So we're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of cells inside this notebook and how to maintain it, I don't know, it will be nightmare to debug it. Such a problem." | Direct critique of Claude's current output |
| 599-601 | "It's not the complex Scala that we are migrating. No need to write Scala code there at all. If you talk about aggregation or ingestion, there are no need to do Scala code." | Both pipeline types are configuration-only |
| 602-604 | "How to teach these agents to understand that we need to create three YAML files with some configuration inside. 20, 50 different parameters like source table name, connection details and so on." | Defines the exact output format |
| 605 | "You don't need to write code itself, just to create config file. It's even simpler than write code." | Simplicity argument for configuration approach |
| 607-609 | "Ask him, hey man, we have 10 jobs, please convert them, generate YAML files, commit them to repo. After that, some developer can quickly review that it's good and that's it." | The ideal end-to-end workflow |

---

## 10. Summary: The Non-Negotiable Requirements from Sergey

1. **Output format:** Three YAML configuration files per job, not code
2. **SQL dialect:** Spark SQL, not Scala or Python
3. **Framework compliance:** All output must be compatible with the existing Databricks framework
4. **No new frameworks:** The production support team already knows the current framework; do not introduce anything new
5. **Batch processing:** The agent should handle multiple jobs at once, not one at a time
6. **Repository integration:** Output should be committed to a repo for developer review
7. **No notebooks:** Databricks notebooks with generated code are explicitly rejected as "spaghetti code" and unmaintainable
8. **20-50 parameters per job:** The YAML files contain a finite, well-defined set of parameters
9. **Production support continuity:** The existing logging, file flows, and support procedures must be preserved
10. **Developer review, not developer writing:** Humans review and approve; they do not write or rewrite the agent's output
