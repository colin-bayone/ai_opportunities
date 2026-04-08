# 04 - Meeting: Demo Scope and Materials Agreement

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive)
**Pass:** Focused deep dive on demo scope, materials, and logistics

---

## 1. Session Disconnect and Recalibration

The meeting opened with a brief but telling disconnect. Colin came prepared with homework -- Cognos SDK/API research, an agent architecture walkthrough, and MCP integration slides -- operating under the assumption that this session was a prelude to building a demo. The Sephora team expected to see a demo today.

**Andrew (line 75):** "I think we were excited to see the demo today."

**Colin (line 82-86):** "I think that's probably where our disconnect is today. I think for the demo perspective, we won't be able to do that until we get some more information. Because for us, everyone's environment's different."

Andrew and Neha mediated the disconnect. Andrew reframed the session as the technical Q&A that would fuel the demo: "This today is really an opportunity for you to come back and ask our expertise here" (line 130). He identified the two experts available: Malika (enterprise architect) and Sergey (IBM tools SME with 10-15 years at Sephora).

Colin recovered with characteristic candor (line 142-143): "I'll say, once all of you know me a little bit better, you'll know that if it would be demo day and if I didn't have it, I'd start typing furiously on this meeting and somehow pull something out of a hat to show you today."

The disconnect was resolved within the first 15 minutes. The remainder of the session became one of the most technically productive meetings in the engagement, with Sephora providing the exact information needed to scope two demo tracks.

---

## 2. Andrew's Scope Expansion: Reports AND Data Migration

Before the demo scope discussion, Andrew made a critical scope clarification that expanded the agent mandate beyond what had been the primary focus to that point.

**Andrew (line 442-443):** "This agent that we are looking to create, my assumption is not only handling the Cognos migration track. We're also looking for agents to help even the table data migration from SQL Server to Databricks. Are you aligned with that?"

**Colin (line 444):** "Yes."

**Andrew (line 446):** "I just want to make sure that we cover both sides of the house, not just one side."

This was a deliberate scope expansion. Previous conversations had centered on the Cognos report conversion (the "front end" of the migration). Andrew was ensuring that the agent work also covered the data pipeline side -- moving the actual table data from the EDW SQL Server into Databricks. He framed it as two sides of the house:

- **Side 1 (Reports):** Re-pointing or re-engineering Cognos reports to work with Databricks as the data source
- **Side 2 (Data):** Migrating the underlying tables and data from SQL Server to Databricks

Colin recognized the implication immediately (line 448-451): "I would say let's spend a lot more energy early on in the front and the latter side of the house to help with that. Because then this is the first part of it which we're actually using agents to reconnect the reports, and it's going to be way more useful to you. If all the data is over here and is ready to go, then this agent pool over here has way more work it can do."

His logic: if agents help accelerate the data migration (Side 2), then the report re-pointing agents (Side 1) have more work they can actually execute against. Doing them in sequence -- data first, then reports -- creates a compounding effect.

---

## 3. The Disconnected Approach: Why and How

The most consequential logistical decision of the meeting was the agreement to run the demo in a disconnected fashion -- no access to Sephora's environment required. This came from Malika and was driven by practical security constraints.

### The Security Problem

Colin had raised the question of whether to demo on Sephora's real data (which would require environment access) or synthetic data (which would require BayOne to build a mock environment). He estimated the mock environment setup at roughly 40% of total demo effort (line 468).

Malika cut through the dilemma by referencing a prior security failure. Sephora's security team had previously blocked an MCP server that the internal team attempted to stand up.

**Malika (line 474-476):** "We will probably have to go through the whole security thing at Sephora if we want an external agent to run on our environment."

**Sergey (line 477-478):** "We tried to run our own... we get blocked by security."

### Malika's Solution

Malika proposed that the work could be done without access to the live environment. The precedent was that Sephora had already performed similar migration work on DataStage by working from exported job definitions rather than connecting to the running system.

