# Meeting 4: Sephora Technical Deep Dive

**Date:** Early March 2026
**Location:** Remote (Video Call)
**Duration:** ~50 minutes
**Recording Status:** Recorded with transcription

---

## Participants

| Name | Organization | Role | Scope in Meeting |
|------|--------------|------|------------------|
| Colin Moore | BayOne | Director of AI | Technical presenter, demo scoping lead |
| Neha Malhotra | BayOne | VP Growth & Customer Success | Meeting facilitator |
| Zahra Syed | BayOne | Sales | Support |
| Andrew Ho | Sephora | Sr. Director, Data & Analytics | Vision owner, meeting rescue |
| Gariashi Chakrabarty | Sephora | Director, Data Engineering | Technical gatekeeper |
| Maher Burhan | Sephora | Enterprise Architect (Consultant) | Architecture validation, practical solutions |
| Sergey Shtypuliak | Sephora | SME - IBM Tools (Consultant) | Deep technical expertise, requirements specification |
| Itisha Singh | Sephora | Data & Analytics | Participant |

**Context:** This meeting was intended to gather technical requirements for building a demo. However, Sephora expected to see a demo today. The disconnect was resolved gracefully and the meeting pivoted to productive technical deep dive.

---

## Transcription

The following corrections were applied throughout this document:

| Original | Corrected |
|----------|-----------|
| "Shaka" | Zahra Syed |
| "my hair", "Mahir", "Malika" | Maher Burhan |
| "Sir" (some contexts) | Sergey Shtypuliak |
| "Gaurishi", "Garishia", "Karish" | Gariashi Chakrabarty |
| "Cardinals", "Card notes", "coughing" | Cognos |
| "Lake bridge" | Lakehouse |
| "EW" | EDW |

---

## Meeting Structure

1. **Phase 1:** Opening & Introductions (~3 min)
2. **Phase 2:** Colin's Recap & Framing (~7 min)
3. **Phase 3:** Expectation Mismatch Revealed & Resolved (~5 min)
4. **Phase 4:** Colin's Technical Presentation (~10 min)
5. **Phase 5:** Andrew's Workflow Walkthrough (~10 min)
6. **Phase 6:** Schema Mapping Methodology Discussion (~7 min)
7. **Phase 7:** Q&A and Demo Scoping (~8 min)
8. **Phase 8:** Next Steps Agreement (~2 min)

---

## Discussion Topics (Chronological)

### 1. Expectation Mismatch and Recovery

The meeting began with an expectation gap. Sephora expected to see a demo today, while BayOne expected to gather requirements for building a demo.

Gariashi surfaced the disconnect directly, stating the team was "excited to see the demo today." Colin acknowledged the gap and Neha apologized for any miscommunication. Andrew rescued the meeting by reframing it as an opportunity for BayOne to gather information from their technical experts.

**Key Quote (Andrew):**
> "I don't think we necessarily need to have support data to actually demo, but it's really about demoing the capability, right? Whether you guys can or whether it's even possible to create all those different smaller agents and have an orchestrator agent to orchestrate all the smaller agents."

### 2. Cognos/DataStage Integration Research

Colin presented research findings on integrating with legacy IBM tools. He confirmed that both Cognos and DataStage have complete SDKs available in Java and .NET, compatible with versions dating back to 2003.

Colin explained the MCP server approach: building custom connectors that provide agents with programmatic access to legacy systems. These are not pre-existing tools but custom-built integrations that BayOne creates regularly for legacy platforms.

**Key Quote (Colin):**
> "On Cognos and on DataStage both - very good news for you. Beautiful, perfect, all-inclusive APIs or SDKs for both of them. These are old enough that they weren't APIs yet. They were just pure SDKs."

### 3. Current Manual Workflow

Gariashi described the current state: using Claude manually for XML extraction and SQL translation, but the process requires significant human intervention. Getting XML from Cognos requires logging into Report Studio and downloading manually. No end-to-end agent exists yet.

**Key Quote (Gariashi):**
> "We are using Claude right now to help us do all of that extraction. But getting that XML, that is still manual effort, we have to log into Cognos, go to report studio, download the XML."

### 4. Andrew's Complete Workflow Walkthrough

Andrew provided a comprehensive explanation of the two types of Cognos reports:

**Framework Model Reports:** Point to IBM Framework Manager Model, which generates SQL dynamically. Migration requires updating the Framework Model to point to Databricks. Reports automatically work if the model is updated correctly.

**Freehand SQL Reports:** Contain custom SQL written directly in queries. Requires extracting SQL, converting to Databricks syntax, testing, and replacing in the report.

Andrew articulated the agent vision: many small specialized agents doing specific tasks, coordinated by an orchestrator agent.

**Key Quote (Andrew):**
> "Is there any way throughout this step that we can create agents? I'm not expecting one agent do it... it's like a lot of smaller agents, agents do a small little thing, you have a lot of this small little agent, and then they just do their own responsibility, do the whole thing, and then you have that one orchestrator to just orchestrating this whole entire all the smaller agents."

### 5. Schema Mapping Methodology

Colin presented the three-phase approach to schema mapping:

**Phase 1 (Structural Discovery - No AI):** Crawl and map tables, columns, relationships, data types on both SQL Server and Databricks sides.

**Phase 2 (Rule-Based Mapping - No AI):** Identify exact matches and known patterns with 100% certainty.

**Phase 3 (AI-Assisted Mapping):** Fill in gaps using semantic similarity and contextual analysis.

