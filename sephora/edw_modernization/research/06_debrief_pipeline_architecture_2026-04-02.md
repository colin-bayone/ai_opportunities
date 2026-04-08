# 06 - Debrief: Pipeline Architecture (Complete Walkthrough)

**Source:** /sephora/edw_modernization/source/saurav-colin_4-2-2026.txt
**Source Date:** 2026-04-02 (Demo Prep Call)
**Document Set:** 06 (Saurav/Colin Demo Prep)
**Pass:** Focused deep dive on the complete pipeline architecture

---

## Pipeline Overview

The LangGraph-based pipeline converts legacy DataStage ETL jobs (IBM InfoSphere DataStage XML, stored procedures, DDL definitions) into modern Spark/Scala pipelines with associated deployment configurations. The pipeline is a multi-stage, gate-controlled workflow with parallel execution, retry loops, human-in-the-loop review, and a learning feedback mechanism.

The current demo pipeline processes a single use case: the inventory periodic daily report. Nine source files are loaded (table definitions, Scala app, XML, schema files). Not all files are needed for every pipeline run; the orchestrator determines which files apply.

---

## Complete Stage-by-Stage Architecture

### Stage 1: Orchestrator

**Purpose:** Entry point. Loads source files and routes to the correct pipeline.

**What it does:**
- Loads all source files (XML, stored procedures, DDL files, view files, Scala references, schema files)
- Examines file names and file contents to determine which pipeline to run
- Selects the appropriate target files based on the source
- Generates a unique **run ID** for tracking this execution through the entire pipeline
- In production, all **MCP connections** (e.g., Cognos connector) would be configured here -- the orchestrator is where external system integrations live

**Current state:** Only one pipeline exists (SQL-to-Spark conversion), but the architecture supports multiple pipeline types. The orchestrator can receive more files than needed and will figure out which ones apply to which workflow.

**Model:** No LLM call at this stage (deterministic routing logic).

---

### Gate 1 (G1): Initial Validation

**Purpose:** Verify that all prerequisites are in place before parsing begins.

**Checks (all deterministic):**
1. **Artifact store loaded** -- Are all source files present and accessible?
2. **Target examples present** -- Are the Scala and YAML reference files (from Sephora) available?
3. **Correct pipeline selected** -- Does the selected pipeline match against a known list of valid pipeline types?
4. **Run ID generated** -- Was a run ID successfully created by the orchestrator?

**Failure behavior:** If any check fails, G1 loops back to the orchestrator to reload or re-resolve. This is a retry loop, not a terminal failure.

---

### Stage 2: Three Parallel Parsers

After G1 passes, three parsers fire simultaneously. Each parser targets a different source file type and extracts different information. Because they have independent source inputs and produce independent outputs, they run in parallel.

#### Parser 1: DataStage Parser (DS Parser)

**Source input:** XML files (DataStage job exports)

**Extracts:**
- Job stages
- Transformations
- Source/target connections
- Data flow (how data moves between stages)

**Internal architecture (two parallel sub-processes):**
1. **Deterministic extraction** -- Directly parses the XML to pull out job stages, transformations, and connections that can be identified structurally from the XML markup
2. **LLM synthesis** -- Takes the deterministic extraction results plus the original XML file and sends both to the LLM. The LLM checks whether the deterministic extraction is complete and identifies anything missed. Produces a comprehensive extraction covering all job stages, transformations, source/target connections, and data flow.

Both sub-processes run in parallel within the DataStage Parser node.

#### Parser 2: SQL Interpreter

**Source input:** Stored procedure text files (e.g., USP_update, populate_stock_inventory_pre_period)

**Extracts:**
- Table joins
- CTEs (Common Table Expressions)
- Temp tables
- Business logic
- Aggregation patterns

**Internal architecture (deterministic + LLM):**
1. **SQLGlot parsing** -- The stored procedure text is parsed through SQLGlot. SQLGlot may or may not catch everything (especially complex business logic), and that is acceptable.
2. **LLM synthesis** -- The SQLGlot extraction output plus the original stored procedure text are sent to the LLM. The LLM produces complete business rules extraction for each file.

**Key note:** Business rules extracted here are critical but are the hardest element to validate deterministically downstream. This is a recurring theme throughout the pipeline.

#### Parser 3: DDL Parser

**Source input:** DDL files and view files (table definition files)

