# Chapter 6 — Cross-Repository Synthesis and Mapping

## 1. The Phase in Context

The previous chapter documented the parallel absorption of structural artifacts. A set of per-repository tree reports was ingested by a swarm of narrowly scoped workers, each producing a structured extraction for one repository. At the end of that phase, the engagement had a folder of per-worker extractions: one for each repository under analysis on both product sides, plus a running findings log that caught cross-agent observations as they surfaced.

The artifact set was rich. It was also not yet usable. A reader of the extractions alone could not answer the question that mattered for the next phase of work: given the POC's own scope, where across this entire repository set does the relevant functionality appear to live? The extractions gave the raw material; what was missing was the cross-cut.

This chapter documents the synthesis stage that produced that cross-cut. Synthesis, in this engagement's methodology, is the work of integrating many narrowly scoped structural extractions into a single cross-repository map organized by the scope the downstream phase will actually work against. It is not delegated; it stays in the orchestrating thread. It uses the full-context aperture that the orchestrator carries from earlier phases to make judgment calls about where each POC sub-surface apparently lives, which observations rise to the level of candidate conclusions and which stay observations, and which gaps are real enough to flag for decision.

The chapter covers the synthesis question, the shape of the synthesis artifact, the observation-versus-conclusion discipline that holds the artifact's epistemic integrity, the cross-cutting findings the synthesis surfaced, the role of the findings log as the synthesis' running memory, the companion primers produced alongside the map, and the disciplines that governed the work throughout.

## 2. The Synthesis Question

Every synthesis phase has a single organizing question. For this engagement, the question was:

> Given the per-repository structural extractions produced during absorption, where — across the full repository set and across both product families — does the functionality in POC scope appear to live?

The phrasing is deliberate. The question is a mapping question, not an implementation question. It asks for apparent location, not definitive assertion. It asks for the POC's own scope decomposition, not a full codebase index. And it asks about both product families in one frame, so that the map reads as a single two-sided reference rather than two separate surveys.

The POC covers two screen families: Inventory and Fault Management. Each is further decomposed into sub-surfaces that the objectives-and-scope document had already committed to — five for Inventory (Network Devices list with filters and toolbar actions; Device Details with its left menu; Chassis View on the left of Device Details; Device 360 popup; Interface 360 nested inside Device 360) and three for Fault Management (Alarms table; Events; Syslogs). The synthesis answers for each sub-surface of each screen family: in what repositories, at what paths, do the relevant artifacts appear? For each sub-surface the answer has two sides — the legacy-product side, where the classic UX currently lives and which the rebuild must faithfully reproduce, and the modern-product side, where the classic rebuild will plug in and which provides the backend contract the rebuild consumes.

Framing the question this way is part of the discipline. It is easier to describe the synthesis as "figure out where the code is" and harder to describe it as "answer for each sub-surface in each screen family, and for each side of the product boundary, the apparent locations of relevant artifacts, with appropriate epistemic qualifiers." The second framing is the correct one. It is the framing that keeps the synthesis' output usable as a targeted reference rather than as an amorphous index.

## 3. The Synthesis Artifact's Shape

The synthesis produces one primary artifact: a cross-repository map organized by the POC's own scope decomposition. The artifact is a working document, maintained in the scratch area alongside the per-worker extractions that feed it. Its structure reflects the synthesis question's structure.

At the top of the artifact sits a short reader's guide — how to interpret the rows, what the columns represent, and the explicit scope caveat that everything below is candidate material pending source-level verification. This preface is load-bearing. A reader skimming the map without reading the preface could mistake the two-column tables for conclusions, and the tables are not conclusions. The preface preempts that reading.

Next sits a big-picture diagram at the repository level, covered in Section 4 below. This diagram orients the reader to the overall shape of both product families and their internal dependency structures before the reader encounters any sub-surface-level detail.

The body of the artifact is then a sequence of sections, one per screen family. Within each screen family, sub-sections for each sub-surface. Within each sub-surface, a two-column table:

- **On the legacy-product side** — the apparent reference paths. Where, in the legacy codebase, the functionality is rendered, backed, or supported. This side represents the source of the classic UX that the rebuild must reproduce.
- **On the modern-product side** — the apparent host paths. Where, in the modern codebase, the classic rebuild is most likely to mount, which shared components it will likely reuse or wrap, and which REST contract it will consume.

Each row in a sub-surface table names an aspect (the list widget, the table primitive, a specific wizard control, the REST contract, a real-time update pipe, a job-scheduling surface) and gives the apparent locations on each side for that aspect. Paths are cited verbatim from the extractions. Line counts, where surfaced by the tree reports, are retained as structural signals — not as throughput measures, but as indications of which files are substantive and which are thin.

Below the tables, for each sub-surface, narrative notes flag the observations that rose above the row level: open questions that appear resolvable by the structural signals, gaps that appear to want a decision, collisions with existing naming, or ambiguities that would need source-level disambiguation.

At the bottom of the artifact sit two cross-cutting sections. The first describes where the classic rebuild apparently mounts — shell-to-library wiring, route registration, navigation registration, theming plumbing, shared-service integration — extracted across sub-surfaces because the wiring concerns are not sub-surface-specific. The second captures the synthesis' own open-question disposition: of the open items captured in the handoff's open-questions document, which ones the synthesis appears to have resolved, which it has refined, and which remain unchanged.

The final section of the artifact is a short read-order recommendation for the downstream execution phase. Given that the map points at many files, the recommendation orders them by what a reader would most usefully open first when actual source becomes readable. This section is prescriptive only about ordering, not about outcome — it is a reading plan, not a conclusion about implementation.

## 4. The Big-Picture Diagram

At the top of the cross-repository map sits an ASCII diagram showing the two product families at the repository level. The diagram's purpose is to give a reader, in a single visual frame, the shape of what they are about to encounter row by row. The diagram looks approximately like this:

```
LEGACY PRODUCT SIDE (classic UX source of truth)
───────────────────────────────────────────────────────
  framework repo              ← UI framework, widget toolkit, themes
        ↑ depended on by
  assembly repo               ← Inventory UI + Fault UI (runtime views)
  inventory repo              ← Inventory backend (Java, relational DB)
  fault repo                  ← Fault backend + policy-mgmt UI
                                (includes correlation engine,
                                 event / syslog domain subtrees)
  chassis-visualization repo  ← Chassis renderer (SVG + JS + Java)

           All feature repos depend on the framework repo.
           Not directly runnable locally; requires product VM.

MODERN PRODUCT SIDE (classic rebuild host and backend)
───────────────────────────────────────────────────────
  shell app                   ← Angular app. Routes, navigation, theming.
        ↓ lazy-loads
  feature library             ← Angular library (projects/<lib>/src/app)
        ↑ uses                   Feature pages, inventory details,
  shared component library       device-panel, shared interface list.
                              ← Shared primitives: tables, form controls,
                                 360-shell, navigation primitives.
                              │
                              │  HTTP
                              ↓
  inventory REST service      ← Spring Boot, container-first.
  inventory collector         ← Spring Boot + gRPC.
  fault REST service          ← Spring Boot, container-first.
  fault assurance service     ← Dependent on internal deployment env.
```

The diagram encodes several structural facts the synthesis relies on elsewhere. On the legacy side: a framework repo sits below a cluster of feature repos and the chassis visualization repo, all depending on the framework. Local execution of the legacy side is not in the map's assumed affordances; reading is the primary mode of engagement, supplemented by a product VM for runtime observation.

On the modern side: a shell application lazy-loads a feature library, which in turn depends on a shared component library. Backend services sit behind an HTTP boundary. The deployment shape of the backend services is not uniform — some are container-first and straightforward to run locally for POC purposes; one depends on an internal deployment environment and is not comparably local-runnable. These asymmetries are not incidental; they shape which parts of the map are testable locally and which require environment access.

The diagram is not a system architecture diagram in the comprehensive sense. It is the map-of-maps that sits above the sub-surface tables, and it is drawn at the resolution that makes the sub-surface tables legible — no higher, no lower.

## 5. Observation Versus Conclusion, Sharpened

