# Chapter 5 — The Parallel Investigation Pattern

## 1. The Pattern in One Sentence

An orchestrating thread plans and integrates; scoped worker agents, launched concurrently, do the bulk reading and structured extraction; the orchestrator then reads the workers' outputs, synthesizes across them, and integrates the result into the final artifact. The point of the pattern is scale — the ability to absorb a large volume of source material in a single working phase — while preserving the judgment and synthesis work in a single thread that carries the full engagement context.

The pattern appeared first in the handoff-package assembly phase (Chapter 3), reached its largest application during the tree-report absorption phase (whose input artifact is the subject of Chapter 4), and is reapplied reflexively in the production of this documentation set itself (per rule 13). This chapter pulls the pattern out of the phases in which it was practiced and documents it as a general-purpose discipline, portable to any future engagement with comparable shape.

## 2. What the Pattern Is For

The problem the pattern exists to solve is a structural one. A working phase may need to absorb a body of source material too large for the orchestrating thread to hold and reason about in sequence without exhausting its working capacity or collapsing its awareness of the broader engagement. The naive response — reading every file in the orchestrating thread — either fails outright (context runs out) or succeeds only at the cost of losing the cross-cutting awareness that made the orchestrating thread the right place to do synthesis.

The pattern responds by splitting the work along a specific seam. Bulk reading and structured extraction are delegated to worker agents, each scoped to a narrow assignment. The worker reads its assigned material cover to cover, produces a structured extraction against a named template, and writes that extraction to a predetermined scratch path. Because workers operate concurrently, the absorption of the whole body of source material happens in roughly the time it takes a single worker to complete, not in the sum of the individual worker run times.

Meanwhile the orchestrating thread preserves the one capability the workers do not have: full engagement context. It has read the prior-phase anchors. It knows what the scope commitments are, where the open questions sit, which framings have been superseded, and which stakeholders own which decisions. When the workers return, the orchestrator reads the scratch extractions and integrates them against that carried context. Synthesis — the judgment about what to include, what to characterize, what to flag, what to tag as open — stays in the thread that can make those calls on full information.

## 3. Why Parallel Rather Than Sequential

Sequential worker execution defeats the purpose. A working phase with several workers will, in a serial version, take roughly as long as the sum of its individual worker run times; the orchestrator blocks on each worker in turn and has to carry the completion of each worker into the briefing of the next. The pattern's efficiency benefit — chapter-scale or bundle-scale absorption in a bounded working window — evaporates the moment the workers are strung end to end.

Parallel execution is the property that makes the pattern tractable at scale. Workers spawned concurrently run independently, do not coordinate with each other, and return roughly together. The orchestrator's attention is consumed once, at briefing time, and once again, at synthesis time — not across every worker's individual read cycle. The working phase compresses to the time of the slowest single worker plus the fixed cost of orchestration overhead.

This is why concurrent spawning, not sequential spawning, is the operative form. Spawning workers across successive messages serializes them even when the workers themselves are capable of running in parallel; the serialization happens in the orchestration layer, not in the worker layer. Single-message spawning preserves the concurrency.

## 4. Why Orchestrator-Synthesized Rather Than Worker-Synthesized

Delegating synthesis to workers is a specific failure mode worth naming. It is tempting — workers are already doing the reading, it seems efficient to have them also produce the finished integration — but it breaks the property that gives the pattern its discipline.

Synthesis is where engagement context, scope discipline, and judgment intersect. It decides what belongs in the final artifact, what gets characterized how, what is flagged as open, what is tagged as superseded, and where a conflict between two sources should be resolved in favor of one over the other. Every one of those calls depends on context a worker does not have.

A worker has been briefed on its assigned scope. It has read the files named in its assignment. It does not have:

- The full engagement arc that shaped what is in scope.
- The prior-phase decisions that constrain what a current-phase document can say.
- The cross-cutting awareness of what other workers in the same swarm were reading and producing.
- The history of scope reframes, superseded framings, and stakeholder commitments.
- The operating posture that decides how an ambiguity is handled when the source material is silent.

