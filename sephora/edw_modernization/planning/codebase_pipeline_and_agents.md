# Sephora EDW Migration Pipeline: Codebase Analysis

**Codebase:** `/home/cmoore/programming/sephora_edw-1/src/etl_agent/`
**Date:** 2026-04-02
**Scope:** Complete graph structure, all agents, state schema, validation/gate logic, retry mechanisms, and end-to-end flow.

---

## 1. Architecture Overview

The pipeline is a **LangGraph StateGraph** implementing a Producer-Gate-Producer pattern. Each "producer" node (an LLM-calling agent) is followed by a "gate" node (a deterministic validator at zero LLM cost). Gates route forward on pass or back to the producer on failure, with a configurable retry cap (`MAX_GATE_RETRIES` from `pipeline_config`).

All LLM calls go through **Claude on Azure AI Foundry** via `ChatAnthropic` with an Azure base URL. Model assignments (Sonnet vs. Opus) are driven entirely by `pipeline_config.yaml` -- nothing is hardcoded in the model layer.

Key design principles:
- Deterministic extraction first (sqlglot, regex, XML parsing), LLM synthesis second
- Parallel execution where possible (3 parsers fan out; batch LLM calls within agents)
- Source grounding checks to catch hallucinated table/column names
- Gate LLM checks (semantic validation) run only after deterministic checks pass
- Human-in-the-loop via LangGraph `interrupt`, with auto-approve after N consecutive approvals

---

## 2. Graph Node/Edge Structure

**File:** `graph.py` -- `build_graph()` function (line 180)

### 2.1 Complete Node Layout

```
START
  --> orchestrator            [LLM, retry policy]
  --> gate_orchestrator       [deterministic]
  --> fan_out_parsers         [no-op passthrough]
  --> datastage_parser        [LLM, retry policy]  \
  --> sql_interpreter         [LLM, retry policy]   } parallel (fan-out)
  --> ddl_parser              [LLM, retry policy]  /
  --> gate_parsers            [deterministic, waits for all 3]
  --> pattern_mapper          [LLM, retry policy]
  --> gate_mapper             [deterministic]
  --> spark_sql_generator     [LLM, retry policy]
  --> gate_sql                [deterministic + LLM]
  --> config_generator        [LLM, retry policy]
  --> gate_config             [deterministic + LLM]
  --> schema_validator        [deterministic only -- zero LLM cost]
  --> human_approval          [LangGraph interrupt]
  --> END
```

### 2.2 Edge Wiring

| From | To | Type |
|------|----|------|
| `START` | `orchestrator` | Direct |
| `orchestrator` | `gate_orchestrator` | Direct |
| `gate_orchestrator` | `fan_out_parsers` OR `orchestrator` | Conditional (`route_gate_orchestrator`) |
| `fan_out_parsers` | `datastage_parser`, `sql_interpreter`, `ddl_parser` | Direct (3 parallel edges) |
| `datastage_parser` | `gate_parsers` | Direct |
| `sql_interpreter` | `gate_parsers` | Direct |
| `ddl_parser` | `gate_parsers` | Direct |
| `gate_parsers` | `pattern_mapper` OR `fan_out_parsers` | Conditional (`route_gate_parsers`) |
| `pattern_mapper` | `gate_mapper` | Direct |
| `gate_mapper` | `spark_sql_generator` OR `pattern_mapper` | Conditional (`route_gate_mapper`) |
| `spark_sql_generator` | `gate_sql` | Direct |
| `gate_sql` | `config_generator` OR `spark_sql_generator` | Conditional (`route_gate_sql`) |
| `config_generator` | `gate_config` | Direct |
| `gate_config` | `schema_validator` OR `config_generator` | Conditional (`route_gate_config`) |
| `schema_validator` | `human_approval` OR `spark_sql_generator` | Conditional (`_should_retry`) |
| `human_approval` | `END` OR `spark_sql_generator` | Conditional (`_route_after_approval`) |

### 2.3 Fan-Out / Fan-In

