# 07 - Demo: New Requirements Surfaced

**Source:** /sephora/edw_modernization/source/edw_demo_4-2-2026_formatted.txt
**Source Date:** 2026-04-02 (Demo Meeting)
**Document Set:** 07 (The Actual Demo)
**Pass:** Focused deep dive on new capabilities and requirements not in the original scope

---

## Overview

The Track B demo scope was defined in Malika's email thread (Set 04a): parse DataStage job XML and SQL Server artifacts, extract transformation logic, map patterns to Spark-based transformations, and generate Databricks-compatible pipelines (Spark SQL plus YAML configuration). The demo built against that scope ran for approximately 13.5 minutes and produced the expected artifacts.

During the Q&A that consumed the remaining ~40 minutes of the meeting, seven distinct new requirements emerged that were not part of the original Track B scope. These requirements came from four different Sephora-side participants (Vishal Sharma, Maher Burhan, Grishi Chakrabarty, and Malika Seth), and every one of them connects to a single operational reality: BayOne does not yet have access to Sephora's production systems. Five of the seven requirements are impossible to deliver without that access. The remaining two (source-to-target mapping ingestion and ADF orchestration) are configuration preferences that can be accommodated at any time.

This document captures each requirement with the exact framing from the person who raised it, Colin's response, and the implications for the exploration SOW and engagement proposal.

---

## Requirement 1: Data Reconciliation Between EDW and Databricks

### Who Raised It

Vishal Sharma initiated the question at [00:36:33]. Grishi Chakrabarty clarified the intent at [00:36:51].

### Exact Framing

**Vishal [00:36:33]:** "And last question about is there any way you guys support data reconciliation? Like I know you there's a validation step in one of your diagram, but if want to do reconciliation then is there anything like that supported as a?"

**Grishi [00:36:51]:** "Reconciliation between, uh, two platforms, Vishal, right? Yeah, yeah."

**Grishi [00:37:00]:** "EDW whatever we have output versus what DP output DP. Yeah, in DP."

**Vishal [00:37:03]:** "Yes. Versus the what we get right, correct."

