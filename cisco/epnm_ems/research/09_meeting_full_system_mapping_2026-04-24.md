# 09 - Meeting: Full System Mapping (14 Repositories)

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on the comprehensive 14-repository mapping and gap analysis

---

## Executive Framing

In the course of building the EPNM-to-EMS UI conversion proof of concept (POC), Colin generated a side-effect deliverable that, by his own description, is the strategically most significant artifact of the engagement to date: a complete, end-to-end system map of every repository involved in both EPNM and EMS, with bidirectional gap analysis across UI, backend, and data layers. The work was not in scope for the POC. It came out of the POC's agentic workflow and now constitutes — in Colin's words — "pretty much the full roadmap done already for the full scope here."

The framing Colin used in the meeting is the most important part of this document to preserve verbatim:

- "We have pretty much the full roadmap done already for the full scope here, which is pretty cool."
- "That happened a lot faster than we thought it would. And that was actually a bigger chunk of the puzzle."
- "The big hurdle is over for us."
- "In a lot better place than I thought we'd be for the bigger scope of things."

This is the language BayOne should use when transitioning the conversation from POC to full-scope conversion. The intellectual work that everyone — Cisco and BayOne both — assumed would be the largest unknown going into a full conversion engagement has effectively been retired in a single week of solo effort by Colin. That is the strategic message.

---

## What Was Mapped: The Full Statement of Scope

Colin's own statement, rendered cleanly from the transcript (with speech-to-text artifacts corrected):

> "We actually did a comprehensive mapping of the entire EPNM and EMS systems. So all 14 repositories between the two, we have the full [comprehensive] analysis of gaps that we found in the UI components and in the backend. We know everything in the front end, you know, what the correlation map is between feature A, feature B, or if there is a reverse direction, what that looks like, even down to the data elements there. So we have pretty much the full roadmap done already for the full scope here, which is pretty cool."

Decomposing what this single statement actually contains:

### 1. Scope is "the entire EPNM and EMS systems"

Not a slice. Not a sample. Not a representative module. The entire surface area of both products, bounded by the 14 repositories that constitute them.

### 2. All 14 repositories were included

Colin called this out explicitly twice in the meeting:

- "All 14 repositories between the two."
- "We found between EPNM and EMS, there's 14 total repositories, at least that are coming from that Confluence page and other ones that are mentioned implicitly."

The sourcing of the 14 is itself a notable detail: it was not a list handed to Colin. He derived the list from:

- **The Confluence page** that the Cisco team shared earlier in the engagement (the one Akilah / the team referenced).
- **Other repositories that are mentioned implicitly** — i.e., repos that surfaced through dependency references, cross-links in code or documentation, or contextual mentions inside the Confluence-listed repos themselves.

This means BayOne's repository inventory is more complete than what Cisco's own central documentation page lists. Colin's agentic process picked up the implicit dependencies that a human reader scanning the Confluence page would likely have missed.

### 3. The analysis is bidirectional

This is one of the most strategically important details in the meeting and Colin emphasized it directly. He did not just map "what's in EPNM that needs to come over to EMS" — the obvious direction. He also mapped "what's in EMS that does not exist in EPNM" — the reverse direction.

Colin's own language:

> "What the correlation map is between feature A, feature B, or if there is a reverse direction, what that looks like, even down to the data elements there."

And later, when explaining why bidirectional matters:

> "Maybe there's new things introduced in EMS that aren't there in EPNM, or maybe they're just behavioral differences, or, you know, one's microservice and one's thick client, so... There's a lot of things that we can take into consideration here."

This is the EMS → EPNM direction: features that EMS already has, that EPNM does not, that should not be lost or regressed when conversion happens. Behavioral differences. Architectural differences (microservice vs. thick client). All catalogued.

### 4. Coverage spans UI AND backend

This was confirmed directly in dialogue. Selva or Guhan asked:

> "Is it both the UI and the backend?"

Colin: **"Both, yes."**

This is critical. A UI-only mapping would have been a much narrower deliverable and would not have given Cisco confidence about the full conversion scope. Backend coverage means the full porting picture is visible.