Giving a worker synthesis responsibility is giving that worker judgment authority it has not been set up to exercise. The worker will do the best it can on partial context, which means one of two outcomes: the worker produces a synthesis that reads plausibly but is subtly miscalibrated to the engagement (the common and dangerous case), or the worker produces one that happens to land correctly (the rarer and harder-to-diagnose case, because the subsequent session cannot distinguish it from careful integration).

The pattern preserves the separation deliberately. Workers extract structured raw material inside narrow scopes. The orchestrator interprets and integrates. Extraction scales with parallelism; judgment does not, because judgment depends on full context, and full context lives only in the orchestrating thread.

## 5. The Write-Capability Pilot — Non-Negotiable

Before any parallel workers are spawned, a single pilot worker executes a small verification task. The pilot is given a minimal assignment: read a known small file and write a short confirmation artifact to a specific path, typically a scratch location under the working folder. The orchestrator then verifies the artifact's existence and content on disk directly, not by relying on the worker's self-report of success.

If the pilot succeeds — the artifact is on disk at the expected path, with content that demonstrates the worker actually executed the task rather than returning a plausible summary — the parallel phase is cleared to proceed.

If the pilot fails, the orchestrator stops immediately and flags the issue to the user. Failure here means any of the following:

- The artifact does not exist at the expected path.
- The artifact exists but is empty, or contains content the worker could have produced without doing the task.
- The worker reports success but on-disk inspection shows no artifact.
- The worker cannot complete the task because writes are blocked, the path is outside its permission scope, or the runtime is misconfigured.

There is no workaround. Attempting the absorption in the orchestrating thread alone defeats the pattern — the whole point is delegation of bulk reading, and if the delegation cannot occur, the phase cannot proceed on the planned shape. The correct response to pilot failure is to stop the phase, surface the problem, and resolve it before any further worker activity is attempted.

### Why the gate is non-negotiable

The core failure mode of the pattern — workers cannot write — is silent in the worker's own reporting. A worker that cannot write often still returns a plausible-looking success message, because the worker's last action is to tell the orchestrator what it believes it did. Only on-disk inspection catches the discrepancy. A pattern whose central failure mode is untested at the gate will discover that failure mid-phase, after substantial briefing work is wasted and after the orchestrator has committed attention to a swarm that cannot deliver.

The gate is cheap: one pilot worker, one small file read, one small file written, one directory listing by the orchestrator. The absence of the gate is expensive: a full swarm briefed, launched, and returned with nothing on disk, and the phase reopened from the top. The economics argue for the gate every time.

### The gate is per-phase, not per-engagement

Write capability is not a stable property across environments, permission models, or working phases. A gate passed in an earlier phase does not license a later phase to spawn without reverification. The pilot is spawned every time parallel work is about to begin. This is not paranoia; it is the recognition that the cost of one pilot agent is small compared with the cost of a swarm that fails silently in a new configuration.

## 6. Pilot-First Followed by Parallel Scale

The pattern's gating structure is pilot → verify → parallel. Specifically:

1. The orchestrator spawns a pilot worker alone, not in the same batch as the eventual parallel swarm.
2. The pilot completes. Its artifact is inspected on disk. The orchestrator reads the artifact, confirms it contains the expected content, and decides whether the environment is cleared to proceed.
3. Only then does the orchestrator spawn the parallel workers.

Spawning the pilot and the swarm in the same batch — a common shortcut under time pressure — defeats the gate's purpose. If the pilot and the swarm launch together, the pilot's verification happens after the swarm is already in flight, and the verification can no longer block a bad spawn. The pilot becomes a ceremonial first result rather than a functional gate.

The verification step between pilot and swarm is therefore load-bearing. It is the only point in the pattern where the orchestrator explicitly stops, inspects the environment's behavior, and makes a go/no-go decision before the more expensive action.

