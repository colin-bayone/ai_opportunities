# Chapter 4 — Codebase Analysis Through Structural Artifacts

## 1. From Narrative Context to Structural Evidence

The handoff package, assembled in the phase documented in the previous chapter, carried the full inheritance of what the discovery conversations had said about the codebase. It named the two products, identified the stacks each product sat on, listed the repositories that stakeholders had called out by name in meetings, restated the module-system and component-model specifics as they had been described verbally, and traced the architectural layering of the modern frontend as the customer's engineers had drawn it on screen during the walkthrough. Each claim in the handoff package traced to a specific transcript or research file.

What the handoff package did not carry was the codebase itself. Every statement it made about what exists in a repository was a statement repeated from a conversation in which someone had described what exists in that repository. A reader could learn from the handoff that the modern frontend is organized as a three-layer shell-app model, that the shell lives in a specific repository and the feature pages live in another, and that the legacy framework sits in yet another — but the reader could not, from the handoff alone, open a directory and see what files are present or confirm that the repository layout matched the verbal account. The handoff was narrative context. It was grounded in source material, but the source material it was grounded in was itself verbal and written account, not structural inspection.

This distinction is the hinge on which the next phase of the engagement turned. Before any substantive downstream investigation could proceed — before anyone could do cross-repository mapping, before anyone could look for where in-scope functionality appeared to live in source, before anyone could reason about conversion-ready subsets of the legacy code — an additional layer of context was required. That layer is the subject of this chapter: a set of structural artifacts that captured what each repository actually contained, at the level of directories and file names, without making any claim about what the source inside those files does.

Structural evidence is distinct from source understanding, and the distinction is treated as load-bearing throughout this chapter. A tree report that records a file named `InventoryListView.js` at a given path under a given repository is evidence that such a file exists at such a path. It is not evidence that the file renders the inventory list screen, nor that it binds to a particular data store, nor that it is a Dijit widget of the form the conversion approach assumes. The name suggests. The source would confirm. The distinction matters methodologically because every claim the rest of the methodology makes about the codebase sits on one of these two kinds of evidence, and conflating them would mask uncertainty that has to remain visible. The rules-of-engagement for the documentation set name this as the observation-versus-conclusion discipline; this chapter is the one where that discipline is operationalized.

## 2. Why Structural Artifacts, Not Source Crawls

Two reasons pushed the phase toward structural artifacts rather than a bulk source read.

The first reason is scale. The engagement spans many repositories across two product families, in multiple languages, with at least one repository family that is deep in legacy markup formats (JavaServer Pages, declarative Dojo markup, vendor schema files, Management Information Base files) and at least one that is dense in modern TypeScript and SCSS. An exhaustive cover-to-cover source read of every repository would consume any single reading phase that tried to perform it, and the read would still only produce a fraction of the total content in an absorbable form. Structural artifacts sidestep that problem: they capture the shape of each repository in a form that is compact enough to produce in a single sweep and can be re-read selectively thereafter.

The second reason is epistemic, and it is the reason the methodology actively preferred structural artifacts over a source crawl rather than merely accepting them as a budget-forced compromise. Structural artifacts have a different epistemic weight than source reads. A reader absorbing a tree report is absorbing a list of facts at the structural level — files exist, directories exist, an extension profile exists, a nesting depth exists. Absorbing those facts does not require making inferential leaps about what any single file does. A reader absorbing a file's source, by contrast, is building a model of behavior, and the act of building that model is where misattribution and overconfidence enter. By staging structural absorption before any source absorption, the methodology produces a factual map that downstream work can stand on without that map itself being a source of false confidence.

The phase therefore produced a repository analysis bundle. The bundle records structural facts about every repository in both product families, holds those facts in both human-readable and machine-readable forms, and locates them in a layout that is navigable as orientation material and durable as an audit substrate. The rest of this chapter documents the bundle's composition, the discipline governing claims drawn from it, and the role it plays in the phases that follow.

## 3. The Bundle's Composition