### 5. Coverage extends to data sources / data elements

Colin called this out as a third gap category beyond UI and backend:

> "UI gaps, any feature gaps or backend things, also any data gaps. So any data sources that aren't there. And these correlate to the features that we found. So even if the backend gets ported over, if there's still not a data source that's ready to get plugged in, there's not much for the backend to do."

The reasoning here is sharp. A backend port without a corresponding data source on the target side is a dead port — the code lands but has nothing to operate on. By identifying data gaps separately and correlating them to feature gaps, Colin has given Cisco a way to sequence the conversion work properly: data first (or in parallel), then backend, then UI.

### 6. Granularity goes down to feature-to-feature correlation and individual data elements

> "What the correlation map is between feature A, feature B... even down to the data elements there."

This is not a summary-level mapping. It is a feature-correlation graph with data-element-level detail. For any given EPNM feature, the documentation identifies the corresponding EMS feature (or absence thereof), the data elements involved, and the relationship between them.

---

## The Three Gap Categories

Colin organized the gap analysis into three distinct categories. Each is captured in its own simple file (per repository, presumably), keeping them separable for downstream consumption:

### Category 1: UI Gaps

User-interface-level differences between EPNM and EMS. Anything that is present on one side and missing or different on the other. Both directions (EPNM → EMS and EMS → EPNM).

### Category 2: Backend / Feature Gaps

Functional and feature-level gaps. **42 backend gaps total**, called out explicitly by Colin near the end of the meeting:

> "It's 42. If you want to know the number, 42 gaps for back-end."

Selva's response to this number: "I mean, it's very comprehensive, really anxious and looking forward to the demo." That is a direct signal that the comprehensiveness of the gap analysis is registering with Cisco leadership as exceeding expectations.

### Category 3: Data Source / Data Element Gaps

Data layer gaps — sources that exist on one side and not the other, data elements that map or fail to map between the two systems. As noted above, these correlate back to the feature-level gaps so the dependencies are explicit.

> "Three simple files, the UI, if there's any gaps, and that goes in both directions."

The "three simple files" framing suggests the per-repository gap output is structured as three companion documents per repo.

---

## Volume Quantification by Language

A specific quality of the mapping that Colin called out: the quantification of code volume by language across the codebases.

> "The code bases look really big at first. We know exactly how much Java we have to do. We know exactly how much SQL we have, how much XML. All of that is documented."

This is the kind of detail that lets BayOne scope and price a full conversion engagement with real numbers rather than estimates. For each of the 14 repositories, the documentation specifies:

- How much Java
- How much SQL
- How much XML
- (and presumably other languages where present)

This is the input for line-of-code-based effort estimation, language-skill-mix planning for the delivery team, and risk identification (e.g., a repo that is 80% XML configuration is a fundamentally different conversion task than one that is 80% Java business logic).

---

## The Agentic Process Colin Used

Colin described the methodology in two distinct phases:

### Phase 1: Full-Picture Mapping

> "It's important to get these ground rules laid out. So the code bases look really big at first. We know exactly how much Java we have to do. We know exactly how much SQL we have, how much XML. All of that is documented. So we get the full picture of absolutely everything in these code bases."

The first pass is breadth-first: characterize every repository at a structural level — language composition, size, shape — so the agentic workflow has the ground rules established before any deep work begins. This is the "ground rules" phase.

### Phase 2: Spawn Deep-Dive Agents Per Repository

> "Then we spawn off our agents to go and do deep dives into every single bit of each of those repositories. So that gives us the full end-to-end map of what the application looks like, both for EPM and for EMS."

Once the ground-rules layer is in place, Colin spawns specialized agents that go deep into each of the 14 repositories individually. Each agent produces detailed mapping output for its assigned repo. The aggregate of those outputs is the full end-to-end application map.

### Self-Auditing Sub-Process

A noteworthy operational detail Colin mentioned about the agentic workflow:

> "Whenever you have the process and it's working well, for me it's fairly hands-off. That's the beauty of the [agentic] workflows. So we audit it ourselves while it's running, so we can make sure everything's working properly."

