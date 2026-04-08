# Demo Prep: Audience Alignment

**Date:** 2026-04-02
**Demo time:** 6:00 PM ET
**Audience:** Andrew Ho, Grishi (Gariashi Chakrabarty)

---

## Who Is in the Room

### Andrew Ho (Director, Enterprise Reporting)
- **What he cares about:** Strategic feasibility. Can this actually compress a 3-year program to 1-1.5 years? Is the agentic approach real or just vendor talk?
- **His own words (Set 03):** "I just want to make sure the wild thinking is not wild, it's real, it can be done."
- **His vision (Set 03):** He independently articulated multi-agent orchestration before Colin pitched it. Multiple small specialized agents, one master orchestrator, parallel execution. He sees this as redirecting manual contractor spend into upfront agent development.
- **His concern (Set 04):** Expanded scope. Agents should help with BOTH report migration AND table data migration from SQL Server to Databricks. Not just one side.
- **What impresses him:** Honesty about limitations, proof over promises, scalability argument ("the work to do 100 reports is about the same as 1,000 once the agents are in place").

### Grishi (Director, Data Engineering, BI and Analytics)
- **What she cares about:** Execution reality. She and her team do this work every day. They already use Claude and get 30% efficiency. She needs to see that agents do dramatically more than that.
- **Her own words (Set 03):** "I just want to see that you guys have done something like this, that you've created agents capable of doing these kind of things."
- **Her pain (Set 04):** The manual workflow is: navigate Cognos, open report, extract SQL, run through AI, get new SQL, snap it back. Each step is human-limited. Claude helps with one step (SQL conversion) but the rest is still manual.
- **What impresses her:** Working code, not slides. Specificity. When Colin walked through the schema mapping three-step workflow in Set 03, that was the moment she engaged most deeply.

---

## What They Explicitly Said They Want to See

From Malika's March 6 email (Set 04a, written on behalf of the technical team including Grishi):

1. **Agent-driven orchestration across multiple tools** (not just one agent doing one thing)
2. **End-to-end workflow automation** (extraction, interpretation, and downstream execution coordinated by agents)
3. **Task sequencing and dependency handling** (how the pipeline manages what runs when)
4. **How the agent handles legacy data pipeline modernization** (parsing DataStage XML, stored procedures, views)
5. **Generating Databricks-compatible output** (Spark SQL + YAML configs for the AggregationApplication framework)

From Andrew directly (Set 04):
6. **That the system can learn** ("after we've approved it, it adds that as a knowledge base so the next generation knows")
7. **That it scales independent of people** ("once we have the agents going, the work for 100 reports is the same as 1,000")

---

## What They Explicitly Said They Do NOT Want

1. **Just code translation.** Malika (Set 04a): "Code translation alone would not be the primary area we are looking to evaluate." They already do this with Claude internally.
2. **A product pitch.** Andrew (Set 03): "I know for a fact, right now outside there's no one has a package... So now I'm just kind of poking a hole and saying, who out there can help us to create this." They want a custom solution.
3. **Spaghetti code notebooks.** Sergey (Set 04): "Lake bridge produces spaghetti code. Hundreds of windows inside a notebook. How to maintain it? It will be a nightmare to debug." Output MUST be YAML configs + Spark SQL that fits their existing framework.
4. **Theory without proof.** Both Andrew and Grishi demanded a demo/POC before committing in Set 03. They don't want another vendor presentation.

---

## Demo Flow Aligned to Their Priorities

### Opening (2 min)
- Do NOT open with slides or a pitch. Open with the dashboard.
- One sentence: "Everything you see was built specifically around your DataStage jobs, stored procedures, and source schemas over the last two weeks."
- Then start the pipeline.

### Phase 1: Show the Orchestrator Loading Their Actual Files (2 min)
**Maps to:** "Can it handle our specific data?"
- Click "Load Demo Files" (their 9 actual files are preloaded)
- Point out: these are Sephora's files. DataStage XML, stored procedures, DDLs, views, Databricks schemas, target framework examples.
- Click "Start Pipeline"

### Phase 2: Watch the Execution Log (3-5 min while pipeline runs)
**Maps to:** "End-to-end workflow automation" and "task sequencing"
- The execution log with live spinners shows each agent step in real time
- Call out when parsers fire in parallel: "Three agents are working simultaneously. DataStage parser is analyzing the XML structure, SQL interpreter is extracting business rules from stored procedures, DDL parser is mapping column types."
- When gates pass: "Each gate runs deterministic checks. No LLM cost. It verifies the tables actually exist in your source files, not hallucinated."
- This directly addresses Andrew's orchestration vision and Grishi's "I want to see agents working" demand.

