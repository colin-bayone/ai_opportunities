# Demo Gap Analysis

**Date:** 2026-04-02
**Method:** Cross-referenced every explicit request from Sephora (Sets 03, 04, 04a) against what the demo actually demonstrates.

---

## Methodology

Reviewed:
- Malika's March 6 scope email (Set 04a) listing 9 specific capabilities to evaluate
- Andrew's statements from Sets 03 and 04 on what he needs to see
- Grishi's statements from Sets 03 and 04 on what gives her confidence
- Sergey's output format requirements from Set 04
- Known demo limitations from Set 06 (Saurav's walkthrough)

Each item is rated: COVERED (demo shows it), PARTIAL (demo touches it but not fully), or GAP (demo does not show it, needs a talking point).

---

## Item-by-Item Assessment

### 1. Agent-driven orchestration across multiple tools
**Source:** Malika email (Set 04a), Andrew (Set 03)
**Rating:** COVERED
**Evidence:** The pipeline has 10 agent nodes coordinated by a LangGraph StateGraph. Orchestrator, three parallel parsers, pattern mapper, SQL generator, config generator, schema validator, review agent, human approval. The execution log shows this live.

### 2. End-to-end workflow automation
**Source:** Malika email (Set 04a)
**Rating:** COVERED
**Evidence:** Pipeline runs from file upload to downloadable YAML/SQL/HQL output with no manual intervention except the approval step. This is the full workflow Grishi described doing manually in Set 04.

### 3. Task sequencing and dependency handling
**Source:** Malika email (Set 04a)
**Rating:** COVERED
**Evidence:** Gates enforce sequencing (orchestrator before parsers, parsers before mapper, etc.). The SQL generator builds a dependency graph of independent vs dependent stages. Parallel execution is visible in the execution log.

### 4. Parse DataStage job XML
**Source:** Malika email (Set 04a)
**Rating:** COVERED
**Evidence:** DataStage parser extracts job stages, transformations, source/target connections, embedded SQL, column definitions from the actual DS_Jobs_inventory.xml Sephora provided.

### 5. Interpret SQL Server stored procedures and views
**Source:** Malika email (Set 04a)
**Rating:** COVERED
**Evidence:** SQL interpreter analyzes SP_usp_Update_Inv_Periodic.txt and views using sqlglot + LLM. Extracts table joins, CTEs, temp tables, business logic, aggregation patterns.

### 6. Map patterns to Spark-based transformations
**Source:** Malika email (Set 04a)
**Rating:** COVERED
**Evidence:** Pattern mapper creates SQL-to-Spark translation dictionary from parser outputs + Sephora's target examples.

### 7. Generate Databricks-compatible output (Spark SQL + YAML + deployment)
**Source:** Malika email (Set 04a), Sergey (Set 04)
**Rating:** COVERED
**Evidence:** Pipeline produces all four outputs: Spark SQL, pipeline YAML, deployment YAML, create.HQL. These match Sergey's AggregationApplication framework format. Config generator copies target templates exactly.

### 8. MCP server / integration layer for Cognos
**Source:** Malika email (Set 04a), item #1 on her list
**Rating:** GAP
**Detail:** The demo uses exported XML files, not a live MCP connection to Cognos. Malika explicitly listed "Demonstration of the MCP server or integration layer for Cognos" as the first capability she wanted to see.
**Talking point:** "The MCP connector architecture is designed and a Java hook exists for Cognos. For this demo, we used your exported files because live MCP requires access to your Cognos environment. The MCP connector is the natural next step once we have environment access, and it replaces the manual export entirely."
**Risk level:** LOW. Colin already positioned this in his March 9 email (Set 04a) and Sephora chose Track B (ETL) knowing MCP was deferred. But if Andrew or Grishi asks about it directly, this talking point must be crisp.

### 9. Automated extraction of report metadata from Cognos
**Source:** Malika email (Set 04a)
**Rating:** GAP (same as #8)
**Detail:** The orchestrator loads files from a directory, not from Cognos directly. In production, the orchestrator would use MCP tools to pull from Cognos programmatically.
**Talking point:** Same as #8. The orchestrator already has a ReAct mode that uses tools for discovery. In production, those tools would be MCP connectors to Cognos and DataStage.

### 10. Timeline compression evidence
**Source:** Andrew (Set 03): "this program can potentially shrink from three years to maybe a year or a year and a half"
**Rating:** PARTIAL
**Detail:** The demo shows the pipeline completing in ~9.5 minutes for one use case. But there is no explicit comparison to "here is how long this takes your team manually." Andrew's core question is about timeline compression.
**Talking point:** "Your team's manual process for one pipeline involves multiple people across multiple days: extract from Cognos, analyze SQL, map schemas, convert code, generate configs, validate, review. This pipeline does all of that in under 10 minutes. And critically, the same pipeline handles the next 100 pipelines with the same effort because the knowledge base accumulates patterns."
**Risk level:** MEDIUM. Andrew may push for numbers. Do not commit to a timeline. Say: "The exact compression depends on how similar your pipelines are to each other. The more pattern consistency, the faster the flywheel. We would scope that in the engagement."

### 11. Comparison to their current Claude usage (30% baseline)
**Source:** Grishi (Set 03): her team gets 30% efficiency with Claude on SQL conversion
**Rating:** PARTIAL
**Detail:** The demo does not explicitly benchmark against their current workflow. It shows a full pipeline, but does not say "your current approach does X, ours does Y."
**Talking point:** "Your team is using Claude for one step in the workflow: SQL conversion. That gets you 30% on that step. This pipeline automates the entire workflow: parsing, interpretation, mapping, generation, validation, and review. The efficiency gain compounds across all steps, and the deterministic gates ensure consistency that manual Claude interactions cannot."
**Risk level:** LOW. Grishi will see this herself when the pipeline runs. She knows her manual workflow.

### 12. Running on Sephora's infrastructure / Databricks
**Source:** Andrew (Set 03): wants it on their ecosystem. Grishi (Set 03): "ideal would be Databricks"
**Rating:** GAP
**Detail:** The demo runs on BayOne's local/Azure infrastructure, not on Sephora's Databricks. The output targets Databricks, but the pipeline itself does not run there.
**Talking point:** "This is running on Azure today. We can deploy it on your infrastructure. We designed it to meet you where you live. The Azure deployment with time-bound credentials is available this week if your team wants to try the workflow directly."
**Risk level:** LOW. This was already addressed in the March 9 email where Sephora chose the "disconnected approach" (demo on BayOne's setup). The Azure deployment offer closes this gap.

### 13. Table data migration (SQL Server → Databricks)
**Source:** Andrew (Set 04): "I just want to make sure we cover both sides of the house, not just one side"
**Rating:** GAP
**Detail:** The demo shows ETL pipeline conversion (DataStage job → Spark SQL + YAML). It does NOT show actual data migration from SQL Server tables to Databricks. Andrew explicitly expanded scope to include this.
**Talking point:** "This demo focuses on the pipeline conversion side: taking your DataStage jobs and generating Databricks-ready configs. The data migration side, moving actual table data from SQL Server to Databricks, is a complementary capability that we would scope as part of the engagement. The same agent architecture applies."
**Risk level:** MEDIUM. Andrew was explicit about wanting both sides covered. He may ask. Be clear that this is engagement scope, not PoC scope.

### 14. Knowledge base / learning from approved patterns
**Source:** Andrew (Set 04), Saurav (Set 06)
**Rating:** PARTIAL
**Detail:** The knowledge base feature exists (approved patterns saved to JSON for future runs). But the demo only runs one use case, so the learning effect cannot be demonstrated live.
**Talking point:** "After you approve the output, those patterns get saved to a knowledge base. The next time the pipeline encounters a similar transformation, it already knows the right approach. The system gets smarter with every run. In a production engagement with hundreds of pipelines, this is where the real acceleration happens."
**Risk level:** LOW. Conceptual, easy to explain.

### 15. Multiple pipeline types / generalization beyond inventory_periodic_daily
**Source:** Mani (Set 01): thousands of reports across finance, supply chain, stores, e-commerce
**Rating:** GAP
**Detail:** Demo only runs one pipeline (inventory_periodic_daily). The run history has hardcoded entries to show variety, but the actual pipeline has only been tested on one use case.
**Talking point:** "We built this around the specific files your team provided. In a production engagement, the orchestrator would handle multiple pipeline types. The architecture is the same; the patterns are what change per pipeline. That is exactly what the knowledge base is for."
**Risk level:** LOW for this demo. They chose the scope. But be ready if Andrew asks about generalization.

---

## Summary Matrix

| # | Capability | Rating | Risk |
|---|-----------|--------|------|
| 1 | Agent orchestration across tools | COVERED | - |
| 2 | End-to-end workflow automation | COVERED | - |
| 3 | Task sequencing and dependency | COVERED | - |
| 4 | Parse DataStage XML | COVERED | - |
| 5 | Interpret stored procedures/views | COVERED | - |
| 6 | Map patterns to Spark | COVERED | - |
| 7 | Generate YAML + SQL + HQL output | COVERED | - |
| 8 | MCP server for Cognos | GAP | LOW |
| 9 | Automated Cognos extraction | GAP | LOW |
| 10 | Timeline compression evidence | PARTIAL | MEDIUM |
| 11 | Comparison to current Claude usage | PARTIAL | LOW |
| 12 | Running on Sephora infrastructure | GAP | LOW |
| 13 | Table data migration | GAP | MEDIUM |
| 14 | Knowledge base learning | PARTIAL | LOW |
| 15 | Multiple pipeline generalization | GAP | LOW |

**Bottom line:** 7 of 15 items are fully COVERED. 3 are PARTIAL with easy talking points. 5 are GAPS, but all have prepared responses and none are deal-breakers. The two MEDIUM-risk items (timeline compression, table data migration) require confident but careful framing: timeline compression is real but should not be committed to with numbers, and table data migration is engagement scope not PoC scope.

---

## Pre-Demo Checklist

- [ ] Pull latest code from worktree
- [ ] Verify Postgres container is running
- [ ] Verify pipeline_runs table exists (Saurav's fix)
- [ ] Check if Azure quota increase was approved
- [ ] Do one full test run to warm the pipeline
- [ ] Have LangSmith open in a separate tab
- [ ] Have this gap analysis open for quick reference on talking points
