# EPNM Forge Skill — Design References to Author

**Audience:** Claude orchestrator session on the Cisco-issued machine.
**Date:** 2026-04-26
**Purpose:** Structure and authoring guidance for the substantive design references the EPNM forge skill must carry. These are different from the workflow/operational references covered in file 06.

---

## What design references are and why they matter

A forge skill that is going to convert code from one stack to another needs to encode "what good looks like" for both the source stack and the target stack. Without that, the skill produces output that compiles, passes tests, and matches the issue description — but doesn't match the patterns the rest of the codebase uses, the conventions the team enforces in code review, or the architectural intent of the modern stack.

DjangoForge encodes this implicitly through its references and through the agent prompts. For a Django-to-Django evolution context that is enough. For an EPNM-to-EMS conversion context, where the source stack and target stack are different in nearly every dimension, implicit encoding is not enough. The skill needs explicit design references that the implementation phases consult.

These references are NOT something the other Claude session can write for you. They require reading the actual EPNM and EMS code. You are the only session with that access. Author them by walking the codebases.

---

## The four design references

### 1. EPNM source stack reference

**File:** `references/source_stack_epnm.md`

**Purpose:** Encode what EPNM actually IS so the skill knows what it is converting from. Capture the patterns, idioms, structural conventions, and architectural quirks of the legacy stack so the skill can recognize them in the source code and translate them faithfully.

**What to capture (read the code, then write):**

- **Architectural overview.** Java Swing fat-client elements vs. Dojo 1.x web-tier elements vs. Java monolith backend. Map each EPNM repo to which architectural tier it belongs to. The Set 08 research file `cisco/epnm_ems/research/08_research_epnm_legacy_stack_2026-04-07.md` is a starting point but is Dojo-focused; verify against actual code and add what is missing about Swing.
- **Java Swing patterns** — how the fat-client UI is structured if Swing is part of EPNM. Component hierarchies, event dispatch, threading conventions (EDT discipline), look-and-feel customization, JTable patterns, dialog patterns. Pull representative code excerpts and annotate.
- **Dojo 1.x patterns** — Dijit widget hierarchies, AMD module structure, declarative vs. programmatic widget instantiation, pub/sub patterns, store/data-binding patterns, lifecycle hooks. Pull representative code excerpts.
- **Java monolith backend patterns** — controller/service/DAO conventions, transaction boundaries, exception-handling patterns, logging conventions, configuration loading.
- **Oracle DB integration** — connection management, ORM (or lack of), query construction patterns, schema versioning approach.
- **SNMP/CLI device integration** — how device communication is structured. Polling vs. event-driven patterns. Connection pooling. Error handling.
- **Cross-cutting conventions** — naming (classes, methods, variables, files), file/package structure, directory layout, internationalization, dependency injection (Spring? hand-rolled?), build system (Maven/Ant/Gradle).
- **Anti-patterns observed during the mapping pass.** Per Set 09, the same things are done multiple ways in EMS, and that debt was carried over from EPNM. Document the EPNM-side instances of those inconsistencies. Bookmarks behavior is one example. Column-handling-in-tables is another. Whatever you find during the read.

**Format:** Markdown. Code excerpts in fenced blocks, tagged with the source repo and file path. Each pattern section ends with a "translation notes" line that says how this pattern maps to its EMS equivalent — that is the bridge into the conversion patterns reference.

**Length:** Substantive. This is not a README. Plan for ~30 to 100 pages of markdown depending on how much surface area the skill needs to handle. The DjangoForge `phase_requirements.md` is roughly an analog in terms of substance density, though it covers a different domain.

### 2. EMS target stack reference

**File:** `references/target_stack_ems.md`

**Purpose:** Encode what EMS IS — what good code looks like in the target. The skill produces code that lands in EMS. It must match the conventions already there.

**What to capture:**

