# Chapter 3 — Handoff Package Assembly

## 1. The Phase in Context

The handoff-package assembly phase was the first fully recorded working phase of the engagement and the point at which the methodology documented in this set becomes directly observable. By the time this phase opened, discovery had concluded: two customer-side stakeholders had hosted three conversations, a team-wide architectural walkthrough had taken place, an internal strategic call had been held, the product-landscape research had been drafted, and the engagement had agreed on a small, two-screen proof-of-concept inside a much larger conversion program. What remained was a question of transfer: how to take the accumulated context — the transcripts, the topic maps, the people files, the bridge documents that recorded what shifted between meetings, the deep-dive research on the legacy and modern stacks, the internal positioning notes, the walkthrough artifacts — and package it so that an execution effort could begin the POC without having to re-derive any of that context from source.

The phase produced one artifact: a handoff package containing twelve purpose-built documents, plus the scratch extractions that supported them, plus a written plan and a tree snapshot that captured the state of the engagement folder at the moment the package was assembled. The package lives under a dedicated POC folder inside the engagement, deliberately separated from the sales-side archive. Every claim in the twelve documents traces to a specific research file or source transcript; nothing was invented.

The disciplines that produced that artifact — the ones this chapter documents — are the substance of the methodology. The gating on an approved plan, the four scoping questions resolved before execution, the non-objectives that prevented drift, the five-phase structure, the parallel-agent production pattern, the orchestrator-versus-worker delegation boundary, the synthesis practice that stayed with the orchestrator — each is covered in its own section below. Later chapters generalize some of these patterns (particularly the parallel-investigation pattern); this chapter documents the pattern as it was practiced here.

## 2. The Objective and the "Desert Island Supply Pack" Framing

The objective of the phase was a complete, self-contained context package sufficient to let a downstream execution effort begin POC work without having to reconstruct engagement context from source. The customer lead's framing during planning — a "desert island supply pack" — captured the standard precisely. The execution phase was assumed to open cold, with access to the two relevant product repositories and nothing else by way of engagement context. Whatever the execution phase needed to know about the problem, the scope, the technical landscape, the stakeholder map, the conversion patterns, the access and compliance rules, the open questions and risks, and the engagement's working conventions had to be in the package.

"Self-contained" meant a specific thing operationally. The package would be consumed without access to the research library it was synthesized from. A reader arriving at the package could optionally follow citations back to a research file, but should not need to do so to understand what the POC is, what the two screens are, what success means, how the conversion is approached, what the stacks look like, who the stakeholders are, what the repositories are, what the work ahead consists of, what remains unresolved, and how the engagement operates day to day. Each of the twelve documents was designed to answer those questions fully on its own, within its scope. The index document oriented new arrivals to the package and to the reading order that would get them oriented fastest.

The framing had one more operational consequence. Because the package was the sole point of context transfer, it could not leave material ambiguity unflagged. Where the transcripts left something undefined, the package named that thing as open rather than filling the gap with a plausible guess. The open-questions document was an explicit artifact of this discipline; the scope document, the work-items document, and the strategic-approach document also contain open-flagged items where the source material did not resolve them. The methodology treats an undefined item surfaced and labeled as open as categorically different from an undefined item papered over.

## 3. The Discipline of Writing the Plan to a File and Gating on Approval

No execution commenced until a plan was written down, reviewed, and explicitly approved. This was not a procedural formality. The authoring of the plan document itself was a methodology practice: the plan surfaced the scope, the phases, the delegation boundaries, the non-objectives, and the open questions that needed resolution before execution could begin, and it put all of that in a single markdown file the reviewer could interrogate.

The plan document named its own purpose at the top. It stated the objective in one paragraph, added a short scope-boundary clarification, and immediately listed the non-objectives — the exclusions that defined what the handoff would not do — before any phase detail. It specified guiding principles: chronological reading through the append-only research chain, no pattern matching or regex as exploration heuristics, parallel agents with write permissions rather than read-only explore agents, pilot-first spawning before any swarm, and a hard restraint against inventing structure the transcripts had not themselves established. It numbered the open questions that needed resolution before Phase A would begin, each one with a short rationale for why the answer materially changed what would be produced.

