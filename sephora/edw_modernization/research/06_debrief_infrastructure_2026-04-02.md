# 06 - Debrief: Infrastructure and Performance

**Source:** /sephora/edw_modernization/source/saurav-colin_4-2-2026.txt
**Source Date:** 2026-04-02 (Demo Prep Call)
**Document Set:** 06 (Saurav/Colin Demo Prep)
**Pass:** Focused deep dive on infrastructure, performance, and LangSmith tracing

---

## Azure AI Foundry: Quotas and Throttling

### Current Quota Allocation
- Both Claude Opus and Claude Sonnet are provisioned through Azure AI Foundry.
- Current quota: **75,000 tokens** for both Opus and Sonnet.
- Colin confirmed this by reviewing the Foundry settings during the call: "You have 75K quota for both Claude and for Opus and for Sana [Sonnet]."

### Quota Increase Request
- Colin submitted quota increase requests for both Opus and Sonnet during the call itself.
- Requested increase: **4-5X** over the current 75K baseline (i.e., targeting 300K-375K tokens per model).
- Colin's exact words: "I put in the two quota requests both for Opus and for Sonnet. For basically a 4X 5X improvement on the token overhead."
- No guarantee of approval or timeline. Colin acknowledged: "We'll see if that happens. I don't know, but you know, fingers crossed."

### Concurrency and 529 Errors
- Maximum concurrency is currently set to **4 parallel requests**.
- Saurav tested higher concurrency previously and hit frequent **529 errors** (rate limit / overloaded responses from the Azure endpoint).
- Saurav's explanation: "Previously when I was trying it, I was hitting like a lot of times what do you call 529 errors, so that's why I kept it as 4."
- The concurrency of 4 is a pragmatic cap. With 7-8 files to process in parallel, the system sends them in two batches of 4 rather than attempting all at once and triggering throttle responses.
- Saurav mentioned he could try increasing to 8 or 9 concurrency if the quota increase comes through, specifically for the demo: "If it totally works out, I can try this with what you call 8 or 9 concurrency... just so that all our parallel process fire like properly."
- The execution log on the front end visually indicates when throttling is occurring.

### Impact on Demo Timing
- Throttling is the primary reason the pipeline runs slower than expected.
- Colin's assessment: "I think what's happening right now is you're just getting throttled. I think that's all that's happening right now."
- The slowness is not a code issue; it is an external constraint from Azure rate limits.

---

## Model Selection Strategy

### Not All-Opus
- The pipeline does **not** use Opus for every stage. Saurav explicitly corrected this assumption.
- Saurav: "No, not all [Opus]. Like for SQL generation we are using Opus. For what do you call pattern mapping we are using Opus. So like the heavy task in which we need like more thinking type and a lot of profiles to look at."

### Opus Use Cases (Heavy Tasks)
1. **Pattern Mapping** -- Uses a single Opus call. This stage creates a translation dictionary from SQL to Spark using target examples and extracted column names. Saurav described it as "one Opus call because it is like what do you call a big process."
2. **SQL-to-Spark Generation** -- The core generation step. Opus is used here because the three-step process (planning, independent stage generation, dependent stage generation) requires deep reasoning about business logic, dependency graphs, and transformation sequencing.
3. **Context Window Advantage** -- Opus provides a 1 million token context window. Saurav noted: "With Opus you were getting like 1,000,000 contacts [context], though we do not need that much, but still it is good to have."

### Sonnet Use Cases (Lighter Tasks)
- Sonnet handles lighter, faster tasks where deep reasoning is not required.
- Specific Sonnet stages were not enumerated in detail during this call, but the distinction is clear: parsing, deterministic gate checks with LLM components, configuration generation (pipeline YAML, deployment YAML, HQL), and validation-phase LLM checks are candidates for Sonnet given their lower reasoning demands.

### Rationale
- The split is driven by task complexity, not cost alone. Opus is reserved for stages where the model must hold large amounts of context (all source files, target examples, mapping dictionaries) and perform multi-step reasoning (dependency graph construction, business logic validation).

---

## LangSmith Tracing