- **Architectural overview.** Shell app architecture (Infra UI → Common UI → EMS UI nested layers). Where the classic-view bolt-on packages fit. How features are decomposed across repos.
- **Angular 21 patterns** — standalone components, signals, computed signals, effects, the reactivity model. Routing patterns, module/standalone migration state. Forms (template-driven vs. reactive). Lazy loading. Dependency injection idioms (`inject()` vs. constructor). HTTP service patterns.
- **Harbor/Magnetic design system usage** — component library inventory, theming, custom-component conventions, how to extend or wrap library components, accessibility requirements.
- **Spring Boot patterns** — controller conventions, service patterns, repository/Spring Data usage, configuration (application.yml conventions, profiles), exception handlers, validation, security, observability.
- **Go services patterns** — where Go is used (per Set 07, device management backend), conventions for handlers, structuring of business logic, dependency-management approach, error handling, gRPC vs. REST conventions.
- **PostgreSQL patterns** — schema conventions, migration tooling, connection pool configuration, query patterns, test data setup.
- **Microservices patterns** — service-to-service communication, contract management, versioning, deployment topology if observable from code, observability hooks.
- **Cross-cutting conventions** — naming, formatting (Prettier? Spotless? gofmt?), test structure (where tests live, naming, frameworks), commit message conventions if observable in `git log`, branch protection rules if visible.
- **Code quality enforcement** — linters configured, CI checks, pre-commit hooks. The skill needs to run the same checks the team runs.

**Format:** Same as the EPNM reference. Code excerpts with paths. Translation-notes lines pointing back to the EPNM reference's equivalent patterns.

**Length:** Substantive. This is the target stack — slightly more depth here than the source stack is appropriate, because more new code lands here.

### 3. Conversion patterns reference

**File:** `references/conversion_patterns.md`

**Purpose:** The bridge between EPNM and EMS. For each EPNM pattern, the corresponding EMS pattern that the skill should produce. The Set 08 research file `cisco/epnm_ems/research/08_research_conversion_patterns_2026-04-07.md` is a strong starting point — copy it into the skill as a seed and extend it with what you find in the actual code.

**What to capture:**

- **Widget mapping table.** Dijit widget → Angular component or Harbor/Magnetic equivalent. Per-row, with notes on behavioral differences and known gotchas.
- **Module mapping.** AMD `define()` modules → ES6 standalone components or NgModules. With code examples on both sides.
- **Data binding mapping.** Dojo `watch()` and `set()` → Angular signals/observables/forms. With examples.
- **Event handling mapping.** Dojo pub/sub → Angular RxJS subjects/Observables/services. With examples.
- **Lifecycle mapping.** Dijit `postCreate`, `startup`, `destroy` → Angular `ngOnInit`, `ngAfterViewInit`, `ngOnDestroy`. With examples.
- **State management mapping.** Dojo stores → Angular services + signals/RxJS. With examples.
- **API integration mapping.** Direct HTTP/Dojo XHR → Angular HTTP service patterns. Note where the EMS modern UI already has services that the classic UI bolt-on can reuse vs. where new services are needed.
- **Theme toggle architecture.** How the classic-view toggle works mechanically: CSS custom properties, ThemeService, route-level vs. screen-level toggling, persisting user preference. Set 08 has a starting design — verify against what you actually implement.
- **Java Swing → Angular mapping.** If EPNM has Swing components that need conversion (vs. just Dojo components), document the patterns: Swing event listeners → Angular event bindings; SwingWorker threading → RxJS observables; Swing layout managers → CSS flex/grid; Swing models → Angular reactive forms or signal-backed state. With examples.
- **Backend conversion mapping.** Java monolith methods → Spring Boot endpoints (or reuse existing). Where to add, where to leave alone. Per Set 07, ~80% of backend is already in EMS — focus on the gap-bridging patterns.
- **Per-screen migration checklist.** A reproducible checklist the skill applies to each screen conversion. Pre-flight reads, conversion steps, post-conversion verification.

**Format:** Tables for mapping rows, fenced code blocks for examples, headers per pattern category.

**Length:** Substantive. This is arguably the most-used reference during implementation phases.

### 4. Best practices and anti-patterns

**File:** `references/best_practices_and_anti_patterns.md`

**Purpose:** Capture the things that are not "patterns" per se but that distinguish good code from passable code in this engagement. What the India team will praise vs. what they will flag in review.

**What to capture:**