## 7. Single-Message Parallel Spawning

In tools and frameworks that support concurrent worker invocation, the parallel workers are launched in a single message or a single batched call. This ensures they execute concurrently. Spawning them across sequential messages — one worker per message — serializes the phase at the orchestration layer even when the worker substrate itself is capable of parallel execution.

The practical rule is: once the pilot gate is passed, every worker in the subsequent swarm is spawned in one action. The orchestrator prepares all worker briefs, then issues the spawn. The orchestrator does not wait for the first worker to return before spawning the second; it does not interleave spawns with other work; it does not spawn a partial swarm and then add more workers later in the phase.

Partial-swarm patterns — launching a subset, waiting, then launching more — reintroduce the throughput ceiling the pattern exists to remove and also introduce a coordination problem (the later workers may be briefed against state that has since shifted). Launch the whole planned swarm at once.

## 8. Worker Briefing Structure

Each worker receives an explicit brief. Ambiguous briefs produce inconsistent extractions; the compounding effect across a swarm is that inconsistencies multiply and the synthesis step has to reconcile them. The remedy is upfront clarity in the brief itself.

A worker brief contains:

1. **Scope of the assignment.** The subject or document set the worker is responsible for, named specifically enough that the worker cannot confuse it with an adjacent scope. "The tree report for repository X" is specific; "the inventory material" is not.

2. **Source files to read, named by path.** Every file the worker is expected to absorb, cited by exact path. The worker is not expected to discover the right files by searching; the orchestrator has already identified them and names them explicitly.

3. **Output path to write to.** The exact path the worker writes its extraction to. One file per worker, by agent number or by subject, under a pre-agreed scratch location. The worker does not choose its own path.

4. **Authoring standards or rules to follow.** By reference, not by reproduction — the brief points at the rules document or the relevant sections of it rather than copying the rules in full. This keeps briefs concise and also ensures that updates to the rules flow through without every brief needing to be rewritten.

5. **What not to do.** Explicit exclusions. What is out of scope for the extraction. What interpretation is not the worker's responsibility. What to ignore when encountered. Workers told only what to extract are more likely to over-include than workers told both what to extract and what to ignore.

### Optional brief elements

Depending on the phase, briefs may also specify:

- A named section template the extraction must follow, so that downstream synthesis can compare parallel sections across workers without reformatting.
- An observation-versus-conclusion reminder (see Section 13) for the worker to carry into its output.
- A note on how to handle items that fall on the edge of the scope — typically, extract and flag, rather than extract silently or drop silently.

### Briefs are not conversations

The brief is given once, at spawn, in the single orchestration message. The worker does not interrogate the orchestrator mid-run for clarification. If the brief is ambiguous enough that the worker would need clarification, the brief was under-specified and the right response is to recall the worker (or to accept that its output will be thinner than expected) rather than to convert the spawn into a back-and-forth exchange.

## 9. Scoped Extractions to a Scratch Location

Workers write to a pre-agreed scratch path under the working folder. The convention used in the engagements documented in this set was one file per worker, named by agent number and by subject — for example, `agent_03_epnm_inventory.md` or `agent_07_ems_infra_ui.md`. The convention is not the point; the consistency of the convention is.

Scratch files are preserved. They are not deleted after synthesis. The reasoning is the same as for the handoff-package assembly phase's scratch folder (Chapter 3): the intermediate artifacts are the audit trail. A later reader who wants to know where a specific claim in the synthesized artifact came from can follow the chain from synthesized artifact to scratch extraction to source file. Deleting scratch closes that chain one link early.

The scratch folder's role continues past the synthesis step. A subsequent working phase that revisits the same source material can read the extractions without rereading the underlying source. A follow-up worker assigned to re-extract a scope can be given the previous extraction as a starting point, not as an authoritative document but as a structured reference.

## 10. Orchestrator Behavior During Worker Execution