The agents audit themselves while running. Colin then audits the audit. This is a two-tier quality control structure embedded in the workflow itself, which is part of why a single person was able to produce this volume of output in one week.

### Human-in-the-Loop Decisions

Colin distinguished between the generated content and his own contributions:

> "Any of the decisions that we had to make along the way, those are also documented with the rational justification. So that's my human in the loop part, if you will. Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly."

Architectural and judgment-call decisions are flagged in the documentation with Colin's own rationale, separately from the AI-generated mapping content. This makes the documentation auditable: a Cisco reviewer can see which decisions were AI-derived structural mapping versus which were Colin's deliberate engineering judgment.

---

## Documentation Output: ~250 Files

Colin gave a specific volume number for the generated documentation:

> "This is one of about, I think probably about 250 files. Those are not meant necessarily to be read by humans, although they are human readable on GitHub. Those are mostly for the next phase in the process. And there's so many because we did the entire thing [end to end]."

Key properties of the documentation output:

- **~250 files total** across all 14 repositories.
- **Primarily machine-readable** — the audience is "the next phase in the process," meaning downstream agents/automation that will consume this mapping when actual conversion work begins.
- **Also human-readable on GitHub** — anyone on the Cisco side can browse the markdown directly in GitHub and read it. The format is markdown (rendered nicely on GitHub) but structured for machine consumption.
- **Comprehensive end-to-end** — the volume comes from the fact that nothing was sampled or summarized; every layer was fully mapped.

The dual-purpose nature (machine-readable but human-readable on GitHub) is deliberate. It means Cisco can audit the work without any tooling on their side, AND BayOne can feed it directly into the next phase of agentic conversion work without any reformatting.

---

## Where the Documentation Lives

Colin already pushed everything to Cisco's GitHub:

> "We've also kept [it] documented... at least all of it is on the GitHub repositories for this too. So absolutely everything throughout this entire process for us is there so you can see it."

> "All the code will be live on your GitHub. So I put everything, I believe, on the same... For each repository, there's a branch that is called [agentic] UI conversion. So it's based on the develop branch for all of these."

Each of the 14 repositories has a branch (named something like `agentic-ui-conversion`, based on speech-to-text "a Gentec UI conversion") branched off `develop`. The mapping documentation, the gap analysis, and the conversion code all live on those branches.

Colin also noted that decision rationales are embedded in the commit messages on those branches, which makes the work auditable at the commit level:

> "I actually put them in the commits that we did on the branch. I put them so specifically they could be audited by the team already."

---

## The Cost Reference

Colin disclosed his own cost expenditure during the week, which is a useful data point for understanding what production of this artifact cost:

> "I maxed out on the Cisco [Claude Code] subscription pretty much every day this week, which was a fun thing for me. We've really enjoyed all of our work."

He maxed out the daily limit on his Cisco-issued Claude Code subscription every day for a week. This is BayOne effort that was fully absorbed by Colin personally, using Cisco-provided AI tooling, with no additional BayOne cost passed through. It is also a useful proof point for full-scope pricing conversations: the AI infrastructure cost of producing this kind of mapping is bounded by daily subscription caps, not by hourly compute spend.

---

## Strategic Implication: The Big Hurdle Is Done

The most important sentence in the entire meeting, for the purposes of the BayOne pivot from POC to full-scope conversion, is this one:

> "The big hurdle is over for us."

Colin contextualizes it with:

> "In a lot better place than I thought we'd be for the bigger scope of things. But even for just the POC's sake, we are more than good. We have a lot of really nice flows built for you. So that's very repeatable work from here on out."

The breakdown of what this means strategically:

1. **The mapping was the unknown.** Going into this, the largest source of risk and effort estimation uncertainty for a full EPNM-to-EMS conversion was always going to be: how big is the actual scope, where are the gaps, and how do we know we have full coverage? That is the question that traditionally takes a discovery engagement of weeks or months to answer.

2. **The mapping is now done.** As a side effect of the POC, that question has been answered. All 14 repos. All UI components. All backend features. All data sources. Bidirectional. With language-level volume quantification.

