# 00 — Index

**This is the entry point for the handoff package.** Read this first. It points to everything else and tells you how to use the package.

---

## What This Package Is

A complete context handoff for a Claude session that will execute the POC for Cisco's EPNM-to-EMS classic view toggle engagement. The session picking this up has access to both the EPNM and EMS / CNC repositories. This package carries everything the session needs to walk into the work cold and be oriented.

The package was assembled on 2026-04-20 after a systematic read of all engagement material through 2026-04-07. Every claim in these documents traces to a research file in `cisco/epnm_ems/research/` or a source transcript in `cisco/epnm_ems/source/`. Nothing is invented.

---

## What The POC Is, in Three Sentences

1. Cisco has a legacy product (EPNM, Dojo-based UI) and a next-generation product (EMS, part of Cisco Crosswork Network Controller, Angular 21 UI). Customers are trained on the EPNM UX and resist the new EMS UX.
2. The POC builds a "classic view" toggle on two specific EMS screens (Inventory and Fault Management) so users can switch between the EPNM-style experience and the modern EMS experience. Both views use the same EMS backend unchanged.
3. BayOne (Colin Moore, Director of AI) is running the POC solo inside Cisco's infrastructure with Cisco-issued Claude Code and local LangGraph as the only AI tools permitted.

---

## Recommended Reading Order

Read in this order on first arrival. Each document builds on the previous ones. You can skip around later once oriented.

| Read order | Document | Why read it here |
|---|---|---|
| 1 | `01_project_overview.md` | The master anchor. What EPNM and EMS are. What the POC is. Why Cisco brought BayOne in. Who the stakeholders are at a glance. |
| 2 | `02_engagement_history.md` | How the scope arrived at what it is. Knowing the history prevents you from treating superseded framing as current. |
| 3 | `03_objectives_and_scope.md` | The exact POC scope. Two screens. What each screen covers. What is in, what is out, what defines done. |
| 4 | `04_strategic_approach.md` | The approach Cisco has endorsed. Fidelity over novelty. Exponential-decay framing. Agent-driven discovery. Four-agent architecture. |
| 5 | `05_technical_landscape.md` | Both stacks (EPNM, EMS) in depth. Repository inventory. The 80 percent backend coverage story. What the 2026-04-06 walkthrough demonstrated. |
| 6 | `06_conversion_patterns_reference.md` | Working-desk technical reference. Dojo-to-Angular widget mapping. Theme toggle architecture. Folder structure. Per-screen migration checklist. |
| 7 | `07_stakeholders_and_organization.md` | Who everyone is, how they interact, where decisions come from, name resolutions for the speech-to-text-garbled transcripts. |
| 8 | `08_repositories_access_and_compliance.md` | What repositories exist, how access is gated, the AI compliance rules that cannot be crossed. |
| 9 | `09_work_items.md` | The backlog at transcript granularity. Work items grouped by A (access), B (deep dive), C (Inventory), D (Fault Management), E (gaps), F (testing), G (closeout). |
| 10 | `10_open_questions_and_risks.md` | The living backlog of unresolved items, plus the risks the engagement has surfaced. Revisit at key decision points. |
| 11 | `11_ways_of_working.md` | How the engagement runs day to day. Escalation patterns. Decision authority. Communication rhythm. What to stop and ask about. |

---

## What Each Document Contains

### 01 — Project Overview
Anchor explanation of the engagement. Covers what EPNM is, what EMS / CNC is, why customers are asking for the classic view, the four-phase lifecycle Cisco is executing, what the POC actually is (UX overlay not conversion), what the two screens are at a glance, why Cisco brought BayOne in, and who the stakeholders are. End with three things the execution session should take from the document.

### 02 — Engagement History
Chronological narrative from the first discovery meeting on 2026-02-09 through the technical walkthrough on 2026-04-06 and the research set on 2026-04-07. Includes the major scope reframe on 2026-03-25 (full-stack conversion to classic view toggle). Commercial events deliberately excluded.

### 03 — Objectives and Scope
The exact POC scope at the level the transcripts established. The two screens (Inventory and Fault Management) broken down by sub-surface. Toggle behavior. Backend constraints. What defines done. What is explicitly NOT in POC scope. Open items the execution session will need to resolve or raise.

### 04 — Strategic Approach
The conversion approach as articulated across the meetings. Visual, interaction, and functional fidelity as the target. Exponential-decay / front-loading principle. Venn diagram feature mapping. Priority versus diversity ordering. Parallelizable workflow for post-POC scale. Automated QA scope boundary (POC versus full engagement). Four-agent architecture. Customer transparency principle. What not to change without going back to Colin.

### 05 — Technical Landscape
EPNM stack (Dojo 1.x, Java, Oracle, SNMP/CLI). EMS stack (Angular 21, Spring Boot + Go, PostgreSQL, Harbor/Magnetic, three-layer shell). Complete repository inventory for both products. Walkthrough findings. The 80 percent backend coverage story. Data flow comparison. What to read before writing code.

### 06 — Conversion Patterns Reference
Working-desk technical reference. Points back to the three Set 08 research files as the canonical source and restates the most immediately actionable patterns: widget mapping table (25 rows), AMD-to-ES6 translation, data binding and event handling translation, lifecycle hook mapping, state management (stores to services), theme toggle architecture (CSS custom properties + signal-based ThemeService), shared service plus display adapter pattern, shell app integration, proposed folder structure, per-screen migration checklist, named conversion risks.