`fan_out_parsers` is a no-op passthrough node (line 171) that exists because LangGraph conditional edges cannot fan out to parallel nodes directly. It has three direct edges to the three parser nodes. All three parsers converge back to `gate_parsers`, which waits for all three to complete.

The parallel parsers run with `max_concurrency=2` (set at graph compile time, line 297 comment) to prevent bursting the Azure API.

### 2.4 Checkpointing

`get_checkpointer()` (line 273) supports two backends:
- **PostgreSQL** (`PostgresSaver`) when a `checkpoint_postgres_uri` is configured
- **In-memory** (`MemorySaver`) as default/fallback

`compile_graph_stepwise()` (line 314) compiles with `interrupt_before` on every node for step-by-step debugging, using the `ALL_NODES` list.

---

## 3. State Schema

**File:** `state.py` -- `ETLMigrationState(TypedDict)` (line 25)

### 3.1 Field Inventory

| Field | Type | Reducer | Purpose |
|-------|------|---------|---------|
| `messages` | `list[AnyMessage]` | `add_messages` (append + dedup by ID) | LangGraph message history |
| `source_artifacts` | `list[dict]` | Last-write-wins | `[{type, name, content}]` -- input files |
| `target_examples` | `list[dict]` | Last-write-wins | `[{type, name, content}]` -- ground truth outputs |
| `source_schemas` | `dict` | Last-write-wins | `{table_name: {columns: [{name, type, nullable}]}}` |
| `datastage_parsed` | `dict \| None` | Last-write-wins | Structured parse of DataStage XML |
| `sql_interpreted` | `list[dict]` | Last-write-wins | Business rules from stored procedures/views |
| `ddl_schemas` | `list[dict]` | Last-write-wins | Parsed DDL/view schemas |
| `pattern_mapping` | `dict \| None` | Last-write-wins | Legacy-to-Databricks mapping rules |
| `spark_sql_output` | `str \| None` | Last-write-wins | Generated Spark SQL |
| `yaml_config` | `str \| None` | Last-write-wins | Pipeline YAML |
| `deployment_yaml` | `str \| None` | Last-write-wins | Deployment YAML |
| `hql_ddl` | `str \| None` | Last-write-wins | CREATE TABLE HQL |
| `validation_result` | `dict \| None` | Last-write-wins | `{status, score, issues[], comparison}` |
| `_gate_llm_checks` | `list[dict]` | `operator.add` (accumulates) | LLM check results from `gate_sql` + `gate_config` |
| `approval_count` | `int` | Last-write-wins | Consecutive approval count |
| `auto_approve_threshold` | `int` | Last-write-wins | Skip human review after N approvals |
| `current_stage` | `str` | `_last_stage` (handles parallel writes) | Current pipeline position |
| `retry_count` | `int` | Last-write-wins | Retry counter |
| `errors` | `list[str]` | `operator.add` (concatenates) | Accumulated error messages |
| `step_validation` | `dict \| None` | Last-write-wins | Gate feedback for producing nodes on retry |
| `run_id` | `str` | Last-write-wins | Unique run identifier |
| `input_hash` | `str` | Last-write-wins | SHA-256 of all input artifacts |

### 3.2 Custom Reducers

- **`_last_stage`** (line 14): When parallel nodes (the 3 parsers) all write to `current_stage`, LangGraph passes a list. This reducer picks the last value.
- **`operator.add`**: Used for `errors` and `_gate_llm_checks` so values accumulate across nodes rather than overwriting.
- **`add_messages`**: LangGraph's built-in message deduplication by ID.

---

## 4. Model Configuration

**File:** `models.py`

All model instances are `ChatAnthropic` pointed at Azure AI Foundry. Two model tiers:
- **Sonnet** (`get_sonnet()`) -- fast, used for routing/parsing/config generation
- **Opus** (`get_opus()`) -- powerful, used for planning/synthesis/validation