The synthesis is where Rule 10 does its heaviest work. The map is produced without source access. Every path it cites comes from a tree report of that path's repository, which is to say every path is a name at a location — not a read of the file's contents. What that file does, what that path means for implementation, what a downstream builder will find when they open it: these are conclusions that exceed the evidence. The synthesis names what it can honestly name and qualifies what it cannot.

The map's entries fall into three epistemic grades, and the artifact is written so that a reader can tell which grade an entry holds without having to reason it out.

### 5.1 Structural facts

A structural fact is a claim drawn directly from a tree report: a file with a specific name exists at a specific path in a specific repository. These claims are safe. They trace from the map, to the per-worker extraction that cited them, to the tree report the extraction absorbed. The traceability chain is preserved through the synthesis so that a later auditor can confirm any structural claim without independent investigation.

Example (paraphrased): "A file named `InventoryListView.js` exists in the assembly repository at a path under `inventory/js/`. The tree report records its line count at approximately eight thousand lines." This is a structural fact. It does not claim what the file does or how it is used. It claims only that the file exists at that path and that the tree report recorded that line count. A downstream reader can verify the claim by opening the tree report.

### 5.2 Name-suggested roles

A name-suggested role is an interpretation layered onto a structural fact. File names in production codebases usually carry semantic weight — a file called `InventoryListView.js` in a directory named `inventory/js/` is, on name evidence alone, most likely the primary view component for an inventory list. This interpretation is valuable. It lets the synthesis produce a usable map rather than a bare file enumeration. It is also not a conclusion. The file could be a deprecated prototype. It could be a wrapper around a different primary component. It could be dead code. The tree does not say.

Name-suggested roles are tagged in the map with phrasing that signals their status: "appears to," "likely," "on name evidence," "probably," "not yet verified in source." These phrasings are not hedging. They are the correct epistemic register for claims that rest on filename semantics alone. A reader consuming the map is expected to read them as specific: a "likely" entry is a hypothesis worth carrying into source, not an assertion safe to build on.

Worked example. Consider the Alarms-table entry on the modern side:

> Expandable-row detail candidate: `cw-epnm-fault/.../View360AlarmController.java`. Likely resolves the open question about expandable-row content source once read.

This entry carries three kinds of information. The structural fact: a file with that name exists at that path. The name-suggested role: a controller named `View360AlarmController` is, on name evidence, a plausible source for the content shown when a user expands a row on the Alarms table, because expanded-row detail patterns in similar codebases frequently share code with 360-view patterns. The qualifier: "likely resolves … once read." The "likely" and the "once read" are the epistemic register. The map is saying: this is a hypothesis worth carrying into source. It is not saying: the expandable-row content provably comes from this controller.

The same entry would be written differently if it were a conclusion. A concluded version would say "the expandable-row content is produced by this controller." The map does not say that, because the evidence does not support it.

### 5.3 Gaps

A gap is a statement about apparent absence. The legacy side appears to render a specific piece of functionality. A corresponding host or backend surface does not appear in the tree reports of the modern side. The synthesis flags this as a candidate gap.

The qualifier is critical. Absence in a tree does not prove absence in source. A feature may exist under a file name the synthesis did not recognize. It may live in a repository that was not included in the absorption scope. It may exist as a small subfolder inside a larger controller the tree only named at the directory level. The synthesis' gap flags are candidates, not confirmations. They deserve a source read before they rise to the level of a decision item.

The methodology treats gap candidates as a specific kind of claim, because a gap that a downstream phase acts on (by scoping backend work, by raising to a decision-maker) costs something. A false-positive gap — one that dissolves on source read — wastes the downstream cost. A false-negative gap — one the synthesis missed — defers a cost to a later phase where it is more expensive. The map names gap candidates specifically and flags them as source-read items, so the downstream phase knows which gap claims to verify first.

Worked example. The Chassis View sub-surface, on the legacy side, names an interactive hotspot layer (a cluster of named interaction files under a `hotspot/` directory covering port state, module state, and card detail behaviors) and a substantial backend service implementation. On the modern side, the tree reports do not surface a chassis-specific backend service. The synthesis flags this as a candidate gap: chassis interactivity may be part of the backend functionality that has not yet been ported. The entry is written with the caveat that absence in the tree is not proof of absence in source, and the downstream phase should confirm by reading modern-side inventory source before treating this as a committed gap.

