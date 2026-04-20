# 02a - Namita Deliverable: Build Log Analysis Updates (Reference Document)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/Build_log_analysis_upadtes_04102026.pdf
**Source Date:** 2026-04-10 (prepared for Friday standup, shared with team chat 4/15)
**Document Set:** 02a (supplementary to Set 02, individual team member deliverable)
**Pass:** Full decomposition of Namita's structured reference document

---

## Document Overview

This is a 6-page PDF titled "Build log analysis project updates (04/10/2026)" marked "Cisco Confidential." Namita prepared this document before the Set 01 standup and presented its contents during that meeting. She later shared related materials (architecture diagrams, log mapping) via the team chat on 4/15. The PDF was uploaded to the team source folder on 4/16.

The document has three sections: (1) Cisco setup access links with steps and status, (2) Meeting links, and (3) Build log analysis understanding from Justin's calls. It includes screenshots from Cisco's internal portals and terminal sessions on ADS machines.

---

## Section 1: Cisco Setup Access Links, Steps, and Status

### 1. Temporary ADS Machine

| Field | Detail |
|-------|--------|
| Portal | https://adsrsvp.cisco.com/#/adsman |
| Note | Do not append @cisco.com to userid |
| Status (as of 4/10) | Request in queue; access received morning of 4/10 |
| Machine type | RHEL8 |
| Lease duration | 4 weeks |
| Availability status | Queued |

**Evidence:** Screenshot of ADS queue confirmation email from `adsmanager@adsrsvp.cisco.com` to `Namita Mane -X (namane - BAYONE SOLUTIONS INC at Cisco)`.

### 2. Permanent ADS Machine

| Field | Detail |
|-------|--------|
| Portal | https://managed.cisco.com/personal-resources |
| Provisioning path | Deploy+ button > Aurora |
| Template | Aurora Development System (ADS) |
| Tenant | DCN Switching |
| Build Environment ESP Application | All_Data Center Networking_BSEs-IT Infrastructure |
| Location | San Jose, US |
| Host Alias | Alphanumeric characters and hyphens only; must include CEC ID |
| REALM Bundle | CN-SJC-ND |
| Operating System | Aurora: RHEL8 |
| CPU x Memory | 8CPU, 32GB |
| Local Storage | 100 GB |
| Status (as of 4/10) | Unable to see DCN Switching as Tenant in portal |

**Evidence:** Screenshot of the Aurora Development System deployment form showing all fields populated.

**REALM bundle request:**
- Request portal: https://realm.cisco.com/asset-search
- Bundle requested: CN-SJC-ND
- Status: Request raised
- Email confirmation: From `REALM@cisco.com` to `Gangfeng Kong (gakong); gmurthy@cisco.com; +31 more` confirming user `namane` requested access to bundle CN-SJC-ND
- Email states: "If you want to provide access, you would have to add this person to the usergroup: CN_REALM.GROUPER through https://myid-groups.cisco.com/groups"
- Email explains recipients are listed as bundle owners

**Todo:** Talk with support to add DCN Switching Tenant.

**Key observation:** The REALM bundle request email was sent to 33+ people (Gangfeng Kong, gmurthy, +31 more). These are all bundle owners who can approve the request. The approval path goes through https://myid-groups.cisco.com/groups, not through a ticket or automated system. This means approval depends on one of 33 people manually adding Namita to the usergroup.

### 3. GitHub Repository Access

| Field | Detail |
|-------|--------|
| Access portal | https://oneaccess.cisco.com |
| Group to request | A2G_group |
| Status (as of 4/10) | Requested access |

**Evidence:** Screenshot of oneaccess.cisco.com showing "Manage User Access" page with Namita's identity selected and A2G_group being added. The A2G_group description visible in screenshot: "For cross functional teams" / Type: Entitlement / Owner: `10006-NX Github - CI Pipeline for NX codebase in GitHub_A2G_group-Owner` / Application: Active Directory Post / Integration Method: memberOf / Logical Application: `NX Github - CI Pipeline for NX codebase in Github`

**After access, per Justin:**
- Tools repo: https://wwwin-github.cisco.com/DCN/tools
- Once logged in, Justin will provide access
- AI triage tool PR: https://wwwin-github.cisco.com/DCN/tools/pull/642

### 4. Training Course

| Field | Detail |
|-------|--------|
| Link | https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8 |
| Status (as of 4/10) | Error: "You do not have permission to access this Content. Please reach out to Administrator." |
| Action | Raised request with support |

### 5. Build Portal

| Field | Detail |
|-------|--------|
| Link | https://wwwin-ins-sw-web.cisco.com/node/branch/build |

### 6. Appstore

| Field | Detail |
|-------|--------|
| Link | https://appstore.cisco.com/ |

### 7. DeepSight

| Field | Detail |
|-------|--------|
| Link | https://deepsight.cisco.com/ |

---

## Section 2: Meeting Links

Two meetings documented with WebEx deep links:

1. **Build log analysis intro with Justin (04/08/2026)**
   - WebEx link: `webexteams://im?space=8fcc5f70-2dcc-11f1-a1fc-a98bb153865a&message=7726afb0-3453-11f1-bacb-858bcec24e03`

2. **Build log analysis with Divakar and Justin (04/09/2026)**
   - WebEx link: `webexteams://im?space=8fcc5f70-2dcc-11f1-a1fc-a98bb153865a&message=c45958f0-3494-11f1-a96b-8f3ce65ee974`

Both links point to the same WebEx space (space ID: 8fcc5f70-2dcc-11f1-a1fc) with different message anchors, suggesting Namita shared recordings or notes within that space.

---

## Section 3: Build Log Analysis Understanding After Calls with Justin

### Build Types and Branches

1. **Two build types:** Official nightly builds and user (PR) builds.
2. **Two branches:**
   - `nx_main` — built with Gmake (legacy, being phased out)
   - `nx_dev` — built with Bazel (current, focus of new development)
3. **Build systems:**
   - **Gmake:** Used for nx_main repo. Old repos built with Gmake. Cisco is moving away from Gmake to Bazel.
   - **Bazel:** Used for nx_dev repo. This is the future and the team's focus (per Decision #1 from Set 01).

### Build Infrastructure

4. **Build metadata** (build number, status, dates) stored in **MySQL database.** The build portal at https://wwwin-ins-sw-web.cisco.com/node/branch/build surfaces this data.

5. **Logs stored on NFS** accessible via ADS machines. **Exact NFS path: `/auto/ins-bld-tools/branches/nx_main/nexus/logs/`**

6. **Build portal data visible in screenshot:**

| Build No | Build Date | Expire By | LOC (Ins/Mod/Del) | Status/# Sanity | Comments |
|----------|-----------|-----------|-------------------|-----------------|----------|
| 10.7(0)IDV9(0.205) | 04/08/2026 10:40 | 04/23/2026 14:56 | 9770/0/2286 | Pass | Build successful (divvenka) |
| 10.7(0)IDV9(0.204) | 04/07/2026 19:32 | 04/27/2026 23:30 | 3109/0/1671 | Pass (42) | Codenet Label (psadhukh) |
| 10.7(0)IDV9(0.203) | 04/07/2026 11:07 | 04/22/2026 14:52 | 38860/0/11639 | Pass (2) | Build successful (divvenka) |
| 10.7(0)IDV9(0.202) | 04/06/2026 19:34 | 05/06/2026 23:16 | 33/0/36 | Pass (2) | QA Label (psadhukh) |
| 10.7(0)IDV9(0.201) | 04/06/2026 15:21 | — | 1906387/0/689105 | Fail | Build failed (psadhukh) |

**Observations from build portal data:**
- Builds are versioned as `10.7(0)IDV9(0.2xx)` — sequential numbering
- LOC changes vary wildly: from 33 insertions (0.202) to 1.9 million (0.201). The 1.9M insertion build failed.
- Sanity test counts shown in parentheses: some builds have 2 sanity tests, one has 42
- Build owners visible: `divvenka` (Divakar) and `psadhukh` (unknown, possibly Pramod Sadhukhan)
- Builds expire 2-4 weeks after creation
- The failed build (0.201) has no expiry date, suggesting failed builds may be retained differently

### Log Directory Structure (Terminal Screenshots)

7. **Left terminal** shows an `ls` of the NFS log directory for a specific build. Visible log file names (exhaustive list from screenshot):

**Build/compilation logs:**
- `all_image_compare.log`
- `build_log.html`
- `build_scope.log`
- `check_changes.log`
- `collect_commits_diffs.log`
- `create_flat_samefile.log`
- `create_latest_link.log`
- `create_latest_symlink.log`
- `create_mli_login_test_smu.log`
- `daily_build.log`
- `diff`
- `disk_usage.txt`
- `do_build_final.mfk`
- `email_body.txt`
- `env.log`
- `env.log.1`
- `env.log.dcnm`
- `error.log` / `error_list`
- `find_commits.log`
- `garbage_collection.log`
- `general.log`
- `git_clone.log`
- `git_top`
- `git_tags.log`
- `prune_build_mfk.log`
- `rsync_final.log`
- `sdk_mfk.log`
- `send_status_email.log`
- `slim_build.log`
- `source_checkout.log`
- `source_tag.log`
- `srg_version_change`
- `standalone_compiler_warnings_exec.txt`
- `standalone_compiler_warnings.html`
- `standalone_compiler_warnings.json`
- `standalone_compiler_warnings_ap.json`
- `wit_snapshot_creation.log`
- `cmts.html`
- `cmts_dir`
- `commits` directory
- `copy_out_workspace.log`
- `post_build_activities.log`

**Right terminal** shows the same directory with additional files visible:
- Multiple `error.log.images/final/*` files (organized by image type: nxos64, bazel, nxos64_s1_dbu, nxos64_mcs, etc.)
- `prune.error.log.images/final/*` files (pruned versions of error logs)
- `standalone_compiler_warnings.json` and `.ap.json` variants
- `child_readiness_sanity_test.log`
- `child_sanity_submission.log`
- `daily_build.log`
- `build_log.mnt`

