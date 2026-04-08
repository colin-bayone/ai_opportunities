# Team Briefing Doc: Content Outline (v2)

Structured as: what to do, then context to do it well.

---

## PART 1: ACTION ITEMS

### First Tasks

1. **WebEx space scraper.** Download the NXOCI workflow WebEx chat content, summarize user issues, rank by priority and severity. This is our starting point for understanding what Cisco engineers actually struggle with. Naga on Srinivas's team may have existing code for this. There is also a public WebEx API. Srinivas expects this to be fast. Build it as a reusable plugin, not a one-off script. Orchestrate with Airflow using Cisco's existing Airflow instance, not a standalone one.

2. **Meeting recording transcriber.** Second plugin: given a WebEx recording, dump the transcript, summarize, extract action items. Prompt-driven, reusable across any WebEx space.

3. **Build log analysis with Justin Joseph.** Meet with Justin (1-2 sessions) to understand the build log structure: official builds (nightly, 1000+ engineer commits) vs. user builds (single PR). Understand log format, typical size, failure types, what tools Justin already has. This must happen before any design work on failure analysis.

4. **Resolve GitHub MFA.** There is a Duo MFA infinite loop blocking GitHub Enterprise access. Raise an IT case and call the support number. This is the single biggest access blocker.

### Design Constraints (Apply to All Work)

5. **Build for reuse.** Everything we build will be used beyond CI/CD. Srinivas was explicit: do not assume anything is single-purpose. Plugins, MCPs, pipelines, all of it must be designed for reuse across DeepSight applications.

6. **Inference cost discipline.** Cisco's inference costs have increased 4X. Srinivas will reject any approach that throws large logs or raw data at a language model without preprocessing. Engineer the solution properly. This is a screening criterion.

7. **Understand before designing.** Spend time with Justin and the build infrastructure before proposing architecture. Srinivas wants the team to understand the artifacts, the log structure, and the failure modes firsthand.

### Team Logistics

8. **Twice-weekly recurring meetings** with Srinivas's extended team are now established. All team members should be available.

9. **Srinivas has requested profiles and resumes** for the two on-site team members. Colin will handle this.

10. **If CI/CD work is blocked on access or dependencies, Srinivas will assign other DeepSight work.** No one should be idle.

---

## PART 2: CONTEXT

### New Cisco Contacts

- **Anupma Sehgal**: Lead engineer, DevEx organization. Co-owns the CI pipeline with Divakar's team. Controls CAT-related databases (likely Cassandra). Represents a separate Cisco organization from Srinivas. She has reservations about exposing database access, and cross-org negotiation is required.

- **Justin Joseph**: Engineer on Srinivas's team, build infrastructure. Owns MySQL databases for official builds, NFS for logs (3-5 day retention policy), and an existing basic MCP (can query latest QA-turning rate, most recent build, sanity results). Has built AI-based fix suggestion tools. He is the primary technical counterpart for build log work.

- **Naga**: Engineer on Srinivas's team. Has existing WebEx automation plugins (chat content scraper, recording transcriber). May have committed code already. Colin will connect the team with Naga.

- **Mazar and Tim**: Work on the call graph and CLAM/LAM system. Relevant for the impact analysis work (which function changed, what is the blast radius). Justin will coordinate with them.

### MCP as the Integration Pattern

All data sources feeding the CI/CD application on DeepSight need to be exposed through MCPs (Model Context Protocol). The workflow Srinivas defined:

1. Inventory existing data sources and databases
2. Check if MCPs already exist for each source
3. If yes, evaluate the tool calls they support
4. If no, create MCPs
5. Map tool calls to user needs
6. Design all tool calls to serve both self-serve (user asks a question) and agentic (system takes action) modes

This is how our work plugs into the DeepSight platform.

### Expanded Database Landscape

In addition to what was previously known (MySQL, MongoDB):

- **Cassandra**: CAT/DevEx data, controlled by Anupma's team. APIs exist but the database is not directly exposed. Access requires cross-org negotiation.
- **NFS**: Build logs stored here, consumed by engineers and sanity systems, retained only 3-5 days. Logs must be processed in near-real-time or copied out before they expire.
- **Justin's MySQL**: Official build data (triggered status, pass/fail, artifacts). Sanity results also posted here.

### Call Graph and Impact Analysis

The CLAM/LAM system can generate call graphs at compile time. Two approaches:

1. **Baseline**: Generated from nightly builds, stored as a lookup database. Shows function-level caller/callee relationships across the entire codebase.
2. **Dynamic**: Generated on the fly for new or modified files not yet in the baseline. Covers new additions that the nightly build has not picked up.

This is distinct from CRFT, which runs on the physical switch and tracks runtime function coverage. The call graph is static analysis at compile time. Both are independent data sources.

### CI Pipeline Co-Ownership

The CI/CD pipeline is co-owned by two Cisco organizations: Divakar's data center team and Anupma's DevEx team. Services that need to be automated span both organizations. This means some access requests go through Divakar, some through Anupma, and coordination between the two is required. Srinivas can direct Divakar's team but must negotiate with Anupma's.

### GitHub MFA Blocker (Detail)

When connecting to GitHub Enterprise via VPN and attempting Duo authentication, the system enters an infinite loop. It asks to add a device but only offers the physical security key option (FIDO). Touch ID and push notifications are not presented as options. The fix path is an IT support case. Other team members (Divakar, Justin) do not experience this issue, so it appears to be account-specific.