The gating was absolute. The phase did not drift into action while the plan was being drafted; planning output went into the file, not into the working stream. When the plan was complete, it was presented to the reviewer with an explicit approval gate: no Phase A reading until the plan was approved. The methodology treats silent drift from planning into execution as a specific failure mode, and the gate is the countermeasure.

The plan and the tree snapshot (a separate structural inventory of the engagement folder produced at the same moment) were written under the POC handoff folder itself, not into a transient scratch space. Both files were preserved through the end of the phase and remain in place as a permanent record of the state at which the handoff was assembled. A later reader can reconstruct what the engagement folder looked like at the moment of handoff and what the approved production plan was, without reasoning from the artifacts alone.

## 4. The Four Scoping Questions Resolved Before Execution

Before Phase A began, four scoping questions were surfaced and answered explicitly with the reviewer. Each answer was a specific scope-boundary commitment that shaped the rest of the work. They are named here because the methodology depends on this kind of front-loaded scope discipline — the shape of the package was determined by these four answers, and leaving any of them implicit would have produced a materially different artifact.

**Question one: granularity of the action plan.** Two shapes were possible. A ticket-sized work-item list would enumerate concrete execution units with dependencies between them. A workstream-sized list would name large tracks for the execution phase to further decompose. The initial lean was toward ticket-sized items. The reviewer overrode that lean toward a middle position: high-level work items at the granularity the transcripts themselves had established, no invented tickets, no prescribed methodologies, no fabricated decomposition. Where the meetings had drawn a line around "Inventory conversion" as a unit, the work-item list named Inventory conversion as a unit. Where the meetings had not decomposed a unit further, the work-item list did not invent the decomposition. The execution phase was expected to fill in execution detail from the repositories themselves, not inherit invented subdivisions.

**Question two: commercial content.** The research library contained pricing strategy, pricing decisions, pricing breakdowns, and engagement-level commitments. The execution phase, by contrast, was a technical execution effort that did not need commercial context to operate. Three options were considered: full inclusion, dollar-figure redaction while retaining engagement shape, and full strip. The answer was full strip. No pricing, no margins, no rate structures, no engagement-level timelines or deliverable commitments. The only commitment surface that entered the handoff was the POC's technical scope: two screens, what they are, what conversion fidelity they required. The larger engagement existed in the package as a single-line contextual note identifying the POC's containing context and nothing more.

**Question three: final output location.** The handoff could have lived alongside the rest of the engagement artifacts in the existing sales-side folder structure, or in a dedicated POC folder that separated execution-phase artifacts from sales-phase artifacts, or in a fully separate top-level folder. The answer was a dedicated POC folder inside the engagement. The rationale held that the execution effort was categorically different work from the sales and discovery work that preceded it, and giving the execution workstream its own subfolder kept the sales archive untouched while giving the execution phase a clear home. All forward-looking artifacts accumulated under the POC folder; discovery artifacts stayed where they were.

**Question four: archive-folder handling.** The engagement folder contained an archive subtree holding earlier iterations of proposals, prior planning drafts, and duplicated pre-reorganization material. The question was whether to read it. The answer was no. The archive was excluded entirely from every phase of the handoff assembly — not source transcripts inside it, not proposal drafts, not earlier planning iterations, nothing. The exclusion was a deliberate decision that the archive contained no unique ground truth not already represented in the active research chain. The archive was acknowledged in the final index as existing for historical reference and then left alone.

Each of these four answers acted as a lever that shaped downstream execution. The ticket-granularity answer shaped how the work-items document was written. The commercial-strip answer removed several agents from the production swarm and reframed others as scope-only extractions. The output-location answer placed the handoff under the POC folder and pulled the plan and tree snapshot into it. The archive-exclusion answer kept the reading surface bounded.

