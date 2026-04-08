# 06 - Debrief: Demo Talking Points and Strategic Framing

**Source:** /sephora/edw_modernization/source/saurav-colin_4-2-2026.txt
**Source Date:** 2026-04-02 (Demo Prep Call)
**Document Set:** 06 (Saurav/Colin Demo Prep)
**Pass:** Focused deep dive on talking points, strategic framing, and presentation strategy

---

## 1. Cognos MCP Positioning: The "Not for a Free PoC" Wedge

Colin confirmed during the call that a Java-based MCP hook exists for accessing Cognos, meaning MCP connectivity to Sephora's source systems is technically feasible. However, he explicitly framed this as a post-contract deliverable, not a PoC feature.

**Colin (line 793-805):** "I'm definitely gonna flag out for the Cognos MCP. We know we can do that. I checked and there's actually a Java, a Java MCP hook that you can use for accessing it, but... I'm going to try to tell them, you know, hey, not for a free PoC. And the good thing for us is the moment we have access to their internal systems, we've already got a contract. So you know, like the moment they give us actual access to Cognos, because they're going to want to see that. We've already got a deal in our hands. You know, I'm not going to do that for free for development for, you know, a very old platform like that."

### Strategic Logic

The reasoning is structural, not technical:

1. **MCP connectivity requires internal system access.** To hook into Cognos via MCP, BayOne needs credentials and network access to Sephora's Cognos environment. That is not something given to a vendor running a free proof of concept.
2. **Access implies contract.** The moment Sephora provisions access to Cognos for BayOne, that action itself signals a formal engagement is underway. No procurement or security team grants internal system access without a signed agreement.
3. **MCP becomes the natural "next step" pitch.** During the demo, Colin can acknowledge the MCP capability, demonstrate that the architecture supports it (the configuration panel has MCP connector placeholders), and position it as the first deliverable once the engagement begins. This creates a clean bridge from PoC approval to contract execution.

### What to Say in the Demo

Colin should mention the Java MCP hook exists, confirm BayOne has validated the approach, and then frame it as: "Once we have access to your Cognos environment -- which would come with the engagement -- we wire this in. The architecture already supports it." This positions MCP as a solved problem that requires access, not effort, keeping it out of the free PoC scope while signaling confidence.

---

## 2. Auto-Fix Framing: "Like Claude Code, Except You're in a Control Center"

The auto-fix feature was a significant addition to the demo. Saurav built it as an alternative to the reject-and-retry path, and Colin latched onto it as one of the strongest demo talking points.

**Colin (line 1345-1346):** "I'm gonna stick with the fix because that's a cool thing. I mean that's a really nice thing to see and even just to show them, hey, it's like Claude Code except you don't have to, you know, you get to be in the kind of the control center for all the different runs. You don't have to, you know, have individual Claude sessions like this, so that's super cool."

### How the Auto-Fix Works (for Demo Narration)

Saurav explained the mechanics clearly during the walkthrough:

**Saurav (line 540-553):** "So we already have our SQL file generated, correct? So it will treat that SQL file, your XML, Scala, everything else as a file. OK, it has tools to read those files and it has tools to edit those files. So you can think this like you are using Claude Code, you gave it everything in a file and you ask it then after the generation that go ahead and review this validation. As well as this generation. Then after it came up with the audit result, you said to it, yeah, go ahead and fix it. Then it opens the SQL, goes to that line number and fixes those exact things. So kind of like surgical edits rather than like full generation."

### Two Paths: Auto-Fix vs. Reject-and-Retry

The demo offers two remediation options at the review stage:

1. **Auto-fix (recommended for demo):** Takes the review findings and makes surgical, line-level edits to the existing generated SQL. Does not regenerate anything. Treats all artifacts as files, reads them, and applies targeted corrections. Re-runs validation after fixing, then returns to the review screen with updated results.
2. **Reject and retry:** Sends the run back to the SQL generator node, regenerating from that point forward through config generation, gates, and validation. This is a full regeneration cycle of 3-4 nodes.

**Saurav (line 525-527):** "I was just what you call kind of messing around with this. I found like the auto fix one, what you call more intuitive. Because we have already done like most of the work and then it comes down to like this final stage, correct. So we have like very small bugs found out."

### Why Auto-Fix Is the Demo Choice

Colin should use auto-fix during the demo for three reasons:

1. **It demonstrates intelligence, not brute force.** Surgical edits are more impressive than "throw it away and try again."
2. **It is faster.** Auto-fix does not re-run the entire generation pipeline.
3. **The DAG animation has a known issue with reject-and-retry.** Saurav flagged that clicking reject-and-retry brings the user to the DAG screen, but the DAG node lighting sequence gets confused during retries (line 1335-1336). The execution log still works properly, but the visual breaks. Auto-fix avoids this entirely.

### What to Say in the Demo

Frame auto-fix as: "Think of this as Claude Code for your migration pipeline. The system already generated the SQL. Now instead of regenerating everything, it reads the generated files, identifies the exact lines that need correction based on the review findings, and makes surgical edits -- just like a developer would in Claude Code. The difference is you are in a control center managing all of your conversion runs, not sitting in individual coding sessions."

---

## 3. LangSmith as the Technical Audience Satisfier

Colin and Saurav had an extended discussion about LangSmith's role versus the UI's role. Colin concluded that LangSmith is the tool that will satisfy technical evaluators, while the UI is the tool that will satisfy business stakeholders.

### What LangSmith Shows

Saurav walked Colin through the LangSmith tracing interface in detail:

- **Waterfall views** showing the full execution timeline, with each node's start time and duration visible (line 1009, line 1081)
- **Parallel execution visibility** -- you can see where stages like DDL parser, SQL interpreter, and data stage parser fire simultaneously, with "7-8 requests going in parallel" visible in the trace (line 962-963)
- **Node-level inputs and outputs** -- clicking on any blue node (stage-level) shows its input state and output state; clicking on orange nodes (LLM-level) shows the actual API call details (line 1091-1099)
- **Gate validation details** -- deterministic gate checks surface structured results showing exactly which checks passed and which failed, including step validation breakdowns (line 1118-1141)
- **Business logic LLM checks** -- the SQL gate's LLM review surfaces structured findings, with Saurav noting "it made 17 findings" with "good nested objects and all the outputs are pretty structured" (line 1157)
- **State management** -- the entire LangGraph state is a JSON object that builds throughout the pipeline; any field that has been populated is visible in LangSmith at every stage (line 1191)

**Colin (line 1181):** "No one will have any question that cannot be answered from this."

### Colin's Assessment of UI vs. LangSmith

Colin made a clear prediction about how different audience members will react:

**Colin (line 1206-1213):** "I think for non-technical people, yep. But I think for technical people they're going to say this is really nice but also, so if I have LangSmith that does the same for me, maybe with less effort for you. So this is nice to have and you know, makes it look nicer and makes it more digestible. But maybe they'll say it's always good to just know that we have this and we don't need to go too crazy on here, so we don't duplicate what's already on here."

### Implication for the Demo

Colin expects the following dynamics:

1. **Non-technical stakeholders** will prefer the UI. The DAG visualization, the progress bar, the review screen with expandable findings -- these are digestible without needing to understand LangGraph internals.
2. **Technical stakeholders (especially Sergey)** will appreciate the UI but will gravitate toward LangSmith because it provides complete transparency into every API call, every state transition, and every parallel execution decision. LangSmith answers questions the UI cannot surface without becoming "too info intensive" (line 1184).
3. **The UI may end up as "nice to have."** Colin acknowledged that if Sephora's technical team decides LangSmith provides sufficient visibility, the custom UI becomes a presentation layer rather than a core requirement. This could reduce future development effort.

### What to Say in the Demo

For a mixed audience, show the UI first to establish the workflow narrative, then switch to LangSmith and say something like: "For those of you who want to see exactly what happened at every step -- every API call, every parallel execution, every gate decision -- this is LangSmith. Every node's input and output is here. You can see the waterfall of how the agents executed in parallel, see exactly what the LLM was asked and what it returned. Nothing is hidden."

For Sergey specifically, the LangSmith walkthrough should include: clicking into a gate node to show step validation results, clicking into an LLM call to show the structured JSON output with findings, and showing the waterfall view to demonstrate parallel execution (independent stages firing concurrently at max concurrency of four).

---

## 4. "Not a Product, This Is a Solution" -- Competitive Differentiation

Colin has been explicit about this framing in prior calls, and it carries into the demo. The system is not a packaged product that Sephora is evaluating against other products. It is a custom solution built for their specific use case.

### Supporting Evidence for the Demo