**Extracts:**
- Table names
- Column names
- Data types
- Typecast specifications
- Constraints
- Precision values (e.g., decimal point precision)

**Internal architecture (deterministic + LLM):**
1. **SQLGlot parsing** -- DDL and view files parsed through SQLGlot for structural extraction
2. **LLM synthesis** -- SQLGlot results plus original files sent to LLM for comprehensive extraction

**Pattern across all three parsers:** Each uses the same two-track approach: deterministic extraction (SQLGlot or direct XML parsing) runs in parallel with LLM synthesis. The deterministic results are fed into the LLM call as additional context, giving the LLM a baseline to validate against and extend.

---

### Gate 2 (G2): Parser Validation

**Purpose:** Verify that parser outputs are accurate and not hallucinated.

**Checks:**
- **Table name verification** -- Do table names from parser output exist in the actual source files? A search-based match confirms each extracted table name, column name, transformation name, and join appears literally in the source.
- **Column name verification** -- Same approach: search source files for each extracted column name.
- **Transformation name verification** -- Confirm extracted transformation names match source.
- **Source reference checks** -- Verify that referenced source tables are real and not hallucinated.

**What G2 cannot check:**
- **Business logic correctness** -- There is no deterministic way to verify whether the extracted business logic (from the SQL Interpreter) is semantically correct. You cannot do a simple string search to confirm that a business rule was correctly interpreted. This limitation is acknowledged and addressed later at G4.

**Method:** Primarily deterministic (string matching / search against source files). Currently described as "not a very mature matching system" -- it takes the LLM's reported table names, column names, etc. and searches for those exact strings in the source files.

---

### Stage 3: Pattern Mapper

**Purpose:** Create a SQL-to-Spark translation dictionary.

**How it works:**
- Takes all three parser outputs (combined: all stages, tables, columns, joins, business logic, data types, constraints, etc.)
- Takes the **target reference files** -- Scala and YAML examples previously generated by the Sephora team. These are the "gold standard" for what the output Spark code should look like.
- Makes **one Opus call** to generate a comprehensive translation dictionary mapping SQL patterns to their Spark/Scala equivalents

**Model:** Claude Opus (single call). This is one of the two heavy-lifting LLM stages. Opus is used because:
- Large context window (1M tokens) accommodates all parser outputs plus target examples
- Complex reasoning required to map between SQL idioms and Spark patterns
- Quality of mapping directly impacts all downstream generation

**Performance note:** This stage "takes time" -- it is one of the longest-running stages in the pipeline along with SQL generation.

**Gate (Pattern Mapper Gate):** Visible in LangSmith. Runs five checks including:
1. Character mapping -- is it empty or populated?
2. Source table presence -- are all referenced source tables real (not hallucinated)?
3. Source reference validation
4. Column mapping validation
5. Type mapping validation

---

### Stage 4: SQL/Spark Generator

**Purpose:** Generate the actual Spark SQL code for every transformation stage.

**Model:** Claude Opus (for the generation calls).

**Three-step process:**

#### Step 1: Planning
- Takes the pattern mapping dictionary, the business logic from the SQL Interpreter, and the extracted fields from all parsers
- Plans out how many stages are needed based on the business logic and transformations
- Creates a **dependency graph** that classifies each stage as either:
  - **Independent** -- loads a single table, has aliases or joins that do not share initial conditions with any other table. Can be generated without reference to any other stage's output.
  - **Dependent** -- relies on the output or state of one or more other stages. Must be generated after its dependencies.

**Example:** For a pipeline with 22 total transformations, the planner might identify 5-7 independent stages and 15-17 dependent stages.

#### Step 2: Generate Independent Stages (Parallel)
- Fires off generation calls for all independent stages in parallel
- **Max concurrency: 4** -- Four stages generated simultaneously at most
- If there are 7 independent stages, they process in two batches (4, then 3)

**Why concurrency is limited to 4:** Higher concurrency (7-10 simultaneous calls) was causing **529 errors** (rate limiting) from the Anthropic API. At the time of the call, the workspace quota was 75K tokens per minute for both Opus and Sonnet. Colin submitted quota increase requests (4-5x) to allow higher concurrency for the demo.

#### Step 3: Generate Dependent Stages
- After all independent stages are complete, generates the dependent stages
- These must run after independent stages because they reference independent stage outputs
- Dependent stages have access to the plan and all previously generated independent stages as context

---

### Gate 3 (G3) / Gate 4 (G4): SQL Validation

