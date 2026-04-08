# Post-Demo Next Steps Strategy

**Date:** 2026-04-02
**Context:** Captured from Colin's strategic direction before the demo. This document defines how to handle the two medium-risk gaps (timeline compression, table data migration) and frames the path from PoC to engagement.

---

## The Core Ask: Get Our Foot in the Door

The goal is not to close a massive engagement today. The goal is to get a small, defined SOW started that gives BayOne access to Sephora's systems. Once inside, we can scope the full engagement with real data instead of assumptions. Even a small start with limited scope before expanding is the best outcome.

---

## Gap Response: Timeline Compression (Andrew's Question)

**When Andrew asks "how fast can this go?":**

Now that we have the approach proven for one pipeline, we can absolutely run with similar ones. The confidence here is high. What we want to do is give them the best possible estimate, and here is how to frame that.

### The optimistic reality

This is real. We built this in two weeks. It works on their actual data at 97%+ first pass. We can run as many agents or flows concurrently as we want. Once we have a good picture of the full complexity landscape, we can do some genuinely exciting things, because we will be able to properly identify acceleration opportunities: where patterns repeat, where the flywheel kicks in, where parallel execution compresses timelines.

If everything across their environment is similar to what we just demonstrated, we could be off to the races and have this done very quickly.

### What we need to unlock that

Two things:

1. **Access to the systems for exploration.** A mapping exercise to understand the full complexity distribution across all of Sephora's reports and data flows. This cannot be done from the outside. We need read access to Cognos, DataStage, SQL Server EDW, and Databricks.

2. **Time with their technical SMEs** (one week) to help us understand the locations and structures, followed by one week of autonomous mapping.

### Why this is the responsible approach

Here is the most responsible estimate we can give right now: provided that all information shared with us is correct, we can make this much more accurate once we see the full picture. We can properly assess the flywheel effect and the timeline pull-in.

Without the exploration, any estimate is a flat calculation: total number of reports and data flows multiplied by the time it took to do this one. That works, but it is riddled with assumptions and does not account for the acceleration that agents provide through pattern reuse and parallel execution.

The flywheel where agents get faster and we can do more in parallel only comes into effect when:
- We have multiple completed pipelines as knowns (approved patterns in the knowledge base)
- We have a good picture of the overall distribution, both in terms of types and complexities

It would not be a good idea for us to claim a specific time savings number right now, because we do not yet know the full complexity distribution. What we can say with confidence is that the approach works and the acceleration is real. Quantifying it properly requires seeing the full landscape.

**How to frame it:** "Here is the most responsible estimate we can give you today. We are confident in the approach and the technology. To give you a number we can stand behind, we need to see the full picture. Two weeks of focused exploration, and we will give you a data-driven proposal with real acceleration numbers, not flat assumptions."

---

## Gap Response: Table Data Migration (Andrew's Scope Expansion)

**When Andrew asks about SQL Server to Databricks data migration:**

This is covered by the same access request. We cannot demonstrate or scope table data migration without read access to the source SQL Server systems and the target Databricks environment. The pipeline we showed today converts ETL logic (the transformation layer). The data migration layer (moving actual table data) is complementary and uses the same agent architecture, but it requires us to see what the source tables look like and how they map to Databricks.

**How to frame it:** "Table data migration is absolutely within scope. It is the other half of what we showed you today. But we need to see your source tables and your Databricks environment to build that pipeline. That is part of the exploration phase we are proposing."

---

## Defining the Full Engagement Scope

As the research library documents, the scope has evolved through the engagement:

| Phase | What Sephora Asked For | Status |
|-------|----------------------|--------|
| Set 03 (Andrew/Grishi meeting) | Agentic orchestration for report migration | Demonstrated in PoC |
| Set 04 (Technical deep dive) | Cognos MCP integration + ETL/DataStage conversion | ETL demonstrated, Cognos MCP deferred |
| Set 04 (Andrew's expansion) | Table data migration (SQL Server to Databricks) | Not yet scoped, requires access |
| Set 04a (Malika's email) | End-to-end workflow with orchestration across tools | Demonstrated in PoC |
| Set 04a (Track selection) | Track B (ETL/DataStage) as the demo, Track A (Cognos MCP) as future | Track B demonstrated |

**The full engagement has two halves:**
1. **ETL pipeline conversion** (what we demonstrated): DataStage jobs to Spark SQL + YAML configs
2. **Cognos MCP integration** (the other half of interest): MCP connectivity for automated report extraction, SQL conversion, re-pointing to Databricks

We can show them one half today. The other half requires environment access. This is the natural bridge to a paid engagement.

---

## Proposed SOW Structure: Exploration Phase

A small, focused SOW to get inside and scope the full engagement.

### Objective
Focused exploration of Sephora's EDW environment to produce a data-driven engagement proposal with accurate timeline and pricing for the full modernization acceleration.

### What BayOne Needs from Sephora
1. **Sephora accounts for Colin Moore and one additional team member** (read-only access within the confines of what is absolutely necessary for the integration)
2. **Cognos access** (if they want MCP integration explored, which is the Track A ask from their own email)
3. **Read access to relevant data platforms** as directed by Sephora's technical team, sufficient for table migration scoping
4. **Technical SME availability** for Week 1 (Sergey, Malika, or their designees to walk through locations and structures)

### Timeline: Two Weeks

**Week 1: Discovery meetings with Sephora's technical team (~8 hours)**
- Contingent on their team's availability. We need Sephora to identify the right people and confirm availability.
- Approximately 8 hours of meetings spread across the week with the relevant SMEs (Sergey, Malika, Grishi, or their designees)
- Objective: understand the full landscape of reports, DataStage jobs, data flows, and where everything lives
- Validate Cognos MCP connectivity against their specific version and environment (the Track A proof point they originally asked for)
- Not full-time work on our side. Paced by their availability.

**Week 2: Autonomous mapping and analysis (~20 hours + 2 hours buffer)**
- BayOne builds the knowledge graph and dependency map of all reports autonomously
- Classify every pipeline by type and complexity
- This is the heads-down work that produces the deliverable
- 2 hours of buffer for follow-up questions or edge cases discovered during mapping

### What BayOne Delivers
1. **Complexity mapping and state analysis:** Full inventory of report types, DataStage job types, and data flows with complexity classification and distribution analysis
2. **Cognos MCP validation:** Confirm the MCP connector works against their specific Cognos version and environment. This closes the loop on Track A.
3. **Table migration assessment:** Identify what is needed for SQL Server to Databricks data migration and what agents can automate
4. **Data-driven engagement proposal:** Scope, timeline with acceleration estimates, and pricing for the full modernization, grounded in actual system complexity

### Cost Structure

The exploration SOW is scoped at approximately **30 hours of work**:
- **Week 1:** ~8 hours of discovery meetings (Colin + one team member with Sephora SMEs)
- **Week 2:** ~20 hours of autonomous mapping and analysis (primarily the second team member, with Colin at ~10% for oversight and Cognos MCP validation)
- **Buffer:** ~2 hours for follow-ups and edge cases

The total is driven by two things: (1) how quickly Sephora can make their SMEs available in Week 1, which determines the pace, and (2) the actual volume and accessibility of the systems in Week 2. 30 hours is a responsible estimate assuming normal access and availability.

This is a modest investment relative to the full engagement. The deliverable is the state analysis and complexity mapping that makes the full engagement proposal accurate rather than assumption-based.

### The Pricing Tension

The deliverable is exploration and a state analysis. That is not a tangible product the way the PoC demo is. This is the hardest part to price because the value is in what it enables (an accurate proposal and accelerated engagement), not in a standalone output.

Options for framing:
- **Standalone exploration SOW:** Small, defined, approximately 30 hours at cost-plus rates. Delivers the complexity mapping and engagement proposal. This is clean but may feel like paying for a proposal.
- **Exploration as Phase 0 of a larger SOW:** Embed the exploration as the first two weeks of a broader engagement. The cost is absorbed into the full engagement price. This feels more natural but requires Sephora to commit to the larger scope upfront.
- **Hybrid:** Exploration SOW at a reduced rate, with the cost credited toward the full engagement if they proceed. This removes the "paying for a proposal" objection while protecting BayOne's time.

The right choice depends on how the demo lands and what Mani's appetite is for the budget conversation.

### Why This Is Worth a Small SOW Beyond the PoC
- The PoC proved the approach works on one pipeline
- The exploration phase proves it works across their environment and produces the roadmap
- Colin serves as the handoff and trainer on BayOne's side, so knowledge transfers internally regardless of team composition
- Mani was supportive of BayOne leveraging existing resources at Sephora for access (from the in-person meeting)
- Defining the full scope, or breaking it into separate SOWs by track, is necessary to move forward responsibly

### Ideal Minimum Outcome
Even if the exploration SOW takes time to formalize, getting Colin access to Sephora's environments is the single most important next step. With that access:
- Colin can begin the complexity mapping immediately
- Colin can validate MCP connectivity against their Cognos
- Colin can knowledge-share with the team for the broader engagement
- BayOne has a foot in the door with real system access

---

## How to Bring This Up in the Demo

Do NOT pitch this during the demo. Let the demo land first. After the demo, when they ask "what is the next step?" (and they will), say:

"We are really confident in what this can do. You just saw it process your actual data end to end. The question now is how do we get the best picture of what the full engagement looks like.

Here is what I would recommend. We do a focused two-week exploration. Week one, we sit with your technical team and they walk us through the full landscape of reports, DataStage jobs, and data flows. Week two, we take that and build the full complexity map autonomously. At the end of those two weeks, we give you a data-driven proposal with real acceleration numbers, not flat assumptions.

For that, we would need read-only access to your systems. Myself and one other team member. Mani mentioned when we met in person that there are existing BayOne resources at Sephora who could help facilitate that, and he was supportive of it.

The other thing this exploration gives us is the Cognos MCP validation that Malika asked about. We could not demonstrate that without your environment, but with access, we can prove it works against your specific Cognos version. That closes the loop on Track A.

If we can get that access started, even just for me to begin with, I can do the initial mapping and knowledge-share with our team from there."

Keep it conversational. Do not hand them a proposal document during the demo. Do not frame it as "paying for a proposal." Frame it as "the responsible next step to give you the most accurate engagement plan." Let them process the demo first. The formal SOW conversation comes after.

---

## Notes on Scope from the Research Library

- Mani (Set 01): 3-year program, trying to compress to 2027 or early 2028
- Mani (Set 02): Wants three engagement options with flexibility
- Andrew (Set 03): Redirecting manual contractor spend into upfront agent development
- Grishi (Set 03): 6,000+ reports, 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20 source systems
- Sergey (Set 04): Thousands of jobs already in the AggregationApplication framework
- Saurav intel (Set 05): All other vendors dismissed. Budget lock-in end of April.
- Mani in person (Set 06): Vendor selection must happen by end of month. Suggested leveraging existing BayOne resources at Sephora for access.