## 5. Non-Objectives

Alongside the scoping questions, the plan declared a set of explicit non-objectives: things the handoff would deliberately not do. These non-objectives were load-bearing. They prevented the package from drifting into material the execution phase would need to reject or work around.

- **No timelines.** No calendar dates for future work, no phases expressed as durations, no sequencing expressed in hours or days.
- **No effort estimates.** No hour counts, no complexity ratings, no sizing weights attached to work items.
- **No prescriptive implementation guidance.** No "how-to" detail beyond what the customer lead had personally stated in a meeting. The execution phase was expected to determine implementation approach from the repositories themselves, guided by the committed conversion approach but not constrained by an invented playbook.
- **No invented workstreams or decomposition.** If the transcripts had not named a module, track, or subtask, the handoff did not invent one. Where the engagement had discussed a conversion in generalities, the handoff preserved the generality rather than inventing a decomposition to make the generality feel actionable.
- **No pattern matching or regex as exploration heuristics.** Reading only. Structure could be listed by a directory traversal, but substance came from reading files cover to cover. Shortcut heuristics were forbidden throughout the phase.
- **No reading of excluded material.** The archive subtree was not read at any phase. If an item in the active research chain pointed back into the archive, the pointer was followed only to the active chain's restatement of the content.

The non-objectives were declared before any execution began and held through every subsequent phase of the work.

## 6. Phase A — Chronological Sequential Reading of Anchor Files

Phase A was the foundational read. It was the only step not delegated to parallel agents. The orchestrating thread read the engagement's anchor files itself, in strict chronological order, to absorb the full engagement arc before briefing any worker and before beginning any synthesis.

The reading order followed the engagement's own append-only structure. The research library was organized as an append-only chain of document sets — each set produced from a single source event (a meeting, a discussion, a research effort), numbered in order, with bridge documents (named by the sets they connect) between sets recording what shifted. For each set, a small number of anchor documents summarized the event and indexed its deep-dive documents: a topic map, a summary, and a people file. Reading the anchors in chronological order traced the engagement's narrative arc at a high level without yet descending into the content of any individual deep-dive.

The read therefore proceeded as follows. The methodology document that describes the research library's structure was read first. Then, for each of the engagement's document sets in order, the anchor files — topic map, summary, people file — were read, followed by the bridge document that recorded the shift into the next set. For the sets whose supplementary content was primarily commercial, the anchor was read only for scope-shaping content; pricing and commercial mechanics were stepped past without being absorbed. After the chronological chain, the latest planning documents and the engagement's living organizational chart were read last, to cap the read with the most recent state of the stakeholder landscape and the most recent planning guidance.

The read's purpose was not comprehension of every detail. Its purpose was to carry the full engagement arc — the sequence of scope shifts, the major reframes, the commitments made and unmade, the cast of stakeholders, the technical picture as it evolved across meetings — into the briefing of each parallel agent and into the synthesis work that would follow. The orchestrating thread did not return to the research library for chronology during synthesis; the chronology was already in head.

The discipline that held through Phase A was cover-to-cover reading of every anchor in sequence. No skimming, no pattern-driven sampling. Bridge documents were read with particular attention because they recorded deltas between sets — what had shifted, what had been confirmed, what had been invalidated. Missing a bridge document meant missing a reframe.

## 7. Phase B — The Pilot Agent and the Write-Verification Gate

Phase B spawned a single pilot agent. Its purpose was dual: produce one high-quality scratch extraction from the most technically dense set in the research library (the architectural walkthrough set from the large customer technical meeting), and verify that agents spawned in this environment could write files to the expected location under the intended permission model.

