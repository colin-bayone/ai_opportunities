# Sephora EDW Demo Codebase Analysis

**Repo:** `/home/cmoore/programming/sephora_edw-1/`
**Worktree:** `.claude/worktrees/perf-optimizations/` (latest with perf optimizations + AI review streaming)
**Date:** 2026-04-02
**Source:** Thorough multi-wave read of all source files from the worktree
**Files read:** graph.py, state.py, models.py, config.py, pipeline_config.yaml, validators.py (full 900+ lines), all 10 agent files, all 7 tool files, all 12 prompt files, api_server.py (300+ lines), CLAUDE.md

---

## Project Overview

LangGraph multi-agent system that migrates ETL pipelines from IBM DataStage/SQL Server to Databricks/Spark SQL. Uses Claude models (Opus and Sonnet) via Azure AI Foundry. FastAPI backend with vanilla HTML/CSS/JS dashboard. PostgreSQL for checkpointing and run history. LangSmith for tracing.

## Setup Commands

```bash
poetry install
docker compose up -d          # Postgres for checkpointing
cp .env.example .env          # Configure Azure AI + LangSmith + Blob Storage
PYTHONPATH=src uvicorn etl_agent.api_server:app --host 0.0.0.0 --port 8100
# Full pipeline e2e: poetry run python tests/test_e2e_local.py (~9.5 min)
```

---

## Architecture: Producer → Gate → Next Producer

Core pattern from `graph.py`: each agent node produces output, then a deterministic gate validator checks it (zero LLM cost). If the gate fails, the producer retries with error context injected into `step_validation` state field. After `max_gate_retries` (default 2), the pipeline proceeds anyway to avoid infinite loops.

### Pipeline Flow

```
START → orchestrator → gate_orchestrator
  → fan_out_parsers → [datastage_parser, sql_interpreter, ddl_parser] (PARALLEL, 2 at a time)
  → gate_parsers → pattern_mapper → gate_mapper
  → spark_sql_generator → gate_sql (deterministic + LLM business logic check)
  → config_generator → gate_config (deterministic + LLM cross-reference check)
  → schema_validator → human_approval → END
```

**Key routing logic:**
- `gate_sql` and `gate_config`: run deterministic checks first, then LLM checks ONLY if deterministic passed (saves tokens). Controlled by `gate_llm_checks` config flag (can disable for faster demos).
- `schema_validator`: score >= 0.80 → human_approval; score < 0.80 → retry once then human_approval regardless.
- `human_approval`: approved → END; rejected → back to `spark_sql_generator`.
- `fan_out_parsers`: no-op passthrough node needed because LangGraph conditional edges can't fan out directly.

### Concurrency and Retry

From `pipeline_config.yaml`:
- `graph_max_concurrency`: 8 (max parallel nodes in a superstep)
- `ddl_parser_batch`: 8, `sql_interpreter_batch`: 8, `config_generator_batch`: 6 (parallel LLM calls within an agent)
- `max_gate_retries`: 2 per gate before force-proceeding
- `llm_max_attempts`: 5 with exponential backoff (2s initial, 2x factor, 60s max) for Azure 529 errors
- `per_stage_retries`: 3 (max retries per SQL generation stage)

**Orchestrator mode:** `pipeline.orchestrator_mode` can be `"react"` (full ReAct agent with tools, needed for MCP) or `"direct"` (Python calls tools directly, single LLM call for pipeline ID, faster for demos).

---

## State Schema (`state.py`: `ETLMigrationState`)

TypedDict with custom reducers:

| Field | Type | Reducer | Purpose |
|-------|------|---------|---------|
| `messages` | list[AnyMessage] | add_messages (append+dedup) | LangGraph message history |
| `source_artifacts` | list[dict] | last-write | [{type, name, content}] input files |
| `target_examples` | list[dict] | last-write | [{type, name, content}] reference outputs |
| `source_schemas` | dict | last-write | {table: {columns: [{name, type, nullable}]}} |
| `datastage_parsed` | dict | last-write | Structured XML parse with embedded_sql, stages, tables, columns, llm_analysis |
| `sql_interpreted` | list[dict] | last-write | Business rules from stored procedures (per-artifact) |
| `ddl_schemas` | list[dict] | last-write | Parsed DDL/view schemas with parsed_schemas per file |
| `pattern_mapping` | dict | last-write | Legacy→Databricks mapping rules (llm_analysis field) |
| `spark_sql_output` | str | last-write | Generated Spark SQL (all CREATE TEMP VIEW statements) |
| `yaml_config` | str | last-write | Pipeline YAML |
| `deployment_yaml` | str | last-write | Deployment YAML |
| `hql_ddl` | str | last-write | CREATE TABLE HQL |
| `validation_result` | dict | last-write | {status, overall_score, issues[], sections[]} |
| `_gate_llm_checks` | list[dict] | operator.add (accumulate) | LLM findings from gate_sql + gate_config |
| `step_validation` | dict | last-write | Gate feedback for retrying agents: {node, passed, checks[], errors[], warnings[]} |
| `current_stage` | str | _last_stage (handles parallel writes) | Current pipeline position |
| `retry_count` | int | last-write | Gate retry counter |
| `run_id` | str | last-write | Unique run identifier |
| `input_hash` | str | last-write | SHA-256 of all input artifacts |
| `approval_count` | int | last-write | Consecutive approval count |
| `auto_approve_threshold` | int | last-write | Skip review after N approvals |

Custom `_last_stage` reducer: when parallel parsers all write to `current_stage` simultaneously, LangGraph passes a list. The reducer picks the last value.

---

## Model Assignments (`models.py` + `pipeline_config.yaml`)

All models are Claude via Azure AI Foundry using `ChatAnthropic` with `base_url`.

| Agent | Model | Rationale |
|-------|-------|-----------|
| orchestrator | Sonnet | Fast routing, no heavy reasoning needed |
| datastage_parser | **Opus** | Complex XML analysis with 1M context |
| sql_interpreter | Sonnet | SQL structure extraction, batch parallel |
| ddl_parser | Sonnet | Schema extraction, batch parallel |
| pattern_mapper | **Opus** | Critical mapping step, needs full context |
| spark_sql_generator (plan) | **Opus** | Plans all stages and dependency graph |
| spark_sql_generator (independent) | Sonnet | Generates independent stages (simpler) |
| spark_sql_generator (dependent) | **Opus** | Generates dependent stages (needs full context) |
| config_generator | Sonnet | Template-based, 3 parallel calls |
| schema_validator | Sonnet | Cross-checks, no generation |

---

## Agents (10 files in `agents/`)

### orchestrator.py
- Two modes: `react` (full ReAct agent with tools for MCP/blob) and `direct` (Python calls `load_all_artifacts` directly, single LLM call for pipeline ID). Direct mode is faster for demos.
- Loads files from `docs/ETL_use_case/` (local) or Azure Blob Storage (production).
- Classifies artifacts by content (DataStage XML, stored procedure, DDL, view, schema, Scala app, YAML, HQL).
- **Side-channel pattern:** file content stored in `_artifact_store` dict, NOT returned to LLM. LLM only sees metadata (name, type, size). Prevents 1.3M char XML from consuming context.
- Filters targets by pipeline name matching (e.g., `inventory_periodic_daily`).
- Generates `run_id` and `input_hash` for reproducibility.

### datastage_parser.py
- **NOT a ReAct agent.** Deterministic extraction + single LLM synthesis.
- Step 1 (Python, zero tokens): `extract_job_metadata`, `extract_embedded_sql`, `extract_column_definitions` from XML.
- Step 2 (1 Opus call): synthesize findings into structured analysis.
- Uses `sqlglot` (T-SQL dialect) to extract table names from embedded SQL fragments.
- Cross-references LLM-mentioned tables against deterministic extraction.
- Quick parse mode for XMLs > 200K chars (skips LLM, deterministic only).

### sql_interpreter.py
- Sonnet model, batch parallel processing.
- Step 1 (Python): `sqlglot` extracts tables, joins, CTEs, temp tables from T-SQL stored procedures and views.
- Step 2 (Parallel LLM): `llm.batch()` processes all SP/view artifacts in parallel (batch size from config).
- Cleans T-SQL artifacts (GO, USE, SET) before parsing.