The orchestrator does not block on workers. Once the swarm is launched, the workers execute asynchronously. The orchestrator can continue preparatory work for the synthesis phase — drafting the synthesis template, rereading the prior-phase anchors for cross-cutting context, surfacing and writing down questions whose answers depend on what the workers return.

Worker completion is asynchronous. As each worker returns, the orchestrator records the arrival and, if it is useful to start incorporating early returns, may begin assembling a running findings log as returns arrive. The synthesis proper, though, waits until the full set is in. A synthesis begun before all workers are back risks being shaped around the early returns' emphasis at the expense of the later returns'.

When every expected worker has returned, the orchestrator lists the scratch folder, confirms each expected file is present, and proceeds to synthesis. If an expected file is missing, that is a case for Section 14 (failure modes): the orchestrator decides whether the scope was the limiting factor (the worker found nothing material), whether a follow-up worker is needed, or whether the phase should pause while the issue is diagnosed.

## 11. After-Swarm Synthesis

Synthesis is the orchestrator's own work. It is not delegated, not in this phase and not by default in any phase that uses the pattern. The orchestrator reads every scratch extraction in full, integrates the extractions against the engagement context already in the thread, and produces the synthesized artifact.

The synthesis step is structured:

- **Cross-cutting view.** The orchestrator identifies the patterns that show up across workers — repeated themes, recurring file types, consistent naming conventions, shared open items. These are the raw material for cross-cutting sections of the final artifact (for example, the "Where the Classic View Mounts" section in the tree-report synthesis is built from observations that several workers made independently).

- **Conflict identification.** Two workers may observe the same material differently, or one may see something another missed. The orchestrator surfaces the conflicts and records them as findings, rather than silently resolving them in favor of whichever version seems more confident. The user sees the conflict explicitly.

- **Gap identification.** Some scratch extractions will be thinner than expected. The orchestrator assesses whether the source material was thin (in which case the extraction is faithful to the source) or whether the worker missed material (in which case a follow-up extraction is warranted). Follow-ups are new worker invocations, not main-thread fixes.

- **Integration into the synthesized artifact.** The orchestrator writes the final document using the carried engagement context, the scratch extractions, and the cross-cutting observations, in the format the artifact requires. Citations point back to scratch extractions where a specific observation came from a specific worker.

If the synthesis itself is too large to hold in one thread, it is broken into smaller units and each unit's synthesis is the orchestrator's own work, not a worker's. Large syntheses are decomposed on scope boundaries (one unit per logical section), not delegated to a second-level swarm.

## 12. Pattern Flow at a Glance

```
ORCHESTRATOR                                 WORKERS / SCRATCH
────────────────────────                     ───────────────────────

[1] Plan phase, identify scopes              ──
                                              │
[2] Spawn pilot worker ────────────────────► pilot reads known file
                                             writes small artifact
                                             reports back

[3] Inspect artifact ON DISK                  ──
    (not self-report)

     │
     ├── artifact present + correct ──► proceed to [4]
     └── artifact missing/blocked ────► STOP, flag to user

[4] Assemble all worker briefs
    (scope, source files, output
    path, rules, exclusions)

[5] Spawn full swarm IN ONE MESSAGE ──────► worker 1 ──► scratch/agent_01_*.md
                                            worker 2 ──► scratch/agent_02_*.md
                                            worker 3 ──► scratch/agent_03_*.md
                                                 ...
                                            worker N ──► scratch/agent_NN_*.md
                                            (run concurrently)

[6] Do preparatory work while
    workers run; record returns
    as they arrive

[7] On full return, list scratch
    folder; confirm all expected
    files present on disk

     │
     ├── complete ──► proceed to [8]
     └── missing ───► diagnose (thin source vs. follow-up worker)

[8] Read every scratch file

[9] Synthesize:
      • cross-cutting patterns
      • conflicts between workers
      • gaps and follow-up needs
      • integration into artifact

[10] Write synthesized artifact
     (scratch preserved, not deleted)
```