Colin explained confidence-based routing, where confidence comes from human reinforcement, not AI guessing. The system learns from human approvals and gradually increases autonomy.

**Key Quote (Colin):**
> "Whenever a human goes and reinforces a decision made by AI, that is confidence. So if you say yes, you are correct or no, you are wrong, that is what determines confidence."

### 6. DataStage Framework Requirements

Sergey Shtypuliak provided critical specifications for DataStage conversion. The existing Databricks framework is configuration-based (YAML files), not code-based. Thousands of jobs already run in production using this framework. The ideal agent output is YAML configuration files, not Python or Scala code.

Sergey Shtypuliak also criticized the Lakehouse approach, calling it "spaghetti code" with notebooks containing hundreds of nested notebooks that are difficult to debug and maintain.

**Key Quote (Sergey Shtypuliak):**
> "Main question right now, how to teach these agents to understand that, okay, we need to create three YAML files with some configuration inside. Let's say 20, 50 different parameters like source table name, connection details and so on. So you don't need to write code itself, just to create config file."

### 7. Security Constraints and Workaround

Maher acknowledged that security has blocked previous attempts to run agents in the environment. Rather than fighting this constraint, he proposed a practical workaround: do the conversion work without direct system access, then validate separately.

Colin offered to help with security/IT conversations if needed in the future, noting that BayOne does this regularly with enterprise clients.

**Key Quote (Maher):**
> "The agent can do the work, the migration work, without having access, without validating whether it's working or not."

### 8. Demo Scope Agreement

The team agreed on a focused demo approach:
- Sephora provides one Cognos report XML from Finance track
- Sephora provides Databricks catalog/schema information for target mapping
- BayOne builds MCP connector and demonstrates lift-and-shift conversion
- No direct system access required
- Validation happens separately by Sephora
- Optional: Include simple DataStage job for additional scope

---

## Decisions Made

| Decision | Made By | Context |
|----------|---------|---------|
| Demo will use real Cognos report, not mock data | Group | More relevant, less BayOne setup work |
| No direct system access for demo | Maher | Avoids security hurdles |
| Focus on Finance track report | Andrew | Aligns with current project priorities |
| DataStage conversion outputs YAML, not code | Sergey | Must fit existing framework |

---

## Commitments Made

### Sephora Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| Gariashi | Provide Cognos report XML from Finance folder | Not specified |
| Maher/Sergey | Provide Databricks schema/catalog information | Not specified |
| Andrew/Team | Internal discussion on additional demo needs | After this call |
| Maher | Consider providing simple DataStage job | Optional/tentative |

### BayOne Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| Colin | Build demo with provided materials (MCP + conversion) | After receiving materials |
| Neha Malhotra | Schedule demo session | After materials received |
| Colin | Help with security conversations if needed | Standing offer |

---

## Open Items / Next Steps

| Item | Owner | Priority | Notes |
|------|-------|----------|-------|
| Provide Cognos report XML | Gariashi (with Vlad) | High | Full XML from Report Studio, Finance folder |
| Provide Databricks schema info | Sephora team | High | Catalog and table structure |
| Build MCP connector for Cognos | Colin | High | Pending materials |
| Internal discussion on scope | Andrew/Gariashi | Medium | May add requirements |
| Schedule demo session | Neha | Medium | After materials received |
| Consider DataStage job sample | Maher | Low | Optional additional scope |

---

## Key Quotes

**Colin on MCP indicators:**
> "A very good indication that you need MCP in the mix is if you find a human being copying and pasting or taking screenshots of something and passing it out to a language model."

**Andrew on agent vision:**
> "I'm not expecting one agent do it... it's like a lot of smaller agents, agents do a small little thing, and then you have that one orchestrator to just orchestrating this whole entire all the smaller agents."

**Sergey on DataStage requirements:**
> "No need to write code itself, just to create config file. It's even simpler than write code."

**Sergey on healthy skepticism:**
> "It's easy said than done. I worked with Collins, I wrote code for the BI server, and that's a complicated word."

**Colin on confidence flywheel:**
> "If I've said, yes, you can do this five times in a row, and time number six, you don't need to ask me to do it."

---

## Key Insights

1. **Security is a solved problem:** Maher's workaround (no direct access) elegantly bypasses what could have been a blocker.

2. **Sergey Shtypuliak defines success criteria:** The agent must output YAML config files that fit their existing framework, not custom code.

3. **Andrew is an internal champion:** He rescued the meeting and positioned BayOne for success.

4. **Databricks is mature:** The platform itself is production-ready with thousands of jobs. Only EDW-specific migration is new (started January 2026).

5. **Framework Model vs Freehand SQL:** Two distinct migration patterns exist for Cognos reports, requiring different agent approaches.

---

## Clarifications Needed

1. Which specific Finance report will be provided?
2. What format should the Databricks schema information take?
3. What is the timeline expectation for the demo?
4. Are there YAML config examples for DataStage that could inform agent output format?

---

## Next Meeting

**What:** Demo of Cognos report conversion capability
**When:** TBD (after materials received)
**Who:** Same participants expected
**Purpose:** Demonstrate feasibility of agent-based migration on real Sephora artifacts

---

## Files Referenced

- IBM Cognos SDK documentation
- IBM DataStage dsjob/dsexport utilities
- Databricks catalog/schema (to be provided)
- YAML configuration framework for DataStage jobs (existing at Sephora)