**Malika (line 478-483):** "This activity actually, we did cause migration of different pieces, including DataStage. We didn't have to have access to the system. We did the migration, and we have the definition of the job, the DataStage, or the report definition. And when we pointed basically to Databricks, and if we have that restriction for it, all the required tables, view, whatever, it should work. Because I'm saying the agent can do the work, the migration work, without having access, without validating whether it's working or not."

This was the key insight: agents can perform the conversion work (parsing, SQL translation, config generation) on exported artifacts. The validation step -- actually running the converted output against Databricks -- would be handled by Sephora internally.

### Colin's Response

Colin was visibly relieved by this approach (line 572-573): "I mean, I'm kind of breathing a sigh of relief. We don't have to set up an independent Databricks instance for a demo."

He confirmed the approach was viable from a technical standpoint (line 486-488): "As long as we know things like the table definitions and things that are in Databricks, we wouldn't necessarily need to access that. Of course, like you said, we would have to skip the validation loop that would go on, but we could definitely do that."

### What This Decision Eliminated

1. **No security review required.** BayOne would not need any access to Sephora's network, servers, or cloud accounts for the demo.
2. **No mock environment build.** BayOne would not need to construct a standalone Cognos + SQL Server + Databricks environment.
3. **No validation step in the demo.** The agents would produce output (converted SQL, YAML configs, remapped report definitions), but testing that output against live Databricks would be Sephora's responsibility.

### What This Decision Required

Sephora would need to provide:
- Exported Cognos report XML (the report definition file)
- Databricks schema information (table definitions, catalog structure, connection details)
- Optionally, a DataStage job definition for the second demo track

---

## 4. Demo Track 1: Cognos Report Conversion

### Malika's Two-Step Proposal

Malika structured the Cognos demo into two distinct phases, each representing a different level of difficulty and a different real-world scenario.

**Malika (line 494-499):** "Assume that it has the same structure, data model, and Databricks. And the second step is to be remapping. Here's the oldest SQL and its own structure, and now we want to move it to the new structure. Don't ask another agent to do the mapping, figure that out."

**Malika (line 499-500):** "What do you think, Grishi and Andrew, if we have the first one, try this approach by lift and shift and abort?"

#### Step 1: Lift and Shift

The first step assumes the Databricks target has the same table structure as the SQL Server source. The agent's job is to take the Cognos report definition and re-point it from the SQL Server data source to the Databricks data source. No SQL rewriting is required -- the schema is assumed identical.

Colin pushed for clarity on what the agent would actually do in this case (line 510-511): "When you're saying convert the Cognos report to make it run on Databricks, if you're doing a lift and shift and just pointing it, what is the agent doing? Just pointing, like taking the endpoints or something?"

Malika clarified (line 512-513) that the conversion work itself -- producing the modified report definition -- is what the agent does, and it does this without connecting to the target environment. The value is in automating the extraction, parsing, and re-pointing of data sources within the Cognos report XML.

#### Step 2: Remapping

The second step is the harder scenario. The Databricks schema is different from the SQL Server schema -- different table names, different structures, different aggregation levels. The agent must:

1. Parse the SQL from the Cognos report
2. Understand the source tables and joins in the SQL Server schema
3. Map those to the equivalent (but structurally different) tables in Databricks
4. Rewrite the SQL to work against the new schema

Malika framed this as the true test: "Don't ask another agent to do the mapping, figure that out." The agent itself should determine how to remap, not rely on a pre-built mapping table.

### Context: Two Types of Cognos Reports

Andrew had earlier walked through the two types of Cognos reports in Sephora's environment, which is essential context for understanding why both steps matter:

**Type A: Framework Model Reports (line 200-209).** These reports point to IBM's Framework Manager model, which is essentially a metadata layer. The SQL is generated dynamically based on how the model was configured. For these reports, if the Framework Manager model is updated to point to Databricks, all reports that reference it automatically work. The agent work here is at the Framework Manager level, not the individual report level.

**Type B: Freehand SQL Reports (line 210-217).** These reports contain manually written SQL queries that bypass the Framework Manager model. Each query must be individually opened, extracted, converted to Databricks SQL, tested, and re-inserted into the report. Andrew described this as the labor-intensive track (line 219): "Every single step of the way, someone has to do that."