The `AGENT_MODELS` dictionary (line 58) maps each agent name to a lazy factory that reads `pipeline_config.agent_models.<key>` to determine Sonnet vs. Opus. Key function: `get_model_for_agent(agent_name)` (line 70).

---

## 5. Agent Details

### 5.1 Orchestrator

**File:** `agents/orchestrator.py` -- `orchestrator_node()` (line 49)
**Model:** Sonnet (fast routing)
**Pattern:** ReAct agent (`create_react_agent`) with artifact loading tools

**What it does:**
1. Calls `load_all_artifacts()` tool to discover and load all source files, schemas, and target examples from local filesystem or Azure Blob Storage
2. LLM identifies which pipeline to build (e.g., `inventory_periodic_daily`) from target Scala app names
3. Python-based filtering: all non-XML sources always included; DataStage XMLs filtered to matching job; targets filtered to matching subdirectory
4. Generates `run_id` and `input_hash` for reproducibility

**Outputs:** `source_artifacts`, `target_examples`, `run_id`, `input_hash`

**Retry behavior:** Reads `step_validation.errors` and appends them to the task prompt as "PREVIOUS ATTEMPT FAILED" context.

### 5.2 DataStage Parser

**File:** `agents/datastage_parser.py` -- `datastage_parser_node()` (line 159)
**Model:** Configurable (default Opus for synthesis)
**Pattern:** Deterministic extraction + single LLM synthesis (NOT ReAct)

**What it does:**
1. **Python (zero tokens):** Extracts job metadata, embedded SQL, column definitions, stage list via `xml_parser` tools; extracts table names via sqlglot
2. **One LLM call:** Synthesizes extracted data into structured analysis JSON with source_tables, target_table, column_mappings, subqueries, business_rules, temporal_logic, key_findings
3. **Post-LLM enrichment:** If sqlglot found no tables, cross-references LLM analysis against source artifacts to find mentioned table names

**Large XML handling:** XMLs >200K chars get `_quick_parse()` (line 125) -- deterministic only, no LLM call.

**Outputs:** `datastage_parsed` dict with `job_name`, `stages`, `embedded_sql`, `column_definitions`, `extracted_tables`, `llm_analysis`, `analysis_mode`

### 5.3 SQL Interpreter

**File:** `agents/sql_interpreter.py` -- `sql_interpreter_node()` (line 74)
**Model:** Sonnet
**Pattern:** Deterministic extraction + parallel LLM batch

**What it does:**
1. Filters artifacts to `stored_procedure` and `view` types
2. **Python:** sqlglot extracts tables, joins, CTEs, temp tables for each artifact (T-SQL dialect, with `_clean_tsql()` preprocessing)
3. **Parallel LLM:** `model.batch()` sends all artifact prompts concurrently with configurable `max_concurrency`
4. Each LLM call returns business rules, joins, temp tables, transformations

**Outputs:** `sql_interpreted` list of `{artifact_name, artifact_type, extracted_structure, llm_analysis}`

### 5.4 DDL Parser

**File:** `agents/ddl_parser.py` -- `ddl_parser_node()` (line 73)
**Model:** Sonnet
**Pattern:** Deterministic extraction + parallel LLM batch (same as SQL Interpreter)

**What it does:**
1. Filters artifacts to `ddl`, `schema`, and `view` types
2. **Python:** sqlglot extracts table names, columns (name, type, nullable), primary keys from CREATE statements (T-SQL dialect)
3. **Parallel LLM:** `model.batch()` with configurable concurrency
4. Builds `source_schemas` lookup dict: `{table_name: [{name, type, nullable}]}`

**Outputs:** `ddl_schemas` list, `source_schemas` dict

### 5.5 Pattern Mapper

**File:** `agents/pattern_mapper.py` -- `pattern_mapper_node()` (line 14)
**Model:** Opus
**Pattern:** Single LLM call with full upstream context