The bundle is organized around two product families and a cross-family view. The top level contains a README orienting a reader to the bundle, three family-level folders (one for EPNM, one for EMS-CNC, one combined), and a repository-inventory folder. Each family-level folder contains a consolidated report describing the repositories in that family, a machine-readable summary covering the same material, and a subfolder holding one tree report per repository in that family. The combined family-level folder holds a cross-family consolidated report and the corresponding machine-readable summary. The repository-inventory folder holds a human-readable inventory document and its machine-readable twin.

The layout is as follows:

```
REPO/
├── README.md
├── EPNM/
│   ├── consolidated_report.md
│   ├── summary.json
│   └── tree-reports/
│       ├── pf-framework_tree_report.md
│       ├── wireless_tree_report.md
│       ├── assembly_tree_report.md
│       ├── inventory_tree_report.md
│       ├── ce-content-device-packs_tree_report.md
│       ├── chassisview_tree_report.md
│       └── fault_tree_report.md
├── EMS-CNC/
│   ├── consolidated_report.md
│   ├── summary.json
│   └── tree-reports/
│       ├── infra-ui_tree_report.md
│       ├── common-ui_tree_report.md
│       ├── unified-ems-ui_tree_report.md
│       ├── cw-inventory_tree_report.md
│       ├── cw-inventory-collector_tree_report.md
│       ├── ems-assurance_tree_report.md
│       └── cw-epnm-fault_tree_report.md
├── EPNM-EMS-CNC/
│   ├── consolidated_report.md
│   └── summary.json
└── repo-inventory/
    ├── repository_inventory.md
    └── repository_inventory.json
```

Several aspects of the layout carry methodological intent.

The README is the entry point. It names what the bundle is (a handoff bundle collecting the current repository analysis artifacts), where to start (the combined consolidated report and the inventory document are the two named starting points), how the folders relate to each other, and which files are present at each path. It is short by design — the reader is expected to move quickly from the README into one of the orientation artifacts — but it is complete, in that every file in the bundle is named and assigned a role.

The two family-level folders mirror each other structurally. Each carries a consolidated report, a machine-readable summary, and a per-repository tree-reports subfolder. The mirroring is deliberate: a reader orienting to one family and then moving to the other encounters the same shape of material in the same layout, which reduces the cognitive cost of navigating between them. It also makes programmatic processing of the bundle simpler, since the per-family structure is regular.

The cross-family folder (named `EPNM-EMS-CNC` in the bundle) holds the combined consolidated report and the combined summary. The combined artifacts are not the sum of the family artifacts stitched together. They present the fourteen repositories side-by-side, with a shared family column, so that cross-family comparisons are possible in a single document without the reader having to hold two separate family reports in parallel.

The repository-inventory folder is separated from the family folders because its role is categorically different. The family folders and the cross-family folder answer structural questions about what each repository contains. The inventory answers a prior question: which repositories are in the bundle, where they live on disk, where they came from, and which of them were freshly cloned versus pre-existing. It is the first file a reader consults when orienting; the family folders are consulted after. That difference in consultation order is preserved by the difference in folder placement.

## 4. The Repository Inventory

The repository inventory is the document that answers "what do I have." It enumerates the repositories present in the bundle, groups them by family and area, records each repository's current on-disk path, its desired organization path, and the origin it was cloned from, and notes whether each repository was freshly cloned in the current pass or pre-existing in the environment. It also records an organization model — a target folder layout under each family — that captures the steady-state organization the inventory is progressing toward, even where a particular repository has not yet been moved to its target location.

The fourteen repositories are distributed between the two product families as follows.

**EPNM family (seven repositories).** The EPNM family is organized into four areas:

- *Core Framework.* Two repositories, `pf-framework` and `wireless`. The inventory names these as the core EPNM framework repositories and situates them under a `core-framework/` directory in the target organization.
- *Inventory.* Three repositories, `assembly`, `inventory`, and `ce-content-device-packs`. The handoff documents identify the assembly repository as the location of the inventory UI screens and the fault management UI; `inventory` and `ce-content-device-packs` are named in the inventory under the inventory area without further functional narration.
- *Chassis.* One repository, `chassisview`. The handoff documents identify this repository as the chassis visualization component — the physical device rendering seen on the Device Details screen.
- *Fault.* One repository, `fault`. The handoff documents identify fault management as spanning both backend and frontend.