The pilot's assignment was narrow. It was given the four most critical deep-dive files from the architectural walkthrough set — the architecture and repositories document, the two product-walkthrough documents (one per POC screen), and the AI compliance and tooling document — and told to produce a structured extraction at a specific scratch path under the POC handoff folder, with named sections for architecture, repositories, the two walkthroughs, compliance rules, tooling constraints, verbatim scope commitments, and open items. It was told to report back with the path it had written and a short summary.

The verification step was done by checking the scratch file's existence and content on disk, not by trusting the agent's self-report. This is the methodology's position on write-capability verification: an agent that reports success has reported success; an agent whose output exists on disk at the expected path with the expected content has succeeded. Only the second confirms the pattern works. The pilot's scratch file was read on return, and its content was evaluated both for structural conformance (the named sections were present) and for substance (the extraction was not a self-congratulatory shell around a few bullet points). It passed both checks.

The pilot's dual purpose matters as a methodological point. A pilot that only verified writes would have been wasted capacity; the extraction it produced was usable content for the synthesis step. A pilot that only produced content but did not verify writes would have provided no guarantee that subsequent agents would be able to do the same. Combining the two functions kept the pilot lean while preserving the guarantee. The parallel swarm was spawned only after both checks passed.

The methodological rule underneath this phase is that parallel spawning is gated on pilot verification every time. Spawning a swarm without first demonstrating that one agent can write to the expected path is a specific failure mode — a swarm that cannot write consumes attention and returns nothing usable. The gate prevents the failure mode. There is no workaround, and the gate does not become optional after being passed once in a prior phase; write-capability is not stable across environments, and the cost of one pilot agent is small compared with the cost of a swarm that fails silently.

## 8. Phase C — Parallel Agent Swarm

Phase C spawned seven general-purpose agents concurrently in a single orchestration message. Each agent received an assignment scoped to a specific research set or a specific concern. Each was given read and write permissions, the exact files to read, explicit instructions about what to extract and what to ignore, and an exact scratch path to write its extraction to. All seven spawned in parallel.

Concurrent spawning is the operative word. Spawning sequentially — waiting for one agent to return before launching the next — would have defeated the pattern's efficiency benefit. Parallelism is what made chapter-scale extraction work tractable; a serial version of the same work would have consumed the orchestrating thread's attention across every individual agent's read cycle rather than absorbing the return of all seven at once.

The agent assignments were shaped by the scoping decisions from Section 4. Agents were assigned to discovery-meeting deep-dive sets (first meeting, second meeting, and third meeting's scope-shaping documents, with the third meeting's timeline-and-costing file deliberately excluded as commercial-only). One agent was assigned to the pricing-heavy middle sets (the internal pricing discussions, the positioning notes, and the pricing breakdown conversations) with explicit instructions to ignore commercial detail and extract only scope-shaping decisions, POC boundary changes, or positioning language that affected what the two screens needed to be. A second agent handled the remaining architectural-walkthrough deep-dives that the pilot had not covered (testing and QA approach; access and next steps). Another handled the latest technical research set (legacy stack, modern stack, conversion patterns). A final agent ran a source-transcript ground-truth pass against specific source files — an internal BayOne call, positioning notes, and the walkthrough transcript — to catch anything not already captured in the research library that was scope-relevant or technical-relevant, again explicitly ignoring commercial and internal color.

No agent was assigned to the deliverables folder or the pricing folder. Their contents were either fully commercial (excluded per scoping decision two) or formally committed scope that the research library had already restated. If the Phase A read surfaced a scope commitment that lived only in a deliverable file, that single file would have been read by the orchestrating thread directly; in practice this did not occur.

Each agent's instructions were explicit on two things. First, what to extract: a named section list (architecture, repositories, walkthroughs, compliance, constraints, commitments, open items, or a comparable set appropriate to its files), and an instruction to write substantively, not to summarize. Second, what to ignore: for the commercial-adjacent agent in particular, the instruction to strip all pricing mechanics was repeated at the top of the assignment. Instructions were given by the orchestrator in the single spawn message; agents did not interrogate the orchestrator mid-run for clarification.

