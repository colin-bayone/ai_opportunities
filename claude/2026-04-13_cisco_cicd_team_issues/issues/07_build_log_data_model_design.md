## Draft Initial Data Model for Build Log Analysis

### Description

Design a star schema data model for persisting build log analysis results and related metadata. This model needs to support downstream agentic AI access (via MCP tools) and provide traceability from build failures back to specific commits and PRs.

### Background

- Cisco wants commit-level transparency: which commit introduced which failure
- Justin's current approach stores metadata in MySQL (build number, date, status) but logs are only on NFS
- The existing Python script extracts a subset of errors and passes them to an LLM, with no structured persistence of the analysis results
- Colin's guidance: star schema is the best approach for enabling downstream agentic AI; avoid NoSQL/JSON for this use case

### Design Principles

**What to persist:**
- Build metadata (build ID, timestamp, branch, status, duration, trigger type)
- Error classifications (error code, severity, category, source file, line reference)
- Analysis results (summaries, suggested fixes, confidence scores)
- Cross-references (SHA hashes for commits, PR numbers)

**What to query live via MCP/Git (do not persist):**
- Git commit lineage and PR membership (use SHA hash as the key, query Git in real-time)
- Full commit diffs (available via Git)
- PR review comments and status (available via GitHub API)
- File contents at a specific commit (available via Git)

**Key identifiers:**
- SHA hashes are the primary link between build logs and Git history
- PR numbers link to GitHub
- Build IDs link to the Cisco build portal and MySQL metadata

### Tasks

- [ ] Draft an entity-relationship diagram for the star schema
- [ ] Define fact table: build_analysis_facts (one row per error per build)
- [ ] Define dimension tables: dim_builds, dim_errors, dim_repos, dim_branches
- [ ] Define the MCP tool interface: what queries should an agent be able to run against this schema?
- [ ] Document which fields come from log parsing vs MySQL metadata vs Git queries
- [ ] Consider: how does CI (developer builds) vs CD (nightly builds) affect the schema?
- [ ] Consider: multiple log files per build; should log_file be a dimension?

### Dependencies

- Depends on log mapping work (issue #6) to understand the actual structure and fields available in log files
- Architecture working session with Colin is planned for this week

### Acceptance Criteria

- [ ] ER diagram drafted
- [ ] Fact and dimension tables defined with field lists
- [ ] MCP tool query interface sketched (what questions should an agent be able to answer?)
- [ ] Decision documented: what gets persisted vs what gets queried live