The orchestrator acts at steps 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10. The workers act only at step 5, concurrently, each against its own scope. Judgment is concentrated at steps 3, 7, 8, and 9.

## 13. Observation Versus Conclusion in Worker Output

Workers are instructed, as part of their brief, to preserve the observation-versus-conclusion distinction (rule 10 in the authoring rules; Chapter 3 Section 13 for the phase-level treatment). A structural fact is cited as fact; a name-based suggestion is tagged as suggestion; a path in a directory is an observation, while what that path implies for implementation is a conclusion that requires validation.

This discipline travels into the scratch extractions. The tree-report absorption phase offers a concrete example: workers observed that a file named `SyslogListViewWebSocket.js` exists in the EPNM assembly repository. That is an observation. The inference that the real-time delivery mechanism for syslogs is therefore a WebSocket stream is a conclusion, cited as a probable pattern rather than a confirmed fact, and flagged for verification by a source read in the execution phase.

The synthesis carries the distinction forward. The synthesized artifact does not promote observations to conclusions during integration. Where a conclusion is drawn, it is tagged as a conclusion, cited to the observations that support it, and flagged for verification if verification has not yet occurred.

The discipline is load-bearing because it prevents a specific class of failure: treating a plausible inference from a filename as a confirmed implementation detail. That kind of drift propagates across a synthesis and becomes very difficult to unwind once the synthesized artifact is consumed downstream.

## 14. Failure Modes to Anticipate

Several failure modes recur in parallel worker phases. Each has a specific countermeasure built into the pattern.

**The pilot succeeds but a parallel worker fails silently.** The pilot gate catches the class of failures that are general to the environment, but not every kind of failure is caught by the pilot. A specific worker in the parallel swarm may still return with nothing on disk despite reporting success. Countermeasure: the orchestrator lists the scratch folder after the swarm returns and confirms every expected file is present. Self-reported success does not close the loop; on-disk presence does.

**Two workers produce conflicting observations.** Worker A observes one thing in its scope; worker B observes an inconsistent thing in its scope. The orchestrator records the conflict as a finding. It is surfaced explicitly in the synthesis, not silently resolved in favor of one worker over the other. The user sees the conflict and can decide how it should be handled — often by a follow-up source read.

**A worker returns thinner output than expected.** The orchestrator assesses whether the scope was the limiting factor (the input material was thin, so the extraction is faithful) or whether the worker needs a follow-up (the input material was dense but the worker missed it). Follow-ups are new worker invocations with sharper briefs, not main-thread fixes. Doing the worker's re-extraction in the orchestrator dilutes the orchestrator's context-carrying role.

**Scratch-path typos lead to lost output.** A worker writes to a path that differs, even by a single character, from the path the orchestrator expects. The output exists on disk but the orchestrator cannot find it. Countermeasure: path conventions are agreed ahead of time and verified in the pilot. The pilot's output path is inspected explicitly; if the pilot's path is correct, subsequent workers following the same convention are unlikely to misname their outputs. When a swarm's returns show a missing expected file, the orchestrator checks for nearby typos before concluding the worker failed.

**A worker's brief is ambiguous and the worker interprets it creatively.** The worker does what seems reasonable given the brief; the orchestrator expected something else. Countermeasure: briefs are explicit on both what to extract and what to ignore, with named section templates where consistency matters. Ambiguous briefs are a brief-authoring failure, not a worker failure, and the remedy is to sharpen the brief before the next phase — and, for the current phase, to accept the resulting extraction as it is or to respawn with a sharper brief.

**Synthesis over-reach under time pressure.** The orchestrator, facing a large swarm return, is tempted to delegate some of the synthesis to a second-level worker. The pattern explicitly rejects this. If the synthesis is too large, it is decomposed on scope boundaries and each unit is the orchestrator's own work. A second-level synthesis worker reintroduces the problem the pattern was set up to avoid.

