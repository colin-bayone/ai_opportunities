# Session 2 Kickoff — Orchestration Handoff for a Fresh Claude Session

**Date prepared:** 2026-04-21
**Prepared by:** The prior Claude session (Session 1), handing off because the kickoff phase for the EPNM-to-EMS POC is too large to finish in a single session context.
**For:** A fresh Claude session (Session 2) taking over Session 1's role.

---

## Read This First

You are Session 2. You are taking over from Session 1, which prepared the initial handoff package for an execution session (on Computer 1) that will perform the actual POC code work. **You are not the execution session.** Your job is orchestration, synthesis, and continuing support for Colin as the POC kicks off.

Three Claude sessions exist in this engagement's flow:

1. **Session 1 (previous, now concluded).** Produced the initial handoff package (12 numbered documents) that Colin hand-delivered to the execution session on his other machine. Session 1 also produced scratch extractions and a proposed plan for the handoff work. Session 1 is the session that wrote this document and then handed off to you.
2. **Execution session (Computer 1).** Has unadulterated access to the EPNM and EMS/CNC repositories. Will do the actual Angular conversion work. Already received the 12-document handoff package (now renamed `init_handoff/` in that environment). Can come back to you with questions.
3. **Session 2 (you, starting now).** Continues Session 1's orchestration and support role. You work from this machine, not Computer 1. You will read materials Colin shares, draft kickoff messages, integrate new context into the handoff, and answer questions relayed from the execution session.

Colin sits across all three, shuttling context. Your partner on the "thinking" side is Colin. The execution session is the one doing the code.

---

## What the Engagement Is (One Paragraph)

Cisco has two products in scope: EPNM (Evolved Programmable Network Manager — legacy, Dojo 1.x frontend, Java + Oracle backend, ~10 years old) and EMS (Element Management System, part of Cisco Crosswork Network Controller — Angular 21, Spring Boot + Go, PostgreSQL). Customers are trained on EPNM's UI and resist the new EMS UX. BayOne (Colin Moore, Director of AI) is building a POC for Cisco: add a "classic view" toggle to two EMS screens (Inventory and Fault Management) so users can flip between the EPNM-style UX and the new EMS UX. Both views call the same EMS backend unchanged. Default on login is classic. POC is Colin solo; full engagement scales after POC. All work on Cisco hardware with Cisco-issued Claude Code and local LangGraph as the only AI tools.

The full background is in the handoff package. Read it before doing anything else.

---

## Your Very First Task — Verify You Can Write Files

Before you do any other work, **spawn one single general-purpose agent** with read and write permissions enabled. Give it a tiny assignment — read one small file in this repo and write a confirmation artifact to a specific path. Check that the file actually exists on disk and has the content the agent reported writing.

If the agent cannot write, **stop immediately and flag it to Colin.** Colin's guidance is explicit: "if they are unable to, they should know to flag it to me immediately." There is no workaround. Do not attempt to proceed without write-capable agents.

If the pilot agent writes successfully, you are cleared to scale. The scaling pattern is: send multiple parallel general-purpose agents in a single message block (multiple tool calls in one response) so they run concurrently. Do not spawn them sequentially; that defeats the parallelism.

Why this matters: some of the materials Colin will share are large (he mentioned tree diagrams in the neighborhood of 10,000 lines of markdown because of repository scale). Agents carry the reading load so the main thread stays clear. If agents cannot write, the whole pattern is dead and we lose the throughput that makes the kickoff phase tractable.

---

## Where Everything Lives

The engagement directory is `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/`. Inside it:

| Path | Contents | How to use |
|---|---|---|
| `research/` | 57-file immutable blockchain-style research library, dated 2026-02-09 through 2026-04-07. Methodology doc, meeting deep-dives, summaries, bridge documents. | Read as reference. Never edit. Start with `research/00_methodology_2026-02-09.md` and the summary files in order. |
| `source/` | Raw transcripts (speech-to-text), formatted transcripts, attendee screenshots for the 2026-04-06 walkthrough. | Read only when you need ground truth the research library may have compressed. |
| `planning/` | Two files: `session_plan_2026-04-07.md` and `session_handoff_2026-04-07.md` from the prior reorganization session. | Informational. These predate Session 1's work. |
| `pricing/` | Internal BayOne pricing artifacts. | **Do not use.** Commercial content is stripped from all handoff output. |
| `deliverables/` | Earlier BayOne proposal and pricing HTML artifacts. | Informational only for Session 2. Not part of technical handoff. |
| `archive/` | Pre-reorganization content. | **Do not read.** Deliberately excluded (Colin confirmed). |
| `org_chart.md` | Living org chart, last updated 2026-04-06. | Reference for people. Also restated in handoff doc 07. |
| `poc/` | POC working folder. Session 1's output lives here. | Your working area. |
| `poc/handoff/` | The 12-document handoff package. On Computer 1 this folder is renamed `init_handoff/`. | **Read every file here as part of your orientation.** |
| `poc/handoff/_scratch/` | 8 agent extraction files (raw material Session 1 used to synthesize the 12 handoff docs). | Reference when you need detail Session 1 compressed. |
| `poc/handoff/_proposed_plan_2026-04-20.md` | Session 1's approved plan for assembling the handoff. | Informational. |
| `poc/handoff/_tree_snapshot_2026-04-20.md` | Tree of the engagement folder excluding archive. | Informational. |
| `poc/handoff/_kickoff_context_2026-04-21.md` | Running context file for kickoff. **Read this** to see what is open and what is confirmed. | Living document. Update as Colin provides more. |
| `poc/context.txt` | Confluence extract from Cisco — repository URLs, scope modules, EPNM wiki link. | Authoritative for repo URLs and branches. |
| `poc/transcripts/` | Transcripts Colin shares during the kickoff phase. As of 2026-04-21: `saurav-colin_4-21-2026_formatted.txt` (raw version removed; formatted only). | Read. Decision on whether to process into the research library as a new Set 09 is Colin's. |
| `poc/REPO/` | **Repository analysis bundle produced by the execution session on Computer 1.** Tree reports for every in-scope repo (EPNM side and EMS-CNC side), consolidated portfolio report, machine-readable summaries, and a repository inventory. **Some tree reports are very large** (the EPNM `fault_tree_report.md` is roughly 918 KB). See the dedicated section below. | Critical. This is the concrete picture of what is actually in each repository. Must be fully understood. Use parallel agents. |

---

## The `poc/REPO/` Folder — Repository Analysis Bundle (critical)

The execution session on Computer 1 ran a repository analysis against every in-scope repo and produced this bundle. It is the concrete picture of what is actually in the code. Session 1 (the session that wrote this kickoff document) did **not** have access to the repositories and therefore could not produce anything like this. You, Session 2, get to start with it. Take the time to understand it thoroughly.

### Structure

```
poc/REPO/
├── README.md                              (start here — 72 lines, short)
├── EPNM/
│   ├── consolidated_report.md             (EPNM family-level summary)
│   ├── summary.json                       (machine-readable EPNM summary)
│   └── tree-reports/                      (one tree report per EPNM repo)
│       ├── assembly_tree_report.md                 (~190 KB — inventory UI + faults UI, POC-critical)
│       ├── ce-content-device-packs_tree_report.md  (~594 KB)
│       ├── chassisview_tree_report.md              (~255 KB — chassis UI component)
│       ├── consolidated_report(1).md               (EPNM-side consolidated, duplicate-ish)
│       ├── fault_tree_report.md                    (~918 KB — LARGEST — fault backend + frontend)
│       ├── inventory_tree_report.md                (~316 KB — inventory backend)
│       ├── pf-framework_tree_report.md             (~777 KB — Prime framework, Dojo core)
│       └── wireless_tree_report.md                 (~1,995 KB — note: LARGER than fault)
├── EMS-CNC/
│   ├── consolidated_report.md             (EMS-CNC family-level summary)
│   ├── summary.json                       (machine-readable EMS-CNC summary)
│   └── tree-reports/                      (one tree report per EMS-CNC repo)
│       ├── common-ui_tree_report.md                (~153 KB — shared components library)
│       ├── cw-epnm-fault_tree_report.md            (~587 KB — fault backend on EMS side)
│       ├── cw-inventory_tree_report.md             (~41 KB — inventory backend)
│       ├── cw-inventory-collector_tree_report.md   (~13 KB — inventory collection service)
│       ├── ems-assurance_tree_report.md            (~540 KB — assurance / fault backend)
│       ├── infra-ui_tree_report.md                 (~324 KB — shell app)
│       └── unified-ems-ui_tree_report.md           (~98 KB — PRIMARY working repo for classic view)
├── EPNM-EMS-CNC/
│   ├── consolidated_report.md             (combined portfolio report, cross-family)
│   └── summary.json                       (combined machine-readable summary)
└── repo-inventory/
    ├── repository_inventory.md            (human-readable inventory + organization plan)
    └── repository_inventory.json          (machine-readable)
```