**Key observations from log directory:**
- Logs are organized in a flat directory structure (not by stage or type)
- There are dozens of distinct log files per build (40+ visible)
- Error logs are further subdivided by image type (nxos64, bazel, etc.)
- Both human-readable (.html) and machine-parseable (.json) formats exist for compiler warnings
- Pruned versions of error logs exist alongside full versions
- The directory contains both logs and artifacts (commits dir, email body, disk usage)

### Justin's Existing Workflow

8. Justin's Python + LLM workflow (4 steps):
   1. Python script extracts errors from build logs
   2. Errors passed to LLM for analysis
   3. LLM suggests and applies code fixes automatically to a separate workspace
   4. Build verification step ensures fixes resolve the errors
   5. Potential to automate PR creation for verified fixes to official builds

### Log Retention Policy

9. **CI builds** run on pull requests with multiple checks including build and static analysis.
10. Jenkins triggers build jobs and generates logs stored on NFS and other storage.
11. **Failed CI build logs:** Retained for approximately 3 days.
12. **Official nightly build logs:** Retained for up to 5 years.
13. Log files are described as "huge size" (consistent with Set 01's 300K-500K lines estimate).

---

## Complete URL Inventory (All Cisco Internal Systems)

| # | System | URL | Purpose | Access Status (4/10) |
|---|--------|-----|---------|---------------------|
| 1 | ADS Reservation | https://adsrsvp.cisco.com/#/adsman | Temporary ADS machine requests | Access received |
| 2 | Managed Resources | https://managed.cisco.com/personal-resources | Permanent ADS machine deployment | Blocked: DCN Switching tenant not visible |
| 3 | REALM | https://realm.cisco.com/asset-search | Bundle access requests | CN-SJC-ND requested |
| 4 | User Groups | https://myid-groups.cisco.com/groups | Manual group membership management | Used by bundle owners to approve access |
| 5 | OneAccess | https://oneaccess.cisco.com | A2G_group request (GitHub) | Requested |
| 6 | NX GitHub | https://wwwin-github.cisco.com/DCN/tools | Tools repo with Justin's code | Pending A2G_group |
| 7 | AI Triage PR | https://wwwin-github.cisco.com/DCN/tools/pull/642 | Justin's AI triage tool PR | Pending access |
| 8 | Training (correct) | https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8 | NX GitHub training video | Permission denied |
| 9 | Build Portal | https://wwwin-ins-sw-web.cisco.com/node/branch/build | Build status, metadata, LOC | Accessible (screenshot taken) |
| 10 | Appstore | https://appstore.cisco.com/ | Cisco internal app store | Listed, status unknown |
| 11 | DeepSight | https://deepsight.cisco.com/ | DeepSight platform | Listed, status unknown |

---

## New Information Not Previously Captured

1. **Exact NFS path** for build logs: `/auto/ins-bld-tools/branches/nx_main/nexus/logs/`
2. **Permanent ADS machine specs:** 8CPU, 32GB RAM, 100GB storage, RHEL8, San Jose location
3. **Build versioning scheme:** `10.7(0)IDV9(0.2xx)` format
4. **Build owners visible:** `divvenka` (Divakar) and `psadhukh` (new name, possibly Pramod Sadhukhan)
5. **LOC scale:** Builds range from 33 to 1.9M lines of code changes
6. **40+ distinct log files per build** in flat directory structure
7. **Error logs subdivided by image type:** nxos64, bazel, nxos64_s1_dbu, nxos64_mcs, etc.
8. **Both HTML and JSON compiler warnings** exist (machine-parseable formats available)
9. **REALM bundle approval requires manual action** from 33+ bundle owners via myid-groups.cisco.com
10. **Official nightly build log retention:** Up to 5 years (not just "retained for years")
11. **Build portal URL** and **Appstore URL** not previously documented
12. **WebEx deep links** to both Justin meeting recordings preserved

---

## Significance for Task 3 Architecture

This document confirms several architecture-relevant details:

1. **Log parsing has structured targets.** The existence of `.json` and `.html` compiler warning files means some log data is already machine-parseable. Colin's Tier 1 (regex/rule-based) approach can leverage these structured formats directly, reducing the scope of raw log parsing needed.

2. **Error logs are already categorized by image type.** The `error.log.images/final/*` file naming convention suggests the build system already segments errors by build target. This is a natural decomposition boundary for the analysis pipeline.

3. **The flat directory structure simplifies file discovery.** All logs for a build are in one directory, not nested. A scraper can enumerate a single directory to find all relevant files.

4. **Build portal metadata is accessible.** The build portal provides build numbers, dates, LOC changes, sanity results, and pass/fail status. This metadata can be correlated with log file contents to build a structured dataset of build outcomes paired with error patterns.

5. **Log retention asymmetry matters.** Failed CI logs vanish after 3 days but nightly build logs persist for 5 years. Any automated analysis system must either process CI failure logs in near-real-time or archive them independently. The nightly build logs provide a rich historical dataset for training and pattern extraction.
