# Kickoff Context — 2026-04-21

**Purpose of this file:** Capture context that is emerging during the kickoff conversation with Colin on 2026-04-21 (the day after the handoff package was produced). This context refines or supplements the handoff docs. Nothing here overwrites the handoff docs silently; items that would change a handoff doc are flagged with "PENDING DOC UPDATE" until Colin confirms.

---

## 1. Branch Constraint (CRITICAL — confirmed by Colin 2026-04-21)

Colin has created a branch named `agentic-ui-conversion` in every repository in scope. **All work happens on this branch. All pushes go only to this branch.** No other branch may be written to.

### Affected repositories (per Confluence `context.txt`)

**EPNM side (legacy, github3.cisco.com/EPNM/* and one ROBOT/* for EPNM-era fault):**
- `EPNM/pf-framework`
- `EPNM/wireless`
- `EPNM/assembly`
- `EPNM/inventory`
- `EPNM/ce-content-device-packs`
- `EPNM/chassisview`
- `EPNM/fault`
- `ROBOT/ems-assurance` (EPNM-era branch `cepnm8.1PI`)

**EMS side (github3.cisco.com/ROBOT/*):**
- `ROBOT/infra-ui`
- `ROBOT/common-ui`
- `ROBOT/unified-ems-ui` (primary working repo)
- `ROBOT/cw-inventory`
- `ROBOT/cw-inventory-collector`
- `ROBOT/cw-epnm-fault`
- `ROBOT/ems-assurance` (EMS-era branch `develop`)
- `EPNM/inventory` (cross-era reuse)
- `EPNM/fault` (cross-era reuse, branch `develop`)

**This supersedes any earlier assumption about working branches.** The handoff docs (08_repositories_access_and_compliance.md, 09_work_items.md) should be updated to reflect this constraint explicitly — **PENDING DOC UPDATE** pending Colin confirmation on where to place the update.

---

## 2. POC Scope — CONFIRMED 2026-04-21

Resolved by Colin: the two-screen POC scope is **Inventory + Fault Management**. Earlier mention of "device management" was a speech slip; "fault management" was intended. This matches the handoff docs (`03_objectives_and_scope.md`) and the Confluence extract. No doc updates required.

---

## 3. CLAUDE.md Rules — PENDING INPUT FROM COLIN

Colin indicated he may share CLAUDE.md directly with the execution session, or may provide a more generalized version. Rules he wants carried through from CLAUDE.md should be added to this context file (or folded into `11_ways_of_working.md`) once he provides them.

**Action:** Await CLAUDE.md content or guidance from Colin.

---

## 4. Saurav Transcript — RECEIVED (2026-04-21)

Formatted version at `cisco/epnm_ems/poc/transcripts/saurav-colin_4-21-2026_formatted.txt`. Raw version removed per Colin. 594 lines, ~40 KB. Processed through `.claude/skills/singularity/scripts/format_transcript.py`.

Content not yet absorbed into the handoff package. Decision on whether to process as Set 09 in the blockchain research library is Colin's.

**Action:** Session 2 to read and surface anything scope-material.

---

## 5. Repository Analysis Bundle — RECEIVED (2026-04-21)

Lives at `cisco/epnm_ems/poc/REPO/`. Produced by the execution session on Computer 1 from the actual cloned repositories. Includes:

- `README.md` at the root of the bundle.
- `EPNM/` — family-level summary + per-repo tree reports (7 reports, ranging ~190 KB to ~2 MB). Repos covered: assembly, ce-content-device-packs, chassisview, fault, inventory, pf-framework, wireless.
- `EMS-CNC/` — family-level summary + per-repo tree reports (7 reports, ranging ~13 KB to ~587 KB). Repos covered: common-ui, cw-epnm-fault, cw-inventory, cw-inventory-collector, ems-assurance, infra-ui, unified-ems-ui.
- `EPNM-EMS-CNC/` — combined cross-family consolidated report and summary JSON.
- `repo-inventory/` — repository inventory in markdown and JSON.

Combined tree-report content across both families is roughly 4+ MB of markdown. Too much for a single-thread read. Agent swarm is the right pattern.

Detailed reading plan and per-agent assignments are in the `poc/REPO/` section of `cisco/epnm_ems/poc/session2_kickoff_2026-04-21.md`.

**Action:** Session 2 absorbs via agent swarm per that plan.

---

## 6. Folder Rename Observation (informational)

Colin mentioned the handoff folder has been renamed to `init_handoff` in the execution session's environment. In this working directory it remains `handoff/`. No action needed on this side; the handoff docs themselves do not reference their own folder name.

---

## 6a. Operating Model — CONFIRMED 2026-04-21

Resolved by Colin during Session 2 kickoff:

- **The "execution session" is Colin's own Claude instance running on his Cisco-issued Mac.** Not a separate engineer's machine. Colin does the code on the Cisco Mac, Session 2 does orchestration and synthesis on the BayOne machine.
- **Tools are not Claude-specific.** Colin and Saurav both have access to Claude and Codex. All kickoff and handoff materials are written with "Claude" as the default term; Colin will find-replace to Codex later if and when that becomes more convenient. Instructions should remain tool-agnostic and not encode assumptions tied to one specific model or CLI.
- **Saurav's role.** Saurav is a BayOne teammate on an adjacent Cisco engagement (NX-OS CI/CD). He appears in the 2026-04-21 transcript as a context-sharing partner, not as the EPNM-EMS execution session. Any future EPNM-EMS kickoff message is for Colin's own Cisco-side Claude instance.

This supersedes the ambiguity originally flagged in the Saurav transcript extract section 1. That section has been updated in place.

---

## 7. Java Multi-Repo Context (to be developed for Colin)

Colin (self-described Django-brained) flagged that the multi-repo shape of EPNM is confusing and slows his own orientation. Five or six EPNM repos, plus the EMS / CNC family, with no obvious entry point equivalent to a Django `manage.py runserver`.

A short primer has been written at `_scratch_repo/java_multi_repo_primer.md` framed in Django analogies: what a JAR and a WAR are, how Maven multi-module builds work, how the EPNM repos likely compose into a deployable, why Spring Boot is not the same shape as a Java monolith, and what `cw-inventory`'s Docker and LocalProfileConfig probably mean for local-run feasibility.

**Action:** Session 2 maintains that primer. The execution session uses it as context but is the authority on how the actual Cisco codebase builds.

---

## 8. Scope Discipline — What Is "Actually in POC Scope"

Colin's explicit guidance: the ten tree reports Session 2 is absorbing surface a lot of code that **may or may not be part of POC scope**. Session 2's extractions describe what exists, not what is needed. The execution session (on the Cisco Mac) is the authority on what actually needs to be read or touched for the two POC screens. Session 2 surfaces candidate paths; the execution session filters.

**Do not treat any agent-extracted file path as in-scope until the execution session confirms.** Session 2's role is to make the filtering job cheaper, not to do the filtering.

---

## 9. Open Question 3.8 — Local Runnability of EMS / CNC (NEW, 2026-04-21)

Surfaced in the Saurav-Colin transcript: "is there a way to run this local? Because I asked that question and no one really had an answer."

Partial evidence from the tree-report swarm: both `cw-inventory` and `cw-inventory-collector` include a `LocalProfileConfig` class and a Dockerfile. That suggests a local profile was intended. It does not confirm a running system can be stood up end-to-end without an ADS (Cisco internal) deployment environment.

**Proposed specific investigation instructions for the execution session on Colin's Cisco Mac:**

1. `cw-inventory` and `cw-inventory-collector`:
   - Read the Dockerfile and any `docker-compose*.yml` or `local-dev*.sh` scripts at each repo root.
   - Identify what external dependencies are required (PostgreSQL instance, Kafka, gRPC counterparts, config server, Eureka / service registry).
   - Check whether the `LocalProfileConfig` class pulls from a local config file and what that file expects.
   - Try to reach the Spring Boot actuator health endpoint after a local build; report what the build and start commands look like.

2. `unified-ems-ui` (Angular library):
   - Confirm no standalone run — it's a library. A consuming shell (`infra-ui`) must host it.

3. `infra-ui`:
   - Read `angular.json`, `package.json` scripts, and any `.env*` files at repo root.
   - Identify whether `ng serve` or an equivalent works standalone or requires backend endpoints.
   - Check whether any config file points at ADS-only URLs by default.

4. Fault backends (`cw-epnm-fault`, `ems-assurance`):
   - Same as item 1.

5. EPNM side:
   - Most likely not runnable locally without an EPNM lab — they're expecting a full Oracle + Java monolith stack. Confirm by reading a top-level README or `build.xml` / `pom.xml` setup docs.

6. Deliverable: a short `local_runnability_report.md` in `poc/` summarizing for each repo whether local-run is feasible, what's missing, and whether a VM is truly required.

**Fallback if local-run proves impractical:** Colin's plan articulated in the Saurav transcript — start with mocked data (screenshot or static JSON) wired to the classic UI, verify the UI behaves, then wire the live backend once VM access is in hand.

This question rolls into `10_open_questions_and_risks.md` on the next handoff update pass as item 3.8.

---

## 10. Tree-Report Swarm — Running Findings (2026-04-21)

Living capture of scope-material findings from the 10-agent tree-report absorption pass. Agents write extractions into `_scratch_repo/agent_NN_*.md`. This section is the high-signal summary; detail is in the agent extractions and in `_scratch_repo/_findings_log_2026-04-21.md`.

Status and findings are maintained in the findings log. See that file for the live state.


---

## 7. Kickoff Message — Still in Draft

Colin asked what to tell the other session to kick them off. Draft is pending resolution of sections 2 through 5 above. Once the open items are closed, a concise kickoff message will be written here.

**Action:** Draft the kickoff message once open items resolve.

---

## Open Items Summary

| # | Item | Status |
|---|---|---|
| 1 | Branch constraint captured | Confirmed |
| 2 | POC scope (Inventory + Fault Management) | Confirmed |
| 3 | CLAUDE.md content or generalized rules | Awaiting Colin |
| 4 | Saurav transcript | Received (formatted only) at `poc/transcripts/`; pending Session 2 read |
| 5 | Repository analysis bundle | Received at `poc/REPO/`; pending Session 2 agent-swarm absorption |
| 6 | Kickoff message draft for execution session | Blocked on #3 and on item 5 being absorbed |