### Reading order

1. `README.md` at the root of `REPO/`. Short. Explains the bundle.
2. `repo-inventory/repository_inventory.md`. Short. Gives the repo organization plan.
3. `EPNM-EMS-CNC/consolidated_report.md`. The combined portfolio view. Best starting point for orientation.
4. `EPNM/consolidated_report.md` and `EMS-CNC/consolidated_report.md`. Family-level summaries.
5. Then the per-repo tree reports, starting with the POC-critical ones.

### POC-critical tree reports (prioritize these)

Inventory + Fault Management is the scope. Focus on tree reports for the repos most directly relevant:

**EPNM side (the legacy code being visually reproduced):**
- `EPNM/tree-reports/assembly_tree_report.md` — contains the inventory UI and fault management UI.
- `EPNM/tree-reports/chassisview_tree_report.md` — the chassis view component used on Device Details.
- `EPNM/tree-reports/inventory_tree_report.md` — inventory backend.
- `EPNM/tree-reports/fault_tree_report.md` — fault backend + frontend. Very large (~918 KB).
- `EPNM/tree-reports/pf-framework_tree_report.md` — Dojo-based core framework that everything EPNM sits on.

**EMS-CNC side (the Angular shell + where the classic view code will live):**
- `EMS-CNC/tree-reports/unified-ems-ui_tree_report.md` — primary working repo.
- `EMS-CNC/tree-reports/infra-ui_tree_report.md` — shell app the toggle fits into.
- `EMS-CNC/tree-reports/common-ui_tree_report.md` — shared component library; classic view should reuse where themable.
- `EMS-CNC/tree-reports/cw-inventory_tree_report.md` and `cw-inventory-collector_tree_report.md` — inventory backend on EMS side.
- `EMS-CNC/tree-reports/cw-epnm-fault_tree_report.md` and `ems-assurance_tree_report.md` — fault backend on EMS side.

Lower priority for POC:
- `EPNM/tree-reports/wireless_tree_report.md` (~2 MB) — wireless framework; may or may not intersect with POC scope.
- `EPNM/tree-reports/ce-content-device-packs_tree_report.md` (~594 KB) — device packs.

### How to process

Do not read these files serially in the main thread. The combined tree reports alone are more than 4 MB of markdown. That is enough to burn main-thread context completely if mis-handled.

**Use parallel general-purpose agents with read and write permissions.** Pilot one agent first (verify it wrote to the expected path on disk). Then scale.

Suggested agent assignments for the POC-critical reads (each agent reads one tree report and writes a structured extraction to a scratch folder like `poc/handoff/_scratch_repo/agent_NN_<repo>.md`):

1. EPNM `assembly` tree report (inventory + faults UI).
2. EPNM `chassisview` tree report.
3. EPNM `inventory` tree report.
4. EPNM `fault` tree report (largest; the agent needs a focused instruction set).
5. EPNM `pf-framework` tree report.
6. EMS `unified-ems-ui` tree report.
7. EMS `infra-ui` tree report.
8. EMS `common-ui` tree report.
9. EMS `cw-inventory` + `cw-inventory-collector` (small enough to combine).
10. EMS `cw-epnm-fault` + `ems-assurance` (fault backend pair).

Each agent should be instructed to:

- Read the assigned tree report in full.
- Extract file and directory paths relevant to the POC scope (Inventory and Fault Management screens).
- Identify key files by name where the name strongly suggests relevance (for example, `InventoryListView.js` in EPNM assembly, which the Confluence extract calls out explicitly).
- Note the repository's overall shape: what broad areas exist, roughly how large each area is.
- **Not** invent content about what files contain; names are evidence but not proof.
- Write a structured extraction.

After all agents complete, synthesize a cross-repo map of where the POC-relevant code lives and where the classic view will need to hook into. That synthesis becomes the basis for updating or extending the handoff package.

### Very important

Colin's standing warnings apply: no pattern matching heuristics when exploring. The tree reports themselves are fine to read (they are just markdown describing directory structures). Do not use grep-style shortcuts to "find interesting things" in them. Have agents read the whole file.

---

## What Has Been Done So Far

### Phase 1 (prior sessions, before Session 1): research library built

Between 2026-02-09 and 2026-04-07, the engagement's research library was built up through meetings with Guhan Selva, Selva Subramanian, and the Cisco engineering team, plus BayOne-internal pricing and strategy discussions. Set 08 (2026-04-07) was a technical research set documenting the EPNM legacy stack, the EMS modern stack, and Dojo-to-Angular conversion patterns.