**What it does:**
1. Gathers all parser outputs (DataStage, SQL, DDL) via `_build_parser_context()` -- prefers deterministic fields (tables from sqlglot, schemas from DDL) over LLM analysis
2. Includes full target examples (up to 8K chars each) as reference
3. **One Opus call:** Maps legacy SQL Server/DataStage patterns to Databricks/Spark equivalents

**Outputs:** `pattern_mapping` dict with `llm_analysis` (type_mappings, sql_pattern_mappings, source_file_manifest, column_renames, key_transformations)

### 5.6 Spark SQL Generator

**File:** `agents/spark_sql_generator.py` -- `spark_sql_generator_node()` (line 64)
**Model:** Opus (planning + dependent stages), Sonnet (independent stages)
**Pattern:** Plan + two-phase generation (3 LLM calls on fresh run, 1 on retry)

**Fresh run (3 steps):**
1. **Plan (Opus):** Analyzes target Scala app, lists ALL transformation stages, marks each INDEPENDENT or DEPENDENT, copies CASE/WHEN mappings verbatim
2. **Phase 1 -- Independent stages (Sonnet):** Generates CREATE OR REPLACE TEMP VIEW for stages that only read source tables
3. **Phase 2 -- Dependent stages (Opus):** Generates remaining stages that depend on Phase 1 views; receives Phase 1 SQL as context
4. **Combine + dedup:** `_dedup_views()` merges Phase 1 + Phase 2, last occurrence wins for duplicate view names

**Retry path (1 LLM call):**
Uses multi-turn conversation pattern: original context as Turn 1, previous SQL as assistant response (Turn 2), gate errors + validation issues + human rejection feedback as follow-up (Turn 3). Instructs Opus to fix ONLY broken views. Uses `opus_dependent` model.

**Key context sources:** `_build_precise_schemas()` builds DDL-sourced column listings; target HQL columns parsed via `_parse_hql_columns()`; full Scala app and HQL provided untruncated (comment: "13% of context window even with everything").

**Outputs:** `spark_sql_output` (deduplicated Spark SQL string)

### 5.7 Config Generator

**File:** `agents/config_generator.py` -- `config_generator_node()` (line 16)
**Model:** Sonnet
**Pattern:** 3 parallel LLM calls via `model.batch()`, one per output file

**What it does:**
1. Loads target template for each file type (pipeline YAML, deployment YAML, HQL DDL) from `target_examples`
2. Builds shared context from pattern mappings, DDL schemas, and generated Spark SQL
3. **3 parallel Sonnet calls:** Each produces one file, instructed to copy target template structure exactly and only change values where pipeline data requires it

**Outputs:** `yaml_config`, `deployment_yaml`, `hql_ddl`

### 5.8 Schema Validator

**File:** `agents/schema_validator.py` -- `schema_validator_node()` (line 477)
**Model:** None (zero LLM cost)
**Pattern:** Deterministic cross-checks + assembly of upstream gate LLM results

**What it does:**
1. Runs `_deterministic_checks()` producing 5 check categories:
   - **sql_syntax_validation** (spark_sql section): sqlglot AST analysis -- view count, joins, aggregates, CASTs, truncation detection
   - **sql_content_validation** (spark_sql section): verifies presence of SKU_Behavior CASE mapping, flag thresholds (>=2/>=1), E3 RAQ/AFS override logic, HQL column coverage
   - **column_mapping** (hql_ddl section): cross-references generated HQL columns against target HQL
   - **data_type_validation** (hql_ddl section): compares column types (exact, implicit_cast, mismatch) with compatible type groups
   - **source_file_coverage** (pipeline_yaml section): YAML sourceFile names vs. target YAML
   - **deployment_config** (deployment section): valid YAML, cluster config keys, schedule/trigger presence
2. Pulls LLM check results from `_gate_llm_checks` state field (accumulated by `gate_sql` + `gate_config`)
3. Computes weighted overall score with section-specific weights (business_logic_preservation = 3.0 highest, deployment = 0.5 lowest)
4. Critical check floor: if any critical check (business_logic, column_existence, sql_syntax) scores below 0.70, overall score is capped

