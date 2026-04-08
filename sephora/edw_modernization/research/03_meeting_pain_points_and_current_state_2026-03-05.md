# 03 - Meeting: Pain Points and Current State

**Source:** /sephora/edw_modernization/source/andrew-girishi-meeting1_formatted.txt
**Source Date:** 2026-03-05 (Andrew/Grishi Meeting)
**Document Set:** 03 (Andrew/Grishi Meeting)
**Pass:** Focused deep dive on pain points and current state of EDW modernization

---

## 1. Scale of the Effort — The Numbers

Colin opened the meeting by recapping what Mani had shared in the prior meeting. The scale numbers were stated without correction from Grishi or Andrew, confirming them as accepted baselines.

**Key statement (line 66):** "Cognos reports, Mani had said there's about 6,000-plus reports, eight SSAS cubes, 800-plus KPIs, 300 dimensions, 20 source systems, a whole lot on your plate, for sure."

Summary of confirmed scale:
- **6,000+ Cognos reports** — the full universe of reporting assets that must be re-engineered
- **8 SSAS cubes** — aggregated analytical datasets served through SQL Server Analysis Services
- **800+ KPIs** — business metrics that must be preserved, validated, and harmonized
- **300 dimensions** — dimensional attributes across the reporting landscape
- **20 source systems** — upstream data sources feeding the enterprise data warehouse

Neither Grishi nor Andrew disputed or refined any of these numbers. They are working assumptions for the engagement.

---

## 2. Current State of Progress — Finance Track

Colin stated his understanding that "the finance track is at least nearing completion" and that it served as "the proving ground to establish patterns and establish the tool" (lines 68-69).

**Grishi corrected this immediately (line 70):** "Not completion, just a quick correction." She clarified: "It'll go throughout, you know, end of this year, but we are making progress" (line 72).

This is an important calibration. The finance track is not near completion — it will continue through the end of 2026. But progress is being made, and it remains the category where patterns are being proven and refined. The finance track was previously identified by Mani as the first category in the roadmap (see Document Set 02).

Andrew later reinforced that migration work is actively underway and will not stop to wait for AI tooling: "From a program perspective, Grishi's team had started the journey already. We're not, you know, right now, just kind of standing still and waiting for all the agents being created. They have started all the migration. There's a lot of, even though, you know, manual work is happening, that's fine. We'll continue executing this program" (lines 430-433).

---

## 3. Pain Point #1: SSAS Cubes to Databricks with Excel Interface Retention

Grishi identified this as the single biggest pain point. She described it in specific, concrete terms.

**Key statement (lines 135-141):** "Our biggest pain point now would be moving SSAS cubes to Databricks with minimal change management. So we have these aggregated tables in form of cubes, but we have an Excel pivot table that's feeding data from those SSAS cubes, and business just drags and drops those KPIs, so they love the Excel view, right? Now SSAS doesn't have a connector to Databricks where we can retain that, so we want to run some POCs so that the change is minimal."

### The Problem Decomposed

1. **SSAS cubes serve as the aggregation layer.** Business users do not interact with raw SQL Server data. They interact with pre-aggregated analytical cubes built in SQL Server Analysis Services (SSAS).

2. **Excel is the primary end-user interface.** Users connect Excel pivot tables to SSAS cubes and use drag-and-drop to manipulate KPIs and dimensions. This is deeply ingrained in their workflow. They "love the Excel view" (line 136).

3. **No native connector exists.** SSAS has no direct connector to Databricks. There is no out-of-the-box way to point an Excel pivot table at Databricks data and retain the same drag-and-drop behavior that SSAS provided (line 137).

4. **Change management is the core concern.** The goal is "minimal change management" (line 135). Forcing users from Excel to a different tool (like ThoughtSpot) would require them to learn an entirely new interface.

### The Current Workaround and Why It Falls Short