- **Built in the last two weeks.** The entire demo -- LangGraph pipeline, UI dashboard, LangSmith integration, auto-fix, knowledge base learning -- was built in approximately two weeks of development by Saurav (line 1550-1551 context: Colin noting the front end was built in less than a week, with the broader pipeline development preceding it).
- **Production-style architecture despite PoC scope.** The pipeline uses deterministic gates between stages, parallel execution with concurrency management, structured state management via LangGraph, LangSmith observability, and a knowledge base that learns from approved patterns. These are production patterns, not demo shortcuts.
- **Custom to Sephora's files.** The demo runs against Sephora's actual source files -- their XML, stored procedures, DDL files, and Scala/YAML target examples. This is not a generic converter.

### What to Say in the Demo

"This is not a product -- this is a solution. We built this specifically for your EDW conversion pipeline. Everything you see was developed in the last two weeks. With a production engagement and more time, it gets significantly better. But even at PoC scale, we built it the way we would build it for production."

---

## 5. Configuration Placeholders as Future-Selling

The UI contains several configuration elements that are visible but non-functional. Colin identified these as strategic assets for the demo.

### What Is Placeholder

Saurav walked through the configuration panel:

**Saurav (line 1465-1491):** "Drop down for like different target platforms here, change retries. We can have like different models here also... then demo files and even like if they want to once we have the MCPs and all present... we can have like different things here and even if we want we can also have suppose a connector column in here and like different source listed so, like MCP connectors, it can directly pick up those also if they want obviously."

The non-functional placeholders include:

1. **Target platform dropdown** -- shows extensibility to different target environments
2. **Model selection dropdown** -- shows the system is not locked to a single LLM; models can be swapped
3. **Retry configuration** -- shows operational tuning is available
4. **MCP connectors section** -- shows where source system connections (like Cognos) would be configured
5. **Drag-and-drop file upload** -- the area is visible but not functional; the "Load Demo Files" button is the working path (line 173-174)

**Saurav (line 1497-1498):** "Yeah, these are just for show. Yeah, these look good, but do not do anything."

### What to Say in the Demo

Do not pretend these work. Instead, use them as forward-looking capability signals: "You can see here we have placeholders for target platform selection, model configuration, retry tuning, and MCP source connectors. These are not active in the PoC, but they show where the system goes next. If you want model selection, we can have it. If you want to configure retry behavior per pipeline, we can have it. The architecture supports all of this."

This accomplishes two things: it shows extensibility without requiring demo-day functionality, and it seeds the conversation about post-PoC scope expansion.

---

## 6. Knowledge Base Learning Pitch

The knowledge base is the system's ability to learn from approved patterns across runs. Colin should present this as one of the key differentiators because it speaks to the "system that gets better over time" narrative.

### How It Works

**Saurav (line 566-575):** "After we have approved it, whatever the wrong patterns we have flagged. Correct. Whatever were the false positive or suppose we made a new rule that null handling should be done in this way or the where clause or the when case should be added in this way or we have to treat a particular type of join or view in a particular way -- after we have approved it, it adds that as a JSON object to a knowledge base so that in the next generation when SQL is doing the generation, it knows that yeah, previously this kind of thing has already been approved. So I should follow this pattern for this."

**Saurav (line 574-575):** "So this will be kind of like a system which will be able to learn based on the runs it is going through."

### The Learning Cycle

1. The pipeline generates SQL and config artifacts.
2. The review stage identifies issues (bugs, advisories).
3. The user can mark findings as false positives, approve corrections, or define new rules (e.g., "null handling should always use COALESCE").
4. Upon approval, the approved patterns are saved as JSON objects to a knowledge base.
5. In subsequent runs, the SQL generation agent reads the knowledge base and applies those patterns during generation.
6. Over time, the system converges: runs 1-3 may require review and correction; runs 10+ apply learned patterns automatically.

### What to Say in the Demo

"When you approve a run, the system learns. It saves the approved patterns -- how null handling should work, how joins should be structured, how specific transformations should map -- into a knowledge base. The next time the system processes a similar pipeline, it already knows those patterns. After three to five runs, the system is applying your team's standards automatically. This is not just a one-time converter; it is a system that learns based on the runs it goes through."

---

## 7. Demo Flow: What to Click and When

Based on the walkthrough, Colin's demo should follow this sequence:

### Step 1: Start Screen

