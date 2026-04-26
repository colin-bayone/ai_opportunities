# Authoring Rules

These rules govern how all documents in this set are written. Every contributor reads this document before adding content. If a rule is unclear or conflicts with material a contributor wants to add, the conflict is surfaced rather than resolved silently.

## 1. Single-Venue Framing

The documentation treats the engagement as having occurred on a single Cisco machine. Do not describe the work as occurring across separate machines, computers, devices, environments, or instances. Do not reference transfer of information between machines, "one side versus the other side," "Computer A versus Computer B," or similar framing. Any operational detail that would require describing multi-machine coordination is reframed or omitted.

## 2. Tool Naming

Refer to the AI development assistant as Codex throughout. This engagement used an AI-assisted development workflow; the specific tool is not the point of the methodology. Writing to a single tool name keeps the documentation readable and keeps the methodology generalizable. Readers can mentally substitute another tool name without the narrative changing in substance.

## 3. No Timelines or Quantitative Metrics

Do not call out:

- Elapsed time for any phase (days, weeks, hours).
- Calendar dates for specific work events except where an external event is being referenced by name.
- Counts of files produced, lines of code, tokens consumed, sizes in bytes or kilobytes, or similar volumetric measures.
- Effort estimates, time-to-complete figures, or productivity comparisons.

Qualitative description is appropriate. Quantitative counting is not the subject.

## 4. Tree Diagrams Welcome

Structural representations of codebases, folder hierarchies, and artifact layouts are useful and should be included where they help comprehension. Tree diagrams do not count as metrics; they are structural references.

## 5. Chapter Scale, Thoroughness, and Completeness

Each chapter is written at book-chapter scale. Short summaries are not the target. Aim for a reader to finish the chapter with a complete understanding of that phase or discipline without needing to consult other sources. Chapters are comprehensive and thorough. Where a chapter requires substantial length to be complete, it is written at that length.

## 6. Generic Descriptions of Internal Frameworks

Do not name specific internal BayOne skills, process frameworks, or tooling layers by their proprietary or project-internal names. Describe practices generically. The goal is a methodology document that is portable across contexts, not a reference to a specific named internal toolchain. When describing, for example, a structured append-only research pattern, describe it by its behavior and purpose, not by any internal project name.

## 7. Discovery as a Single Grouping

Everything that preceded the central recorded phase of the engagement — the pre-work, preliminary meetings, scoping conversations, strategic positioning, methodology presentation, and initial commitments — is grouped under "discovery" and described at a high level. The discovery chapter summarizes this pre-work without reproducing fine-grained detail. The central recorded phase begins where the handoff-package work started.

## 8. Cisco Specifics Allowed; Sensitive Material Excluded

Cisco technical and organizational specifics are appropriate for this documentation. Product names (EPNM, EMS, Crosswork Network Controller), repository names, stakeholder roles at the level of organization and function, technical architecture, and process specifics may all appear. Excluded:

- Commercial terms, pricing, margins, financial arrangements.
- Internal security incidents unrelated to the methodology being documented.
- Personnel matters.
- Anything that would be considered internally sensitive at either BayOne or Cisco and not relevant to the methodology itself.

When in doubt, omit the item and flag it in the session recap for the author to resolve.

## 9. Continuity Markers

At the end of each working session that adds content, the contents document (`contents.md`) is updated with:

- The current state of each chapter (planned, in progress, complete).
- A recap of what was added in the session.
- The date of the session's end and a time marker sufficient to establish ordering for subsequent sessions.

This is the mechanism by which a future session picks up without rereading the entire set.

## 10. Observation Versus Conclusion

The engagement surfaced many artifacts (tree reports, repository structures, handoff documents paraphrasing verbal conversations) that were consulted without direct source access. When documenting, distinguish cleanly between what was observed and what was concluded. Structural patterns in a directory are observations; what those patterns mean for implementation is a conclusion that requires validation. The methodology document preserves this distinction because it is part of what made the engagement's output disciplined.

## 11. Scope and Authorial Voice

Write in a neutral, technical voice. Do not personalize the narrative to a specific contributor, session, or author identity. The subject is the methodology and the work, not the individuals performing it. Where a stakeholder role is material to a decision, the role is referenced by organization and function ("the customer engineering lead," "the customer operational counterpart"), never by individual name. Authorial flourishes, editorial asides, and speculation outside the scope of the methodology are avoided.

## 12. Iterative Production

The documentation is produced iteratively across sessions. No single session is expected to finish the set. Contributors start where the contents document indicates, work in chapter-sized units, and update the contents document at session end. Drafts are fully functional material — not placeholder text — but a chapter may be revised in a subsequent session if new material or reframing warrants.