### Connection and Purpose
- LangSmith is connected to the backend for **tracing only**. It is not used for development (Saurav considered using LangSmith's Playground/Studio for development but avoided it due to potential licensing costs).
- Saurav: "We are currently using Langsmith just for tracing. On the back end we did use like Langsmith."

### Waterfall View
- LangSmith's primary visualization is the **waterfall view**, which shows every API call and node execution across the entire pipeline run.
- It displays the full timeline of the pipeline: orchestrator start, parallel parsing stages, pattern mapping, SQL generation, gates, configuration generation, validation.
- Parallel execution is visually apparent: stages that start at the same timestamp line appear at the same horizontal position. Saurav demonstrated: "If you see here these are all starting at like the same line. So these are like 4 files firing in parallel with these stages firing in parallel, so 3 stages. So it's like 7-8 request going in parallel."

### Node Color Coding
- **Blue nodes** = LangGraph stage level (e.g., "pattern mapper," "SQL generator," "gate SQL"). These represent the logical stages of the pipeline.
- **Orange nodes** = LLM call level (e.g., individual Claude API calls, chat/anthropic calls). These represent the actual model invocations within each stage.
- Saurav: "If we want individual like what you call LLM level outputs, you can click on these chat and tropics [chat anthropic]. If we want stage level output we can click on those blue pattern mapper or SQL generator."

### Inspecting Input/Output
- Clicking on any node (blue or orange) reveals its **input and output** data.
- For blue (stage-level) nodes: shows the LangGraph state at entry and exit of that stage. This includes all accumulated fields -- source artifacts, parsed results, generated SQL, validation results.
- For orange (LLM-level) nodes: shows the exact prompt sent to the model and the response received.
- Example from the call: clicking on the SQL Spark Generator node shows the current state with spark_generator as null (before execution) and the SQL interpreter output from the previous parsing stage, including extracted business rules for each file.

### Gate Inspection in LangSmith
- Gate nodes are also inspectable. Clicking a gate shows its **step validation** results.
- Deterministic checks appear as structured validation objects (e.g., "four out of five are passed").
- LLM-based gate checks appear separately (e.g., "gate LLM check" with 17 findings on business logic).
- All outputs use structured nested JSON objects. Saurav emphasized the structured output design: "I put in a lot of [effort] because I was thinking this like what will be a good example to like even if we want to replicate any other agentic demo."

### Threads vs. Runs
- LangSmith has two navigation paradigms:
  - **Runs view**: Shows individual runs listed by run ID. Each run appears as a separate entry.
  - **Threads view**: Shows individual pipeline executions end-to-end, including all retries and continuation within a single thread.
- Saurav directed Colin to use the threads view for a complete picture: "Rather than in runs, you can check this in threads."
- Within a thread, toggle between "trace" and "turn" views. The waterfall view is available as a filter option at the top of the thread view.

### Latency (Not Real-Time)
- LangSmith does **not** update in real-time. There is a delay of approximately **1-2 minutes** before a completed run appears.
- Saurav: "It is not like real time, but maybe couple of minute, not 15 minutes."
- The front-end execution log is the real-time monitoring tool. LangSmith is the post-hoc deep-inspection tool.
- Colin observed a 17-minute gap between the current run and the last visible run in LangSmith, which Saurav attributed to the normal delay plus the run still being in progress.

### LangSmith API
- Saurav mentioned that LangSmith provides a backend API. If Sephora wants to build a custom dashboard using LangSmith data (rather than surfacing everything on the front end), they can hook directly into that API.
- Saurav: "We even have like a what do you call API available on back end for like Langsmith. So if you want to access any of those details or just create like a dashboard just based on those details, we can like directly hook their [into it]."

---

## LangGraph State Management

### State as a JSON Object
- The LangGraph state is a single **JSON object** that is built incrementally throughout the pipeline execution.
- Each node in the graph fills in its designated portion of the state object. As Saurav described: "You can consider them as like a JSON object which we are building throughout this whole LangGraph and whenever we have one field of that JSON object present, it goes in and fills in that part of the object."

### State Availability
- Every field in the state object is available to surface on the front end at any point.
- Saurav deliberately chose **not** to surface everything to avoid information overload: "We have a lot of thing which we have not surfaced on like the front end... I did not want to make like the demo itself like too info intensive."
- The full state is always visible in LangSmith by clicking on any node's input/output.

### Chat Thread Architecture for Retries
- Each node internally maintains a **chat thread** model. This is critical for the retry and auto-fix mechanisms.
- When a retry occurs, the previous context, previous generation, and the rejection reason (including the verdict on why it was rejected or what was marked as false positive) are all fed back into the chat thread.
- Saurav: "You can think of each of these nodes as like suppose individual chat threads. So it keeps in mind the previous context as well as previous generation."
- This means retries are not blind re-runs; they carry forward the full conversation history of what was generated and why it was rejected.

### Fields Tracked in State
Based on transcript details, the state object includes at minimum:
- Source artifacts (11 files for the demo pipeline)
- Schemas and column definitions
- Pipeline selection and run ID
- Data stage parser output (job stages, transformations, source/target connections, data flow)
- SQL interpreter output (stored procedures, table joins, CTEs, temp tables, business logic, aggregation patterns)
- DDL parser output (table names, column names, data types, typecasts, constraints, precision)
- Pattern mapping dictionary (SQL-to-Spark translation)
- Spark generation plan (dependency graph, independent vs. dependent stages)
- Generated Spark SQL
- Configuration files (pipeline YAML, deployment YAML, HQL/DDL)
- Gate validation results (deterministic and LLM-based)
- Review findings and auto-fix results

---

## Performance Characteristics

### What Runs Fast
- **Deterministic gate checks**: Saurav noted these "can easily finish" quickly. The time in gate stages is dominated by the LLM-based checks added to gates, not the deterministic validations.
- **Data stage parsing** and **DDL parsing**: These are lighter stages. Saurav characterized them as taking "a small amount of time."
- **Configuration generation**: Three parallel agents (pipeline YAML, deployment YAML, HQL) fire simultaneously and complete relatively quickly since they use the already-generated SQL as context.

### What Runs Slow
- **Pattern mapping**: This is "a big process" that "takes time." It is a single Opus call that must process all target examples and create a complete translation dictionary.
- **SQL-to-Spark generation**: The three-step process (plan, generate independent stages, generate dependent stages) is the heaviest computation in the pipeline. With 22+ transformations and a max concurrency of 4, the independent stages alone require multiple batches.
- **LLM-based gate checks (especially G4)**: The business logic validation in the SQL gate adds significant time. Saurav added this check specifically to avoid wasting tokens downstream: previously, a bad SQL generation would pass through config generation, deployment YAML generation, HQL generation, and review before being caught and retried -- burning tokens on 3-4 additional nodes unnecessarily.

### Total Pipeline Duration
- The displayed duration includes human review time (the timer does not pause during human-in-the-loop steps).
- Saurav confirmed: "This is like including the retries as well as like the time it took from what you call at the end of human approval as well. So suppose it was sitting there 10-20 minutes just for like human approval so it will count that time as well."
- The pipeline appeared to take longer than expected during the call, but Colin and Saurav attributed this to the conversation time being included and to throttling.

---

## The Caching Idea

### Proposal
- Saurav proposed a "click through stages" button that would load **cached data from a previous successful run** while the real pipeline runs in the background.
- Saurav: "Maybe add a button which can like move through the stages and while you are talking just click through the stages and it will load all the data as it has already processed once and cached once and the real process may be running in the background just because it is taking time."

### Status
- **Not implemented.** This was discussed as a contingency option if throttling makes the live demo too slow.
- Colin acknowledged it as a reasonable idea but believed the primary issue was throttling, not inherent slowness: "Even for the cache run, because it could still take like a reasonable amount of time per block. But I think what's happening right now is you're just getting throttled."

### When This Would Be Needed
- Only if the quota increase request is denied and throttling remains severe enough to make a live demo impractical. The approach would let the presenter walk through results while the actual pipeline catches up in the background.

---

## PostgreSQL Setup

### Role
- PostgreSQL is used for **run history** storage. The pipeline runs table stores run IDs, project names, timestamps, status (pass/pending/failed), and associated metadata for each pipeline execution.
- The front-end dashboard reads from this table to display the list of previous runs and their outcomes.

### Runtime Characteristics
- Lightweight and always running. Colin and Saurav both leave their PostgreSQL containers running at all times.
- Colin: "That's why I like Postgres, because it's lightweight and you don't even have to think about it."
- Saurav: "I don't even like stop my PG containers anytime. Like I don't remember like ever stopping them apart from when they crashed."

### Missing Table on Colin's Machine
- After pulling the latest code, Colin's machine was missing the **pipeline_runs table**. The table existed on Saurav's machine but Saurav had not included an auto-creation command in the setup.
- Symptom: the pipeline completed successfully but the run history page failed to load / showed errors because it could not write to or read from the missing table.
- Saurav's fix: adding a check that creates the table if it does not exist. Saurav: "It was basically missing like a check if the DB like the table was not present. So I'm just adding if it is not present, just create it."
- Saurav also planned to **pre-populate** the table with 3-4 sample runs (a couple of passes, one pending, one failed) so the dashboard looks populated for the demo without requiring 40-50 actual runs.

---

## TiDB Discussion (Rejected Alternative)

### Context
- Ascari (another team member working on Cisco) suggested **TiDB**, a distributed database, for that engagement.
- Saurav investigated TiDB independently. His assessment: TiDB provides good handling for large distributed data across regions, but it is a port of TiDB (the distributed SQL database) and introduces significant overhead.

### Why It Was Rejected
- Both Colin and Saurav agreed it is **overkill** for the use cases they handle.
- Saurav's math: even 1,000 developers doing 100 PRs per day is only 100,000 records per day -- well within PostgreSQL's capacity.
- Colin added that PostgreSQL's worst case under load is connection pooling (requests queue up), not failure. As long as the system does not enter a sustained traffic jam state, the queue drains naturally.
- Colin's engineering principle: "If we've done math and we have numbers that we can show that something like that's necessary, it's necessary. But if we don't have math and we're just guessing, that's where engineering is not there."
- Classic over-provisioning anti-pattern: "The classic case in IT is whenever people way over provision things because they're just not sure... for their 10 users that will use this, they want Kubernetes."

---

## Docker and Poetry Setup

### Docker Compose
- The environment is set up using **Docker Compose**.
- The PostgreSQL container is the primary Docker-managed service.
- Command to start: `docker compose up` (specifically for the PG container).
- Saurav referenced it casually: "PG up. Yeah, Docker Compose."

### Poetry for Python Dependencies
- Python dependencies are managed via **Poetry**.
- After pulling the latest code, Colin ran `poetry install` to sync dependencies.
- This was part of Colin's setup sequence: pull latest code, stash any conflicting local files, run `poetry install`, then `docker compose up` for PostgreSQL.

### .env File
- The pipeline uses an `.env` file for configuration (Azure API keys, LangSmith project ID, database connection strings, etc.).
- Saurav confirmed no changes were made to the `.env` file in the latest update: "Nothing changed in .env."

---

## What Colin Needs to Run on His Machine

### Setup Sequence (Confirmed During Call)
1. `git pull` to get the latest code.
2. `git stash` any conflicting local files (some target files were being ignored by `.gitignore`).
3. `poetry install` to update Python dependencies.
4. `docker compose up` to start the PostgreSQL container.
5. Ensure the `.env` file is populated with correct Azure AI Foundry credentials and LangSmith project ID.
6. Run the dashboard application (the primary front-end entry point, not the Streamlit version).

### Outstanding Items After Call
1. **Pipeline runs table creation**: Saurav committed to adding auto-creation logic so the table is created if it does not exist on Colin's machine.
2. **Pre-populated demo data**: Saurav planned to add a database seeding command that inserts 3-4 sample runs with different statuses (pass, pending, failed) to populate the dashboard for demo purposes.
3. **Quota increase**: Colin submitted requests through Azure AI Foundry for both Opus and Sonnet. Approval pending.
4. **LangSmith access**: Colin connected to the same LangSmith project ID as Saurav. Confirmed working, with the expected 1-2 minute delay on run visibility.

---

## Front End: Implementation Details

### Technology
- **Vanilla HTML/CSS/JavaScript** -- no framework (no React, no Vue, no Angular).
- Saurav acknowledged the trade-off: "This is like not based on any framework for the front end, correct. So we have very stick with glue kind of thing for the front end part."
- Despite no framework, Colin noted it looks professional enough that it appears framework-built: "It looks like we used a framework, frankly, but you know that's a good thing."

### Execution Log with Live Spinners
- The execution log at the bottom of the dashboard shows live status updates with timers.
- Each agent stage gets a spinner with elapsed time (e.g., "parsing XML structure 4 second, 5 second").
- Spinners update whenever an agent completes its stage. The timer tracks how long each particular agent has been running.
- When a spinner disappears, it typically means the response has been received and the system is waiting for the next stage (e.g., a gate check) to complete.

### DAG Visualization Limitation
- The DAG visualization (node lighting) works correctly for the initial forward pass.
- **Known issue**: If "reject and retry" is clicked (as opposed to "auto fix"), the pipeline returns to earlier stages, but the DAG node lighting does not correctly reset to show the retry path. The execution log and backend still function properly; the visual representation of which DAG nodes are lit is what gets confused.
- Saurav flagged this explicitly: "The DAG light up get messed up whenever we are retrying on that... using that button."
- Colin's decision for the demo: stick with "auto fix" rather than "reject and retry" to avoid this visual issue.

### Streamlit Alternative
- A Streamlit version also exists with recent changes, but Saurav described it as "not visually that appealing" compared to the custom dashboard. The custom HTML/CSS/JS dashboard is the primary demo vehicle.

---

## Summary: Infrastructure Stack

| Component | Role | Notes |
|---|---|---|
| Azure AI Foundry | LLM API gateway | 75K quota per model, increase requested |
| Claude Opus | Heavy reasoning tasks | Pattern mapping, SQL generation |
| Claude Sonnet | Lighter/faster tasks | Parsing, validation, config generation |
| LangGraph | Pipeline orchestration | State management via JSON object |
| LangSmith | Backend tracing | Waterfall view, not real-time (1-2 min delay) |
| PostgreSQL | Run history storage | Docker-managed, lightweight |
| Docker Compose | Environment setup | Primarily for PostgreSQL container |
| Poetry | Python dependency management | Standard Python tooling |
| Vanilla HTML/CSS/JS | Front-end dashboard | No framework, custom-built execution log |
| SQL Glot | Deterministic SQL parsing | Used in SQL interpreter and DDL parser |
| Highlight.js | Syntax highlighting | Added for code preview in the UI |