### ddl_parser.py
- Same pattern as sql_interpreter: sqlglot extraction + parallel LLM batch.
- Extracts table names, column names with FULL precision (e.g., `decimal(13,3)`), nullable constraints, primary keys.
- Handles both CREATE TABLE and CREATE VIEW statements.

### pattern_mapper.py
- **Single Opus call.** Reads all parser outputs + target examples.
- Produces translation dictionary: surrogate keys → business keys, SQL Server types → Databricks types, temp tables → intermediate views, CASE WHEN → withColumn patterns, etc.
- Builds context from deterministic fields first, falls back to LLM analysis.

### spark_sql_generator.py
- Three-phase generation (the proven 0.97-scoring approach):
  1. **Plan** (1 Opus call): Analyzes full Scala app, extracts stage snippets, builds dependency graph (independent vs dependent stages).
  2. **Phase 1** (1 Sonnet call): Generates all independent stages.
  3. **Phase 2** (1 Opus call): Generates dependent stages with Phase 1 output as context.
- On **retry**: passes previous SQL + gate errors to Opus for targeted fix (1 call, not 3).
- Deduplicates views (last occurrence wins).
- Context limits from config prevent prompt overflow.

### config_generator.py
- **3 parallel Sonnet calls** via `llm.batch()`: pipeline YAML, deployment YAML, create.HQL.
- Each call gets the target template as ground truth and is told to copy structure exactly, only changing values where needed.
- Shared context: pattern mapping + source schemas + generated Spark SQL.

### schema_validator.py
- **Zero LLM calls.** Deterministic cross-checks + assembly of upstream gate LLM results.
- Organizes checks into 4 sections for dashboard rendering: Spark SQL, HQL DDL, Pipeline YAML, Deployment Config.
- Computes overall_score by combining deterministic pass rates with LLM findings (warnings deduct 0.2, bugs deduct more).
- Produces the `validation_result` dict that the review screen displays.