## 13. Parallel Agent Production — Mandatory Workflow

Chapters are written by parallel general-purpose agents spawned from the main session, not by the main session thread directly. This is the required production pattern for this documentation set. The main session orchestrates, assigns, reviews, and integrates; the agents do the drafting.

### Write-capability verification is non-negotiable

Before any chapter-writing agent is spawned, the main session spawns one pilot agent with read and write permissions enabled. The pilot is given a small verification task: read one small file and write a short confirmation artifact to a specific path. The main session then verifies on disk that the artifact exists with the expected content — not by relying on the agent's self-reported success.

If the pilot succeeds, the session is cleared to proceed with parallel chapter-writing agents.

If the pilot fails — the artifact does not exist, writes are blocked, or the agent cannot complete the task — the session stops immediately and flags the problem to the user. Under no circumstances may the session continue the documentation work without write-capable agents. There is no workaround. Attempting to do the work in the main session thread alone is not permitted; the orchestration pattern is the point.

### Parallel spawning

Once the pilot is verified, chapter-writing agents are spawned in parallel, not sequentially. Each is given:

- The chapter scope and subject matter.
- The source material it needs to read (the reference transcript for this documentation set, specific engagement artifacts under the POC folder, the foundation documents for authoring rules).
- The exact output path to write its chapter to.
- The authoring rules it must follow (by reference to `rules.md`).

Parallel execution is what makes chapter-scale production tractable. Sequential execution defeats the pattern.

### After chapters return

The main session reads each returned chapter, verifies it against the rules, integrates any cross-chapter consistency adjustments, and updates the contents document. Revisions within the same session can be delegated back to a fresh agent or handled in the main thread depending on the scope of the change.

### Why this rule exists

The methodology being documented itself relied on parallel agent work at multiple points. The documentation of that methodology follows the same pattern. It is the engagement's operating posture applied reflexively to its own record-keeping.

## 14. Sensitive and Identifiable Information — Never Permitted

No document in this set contains any information that is sensitive, identifiable, or otherwise inappropriate. This rule is absolute and covers, at minimum:

- **Personal names.** No individual's name appears in the documentation. Where a person's role is relevant to the methodology, they are referred to by organization and role only. Examples of acceptable framings: "the customer engineering lead," "the customer-side team lead responsible for Inventory," "the BayOne engagement lead," "the customer operational counterpart." Examples of what is never written: a first name, a last name, a nickname, or any initials tied to a specific person.
- **Email addresses, handles, phone numbers, and similar identifiers.** None of these appear in any document.
- **Credentials, API keys, tokens, passwords, repository secrets, or any other form of access material.** Never, under any circumstances.
- **Personal commentary, anecdotes, personal issues, or incidental remarks from conversations.** Even when such material appeared in source transcripts consumed during the engagement, it does not cross into the documentation. Only material directly relevant to the methodology itself may be referenced.
- **Direct quotations from individuals.** Paraphrased summaries at the role level are appropriate ("the customer engineering team framed the scope as..."); verbatim quotes attributed to a named or implied individual are not.
- **Specific data-source identifiers beyond repository names.** Repository names are appropriate because they are already part of the engagement's public shared context with the customer. Specific URLs to internal tooling, internal servers, internal dashboards, specific document IDs, or anything that would function as an access pointer to sensitive material are not.
- **Internal security incidents or personnel matters** on either the customer's side or BayOne's side. These have no place in a methodology document regardless of how tangentially they appeared in source material.
- **Commercial terms, pricing, rates, margins, or deliverable-timing commitments.** Already excluded by rule 8; restated here because sensitive-information discipline and commercial-exclusion discipline overlap.

The test is a conservative one: if a piece of information could reasonably embarrass or expose any individual or organization, or if it could be interpreted by a reader as material the author should not have included, it does not appear. When in doubt, omit.

## 15. Professional Posture — Meticulous, Never Circumventing

The documentation is produced in the best light. The engagement was conducted meticulously, within the customer's policies, rules, and guidelines. The documentation reflects that posture.

- No document describes or implies any action that circumvented, subverted, or worked around a customer policy, rule, guideline, or constraint.
- No document describes any action that could be characterized as hazardous to the customer's systems, data, personnel, or posture.
- The tone throughout is that of a professional engagement conducted with care. Any phrasing that could be read as clever-at-the-customer's-expense is omitted.
- The framing of compliance constraints is that of accepted preconditions, not of inconvenient obstacles. The methodology's rigor is what lets the engagement operate effectively inside the customer's constraints — the constraints are not described as limitations on the work; the work is described as designed to fit within them.

This is a document that will be read by the customer. It reflects the engagement's actual discipline. It should never suggest otherwise.