Grishi described what they are currently doing as a fallback approach (lines 138-141): "How we are currently approaching the problem is we move all the data, all the aggregated layer onto Databricks, and we make it accessible through ThoughtSpot. We give the KPIs and they just access it. But then they have to change from Excel to ThoughtSpot, which is two different UIs, two totally different look and feel."

The workaround delivers the data but fails on user experience. Moving users from Excel pivot tables to ThoughtSpot means:
- Different user interface entirely
- Different interaction model (no drag-and-drop pivot table)
- Different look and feel
- Significant change management burden — precisely what the team is trying to avoid

Grishi explicitly framed this as their "biggest point" (line 141).

### Colin's Response: Custom Excel Plugin

Colin acknowledged the problem and proposed a potential path (lines 361-373). He described having done a similar integration for Hyperion at a previous engagement — building a custom Excel connector to bridge from a legacy analytical tool to a modern data platform. He assessed the SSAS case as "a little bit easier than it was for what we had to see with Hyperion" (line 381) and said it was "certainly doable as a POC" (line 381).

The proposed solution would be a custom Excel plugin that connects to the Databricks semantic layer while preserving the native Excel drag-and-drop pivot table experience (lines 370-371).

---

## 4. Pain Point #2: AI-Assisted Report Migration Is Still Human-Limited

This pain point was described by both Grishi and Andrew, with each adding complementary detail. The core issue: they are already using AI (Claude) for SQL conversion, but the efficiency gain is only ~30%, and the overall process remains bottlenecked by manual human steps.

### Grishi's Framing: Want Agents, Currently Doing Everything Manually

**Key statement (lines 142-148):** "We are using Claude and we are experimenting with all these tools and we are using, but at this point we are not finding something like — we want to ideally have an agent that would integrate with let's say Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks, right?"

Grishi described the aspiration clearly: an agent that can integrate directly with Cognos, read the reports, extract and re-engineer the embedded SQL and metadata, and automatically point the output at the Databricks semantic layer. This does not exist today.

**The manual reality (line 147):** "Now we are picking all the — we are going to each job and getting it, getting an XML, feeding it and checking, getting the re-engineered code and then feeding onto Databricks, right?"

The current process for each report or DataStage job:
1. Go to the individual report or job
2. Extract the XML or SQL manually
3. Feed it into an AI tool (Claude)
4. Review the re-engineered output
5. Manually integrate the output back into the target system

This is a one-at-a-time, human-driven process with no automation of the extraction or integration steps.

### Andrew's Framing: 30% Efficiency Gain, Still Overwhelmingly Manual

Andrew provided the quantitative assessment and the strategic framing.

**Key statement (lines 156-161):** "AI can help us to convert some of the SQL data embedded in all the Cognos reports that are SQL Server-specific SQL to automatically transform into Databricks-aware kind of SQL, right? So that's great. That's cut us quite a bit of a time. But the efficiency gain that Grishi and the team had figured out was about 30%."

**The 30% figure** represents the total efficiency improvement they have achieved by using Claude for SQL conversion. This means:
- 70% of the effort is still manual
- The AI is handling only the SQL transformation step
- Everything before and after that step (extraction, context gathering, validation, re-integration) is still done by people

**The manual workflow spelled out (lines 160-161):** "You still have to manually go to Cognos, and then open the report, then take the SQL out, and then run through the AI, spit out the new SQL, then you have to manually snap it back to the Cognos."

Andrew's step-by-step description of the current process:
1. Manually navigate to Cognos
2. Open the specific report
3. Extract the SQL from the report
4. Run the SQL through an AI tool (Claude)
5. Receive the converted Databricks-compatible SQL
6. Manually insert the new SQL back into the report in Cognos

Steps 1-3 and 5-6 are entirely manual. Only step 4 is AI-assisted. The AI is doing the narrow task of SQL dialect conversion (SQL Server to Databricks SQL), but the human is responsible for all the surrounding workflow — extraction, context, re-integration, and validation.

Colin characterized the situation succinctly (line 236): "It's essentially human limited because it's so manual."