### review_agent.py (AI Review)
- Tool-using agent for surgical SQL review and fix.
- Tools: `read_sql`, `read_scala`, `read_validation`, `patch_view` (surgically replace a specific view's SQL), `run_validation` (re-run checks on current SQL).
- Single conversation thread (not split into review + fix like before).
- Module-level `_review_context` dict set by API server before each conversation.

### human_approval.py
- Uses LangGraph `interrupt()` for human-in-the-loop.
- Auto-approves after threshold reached (configurable, default 1 for demo = always manual).
- Approved → increment counter, proceed to END.
- Rejected → reset counter, add error, route back to `spark_sql_generator`.

---

## Validators (`validators.py` — 900+ lines)

All deterministic (zero LLM cost) with source grounding checks.

### Core patterns:
- **Source grounding:** builds lowercase corpus from all source/target artifacts, checks if generated names actually exist in original files. Prevents hallucination.
- **sqlglot:** AST-based table and column extraction from both T-SQL and Spark SQL dialects.
- **YAML validation:** custom safe loader that handles Databricks `!secret` tags.

### validate_orchestrator
- Checks: source artifacts loaded, has DataStage XML, has target examples, all artifacts have content, run_id set.

### validate_parsers
- DataStage: has stages, has embedded SQL, has tables (sqlglot), has columns, has LLM analysis (>100 chars).
- Cross-check: compare deterministic tables vs LLM-mentioned tables. Warns on discrepancies.
- SQL interpreter: present check. DDL: present + column names grounded in source.

### validate_pattern_mapper
- Mapping non-empty, mentions actual source table names from DDL schemas.
- Checks for key concepts: source references, type mappings, column mappings.

### validate_spark_sql (most complex, ~230 lines)
- SQL not empty and substantial (>5000 chars, real migration is 10K+).
- **sqlglot syntax check:** parse statement by statement, pass rate >= 50%.
- **DDL table coverage:** at least 30% of DDL tables must appear in SQL.
- **Column coverage:** at least 20% of known DDL columns in SQL.
- **Source table grounding:** FROM/JOIN table refs checked against source+target corpus. Excludes intermediate views the SQL itself creates. Warns on ungrounded names.
- **Truncation detection:** both end-of-file and per-view. Checks if SQL ends with comma/AND/OR/ON/=. Checks each CREATE TEMP VIEW for missing semicolons.
- **HQL column match:** if HQL DDL exists, its columns should appear in SQL.

### validate_config_generator
- Pipeline YAML: non-empty (>200 chars), valid YAML structure.
- Deployment YAML: non-empty (>100 chars), valid YAML.
- HQL: has CREATE TABLE statement.
- **Source grounding:** HQL column names must exist in target corpus. YAML sourceFile names must exist in source corpus.

### LLM gate checks (llm_check_sql, llm_check_config)
- Run AFTER deterministic checks pass. Called from `gate_sql` and `gate_config`.
- `llm_check_sql`: extracts view dependency graph from SQL, sends to LLM with Scala target for business logic verification. Two checks: column_existence and business_logic_preservation.
- Supports multi-turn: on retry, includes previous findings and AI Review verdicts so LLM doesn't re-flag resolved issues.
- `llm_check_config`: verifies YAML token names, column type consistency vs SQL CASTs, deployment config structure.

---

## Tools (7 files in `tools/`)

### artifact_tools.py
- **Side-channel store** (`_artifact_store`): tools write file content here, LLM never sees it. Orchestrator node reads after agent finishes.
- `load_all_artifacts`: walks directories, classifies each file (DataStage XML, stored_procedure, view, ddl, schema, scala_app, yaml_config, hql_ddl, binary_skip).
- Classification logic: checks content patterns (XML detection, CREATE PROCEDURE, CREATE TABLE, YAML structure, Scala patterns).
- Two backends: local filesystem and Azure Blob Storage.

### xml_parser.py
- Pure Python XML processing with `xml.etree.ElementTree`.
- `extract_job_metadata`: job name, stage count, descriptions from DSExport format.
- `extract_embedded_sql`: finds SQL in stage properties (custom SQL queries, WHERE clauses).
- `extract_column_definitions`: column names, types, precision from stage ports.
- `chunk_with_ports`: splits large XML into per-stage chunks with their associated I/O ports.
- Handles Sephora's specific DSExport format (ODBCStage, TransformerStage, PxSequentialFile, etc.).

### sql_tools.py
- `parse_sql_structure`: sqlglot-based extraction of tables, joins, CTEs, temp tables, statement types.
- Deterministic, no LLM needed for structure.

### datastage_tools.py
- Side-channel store (`_ds_store`): XML content pre-loaded by parser node before agent starts.
- Tools: `get_job_overview`, `get_embedded_sql`, `get_column_definitions`, `list_stages`, `read_stage`, `search_xml`, `write_notes` (scratchpad).
- LLM never sees raw XML; tools return summaries.

### scratchpad.py
- Simple key-value note storage for agents to record findings between tool calls.
- `write_notes(key, content)` and `read_notes(key)`.
- Cleared between agent runs.

### blob_storage.py
- Azure Blob Storage operations for production deployment.
- List containers, read blobs, upload outputs.

### result.py
- `ok(data, **kwargs)` and `fail(message, can_retry, suggestion)` helpers for consistent tool responses.

---

## Prompts (12 files in `prompts/`)

Each prompt is a system message defining the agent's role, workflow, and output rules.

| Prompt | Key Instructions |
|--------|-----------------|
| `orchestrator.txt` | Discover/load/classify artifacts, identify pipeline name from target Scala apps |
| `datastage_parser.txt` | Tool-based XML exploration workflow (5 steps), scratchpad usage for consistency |
| `sql_interpreter.txt` | Extract business rules (flag calculations, SKU_Behavior thresholds, dotcom handling, temp tables, 7-day lookbacks) |
| `ddl_parser.txt` | Extract COMPLETE schema with EXACT decimal precision. Every column, every constraint. |
| `pattern_mapper.txt` | Map 9+ legacy pattern types (surrogate keys, types, temp tables, EXISTS subqueries, CASE WHEN, GETDATE, NOLOCK hints, CAST, Scala helper functions) |
| `spark_sql_planner.txt` | Output dependency graph: `Stage N (viewName) -- INDEPENDENT/DEPENDENT on Stages X,Y` |
| `spark_sql_generator.txt` | Two-phase generation. Quality rules: exact type precision, no invented COALESCE, copy CASE/WHEN mappings verbatim from Scala |
| `spark_sql_stage_generator.txt` | Single-stage generation. Raw SQL only, no markdown, starts with CREATE OR REPLACE TEMP VIEW, ends with semicolon |
| `config_generator.txt` | Copy target templates EXACTLY. Do NOT invent token names, add/remove columns, or modify deployment settings |
| `schema_validator.txt` | 5 semantic checks (YAML structure, column types, column existence, business logic, deployment). Focus on what code can't judge. |
| `gate_sql_llm.txt` | 2 checks (column existence, business logic). Two-phase analysis: first use scratchpad to think, then output JSON. Impact-aware scoring using dependency graph. |
| `gate_config_llm.txt` | 3 checks (YAML structure, column types, deployment). Match against target examples exactly. |

---

## API Server (`api_server.py`)

FastAPI at port 8100. Key endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serves `static/index.html` dashboard |
| `/run` | POST | Starts pipeline (accepts `manual_approval` flag) |
| `/status` | GET | Current state with node events, gate results, outputs |
| `/output/{key}` | GET | Specific output (spark_sql, yaml_config, deployment_yaml, hql_ddl) |
| `/live` | GET | Rolling buffer of 100 recent tool/LLM activity events |
| `/runs` | GET | Past runs from Postgres |
| `/runs/{run_id}` | GET | Specific past run |
| `/approve` | POST | Resume from human approval interrupt (approve or reject with reason) |
| `/chat` | POST | AI Review conversation (sends to review_agent) |
| `/fix` | POST | Auto-fix (review_agent surgical edits) |

**LiveActivityHandler:** Callback handler that tracks tool calls and LLM invocations in real-time. Populates the execution log on the dashboard. Resolves current LangGraph node from callback metadata/tags.

**Run state management:** Global `_run_state` dict tracks: `is_running`, `is_complete`, `awaiting_approval`, `node_events`, `completed_nodes`, `current_node`, `final_state`, `thread_id`, `compiled_graph`.

**Async streaming:** Uses `compiled.astream()` with `stream_mode="updates"` to get node-by-node events. Detects `__interrupt__` events for human approval pause. Saves run to Postgres on completion.

---

## Dashboard (`static/index.html`)

Single HTML file with embedded CSS/JS (no framework). Recent perf-optimizations branch added 316 lines.

Key features:
- Run history list (clickable, loads cached data from Postgres)
- New run: load demo files (hardcoded 9 files) + configuration dropdowns (placeholders)
- DAG visualization with nodes lighting up per stage
- Execution log with live spinners and timers (polls `/live` endpoint)
- Gate result dropdowns (open if issues, closed if 100%)
- Code preview with highlight.js syntax highlighting
- AI Review button (streams conversation via `/chat`)
- Auto-fix button (calls `/fix`, surgical edits)
- Approve/Reject buttons (calls `/approve`)
- Individual file downloads (zip is broken)
- Progress bar and collapsible sections

---

## Project Structure

```
sephora_edw-1/
├── app.py                         # Entry point
├── pipeline_config.yaml           # All config: models, concurrency, retries, context limits, behavior flags
├── docker-compose.yml             # Postgres service
├── pyproject.toml                 # Poetry dependencies
├── static/index.html              # Dashboard (single file, vanilla HTML/CSS/JS)
├── prompts/                       # 12 system prompt templates
├── src/etl_agent/
│   ├── graph.py                   # LangGraph StateGraph (15 nodes, 5 gates, conditional routing)
│   ├── state.py                   # ETLMigrationState TypedDict (20+ fields, 3 custom reducers)
│   ├── api_server.py              # FastAPI (10+ endpoints, async streaming, LiveActivityHandler)
│   ├── config.py                  # Pydantic settings (Azure AI, Blob Storage, Postgres)
│   ├── pipeline_config.py         # YAML config loader with dot-access
│   ├── models.py                  # Claude model factory (Opus/Sonnet via Azure AI Foundry)
│   ├── runner.py                  # CLI pipeline runner
│   ├── validators.py              # 900+ lines: 5 validators, 2 LLM gate checks, sqlglot, source grounding
│   ├── agents/                    # 10 agent implementations
│   │   ├── orchestrator.py        # ReAct or direct mode, artifact discovery
│   │   ├── datastage_parser.py    # Deterministic XML + 1 Opus synthesis
│   │   ├── sql_interpreter.py     # sqlglot + parallel Sonnet batch
│   │   ├── ddl_parser.py          # sqlglot + parallel Sonnet batch
│   │   ├── pattern_mapper.py      # 1 Opus call, all context
│   │   ├── spark_sql_generator.py # 3-phase: plan (Opus) → independent (Sonnet) → dependent (Opus)
│   │   ├── config_generator.py    # 3 parallel Sonnet calls (YAML, deployment, HQL)
│   │   ├── schema_validator.py    # Zero LLM, assembles gate results
│   │   ├── review_agent.py        # Tool-using agent for AI review + surgical fix
│   │   └── human_approval.py      # LangGraph interrupt for human-in-the-loop
│   └── tools/                     # 7 tool implementations
│       ├── artifact_tools.py      # Side-channel store, file discovery + classification
│       ├── xml_parser.py          # DataStage XML parsing (ET, no LLM)
│       ├── sql_tools.py           # sqlglot-based SQL structure extraction
│       ├── datastage_tools.py     # Agent tools for XML exploration (side-channel)
│       ├── scratchpad.py          # Key-value note storage for agents
│       ├── blob_storage.py        # Azure Blob Storage operations
│       └── result.py              # ok/fail response helpers
├── docs/ETL_use_case/             # Sephora's source materials (DataStage XML, SPs, DDLs, views, schemas)
├── docs/Sephora/                  # Databricks schema reference files
├── initial/                       # Pre-loaded Sephora context from prior analysis
├── output/                        # Generated pipeline outputs
├── tests/                         # E2E and step-by-step test runners
└── claude/                        # Claude Code skill files (alternative lightweight pipeline)
```

---

## Key Design Patterns

1. **Side-channel stores:** File content stored in module-level dicts, not in LLM context. Prevents massive files (1.3M char XML) from consuming context windows. Both `_artifact_store` (orchestrator) and `_ds_store` (DataStage tools) use this pattern.

2. **Deterministic-first:** Every agent does Python/sqlglot extraction before LLM calls. LLM fills gaps and adds semantic understanding. Gates are deterministic (zero LLM cost) by default, with optional LLM checks gated behind a config flag.

3. **Source grounding:** Validators build text corpora from original source files and check that generated names (tables, columns, source files) actually exist. Catches hallucination before it propagates.

4. **Retry with feedback:** Gate errors are written to `step_validation` in state. Agents read this field on entry to know exactly what to fix. Retry messages include the specific errors. Max retries configurable per gate.

5. **Parallel execution:** Three parsers run in parallel (fan-out/fan-in). SQL generator plans first then generates independent stages in parallel (max concurrency 4). Config generator runs 3 files in parallel. All via `llm.batch()` or LangGraph edges.

6. **Template-based config generation:** Config generator copies target templates exactly, only changing values where data requires. This ensures output matches Sephora's existing AggregationApplication framework format.

---

## Perf-Optimizations Branch Changes

The worktree has 911 lines added across 7 files (recent commits):
- `api_server.py`: +438 lines (AI review streaming, UX improvements, demo mode with real run data, approval phase fix)
- `static/index.html`: +316 lines (enhanced dashboard UI)
- `agents/datastage_parser.py`: refactored parsing
- `agents/orchestrator.py`: +83 lines (expanded artifact handling)
- `graph.py`: +7 lines (gate_llm_checks config flag)
- `tools/artifact_tools.py`: +19 lines (classification improvements)
- `pipeline_config.yaml`: +2 lines (new config options)
- Fix: warnings deduct 0.2 from score, concurrency bump, GeneratorExit traceback fix, demo mode approval, ZIP download fix