- **Best practices**:
  - Audit-ready commit pattern (cross-reference to `references/audit_ready_commit_pattern.md`).
  - Same-backend discipline (toggle never spawns new backends).
  - Bolt-on, not invasive (no modification of existing EMS Angular code).
  - Out-of-scope discipline (no DPM, no debt fixes, no new screens, no bookmarks behavior change).
  - Test parity with the modern UI (the classic UI's tests should mirror the modern UI's tests where applicable).
  - Resource consciousness (per Guhan's memory/load review — bundle size, render performance, memory leaks).
  - Documentation discipline (in-line decision rationales authored by Colin, not generated; agent-generated content tagged distinctly).
- **Anti-patterns**:
  - Touching EMS Angular code to "fix" the bolt-on integration. The bolt-on must be self-sufficient.
  - Modifying backend services or contracts. Toggle hits the same backend always.
  - Making architectural-debt fixes opportunistically. Note them, do not silently change them.
  - Expanding scope into out-of-POC areas (DPM, additional screens, bookmarks behavior change).
  - Generating documentation that purports to be Colin's reasoning. Human-in-the-loop content is human-authored.
  - Squashing or rebasing commits in ways that destroy attribution or rationale tags.
  - Forward-leaning claims in PR descriptions or commit messages. The India team will be reviewing — what is in the artifacts is what is true. (See file 06 hard rule on honest state.)
- **Stack-specific anti-patterns** — pull from what you observe during the codebase walk:
  - Angular: subscriptions without unsubscribe, signals used as plain variables, change-detection thrash, monolithic components, `any` types.
  - Spring Boot: controller-level transaction management, business logic in DAOs, exception swallowing, missing validation.
  - Go: goroutine leaks, unhandled errors, naked returns, interface bloat.
  - Postgres: N+1 query patterns, missing indexes on query paths the conversion uses, schema migrations applied without coordination.
  - Java Swing (if relevant): blocking the EDT, swing components used outside the EDT, memory retention via component listeners.

**Format:** Bullet lists for the rules; code excerpts where an anti-pattern is best illustrated. Each rule has a "why" line that ties to a real concern (audit, performance, scope, customer-commitment risk).

**Length:** Substantive but tighter than the stack references. ~10 to 30 pages depending on how much you observe.

---

## Authoring approach

Walk the codebases in this order:

1. **EMS first.** It is the target stack. Read the modern code first to understand what good looks like in this engagement. The Harbor/Magnetic design system, Angular 21 conventions, and Spring Boot patterns are the foundation everything else maps to. Read top-down: shell app → common UI → feature pages.
2. **EPNM second.** Read the source stack with translation in mind. For each pattern you encounter, ask "what is the EMS equivalent" — that conversion is what the skill produces.
3. **Cross-reference the gap analysis.** The 14-repo mapping (per `cisco/epnm_ems/research/09_meeting_full_system_mapping_2026-04-24.md` and the ~250 generated files) already encodes the bidirectional gaps. Use that as the reading list — every gap noted there is something the design references must address.
4. **Sample, don't exhaustively read.** Pick representative examples per pattern. Code excerpts in the references should be illustrative, not encyclopedic. The skill needs to recognize the pattern, not memorize every instance.
5. **Validate by writing one PR end-to-end.** The first issue the skill processes will reveal gaps in the design references. Update them after the first run.

---

## Self-containment

Like all references in this skill, the design references live in `references/` inside the skill folder. They are NOT symlinks or copies of `cisco/epnm_ems/research/08_research_*.md` files. The research files are seed material — copy what is useful into the skill's references and extend, do not link.

When the engagement-side research library updates with new findings (new bridge documents, new pricing decisions, new architectural notes), the skill's design references may need to be updated too. That is a manual sync, owned by whoever updates the skill — not an automatic pull.

---

## What good looks like

A well-written design reference set in this skill should let a future Claude session, opening the skill cold, answer:

- "When the source code is doing X in EPNM, what is the EMS equivalent I should produce?"
- "What does idiomatic Angular 21 look like in this codebase, specifically?"
- "What patterns in the modern code are stable conventions, and what are inconsistencies the team is tolerating but not endorsing?"
- "What would the India team flag in code review that is not flagged by the linter?"

If the references can answer those four questions for any in-scope screen or backend element, they are doing their job. If they only restate generic Angular/Spring Boot best practices, they are not substantive enough.

---

## When in doubt

The codebase is authoritative. If the design reference says one thing and the code does another, update the reference. If the reference says one thing and Colin's stated direction in the engagement research library says another, the engagement research wins (those are the active engagement constraints). If the reference says one thing and a generic best-practices source online says another, the codebase wins (because we are matching the team's conventions, not the world's).

The four hard constraints (agentic-label requirement, bolt-on rule, same-backend rule, audit-ready commit pattern) are the only things that do not flex. Everything else is shaped by what you find in the code.