**Note on naming:** Saurav refers to this as "G3" early in the conversation and "G4" later. Based on the discussion, there appear to be combined deterministic and LLM checks that function as a single gate stage after SQL generation. The key checks are:

**Deterministic checks:**
1. **SQL truncation check** -- Is the generated SQL complete or was it cut off?
2. **Logic soundness** -- Basic structural validation
3. **Stage count verification** -- Compare the number of generated stages against the planned count. Example: if the plan called for 26 stages but only 23 were generated, this flags a failure.
4. **All stages present** -- Every planned stage must have corresponding generated SQL

**LLM check (added later to save tokens):**
- **Business logic accuracy assessment** -- An LLM call evaluates whether the generated SQL faithfully represents the business logic from the source stored procedures
- **Scala schema adherence** -- Checks how closely the generated SQL follows the target Scala schema patterns

**Business logic accuracy threshold: 75%** -- The pipeline requires at least 75% business logic accuracy to proceed. This threshold applies specifically to business logic, not to column consistency, source tables, or other structural elements. Those are handled by the deterministic checks.

**Why this LLM gate was added:** Previously, the pipeline let questionable SQL through to config generation, then to review, where it would get rejected and retry -- burning tokens on config generation, config gate, and validation for SQL that should have been caught earlier. Adding the LLM business logic check at the SQL gate saves those downstream token costs by catching problems before they propagate.

**Failure behavior:** If checks fail (particularly the stage count or business logic threshold), the pipeline can loop back to the SQL/Spark Generator for regeneration.

---

### Stage 5: Config Generation (Three Parallel Agents)

**Purpose:** Generate all deployment configuration artifacts using the validated SQL as context.

Three agents fire in parallel:

1. **Pipeline YAML generator** -- Produces the pipeline configuration YAML
2. **Deployment YAML generator** -- Produces the deployment configuration YAML
3. **Create.HQL generator** -- Produces the HQL (Hive Query Language) DDL file (also referred to as HQL.DTL)

**Context provided:** All three agents receive the previously generated Spark SQL as context, enabling them to produce configurations that are consistent with the generated code.

---

### Config Gate: Configuration Validation

**Deterministic checks:**
- Column names present and correct in deployment configs
- All configs passed correctly between files
- Structural consistency of YAML files

**LLM cross-reference check:**
- Takes the deterministic check results plus the generated XML, deployment YAML, and generated Spark SQL
- Asks the LLM to cross-reference across all generated artifacts and filter/flag inconsistencies
- This catches issues that span multiple generated files where a simple deterministic check on one file would miss the cross-file inconsistency

---

### Stage 6: Validation

**Purpose:** Final deterministic validation pass across all generated artifacts.

**Method:** Deterministic checks only (LLM checks were moved upstream into the gates to catch issues earlier).

**UI presentation:**
- Results displayed as **dropdown boxes** in the dashboard
- If a check scores **100%**, the dropdown is **closed** (collapsed) -- nothing to review
- If a check has **flagged issues**, the dropdown is **open** -- showing exactly what was flagged
- Issues include descriptions that are "very descriptive" so that someone familiar with the databases can understand and act on them in one read
- Syntax highlighting (Highlight.js) is applied to code previews

---

### Stage 7: AI Review

**Purpose:** LLM-powered audit of the validation results. Catches false positives and missed issues.

**Trigger:** Manual -- the user clicks an "AI Review" button in the dashboard.

**What it does:**
- Sends all validation details to an LLM
- Asks the LLM to audit the validation findings
- Checks for **false positives** (things flagged as issues that are actually correct)
- Checks for **missed issues** (real problems the validation did not catch)
- Produces descriptive review findings with highlighting indicating what exactly needs attention

**Why this exists:** Many of the "errors" surfaced by validation are actually false positives (Saurav noted seeing this frequently across 40-50 runs). The AI review provides a second opinion layer before human intervention.

---

### Stage 8: Human Review and Action

At this point, the user reviews the AI Review output and validation results, then chooses one of three paths:

#### Path A: Auto-Fix

**Concept:** "Like Claude Code for the pipeline."