Each agent wrote its output to a path under the scratch folder inside the POC handoff directory, following a consistent filename convention. When all seven returned, the orchestrating thread listed the scratch folder, confirmed each expected file was present, and proceeded to synthesis. The scratch folder became the raw-material substrate for Phase D.

## 9. Phase D — Synthesis Into Twelve Handoff Documents

Phase D was not delegated. It was the work of the orchestrating thread: reading every scratch extraction, integrating the extractions with the chronological narrative carried over from Phase A, and writing twelve final handoff documents. Each document had a specific role in the package. Each document was written as a complete answer to its scope question, not as a summary of the supporting material.

The principle governing synthesis was that judgment about what to include, emphasize, or characterize stayed with the orchestrating thread because that was where the full context lived. Agents produced faithful structured extractions inside narrow scopes. The orchestrating thread had read every anchor file in sequence, had briefed each agent, and had integrated the returns. That position — the one with the widest aperture — was the only one from which judgment calls about what belonged in a given handoff document could be made without extrapolation.

The synthesis practice followed several working rules. Claims were traceable to source: every substantive statement in a handoff document was supported either by a research file in the engagement's library or by a source transcript. Where the source material left something open, the document named the item as open rather than closing it with a guess. Where the source material contradicted itself (for example, stakeholder name spellings garbled in speech-to-text transcripts), the authoritative source was preferred (for names, the attendee screenshots from the technical meeting) and the resolution was recorded. Where the source material had been superseded by a later reframe, the superseded version was captured in the engagement history document as part of the arc and the current version was captured in the objectives-and-scope document as the current commitment; the two did not mix.

### 9.1 The Twelve-Document Roster

The final package contained the following twelve documents, each filling a specific role and written for a specific aspect of execution-phase readiness. Documents are grouped by the reading order they were designed to be consumed in.

| # | Document | Role | Audience expectation |
|---|---|---|---|
| 00 | Index | Entry point. Names each document, the reading order, the quickest-start path for a reader arriving cold, and the reference paths for the research library, source transcripts, and POC working folder. | Every reader opens this first. |
| 01 | Project Overview | Anchor explanation of what the two products are, why customers are asking for the classic view, what the POC is (UX overlay, not a conversion), what the two screens are at a glance, the stakeholder landscape in brief, and three high-level takeaways. | First substantive read after the index. |
| 02 | Engagement History | Chronological narrative from first contact through the technical walkthrough. Scope evolution, the major scope reframe mid-engagement, and the sequence of commitments and reversals. Commercial events deliberately excluded. | Read to understand why the scope is what it is; prevents treating superseded framings as current. |
| 03 | Objectives and Scope | The exact POC scope. The two screens by sub-surface. Toggle behavior. Backend constraints. Definition of done. Explicit exclusions. Open items the execution phase will need to resolve or raise. | The operational anchor for execution-phase work. |
| 04 | Strategic Approach | The conversion approach as articulated in the transcripts: fidelity as the target, the exponential-decay front-loading principle, feature-mapping approach, priority-versus-diversity ordering, parallelization posture for post-POC scale, automated-QA scope boundary, the four-agent architecture, customer transparency principle, and constraints on change without re-raising. | Read to understand the approach Codex will execute within. |
| 05 | Technical Landscape | Both stacks in depth. Legacy stack: web-component toolkit, Java layer, Oracle, device protocols. Modern stack: Angular front end, Spring Boot and Go services, Postgres, container runtime. Repository inventory across both. Walkthrough findings. Data-flow comparison. | The technical substrate that every work item sits on. |
| 06 | Conversion Patterns Reference | Working-desk technical reference. Points to the three deep-dive research files as the canonical source and restates the most immediately actionable patterns: widget mapping, module-system translation, data-binding translation, lifecycle-hook mapping, state-management translation, theme-toggle architecture, shared-service and display-adapter pattern, shell app integration, proposed folder structure, per-screen migration checklist, named conversion risks. | Consulted at the working desk during actual conversion work. |
| 07 | Stakeholders and Organization | Customer-side leadership, customer-side operational counterparts, customer-side tech leads, customer-side referenced-but-not-present people, BayOne-side team, speech-to-text name resolution table, decision ownership map, time zones, communication channels and etiquette. | Read to know who owns what decision and who to route which question to. |
| 08 | Repositories, Access, and Compliance | Repository inventories for both products. Classic-UI code location (marked open). Access provisioning path. AI compliance rules enumerated in full. The explicit list of things the execution phase must never do. Escalation routing when blocked on access, libraries, backend changes, tooling, or scope. | Read before any tool use; reread when any compliance-adjacent question arises. |
| 09 | Work Items | The backlog at transcript granularity. No invented tickets. Grouped by access and environment setup, code deep dive, Inventory conversion, Fault Management conversion, backend gap handling, verification and testing, closeout, and out-of-POC-scope items captured for context. | The backlog the execution phase works. |
| 10 | Open Questions and Risks | Open questions organized by category (product and scope, architecture and technology, access and operations, testing, AI compliance), each with a source citation and a how-to-resolve note. Risks surfaced during discovery, each with a mitigation. Guidance on how to use the document as a living backlog. | Revisited at key decision points. |
| 11 | Ways of Working | The engagement's operating posture. Bandwidth reality. Escalation routing. Decision authority (what the execution phase decides versus what it raises). Documentation and progress tracking rules. Communication rhythm. Patterns that define good execution. Customer-transparency principle. Guidance on when to stop and ask. | Read to know how the engagement runs day to day. |