### 5.4 The writing pattern

In practice, entries in the map follow a writing pattern that keeps the three grades distinguishable. A row cites paths (structural fact). A row's narrative prose, where it interprets the paths, uses qualifying phrasing (name-suggested role). Where a row names an apparent absence, a sentence below the row flags it as a candidate gap and names the source read that would confirm or dissolve it.

The pattern is not decorative. It is the mechanism by which a reader can consume a long map, build a mental model of which parts are load-bearing, and know which entries they can carry into planning and which they need to verify before acting.

## 6. Cross-Cutting Findings

The synthesis produces more than sub-surface maps. Working across the entire repository set surfaces observations that apply across the POC scope rather than to any single sub-surface. These cross-cutting findings are captured in dedicated sections of the map, at the bottom, because they do not belong inside any sub-surface's tables but are central to how the downstream phase approaches the work.

### 6.1 Where the classic code apparently mounts

On the modern side, the feature layer appears structured as a library consumed by a shell application. Under that structure, feature code lives inside the library. Mount-point registration — where a feature's routes become reachable URLs in the running application — happens in the shell. Navigation registration — where a feature's entries appear in the navigation tree — also happens in the shell, through a data-driven configuration file the shell reads at startup.

This shape has implications for where the classic rebuild most plausibly lives. A classic subfolder inside the feature library, sibling to existing feature directories, is the cleanest location. Routes for that subfolder register in the shell's route table. Navigation entries for that subfolder register in the shell's navigation configuration. The feature library packages, the shell consumes it, the whole assembly deploys. This matches the constraint established during discovery that the classic rebuild must build as part of the modern product rather than as a standalone artifact.

An alternative placement directly inside the shell is possible for parts of the Fault surface, because the runtime alarms UI in the existing modern product appears to live inside the shell rather than inside the feature library. This asymmetry between Inventory (feature-library-hosted) and Fault (shell-hosted) in the current modern product is observable from the tree but not explainable from the tree. The synthesis flags it as an asymmetry and defers placement of the classic fault surface to the downstream phase, noting that the placement decision likely depends on architectural intent not visible in names alone.

### 6.2 Shared-component reuse

The shared component library on the modern side holds a range of primitives relevant to the POC: table primitives, form primitives (input, select, checkbox, radio, datetime, modal, stepper), and a 360-shell directory that hosts device-360, interface-360, and related overlay patterns.

Not all primitives are equal for reuse under a classic theme. The synthesis identifies a pattern in the prefixes used by these primitives. Some carry a theme-agnostic prefix — they appear, on name evidence, to be intended as generic form controls adaptable to any theme. Others carry a prefix that corresponds to the current design language, suggesting they are coupled to the design-system-specific rendering and would need wrappers or extension to render under a classic look.

A reuse policy emerges from the synthesis at this cross-cutting level. For theme-neutral primitives, direct reuse is plausible; theming is applied via the variable layer without modifying the primitives. For design-system-coupled primitives, a classic variant is produced that reads theme variables and renders in a classic style. For table primitives specifically, a pluggable theme pattern appears to be the lowest-risk path: the modern codebase already contains evidence of a pluggable theme mechanism for a grid primitive, with named theme variants coexisting as peers. Adding a classic theme as a peer is a smaller undertaking than wrapping or forking the grid primitive, and it uses a precedent the codebase already establishes.

The policy is named in the map as a working hypothesis, not as an implementation commitment. The downstream phase decides by reading actual source and confirming that the pluggable pattern works as the names suggest.

### 6.3 Real-time update patterns

Both product families involve user-facing data that updates in real time — alarms, events, syslogs, and in some cases inventory state changes. How those updates reach the user matters for the classic rebuild, because the rebuild must either subscribe to the same updates the existing UX consumes or produce a UX that does not rely on live updates at all. The first is the target.

Structural signals on the legacy side suggest a push-based mechanism at least for some data types. The synthesis observes a filename in the assembly repo that includes a WebSocket-style naming convention for the syslog list view, and a notification-websocket pipeline in the fault repo. On name evidence, WebSocket is a probable pattern for real-time updates on the legacy side, at least for the data types where the naming surfaces.

