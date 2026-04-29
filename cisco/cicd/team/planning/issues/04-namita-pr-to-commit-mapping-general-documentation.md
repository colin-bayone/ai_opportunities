# Issue: Document the generalized PR-to-commit mapping approach, decoupled from the Cisco CI/CD context

**Repository:** https://wwwin-github.cisco.com/DeepSight/ci-cd
**Branch:** `skills/webex`
**Working folder:** Your choice. A docs-style folder co-located with the research is natural; pick what makes sense once the research lands.
**Dependencies:** The PR dependency research is complete and committed to the Cisco repository (prior issue).

---

## Description

The research you completed describes the PR-to-commit mapping approach as it applies to the Cisco NX repository. This issue captures the same approach as general-purpose documentation, decoupled from the CI/CD context. The reader should be able to take this document into a different engagement, with a different repository structure and different tooling, and apply the approach without having to re-derive it from the specific Cisco work.

This documentation is shaped and informed by your research. You did the work to understand how the approach behaves in a real repository, and this issue is your opportunity to articulate that understanding in your own terms at a level that holds up beyond this engagement. You own the approach. You will need to present it, so treat the document as both the artifact and your reference for explaining it to a technical audience. The accountability is on understanding the approach in depth: the inputs, the outputs, the methodology choices, the limitations, the variations across repository styles. You should be able to walk through any section of the document and answer follow-up questions without reading from the page.

The point is generalization. Articulating the approach abstractly forces the underlying logic into the open and produces a reusable artifact for future engagements. References to Cisco-specific tooling, naming, and infrastructure stay out of the document; the methodology, the inputs, the outputs, and the reasoning stay in.

## Tasks

1. **Read the research from the prior issue.** Identify what is general and what is Cisco-specific. The research is the source material; the documentation is the abstraction.

2. **Write the general approach.** Produce a markdown document that covers:
   - What PR-to-commit mapping is and what problem it solves
   - The inputs the approach assumes (a git repository, a PR identifier, access to commit and branch metadata)
   - The outputs the approach produces (the data shape of the mapping, the relationships captured)
   - The methodology applied (parallel-agent research, attribute-based prompting, the rules.md scaffolding pattern)
   - How the approach handles common variations across repositories
   - Limitations and where the approach breaks down

3. **Include examples that are not Cisco-specific.** Use a generic example repo or describe the approach in terms that would apply to any open-source project. If a Cisco-specific example helps illustrate a point, isolate it as an appendix or call it out as such.

4. **Commit and push directly to `skills/webex`.**

## Verification

- The document reads as a general guide, not as a Cisco trip report
- Someone reading the document with no Cisco context can understand the approach
- The methodology principles are stated as principles, not as Cisco-specific instructions

## Acceptance Criteria

- [ ] Generalized documentation is committed to `skills/webex`
- [ ] The document covers the approach, the inputs and outputs, the methodology, and the limitations
- [ ] Cisco-specific tooling, naming, or infrastructure does not appear in the main body
- [ ] The methodology is articulated as transferable principles
- [ ] You can walk through the document and explain any section in detail, including methodology choices and limitations, without reading from the page
- [ ] Pushed daily as the document progresses

## Notes

### Working folder and branch

All work lands on https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex. Pick a docs-style folder location that matches where the research from the prior issue landed.

### Using Codex effectively

Codex can help with structure, organization, and keeping the level of abstraction consistent. The prompt below is a starting point; expand or contract as the document takes shape. The point is to move with velocity using Codex on the structuring and the consistency-checking, not to follow a recipe.

```
Start here:

I am writing general-purpose documentation for the PR-to-commit
mapping approach. The source material is research I completed for
a specific repository (Cisco NX). The documentation has to be
decoupled from that specific context so the approach is reusable
in other engagements.

Help me:
- Outline the document structure (sections covering: what is
  PR-to-commit mapping, inputs, outputs, methodology, limitations,
  variations across repository styles)
- Review drafts for places where Cisco-specific terminology has
  leaked in and propose generic substitutes
- Keep the level of abstraction consistent across sections
- Generate a small generic example that illustrates the approach
  without referencing the source research

The goal is documentation that someone in a different engagement
could pick up and apply.
```

Refine the prompt as the document shape settles.

### Presentation readiness

The document and your understanding of it go together. Treat the writing as preparation for explaining the approach to a technical audience. By the time the document is committed, the inputs, outputs, methodology choices, limitations, and variations should be at your fingertips. The strongest test of the document is whether you can answer "why this choice and not that one" for every decision the approach embeds.

### Common pitfalls

- Pasting sections of the research into the documentation. The research is the input; the documentation is the abstraction. They should not look alike.
- Generalizing so far that the document loses utility. There is a balance: abstract enough to transfer, concrete enough to apply.
- Writing the methodology as a procedure ("first do X, then Y"). The methodology is a set of principles applied with judgment, not a runbook.
- Treating the document as the deliverable in isolation. The deliverable is the document plus the depth of understanding behind it.

### What this issue does NOT cover

- A working implementation. Separate issue.
- The Cisco-specific research. Covered in the prior issue.