The numbering is deliberate and carries semantic weight. The leading `00` index is the navigation anchor. The `01` through `08` documents establish context. The `09` document is the operational backlog. The `10` and `11` documents hold the discipline material — the open-questions and risks backlog, and the ways-of-working rules — that the execution phase returns to repeatedly rather than reading once. The reading order captured in the index matches this progression.

### 9.2 Folder Layout

The assembled handoff folder looked like this at the end of Phase D:

```
poc/
└── handoff/
    ├── 00_index.md
    ├── 01_project_overview.md
    ├── 02_engagement_history.md
    ├── 03_objectives_and_scope.md
    ├── 04_strategic_approach.md
    ├── 05_technical_landscape.md
    ├── 06_conversion_patterns_reference.md
    ├── 07_stakeholders_and_organization.md
    ├── 08_repositories_access_and_compliance.md
    ├── 09_work_items.md
    ├── 10_open_questions_and_risks.md
    ├── 11_ways_of_working.md
    ├── _proposed_plan_2026-04-20.md
    ├── _tree_snapshot_2026-04-20.md
    └── _scratch/
        ├── agent_01_set07_core.md
        ├── agent_02_set01_deepdives.md
        ├── agent_03_set02_deepdives.md
        ├── agent_04_set03_deepdives.md
        ├── agent_05_scope_only_sets_04_05_06.md
        ├── agent_06_set07_remaining.md
        ├── agent_07_set08_research.md
        └── agent_08_source_ground_truth.md
```

The twelve numbered documents at the top level are the handoff proper. The two leading-underscore files (the approved plan and the tree snapshot) are the working artifacts that recorded the phase's own state. The scratch folder holds the eight agent extractions that fed the synthesis.

## 10. Phase E — Verification and Cleanup

Phase E closed the loop. The twelve final documents were reviewed against their supporting scratch extractions and against the research library to confirm that every substantive claim was traceable. The index document was verified to reference every other document in the package. The scratch folder was preserved rather than deleted, explicitly, to maintain traceability from final document back to raw extraction back to source. A later reader who wanted to audit where a specific claim in a handoff document came from could follow the chain: handoff document to scratch extraction to source research file to source transcript.