### Phase 3: Walk Through Gate Results (2-3 min)
**Maps to:** "How does it handle quality?"
- Open the gate dropdowns. Show pass/fail checks.
- Point out: "Column mapping, source table grounding, SQL syntax validation. These are all deterministic. The LLM checks only run after the deterministic checks pass, which saves tokens."
- This addresses Grishi's data engineering instincts. She will want to see specifics.

### Phase 4: Review Step (3-5 min)
**Maps to:** "Human-in-the-loop" and "confidence score"
- When the pipeline reaches the review step, explain the score: "97% confidence means the remaining items are not errors. They are small conversion items flagged for a quick human review."
- Show the issues: warnings and infos, never errors (orchestrator retries until errors resolve).
- Explain: "The issues are things like implicit decimal casts and performance considerations. An engineer would look at these and say 'yeah, I see this all the time.' That is the human-in-the-loop value."
- Click "AI Review" to show the audit feature.

### Phase 5: Auto-Fix (2-3 min)
**Maps to:** "Can the system self-correct?"
- Click Auto-Fix (NOT reject-and-retry).
- Explain: "This is like Claude Code for your pipeline. It takes the generated SQL, treats everything as files, and makes surgical edits based on the review findings."
- This is the feature that will land hardest with Grishi because it eliminates the manual iteration she described in Set 04 (run through AI, check output, go back and fix, run again).

### Phase 6: Approve and Download (2 min)
**Maps to:** "Does the output fit our framework?"
- Click Approve.
- Download the individual files. Show them:
  - Spark SQL (syntax highlighted, production-ready)
  - Pipeline YAML (matches their existing AggregationApplication format)
  - Deployment YAML (matches their deployment pattern)
  - Create.HQL (table definition)
- Point out: "These are the three YAML files Sergey described. They plug directly into your existing framework. No new code, no notebooks, no new framework to learn."

### Phase 7: LangSmith (optional, for deep questions)
**Maps to:** Andrew's technical depth, Grishi's "show me the details"
- If anyone asks "how does it work under the hood?" or wants to see the parallel execution or the dependency graph: open LangSmith.
- Waterfall view shows every API call, every node, parallel execution visually.
- "No question you have cannot be answered from this."

---

## Talking Points Mapped to Their Concerns

| Their Concern | What to Say |
|---------------|-------------|
| "Is this real?" (Andrew) | "The pipeline just processed your actual DataStage XML, stored procedures, and schemas. The output plugs into your existing framework." |
| "Does it beat Claude alone?" (Grishi, 30% baseline) | "Your team is doing one step with Claude. This automates the entire workflow. Parsing, interpretation, mapping, generation, validation, and review. The 30% gains become available across every step, and they compound." |
| "What about our old software versions?" | "We confirmed Cognos and DataStage both have Java/.NET SDKs going back to 2003. For this demo we used exported files. In production, MCP connectivity replaces the manual export step." |
| "Does it fit our framework?" (Sergey's YAML requirement) | "The output is exactly what Sergey described: pipeline YAML, deployment YAML, and HQL. No Scala code, no notebooks. These config files work with your existing AggregationApplication framework." |
| "Can it scale?" (Andrew) | "Once the agents and patterns are in place, the work for 100 reports is the same as for 1,000. The knowledge base learns from each approved run." |
| "What about the Cognos MCP?" | "The MCP connector is the natural next step. A Java hook exists for Cognos. Once we have access to your environment, the pipeline can pull source files and push output directly, making the full workflow autonomous." |
| "What is the next step?" | "We can deploy this on Azure with secure credentials so your team can try the workflow themselves. Time-bound access, your data already loaded. Or we can schedule a deeper session." |

---

## Things to Avoid

1. **Do NOT click "Reject and Retry"** (DAG animation breaks)
2. **Do NOT interact with configuration dropdowns** (non-functional placeholders)
3. **Do NOT mention cost per run or token counts** (they'll multiply by 6,000 reports)
4. **Do NOT say "migration"** (Mani corrected this in Set 02: "re-engineering, not migration")
5. **Do NOT oversell the MCP** (it requires their environment access, which means a contract)
6. **Do NOT dwell on the UI** (if technical people want depth, pivot to LangSmith)
7. **Do NOT use the word "product"** (this is a custom solution built for them)