The lift-and-shift step targets Type A scenarios (or the simpler subset of Type B). The remapping step targets the harder Type B scenarios where the SQL must be genuinely rewritten.

### Target Area: Finance

The group agreed to start with a Finance report as the demo target.

**Malika (line 564-565):** "Malika, I think we need to work with Vlad to get that. We can pick one report from finance."

Finance was chosen because it was the first subject area tackled in the modernization project (line 457): "We have a whole project plan where we are tackling finance, dot-com, vendor seller, these kind of tracks, with the priority first being finance reports."

Vlad is the person Malika would coordinate with to select and export the specific report. His role was not elaborated in the meeting, but the implication is that he has access to the Cognos environment and can perform the XML export.

### What BayOne Would Build for the Demo

**Colin (line 538-543):** "So it sounds like if we can get one of the Cognos reports, what we will be able to do is we can take that, build the MCP for it, make sure that we can A, connect to it, B, dissect it, and be able to get into it... And then to remap it up to Databricks is part two."

The demo deliverable would be:
1. A custom MCP server capable of parsing and interacting with Cognos report XML
2. An agent that uses the MCP to extract report metadata, SQL queries, table references, and joins
3. A remapping agent that takes the extracted information plus the Databricks schema and produces converted output

---

## 5. Demo Track 2: DataStage ETL Conversion

### Sergey's Introduction of the Track

Malika suggested extending the demo to include a DataStage conversion as a second track, and Sergey provided the critical technical details.

**Malika (line 579-582):** "If you want to extend the demo, one of the DataStage out and see how... did that work on the address, because we did that with Claude. But it was almost like 85% need to do something... we can on the Databricks side, convert it to Spark."

Malika was referencing Sephora's prior experience using Claude directly (not through an agent framework) to convert DataStage jobs. The 85% figure is significant: Claude got 85% of the DataStage-to-Databricks conversion right, but the remaining 15% required manual intervention. This establishes both a baseline and a benchmark for what BayOne's agent approach would need to exceed.

**Malika (line 582):** "None of we have, we probably can have a simple DataStage job that we can share."

### Sergey's Framework Requirement

Sergey's contribution here is the most technically consequential detail of the entire meeting. He explained that the target output is not a Databricks notebook or Python script -- it is a set of YAML configuration files for an existing framework.

**Sergey (line 585-589):** "Our goal is to migrate DataStage jobs to existing framework. So on Databricks, we develop frameworks, YAML-based, where you don't need to do Python development or something. So you just need to do configuration. And we have thousands of jobs running in production today, support team aware how to support them."

**Sergey (line 589-590):** "No need to create new framework by using some Python or something. Everything is there, we just need to configure."

**Sergey (line 590-591):** "Ideally this agent should create all needed configurations."

The agent's job for Track 2 would be:
1. Take a DataStage job definition (XML)
2. Parse out the stored procedures and SQL logic
3. Convert stored procedures to Spark SQL (not Scala, not Python)
4. Generate the YAML configuration files that slot into Sephora's existing Databricks framework

**Sergey (line 602-604):** "How to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside. Let's say 20, 50 different parameters like source table name, connection details and so on. So you don't need to write code itself, just to create config file."

### Sergey's Critique of Claude's Output Quality

Sergey explained why the 85% success rate with Claude was not sufficient and why the output format matters.

**Sergey (line 596-598):** "This is also a problem with Claude. So we're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of windows inside this notebook and how to maintain it, I don't know, it will be nightmare to debug it."

Claude's direct output was Databricks notebooks -- unstructured, monolithic, difficult to maintain. The existing production support team knows how to support the YAML-based framework. Introducing a different output format (notebooks, Python scripts) would require retraining the support team and break the existing operational model.

**Sergey (line 599):** "The best scenario is to convert to existing framework."

### The Ideal Workflow

Sergey described the ideal end-to-end flow (line 607-609): "Ask him, hey man, we have 10 jobs, please convert them, generate YAML files, commit them to the git repo. After that, some developer can quickly review that it's good and that's it."