On the modern side, the picture is less resolved. The tree reports show multiple messaging primitives in use — naming-level evidence of a message bus, an RPC mechanism, a message broker, and a legacy message-queue pattern. Which of these primitives drives user-facing live updates in the running modern product is not resolvable from structural data. Any of them could. A combination is possible. The synthesis flags this as a source-read item for the downstream phase and does not guess.

This is an example of an open question the synthesis refines without resolving. Before the synthesis, the open-questions document noted that the real-time update mechanism was undefined. After the synthesis, the open question is refined: on the legacy side, WebSocket is the probable mechanism on name evidence; on the modern side, the candidate primitives are named and the one that drives UI live updates is the specific item to resolve. The question is narrower, not closed.

### 6.4 Naming collisions

The synthesis surfaces a practical finding that a narrower worker-level extraction would not have: the word "classic" is not unclaimed in the modern codebase. A pair of stylesheet files in the shell use the term as a tier name in the current design system (light-classic, dark-classic). "Classic" already carries a meaning in the modern codebase, and that meaning is orthogonal to the classic-rebuild work.

Naming collisions of this sort are unimportant in theory and load-bearing in practice. If the classic rebuild uses the term "classic" as its directory name, class prefix, route name, or theme identifier without disambiguation, a downstream reader will routinely confuse rebuild artifacts with design-system-tier artifacts. The map flags the collision and recommends a distinct prefix for classic-rebuild work — something that names the legacy product family, not just "classic" — so that the rebuild's artifacts are distinguishable at a glance from artifacts that happen to share the word.

This is the kind of finding that sits naturally in the synthesis. No single worker-level extraction would surface it, because each worker sees only its own repository. The synthesis sees both sides and both uses of the word and observes the collision.

### 6.5 Deployment-shape asymmetries

On the modern side, the backend repositories do not share a deployment shape. Two of them appear container-first — they include container-build descriptors and local-profile configuration classes suggesting they are designed to run as self-contained services against a local development database. One of them appears to depend on an internal deployment environment; it lacks a container-build descriptor for its main service and includes helper scripts suggesting its development workflow assumes provisioned infrastructure.

This asymmetry shapes what is feasible for local POC testing. Parts of the modern backend can plausibly be run on a developer workstation; parts cannot. For sub-surfaces whose REST contract comes from the container-first repos, local end-to-end development is a live option. For sub-surfaces that depend on the environment-dependent repo — and the synthesis flags which ones appear to, based on which legacy-era twin classes are present in that repo — local development is constrained by access to that environment.

This is not a conclusion about how the downstream phase should work. It is a structural observation about what options are open. The downstream phase decides the operational model; the map names the constraints that decision sits within.

## 7. The Findings Log as the Synthesis' Running Memory

Alongside the cross-repo map, a findings log was maintained — a living document that recorded observations as they surfaced across the parallel absorption, resolved items once enough evidence accumulated to close them, and adjusted items that looked like conflicts but resolved into something else on inspection.

The log is a methodological artifact, not a draft of the map. Its role is to preserve the synthesis' reasoning trail so that a future consumer of the map — a downstream engineer, an auditor, a later contributor to the documentation — can see how the final map was arrived at. The map presents a cleaned and structured view. The log preserves the path that produced the map, including items that looked one way at first and another way after further absorption.

Several patterns appear in the log. Agent-status rows at the top track which workers have returned and which are still in flight, which enables the orchestrator to know when the map can be closed and when it cannot yet. Cross-cutting finding entries accumulate as observations that span more than one worker's scope — entries that, during the absorption phase, the orchestrator captured as they arose rather than deferring until all extractions were in. Per-worker findings sections hold each worker's most significant observations after its return, written at the level of the synthesis rather than at the level of the worker's own extraction.