**Score thresholds:**
- `overall_score >= 0.90` -> pass
- `hard_fail` (empty outputs, missing columns, truncated SQL) -> capped at 0.50

**Outputs:** `validation_result` dict with status, overall_score, checks, issues, summary_scores, sections; increments `retry_count` on fail

### 5.9 Review Agent

**File:** `agents/review_agent.py`
**Model:** Opus (bound with tools)
**Pattern:** Tool-using agent for post-pipeline interactive review

**Not a graph node** -- this is an interactive agent used by the API server during the human review phase. It maintains a multi-turn conversation with tools:

| Tool | Purpose |
|------|---------|
| `read_sql()` | Returns full generated Spark SQL with view count |
| `read_scala()` | Returns full target Scala application |
| `read_validation()` | Returns current validation results, scores, findings, scratchpad |
| `patch_view(view_name, new_sql)` | Surgically replaces a specific view's CREATE statement using regex matching |
| `run_validation()` | Re-runs deterministic + LLM checks on current SQL and updates context |

Context is set via `set_review_context()` by the API server. The `on_sql_updated` callback propagates patched SQL back to the pipeline state.

### 5.10 Human Approval

**File:** `agents/human_approval.py` -- `human_approval_node()` (line 13)
**Model:** None
**Pattern:** LangGraph `interrupt` for human-in-the-loop

**Flow:**
1. If `approval_count >= auto_approve_threshold` (default 3) -> auto-approve, skip human review
2. Otherwise, `interrupt()` with approval summary (validation status, score, issue count, generated files, approval progress)
3. On approve: increment `approval_count`, set stage to `human_approved`
4. On reject: reset `approval_count` to 0, append rejection reason to `errors` list, set stage to `human_rejected`

---

## 6. Validation and Gate Logic

**File:** `validators.py`

### 6.1 ValidationCheck Dataclass (line 142)

```python
@dataclass
class ValidationCheck:
    passed: bool
    node: str
    checks: list[dict]    # [{name, passed, detail}]
    errors: list[str]     # Hard failures -- should retry
    warnings: list[str]   # Soft issues -- log but continue
```

### 6.2 Deterministic Gate Validators

Each gate calls a deterministic validator, converts the result to a state update via `_gate_result()`, and the graph routes based on `step_validation.passed`.

#### gate_orchestrator -> `validate_orchestrator()` (line 162)
Checks:
- `source_artifacts_loaded`: at least 1 source artifact
- `has_datastage_xml`: at least 1 DataStage XML
- `target_examples_loaded`: at least 1 target example (hard fail if missing)
- `all_have_content`: no empty artifacts
- `run_id_set`: run_id was generated

#### gate_parsers -> `validate_parsers()` (line 226)
Checks:
- `datastage_has_stages`: stages parsed from XML
- `datastage_has_sql`: embedded SQL fragments extracted
- `datastage_has_tables`: tables extracted via sqlglot
- `datastage_has_columns`: column definitions from XML
- `datastage_has_analysis`: LLM analysis exists and is >100 chars
- `table_crosscheck`: deterministic tables vs. LLM-mentioned tables (warns on discrepancies)
- `sql_interpreted_present`: SQL interpreter produced results
- `ddl_schemas_present`: DDL parser produced results
- `ddl_columns_grounded`: DDL column names found in source artifacts (source grounding)

#### gate_mapper -> `validate_pattern_mapper()` (line 350)
Checks:
- `mapping_present`: analysis is non-empty
- `mentions_source_tables`: mapping references DDL source table names
- `mentions_source_references`: references source files/tables
- `mentions_type_mappings`: includes type conversion concepts
- `mentions_column_mappings`: includes column/field mapping concepts

#### gate_sql -> `validate_spark_sql()` (line 408) + `llm_check_sql()` (line 853)