3. **The remaining work is "repeatable."** Once the map exists, the conversion work itself becomes a templated, parallelizable execution problem. The same agentic flow Colin built for the POC scope (fault management inventory) can be applied screen-by-screen, repository-by-repository, against the gap analysis as the work list.

4. **The conversation with Cisco product management can happen now.** Selva said it directly in the meeting:

   > "Based on this, we are going to go to the product management and say, hey, we got this covered. You can go promise the customers that they will get this functionality, right? So I want to ensure that that is taken care of."

   Cisco's product management can use this mapping to make customer-facing commitments about feature parity and conversion timeline. This is exactly the kind of artifact that unlocks the full-scope engagement decision on Cisco's side.

5. **DPM (Data/Performance Management) is in the gap analysis.** Selva specifically asked about DPM, a key area for customers, and Colin confirmed it is captured:

   > Selva: "It's a key thing, right? The customers use the performance management quite a bit. So we will see that is all part of the whatever you have generated... It's not in the POC, but..."
   > Colin: "It's not part of the POC, you're right, but that's in the gap."

   This is a useful concrete example of the breadth of coverage: a feature area that wasn't in POC scope is nonetheless fully captured in the gap analysis for full-scope planning.

---

## Architectural-Decision Bonus Output

Colin mentioned an additional artifact he prepared but did not push during the POC, deliberately holding it for the full-scope conversation:

> "I didn't want to bring this up for the POC, but I have it ready, even along [with] some architectural decisions, because there's even some, you know, we could see whatever things were getting ported over to EMS. There's some debt that it's carried over too. There's different ways to do the same thing. For instance, even just looking at the way columns are handled in a table, something that's simple. We can even fix that along the way."

This is a separate deliverable: an architectural-decisions register identifying technical debt and inconsistencies in EMS that have been carried over from EPNM, along with proposed remediation. Colin specifically chose not to make those decisions unilaterally during a POC ("I didn't want to make that decision on a POC without the team involved") but flagged them as accelerators for the full-scope engagement:

> "We can definitely accelerate the timeline even further with that in mind."

This is yet another piece of the case for the full-scope engagement — BayOne is not just bringing a conversion factory, it is bringing engineering-judgment improvements that make the resulting EMS codebase cleaner than a literal port would produce.

---

## Summary: What BayOne Now Has

For the file's purpose — being referenced when BayOne pivots from POC to full-scope conversion — here is the inventory of artifacts that exist today as a result of this work:

| Artifact | Detail |
|---|---|
| Repository inventory | 14 repositories, sourced from Confluence + implicit references |
| Per-repo language volume | Java / SQL / XML quantification per repository |
| End-to-end application map | Full structural map of EPNM and EMS, both directions |
| Feature correlation map | Feature-A-to-Feature-B relationships, both directions |
| Data element correlation | Down to the individual data element level |
| UI gap list | Bidirectional, per repo |
| Backend / feature gap list | 42 backend gaps total, bidirectional, per repo |
| Data source gap list | Bidirectional, correlated to feature gaps |
| Documentation files | ~250 markdown files, machine-readable + human-readable on GitHub |
| Branch location | `agentic UI conversion` branch (off `develop`) on each of the 14 repos |
| Decision rationales | Embedded in commits and inline, separable from AI-generated content |
| Architectural-debt register | Held back from POC, ready for full-scope conversation |

---

## Quotes to Keep Handy for the Pivot Conversation

For BayOne's use when steering the conversation from POC to full-scope:

- "We have pretty much the full roadmap done already for the full scope here."
- "That happened a lot faster than we thought it would. And that was actually a bigger chunk of the puzzle."
- "The big hurdle is over for us."
- "In a lot better place than I thought we'd be for the bigger scope of things."
- "That's very repeatable work from here on out."
- "All 14 repositories between the two, we have the full [comprehensive] analysis of gaps."
- "Even down to the data elements there."
- "42 gaps for back-end." (when comprehensiveness needs to be quantified)

And from Selva, validating the value of what BayOne produced:

- "I mean, it's very comprehensive, really anxious and looking forward to the demo."
- "Based on this, we are going to go to the product management and say, hey, we got this covered."