The requirement is clear: after migration, can the system validate that the output produced in Databricks matches what was originally on SQL Server? This is not about validating the converted code (which the demo's gate system already handles). This is about validating the data -- running the migrated pipeline and confirming the results match the legacy output.

### Colin's Response

**Colin [00:37:09]:** "I see, I see. I would say, yeah. And there's no reason why we can't. The only reason why that's not explicitly in here now is because we would have to have access to the systems to test it, make sure that's working properly. But there's no reason why we shouldn't. And actually that's one of the things in the form that I gave that I'll give at the end of this meeting. You'll see I called that out because that's only not here because we didn't have the access to the systems."

Colin then disclosed the implementation status:

**Colin [00:37:34]:** "If we had that, that just is an extra gate at the end. It's already built actually, so it's just waiting to get wired in if we have some access to those systems."

He followed with the implementation approach:

**Colin [00:37:39]:** "So for reconciliation, no, no problem. If it was between two systems, we just need to -- if we didn't have an idea of how to do that, and I'll just give an idea for this. What we'd probably want to do is spend a couple minutes with someone that's actually doing that manually, see what their workflow's like, and then we can capture that into a new agent and build it in here for you."

### What This Means

1. **Already built, waiting to be wired in.** Colin stated the reconciliation gate exists in code but cannot be connected without access to both SQL Server (legacy) and Databricks (target). This is consistent with the architecture shown in the demo: gates are modular steps in the LangGraph pipeline. Adding one more gate at the end is architecturally trivial if the system connections exist.

2. **Requires shadow-a-human step.** Colin's approach to building the reconciliation workflow is to observe someone doing it manually, capture their workflow, and encode it into an agent. This is not a pure automation play -- it requires domain knowledge transfer from whoever currently validates migrations at Sephora.

3. **Directly blocked by system access.** No reconciliation is possible without read access to both SQL Server and Databricks. This makes it a post-contract deliverable exclusively.

### Scope Implications

This requirement does not change the exploration SOW. Reconciliation is a natural extension of the pipeline that would be scoped and delivered as part of the production engagement. It reinforces the "need access to systems" theme because it is the purest example of a capability that is architecturally ready but operationally blocked.

For the engagement proposal, reconciliation should be listed as a deliverable that comes online once system access is provisioned. Colin's disclosure that it is already built should be leveraged -- it signals that the AI practice anticipated this need and pre-invested in the capability.

---

## Requirement 2: Detecting What Has Already Been Migrated to Databricks

### Who Raised It

Maher Burhan initiated the question at [00:43:27]. Andrew Ho confirmed it was his question too at [00:45:10].

### Exact Framing

**Maher [00:43:27]:** "The second one, which Andrew asked before, do you have a way of figuring out what's already exist on the target? So we can give you the our EDW. So here's the schema and the old EDW."

**Maher [00:43:47]:** "I want you to go to Databricks, look in this catalog and find. Can you find to see if these tables or this data set been already migrated?"

This is a discovery requirement, not a conversion requirement. Sephora has been migrating piecemeal -- some tables and datasets have already been moved to Databricks by different teams at different times. They do not have a comprehensive map of what has been migrated and what has not. They want the agent to build that map.

### Colin's Response

Colin described the approach using a video game exploration metaphor:

**Colin [00:44:03]:** "Yes, yes. And that one I have a lot of fun with that because it's almost like you're in a mini video game almost like right and like you're exploring the map and the map's all dark and you've got a flashlight."

**Maher [00:44:16]:** "Yeah, yeah, yeah. What's the success rate in figuring out what's already migrated in your experience?"

Colin laid out a three-step methodology:

**Colin [00:44:27]:** "So first of all, do essentially a state map. Even if it changes, even if there's active work going on, it still is helpful to do that. So say on this day I'm going to do exploration of this entire, you know, on-prem SQL Server."

He then referenced prior experience at scale:

**Colin [00:44:47]:** "The first time it was 72 different unique production SQL Server instances all running Oracle. All kinds of craziness to collect, but build that knowledge graph over here. Same thing on Databricks or Snowflake or whatever else you want to do."

**Colin [00:45:03]:** "And then as a third step, see where the alignment is at that moment in time."

The three steps are:
1. Build a knowledge graph of the on-prem environment (SQL Server, DataStage)
2. Build a knowledge graph of the Databricks environment
3. Find alignment between the two -- identify what has been migrated and what has not

### Andrew's Confirmation

**Andrew [00:45:10]:** "I was gonna ask exactly that question. Well in other words like I was gonna ask you like are you, if we gonna let's say great you know what they want, we like you guys, we want to have you guys help us in this project, then what will be really the step one right?"

Andrew's framing is significant. He is not asking whether this is possible. He is asking what day one looks like. He is thinking about the engagement, not the demo. This is the moment where the demo shifted from evaluation to next-steps planning.

### What This Means

1. **This is the exploration SOW itself.** What Maher and Andrew described is precisely the two-week exploration engagement Colin proposed at [00:46:22]: "A guided discovery to understand exactly what we can do and map out not just the databases, but our approach." The exploration SOW and the migration discovery requirement are the same workstream.

2. **The 72-instance reference establishes credibility.** Colin's reference to having done this across 72 SQL Server instances running Oracle is a direct experience claim. This is the AI practice's prior work, not a theoretical capability. It should appear in the proposal.

3. **Knowledge graph as deliverable.** The output of the exploration is not just a list of tables. It is a knowledge graph -- a structured representation of what exists on-prem, what exists in Databricks, and where the two align. This is a tangible deliverable that Sephora can use independently of BayOne's migration system.

4. **Directly blocked by system access.** No exploration can begin without read access to SQL Server, DataStage, and Databricks. This is another post-contract deliverable exclusively.

### Scope Implications

This requirement validates the exploration SOW. It should be the primary deliverable of that engagement: two comprehensive knowledge graphs (on-prem and Databricks) plus an alignment analysis showing what has been migrated, what has not, and what the gaps are. The exploration SOW should explicitly name this as the output.

---

## Requirement 3: Schema Mismatch Handling

### Who Raised It

Grishi Chakrabarty at [00:38:08].

### Exact Framing

**Grishi [00:38:08]:** "Well, I want to talk a little bit about the modernization piece in this flow, right? So we have these two systems and we have this modern DP and we have this EDW legacy system, right?"

**Grishi [00:38:26]:** "And in this modern system we already have some data available."

**Grishi [00:38:32]:** "So it's not a direct lift and shift. So while we're doing in your pipeline flow, we wouldn't be migrating all of it, right? And the schema will not be same. My target schema won't be same what my legacy schema is, right?"

**Grishi [00:38:52]:** "How would you tackle that piece and at which stage in this flow you would tackle that?"

Grishi is stating a fact about Sephora's environment that changes the conversion problem. The demo assumed a known target schema (Malika provided four Databricks table schemas via email). In reality, the Databricks schema does not mirror the legacy EDW schema. Tables have been restructured. Not all columns have been migrated. Some data has been reorganized. The agent cannot simply translate SQL syntax from one schema to an identically structured schema -- it must handle the mismatch.

### Colin's Response

Colin described two distinct paths depending on severity:

**Path 1 -- Reasonably resolvable mismatches:**

**Colin [00:38:57]:** "One where it can reasonably be resolved, where it's just a case where there's not an exact match. But if you looked you could say, OK, maybe not everything is here, maybe not all fields have been migrated or something like that. But will that actually break the report?"

For this path, the system uses the confidence-based human/auto decision framework already demonstrated:

**Colin [00:40:17]:** "If it's something where we are confident, we've done this type of a mapping before, then go and do it automatically. But if it's something that's the very first time, just to make sure it's actually correct, that would still be a human step."

**Path 2 -- Breaking mismatches:**

**Colin [00:39:30]:** "The other part is to say if it's not resolvable, if it would break the report, what to do now? And the answer for that second one is that's where you flagged at the human. We can't continue because there's something that's a critical mismatch. That can't be resolved."

Colin then escalated to a broader system response:

**Colin [00:39:39]:** "If you know me by now, my answer back to that is, well, great, well, looks like we're going to expand on this pipeline a little bit and add in some agents in some part of the workflow that can go and say specifically what we need to move over. If it would be breaking for the report and specifically how you do that, maybe they even can go and take on some of those data stage jobs for you."

### What This Means

1. **This changes the conversion problem.** The Track B demo assumed a source-to-target mapping where the target schema was provided and known. Grishi is saying the production reality is that schemas do not align. The pattern mapper step in the pipeline must become more sophisticated -- it cannot just map table-for-table, column-for-column.

2. **Two-tier resolution approach.** Colin's response is architecturally sound: non-breaking mismatches get handled through the existing confidence/human-approval framework; breaking mismatches get escalated. The second tier implies new agents that go beyond conversion and into actual data pipeline work (moving data that has not been migrated yet).

3. **Potential scope expansion into data migration.** Colin's statement about "agents that can go and take on some of those data stage jobs for you" is a significant scope expansion hint. The original Track B scope is converting existing ETL jobs from DataStage to Databricks. If schema mismatches require actually moving data that has not been migrated, that is a new workstream beyond conversion.

4. **Not blocked by system access per se, but blocked by knowledge.** The system can handle schema mismatches in the abstract. What it needs is the actual Databricks schemas and the mapping between legacy and modern schemas. This could come from human-provided mappings (see Requirement 4) or from the exploration phase (see Requirement 2).

### Scope Implications

Schema mismatch handling should be explicitly addressed in the engagement proposal. The exploration SOW should include a schema alignment analysis as part of the knowledge graph deliverable. The production engagement should distinguish between two tiers of work:

- **Tier 1 (conversion with resolution):** Jobs where schema mismatches are non-breaking and can be handled through the confidence framework. This is the core Track B work.
- **Tier 2 (conversion with data pipeline expansion):** Jobs where schema mismatches are breaking and require additional data movement. This is a separate workstream that should be scoped independently.

Pricing should account for the fact that not all jobs will fall into Tier 1. The ratio between Tier 1 and Tier 2 will only become clear after the exploration phase.

---

## Requirement 4: Source-to-Target Mapping Provided by Sephora

### Who Raised It

Maher Burhan at [00:43:09].

### Exact Framing

**Maher [00:43:09]:** "So there is two more things that we want to ask for. One of them is to do the remapping by either we feeding you the mapping from the source to the target so things change in Databricks side."

**Maher [00:43:27]:** "And here is the mapping between the two."

This is a practical request: if Sephora already has a manual mapping document that shows which legacy tables correspond to which Databricks tables (and which columns map to which), can they feed that directly into the system instead of having the agent figure it out?

### Colin's Response

Colin confirmed at [00:43:36] with "Mhm. Mhm." in direct response to Maher's mapping statement. He did not elaborate further because Maher immediately moved to his second question (Requirement 2, detecting what has already been migrated). The confirmation was unambiguous but brief.

### What This Means

1. **This is the simplest of all seven requirements.** Accepting a human-provided mapping file and feeding it into the pattern mapper is a configuration input, not a new capability. The orchestrator already classifies input files by identity and routes them to the appropriate step. A mapping file would simply be another classified input.

2. **It creates a hybrid workflow option.** Some jobs could use the agent's automatic schema mapping (with or without sample data). Other jobs, where Sephora already knows the correct mapping, could skip the inference step entirely and use the provided mapping. This is a valuable efficiency gain for the production engagement.

3. **Not blocked by system access.** Sephora could provide mapping files at any time. This capability can be developed and tested without production system access.

### Scope Implications

This should be listed as a feature in the engagement proposal: "Support for human-provided source-to-target mapping files as an alternative to agent-inferred mapping." It reduces risk for Sephora (they can override the agent where they have certainty) and reduces processing time (skipping the inference step). It is low effort to implement and high value to the client.

---

## Requirement 5: ADF as Alternative Orchestration

### Who Raised It

Vishal Sharma at [00:31:01] and again at [00:31:57].

### Exact Framing

**Vishal [00:31:01]:** "So this FastAPI, what exactly are handled here? Like is it like parsing? It's handling AI calls? It's handling like orchestration? Like why can't we use ADF right?"

Maher immediately offered context:

**Maher [00:31:16]:** "That's the engine, I believe. This is Python, right? The Python library."

Vishal pressed the point:

**Vishal [00:31:29]:** "OK, but we did also handle orchestration too, because that's what it will do, correct?"

**Vishal [00:31:57]:** "So for orchestration, if you want to use ADF for example, we can do that, correct?"

ADF is Azure Data Factory, Microsoft's cloud-based data integration service. Vishal is asking whether the migration pipeline's orchestration layer can be replaced with ADF instead of running through FastAPI. This suggests Sephora may have existing ADF infrastructure and operational familiarity, and they would prefer to use their own orchestration layer rather than adopting BayOne's FastAPI-based approach.

### Colin's Response

**Colin [00:31:43]:** "The orchestrator, the thing that's making the calls, parsing, running those deterministic steps, that is all this FastAPI server and FastAPI is just what we picked. For our stack, we can adapt to pretty much anything in case there's a preference."

**Colin [00:32:02]:** "Yeah, yeah. We would just have to know what you want and we can build around that, no problem."

### What This Means

1. **This is an infrastructure preference, not a new capability.** The pipeline logic (LangGraph agents, gates, parsers) is independent of the hosting layer. FastAPI is the HTTP server that exposes the pipeline as an API. Replacing it with ADF means re-hosting the same logic within ADF's orchestration framework. The agents themselves do not change.

2. **It signals Sephora's Azure-first orientation.** Vishal's question implies the team thinks about infrastructure in terms of Azure-native services. ADF, AKS, Azure Container Apps -- these are the tools they know and operate. Anything that runs outside that ecosystem creates operational overhead.

3. **Not blocked by system access.** This is a design decision that can be made at any time. It does affect the development effort -- adapting the pipeline to run within ADF is non-trivial but well-understood work.

### Scope Implications

The engagement proposal should include a section on infrastructure preferences and list ADF as a supported orchestration option. This is not a separate deliverable -- it is a configuration choice that affects how the pipeline is deployed. The exploration SOW should include a brief infrastructure alignment session to determine whether Sephora prefers FastAPI (as built), ADF, or another orchestration approach. Making this decision early prevents rework.

---

## Requirement 6: Platform Portability and No Vendor Lock-In

### Who Raised It

Vishal Sharma at [00:34:09] and [00:35:03]. Maher Burhan provided the definitive framing at [00:36:02].

### Exact Framing

**Vishal [00:34:09]:** "And you use YAML like plus that kind of capability right here, right? So like what if you see suppose in future we decide to stop using that platform like what will be our options in that case?"

Colin responded by explaining agents are customizable and can be rebuilt for different targets.

**Vishal [00:35:03]:** "Yeah, because we want to make sure that you know we can run something fully in our environment like without your system as well. So that you know, we're sure that in case we want to move ahead, we want to change it in the future. So that should, that capability should be supported. That's all."

Colin's full response covered three points:

**Colin [00:35:18]:** "Yes, yes, yes. And actually what you'll have no matter what, because I'll put it this way, you know, agents, especially anything like this where there is some kind of a prompt, you could look at this and say I could do it way better, you know, and all I will do is I'll give you the effectively the default versions of them. Anything like these are fully customizable. If you want to add on new ones, we have -- we didn't add it included in this PoC, but typically we have a configuration screen so that you can go and create your own if you'd want. Now can I be accountable for how well those perform? Of course not, but at least the possibility will be there."

Maher then reframed the entire concern definitively:

**Maher [00:36:02]:** "Yeah, I mean, yeah, this is the transition period. Basically we use it to migrate. When we migrate, we don't need it anymore. We are in our platform, yeah."

**Colin [00:36:13]:** "Yes, exactly. Exactly. If we do a good job, then this means that this is temporary for you, right?"

**Maher [00:36:17]:** "Yeah, yeah, exactly. That's the plan, basically migrate. And when we migrate, we're running in Databricks. Yeah, that's the goal."

### What This Means

1. **The system is explicitly understood as temporary.** Maher's framing is the healthiest possible outcome for this conversation. He does not view BayOne's migration system as a permanent platform. He views it as scaffolding that gets removed once the migration is complete. This means Sephora is not evaluating BayOne's tool as a long-term operational dependency -- they are evaluating it as a time-limited accelerator.

2. **Colin's "if we do a good job" framing is correct.** The implication is: if the migration system works well, Sephora completes migration faster and no longer needs BayOne's tooling. BayOne's success metric is its own obsolescence for this engagement. This is the right framing for a consulting engagement as opposed to a product sale.

3. **Agent customization as a deliverable.** Colin committed to providing "the default versions" of all agents with the ability to customize. This means the engagement deliverables include not just the migrated pipelines but the agents themselves -- their prompts, configurations, and knowledge bases. Sephora gets to keep the tools.

4. **Not blocked by system access.** This is a contractual and architectural commitment, not a technical capability to build.

### Scope Implications

The engagement proposal should explicitly state:

- All agents, prompts, knowledge bases, and configurations are delivered to Sephora as part of the engagement
- The migration system is designed to be temporary -- it is decommissioned after migration is complete
- Sephora retains full ownership of all artifacts produced during the engagement
- No ongoing licensing or subscription is required after the engagement concludes

This is a competitive differentiator. Competing vendors who offer platform-based migration tools create long-term dependencies. BayOne's approach creates a time-limited engagement with full IP transfer. Maher's framing confirms this is exactly what Sephora wants.

---

## Requirement 7: Sample Data Reading for Column Mapping

### Who Raised It

Malika Seth at [00:40:30].

### Exact Framing

**Malika [00:40:30]:** "But it, in order for it to be automatic, it would have to read the data off of the tables, right? It would have to like actually query that live data and then do the mapping because just by the names of the columns in the table it, you know, that may not be a exact match with the EDW legacy tables. So will the LLM actually go and read the data? So will that data be fed to the LLM in that case?"

Malika then specified the scale:

**Malika [00:41:04]:** "Like sample records, I meant yeah like maybe it takes like 10 records from the EDW table, 10 records from the Databricks table and then it does the mapping based on you know what are the values, what are the patterns in the values."

This is a data access requirement with privacy implications. Malika is asking whether the LLM will see actual production data (customer records, transaction records, product data) in order to perform column mapping. The question reveals a gap in the demo: the demo used provided schemas (column names and types) for mapping, but in production, column names and types alone may not be sufficient to establish correct mappings.

### Colin's Response

Colin described two paths:

**Path 1 -- Pre-cache during exploration (recommended):**

**Colin [00:41:18]:** "Path number one to say is what's our starting state, what's the initial, because to do them real time is both a little bit of risk but also a little bit of latency. So if we can do that exploration step first, even though that of course will be stale at some point. If we can do that first, at least to preload everything in good to go. At that point all I need to know is if the data types and the columns changed. Other than that I can get my 10 rows as a deterministic step during exploration. And save that and after that I don't need to live query and try to pull data all the time. I could just look for changes to the database itself so that can be easier to prevent it from needing to query a production database while it's running."

**Path 2 -- Live read-only tools as fallback:**

**Colin [00:42:17]:** "Option two on the other hand of course is give the language model access to read-only tools. That can do very specific things within your database. So this is the anti-Twitter stories that say 'GPT deleted my production database.' For us it would be it has specific access to one specific tool within LangGraph which allows it to go and retrieve me the top 10 records."

Colin then explained why sample data is necessary even beyond column names:

**Colin [00:42:30]:** "Even just column names plus column types, you still need to see some of that data to make sure you know column names, column types are great, but what if everything's null?"

He recommended a hybrid approach:

**Colin [00:42:45]:** "I would recommend both. One to observe and look for changes. The second one, if that fails, you can go on live query if and as needed, but not as the first line because we could skip that a little bit by just caching that."

### What This Means

1. **Pre-caching is the AI practice's recommended approach.** During the exploration phase, the agent pulls 10 sample rows from each table and caches them. These cached samples are used for column mapping during subsequent conversion runs. The agent then monitors for schema changes (new columns, changed types) rather than re-querying data on every run. This minimizes production database impact.

2. **Live query is the fallback, not the default.** Giving the LLM read-only database tools is technically feasible but introduces latency and production database load. Colin explicitly positioned this as the second option, not the first.

3. **Privacy and security implications.** If the LLM sees actual production data (even 10 rows), that data passes through the language model's context window. Colin addressed this implicitly by noting the system runs entirely within Azure (no external calls), but the engagement proposal should explicitly address data handling practices for sample data.

4. **Directly blocked by system access.** Neither path works without read access to both SQL Server and Databricks.

5. **Connects to the exploration SOW.** Pre-caching sample data is a natural part of the exploration phase (Requirement 2). When the agent builds its knowledge graph of on-prem and Databricks environments, it should simultaneously cache sample data for column mapping. This makes the exploration deliverable more valuable.

### Scope Implications

The exploration SOW should include sample data caching as an explicit deliverable alongside the knowledge graphs. The engagement proposal should address:

- How sample data is handled (cached locally, not transmitted outside Azure)
- The read-only constraint on database access (no write, no delete, no schema modification)
- The cache staleness monitoring mechanism
- The fallback to live query when cache is insufficient

---

## The "Need Access to Systems" Theme

Five of the seven requirements share a single blocker: BayOne does not have access to Sephora's production systems. The pattern is consistent across the entire Q&A:

| Requirement | Blocked by Access? | What Access Is Needed |
|---|---|---|
| 1. Data reconciliation | Yes | Read access to SQL Server + Databricks |
| 2. Migration detection | Yes | Read access to SQL Server + DataStage + Databricks |
| 3. Schema mismatch handling | Partially | Knowledge of actual schemas (can come from access or from human-provided mapping) |
| 4. Source-to-target mapping | No | Sephora provides the file |
| 5. ADF orchestration | No | Design decision, no access needed |
| 6. Platform portability | No | Contractual commitment, no access needed |
| 7. Sample data reading | Yes | Read access to SQL Server + Databricks |

This is not accidental. The demo was built in a disconnected environment by design (agreed in Set 04a). The Q&A surfaced every capability that the disconnected approach could not demonstrate. Every question from the Sephora side that required system access received the same answer from Colin: "We can do this. We already anticipated it. We need access."

The access dependency creates a natural engagement gate: the exploration SOW requires system access, system access requires a signed agreement, and a signed agreement requires Sephora to commit. There is no intermediate step where BayOne can demonstrate these capabilities for free. This is the same structural logic Colin described in the Set 06 debrief regarding the Cognos MCP connector: "The moment they give us actual access, we've already got a deal in our hands."

---

## Implications for the Exploration SOW

Colin proposed a two-week exploration SOW at [00:46:22]. The new requirements validate and expand that scope. The exploration SOW should deliver:

### Week 1: Guided Discovery (Human-Dependent)

1. **Infrastructure alignment session** -- Determine FastAPI vs. ADF vs. other orchestration preference (Requirement 5). Determine deployment model (AKS, Container Apps, etc.).
2. **Schema mismatch assessment** -- Work with Grishi and Malika to understand the actual gap between legacy EDW schemas and Databricks schemas. Identify which jobs fall into Tier 1 (resolvable mismatches) vs. Tier 2 (breaking mismatches) (Requirement 3).
3. **Reconciliation workflow capture** -- Shadow whoever currently does manual reconciliation between EDW and Databricks. Document their workflow. Design the reconciliation agent (Requirement 1).
4. **Existing mapping collection** -- Collect any source-to-target mapping documents Sephora already has (Requirement 4).

### Week 2: Automated Discovery (System-Dependent)

1. **On-prem knowledge graph** -- Automated exploration and classification of SQL Server schemas, DataStage jobs, stored procedures, and views (Requirement 2).
2. **Databricks knowledge graph** -- Automated exploration and classification of existing Databricks catalogs, tables, and pipelines (Requirement 2).
3. **Alignment analysis** -- Cross-reference the two knowledge graphs to identify what has been migrated, what has not, and where gaps exist (Requirement 2).
4. **Sample data caching** -- Pull 10 sample rows from each table on both sides for column mapping purposes (Requirement 7).

### Exploration Deliverables

1. Two knowledge graphs (on-prem and Databricks) with full schema, pipeline, and relationship documentation
2. Alignment analysis showing migration status of every table and pipeline
3. Schema mismatch report classifying jobs into Tier 1 (resolvable) and Tier 2 (breaking)
4. Reconciliation agent specification based on manual workflow observation
5. Cached sample data for column mapping
6. Full scope estimate for the production migration engagement, broken down by tier

---

## Implications for the Engagement Proposal

The seven requirements surface several items that should appear in the engagement proposal:

### Capabilities to Highlight

- **Data reconciliation gate** -- Already built, waiting to be wired in. Positions the AI practice as having anticipated Sephora's needs before they were articulated.
- **Migration detection via knowledge graphs** -- Prior experience with 72 SQL Server instances. Positions the AI practice as having done this at scale before.
- **Two-tier schema mismatch handling** -- Shows architectural sophistication. Not just lift-and-shift, but intelligent resolution with human escalation for breaking changes.
- **Hybrid mapping support** -- Accepts both agent-inferred and human-provided mappings. Reduces risk for the client.
- **Platform portability** -- No lock-in. Agents, prompts, and knowledge bases are delivered to Sephora. System is temporary.

### Contractual Items to Include

- All IP produced during the engagement is Sephora's property
- No ongoing licensing or subscription required after engagement concludes
- Read-only database access with explicit constraints (no write, no delete, no schema modification)
- Data handling practices for sample data (stays within Azure, not transmitted externally)
- Infrastructure preference accommodation (FastAPI, ADF, or other)

### Pricing Considerations

- The exploration SOW should be priced as a fixed two-week engagement with defined deliverables
- The production engagement should be priced with awareness that not all jobs will be Tier 1. The ratio between Tier 1 and Tier 2 affects effort and timeline significantly.
- Reconciliation agent development should be included in the production engagement scope, not treated as an add-on
- Sample data caching and monitoring should be included in the exploration SOW, not treated as a separate deliverable

---

## Summary Table: All New Requirements

| # | Requirement | Raised By | Timestamp | In Original Scope? | Blocked by Access? | BayOne Can Deliver? | Scope Impact |
|---|---|---|---|---|---|---|---|
| 1 | Data reconciliation between EDW and Databricks | Vishal, clarified by Grishi | [00:36:33] | No | Yes | Yes (already built, needs wiring) | Extra gate in pipeline; needs shadow-a-human step |
| 2 | Detecting what has already been migrated | Maher, confirmed by Andrew | [00:43:27] | No | Yes | Yes (done before at 72-instance scale) | Becomes primary exploration SOW deliverable |
| 3 | Schema mismatch handling | Grishi | [00:38:08] | No (demo assumed matching schemas) | Partially | Yes (two-tier approach) | May expand scope into data pipeline work |
| 4 | Source-to-target mapping provided by Sephora | Maher | [00:43:09] | No | No | Yes (configuration input) | Low effort, high value feature |
| 5 | ADF as alternative orchestration | Vishal | [00:31:01] | No (demo used FastAPI) | No | Yes (design decision) | Infrastructure alignment needed early |
| 6 | Platform portability / no lock-in | Vishal, framed by Maher | [00:34:09] | Not explicit | No | Yes (contractual commitment) | System is temporary; full IP transfer |
| 7 | Sample data reading for column mapping | Malika | [00:40:30] | No | Yes | Yes (two-path approach) | Adds to exploration SOW; privacy implications |