**EMS-CNC family (seven repositories).** The EMS-CNC family is organized into three areas:

- *Frontend.* Three repositories, `infra-ui`, `common-ui`, and `unified-ems-ui`. The handoff documents describe the modern frontend as a three-layer shell-app: the infra-ui repository hosts the shell, `common-ui` holds the shared reusable components, and `unified-ems-ui` holds the feature-specific EMS pages.
- *Backend Inventory.* Two repositories, `cw-inventory` and `cw-inventory-collector`.
- *Backend Fault/Assurance.* Two repositories, `ems-assurance` and `cw-epnm-fault`.

The inventory distinguishes ten repositories that were newly cloned from four that were pre-existing in the environment. Three of the pre-existing repositories (`common-ui`, `unified-ems-ui`, and `cw-inventory-collector`) still sit at the top level of the programming workspace at the time the inventory was produced, with the inventory's target column showing the intended steady-state location under the EMS-CNC family folder. One pre-existing repository (`cw-inventory`) was intentionally left in place because it was the active workspace for the current work; the inventory records the intent to relocate it later, once it is no longer the active workspace.

The inventory also records two branch-context facts that are specifically called out as not enforced by the clone layout. The fault repository in the EPNM family carries distinct branches corresponding to the legacy-branded stream and the modern-branded stream. The `ems-assurance` repository in the EMS-CNC family carries the same two branches. The inventory's note is a structural observation: the same repository can therefore serve either family depending on which branch is checked out, and the bundle's clone-layout organization does not itself disambiguate the branch context. The implication — that fault-related work needs to track the branch as carefully as the repository — is a conclusion that follows from the structural fact, but the structural fact is what the inventory carries.

Finally, the inventory names the organization model alongside the current state. The model is a target folder layout per family; the current paths of pre-existing repositories are shown alongside their target paths so that a reader orienting to the bundle can see which relocations remain. The inventory lists a set of suggested next moves for those relocations in its closing section. These are structural housekeeping observations, not scope commitments.

## 5. The Consolidated Reports

Each family-level folder holds a consolidated report, and the cross-family folder holds a combined consolidated report that spans both families. The reports are compact structural summaries designed for orientation, not for deep technical analysis.

A consolidated report carries, for each repository in its scope:

- The repository name and the product family it belongs to.
- The repository's on-disk root path.
- A counted footprint — the count of text-like files that were included in line-count computations, and the corresponding raw line total across those files.
- A separate Java footprint figure — the count of Java files and the corresponding raw line total. Java is broken out because both product families have substantive Java content at different layers, and the Java footprint is a useful orientation signal for where legacy and modern backend code lives.
- A list of ignored file extensions with per-extension file counts. Ignored extensions are binary, near-binary, or image-and-asset extensions whose contents are not counted as text lines.
- A count of binary files that were skipped during the text-counting pass.
- A tree-report path pointing at the repository's tree report within the bundle.
- A ranking of dominant file types by raw line count.
- A ranking of largest file-type groups by file count.

The report's opening section is a portfolio-level overview: how many repositories are in the family, how many files are discovered across them, how many files are counted, and how many raw lines are counted in total. The family-breakdown section (most visible in the combined report) presents the same figures grouped by family so that a reader can compare family-level footprints at a glance.

The reports describe the bundle's own structural reality. They do not claim to explain what the code does. The dominant file types by line count tell a reader which file types carry most of the textual volume in each repository, which is useful for orientation — a repository dominated by `.ts` files with `.html` and `.scss` beside them has a different shape than a repository dominated by `.jsp` and `.my` files with `.java` beside them — but the reports stop at that shape. What the `.ts` files do, what the `.jsp` files do, is not the consolidated report's concern.

## 6. Human-Readable and Machine-Readable Twins

Every human-readable artifact in the bundle has a machine-readable twin. Each family-level consolidated report (`consolidated_report.md`) is accompanied by a family-level summary (`summary.json`). The cross-family consolidated report is accompanied by a cross-family summary. The inventory document (`repository_inventory.md`) is accompanied by an inventory summary (`repository_inventory.json`).

The rationale for producing both forms is that they serve different consumption patterns and neither dominates the other.