A specific role of the log is handling apparent conflicts. Two workers will sometimes return observations that look contradictory at first read — one reports that a feature is present in repository A, another reports that the same feature is absent in repository B, and a naive reading concludes the feature is incompletely ported. On closer inspection, the feature lives only in repository A by design, repository B was never expected to host it, and the absence is not a gap but a structural fact about the product's layout. The log records both the initial observation and the resolution. Erasing the initial observation on resolution would be bad methodology — it hides the reasoning that produced the cleaned map, and a later reader who rediscovers the apparent conflict has to re-derive the resolution from scratch.

The log is preserved alongside the map in the scratch area. When the cross-repo map is consumed downstream, the log sits behind it as the auditing trail. The pattern is the same as the scratch-folder preservation from the handoff-package phase: intermediate artifacts are kept because they are the link between the cleaned output and the raw evidence.

## 8. Companion Primers

Some orientation material was produced as part of the synthesis phase that does not belong in the map itself but helps a reader interpret it. These primers are part of the synthesis output in the sense that their presence is necessary for the map to be legible to the intended reader, and their absence would leave the reader to reason through context the synthesis already has.

### 8.1 A primer on the multi-repository build ecosystem of the legacy product's language

The legacy product is built across several repositories whose build composes in a way specific to the legacy product's language and its Java build conventions. The modern product's build is differently structured, and the downstream phase's reader may be familiar with the modern product's shape but not with the legacy product's build ecosystem.

A primer was produced to answer the question "why are there multiple repositories for one product, and how do they compose into a deployable?" — at the level needed to orient a reader who will not become a full practitioner of that ecosystem during the POC. The primer covers archive formats (the unit a library ships as and the unit a deployable web application ships as), the reasons a large project in that language typically spans multiple repositories (shared framework reuse, build-ordering requirements), the build descriptors that encode the dependency graph, and the rough ordering in which the repositories compose.

The primer's role is functional, not comprehensive. It is not a tutorial on the legacy product's language or a complete reference on its build tooling. It is a bridge from the reader's known domain to the unfamiliar domain, focused narrowly on the concepts the reader will need to interpret the map's legacy-side entries without having to guess. The primer names, where appropriate, the parts of the legacy product's build that are not visible from the tree reports (for example, the top-level assembler that composes all the feature repositories into a deployable is not in the absorbed set; the primer names this explicitly so the reader is not confused by its absence from the map).

The primer is kept short. It is a starting-context document, not a reference manual. A reader who needs more depth than the primer provides is pointed at the artifacts or reads deeper into the legacy source directly.

### 8.2 A primer on the widget toolkit observed in the legacy framework repo

The handoff package's conversion-patterns reference, prepared earlier in the engagement, contained a widget-mapping table for the legacy product's general-purpose UI framework. The absorption surfaced a parallel widget-toolkit namespace in the legacy framework repo that was not in the conversion-patterns reference — a Cisco-internal widget toolkit layered on top of the general-purpose framework.