**How it works:**
- The auto-fix agent receives the generated SQL file, the XML source, Scala references, and all other artifacts **as files**
- It has **tools to read files** and **tools to edit files** (analogous to Claude Code's file reading and editing capabilities)
- Based on the AI Review findings (e.g., 2 bugs and 1 advisory), it opens the SQL file, navigates to the specific line numbers, and makes **surgical edits** -- fixing only the specific issues rather than regenerating entire files
- The chat thread is preserved, so the agent has context of the entire generation history, previous validation results, and the specific rejection reasons

**After auto-fix completes:**
- Validation runs again automatically on the edited files
- The user returns to the review screen with updated results
- The cycle can repeat (fix, validate, review) as many times as needed

**When to use:** Best for small issues in an otherwise correct generation -- e.g., one wrong table name, one incorrect WHERE condition, one null handling error out of 25-26 total transformations.

#### Path B: Reject and Retry (Full Regeneration)

**How it works:**
- Goes back to the **SQL/Spark Generator** stage
- Runs through all subsequent nodes again: SQL generation, SQL gate, config generation, config gate, validation
- This is a full regeneration, not a surgical edit

**The rejection context is preserved:** The retry operates in a chat-fashion backend. Each node maintains a chat thread that includes:
- Previous generation output
- The validation findings
- The rejection reason / verdict (why it was rejected, which items were marked false positive)
- All of this feeds back into the next generation attempt so the model knows what went wrong

**UI caveat:** The DAG visualization on the frontend does not correctly light up the retry stages (the nodes that re-execute do not animate properly on retry). The execution log works correctly, and the backend processes correctly -- it is only a visual issue. For the demo, Colin will use auto-fix instead of reject-and-retry.

**When to use:** When the issues are too fundamental for surgical edits -- the generation needs a fresh attempt with the feedback incorporated.

#### Path C: Approve

**What happens on approval:**
- The generated artifacts are finalized
- Any patterns that were flagged, corrected, or confirmed during review get **added to a JSON knowledge base**
- This knowledge base entry includes: the pattern, how it should be handled (e.g., null handling approach, WHERE clause structure, CASE/WHEN patterns, join/view treatment)

---

### Stage 9: Knowledge Base Learning Loop

**Purpose:** The system learns from each run to improve future generations.

**Mechanism:**
- On approval, the approved patterns (including any corrections made during review/fix) are written as JSON objects to a knowledge base file
- On future SQL generation runs, the SQL/Spark Generator reads this knowledge base
- If a previously approved pattern applies, the generator follows the approved approach
- Patterns may take several runs to "stick" -- after 3-4-5 approval cycles with the same correction, the generator reliably produces the correct pattern on first try

**Effect:** The pipeline improves over time. Early runs may require more review and fixing. Later runs benefit from accumulated approved patterns and produce correct output more often on the first attempt.

---

### Stage 10: Download

**Current state:**
- **Individual file downloads:** Working correctly. Each generated artifact (SQL, YAML, HQL) can be downloaded separately.
- **Zip download (all files):** Broken at the time of this call. Not yet functional.

---

## Model Selection Strategy

| Model | Used For | Reason |
|-------|----------|--------|
| **Claude Opus** | Pattern Mapper, SQL/Spark Generator | Heavy tasks requiring deep reasoning, large context, and complex code generation. Opus provides 1M token context window for handling all parser outputs, target examples, and business logic simultaneously. |
| **Claude Sonnet** | Lighter tasks (gate LLM checks, AI review, config generation, auto-fix) | Faster and more cost-effective for tasks that do not require the same depth of reasoning. Sufficient for validation, review, and configuration generation. |

---

## Concurrency and Rate Limiting

- **Max concurrency: 4** for parallel stage generation in the SQL/Spark Generator
- Higher concurrency (7-10) caused **529 errors** (HTTP rate limiting) from the Anthropic API
- Workspace quota at time of call: **75K tokens/minute** for both Opus and Sonnet
- Colin submitted quota increase requests for both models (targeting 4-5x the current quota)
- If quota is increased, concurrency could be raised to 8-9 for the demo to speed up parallel processing
- The three parallel parsers and three parallel config generators also contribute to concurrent API load

---

## Parallel Execution Points (Summary)

1. **Three parsers** (DataStage, SQL Interpreter, DDL) -- all fire simultaneously after G1
2. **Within each parser** -- deterministic extraction and LLM synthesis run in parallel (so up to 6-7 concurrent API calls during parsing: 3 parsers x 2 sub-processes, though deterministic steps do not use the API)
3. **Independent SQL stages** -- up to 4 at a time during SQL generation
4. **Three config generators** -- pipeline YAML, deployment YAML, create.HQL all fire simultaneously

---

## Retry and Loop-Back Mechanisms (Summary)

| Gate/Stage | Failure Loops Back To | What Happens |
|------------|----------------------|--------------|
| G1 | Orchestrator | Reloads files, re-resolves pipeline selection |
| G2 | Parsers (implied) | Re-extraction if hallucinated content detected |
| G3/G4 (SQL Gate) | SQL/Spark Generator | Regeneration with feedback from gate findings |
| Config Gate | Config Generation | Re-generation of config artifacts |
| Human Review (Reject) | SQL/Spark Generator | Full regeneration through all subsequent nodes |
| Human Review (Auto-Fix) | In-place edit | Surgical edit, then re-validation only |

---

## Deterministic vs. LLM Checks (Summary by Gate)

| Gate | Deterministic Checks | LLM Checks |
|------|---------------------|-------------|
| **G1** | All artifacts loaded, target examples present, correct pipeline selected, run ID generated | None |
| **G2** | Table names match source files, column names found in source, transformation names verified | None (business logic cannot be verified deterministically) |
| **Pattern Mapper Gate** | Character mapping populated, source table presence, column mapping, type mapping, source references | None explicitly stated |
| **G3/G4 (SQL Gate)** | SQL not truncated, stage count matches plan, all stages present | Business logic accuracy (75% threshold), Scala schema adherence |
| **Config Gate** | Column names present, configs passed correctly | Cross-reference check across generated SQL, YAML, and HQL |
| **Validation** | Basic deterministic validations (moved LLM checks upstream to gates) | None (LLM checks moved to gates) |
| **AI Review** | None | Full audit of validation findings, false positive detection, missed issue detection |

---

## LangSmith Integration

- LangSmith is used for **tracing only** (not for development via Playground/Studio, due to potential licensing costs)
- Provides a **waterfall view** showing every API call, node execution, and parallel process timing
- **Blue nodes** in LangSmith = LangGraph stage-level outputs (pattern mapper, SQL generator, etc.)
- **Orange nodes** = individual LLM-level API calls
- Each node's input and output state is visible, including the full LangGraph state object at each point
- Not real-time -- updates appear within 1-2 minutes of actual execution (execution log in the dashboard is the real-time view)
- The full LangGraph state is a JSON object that builds throughout the pipeline; each node fills in its portion, and any downstream node can access any upstream field

---

## Pipeline Timing and Human-in-the-Loop

- The total pipeline duration displayed in the dashboard **includes human review time** (e.g., if the user spends 10-20 minutes reviewing before approving, that counts toward total duration)
- It also includes retry time
- The longest-running LLM stages are the Pattern Mapper and the SQL/Spark Generator
- Parsing stages are relatively fast
- Config generation is moderate

---

## Step Count in the Pipeline

- The standard pipeline run (no retries) has approximately **15 steps** through to human approval
- Reject-and-retry adds 3-4 more steps per retry cycle (SQL generation, SQL gate, config generation, config gate)
- Multiple retries can push the step count past 20 (observed: 19, 20, 22 steps in LangSmith)

---

## Known Issues at Time of Call

1. **Zip download broken** -- Individual file downloads work; zip does not
2. **DAG visualization on retry** -- When using reject-and-retry, the DAG node lighting does not correctly show which stages are re-executing (backend works correctly; visual-only issue)
3. **Pipeline runs table missing on Colin's local** -- Saurav's migration did not include auto-creation of the pipeline_runs table; Saurav is adding a check to auto-create if not present
4. **Auto-fix text rendering** -- Advisory/bug detail text was not displaying in the auto-fix expanded view (rendering issue; data is present in backend)
5. **Run duration display** -- Includes human idle time, making it appear longer than actual processing time

---

## Demo Flow (Recommended)

Based on this call, the planned demo sequence is:

1. Load demo files (9 files, hard-coded for the demo)
2. Start pipeline
3. Watch execution log with live spinner/timer showing each agent's progress
4. Walk through gate checks as they pass
5. Review generated SQL with syntax highlighting
6. Click AI Review to show the audit capability
7. Click Auto-Fix (not reject-and-retry, to avoid the DAG visualization issue)
8. Show the auto-fix results and updated validation
9. Approve
10. Download individual files
11. Show LangSmith waterfall view for technical audience (parallel execution, gate details, input/output states)
12. Show previous runs list (pre-populated with a few hard-coded entries: some passed, one pending, one failed)
