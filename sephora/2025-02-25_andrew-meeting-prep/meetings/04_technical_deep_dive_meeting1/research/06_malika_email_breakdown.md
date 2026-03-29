# Understanding Malika's Email: Line-by-Line Breakdown

**Created:** March 9, 2026
**Purpose:** Clarify what Sephora actually wants in the demo based on Malika's email

---

## The Key Shift Statement

> "While the initial expectation was to provide a Cognos report XML and demonstrate code translation to Databricks SQL, we should note that our team is already performing report logic extraction and SQL conversion using our internal enterprise AI tooling and LLM-assisted workflows. As such, code translation alone would not be the primary area we are looking to evaluate."

**Translation:** "Don't just show us you can convert SQL. We can already do that. Show us what you can do that we can't."

---

## What They Say They Want (5 Bullet Points)

### 1. "Demonstration of the MCP server or integration layer for Cognos"

**What this means:** They want to see an actual connection to Cognos, not manual XML exports.

**From Meeting 4:** Colin mentioned building an MCP server for Cognos. They latched onto this.

**What we'd need to show this:**
- Access to a Cognos environment, OR
- A mock/simulated MCP server that demonstrates the capability

**Do we have materials for this?** NO - they gave us no Cognos access or credentials.

---

### 2. "Automated extraction of report metadata or XML from Cognos"

**What this means:** They don't want to manually export XMLs from Report Studio. They want agents to pull it automatically.

**Relates to Meeting 4:** Gariashi mentioned working with Vlad to manually export an XML. Malika is saying "don't make us do that manually."

**What we'd need to show this:**
- Cognos API access (Content Store or SDK), OR
- Demonstrate the architecture of how this would work

**Do we have materials for this?** NO - no Cognos access provided.

---

### 3. "Agent orchestration across multiple tools (e.g., Cognos, Databricks)"

**What this means:** They want to see multiple agents working together - one talks to Cognos, another talks to Databricks, they coordinate.

**This is the "wow factor" they're looking for.** Not code conversion. Coordination.

**What we'd need to show this:**
- Multi-agent demo with handoffs
- Could mock this with the ETL materials they provided (DataStage → agent → Databricks output)

**Do we have materials for this?** PARTIALLY - we have DataStage XML and Databricks target examples, but no Cognos.

---

### 4. "End-to-end workflow automation"

**What this means:** Start to finish. Input goes in, output comes out, human doesn't have to babysit.

> "where the agent coordinates the extraction, interpretation, and downstream execution steps"

**What we'd need to show this:**
- A pipeline demo: Source artifact → Agent parsing → Transformation logic → Output generation
- The ETL materials could work for this

**Do we have materials for this?** YES - for DataStage. NO - for Cognos.

---

### 5. "How the agent manages tool communication, task sequencing, and dependency handling"

**What this means:** They want to understand the orchestration architecture. How do agents talk to each other? How do they know what order to do things?

**This is about our agent framework, not about Cognos or DataStage specifically.**

**What we'd need to show this:**
- Architecture diagram or explanation
- Demo that shows agent handoffs and sequencing

**Do we have materials for this?** This is about OUR capabilities, not their materials.

---

## The ETL Addition

> "Additionally, we would also like to include an ETL migration use case (attached)"

**Translation:** "We're adding scope. Now we want to see DataStage conversion too."

### What they want for ETL:

| Request | What They Provided | Sufficient? |
|---------|-------------------|-------------|
| Parse DataStage job XML | DS_Jobs_inventory.xml (39KB), DS_Jobs_lod_F_Purchase_Order.xml (565KB), DS_Jobs_sqr_DF_Punch_Daily.xml (1.4MB) | YES |
| Parse SQL Server DDL | 3 DDL files | YES |
| Parse stored procedures | 2 stored procedure files | YES |
| Parse views | 2 view files | YES |
| Extract transformation logic | Embedded in DataStage XML and stored procs | YES |
| Map to Spark transformations | Target Scala apps show the pattern | YES |
| Generate Databricks pipelines | Target YAML + Scala examples | YES |
| Generate deployment artifacts | Deployment YAML examples | YES |

**For ETL: They provided a complete example.** We could demo this.

---

## The Output Format Confusion

**Email says:** "Generate Databricks-compatible pipelines (Spark SQL / Scala)"

**Sergey said in Meeting 4:** "No need to write code itself, just to create config file... generate YAML files, commit them to repo."

**What they actually have in their target folder:**
- YAML config files (aggregation + deployment)
- Scala applications
- Hive DDL

**Resolution:** Their framework uses BOTH. The YAML configs drive the Scala applications. So "Spark SQL / Scala" and "YAML configs" are not contradictory - they want the full stack.

---

## Is This Scope Different From Meeting 4?

**YES. Significantly.**

| Meeting 4 Scope | Malika's Email Scope |
|-----------------|---------------------|
| Cognos report conversion | Cognos MCP server + automated extraction |
| Code translation demo | Orchestration and agent coordination |
| "Show us you can do it" | "Show us how your agents work together" |
| One track (Cognos) | Two tracks (Cognos + ETL) |
| Output: converted SQL | Output: full pipeline + deployment artifacts |

**Meeting 4 was about proving capability. Malika's email is about proving architecture.**

---

## What We CAN Demo With Current Materials

### ETL Track (DataStage → Databricks):
1. Parse DataStage XML and extract the embedded SQL
2. Parse the stored procedures and understand the logic
3. Map the transformations to Spark patterns
4. Generate YAML config + Scala output matching their existing framework
5. Show agent orchestration during this process

### What's Missing for Cognos Track:
1. No Cognos report XML
2. No Cognos environment access
3. No target Databricks schema for remapping

---

## Bottom Line: What Does Malika Actually Want?

She wants to see **how our agents coordinate**, not just that they can convert code.

The demo should show:
1. **Agent 1** extracts from source system (Cognos or DataStage)
2. **Agent 2** interprets the logic
3. **Agent 3** generates target code
4. **Agent 4** creates deployment artifacts
5. **Orchestrator** coordinates all of this

The specific source system (Cognos vs DataStage) matters less than demonstrating the coordination pattern.

**However:** They specifically asked for Cognos MCP server. If we can't show that, we need to set expectations or ask for access.