**Deterministic checks:**
- `sql_not_empty`: SQL is >= 5,000 chars (real migration is 10K+)
- `sqlglot_syntax_valid`: >= 50% of statements parse successfully
- `ddl_table_coverage`: >= 30% of DDL tables referenced in SQL
- `column_coverage`: >= 20% of known DDL columns referenced
- `source_tables_grounded`: FROM/JOIN references found in source/target artifacts (excludes intermediate views the SQL itself defines)
- `sql_not_truncated`: file-level truncation (ending in `,`, `AND`, `OR`, `=`) and per-view truncation (views missing terminal semicolons)
- `hql_sql_column_match`: HQL columns appear in generated SQL

**LLM checks (only if deterministic passed):**
- `business_logic_preservation`: Verifies SQL-to-Scala behavioral equivalence with view dependency graph
- `column_existence`: Verifies all required columns present
- Gate fails if `business_logic_preservation` score < 0.75
- Scores 0.75+ pass to human review (style issues, not bugs)
- Supports multi-turn re-review with previous findings context (`previous_review` parameter)

**Source grounding infrastructure:**
- `_build_source_corpus()`: combines all source artifact and target example content (truncated to 20K chars each) into lowercase searchable text
- `_check_names_grounded()`: verifies names exist in corpus, skipping short names and SQL keywords
- `_sqlglot_extract_tables()`: deterministic table extraction from SQL AST
- `_extract_view_dep_graph()`: builds view dependency adjacency graph with downstream impact counts for LLM scoring

#### gate_config -> `validate_config_generator()` (line 634) + `llm_check_config()` (line 984)

**Deterministic checks:**
- `yaml_config_not_empty`: >= 200 chars
- `yaml_config_valid`: parses as valid YAML (with custom tag tolerance via `_safe_yaml_load()`)
- `deployment_yaml_not_empty`: >= 100 chars
- `deployment_yaml_valid`: parses as valid YAML
- `hql_has_create_table`: contains CREATE TABLE statement
- `hql_columns_in_target`: HQL column names found in target HQL (source grounding)
- `yaml_sourcefiles_grounded`: YAML sourceFile names found in source artifacts

**LLM checks (only if deterministic passed):**
- `yaml_structure`: structural comparison to target YAML
- `column_type_consistency`: cross-references HQL types with SQL CASTs
- `deployment_validation`: deployment config correctness

### 6.3 Gate Routing Logic

All gates use the same pattern via `_route_gate()` (line 107):
```
if validation.passed: return pass_target
if retry_count >= MAX_GATE_RETRIES: return pass_target  # don't loop forever
return retry_target
```

Gate nodes write validation feedback to `step_validation`. Producing agents read `step_validation` on retry to know what to fix. Each agent's retry path appends gate errors to its prompt as "PREVIOUS ERRORS" context.

---

## 7. Retry Mechanisms

### 7.1 Gate Retry (Deterministic Loops)

Each gate can route back to its producing node up to `MAX_GATE_RETRIES` times. After exhausting retries, the pipeline proceeds forward regardless (prevents infinite loops).

| Gate | On Fail Routes To |
|------|-------------------|
| `gate_orchestrator` | `orchestrator` |
| `gate_parsers` | `fan_out_parsers` (re-runs all 3 parsers) |
| `gate_mapper` | `pattern_mapper` |
| `gate_sql` | `spark_sql_generator` |
| `gate_config` | `config_generator` |

### 7.2 Schema Validator Retry (`_should_retry`, line 151)