The preservation of scratch material deserves a specific note. The default convention in many kinds of synthesis work is to delete intermediate artifacts once final output is produced, on the premise that intermediate artifacts carry no value after synthesis. The methodology applied here takes the opposite position: intermediate artifacts are the audit trail that makes final output interrogable. If the final handoff document says something specific about the backend coverage of the two POC screens, and a later reader wants to know where that specific claim came from, the scratch extraction is the first stop, and the research file the scratch extraction cites is the second. Deleting scratch closes off the audit chain one link early.

The approved plan and the tree snapshot were likewise preserved in place. A reader a month later could look at the plan and see exactly what was committed to before execution began, and at the tree snapshot to see what the engagement folder's state was at the moment the commitment was made.

## 11. The Parallel-Agent Production Discipline

Several elements of the parallel-agent pattern as practiced in this phase are worth naming as methodology rules, even though the cross-cutting chapter later in the set covers the pattern's generalization. The rules here are the load-bearing ones for this specific phase.

**Pilot before swarm, every time.** A pilot agent is spawned first, with the same permission model the swarm will use, to verify write capability by on-disk inspection of its output. The swarm is spawned only after the pilot's artifact has been confirmed to exist at the expected path with the expected content. A pilot that succeeds does not grant the environment a blanket license; a new pilot is spawned whenever the orchestrating thread is uncertain that the permission model has held. The cost of a pilot is trivial compared with the cost of a swarm whose outputs do not materialize.

**Parallel spawning, not sequential.** Once pilot verification is complete, swarm agents are spawned concurrently, in a single orchestration message, not one after another. Parallelism is the property that makes the pattern tractable at scale. Sequential spawning collapses the pattern's benefit and consumes the orchestrating thread's attention across every agent's run time.

**Write-verification by on-disk inspection, not self-report.** An agent's self-reported success does not confirm its output's existence. Whether for the pilot or for swarm returns, the orchestrator verifies by listing the expected output directory and confirming the expected files are present. Agents that report success without the corresponding on-disk artifact are a known failure mode.

**One concern per agent.** Each agent's assignment is scoped to a specific research set or a specific extraction concern. Broadening an agent's scope to cover multiple unrelated sets dilutes the extraction quality and makes agent failure harder to diagnose. Narrow scope, named sections, explicit exclusions — this is the pattern that returns usable extractions.

**Explicit exclusions.** For scope-adjacent material an agent is expected to step around (in this phase, the commercial mechanics in the pricing-heavy sets), the instruction to ignore is stated at the top of the agent's assignment and repeated where the exclusion is most likely to be tempting. Agents that are told only what to extract are more prone to including excluded material than agents that are told both what to extract and what to ignore.

These five rules — pilot-before-swarm, parallel spawning, on-disk verification, one-concern-per-agent, and explicit exclusions — held throughout Phase C and carried forward into later work that used the same pattern.

## 12. Delegation Boundaries Between Orchestrator and Workers

The orchestrator-versus-worker boundary held strictly throughout the phase. What agents did and did not do is the central methodological question of parallel-agent work, and the boundary drawn in this phase is worth making explicit.

**What agents did.** Bulk reading of assigned document sets. Structured extraction into named sections, following the orchestrator's template. Faithful preservation of the content they read, including specific technical detail, stakeholder names, verbatim commitments, and open items. Writing their extraction to the specified scratch path. Returning a short report of path and summary.

**What agents did not do.** Synthesis into final handoff documents. Judgment calls about what to include, exclude, or emphasize. Characterization of ambiguity (whether an item is open, superseded, or resolved). Cross-document consistency checks. Final-document-level decisions about structure, ordering, audience, or reading path. Any work that required the full engagement context rather than the narrower context of a single assignment.

The boundary is asymmetric on purpose. Extraction scales with parallelism. Judgment does not; judgment depends on full context, and full context lives only in the orchestrating thread. Placing judgment work inside an agent with narrow scope produces judgments made on partial context, which is either worse than judgment on full context (the common case) or better by accident (a failure mode that looks like a success). The methodology treats both as avoidable and keeps judgment with the orchestrator.