Human-readable forms are optimized for direct absorption by a human reader arriving at the bundle. A markdown report is readable in any editor, renders well in a browser, supports tables and headings, and is structured for the eye to scan. A reader orienting to the bundle opens the README, the inventory, and the consolidated report as markdown; the markdown is what carries them through.

Machine-readable forms are optimized for downstream programmatic consumption. A JSON summary can be loaded by any tooling that needs to iterate over the repository list, cross-check a count against a master list, feed a structured inventory into a downstream workflow, or verify that every expected repository is present in the bundle before proceeding. The machine-readable twin carries the same information the markdown does, in a structure that is stable, indexable, and scriptable.

The methodological point is that a structural artifact intended to be a durable substrate for downstream work should not assume only one consumption mode. A reader consumes the markdown; a downstream automated check consumes the JSON; both are legitimate. The bundle commits to both forms up front so that neither consumption pattern has to reconstruct the other.

## 7. The Tree Reports

Each repository in the bundle has a dedicated tree report, stored under the tree-reports subfolder of its family folder. A tree report is a structured listing of the repository's directory hierarchy with per-directory annotations.

Tree reports range widely in size by repository. Some repositories produce small, focused tree reports — repositories with shallow directory structures, a limited set of file types, or a single functional purpose tend to fit in a tree report that a single reader can absorb end-to-end in one pass. Other repositories produce very large tree reports. Framework repositories, repositories that carry heavy Management Information Base content, repositories that carry generated schema files, and repositories that carry substantial JavaServer Pages surfaces tend to produce tree reports of substantial size.

The size range is an important framing point. Large tree reports are not intended to be read end-to-end by a single human in one pass. Their role is different. A large tree report is the substrate for a parallel-absorption pattern — the one documented in the next chapter — in which the tree report is partitioned across parallel workers, each of which absorbs one section, and the aggregated output is consumed by the orchestrating thread. The bundle's tree reports are produced at whatever size the underlying repositories dictate; the methodology for absorbing them is what scales to the size the tree reports happen to be.

A tree report is not a file-content report. It does not open any file. It names files by their path, groups them by directory, and carries structural annotations at the directory level. It answers "what exists" at repository scope. It does not answer "what does this code do." The downstream methodology takes the tree reports as input to the next layer of analysis; it does not treat them as a substitute for source reading where source reading is actually required.

## 8. Observation Versus Conclusion, Operationally

The observation-versus-conclusion discipline named in the authoring rules applies throughout the documentation set, but this is the chapter where it requires the most operational specificity. Structural artifacts are powerful precisely because they are grounded in facts about what exists. Structural artifacts are also dangerous precisely because the facts they carry are easy to over-interpret. A file name suggests a purpose; the suggestion is not the same as the purpose. The discipline applied to the bundle distinguishes three classes of statements that a structural artifact can support.

**Class 1. Pure structural facts.** These are statements that the artifact fully supports on its own, with no inference beyond the content of the artifact. Examples:

- *"The `pf-framework` repository contains a subdirectory at path X."* This is a tree-report fact.
- *"In the `wireless` repository, `.java` is the dominant file type by raw line count among counted files."* This is a consolidated-report fact.
- *"The `infra-ui` repository is in the EMS-CNC family, in the Frontend area, and was newly cloned in the current pass."* This is an inventory fact.
- *"The combined bundle covers fourteen repositories split across two product families, seven in each."* This is a cross-family consolidated-report fact.

Statements of this class are safe to cite directly. They appear in the bundle as-written; a reader can verify them against the artifact without reasoning beyond it.

**Class 2. Name-based suggestion.** These are statements in which a file or directory name is cited as evidence of purpose, with the interpretation explicitly tagged as likely or apparent rather than stated as fact. A file named `ChassisViewServiceImpl.java` under a directory named `chassis` in a repository named `chassisview` is strong contextual evidence that the file is a chassis-view-related backend service implementation — but the strength of the evidence is a contextual likelihood, not a confirmation. The discipline is to cite the name, to state the interpretation, and to tag the interpretation explicitly: "a file named `ChassisViewServiceImpl.java` is apparently a backend service implementation for the chassis view," or "the presence of a directory path like `.../inventory/list/...` suggests an inventory-list surface." The tag is the rule-10 safeguard: it signals that the statement is an interpretation of a structural observation, not a confirmed fact about behavior.