- Show the configuration panel briefly. Point out the placeholder dropdowns (target platform, model, retries, MCP connectors) as future capability.
- Click "Load Demo Files" to populate the nine source files. Note: drag-and-drop is placeholder only; do not attempt it.
- Mention the files: "These are Sephora's actual files -- their XML job definitions, stored procedures, DDL and view definitions, and Scala/YAML target examples."
- Click "Start Pipeline."

### Step 2: During Execution

- Watch the execution log at the bottom of the screen. It shows Claude-style status messages ("Extracting SQL currently," "Parsing XML") with a running timer per agent.
- Let the audience see the DAG nodes lighting up as each stage completes.
- Use this time to narrate the pipeline stages: orchestrator loads files and selects pipeline; Gate 1 validates all files are present; three parsers run in parallel (data stage, SQL interpreter, DDL); Gate 2 checks for hallucinations against source files; pattern mapping creates translation dictionary; SQL generation plans then generates independent stages in parallel then dependent stages; Gate 4 checks business logic; config generation fires three parallel agents (pipeline YAML, deployment YAML, HQL); validation runs deterministic checks.
- If the pipeline is slow (throttling), Colin can talk through the architecture rather than waiting in silence. Saurav noted most slowdown is from API throttling, not computation (line 858-859).

### Step 3: Review Screen

- Expand the review findings. They are descriptive enough that someone familiar with the databases can understand them immediately.
- Show the highlight.js syntax highlighting in the generated SQL preview.
- Click "AI Review" to show the audit re-review capability -- the system re-examines its own validation results to catch false positives.
- Click "Auto Fix" (not reject-and-retry -- the DAG animation breaks on retry). While auto-fix runs (1-2 minutes), scroll up and read through the AI review findings to show the audience the quality of analysis.

### Step 4: Post-Fix Review

- After auto-fix completes, the validation re-runs and the review screen refreshes with updated findings.
- Click "Approve" to complete the run.
- Show the download buttons for individual artifacts (SQL, YAML, HQL). Note: the zip download is broken; use individual file downloads only (line 684-691).

### Step 5: Run History

- Navigate to the run history page. With Saurav's database pre-population, it should show a few hardcoded entries (couple passes, one pending, one failed) plus the live run just completed.
- Click into a previous run to show it is reviewable after the fact.

### Step 6: LangSmith

- Switch to the LangSmith browser tab.
- Show the waterfall view. Point out parallel execution.
- Click into a gate node to show step validation results.
- Click into an LLM node to show structured outputs.
- Deliver the "no question that cannot be answered" line.

---

## 8. Saurav's Availability and Backup Plan

### The Situation

The demo is scheduled at a time that translates to 3:30 AM for Saurav in India. Colin explicitly told Saurav not to feel obligated to join.

**Colin (line 1414):** "I forwarded you the invite again. I know it's literally going to start at 3:30 AM your time. So don't just don't stretch yourself then. I mean you already did a ton of work for this so."

### Saurav's Response

**Saurav (line 1391-1398):** "I will check like if maybe I'm available, so maybe I will join in the call. Yeah, if I am like awake at that time, I may not be able to not in a state to give the demo, but... maybe I can just join in if they have any kind of like doubts or you want to ask any question."

**Saurav (line 1404):** "Don't quote me on the matter."

### Backup Plan

- **If Saurav joins:** He can field deep technical questions about the LangGraph architecture, gate logic, parallel execution strategy, and SQL generation approach. He should not be expected to present.
- **If Saurav does not join:** Colin will record the meeting (line 1586). Colin has been taking notes throughout this walkthrough specifically to handle questions independently. LangSmith provides answers to most technical questions visually.
- **If Colin is asked a question he cannot answer:** He can defer with "I want to make sure I give you the right answer on that -- let me confirm with our architect and follow up." This is standard and acceptable.

### Colin's Commitment to Saurav

**Colin (line 1407):** "If you are there, I expect you to not be on some of the meetings on Friday."

This sets the expectation that if Saurav sacrifices sleep for the demo, he gets recovery time. Colin is managing this correctly.

---

## 9. Handling Questions: Technical Depth Answers

Based on the walkthrough, Colin now has answers to the most likely technical questions:

### "How does the system handle hallucinations?"

Every gate includes deterministic checks that search the original source files for table names, column names, transformation names, and join references extracted by the LLM. If the LLM produces a table name or column name that does not exist in the source files, the gate flags it. Gate 2 specifically checks parser outputs against source content (line 300-307). The one area where deterministic checking cannot catch hallucination is business logic correctness within SQL -- that requires the LLM gate check added in Gate 4 (line 418-436).