## 15. Where the Pattern Was Applied in This Engagement

The pattern was applied at three distinct points in the engagement, in progressively larger and more complex forms.

**Handoff-package assembly.** During Phase C of the handoff-package phase (Chapter 3), workers absorbed specific document sets in parallel — some discovery-meeting deep-dives, some research categories, some source-transcript ground-truth passes — each with narrow scope and explicit exclusions. The orchestrator synthesized the returns, along with the chronology already in the thread from Phase A's cover-to-cover read, into twelve final handoff documents. The pattern's load-bearing rules — pilot-before-swarm, on-disk verification, single-message concurrent spawning, one concern per worker, explicit exclusions — were established in this phase and carried forward.

**Tree-report absorption.** The largest application. The input was a structural bundle for each repository in the POC's scope — one tree report per repository (see Chapter 4 for the artifact's structure and generation). A worker was assigned to each repository's tree report. The assignments followed the one-concern-per-worker rule: a single worker was responsible for a single repository's absorption, with its brief naming the tree report by path and specifying the named sections the extraction was to follow. The workers ran concurrently. Their scratch extractions landed in a pre-agreed scratch folder, one file per worker. After the swarm returned, the orchestrator read each extraction, identified cross-repository patterns (where the classic view probably mounts, which shared components are theme-neutral versus theme-bound, which backend gaps may exist, where naming collisions are present), and produced the cross-repository synthesis. The synthesis is the input to the execution phase's internal mapping work. The running findings log kept during the absorption and the synthesis are both preserved; the per-worker scratch extractions are preserved alongside.

**Production of this documentation set.** The documentation itself follows the pattern it describes. The orchestrating thread plans chapters, verifies write capability via a pilot worker (per rule 13), and spawns chapter-writing workers in parallel. Each worker receives a chapter scope, a source-material list, an output path, and a reference to the authoring rules. The orchestrator integrates the returned chapters, maintains cross-chapter consistency, and updates the contents document. This is the engagement's operating posture applied reflexively to its own record-keeping.

Each of these three applications used the same pattern. The application differed in scale (a small swarm for handoff assembly, a larger one per-repository for tree-report absorption, a chapter-per-worker pattern for the documentation) but the structure held: pilot first, parallel scale afterward, orchestrator synthesis, scratch preservation, on-disk verification at every step.

## 16. The Discipline's Portability

The pattern generalizes to any domain where a large absorption workload needs to be done in a bounded working window with quality discipline intact. Specific domains where the pattern applies:

- **Codebase analysis** — one worker per module, repository, or subsystem, with the orchestrator synthesizing the cross-cutting architecture view.
- **Transcript processing** — one worker per meeting or conversation, with the orchestrator synthesizing the engagement arc.
- **Documentation production** — one worker per chapter or section, with the orchestrator maintaining consistency and integration.
- **Compliance audits** — one worker per control or policy area, with the orchestrator synthesizing findings and flagging gaps.
- **Research synthesis** — one worker per source document or source domain, with the orchestrator synthesizing the cross-source view.

The customer-facing point is straightforward: the methodology scales because the pattern scales. Not because any individual worker does more work, and not because the orchestrator itself somehow absorbs more than it could before — but because the orchestrator can marshal many workers at once while keeping judgment in one thread. The ceiling on throughput is the ceiling on parallelism, not the ceiling on a single thread's context window.

The pattern's cost is the orchestration discipline: the pilot gate, the brief-writing rigor, the on-disk verification, the synthesis discipline, the scratch preservation, the explicit handling of conflicts and gaps. These are not optional; they are what distinguishes a pattern that produces reliable output from one that produces plausible-looking output that is subtly wrong. The discipline is the methodology.

---

The pattern's largest application in this engagement — the tree-report absorption — carried into a synthesis whose output is a cross-repository map of where the classic view probably mounts, what the shared components look like, and where the backend gaps may sit. The next chapter takes that synthesis up as its subject.