**Class 3. Claims about behavior.** These are statements about what a file does, what functions it exposes, what interactions happen between modules, what is rendered, what is persisted, what is called, what is returned. A structural artifact cannot support these statements. A file-path-based claim that the chassis view service "returns a list of chassis objects" is outside the bundle's warrant; confirmation requires opening the file. The discipline with respect to this class is uncompromising: structural artifacts do not support class-3 claims, and any class-3 claim that appears downstream must be sourced from a source read, not from the bundle.

Three consequences follow from this discipline.

First, the bundle is a legitimate input to downstream investigation rather than a source of false confidence. A reader who treats every tree-report line as a class-1 fact, every name-based suggestion as a class-2 observation explicitly tagged as interpretive, and every behavioral claim as requiring source reading will use the bundle correctly. A reader who conflates the classes will build a model of the codebase that looks more confident than the evidence supports.

Second, the bundle is not a deliverable to a customer. It is a working orientation aid for the engagement's internal downstream work. Its claims are scoped appropriately for that role; they are not scoped to support customer-facing conclusions about implementation.

Third, the bundle's value is preserved by keeping the class-distinction visible when downstream artifacts cite the bundle. A downstream document that says "the modern frontend's feature pages live under the `unified-ems-ui` repository" is citing a combination of a class-1 fact (that repository exists in the inventory) and a class-2 interpretation sourced from handoff documents and meeting transcripts (what that repository's role is). A downstream document that says "the feature pages implement lazy-loaded routes via the shell" is making a class-3 claim that requires source confirmation and should not be sourced from the bundle alone.

## 9. Ignored Extensions and Binary Skipping

The consolidated reports list ignored file extensions per repository with per-extension file counts, alongside a count of binary files skipped. This is a structural fact worth noting in its own right because it affects how a reader should interpret the reports' line-count figures.

The extensions skipped per repository vary. Asset-oriented extensions (`.png`, `.jpg`, `.gif`, `.ico`, `.svg` in some contexts), font extensions (`.woff`, `.woff2`, `.ttf`, `.eot`, `.otf`), archive and compiled extensions (`.zip`, `.tar`, `.gz`, `.jar`, `.war`, `.class`), and occasional document extensions (`.pdf`, `.xlsx`) show up as ignored in various repositories. The specific ignore list varies from repository to repository as its asset profile varies.

The methodological consequence is straightforward. The "counted lines" figure in a consolidated report is a reading of text-bearing files, not of total file payloads. A repository whose raw footprint is dominated by images, fonts, and archives will show a smaller counted-line figure relative to its total on-disk size than a repository whose footprint is all source text. This is desirable — line counts over binary assets are not meaningful — but a reader who treats "counted lines" as a measure of repository size rather than as a measure of text-bearing content will draw the wrong conclusion.

The binary-skipping behavior sits in the same register. The consolidated report's "skipped binary file count" is the count of files that the line-counting pass identified as binary and stepped around. These files exist in the repository; they are not counted. The bundle is explicit about their exclusion rather than silent about it, which preserves the reader's ability to interpret the counts correctly.

## 10. The Bundle as Orientation Substrate

The bundle's role in the methodology is orientation, not conclusion. It is the first structural input that downstream investigation stands on — the first artifact that lets a reader form a picture of the codebase from something other than verbal account — and its value is in being a grounded, factual starting map.

The word "substrate" is used deliberately. A substrate is what downstream work rests on; it is not the final form of the work. The bundle is consumed as orientation material by a reader first arriving at the repositories, and it is consumed as structured input by downstream automated or semi-automated processes that partition the tree reports and absorb them at scale. In both consumption modes, the bundle is an input to further work, not an output that speaks to a customer about implementation direction.

The bundle's placement in the engagement reflects that role. It sits under the POC folder alongside the handoff package, but in its own top-level directory, so that a reader can navigate to it independently without having to find it through the handoff. It is copied into the POC folder as a snapshot for sharing rather than being produced in place; the canonical working location of the underlying generated outputs lives elsewhere, and the bundle's README notes the distinction. The snapshot is stable and self-contained; updates to the underlying generators do not retroactively rewrite the bundle.