After `schema_validator` runs:
- Score >= 0.80: route to `human_approval` (good enough for review)
- Score < 0.80 AND retry_count < 1: route to `spark_sql_generator` (one auto-retry for bad scores)
- Score < 0.80 AND retry_count >= 1: route to `human_approval` (don't loop, let human review)

### 7.3 Human Rejection Retry (`_route_after_approval`, line 144)

When human rejects, routes back to `spark_sql_generator`. The rejection reason is appended to `errors` (which accumulates via `operator.add`). The SQL generator's retry path includes `HUMAN REVIEWER FEEDBACK` in its prompt context.

### 7.4 LLM-Level Retry (Azure 529 Handling)

All LLM-calling nodes use `RetryPolicy` (line 202) with configurable:
- `max_attempts` (from `pipeline_config.retry.llm_max_attempts`)
- `initial_interval` (from `pipeline_config.retry.llm_initial_interval`)
- `backoff_factor` (from `pipeline_config.retry.llm_backoff_factor`)
- `max_interval` (from `pipeline_config.retry.llm_max_interval`)

This handles Azure 529 (Overloaded) errors at the LangGraph node level, separate from the application-level gate retries.

### 7.5 Spark SQL Generator Retry Path (Special Case)

On retry, the SQL generator uses a multi-turn conversation pattern instead of regenerating from scratch (line 142-175):
- Turn 1 (HumanMessage): original generation context
- Turn 2 (AIMessage): the previously generated SQL
- Turn 3 (HumanMessage): "fix only what's broken" with gate errors, validation issues, and human rejection feedback (truncated to 3K chars)

This targeted approach avoids regenerating correct views and focuses Opus on fixing identified issues.

---

## 8. Pipeline Runner

**File:** `runner.py` -- `run_pipeline()` (line 80)

### 8.1 Input Loading

`load_local_artifacts()` (line 17) loads from local filesystem:
- **Source files** from `docs/ETL_use_case/`: DataStage XML, stored procedure, 2 DDLs, 2 views
- **Schema files** from `docs/Sephora/`: `retfl030_skuloc.txt`, `edwlib_whintr.txt`
- **Target examples** from `docs/ETL_use_case/target/`: Scala app, pipeline YAML, deployment YAML, HQL DDL

### 8.2 Initial State

All fields initialized with empty defaults. Notable settings:
- `auto_approve_threshold`: 3 (skip human review after 3 consecutive approvals)
- `retry_count`: 0
- `current_stage`: "initialized"
- `_gate_llm_checks` is not explicitly set (accumulates via `operator.add` reducer)

### 8.3 Execution

Compiles graph with checkpointer, invokes with `thread_id: "demo-run-1"`. Single-shot `app.invoke()` runs the entire pipeline synchronously.

---

## 9. End-to-End Flow Summary

1. **Orchestrator** discovers and loads all artifacts (local or Azure Blob), identifies target pipeline by name, filters sources/targets, generates run_id and input_hash.

2. **Gate: Orchestrator** verifies artifacts loaded, DataStage XML present, targets found, all have content, run_id set. On fail -> retry orchestrator.

3. **Fan-Out** to 3 parallel parsers (max 2 concurrent):
   - **DataStage Parser**: XML extraction (metadata, SQL, columns, stages) via Python tools + single Opus synthesis call
   - **SQL Interpreter**: sqlglot structure extraction + parallel Sonnet batch for business rules from stored procedures and views
   - **DDL Parser**: sqlglot schema extraction + parallel Sonnet batch; builds `source_schemas` lookup dict

4. **Gate: Parsers** verifies all 3 produced output -- stages, SQL, tables, columns, analysis; cross-checks deterministic vs. LLM table lists; verifies DDL columns grounded in source files. On fail -> re-run all 3 parsers.

5. **Pattern Mapper**: single Opus call with all parser outputs + target examples to produce legacy-to-Databricks mappings.

6. **Gate: Mapper** verifies mapping references source tables and includes type/column mapping concepts. On fail -> retry mapper.

7. **Spark SQL Generator**: Plan (Opus) -> Phase 1 independent stages (Sonnet) -> Phase 2 dependent stages (Opus) -> combine + dedup. On retry: single multi-turn Opus call with previous SQL + feedback.

8. **Gate: SQL** runs deterministic checks (syntax, size, table/column coverage, truncation, source grounding), then LLM checks (business logic preservation with view dependency graph, column existence). Business logic score < 0.75 triggers gate failure. On fail -> retry SQL generator.

9. **Config Generator**: 3 parallel Sonnet calls produce pipeline YAML, deployment YAML, and HQL DDL by copying target templates and substituting pipeline-specific values.

10. **Gate: Config** runs deterministic checks (YAML validity, size, CREATE TABLE presence, source grounding for HQL columns and YAML sourceFiles), then LLM checks (yaml_structure, column_type_consistency, deployment_validation). On fail -> retry config generator.

11. **Schema Validator** (zero LLM cost): runs comprehensive deterministic cross-checks (SQL syntax metrics, content checks for business-specific logic, column mapping, data type validation, source file coverage, deployment config), assembles upstream gate LLM results, computes weighted overall score with critical check floor. Score >= 0.80 -> human approval. Score < 0.80 -> one auto-retry of SQL generator, then human approval.

12. **Human Approval**: presents validation summary via LangGraph `interrupt`. Auto-approves after 3 consecutive approvals. On approve -> END. On reject -> back to SQL generator with rejection reason in errors.

---

## 10. Key Function/Class Reference

| Item | File | Line | Purpose |
|------|------|------|---------|
| `build_graph()` | `graph.py` | 180 | Constructs the full StateGraph |
| `compile_graph()` | `graph.py` | 287 | Compiles with checkpointer |
| `compile_graph_stepwise()` | `graph.py` | 314 | Compiles with interrupt_before on all nodes |
| `ETLMigrationState` | `state.py` | 25 | TypedDict state schema |
| `_last_stage()` | `state.py` | 14 | Reducer for parallel writes to current_stage |
| `get_model_for_agent()` | `models.py` | 70 | Agent-to-model resolution |
| `AGENT_MODELS` | `models.py` | 58 | Agent name -> model factory mapping |
| `ValidationCheck` | `validators.py` | 142 | Dataclass for gate results |
| `validate_orchestrator()` | `validators.py` | 162 | Orchestrator gate logic |
| `validate_parsers()` | `validators.py` | 226 | Parser gate logic |
| `validate_pattern_mapper()` | `validators.py` | 350 | Mapper gate logic |
| `validate_spark_sql()` | `validators.py` | 408 | SQL gate deterministic checks |
| `validate_config_generator()` | `validators.py` | 634 | Config gate deterministic checks |
| `llm_check_sql()` | `validators.py` | 853 | SQL gate LLM checks |
| `llm_check_config()` | `validators.py` | 984 | Config gate LLM checks |
| `_extract_view_dep_graph()` | `validators.py` | 799 | View dependency graph for LLM scoring |
| `_build_source_corpus()` | `validators.py` | 30 | Source grounding corpus builder |
| `_check_names_grounded()` | `validators.py` | 53 | Name-in-corpus verification |
| `orchestrator_node()` | `agents/orchestrator.py` | 49 | ReAct agent for artifact discovery |
| `datastage_parser_node()` | `agents/datastage_parser.py` | 159 | Deterministic + LLM DataStage parsing |
| `sql_interpreter_node()` | `agents/sql_interpreter.py` | 74 | Deterministic + batch LLM SQL analysis |
| `ddl_parser_node()` | `agents/ddl_parser.py` | 73 | Deterministic + batch LLM DDL parsing |
| `pattern_mapper_node()` | `agents/pattern_mapper.py` | 14 | Single Opus call for pattern mapping |
| `spark_sql_generator_node()` | `agents/spark_sql_generator.py` | 64 | 3-phase SQL generation |
| `config_generator_node()` | `agents/config_generator.py` | 16 | 3 parallel Sonnet calls |
| `schema_validator_node()` | `agents/schema_validator.py` | 477 | Deterministic cross-checks + score assembly |
| `human_approval_node()` | `agents/human_approval.py` | 13 | LangGraph interrupt gate |
| `create_review_agent()` | `agents/review_agent.py` | 336 | Interactive tool-using review agent |
| `run_pipeline()` | `runner.py` | 80 | Full pipeline execution entry point |
| `load_local_artifacts()` | `runner.py` | 17 | Local filesystem artifact loader |