### "How does the parallel execution work?"

Three parsers (data stage, SQL interpreter, DDL) run in parallel because they parse different source file types and produce independent outputs (line 294). In SQL generation, independent transformation stages (those with no shared dependencies) are generated in parallel at max concurrency of four, then dependent stages are generated sequentially using the independent stage outputs (line 399-406). Config generation fires three agents in parallel (pipeline YAML, deployment YAML, HQL) because they are independent artifacts derived from the same SQL output (line 447-449).

### "What models are you using?"

Opus for heavy tasks requiring large context and deep reasoning: pattern mapping and SQL generation. Sonnet for lighter tasks. The system is not locked to any specific model -- the configuration panel shows model selection as an available parameter (line 372-378).

### "How long does a run take?"

Run duration includes both processing time and human review time. The timer displayed on the results screen includes the time spent waiting for human approval, so it will look inflated (line 697-703). Actual machine processing time depends on API throttling. Colin requested a 4-5x quota increase for both Opus and Sonnet to reduce throttling delays (line 1284-1285).

### "Can this connect to our systems directly?"

Yes, via MCP. A Java MCP hook exists for Cognos. The architecture supports MCP connectors -- visible in the configuration panel. This would be wired in once BayOne has access to Sephora's internal systems, which comes with the engagement contract. (See Section 1 above.)

### "Is this a product or something you built for us?"

This is a custom solution, not a product. It was built specifically for Sephora's EDW conversion use case using their actual source files and target formats. (See Section 4 above.)

---

## 10. Pre-Demo Technical Setup Items

### Database Pre-Population (Saurav's Action Item)

Saurav agreed to add hardcoded run entries to the database so the run history page shows variety:

**Saurav (line 1569-1570):** "One for like a couple of pass, one in pending and one failed. Something like this, correct?"

**Colin (line 1567):** "I wouldn't do too many, like maybe like 3 or 4, something like that."

The entries should use different project names (not all "inventory_periodic") to show the system handles multiple pipeline types. Saurav also committed to adding a table-creation check so the pipeline_runs table is auto-created if missing (line 1361).

### Quota Increase Request

Colin submitted quota increase requests for both Opus and Sonnet on the Anthropic Foundry account, requesting approximately 4-5x the current 75K token quota (line 1279-1285). This may or may not be approved before the demo. If not approved, throttling may cause delays during live execution.

### Known Issues to Avoid During Demo

1. **Do not click reject-and-retry.** The DAG animation breaks on retry cycles (line 1335). Use auto-fix instead.
2. **Do not attempt drag-and-drop file upload.** It is non-functional. Use "Load Demo Files" button only (line 173-174).
3. **Do not attempt zip download.** Individual file downloads work; the zip button does not (line 684-691).
4. **The advisory text rendering may be blank.** Saurav noted a rendering issue where the advisory detail text does not display even though the data is present (line 633-638). He committed to fixing this.
5. **Progress bar beyond 100%.** If a run includes multiple retries, the step count can exceed the expected total (e.g., 22 steps out of a 15-step baseline), which may cause display oddness (line 1450-1451).
6. **LangSmith is not real-time.** Traces appear within a couple of minutes, not instantly (line 1023-1032). If demonstrating LangSmith during a live run, the trace may not be immediately available. Use a prior run's trace for the LangSmith walkthrough.

---

## 11. The "System That Learns" Narrative Arc

Taking all the talking points together, Colin's overarching narrative for the demo should follow this arc:

1. **This is custom, not a product.** We built this for your specific conversion pipeline using your files.
2. **It is production-architected.** Deterministic gates, parallel execution, structured state management, observability via LangSmith.
3. **It finds its own mistakes.** Gates check for hallucination, missing references, truncated SQL, and business logic soundness. The AI review re-audits the validation results.
4. **It fixes its own mistakes.** Auto-fix makes surgical edits to generated code, just like a developer using Claude Code.
5. **It learns from corrections.** Approved patterns are saved to a knowledge base. Future runs apply those patterns automatically.
6. **The next step is access.** MCP connectivity to Cognos is validated and ready. Once BayOne has access to your systems -- which comes with the engagement -- we wire it in.

This arc takes the audience from "what is this" to "this gets better over time" to "here is what comes next," which is the contract.
