# 04 - Meeting: Cognos MCP Server and SDK Research

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive)
**Pass:** Focused deep dive on Cognos/DataStage SDK findings and MCP approach

---

## 1. Context: The Homework Assignment from Set 03

In the prior meeting (Set 03), Andrew raised the central technical feasibility question: can AI agents even connect to Sephora's old software? He identified the specific concern with precision — Cognos 10.2 or 10.3 is "super old," DataStage is not the latest version, and unless the software has "an open SQL server" or "an API endpoint or some sort," the agent "can be as smart as you can be. It won't be able to connect to that software. Then it's moot point" (Set 03 transcript, lines 518-522).

Colin acknowledged the concern in that meeting and argued in general terms that older on-prem software is actually easier to integrate with. Andrew conceded the logic but the question was explicitly deferred to a POC or technical deep dive for validation. This was the single largest open risk item from Set 03 — the feasibility of the entire agentic approach depended on answering it.

Between meetings, Colin did the research. He opened this meeting (Meeting 4) by stating he had "done some homework" on behalf of the Sephora team and had "good news to share" (lines 46-52).

---

## 2. The SDK Discovery: Cognos and DataStage

### 2a. What Colin Found

Colin presented his findings directly (lines 146-153):

> "So the first thing is I did some homework on this so on Cognos and on DataStage both. Very good news for you. Beautiful, perfect, all-inclusive APIs or SDKs for both of them. These are old enough that they weren't APIs yet. They were just pure SDKs. They're available in both Java and .NET. That goes all the way back to even the earliest versions of Cognos. So as long as you're using a version that's after 2003, we're in good shape."

Note: The transcript renders "DataStage" as "DataSage" in this passage due to speech-to-text errors, but the meaning is unambiguous from context.

### 2b. Key Technical Details

The SDK findings contain several important specifics:

1. **Both Cognos and DataStage have full SDKs** — Colin described them as "beautiful, perfect, all-inclusive," indicating comprehensive coverage of functionality, not partial or limited interfaces.

2. **These are SDKs, not APIs** — Colin drew an explicit distinction. The tools are old enough that they predate the modern convention of exposing REST or web APIs. Instead, they ship traditional Software Development Kits in the older sense — libraries that are linked into applications at build time. This is a historically accurate characterization: IBM Cognos and DataStage from the mid-2000s era provided Java and .NET class libraries rather than HTTP-based service endpoints.

3. **Available in both Java and .NET** — Two language bindings, which gives BayOne flexibility in implementation. Java would be the more natural choice for server-side integration, but the availability of .NET means the approach is not constrained to a single technology stack.

4. **Backward compatibility to post-2003 versions** — Colin stated the SDKs go "all the way back to even the earliest versions of Cognos" and that "as long as you're using a version that's after 2003, we're in good shape" (lines 149-150). Since Sephora's Cognos is version 10.2 or 10.3 (released well after 2003), this places their environment squarely within the supported range.

5. **Complete access with no restrictions** — Colin reported that he could find no limitations on what the SDK exposes (line 161): "there's basically complete access to everything within Cognos with no restrictions that I could find." He characterized the SDK documentation as "very positive, well-documented, very established" (line 162).

### 2c. How This Resolves the Set 03 Feasibility Question

Colin stated the conclusion directly (lines 151-153):

> "So that is definitely there. We can definitely link into any of the Cognos reports for any past or current versions of IBM Cognos. So that is totally possible."

This is a definitive answer to Andrew's concern from the prior meeting. The feasibility question — "can agents connect to old Cognos 10.2/10.3?" — is answered affirmatively. The mechanism is not a modern API, not a database query against a content store, and not screen scraping. It is a supported, documented SDK that IBM ships with the product, available since the product's earliest post-2003 versions, covering the full breadth of Cognos functionality.

### 2d. DataStage SDK

Colin's reference to DataStage was briefer than his Cognos discussion but explicitly included in the same finding. He stated "on Cognos and on DataStage both" have "beautiful, perfect, all-inclusive APIs or SDKs" (line 146). The same SDK characteristics — Java and .NET, backward-compatible, full-coverage — apply to DataStage as well.