The research library is organized blockchain-style: append-only, chronologically numbered sets, bridge documents (`NN-NN_changes_YYYY-MM-DD.md`) capturing what changed between sets. You do not edit these files. You may read them freely.

### Phase 2 (Session 1, 2026-04-20): 12-document handoff package built

Session 1 followed a five-phase process (defined in `poc/handoff/_proposed_plan_2026-04-20.md` and approved by Colin before execution):

- **Phase A.** Read 19 anchor files chronologically to absorb the engagement arc.
- **Phase B.** Spawned one pilot agent to verify write permission on a specific path.
- **Phase C.** Spawned seven parallel general-purpose agents, each with a specific extraction scope, each writing to `poc/handoff/_scratch/agent_NN_*.md`.
- **Phase D.** Synthesized 12 numbered handoff documents from the scratch extractions plus Session 1's own narrative absorption.
- **Phase E.** Verified traceability, presented to Colin. Scratch preserved per Colin's direction.

Constraints Session 1 worked under (confirmed with Colin before Phase A):

- POC scope is two screens only (Inventory + Fault Management).
- All commercial detail stripped — no pricing, margins, dollar figures, engagement-level timelines.
- No timelines, no hour estimates, no complexity or effort estimates anywhere.
- Action plan at transcript granularity only — no invented tickets, no prescribed decomposition.
- `archive/` folder excluded entirely.
- Handoff package location: `cisco/epnm_ems/poc/handoff/`.

### Phase 3 (kickoff, still in progress): emerging context

As of 2026-04-21, Colin is providing additional context to incorporate into the handoff flow:

- Confluence extract (`poc/context.txt`) — authoritative repository URLs. Confirmed.
- Branch constraint — `agentic-ui-conversion` branch in every in-scope repo is the only branch any work pushes to. Confirmed.
- POC scope confirmed: Inventory + Fault Management. Confirmed.
- CLAUDE.md rules — Colin intends to share content to fold into a more general-audience version. **Pending.**
- Saurav transcript (`poc/transcripts/saurav-colin_4-21-2026.txt`) — from a conversation on 2026-04-21. **Read this when Colin directs.**
- Repository tree diagrams — Colin is preparing these. Some are very large (around 10,000 lines of markdown). **Pending.**

Current state of open items is captured in `poc/handoff/_kickoff_context_2026-04-21.md`. Keep that file current as new items arrive and old ones resolve.

---

## What Is Remaining / What Is Next on the Agenda

In rough order of arrival:

1. **Read the 12 handoff documents yourself.** Do not delegate orientation; your credibility as Colin's partner depends on knowing what was said. Order: `00_index.md` → `01` through `11`. Use the reading order in `00_index.md`.

2. **Read the kickoff context file** (`_kickoff_context_2026-04-21.md`). Know what is confirmed and what is still open.

3. **Read the Confluence extract** (`poc/context.txt`). Short file. Gives the concrete repo URLs.

4. **Read the Saurav transcript** (`poc/transcripts/saurav-colin_4-21-2026.txt`) when Colin points you to it. Colin has not yet directed that the transcript be processed into the research library; check with him before treating it as a new Set 09.

5. **Absorb the tree diagrams Colin will share.** Expect several large files. Use parallel general-purpose agents to read them. Pilot one agent first to verify writes, then scale. Each agent's job: summarize one repository tree, focusing on the directories and file names relevant to Inventory + Fault Management (the POC scope). Ignore irrelevant branches of the tree. Agents write structured extractions to a scratch folder (suggest `poc/kickoff_scratch/` or similar — Colin may direct a different location; ask if unsure).

