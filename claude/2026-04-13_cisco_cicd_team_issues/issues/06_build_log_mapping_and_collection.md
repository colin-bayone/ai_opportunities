## Map Available Log Types on ADS and Collect Bazel Log Samples

### Description

Before designing the log analysis architecture, the team needs firsthand knowledge of what log files exist, how they are structured, and whether they are consistent over time. This is the foundational data collection work that informs all downstream architecture and processing decisions.

### Background

From meetings with Justin (week of 2026-04-07):
- Build logs are stored on NFS, accessible via ADS machines
- Metadata (build number, date, status) is in a MySQL database accessible through a web portal
- Actual log files are not in the database; they must be retrieved from NFS
- A single Bazel build generates multiple log files (12-15 observed), ranging from 50K to 500K lines each
- Justin's current work: a Python script that extracts some top-level errors, passes them to an LLM for summary and fix suggestions (PR #642 in the DCN/tools repo)
- Gmake logs are excluded per Srinivas directive (Gmake is legacy on nx_main; Bazel is the focus on nx_dev)

Namita currently has:
- Temporary ADS access (granted 2026-04-10, valid for 4 weeks)
- GitHub repo access (granted 2026-04-10, includes visibility into Justin's PR)
- Access to dev environment Bazel logs (recent logs, all passing; no failures in the past 4 days)

### Tasks

**Log Type Mapping:**
- [ ] Document all log types available on the ADS machine (not just Bazel)
- [ ] Identify CI logs (developer builds triggered by PRs) vs CD logs (nightly production builds)
- [ ] Determine if nightly build (CD) logs are accessible from the same NFS location or require separate access
- [ ] Check whether log files are composite (multiple applications blended into one file) or individual per application/stage
- [ ] Document: within a single Bazel build, what are the 12-15 log files? Are they per-stage, per-module, or something else?
- [ ] Note the NFS path structure and how logs are organized (by date? by build number? flat directory?)

**Sample Collection:**
- [ ] Collect Bazel log samples from the dev environment, even if all are passing builds (passing logs are still valuable for understanding format and structure)
- [ ] Organize collected samples in folders: date, build type (nightly/user), source
- [ ] Collect samples over multiple days to verify format consistency over time
- [ ] Select samples from different time points if available (oldest accessible, middle, newest) to detect any format changes
- [ ] Collect both success and failure logs when failure logs become available

**Automation:**
- [ ] Write a simple script to automate log collection rather than manually downloading files daily
- [ ] Script should run over VPN, connect to NFS, and pull new log files into an organized local directory
- [ ] This is for internal use only; does not need to be polished

**Production Log Access (Priority):**
- [ ] Request read-only access to the NFS server containing production (main branch) build logs
- [ ] If direct access is not possible, request log file samples from Justin, but push for access over samples (samples selected by non-AI practitioners are typically unrepresentative)
- [ ] Escalate through Colin to Srinivas if access is blocked

### Key Questions to Answer

1. Are the log files consistent in format across multiple days and builds?
2. Is there a log format version history (did the format change at some point)?
3. Are logs from NFS the raw Bazel output, or have they been processed/truncated by a custom layer?
4. What is the source of truth: the raw Bazel stderr/stdout, or something post-processed?

### Acceptance Criteria

- [ ] Log type map documented (what exists, where, CI vs CD)
- [ ] At least 3 days of Bazel log samples collected from dev environment
- [ ] Log file structure and organization documented
- [ ] Collection script operational (even basic)
- [ ] Production log access requested or escalated