A reader working the bundle top to bottom proceeds through the README first to understand what is present, through the repository inventory next to understand which repositories are in scope and where they live, through the combined consolidated report to absorb a cross-family structural view, and into the per-family consolidated reports and the per-repository tree reports as the next layer of detail. A reader with a narrower question navigates directly: an inventory question goes to the inventory document, a language-footprint question goes to the consolidated reports, a directory-level question goes to the relevant tree report. Both modes are intended.

## 11. Relationship to the Handoff Package

Chapter 3 documented the handoff package's construction. The two artifacts — handoff package and repository analysis bundle — are complementary and are designed to be consumed together.

The handoff package carries narrative context: the engagement arc, the scope, the strategic approach, the technical landscape as described by stakeholders, the conversion patterns reference, the stakeholder map, the repositories-access-and-compliance rules, the work items, the open questions and risks, and the ways-of-working. Its claims are grounded in transcripts and research files.

The bundle carries structural context: the factual footprint of each repository, the family organization, the inventory of what exists, and the tree reports that enumerate directory contents. Its claims are grounded in repository inspection.

Together, the two artifacts provide complementary coverage. The handoff's technical landscape document names the repositories in each family and describes their roles; the bundle's inventory lists the same repositories with on-disk paths and branch-context notes; the bundle's tree reports enumerate what each of those repositories contains. A reader who holds both artifacts can cross-check a handoff-level claim about a repository against the bundle's structural picture of that repository, and can use the bundle's structural picture to form questions that the next layer of source reading will need to answer.

One explicit cross-reference pattern deserves naming. Where the handoff-level technical landscape document identifies a repository as holding a particular class of content (for example, the assembly repository as the location of inventory and fault UI screens, or the infra-ui repository as the location of the shell), the bundle's inventory and consolidated report confirm the repository's presence, area, and gross structural footprint, and the bundle's tree report enumerates the repository's directory and file layout. A reader combining the three sources can form a grounded view of the repository without yet having read any source. The view is at the structural level. The next layer — source-level investigation of what the files contain — is what the rest of the methodology then takes up.

## 12. The Bundle's Place in the Broader Methodology

The repository analysis bundle is the first structural artifact of the execution-preparation phase, and it is the input substrate for the phases that follow. Two of those phases bear on how to read this chapter in the context of the whole documentation set.

The phase immediately following the bundle's production takes the tree reports as input and processes them at scale through a parallel-worker absorption pattern. Large tree reports that would not be absorbed in one reading pass by a single reader are partitioned, assigned to workers, and absorbed section by section in parallel. The worker outputs are aggregated and returned to the orchestrating thread for synthesis. The pattern's operating details — how partitioning is done, how workers are briefed, how aggregation is performed, how the orchestrator integrates — are the subject of the next chapter. This chapter's role is to establish that the tree reports exist, that they are shaped to be an input to such a pattern, and that the pattern is what scales their absorption.

The phase after that synthesizes the absorption output into a cross-repository map: a view of where in-scope functionality appears to live in source across the fourteen repositories, grounded in the structural map the bundle provides and disciplined by the observation-versus-conclusion tagging this chapter named. The cross-repository map is what then feeds scope-disciplined planning of the actual POC conversion work. The bundle's role at that stage is as the structural anchor: the map's claims about where functionality lives are anchored to specific repositories, directories, and files identified in the bundle, and the map's tagging of interpretive claims versus confirmed claims reflects the same class-distinction this chapter named.

The methodology treats the bundle as permanent. It is preserved under the POC folder in its snapshot form, with the README, the inventory, the family-level reports, the combined report, and the tree reports all kept in place. A reader returning to the engagement a long interval later can load the bundle and recover the structural picture that downstream work stood on. The bundle is neither regenerated opportunistically nor discarded when the next phase's output is produced; intermediate structural artifacts, like the scratch extractions preserved with the handoff package, are part of the audit chain for the claims downstream artifacts make.

---

The bundle provides the structural map. The next chapter documents how that map is absorbed at scale through a parallel-worker pattern designed to process tree reports whose size exceeds what a single reader can carry in one pass.