### 07 — Stakeholders and Organization
Cisco leadership (Guhan, Venkat), Cisco operational counterparts (Selva, Praveen), Cisco tech leads (Akhil, Ramesh, Ramkrishna, Aadit, Jenis, Senthilkumar), Cisco people referenced but not present, BayOne team (Colin, Neha, Rahul Bobbili, Zahra), speech-to-text name resolution table, decision ownership map, time zones, communication channels and etiquette.

### 08 — Repositories, Access, and Compliance
EPNM and EMS repository inventories. Classic UI code location (undecided, Colin to propose). Access provisioning (AD groups, two VMs, Confluence, email pointers). AI compliance rules in full (10 rules). What the execution session must never do (7 lines). Escalation routing when blocked on access, libraries, backend changes, tooling, scope. The 12 Set 07 action items with pending status.

### 09 — Work Items
The backlog at transcript granularity. No invented tickets. Grouped by:
- A: Access and environment setup.
- B: Code deep dive and planning.
- C: Classic view construction — Inventory (POC Part 1).
- D: Classic view construction — Fault Management (POC Part 2).
- E: Backend gap handling.
- F: Verification and testing.
- G: Closeout.
- H: Not in POC scope (deferred).

### 10 — Open Questions and Risks
Sections 1 through 5: open questions organized by product/scope, architecture/technology, access/operations, testing, and AI compliance. Each question has a source citation and a how-to-resolve note. Section 6: risks the engagement has surfaced (12 risks) with mitigations. Section 7: how to use the list.

### 11 — Ways of Working
How the engagement runs day to day. The bandwidth reality. Escalation routing. Decision authority (execution session decides versus raises). Documentation and progress tracking (blockchain research library is immutable; POC artifacts go under `cisco/epnm_ems/poc/`). Communication rhythm. How progress gets reviewed. Patterns that define "good" execution. Customer transparency as a working rule. When to stop and ask.

---

## Quickest-Start Path (If You Are Picking This Up Cold)

Forty-five minutes of reading to be oriented:

1. `01_project_overview.md` — 10 minutes.
2. `03_objectives_and_scope.md` — 10 minutes. You now know what you are building.
3. `06_conversion_patterns_reference.md` Sections 1 through 6 and 9 — 15 minutes. You now know how to build it.
4. `08_repositories_access_and_compliance.md` Sections 3 and 4 — 5 minutes. You now know the rules.
5. `11_ways_of_working.md` Sections 3 and 4 — 5 minutes. You now know how to escalate.

Then go look at the actual repositories.

---

## Reference Paths

### The engagement folder
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/`

### This handoff package
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/handoff/`

### The research library (immutable, blockchain-style)
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/research/`

Contains 57 research documents across nine document sets, dated 2026-02-09 through 2026-04-07. Summary files and bridge (`NN-NN_changes`) documents give the narrative arc; deep-dive files give the specifics. The methodology document at the top of the folder (`00_methodology_2026-02-09.md`) explains the blockchain-style structure.

Start with `research/00_methodology_2026-02-09.md` if you want to understand how the research library works. Then read the summary files in order: `01_meeting_summary`, `01a_call_prep_summary`, `02_meeting_summary`, `03_meeting_summary`, `04_discussion_summary`, `05_internal_call_summary`, `05a_notes_summary`, `06_discussion_summary`, `07_meeting_summary`, `08_research_summary`.

The `08_research_*` files are the deepest technical references and are the immediate substrate for `06_conversion_patterns_reference.md` in this handoff.

### Source transcripts
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/source/`

Raw speech-to-text transcripts from the three Guhan/Selva meetings and the April 6 team walkthrough, plus Colin's internal BayOne call and Venkat positioning notes. The `_formatted` versions are the readable ones (produced by a transcript formatting script). Two PNG screenshots in the source folder are the authoritative attendee list for the April 6 walkthrough.

### The archive
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/archive/`

Contains earlier iterations of planning documents, POC proposal drafts, and reorganization-era materials. **Deliberately excluded from this handoff.** The archive is preserved for historical reference only; nothing in it is a current source. If you notice an inconsistency between the archive and the handoff, trust the handoff.

### The POC working folder (where new artifacts go)
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/`

This is where execution-session output accumulates (progress notes, decision logs, artifacts produced during the POC). The handoff package lives under `poc/handoff/`. Additional subfolders for specific categories of artifact are fine.

---

## A Final Note on Tone

This handoff was assembled for a session that may be picking up the work days or weeks after it was prepared. The language is deliberately specific rather than general. Where the transcripts gave an exact phrasing, the phrasing is preserved. Where an item is open, it is flagged as open rather than glossed. Where a risk is real, it is named.

If you encounter a situation where this handoff's framing feels inconsistent with current reality, trust what you see in the actual repositories and in Colin's current guidance over what this handoff says. The handoff is a strong starting snapshot, not a frozen specification. Update the relevant handoff document (with a dated note) when something material shifts.

The engagement has been characterized from the start by high trust, high clarity, and a preference for direct code exploration over meeting overhead. Continue that pattern. The Cisco team has been generous with context and patient with the setup time; the right way to reciprocate is to move work forward efficiently, surface questions cleanly, and keep the scope disciplined.