Later in the meeting, Sergey (Sephora's DataStage subject matter expert) raised DataStage as a second demo candidate beyond Cognos (lines 579-582). Sergey noted they had attempted DataStage-to-Databricks conversion using Claude directly and achieved approximately 85% accuracy but still required manual cleanup. This sets the stage for demonstrating that an agent with proper MCP connectivity and context management could improve on the 85% baseline that raw Claude interaction produced.

---

## 3. The MCP Server Concept

### 3a. What an MCP Server Is and Why It Is Needed

Colin introduced the MCP server concept immediately after the SDK findings (lines 154-159):

> "Just as a quick note, the way that we do this, we build what's called an MCP server. These don't typically already exist. So these are things that we build from scratch as part of what we do. This is not uncommon for us at all. We have to do this very often when it comes to legacy platforms. And essentially gives us a way to interact with that SDK programmatically with agents."

MCP stands for Model Context Protocol. It is the standard protocol by which AI agents connect to external tools and systems. An MCP server is a lightweight service that wraps a tool's native interface (in this case, the IBM Cognos Java or .NET SDK) and exposes it as a set of capabilities that an AI agent can invoke. Without an MCP server, an agent has no way to take actions in Cognos — it can reason about reports but cannot read, extract, or modify them. The MCP server is the bridge between the agent's intelligence and the legacy system's functionality.

### 3b. Colin's Experience Building MCP Servers

Colin made two credibility statements about BayOne's MCP server experience:

1. **"This is not uncommon for us at all"** (line 157) — Building custom MCP servers for legacy platforms is a routine activity for BayOne's AI practice, not a novel or experimental undertaking.

2. **"We have to do this very often when it comes to legacy platforms"** (lines 157-158) — The legacy platform qualifier is important. Colin is not saying they build MCP servers in general; he is saying they specifically build MCP servers for old systems that lack modern connectivity, which is exactly Sephora's situation. This implies a pattern of prior engagements where the AI practice has bridged agents to older enterprise software through custom MCP development.

### 3c. How the MCP Server Works with the SDK

Colin described the mechanics at a conceptual level (lines 158-161):

> "Essentially gives us a way to interact with that SDK programmatically with agents. So we define here's what some action should be taken as, here's all the different controls, constraints, and parameters that you can interact with with Cognos, and that basically gives you a mini-agent with the capability to take some action into Cognos."

The MCP server definition process involves:

1. **Defining actions** — Each operation the agent might need to perform against Cognos is defined as a discrete tool within the MCP server. The MCP server translates between the agent's request (in natural language or structured parameters) and the corresponding SDK call.

2. **Defining controls, constraints, and parameters** — Each action has a schema that specifies what inputs it accepts, what constraints govern its behavior, and what parameters the agent must provide. This prevents agents from making arbitrary or malformed SDK calls.

3. **Producing a "mini-agent with capability"** — The MCP server effectively gives the agent hands to work with Cognos. Without MCP, the agent can think but not act. With MCP, it can execute operations against the live Cognos environment.

### 3d. Specific Operations the MCP Server Enables

Colin described several specific capabilities that the MCP server would provide agents. These were articulated across multiple points in the discussion:

**Report Metadata Extraction (lines 166-168):**

> "Any of the data sets that are part of that report, any of the data, any of the other calculations or otherwise that might be a part of that report, rather than trying to access it through a human or even for the sake of verification, we can pull it out programmatically. So programmatic access is first and foremost."

This means the MCP server enables agents to:
- Pull the list of datasets referenced by a Cognos report
- Extract calculated fields and their definitions
- Read all metadata about a report's structure and dependencies
- Do all of this without a human manually opening Cognos and navigating the report studio interface

**SQL Extraction (lines 248, 269):**

Colin specifically mentioned the ability to "strip out the SQL" from Cognos reports via MCP. This is critical because, as Andrew explained in detail during the meeting (lines 210-217), many Cognos reports contain freehand SQL rather than relying on the Framework Manager model to generate queries dynamically. For those reports, the migration path requires extracting the SQL, converting it to Databricks-compatible syntax, and replacing it in the report definition. The MCP server automates the extraction step that Sephora's team was doing manually.

**Report Definition Access (lines 166-174):**

Colin described the MCP server as enabling agents to "more deeply explore" report nuances "rather than something that might just be a screenshot or some human notes that we're given" (lines 170-171). This means agents can read the full report definition programmatically — the same information a human would see by opening the report in Cognos Report Studio and examining its properties, queries, and layouts, but accessible at machine speed and without manual intervention.

**RBAC Information (lines 160-161):**

> "If you have things like with RBAC that you want to keep consistent between those two, depending upon how you have it set up right now, there's basically complete access to everything within Cognos with no restrictions that I could find."

RBAC (Role-Based Access Control) refers to the security model within Cognos that governs which users and roles can access which reports and data. Colin noted that the SDK exposes this information as well. This is significant for migration because if Sephora moves reports to a new platform or reconfigures them for Databricks, the access control rules need to be preserved. The MCP server would enable agents to read the current RBAC configuration and ensure parity in the migrated reports.

**Parity Verification (lines 169-171):**

> "The second is to make sure that we actually have good parity between the two. So if there's some nuance to it, we're able to more deeply explore that, rather than something that might just be a screenshot or some human notes that we're given."

The MCP server enables programmatic comparison between the original and migrated reports, which is more reliable and thorough than human-driven comparison based on screenshots or notes.

**Bidirectional Access (lines 173-175):**

Colin confirmed the MCP server supports both reading and writing:

> "Long story short, if it involves Cognos, we'll be able to interact with it, either pull information out, put information in, or otherwise take over."

This means agents could not only extract report metadata and SQL but also write updated configurations back to Cognos — for example, updating a report's data source connection from SQL Server to Databricks, or replacing freehand SQL with a Databricks-compatible version.

---

## 4. The Current Manual Process the MCP Server Would Replace

Sergey (Sephora's Cognos/DataStage SME) described the current manual workflow that the MCP approach would automate (lines 225-230):

> "Right now we're doing all of this manually, like exporting the XML from the Cognos and then, you know, extracting all the joints, the source tables, everything. We are using Claude right now to help us do all of that extraction. But getting that XML, that is still manual effort, we have to log into Cognos, go to report studio, download the XML."

The current process is:
1. A human logs into Cognos
2. Navigates to the report in Report Studio
3. Manually exports the report definition as XML
4. Feeds the XML to Claude for extraction of joins, source tables, and SQL
5. Uses Claude to assist with SQL conversion from SQL Server to Databricks syntax
6. Manually applies the converted SQL back to the report

Steps 1-3 are pure manual effort that the MCP server would eliminate entirely by giving agents direct programmatic access to the same report definitions. Steps 4-5 are already partially AI-assisted but lack the context management and orchestration that an agent framework provides. Step 6 would potentially be handled by the MCP server's write capability.

Colin directly addressed this workflow pattern (lines 244-249):

> "You'll always find a very good indication that you need MCP in the mix is if you find a human being copying and pasting or taking screenshots of something and passing it out to a language model. It's a very good indication that there's something that should be there with MCP that might not be there yet. So MCP just gives us a way to connect into applications like we would have to build for Cognos. So we're able to strip out the SQL for it."

This is a diagnostic heuristic for identifying where MCP servers should be built: any workflow where a human is manually mediating between a legacy system and an AI tool is a candidate for MCP automation.

---

## 5. The Demo Approach vs. Production Approach Distinction

### 5a. The Security Constraint

A critical distinction emerged during the meeting between how the MCP server would work in production and what would be feasible for the proof-of-concept demo. Sergey and the Sephora team raised the security constraint (lines 474-483):

Sergey noted that when the team tried to run their own agents against the Cognos environment, "we get blocked by security" (line 477). However, he then explained that migration work had been successfully performed without live system access by working from exported definitions:

> "We did the migration, and we have the definition of the job, the DataStage, or the report definition. And when we pointed basically to Databricks... the agent can do the work, the migration work, without having access, without validating whether it's working or not."

Andrew (referred to as "my hair" in the transcript due to speech-to-text errors — this is Andrew, the enterprise architect) confirmed that security approvals for external agent access to Cognos would require going through Sephora's security review process, which had already blocked internal attempts.

### 5b. The Agreed Demo Approach: Exported XML, Not Live MCP

Given the security constraint, the team converged on a demo approach that does not require live MCP connectivity to Cognos:

1. Sephora would provide the XML export of a Cognos report definition (the same artifact they currently export manually from Report Studio)
2. BayOne would demonstrate the agent's ability to parse, extract, and convert the report using that exported XML
3. No live connection to Sephora's Cognos environment would be required

This was agreed to by both sides. Colin expressed relief (line 572): "I'm kind of breathing a sigh of relief. We don't have to set up a, you know, independent Databricks instance for a demo." The team decided to pick one finance report as the demo candidate (line 565): "We can pick one report from finance."

Sergey asked whether Colin needed the full XML or just the SQL query (line 566): "Are you looking for the XML or just the SQL query?" This was left for follow-up, but the intent was to provide a complete report definition.

### 5c. The Production Vision: Live MCP Connectivity

The demo approach using exported XML is explicitly a compromise for the proof-of-concept phase. The production approach would use the full MCP server with live SDK connectivity to Cognos, eliminating the manual export step entirely.

Colin described the production architecture earlier in the meeting (lines 538-543):

> "So it sounds like if we can get one of the Cognos reports, what we will be able to do is we can take that, build the MCP for it, make sure that we can A, connect to it, B, dissect it, and be able to get into it. I know, as you said, the SDK, they're not pretty, but we have ways to do this, and we use AI ourselves to help them build these."

The distinction is:
- **Demo/POC:** Agent receives exported XML as input; processes it offline; no live Cognos connectivity; no security review needed; faster to set up
- **Production:** MCP server connects directly to Cognos via the Java/.NET SDK; agents can read and write to Cognos programmatically; eliminates all manual export steps; requires security team approval

### 5d. Colin's Offer to Help with Security Unblocking

Colin proactively addressed the security blocker for the eventual production deployment (lines 643-667):

> "So if the security team, you said they blocked an MCP server that you tried to create for this one? So is that something that also you might have some trouble with or something that we can help with? I'll say it like this. We do this all the time, so we're used to talking to IT and security teams to kind of tell them, no, we're not crazy. No, we're not going to hurt anything. We know how to talk to them about this to kind of unblock things."

Colin then described his approach to security conversations (lines 663-667):

> "I think as soon as people understand like, hey, we're doing this with your own tools within your own environment, literally no information goes beyond that. That takes care of about 80% of the... I would say knee-jerk reaction to say something's dangerous in the IT space. And the remaining 20%, we can say, any guardrails you want, we can put in the system."

This experience claim — "we do this all the time" — positions BayOne as having institutional experience navigating enterprise security reviews for agentic AI deployments, which is directly relevant to overcoming the barrier that had already blocked Sephora's internal attempts.

---

## 6. How MCP Fits into the Broader Agent Architecture

Colin positioned MCP as the connectivity layer within a broader agentic architecture. Throughout the meeting, he described the relationship between MCP and agents in several ways:

### 6a. MCP as the Agent's Toolbox

Line 243-244: "Agents plus MCP is the way to go here, for sure. MCP is essentially a connector to all these tools."

Line 289: "Getting them combined with MCP so they have the right tools at their disposal whenever they need to actually go and take some action, that is where the power comes in from this."

### 6b. Multiple MCP Servers for Multiple Systems

Colin described MCP as applicable across the full tool stack, not just Cognos (lines 378-379):

> "With Databricks itself, whether that's SQL Server, whether it's Cognos, MCP just becomes the connector into those things."

This implies the production architecture would involve multiple MCP servers:
- One for Cognos (built on the IBM Cognos Java/.NET SDK)
- One for DataStage (built on the IBM DataStage SDK)
- One for SQL Server (potentially leveraging existing connectors)
- One for Databricks (potentially leveraging existing connectors or the Databricks SDK)

Colin noted that for standard platforms like Databricks, MCP connectors may already exist (referencing his earlier comment that "the more normal things are, the more support there is, the more likely it is that someone already has made a connector" — from Set 03). The custom build effort is specifically for the legacy tools — Cognos and DataStage — where pre-built MCP servers do not exist.

### 6c. Specific Agents Enabled by MCP

Colin listed specific agents that would operate through MCP connections (lines 267-272):

> "For instance, something to extract report metadata or something to go and parse SQL and figure out what the equivalent would be in Databricks. And maybe this isn't even one agent, maybe it's two. Maybe there's one that's a Databricks agent, one that's SQL Server and one that takes both of their inputs and then figures out what the rehashing of the SQL might be in order to keep that report working."

The agent decomposition enabled by MCP includes:
1. **Report metadata extraction agent** — Uses MCP to connect to Cognos and pull report structure, datasets, calculations, and dependencies
2. **SQL parsing agent** — Extracts SQL from report definitions and analyzes its structure
3. **Databricks agent** — Understands the Databricks environment (schema, tables, data types) through its own MCP connection
4. **SQL Server agent** — Understands the legacy SQL Server environment through MCP
5. **SQL conversion agent** — Takes input from the SQL Server agent and Databricks agent to produce converted queries
6. **Validation agent** — Can take screenshots of reports or perform point-wise validation on key values (line 282)

---

## 7. The DataStage Conversion Opportunity

### 7a. Sergey's Experience with Claude for DataStage

Sergey (Sephora's DataStage SME, who has been "the developer for us throughout the last 10, 15 years" per Andrew at line 133) raised DataStage as a second candidate for the demo (lines 579-582):

> "If you want to extend the demo one of the DataStage and see how that work on the address because we did that with Claude. But it was almost like 85% need to do something."

This means the team has already attempted DataStage job conversion using Claude directly (without agents or MCP) and achieved approximately 85% accuracy — meaning 15% of the output still required manual correction.

### 7b. Sergey's Framework Constraint

Sergey provided critical detail about the target state for DataStage migration (lines 585-604). The target is not arbitrary Python notebooks or new code — it is an existing, mature Databricks framework that the team has already built and runs in production:

> "On Databricks, we develop frameworks, color-based, where you don't need to do, let's say, Python development or something. So you just need to do configuration. And we have, let's say, thousands of jobs running in production today."

The key constraint: the DataStage agent does not need to write code. It needs to generate YAML configuration files with specific parameters (source table name, connection details, etc. — "20, 50 different parameters" per line 603). This is actually simpler than code generation, as Sergey noted (line 605): "It's even simpler than write code. But just we need to see how agent can do it."

Sergey explicitly warned against the approach Claude had taken (lines 596-598):

> "We're just converting some, be honest, spaghetti code. When you have Databricks notebook with hundreds of Windows inside this notebook and how to maintain it. I don't know if it will be nightmare, you know, to debug it and so on."

This is a direct critique of the Claude-only approach (without agents or MCP) — it produces working code but in a format that is unmaintainable and incompatible with the existing production support model. The agent approach needs to be aware of the target framework and generate output that conforms to it, not just produce functionally equivalent code in an arbitrary format.

### 7c. Sergey's Ideal Scenario

Sergey articulated the ideal end state (lines 607-610):

> "If we can ask him... hey man, we have 10 jobs, please convert them, generate YAML files, commit them to packet. After that, some developer can quickly review that it's good and that's it."

This is a concrete, measurable success criterion for the DataStage agent: given a set of DataStage jobs as input, produce YAML configuration files conforming to the existing Databricks framework, and commit them to version control for human review.

---

## 8. Sergey's Skepticism: "Easier Said Than Done"

Sergey, as the hands-on Cognos and DataStage developer with 10-15 years of experience on Sephora's specific environment, expressed measured skepticism about Colin's presentation. After the broader team said Colin's strategy was aligned with their thinking, Sergey added (lines 409-411):

> "It's easy said than done. I worked with Collins, I wrote code for the BI server, and that's a complicated word."

Note: "Collins" is a speech-to-text rendering of "Cognos" and "BI server" refers to the Cognos BI Server component. Sergey is speaking from direct experience writing code against the Cognos SDK/API and noting that it is genuinely complicated, not something that should be taken lightly. This is not a rejection of the approach but a reality check from the person who has actually worked at the SDK level — a useful counterweight to Colin's optimistic framing of the SDK as "beautiful, perfect, all-inclusive."

---

## 9. Summary: What Was Resolved and What Remains Open

### Resolved

| Question | Resolution |
|---|---|
| Can agents connect to old Cognos (10.2/10.3)? | Yes. Full Java and .NET SDKs exist back to post-2003 versions. Colin verified this through research between meetings. |
| Can agents connect to DataStage? | Yes. Same SDK availability as Cognos — full Java and .NET SDKs. |
| Is building a custom MCP server for Cognos feasible? | Yes. Colin stated this is "not uncommon for us at all" and is a routine activity for BayOne's AI practice with legacy platforms. |
| What can agents do once connected via MCP? | Extract report metadata, parse SQL, read report definitions, access RBAC information, verify parity, and write updated configurations back to Cognos. |

### Agreed for Demo

| Decision | Detail |
|---|---|
| Demo will use exported XML, not live MCP | Sephora's security team blocks external agent access to their Cognos environment. The demo will work from manually exported report XML. |
| Sephora will provide one finance report | The team agreed to select a representative Cognos report from the finance subject area. |
| Databricks schema information will be provided | The agent needs to know the target table structure in Databricks to perform the conversion. |
| DataStage conversion is a potential second demo track | Sergey offered a simple DataStage job as an additional candidate, benchmarked against the 85% accuracy they achieved with direct Claude use. |

### Open / Deferred to Production Phase

| Item | Status |
|---|---|
| Security team approval for live MCP connectivity | Required for production but bypassed for the demo. Colin offered to help navigate the security conversation. |
| Production MCP server build for Cognos | Will be needed once the demo validates the approach and the engagement moves forward. |
| Production MCP server build for DataStage | Same status — deferred pending demo results. |
| MCP server complexity with the actual Cognos SDK | Sergey's caution that the BI server SDK is "complicated" remains unresolved. The demo using exported XML sidesteps this complexity but does not validate it. |
| RBAC migration via MCP | Colin mentioned RBAC access is available through the SDK but no specific demo or validation was planned for this capability. |