This is the target state: an agent that takes DataStage job definitions as input, produces YAML configuration files as output, commits them to the code repository, and a human developer does a quick review before the job goes live. The human role is reviewer, not builder.

---

## 6. Materials Sephora Committed to Providing

The following materials were explicitly agreed upon during the meeting:

### Confirmed

| Material | Description | Owner | Source |
|----------|-------------|-------|--------|
| Cognos report XML | One exported report definition from the Finance subject area | Malika, coordinating with Vlad | Lines 564-565 |
| Databricks schema info | Table definitions, catalog information, schema structure for the target Databricks environment | Malika / Sergey | Lines 543-548, 556-561 |

### Tentatively Offered

| Material | Description | Owner | Source |
|----------|-------------|-------|--------|
| DataStage job definition | A simple DataStage job XML that could serve as input for Track 2 | Malika / Sergey | Line 582 |
| YAML framework examples | Examples of the existing configuration files so the agent knows the target output format | Sergey (implied) | Lines 602-604 |

Malika indicated that the DataStage job was a possibility ("we probably can have a simple DataStage job that we can share") but it was not as firmly committed as the Cognos report.

### What Was NOT Needed

- No access to Sephora's Cognos environment
- No access to Sephora's SQL Server
- No access to Sephora's Databricks instance
- No credentials, VPN, or security review

---

## 7. The Playbook Concept

Colin introduced the playbook concept as a methodology for capturing the human expertise needed to instruct agents. This came in response to Sergey's question about how to teach agents to understand the YAML configuration requirements.

**Colin (line 612-614):** "There is a concept, we call it as a playbook. So if there's like a well-defined task that humans already have known and documented, that is a good set of instructions for the agent."

He then described a second, lower-friction approach for cases where documentation does not exist (line 616-623): "We get on a call, we hit the record button on the call to enable the transcript, and essentially someone walked through the exact process calling out those details. That's it. And then I have one of our team on just asking some questions along the way. It's usually something that's like 30 minutes to 45 minutes. At the end of that, that transcript itself becomes distilled as the first input to the agent."

The playbook concept serves two purposes:
1. **For the demo:** Sergey's explanation of the YAML framework, the configuration parameters, and the existing support model is itself the raw material for a playbook. The meeting transcript captures much of what an agent would need to know about the target output format.
2. **For the engagement:** This is BayOne's methodology for onboarding agents to new tasks at scale. Rather than requiring comprehensive documentation upfront, they capture knowledge through structured conversations and distill it into agent instructions.

Sergey responded positively (line 628): "Yeah, we did one of those too." He referenced a prior exercise where they used Claude to introduce a new ingestion pipeline from an Oracle database source, suggesting familiarity with the transcript-to-instructions workflow.

---

## 8. Security Constraints and Workarounds

### The Known Blocker

Sephora's security team had previously blocked the internal team's attempt to run an MCP server. This was referenced by both Malika and Sergey (lines 474-478). The details of the block were not elaborated, but the implication was clear: getting any external tooling approved to run inside Sephora's environment would be a prolonged process.

### Colin's Offer

**Colin (line 643-648):** "If the security team blocked an MCP server that you tried to create for this one, is that something that also you might have some trouble with or something that we can help with?... We do this all the time, so we're used to talking to IT and security teams to kind of tell them, no, we're not crazy. No, we're not going to hurt anything. We know how to talk to them about this to kind of unblock things."

**Colin (line 663-666):** "I think as soon as people understand, hey, we're doing this with your own tools within your own environment, literally no information goes beyond that. That takes care of about 80% of the knee-jerk reaction to say something's dangerous in the IT space."

### The Workaround for the Demo

The disconnected approach (Section 3) effectively sidesteps the security issue entirely for the demo phase. No MCP server needs to run inside Sephora's network. No data leaves Sephora's environment in real-time. The exported XML and schema definitions are static artifacts that can be shared without security escalation.