This boundary is why Phase D was not delegated. A synthesis of the twelve handoff documents performed by a parallel swarm would have produced twelve documents each written from its author's partial view of the engagement, and cross-document consistency would have been a separate reconciliation problem. Writing the twelve documents from a single orchestrating thread that had carried the full arc through Phase A and had read every scratch extraction kept the documents coherent with each other and coherent with the underlying material.

## 13. Working Disciplines That Held Throughout

A set of working disciplines held through every phase of the handoff assembly. They are not phase-specific and are worth listing together.

**Chronology over convenience.** The research library is append-only and chronological. The read followed the chronology, and the synthesis preserved it. Scope reframes were recorded in the engagement-history document as events that happened at a moment in the arc, not as a revised current state that erased its own history. A reader of the history document sees the arc; a reader of the objectives document sees the current commitment. The two views coexist without contradiction.

**Observation versus conclusion.** Structural observations (what a research file said, what a screenshot showed, what a stakeholder committed to in a specific meeting) were distinguished from conclusions (what those observations imply for execution). The handoff documents preserved observations with citations and offered conclusions only where the source material supported them. Where a conclusion would have required extrapolation beyond the source, the item was flagged as open.

**Fidelity to stated language.** Where the transcripts gave a specific phrasing — "classic view," "fidelity over novelty," "exponential decay," "four-agent architecture," "two-screen POC" — the phrasing was preserved in the handoff documents. Paraphrase was used for clarity only; stated commitments were preserved verbatim.

**Explicit exclusions, repeated.** The non-objectives from the plan (no timelines, no estimates, no prescriptive implementation guidance, no invented decomposition, no commercial content, no archive reading) were repeated in agent assignments where an exclusion was at risk, and in the handoff documents themselves where the exclusion affected scope or framing.

**Planning in files, not in stream.** Design decisions, plan drafts, and scope commitments went into markdown files. Stream-of-orchestration commentary was the exception, not the rule. The plan document, the tree snapshot, and the final handoff documents were the substantive outputs; orchestration narration did not substitute for them.

**No unilateral decisions on ambiguity.** Where instructions or source material were ambiguous, the ambiguity was surfaced and resolved with the reviewer before execution continued. Silent adjustments were treated as a specific failure mode to avoid.

## 14. Outcome

The phase produced a complete, self-contained, interrogable context package for the execution phase of the POC. The twelve handoff documents under the POC handoff folder covered project context, engagement history, objectives and scope, strategic approach, technical landscape, conversion patterns, stakeholders, repositories and compliance, work items, open questions and risks, and ways of working, with an index to orient a reader arriving cold. The scratch folder preserved the eight agent extractions that fed the synthesis. The plan and tree snapshot preserved the phase's own state at the moment the handoff was committed. Every claim in every final document traces to a specific research file or source transcript.

A reader picking up the package can walk into the execution phase without having to reconstruct engagement context from source. The quickest-start reading path — index, objectives, conversion patterns for the core sections, repositories and compliance for the core rules, ways of working for escalation — orients a reader inside a short reading window. A reader seeking full depth can work the package top to bottom; a reader seeking a specific question can navigate to the relevant document via the index. The package was designed to be readable in both modes.

The handoff package is not a frozen specification. The final index document notes explicitly that where the package's framing feels inconsistent with what a reader sees in the actual repositories, the repositories and the customer lead's current guidance take precedence over the package, and the relevant handoff document is updated with a dated note when something material shifts. The package is a strong starting snapshot of the engagement's state at the moment the execution phase opened, not a permanent specification that freezes that state.

---

The package was written with the assumption that execution would open against the actual codebase — the two product repositories, the classic-UI code, the shared infrastructure repositories — and that the next phase's substance would depend heavily on what that codebase turned out to contain. The arrival of concrete codebase analysis artifacts is the subject of the next chapter.