A companion primer was produced to give the downstream phase a factual starting catalog of files in this namespace: which widget directories exist, what primary files each contains, what line counts suggest about which widgets are substantial, and where theme-specific CSS files appear in relation to the widget code. The primer also notes observations the absorption surfaced across this toolkit — for example, that three generations of grid widget appear to coexist in the repo (a base grid primitive from the general-purpose framework, a wrapper around it, and the internal toolkit's table primitive), and that which generation the POC-scoped legacy screens actually instantiate is not resolvable from the tree.

The primer is deliberate in what it does not do. It does not propose cross-framework mappings from the internal toolkit's widgets to modern-product components. It does not extend the handoff package's widget-mapping table. It does not claim the internal toolkit is in POC scope or out of it. Proposing any of those would cross the observation-conclusion boundary: on tree-report evidence alone, the primer cannot responsibly say what the internal toolkit widgets do, how they differ from the general-framework equivalents, or what the right modern-product counterpart is. The primer lists the observed widgets, flags the open questions, and stops.

This restraint is the point. A primer that mapped the internal toolkit to modern counterparts would be a conclusion dressed as orientation. A primer that catalogs what the tree reports surface and names the open questions is orientation that preserves the downstream phase's authority over the actual mapping decisions.

### 8.3 Why primers are part of the synthesis

Primers like these are part of the synthesis because they make the map legible to a reader who does not already have the domain expertise the map assumes. A map of the legacy side's repositories is useless to a reader who does not know how the repositories compose; a map of the internal widget toolkit's files is useless to a reader who does not know a separate toolkit exists and what its relationship to the base framework is. The primers close the gap between what the map assumes and what the reader brings. Without them, the map's usefulness depends on context the reader may not have.

The primers are kept out of the map itself to preserve the map's focus. The map is a reference document consulted at a working desk. Primers are orientation documents read once to establish context. Conflating the two — embedding primers inline in the map — would dilute the map's utility as a reference. Separating them keeps both documents doing what they are designed to do.

## 9. The Artifact's Intended Use

The cross-repo map is starting context for the next phase of work. This statement is precise in what it says and, just as importantly, in what it does not say.

The map is a starting point for source-level investigation in the downstream phase. When the downstream phase opens actual source and begins reading, the map orients them — it points at the files most likely to be relevant, in the order most likely to be useful for building a first internal model, and with the open questions flagged for targeted attention.

The map is explicitly not three things.

First, it is **not a commitment about what will be touched**. Nothing in the map is committed in-scope for the POC. The downstream phase decides what is actually in scope after source reads. A path the map names may, on source read, turn out to be irrelevant — a deprecated version, a duplicate, dead code, a path replaced by a newer mechanism. A sub-surface the map covers in depth may, on source read, be simpler than the map's structural signals suggested. The map makes none of these calls. It surfaces candidates; the downstream phase commits.

Second, it is **not a conclusion about implementation**. The map does not prescribe an approach. It does not say "the classic Alarms table will be built this way." It says "these files appear to be involved in the current Alarms table; these host locations appear to be where a classic rebuild would mount; these shared components appear reusable." The translation from those observations to an implementation approach is a downstream decision that belongs in the downstream phase's authority. The synthesis' restraint here is not hedging; it is scope discipline.

Third, it is **not complete**. The map covers POC-scope surfaces. It does not attempt to map the full modern codebase, the full legacy codebase, or every repository in the absorption set. It maps the screens and cross-cutting concerns the POC commits to. Incidental repositories or paths outside POC scope are noted only briefly in the structural reports and are not mapped in detail. A reader who expects an encyclopedic index will find the map limited in exactly the ways it was designed to be limited.

Stating these non-uses plainly is part of the artifact. Consumers of the map who would otherwise treat it as a commitment, as a prescription, or as a comprehensive reference would consume it incorrectly. The map's preface names the non-uses so the artifact is used as intended.

## 10. Synthesis Under Scope Discipline

The synthesis is run with explicit scope walls. Only POC-relevant paths surface into the map in detail. Incidental repositories or paths outside POC scope are noted briefly in the structural reports but are not mapped, not analyzed, and not cross-referenced to POC concerns.

This discipline matters because a synthesis without scope walls devolves. Each worker's extraction contains material that is not POC-scoped — repositories exist for reasons unrelated to the POC, directories inside POC-relevant repositories hold code for other purposes, and the tree reports name files the POC will never touch. If the synthesis tried to integrate all of that material into the map, the map would become an index of the repository set rather than a POC-scoped reference. An index of the repository set is not what the downstream phase needs. The downstream phase needs to know, for the screens and sub-surfaces in POC scope, where the relevant artifacts apparently live. Everything else is noise at the resolution the map is intended for.

The scope walls are declared at the top of the map and enforced at the synthesis level. When a worker surfaces an extraction that includes substantial material outside POC scope, the synthesis extracts only the POC-relevant portions into the map and leaves the rest in the worker's extraction for anyone who wants it. The worker's extractions are preserved unchanged; the map is the filtered view.

A related scope discipline is the restraint against cross-cutting analyses that do not serve the POC. A structural sweep across ten repositories could produce any number of interesting observations — license consistency patterns, naming convention variations, code organization comparisons between the two product families — that are not directly useful to the POC. The synthesis does not produce those observations. It produces the observations that serve the map's intended use, and it stops.

This restraint is part of why the map is useful. A reader consulting the map can trust that every entry is there because it bears on POC scope. A map that blended POC-scoped and incidentally-interesting observations would force the reader to filter at every read; the synthesis does the filtering once, so the reader does not have to.

## 11. Working Conventions During Synthesis

A set of working conventions governs the orchestrating thread during synthesis. They are disciplines, not rules of presentation, and they shape what ends up in the map and what does not.

**Traceability through the chain.** Every structural claim in the map traces to a specific worker extraction, which traces to a specific tree report, which names a specific file in a specific repository. Traceability is preserved through the chain, so that any claim a downstream reader questions can be followed back to its evidence. The scratch folder that holds the worker extractions is preserved alongside the map; the tree reports that fed the workers are preserved in their own location. The chain does not break.

**Suggestions are tagged explicitly.** Phrasings like "appears to," "likely," "on name evidence," "not yet verified in source" are used where an entry rises above structural fact into name-suggested role. These phrasings are not filler. They are the correct register for the underlying claim, and reading them as filler defeats their purpose. The synthesis uses them deliberately and consistently.

**Open questions resolved by the structural pass are flagged clearly.** When the structural artifact makes a previously unresolved open question suddenly obvious, the resolution is flagged. But resolution by structure typically leaves a last-mile source-read verification. A "resolved" open question becomes, in practice, a "source-read item": the answer looks obvious from the tree, but the downstream phase still reads source before acting. The synthesis captures both the apparent resolution and the verification step. The open-questions document inherits this refinement: the status moves from "open" to "resolved subject to source-read," not from "open" to "closed."

**Escalation flags are separated from the map.** Some synthesis findings want a decision from a party outside the downstream phase's authority. A commercial question about scope boundary, a stakeholder decision about a specific screen's inclusion, a compliance question about a specific backend service's treatment — these are not findings the downstream phase can act on alone. They are escalation flags. The synthesis keeps them out of the map proper so the map remains a clean technical reference. Escalation material lives in a separate document that the next chapter's flag-surfacing process picks up.

**Orchestrator-level judgment.** The synthesis is not delegated, and the reason is the same reason the handoff-package synthesis was not delegated: judgment about what belongs in the map, what qualifies as a candidate gap versus a structural observation, what rises to the level of an escalation flag, and how to phrase the epistemic qualifier on each entry — all of these judgments require the full context the orchestrating thread carries. Delegating the synthesis to workers would produce a mosaic of narrow-context judgments, each correct within its aperture and inconsistent across the set. The map would lose coherence. Keeping the synthesis with the orchestrator preserves coherence and keeps the judgment register consistent across the document.

**Planning in files, not in stream.** The map, the findings log, and the companion primers are markdown files written under the scratch area. Orchestration commentary about what to investigate next, what a worker's return implies, or how an observation should be framed is captured in the log or directly into the map, not left as transient stream-of-orchestration that dissipates. The principle from earlier phases — substantive design and synthesis go into files — holds through this phase.

## 12. Outcome

The phase produces a cross-repository map organized by POC scope, a findings log that preserves the synthesis' reasoning trail, and companion primers that make the map legible to the intended downstream reader. All three artifacts live in the scratch area alongside the per-worker extractions that fed them. Every structural claim in the map traces to a per-worker extraction, which traces to a tree report. Every suggestion is tagged with epistemic qualifiers that register its confidence grade. Every gap candidate is flagged as a source-read item rather than a confirmed gap. Every cross-cutting finding is captured in the map's dedicated sections rather than buried inside a sub-surface entry that would not do it justice.

The downstream phase, opening against actual source for the first time, has starting context. It knows, for each screen and sub-surface in POC scope, which files are candidates for first reading, which open questions have structural signals that point at resolutions worth verifying, which gap candidates want source-read confirmation, and which cross-cutting decisions will need to be made after source reading. The map does not tell the downstream phase what to build. It tells the downstream phase where to look first.

---

The synthesis produced the map, and the map surfaced findings. Some of those findings are structural observations that the downstream phase will carry into source reading. Some are candidate gaps that want a decision from a party outside the downstream phase's authority. Some are naming collisions or deployment-shape asymmetries that shape the operating model for the POC work. The next chapter addresses what happens when some of the synthesis' findings want decisions — how they are surfaced, how they are routed, and how the engagement's scope-and-policy review absorbs them without letting them contaminate the map's technical register.
