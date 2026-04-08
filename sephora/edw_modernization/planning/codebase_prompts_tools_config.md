# Sephora EDW Demo Codebase: Prompts, Tools, and Configuration Analysis

**Date:** 2026-04-02
**Codebase:** `sephora_edw-1/`
**Purpose:** Multi-agent ETL migration system that converts IBM DataStage / SQL Server pipelines to Databricks Spark SQL

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Agent Prompts](#agent-prompts)
3. [Tool Modules](#tool-modules)
4. [Configuration](#configuration)
5. [Pipeline Flow Summary](#pipeline-flow-summary)

---

## Architecture Overview

The system is a LangChain/LangGraph-based multi-agent pipeline. Each agent has a dedicated system prompt (in `prompts/`) and a set of tools (in `src/etl_agent/tools/`). Agents communicate through shared state and a scratchpad mechanism. The pipeline reads legacy DataStage XML exports, SQL Server stored procedures, DDLs, and views, then generates equivalent Spark SQL, HQL DDLs, YAML pipeline configs, and deployment configs for Databricks.

Key design principles:
- **Side-channel content storage**: Large files (DataStage XML can be 1.4M+ characters) are stored in Python dictionaries, never passed directly to LLM context. Agents see only metadata summaries.
- **Deterministic + LLM hybrid**: Python tools handle structural parsing (sqlglot for SQL, xml.etree for XML). LLMs handle semantic interpretation (business rules, pattern mapping, code generation).
- **Scratchpad for agent memory**: Each agent writes incremental findings to a namespaced scratchpad, then reads them back before final synthesis. This prevents context window degradation across many tool calls.
- **Structured tool results**: Every tool returns a consistent `{status, data, detail, can_retry, suggestion}` envelope so agents get actionable error feedback.

---

## Agent Prompts

### 1. Orchestrator (`orchestrator.txt`)

**Role:** Pipeline entry point. Discovers, loads, and classifies all source artifacts, then identifies which pipeline to build.

**Workflow:**
- Calls `load_all_artifacts` with three directories (source, schema, target) in a single batch call
- Examines target subdirectories to identify the primary pipeline (e.g., `inventory_periodic_daily/`, `stock_continuity_all_sku/`)
- Ends response with `PIPELINE: <subdirectory_name>`

**Key constraint:** Must use the batch `load_all_artifacts` tool rather than individual file loads, to minimize tool call overhead.

---

### 2. DataStage Parser (`datastage_parser.txt`)

**Role:** Analyzes IBM InfoSphere DataStage XML job exports. Extracts source tables, target tables, column mappings, business rules, and temporal logic.

**Workflow:**
1. `get_job_overview` -- understand job structure
2. `get_embedded_sql` -- find SQL in ODBC/transformer properties. If SQL found, classify as "SQL-heavy" job; otherwise "visual ETL" requiring stage-by-stage inspection
3. `get_column_definitions` -- extract the data model
4. `list_stages` + `read_stage` on key stages (ODBC for connections, Transformers for logic)
5. `search_xml` for specific patterns
6. Uses `write_notes` / `read_notes` throughout to preserve findings

**Output:** JSON with `source_tables`, `target_table`, `column_mappings`, `subqueries`, `business_rules`, `temporal_logic`, `key_findings`.

**Key constraint:** Must use tools to explore. Must not fabricate data. Must list ALL columns, not a subset.

---

### 3. SQL Interpreter (`sql_interpreter.txt`)

**Role:** Extracts business rules from SQL Server stored procedures and views for a financial reporting pipeline.

**Extracts per rule:** `rule_name`, `description`, `logic`, `sql_pattern`, `source_lines`, `dependencies`, `temporal_logic`.

**Domain-specific focus areas:**
- Flag calculations (Active_Store_Flag, Store_With_Inv_Flag, Store_With_Sales_Flag)
- SKU_Behavior_Code = '9' threshold differences (>= 1 vs >= 2)
- Dotcom DC handling (Is_Dotcom, Is_DmgDC, DC_Name)
- Temp table patterns (#TEMP_IP_DAILY_ACTIVE_FLAG)
- 7-day lookback windows for sales verification
- Dual DC / commingled location overrides

**Output:** JSON with `business_rules`, `joins`, `temp_tables`, `transformations`.

---

### 4. DDL Parser (`ddl_parser.txt`)

**Role:** Parses SQL Server DDLs, Databricks table schemas, and view definitions to extract complete schema information.

**Extracts:** `table_name`, `columns` (name, full type with precision, nullable, is_key), `primary_key`, `constraints`. For views: `base_table`, `joins`, `computed_columns`.

**Key constraint:** Financial data precision is critical. Must capture exact decimal precision (e.g., `decimal(13,3)` not `decimal(13,0)`), exact column counts, nullable vs NOT NULL, and char vs varchar vs string distinctions.

**Output:** JSON.

---

### 5. Pattern Mapper (`pattern_mapper.txt`)

**Role:** Maps legacy SQL Server / DataStage patterns to their Databricks / Spark equivalents. Acts as the translation dictionary between old and new platforms.

**Standard mappings:**
1. Surrogate keys (Date_SK, Location_SK) to business keys (Business_Date, Location_Number)
2. SQL Server types to Databricks types
3. Temp tables (#temp) to intermediate DataFrame variables
4. EXISTS subqueries to joins with filters
5. CASE WHEN flag logic to `.withColumn()` + `when().otherwise()`
6. GETDATE() to `current_date()` / `current_timestamp()`
7. NOLOCK hints dropped
8. SQL Server CAST to Spark SQL CAST

**Scala-specific patterns extracted from target reference application:**
9. Helper functions (notNullColumn, isNullColumn) -- exact implementation + SQL equivalent
10. Collection patterns (.isin() with collected values) -- collection types noted
11. NULL comparison semantics -- concrete SQL guards for every NULL-prone pattern
12. UNION ALL type handling
13. `.dropDuplicates()` keys
14. Missing `.otherwise()` in `.when()` chains

**Output:** JSON with `type_mappings`, `sql_pattern_mappings`, `scala_patterns` (with explicit `null_behavior` field), `source_file_manifest`, `column_renames`, `key_transformations`.

---

### 6. Spark SQL Planner (`spark_sql_planner.txt`)

**Role:** Analyzes a reference Scala Spark application and produces a structured dependency graph of transformation stages. Does NOT generate SQL -- only plans.

**Output format per stage:**
```
Stage N (viewName) -- INDEPENDENT (source_table1, source_table2)
Stage N (viewName) -- DEPENDENT on Stages X,Y (reads from viewX, viewY)
```

**Rules:**
- Every DataFrame transformation assigned to a variable or temp view is a stage
- INDEPENDENT stages read only from source tables, not from generated views
- DEPENDENT stages read from any view created by a prior stage
- Must include exact Scala code snippets for each stage
- Must copy ALL CASE/WHEN value mappings verbatim (no summarization)
- Final stage marked with "(FINAL)"

---

### 7. Spark SQL Generator (`spark_sql_generator.txt`)

**Role:** Generates Spark SQL implementing the transformation logic from the reference Scala application and source stored procedures.

**Two-phase operation:**
1. **Planning**: Receives full Scala app, identifies all transformation stages with code snippets
2. **Per-stage generation**: Receives one stage at a time, generates corresponding `CREATE OR REPLACE TEMP VIEW`

**Critical accuracy rules:**
- Type casts must match exact precision from target HQL DDL (e.g., `DECIMAL(17,3)`)
- Only add COALESCE, ELSE, or NULL checks where the source Scala/stored procedure explicitly has them -- no invented defensive patterns
- CASE/WHEN value mappings copied verbatim from Scala
- Goal is **behavioral equivalence** with source, not "better" SQL
- NULL handling: IS NULL / IS NOT NULL only, never `= 'null'` or `= NULL`
- NOT IN subqueries: add `WHERE col IS NOT NULL` inside subquery when column can contain NULLs
- Uses pattern mapper's `scala_patterns` for helper function translations

---

### 8. Spark SQL Stage Generator (`spark_sql_stage_generator.txt`)

**Role:** Generates ONE focused `CREATE OR REPLACE TEMP VIEW` statement at a time, given a specific stage's context.

**Receives:** Stage name, dependencies, Scala code snippet, dependency SQL, source schemas, target HQL columns.

**Key differences from spark_sql_generator:**
- More prescriptive about defensive patterns (COALESCE on nullable join columns, ELSE clauses on CASE, full NULL check patterns)
- Specifies the exact notNullColumn() translation: `col IS NOT NULL AND TRIM(CAST(col AS STRING)) != '' AND CAST(col AS STRING) != 'null'`
- Embeds domain-specific flag/threshold logic directly: SKU_Behavior_Code = '9' uses >= 1, all others use >= 2
- For FINAL stage: SELECT must produce EXACTLY the columns listed in target HQL DDL

**Output:** Raw SQL only (no markdown fences, no explanations).

---

### 9. Config Generator (`config_generator.txt`)

**Role:** Produces configuration files by copying target templates exactly. Generates 3 files separated by `--- FILE: filename ---`.

**Rules:**
- Copy ALL token names (`#{...}#`) from targets exactly
- Copy ALL column names and types from target HQL DDL exactly
- Copy deployment settings (num_workers, main_class_name) from target exactly
- Copy pipeline YAML structure (sourceFiles, jobName, paths) from target exactly
- Only change values where generated Spark SQL or source schemas require different values
- Target is ground truth; when in doubt, copy from target

---

### 10. Schema Validator (`schema_validator.txt`)

**Role:** Semantic validation of generated output against target examples. Deterministic validators (sqlglot syntax, column name matching, type comparison, YAML structure) run separately; this agent handles what code cannot judge.

**5 semantic checks:**
1. **yaml_structure**: Token placeholder names match target; key hierarchy correct
2. **column_type_consistency**: HQL DDL types match Spark SQL CAST operations across ALL columns
3. **column_existence**: All column names in SQL trace back to source DDL/DataStage definitions (detects hallucinated columns)
4. **deployment_validation**: Token names, init_scripts paths, library versions, cluster config
5. **business_logic_preservation** (most critical):
   - Flag/threshold logic (SKU_Behavior_Code = '9' threshold)
   - CASE/WHEN edge cases (missing ELSE = NULL)
   - NULL handling correctness
   - Join condition fidelity
   - Aggregation accuracy
   - Date handling

**Output:** JSON with per-check `{status, score, detail, findings[]}`. Scores: 1.0 = all ok, 0.9+ = warnings only, < 0.8 = multiple errors.

---

### 11. SQL Quality Gate (`gate_sql_llm.txt`)

**Role:** Quality gate verifying generated Spark SQL against the reference Scala application. Focuses on semantic correctness after deterministic checks pass.

**Two checks:** `column_existence` and `business_logic_preservation`.

**Three-phase analysis:**
1. **Scratchpad phase**: List ALL discrepancies view-by-view (SQL code, Scala code, what seems different)
2. **Self-review phase**: Classify each as REAL BUG (specific input produces wrong output), FALSE POSITIVE (different syntax, same behavior), or UNCERTAIN
3. **Scoring phase**: Uses dependency graph. Deductions cascade -- a REAL BUG in a stage with 5+ dependents costs more than a standalone error.

**Scoring model:**
- REAL BUG with 5+ dependents: deduct 1.0 (stage) + 0.5 per dependent
- REAL BUG with 1-4 dependents: deduct 1.0 (stage) + 0.25 per dependent
- REAL BUG standalone: deduct 1.0
- UNCERTAIN: deduct 0.2 each
- FALSE POSITIVE: zero deduction

**Gate verdict:** "fail" ONLY if any finding is a confirmed REAL BUG (breaks_output=true). Warnings alone do not fail the gate.

**Output:** JSON with `scratchpad[]` (showing reasoning), `gate_verdict`, `should_retry`, `checks{}`, `issues[]`.

---

### 12. Config Quality Gate (`gate_config_llm.txt`)

**Role:** Quality gate for YAML configs, deployment config, and HQL DDL against target examples.

**Three checks:**
1. **yaml_structure**: Token placeholder names, key hierarchy, sourceFiles entries
2. **column_type_consistency**: Cross-reference HQL DDL types with Spark SQL CAST operations for ALL columns
3. **deployment_validation**: Token names, init_scripts, library versions, cluster config

**Output:** JSON with `gate_verdict`, `should_retry`, `checks{}`, `issues[]`.

---

## Tool Modules

### 1. `artifact_tools.py` -- Artifact Discovery and Loading

**Purpose:** Orchestrator's toolset for discovering, reading, classifying, and storing all pipeline artifacts.

**Side-channel architecture:** File content is stored in `_artifact_store` (a Python dict), never returned to the LLM. The LLM only sees metadata (name, type, size, validity). This prevents a 1.3M+ character DataStage XML from consuming the orchestrator's context window.

**Classification logic** (`_classify_content`):
- Binary file detection (by extension and heuristic null-byte analysis)
- XML validation (DataStage XML, .dsx files)
- SQL keyword detection and type classification: stored_procedure, ddl, view, sql_unknown, schema

**Local backend tools:**
- `list_files(directory)` -- list files in a single directory
- `list_files_recursive(directory)` -- recursive file listing
- `load_and_classify(file_path)` -- read, classify, store one file
- `load_all_artifacts(directories)` -- batch: recursively discover, read, classify all files across multiple directories in one call

**Blob backend tools:**
- `list_blobs(container, prefix)` -- list Azure Blob Storage blobs
- `load_and_classify_blob(container, blob_path)` -- read and classify a blob

**Tool selection:** `get_orchestrator_tools()` returns blob tools if Azure credentials are configured, local tools otherwise.

---

### 2. `xml_parser.py` -- DataStage XML Pre-processing

**Purpose:** Python-native (no LLM) structural decomposition of large DataStage XML files. Handles the Sephora DSExport format.

**DataStage XML structure:**
```
<DSExport>
  <Header> export metadata
  <Job Identifier="...">
    <Record Type="JobDefn"> job definition
    <Record Type="ContainerView"> visual layout
    <Record Type="ODBCStage"|"TransformerStage"|...> stages
    <Record Type="ODBCInput"|"TrxOutput"|...> stage ports
    <Record Type="Annotation"> comments
```

**Recognized stage types (20):** ODBCStage, TransformerStage, PxSequentialFile, PxDataSet, PxLookup, PxJoin, PxFilter, PxFunnel, PxAggregator, PxSort, PxModify, PxCopy, PxRemoveDuplicates, PxRowGenerator, PxHead, PxTail, PxPeek, CTransformerStage, PxSurrogateKeyGenerator, PxChangeApplyComponent, PxChangeCapture.

**Functions:**
- `extract_job_metadata(xml_content)` -- job name, type, parameters, connections, stage list
- `chunk_stages(xml_content)` -- split XML into per-stage chunks for LLM processing
- `chunk_with_ports(xml_content)` -- split into per-stage chunks INCLUDING associated I/O port records (grouped by Identifier prefix)
- `extract_embedded_sql(xml_content)` -- find SQL in known properties (SqlInsert, SqlBefore, SqlAfter, SqlSelect, etc.) and heuristically in any long text containing SQL keywords
- `extract_column_definitions(xml_content)` -- extract column metadata (name, sql_type, precision, scale, nullable, derivation) from port records

---

### 3. `sql_tools.py` -- SQL Analysis Tools

**Purpose:** Deterministic SQL parsing using sqlglot. LLM adds business interpretation on top.

**Tools:**
- `parse_sql_structure(sql, dialect)` -- extract tables, joins, CTEs, temp tables, statement types from any SQL. Default dialect: tsql
- `parse_ddl(sql, dialect)` -- parse CREATE TABLE / CREATE VIEW into structured schema with columns, types, precision, nullable, primary keys
- `validate_sql_syntax(sql, dialect)` -- syntax check via sqlglot parse. Default dialect: spark
- `transpile_sql(sql, source_dialect, target_dialect)` -- convert SQL between dialects (default: tsql to spark)

**Tool sets for specific agents:**
- `get_sql_interpreter_tools()` -- parse_sql_structure, transpile_sql, + scratchpad
- `get_ddl_parser_tools()` -- parse_ddl, parse_sql_structure, + scratchpad
- `get_spark_sql_tools()` -- validate_sql_syntax, parse_sql_structure, transpile_sql, + scratchpad

---

### 4. `datastage_tools.py` -- DataStage XML Exploration Tools

**Purpose:** Agent-facing tools for the DataStage Parser agent. XML is pre-loaded into a side-channel store (`_ds_store`) by the parser node before the agent starts.

**Tools:**
- `get_job_overview()` -- high-level job metadata (name, type, parameters, stages). Call first.
- `get_embedded_sql()` -- extract SQL fragments; returns previews (first 500 chars each), stores full SQL for downstream
- `get_column_definitions()` -- column metadata grouped by port (name, sql_type, precision, nullable)
- `list_stages()` -- list all stages with types and XML sizes
- `read_stage(stage_name)` -- read full XML for a specific stage including I/O ports
- `search_xml(pattern)` -- case-insensitive text search across all Property elements; returns match context

All tools return metadata/summaries to the LLM. Full data is stored in `_ds_store` for downstream agents.

---

### 5. `scratchpad.py` -- Shared Agent Scratchpad

**Purpose:** Per-agent namespaced scratchpad for accumulating findings during multi-step exploration. Prevents context window degradation.

**Architecture:** Global dictionary `_scratchpads: {agent_name: {section: content}}`. Each agent gets isolated storage.

**Tools (created per agent via `make_scratchpad_tools(agent_name)`):**
- `write_notes(section, content)` -- write findings under a named section (e.g., "source_tables", "business_rules")
- `read_notes()` -- read all sections from own scratchpad (call before final synthesis)
- `read_upstream_notes(upstream_agent)` -- read another agent's scratchpad for cross-agent context

**Python-side access:**
- `get_scratchpad(agent_name)` -- read an agent's notes from orchestrator code
- `get_all_scratchpads()` -- read all agent notes
- `clear_scratchpad(agent_name)` / `clear_all_scratchpads()` -- reset

---

### 6. `blob_storage.py` -- Azure Blob Storage Operations

**Purpose:** Read/write/list operations for Azure Blob Storage across 4 containers.

**Containers:**
| Container | Purpose |
|---|---|
| `source-systems` | Mock Cognos reports (demo showcase) |
| `pipeline-input` | Source artifacts the agent reads |
| `target-examples` | Reference outputs for validation |
| `pipeline-output` | Generated files (Spark SQL, YAML, HQL) |

**Functions:**
- `read_blob(container, blob_path)` -- read blob as UTF-8 text
- `write_blob(container, blob_path, content)` -- write text to blob (overwrite)
- `list_blobs(container, prefix)` -- list blob names with optional prefix filter
- `write_run_output(run_id, filename, content)` -- write to `pipeline-output/{run_id}/`
- `write_audit_package(run_id, manifest, outputs)` -- write complete audit package (manifest.json + all output files)
- `read_local_file(file_path)` -- local filesystem fallback for dev/demo mode

**Auth:** Lazy-initialized BlobServiceClient; supports connection string or account name/key.

---

### 7. `result.py` -- Structured Tool Result Envelope

**Purpose:** Consistent return format for all tools so agents get actionable feedback.

**Functions:**
- `ok(data, detail)` -- success: `{status: "ok", data: ..., detail: "...", can_retry: false}`
- `fail(error, can_retry, suggestion)` -- failure: `{status: "error", data: null, detail: "...", can_retry: true/false, suggestion: "..."}`

Every tool in the system returns one of these two envelopes.

---

## Configuration

### `config.py` -- Application Settings

Uses `pydantic_settings.BaseSettings` with `.env` file loading.

**Settings classes:**

| Class | Env Prefix | Key Settings |
|---|---|---|
| `AzureAISettings` | `AZURE_AI_` | `endpoint`, `api_key` (for Claude models via Azure AI Foundry) |
| `AzureBlobSettings` | `AZURE_STORAGE_` | `account_name`, `account_key`, `connection_string`, container names (`source-systems`, `pipeline-input`, `target-examples`, `pipeline-output`) |
| `Settings` (top-level) | none | `model_sonnet` (claude-sonnet-4-6), `model_opus` (claude-opus-4-6), `temperature` (0.0), `max_retries` (2), `auto_approve_threshold` (3), `checkpoint_postgres_uri` |

---

### `pipeline_config.py` -- Pipeline Configuration Loader

Reads from `pipeline_config.yaml` (or falls back to hardcoded defaults). Provides dot-notation access via `_DotDict`. Also loads prompts from the `prompts/` directory.

**Configuration sections (from fallback defaults):**

**Models:**
- Sonnet: `claude-sonnet-4-6`
- Opus: `claude-opus-4-6`
- Temperature: 0.0
- Max tokens: 16384

**Agent-to-model assignments:**

| Agent | Model |
|---|---|
| orchestrator | Sonnet |
| datastage_parser | Opus |
| sql_interpreter | Sonnet |
| ddl_parser | Sonnet |
| pattern_mapper | Opus |
| spark_sql_generator_plan | Opus |
| spark_sql_generator_independent | Sonnet |
| spark_sql_generator_dependent | Opus |
| config_generator | Sonnet |
| schema_validator | Sonnet |

Design rationale: Opus (more capable, more expensive) is used for the hardest tasks -- DataStage XML analysis, pattern mapping, planning, and dependent stage generation. Sonnet handles more formulaic work -- DDL parsing, SQL interpretation, independent stages, config generation, validation.

**Concurrency:**

| Setting | Value |
|---|---|
| graph_max_concurrency | 4 |
| ddl_parser_batch | 4 |
| sql_interpreter_batch | 4 |
| config_generator_batch | 3 |

**Retry policy:**

| Setting | Value |
|---|---|
| max_gate_retries | 2 |
| llm_max_attempts | 5 |
| llm_initial_interval | 2.0s |
| llm_backoff_factor | 2.0 |
| llm_max_interval | 60.0s |
| per_stage_retries | 3 |

**Context limits (character budgets to prevent context overflow):**

| Setting | Chars |
|---|---|
| mapping_text | 8,000 |
| rules_text | 4,000 |
| schemas_text | 3,000 |
| ddl_llm_text | 2,000 |
| source_corpus_per_artifact | 20,000 |
| datastage_sql_preview | 2,000 |

**Pipeline settings:**
- `auto_approve_threshold`: 1
- `datastage_quick_parse_threshold`: 200,000 chars (XMLs below this threshold use a faster parse path)

**Prompt loading:** `get_prompt(agent_name)` reads from `prompts/{agent_name}.txt`, falling back to inline Python constants.

---

### `pipeline_config.yaml`, `pyproject.toml`, `docker-compose.yml`

**Note:** These three files could not be read due to filesystem permission restrictions (they reside in the `sephora_edw-1` repo, outside the current working directory's allowed read scope). The `pipeline_config.py` fallback defaults documented above mirror the expected YAML structure. The following is inferred from configuration references within the codebase:

**`pipeline_config.yaml`** -- Expected to contain the same structure as the fallback defaults in `pipeline_config.py`: models, agent_models, concurrency, retry, context_limits, and pipeline sections.

**`pyproject.toml`** -- Project metadata and dependencies. Based on imports observed in the codebase, key dependencies include:
- `langchain-core` (tool decorators, agent framework)
- `langgraph` (graph-based agent orchestration, implied by pipeline architecture)
- `pydantic-settings` (configuration management)
- `python-dotenv` (env file loading)
- `sqlglot` (SQL parsing, transpilation, validation)
- `pyyaml` (YAML config loading)
- `azure-storage-blob` (Azure Blob Storage client)
- Anthropic Claude models accessed via Azure AI Foundry endpoint

**`docker-compose.yml`** -- Based on the `checkpoint_postgres_uri` setting in `config.py`, the Docker setup likely includes:
- A PostgreSQL service for LangGraph checkpoint persistence (conversation state, retry tracking)
- Possibly the application service itself
- Possibly an Azure Storage emulator (Azurite) for local development

---

## Pipeline Flow Summary

```
1. ORCHESTRATOR
   |-- Discovers and classifies all artifacts (XML, SQL, DDL, schemas, targets)
   |-- Identifies the target pipeline (e.g., inventory_periodic_daily)
   |
   v
2. PARALLEL PARSING PHASE
   |-- DATASTAGE PARSER --> Analyzes DataStage XML job
   |-- SQL INTERPRETER  --> Extracts business rules from stored procs/views
   |-- DDL PARSER       --> Extracts schemas from all DDLs (batched, 4 concurrent)
   |
   v
3. PATTERN MAPPER
   |-- Maps legacy patterns to Spark equivalents
   |-- Extracts Scala-specific patterns from target reference app
   |-- Produces translation dictionary for downstream generators
   |
   v
4. SPARK SQL PLANNER
   |-- Analyzes reference Scala app
   |-- Produces dependency graph of transformation stages
   |-- Classifies each as INDEPENDENT or DEPENDENT
   |
   v
5. SPARK SQL GENERATION (per-stage, respecting dependencies)
   |-- INDEPENDENT stages: Generated in parallel (Sonnet)
   |-- DEPENDENT stages: Generated sequentially (Opus)
   |-- Each produces one CREATE OR REPLACE TEMP VIEW
   |
   v
6. SQL QUALITY GATE (gate_sql_llm)
   |-- Three-phase analysis: scratchpad, self-review, scoring
   |-- PASS --> continue
   |-- FAIL --> retry generation (up to max_gate_retries)
   |
   v
7. CONFIG GENERATOR
   |-- Produces 3 files: pipeline YAML, deployment YAML, HQL DDL
   |-- Copies target template structure exactly
   |
   v
8. CONFIG QUALITY GATE (gate_config_llm)
   |-- Validates YAML structure, column types, deployment config
   |-- PASS --> continue
   |-- FAIL --> retry config generation
   |
   v
9. SCHEMA VALIDATOR (final semantic validation)
   |-- 5 checks: yaml_structure, column_type_consistency, column_existence,
   |   deployment_validation, business_logic_preservation
   |-- Produces per-check scores and findings
   |
   v
10. OUTPUT (written to pipeline-output/ or Azure Blob Storage)
    |-- spark_sql.sql
    |-- pipeline_config.yaml
    |-- deployment_config.yaml
    |-- target.hql
    |-- manifest.json (audit package)
```

**Key architectural decisions:**

1. **Two quality gates** -- SQL gate focuses on behavioral equivalence between Scala and generated SQL. Config gate focuses on structural correctness of YAML/HQL against templates.

2. **Dependency-aware generation** -- The planner creates a DAG. Independent stages (reading only from source tables) generate in parallel with Sonnet. Dependent stages (reading from prior generated views) generate sequentially with Opus to ensure correctness.

3. **Target-driven generation** -- The system uses existing target Scala/Spark applications as reference implementations, not just source DataStage/SQL Server artifacts. This is a "translate the working Scala app to SQL" approach, not a "reverse-engineer DataStage" approach.

4. **Context management** -- Character budgets prevent any single artifact from consuming the LLM's context. Side-channel stores keep raw content out of agent messages. Scratchpads let agents accumulate findings without re-reading long tool outputs.

5. **Financial precision emphasis** -- Multiple prompts stress exact decimal precision (e.g., `decimal(17,3)` not `decimal(17,2)`), exact flag thresholds, and exact COALESCE defaults. This is inventory/financial reporting data where precision differences break reconciliation.