6. **Absorb CLAUDE.md content** when Colin shares it. Generalize appropriately for an external handoff audience. Fold key rules into `11_ways_of_working.md` in the handoff package (or into a separate doc, depending on Colin's preference — ask).

7. **Draft the kickoff message** for the execution session on Computer 1. This is a Colin-facing deliverable: it is what Colin copies and sends to the execution session to get them started. Content should at minimum include:
   - What to read first (pointing to `init_handoff/00_index.md` and the reading order).
   - The branch constraint (`agentic-ui-conversion`, only branch writable).
   - The confirmed two-screen POC scope.
   - The AI compliance constraints (only approved tools).
   - The agent protocol (pilot first, then scale).
   - Pointer to any CLAUDE.md-derived rules once shared.
   - How to come back with questions (via Colin, who routes to you).

8. **Respond to questions from the execution session** as Colin relays them. The execution session can come back. When they do, you work with what you have: research library, handoff docs, scratch extractions, Confluence context, transcripts, tree diagrams. You do not have access to the repositories directly. For any question where the answer is in the repositories, you help the execution session find it rather than answering it yourself.

9. **Maintain the handoff package as living.** If new material arrives that changes something in the 12 handoff docs, update the doc with a dated note appended, not a silent rewrite. The execution session may be reading a stale copy; note the update date so they see it has moved.

---

## How Session 1 Operated (and How You Should Too)

### Colin's standing behavioral rules

These live in Colin's auto-memory across sessions. Session 1 followed them throughout. They apply to you:

- **Never make unilateral decisions.** When instructions cannot be followed exactly, stop and ask Colin. Do not silently adjust. This one is load-bearing.
- **No pattern matching, regex, or grep during exploration** unless Colin explicitly allows it. Read files. Session 1 was warned about this three times early and the lesson stuck. When in doubt, write a small Python tree-mapping script instead of using `find` or shell glob patterns.
- **Planning goes in files.** Never put designs, plans, specs, or anything substantive in chat output. Write them to markdown files and reference the file in chat.
- **Discussion mode is one question at a time** with perspective and insights. Not batched questions. Not empty prompts.
- **Do not ask to break or pause or stop.** Keep processing until done.
- **No filler questions.** Don't pad with obvious exclusions or self-evident questions. Think, then propose.
- **Create things when obvious.** When the next step is obvious, just do it. Don't describe and wait for confirmation.
- **Use actual transcript details** in deliverables, not vague summaries.
- **Skills must be self-contained** — no cross-skill file dependencies.
- **Chronological processing only.** Never suggest skipping ahead; strict chronological order.
- **Always full Singularity structure** — never ask subset vs full; always create all folders when a Singularity engagement is being stood up.
- **Colin uses a dictation tool.** Treat garbled names or terms as transcription errors; match against known context before asking.
- **BayOne leadership:** Sripriya is CTO (Colin's boss). Rahul Sharma is former president. Rahul Bobbili is the current President at BayOne on this engagement (present in the 2026-04-06 walkthrough).
- **Viewport vs output size:** render at full size in a large viewport; embed at target print size via CSS. Never conflate.
- **Deliverable standards:** no em-dashes, no contrastive framing ("not X, but Y"), no contractions in formal text, no emojis, no direct quotes of individuals in client-facing deliverables. These are the `/big4` standards. Internal documents (like this one, like handoff scratch, like `_kickoff_context`) are looser but still avoid em-dashes and emojis.
- **AI practice attribution:** attribute Colin's methodology to the AI practice at BayOne specifically, not to BayOne generically.

### The agent protocol

When you need to process large files (tree diagrams, long transcripts, anything that would burn main-thread context):

1. Spawn **one** general-purpose agent with read and write permission. Give it a tiny verification task (read one small file, write a confirmation artifact).
2. Confirm the artifact exists on disk with the expected content. Do not just trust the agent's self-report.
3. If the pilot succeeds, spawn the rest of the agents **in parallel** — multiple tool calls in a single assistant message. Never sequentially.
4. Each agent writes its own scratch extraction to a pre-agreed path. You read the scratch files afterward and synthesize into final output.
5. If the pilot fails, **stop and flag to Colin.** Do not attempt workarounds.

Session 1 used this pattern for the Phase C swarm (7 parallel agents producing ~5,347 lines of extraction in roughly three minutes). It works. The only failure mode is not verifying the pilot write, or skipping the pilot.

### When to write to a file versus chat

Default to files. Specifically:
- Plans, proposals, specs, strategies → files.
- Multi-section synthesis → files.
- Long explanations the user might need to re-reference → files.
- Status updates and short confirmations → chat.
- Questions that do not require multi-paragraph framing → chat.

When in doubt, file.

### When you do not have the answer

If the research library, handoff docs, scratch extractions, transcripts, Confluence extract, and tree diagrams (when arrived) do not contain the answer, say so. Ask Colin. Do not guess. Do not extrapolate. Colin would rather answer a question than unwind a fabrication later.

---

## What the Execution Session Already Has

Colin delivered the following to the execution session on Computer 1. Assume they have these as of their kickoff:

- The 12-document handoff package, renamed `init_handoff/` on that machine.
- The `extract_pdf.py` script (which is separate tooling, not strictly related to the POC but available to them).

Colin has not yet delivered the project files themselves. The execution session has repository access but may not yet have the full kickoff message with constraints and next-actions. That is the deliverable you help produce.

---

## Pending Items Summary (as of 2026-04-21 evening)

| # | Item | Status |
|---|---|---|
| 1 | Branch constraint (`agentic-ui-conversion` in every repo; only branch writable) | Confirmed. Fold into kickoff message and ultimately into handoff doc 08. |
| 2 | POC scope: Inventory + Fault Management | Confirmed. No handoff doc update needed. |
| 3 | Confluence extract `context.txt` | Received. Contains authoritative repo URLs. |
| 4 | Saurav transcript | **Received. Formatted version only at `poc/transcripts/saurav-colin_4-21-2026_formatted.txt`.** Raw deleted. Read it. Decision on Set 09 treatment is Colin's. |
| 5 | Repository analysis bundle (`poc/REPO/`) | **Received.** Run agent swarm to absorb per the instructions above. |
| 6 | CLAUDE.md-derived rules | Pending. Generalize and fold into handoff once received. |
| 7 | Kickoff message for execution session | Pending. Blocked on item 6 and on absorbing the REPO bundle. |

---

## Useful Things to Keep in Mind

- **The execution session is the one doing the code work.** You are not. Do not propose implementation details. Do not try to architect the classic view yourself. Your job is orchestration and synthesis of context.
- **The research library is immutable.** Never edit anything in `cisco/epnm_ems/research/`. If new source material arrives (a new meeting, transcript, discussion), it becomes a new numbered set appended to the library. Colin runs that flow through the Singularity skill.
- **The handoff package is living but tracked.** If you update one of the 12 docs, add a dated note to its footer so readers can see when it changed. Do not silently overwrite.
- **The `_scratch/` folder is preserved for traceability.** Do not delete. Colin explicitly said keep it.
- **When in doubt, read the transcript.** The engagement's ground truth lives in the `_formatted` transcripts under `source/` and in the new transcripts Colin shares in `poc/transcripts/`. The research library is a distillation; transcripts are the source.

---

## Your First Response

When you start, acknowledge receipt of this document in a short chat message, confirm you understand your role (orchestration support, not execution), and then work through this order:

1. **Pilot-agent write verification.** One agent, small task, verify the file exists on disk. If it fails, stop and flag to Colin.
2. **Orientation reading (you do this yourself in the main thread).** The 12 handoff documents in `poc/handoff/` (renamed `init_handoff/` on Computer 1), in the reading order in `00_index.md`. Plus `_kickoff_context_2026-04-21.md`, `poc/context.txt`, and the Saurav transcript at `poc/transcripts/saurav-colin_4-21-2026_formatted.txt`. These are the narrative spine.
3. **REPO bundle orientation (you do this yourself).** The short files: `poc/REPO/README.md`, `poc/REPO/repo-inventory/repository_inventory.md`, `poc/REPO/EPNM-EMS-CNC/consolidated_report.md`, `poc/REPO/EPNM/consolidated_report.md`, `poc/REPO/EMS-CNC/consolidated_report.md`. Skim the machine-readable `summary.json` files if useful.
4. **REPO tree-report absorption (agent swarm).** Ten parallel general-purpose agents per the assignment table above. Each reads one tree report (or a small pair) and writes structured extractions to a scratch folder. Pilot one first; scale in a single message block.
5. **Synthesis.** Read the agent extractions, build a cross-repo map of POC-relevant code locations, and report back to Colin.
6. **Status check with Colin.** Short status: what you have absorbed, what is still pending (CLAUDE.md rules), what questions you have, what you propose as the next step.

Do not start drafting the kickoff message for the execution session until the REPO bundle is fully absorbed and CLAUDE.md rules are in hand. Both will materially shape what the kickoff message says.

---

## One Last Thing

The execution session on Computer 1 can come back to us with questions as they work. Those questions route through Colin, who relays them to you. You answer using the materials you have. If a question genuinely cannot be answered from the materials, tell Colin, and Colin can route to the Cisco tech leads through Selva. The chain is: execution session → Colin → you (and/or Selva via Colin) → back to execution session.

Treat the execution session as a colleague on the other end of a latency-heavy link. Give them complete answers when you can, clean escalations when you can't, and always err toward giving them more context than they strictly asked for, because the round-trip is expensive.

Good luck. Session 1 signing off.