---

## 5. Pain Point #3: DataStage ETL Re-Engineering

Grishi raised DataStage as a parallel challenge to the Cognos report migration.

**Key statement (lines 145-148):** "We have DataStage tool, which is the ETL tool that grabs data from different sources and dumps it into our SQL data warehouse. So we would want an agent to go integrate with DataStage, read all that and re-engineer code automatically on Databricks."

### What DataStage Does in the Current Architecture

DataStage (IBM's ETL tool) is the mechanism that:
- Connects to 20 source systems
- Extracts data from those sources
- Transforms it according to business rules
- Loads it into the SQL Server-based enterprise data warehouse

### What They Want

An AI agent that can:
1. Integrate directly with DataStage
2. Read the existing DataStage job definitions
3. Understand the ETL logic encoded in those jobs
4. Re-engineer that logic automatically for Databricks

### What They Have Today

The same manual process as with Cognos reports (line 147): going to each DataStage job individually, extracting the XML job definition, feeding it through AI, checking the output, and manually deploying the re-engineered code onto Databricks. No direct integration. No automation of the extraction or deployment steps.

---

## 6. Pain Point #4: Old Software Versions and Integration Viability

Andrew raised a foundational concern about whether agent integration is even technically possible given the age of their software.

**Key statement (lines 514-522):** "Because of our version of the software — for example, Cognos that we have is a very, very old version. We actually, I think it's like a 10.3 or 10.2, something like that. And it's super old version. DataStage, it's not the latest version either. And so what I don't know is whether — because even in order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL Server for some of that kind of database that you can just easily have the AI to go with, or it has an API endpoint or some sort. Otherwise, your agent — it can be as smart as you can be. It won't be able to connect to that software. Then it's moot point, right?"

### The Concern Decomposed

1. **Cognos version 10.2 or 10.3** — this is described as "super old." IBM Cognos 10.x dates from approximately 2012-2014. It predates the modern API-first era of enterprise software.

2. **DataStage is also not the latest version** — the exact version was not specified, but Andrew characterized it as similarly dated.

3. **The integration question** — Andrew is asking whether these old versions expose any programmatic interface (SQL Server metadata database, API endpoint, or similar) that an agent could use to read report definitions, job configurations, and metadata. If they do not, then no amount of AI sophistication can help — the agent simply cannot access the software.

4. **Andrew framed this as a blocking prerequisite (line 522-524):** "It can be as smart as you can be. It won't be able to connect to that software. Then it's moot point, right? So I think that's one thing that I do want to see. Is it even possible, right?"

### Colin's Response

Colin acknowledged the concern and reframed it somewhat positively (lines 534-536): "The good news with older software, to be honest with you, is the same reason why it gets old is because — I shouldn't say it like this, but I will. It's easier to get into older software." He noted that older, on-premises versions tend to have less security hardening than modern cloud-based deployments, making programmatic access more feasible.

Andrew confirmed (lines 541-543): "I think it's on-prem. So you're right. From that perspective, it's much easier."

Colin also noted that IBM Cognos and DataStage, while dated, are not obscure or proprietary — they are well-known enterprise tools with established ecosystems, making it more likely that connectors or integration approaches already exist (lines 547-551).

His one stated concern was performance impact: querying production systems heavily with an agent could degrade performance for production workloads (lines 554-557).

---

## 7. The Timeline Problem: 3 Years Manual vs. 1-1.5 Years with Agents

Andrew provided the clearest strategic framing of why AI agents are needed — it is fundamentally a timeline compression problem.

**Key statement (lines 153-154):** "Without AI... when we estimate this project or this program, we know it's such a big program that we cannot just boil the whole ocean in one shot."

**Key statement (lines 165-171):** "Rather than spending money on manual — you know, at the end of the day, we still need to spend the money, you know, on a contractor to do the manual work. Rather than spending that money there, I take the money and resources and spend it upfront to create all these agents so that it will then, once it's all done, then it can parallel run and do all the thing by itself. Of course, at the end, you still need QE to validate your data. I get that, right? But if we can do that, then all of a sudden, you can parallel track a lot of this migration."

**The timeline (line 171):** "And so then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half, or something like that, right?"

### Andrew's Economic Argument

Andrew is making a build-vs-hire argument:
- **Status quo path:** Spend money on contractors to do manual work across a 3-year timeline
- **Agent path:** Redirect that same budget to upfront agent development, then run agents in parallel to compress the timeline to 1-1.5 years
- **Residual human role:** QA/QE validation at the end of the process is still required regardless of approach

The key insight is parallelization. Manual work is sequential and human-limited — one person works on one report at a time. Agents can run in parallel across many reports simultaneously. The investment shifts from ongoing labor cost to upfront development cost.

---

## 8. The Semantic Layer Strategy

The semantic layer was discussed at the beginning of the meeting after Colin raised it from the prior conversation with Mani.

**Key statement from Grishi (lines 87-93):** "That is the ideal state, right, that we are looking for, so that the semantic layer stays common between all these different reporting tools — Cognos, cubes that will be migrated to, you know, ThoughtSpot or whichever tool is efficient, right? So that we can use these common semantic layer, feed all these tools. We want to stay tool agnostic so that whichever tool we use, we just point it to the same data set. And the KPIs that they are showing — we don't have questions on, oh, this is something different, that's something different. It's the same KPI. It's coming from different tables, and it's updating at different times."

### Principles of the Semantic Layer

1. **Tool-agnostic by design.** The semantic layer must serve multiple reporting tools — Cognos (current), ThoughtSpot (planned), SSAS cubes (transitional), and potentially others. No single BI tool should be the exclusive consumer.

2. **Domain-based organization.** Grishi confirmed (line 84) that the semantic layer is organized "by domains" — meaning business domains like finance, merchandising, supply chain, etc.

3. **KPI consistency is the goal.** The core problem the semantic layer solves: the same KPI reported through different tools today can show different numbers because it pulls from different tables and updates at different times. The semantic layer eliminates this by providing a single source of truth for each KPI.

4. **Sits on Databricks.** Grishi explicitly referenced "our semantic layer that's sitting on Databricks" (line 143), confirming the semantic layer is being built on the target platform.

5. **Mani had previously de-prioritized this relative to the core migration.** Colin referenced Mani saying the semantic layer was "not not a priority, but it's not something that he would be willing to block other things on if it didn't resolve in time" (lines 78-79). This positions it as desired but not on the critical path — the migration will proceed regardless.

---

## 9. What Is Working Today vs. What Is Not

### Working

- **Finance track migration is underway.** The team is actively working through the finance category. Progress is being made, though completion extends through end of 2026.
- **Architectural patterns are established.** Confirmed in this meeting implicitly and explicitly in prior meetings with Mani (Document Set 02). The target platform (Databricks), roadmap, and category sequencing are decided.
- **Claude is being used for SQL conversion.** The team is actively using Claude to convert SQL Server-specific SQL to Databricks-compatible SQL. This delivers a 30% efficiency improvement.
- **Schema mapping with Claude.** Grishi mentioned (lines 268-274) that they have used Claude for schema mapping between the EDW and the data platform, noting that "three tables in EDW could be one table in DP" — it is not one-to-one mapping.
- **Manual migration work continues.** The team is not waiting for AI solutions. They are executing the migration program through manual effort while exploring AI acceleration.

### Not Working / Insufficient

- **No agent integration with Cognos.** There is no automated way to extract report definitions, SQL, or metadata from Cognos. Every report must be opened and inspected manually.
- **No agent integration with DataStage.** Same problem — no automated extraction of ETL job definitions from DataStage. Each job must be manually exported and processed.
- **30% efficiency is not enough.** Andrew was explicit that 30% is appreciated but insufficient given the scale. At 6,000+ reports with a 70% manual burden, the timeline remains unsustainable.
- **No SSAS-to-Databricks connector for Excel.** The highest-priority pain point has no solution today. The workaround (ThoughtSpot) fails on change management grounds.
- **Schema mapping with Claude is not fully accurate.** Grishi noted (line 274) that the AI-assisted schema mapping "is not 100% accurate" and still requires manual intervention.
- **No commercial off-the-shelf solution exists.** Andrew stated clearly (lines 174-176): "I know for a fact, right now outside there's no — no one has a package that we can just say, hey, I want to buy your package... so I can just run through this migration without any human involved or even a little human involved."

---

## 10. The Agent Swarm Vision

Both Grishi and Andrew articulated a clear vision for what they want to build: a multi-agent orchestration system.

**Andrew's description (lines 164-167):** "Can we, you know, is there a way we can create multiple agents, small little agents that can do all this little step by step for us? And they have a big orchestration kind of agent that orchestrates this entire flow, right?"

**Andrew's confirmation of market search (lines 173-178):** "I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendors right now. Because I know for a fact, right now outside there's no — no one has a package... So now I'm just kind of poking a hole and saying, who out there can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing?"

### What They Want Specifically

1. **Small, task-specific agents** — not one monolithic AI, but individual agents for individual steps in the workflow
2. **A master orchestration agent** — coordinates the flow across the smaller agents
3. **Parallel execution capability** — the ability to run agents across many reports/jobs simultaneously
4. **Built on their infrastructure** — using their enterprise accounts for Claude, Vertex AI, or Azure (lines 409-413)
5. **Integration with existing tools** — agents that can actually connect to Cognos and DataStage, not just process extracted files

### Andrew's Confidence Prerequisites

Andrew was clear about what he needs to see before committing (lines 512-529):
1. **Proof that integration with old Cognos (10.2/10.3) is technically feasible** — not just that agents are smart, but that they can actually connect to the software
2. **Proof that the agent approach will shorten the timeline** — that the investment is justified
3. **A demonstration** — Grishi specifically asked (lines 489-490): "It would really help me if we could see some kind of a demo or, like, agents that you guys have created... that has done this kind of job"

---

## 11. Infrastructure and Deployment Preferences

The discussion about where agents would be built and run revealed clear preferences.

**Grishi's question (lines 384-385):** "Would you guys develop like the agents in our ecosystem, like using Databricks cloud, or is it something like a new tool you guys bring in?"

**Andrew's preference (lines 409-413):** "I'm assuming you can use our account infrastructure. Because as you run through those agents, like you mentioned, it's going to use tokens. And we have enterprise accounts or whatnot, right, with Claude and with all those stuff, even Google Vertex AI."

**Andrew's explicit requirement (line 413):** "It has to be using our own kind of platform and our stuff to execute."

Key infrastructure details revealed:
- Sephora has **enterprise accounts with Claude** (Anthropic)
- Sephora has access to **Google Vertex AI**
- The software stack (Cognos, DataStage) is **on-premises** (confirmed line 541)
- **Databricks** is the preferred platform for agent development and execution (line 593: "My ideal would be Databricks")
- There is an enterprise architect on Grishi's team who has been laying out the data migration architecture (line 571)

---

## 12. Competitive Context

Andrew explicitly stated they are evaluating multiple vendors for this work.

**Key statement (lines 173-174):** "I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendors right now."

**Key statement (line 175-176):** "I know for a fact, right now outside there's no — no one has a package that we can just say, hey, I want to buy your package... so I can just run through this migration."

Colin noted that the closest commercial solution would be Palantir, but characterized it as "probably prohibitively expensive" with "six zeros attached to the price tag" and still requiring manual effort (lines 188-198).

Andrew's approach: he is asking multiple vendors the same question — who can build a custom multi-agent orchestration system for this migration? No one has an off-the-shelf answer. The vendor who demonstrates capability and feasibility first has the advantage.