The security challenge remains for a production deployment, but it was deliberately deferred. The demo proves capability without triggering the security review process.

---

## 9. Timeline and Next Steps

### Immediate Actions

| # | Action | Owner | Source |
|---|--------|-------|--------|
| 1 | Select and export one Cognos report XML from Finance | Malika, working with Vlad | Lines 564-565 |
| 2 | Provide Databricks schema/catalog information | Malika / Sergey | Lines 543-548 |
| 3 | Optionally provide a simple DataStage job definition | Malika / Sergey | Line 582 |
| 4 | Send all materials to BayOne | Grishi (coordination) | Lines 671-672 |
| 5 | Schedule the demo session once materials are received | Zahra / Neha | Lines 671-672 |

### Demo Build (BayOne)

Once materials are received:
1. Build MCP server for Cognos report XML parsing
2. Build agent to extract metadata, SQL, table references from the report
3. Build remapping agent for SQL Server-to-Databricks conversion
4. Optionally build DataStage-to-YAML conversion agent (if DataStage job definition is provided)
5. Prepare demo walkthrough showing both tracks

### Wrap-Up

**Neha (line 670-672):** "As next steps, just waiting on those reports from you, and then we set up a time for that first level demo to showcase capabilities. And if there is anything else that you want to add on or you'd like us to showcase in terms of a POC, just let us know and then we can set up a time accordingly."

**Grishi (line 637-640):** "I guess for our next steps... is that the plan then? We'll get a report with the full report for all the XML included, and then we'll try to lift and shift it to some definition that's given to us from Databricks. So that's probably the first step. And why don't we admire internally, maybe, as a team, we want to regroup and see what else would be helpful for us."

Grishi left open the possibility that the Sephora team might identify additional demo requirements after internal discussion, but confirmed the Cognos report + Databricks schema as the baseline deliverable.

---

## 10. Summary: The Two Demo Tracks

### Track 1: Cognos Report Conversion

| Attribute | Detail |
|-----------|--------|
| **Input** | One exported Cognos report XML from the Finance subject area |
| **Additional input** | Databricks schema information (table definitions, catalog structure) |
| **Step 1 (lift and shift)** | Re-point the Cognos report data source from SQL Server to Databricks, assuming identical schema |
| **Step 2 (remapping)** | Rewrite the SQL within the report to work against a structurally different Databricks schema |
| **Output** | Modified report definition and/or converted SQL |
| **Validation** | Sephora takes the output and tests it internally (not part of demo) |
| **Agent components** | MCP server for Cognos XML parsing, report metadata extraction agent, SQL conversion/remapping agent |
| **Report source** | Malika to work with Vlad to select and export the report |

### Track 2: DataStage ETL Conversion

| Attribute | Detail |
|-----------|--------|
| **Input** | One DataStage job definition (XML) |
| **Additional input** | YAML framework specification (configuration parameters, file structure) |
| **Process** | Parse stored procedures from DataStage job, convert to Spark SQL, generate YAML config files for existing framework |
| **Output** | Three YAML configuration files per job (pipeline, deployment, HQL), ready for commit to git repo |
| **Validation** | Developer reviews generated YAML files |
| **Benchmark** | Claude achieved 85% conversion accuracy working directly; agent approach should exceed this and produce maintainable output (YAML configs, not notebook spaghetti) |
| **Agent components** | DataStage XML parser, stored procedure-to-Spark SQL converter, YAML config generator |
| **Material source** | Malika/Sergey may provide a simple DataStage job |

### Key Design Decisions Across Both Tracks

1. **Disconnected execution.** No access to Sephora's live environment. Agents work on exported artifacts.
2. **No validation in demo.** Sephora handles testing internally after receiving the output.
3. **Existing framework as target.** Track 2 output must conform to the existing YAML-based framework, not introduce new tooling.
4. **Finance as starting domain.** Both tracks draw from the Finance subject area, which is the first priority in Sephora's migration plan.
5. **Human role is reviewer, not builder.** The target state for both tracks is agents producing output that a human reviews and approves, not agents assisting humans who are doing the primary work.
