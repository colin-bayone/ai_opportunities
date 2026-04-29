# Issue: Build a working local implementation of the PR-to-commit mapping approach

**Repository:** https://wwwin-github.cisco.com/DeepSight/ci-cd
**Branch:** `skills/webex`
**Working folder:** Co-located with your research and documentation. A sibling location like `build-issue-responder/pr-dependency-mapper/` works if you want to graduate the work from research into a runnable component; place it where it makes sense given how the research and documentation landed.
**Dependencies:** The research is committed to the Cisco repository; the generalized documentation is committed to the Cisco repository.

---

## Description

You did the research. You articulated the approach in your own terms. The natural next step is to build it. This issue is the working local implementation of the PR-to-commit mapping approach using the research and documentation as your inputs.

The deliverable is code that runs on your machine, takes a PR identifier as input, and produces the mapping the research describes and the documentation generalizes. The point of doing this locally first is to prove the approach end to end before the result gets wired into anything else. Once it works locally against representative PRs from the NX repository, it becomes a component the bot work and the build-failure analysis path can build on.

The research is the source of truth for what the data looks like in practice. The documentation is the source of truth for the approach in the abstract. The implementation is where they meet: take what the documentation says, apply it to what the research found, produce code that works. You own this end to end. By the time it runs, you should be able to walk through the code and explain why each piece is there, where it came from in the research or the documentation, and what each output field represents.

## Tasks

1. **Set up the implementation folder on `skills/webex`.** Pick a location that fits with where the research and documentation landed. Initialize the implementation skeleton (Python module structure, `requirements.txt` or equivalent, a `.env.example` for any credentials).

2. **Implement the core mapping logic.** Per the documentation's stated inputs and outputs, write a callable that takes a PR identifier and returns the structured mapping. Use the research findings to drive the data extraction details (which fields the upstream provides, how relationships are captured, how edge cases are handled).

3. **Run it against representative PRs.** Pick at least ten recent PRs from the NX repository, including a mix of merged and unmerged, and confirm the implementation returns the structured mapping for each.

4. **Validate against a known case.** Pick at least one historical case where the mapping should match a known release-lead PR backout. Confirm the implementation produces the expected mapping for that case.

5. **Commit and push directly to `skills/webex`.** Push daily as the implementation progresses. The implementation, the validation runs, and any helper scripts all live on the branch.

## Verification

**Set up:**
- The branch `skills/webex` checked out locally
- The research and documentation accessible from the same branch
- Credentials for the NX GitHub access in your local environment using a `.env.example` pattern

**Functional flow:**
1. Run the implementation against a recent NX PR by ID
2. Inspect the structured output and confirm it matches what the documentation says the output should look like
3. Repeat for ten representative PRs
4. Run against the known historical case; confirm the mapping matches the expected result
5. Capture the validation runs as artifacts on the branch (logs, sample outputs)

**Edge cases:**
- A PR that was closed without merging
- A PR with multiple commits
- A PR with no upstream parent in the mapping
- A malformed PR identifier (string vs integer, unexpected format)

## Acceptance Criteria

- [ ] Working implementation is committed to `skills/webex` in a runnable form
- [ ] Implementation runs locally and produces the structured mapping for at least ten recent NX PRs
- [ ] At least one historical case is validated end to end with the expected output
- [ ] Implementation matches what the documentation describes for inputs and outputs
- [ ] You can walk through the code and explain what each piece is doing and where it came from in the research or documentation
- [ ] Pushed daily as the implementation progresses
- [ ] No hard-coded credentials; secrets follow the project's existing pattern

## Notes

### Working folder and branch

All code lands on https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex. Co-locate the implementation with where the research and documentation landed so the lineage is obvious. Commit and push early; push daily.

### Using Codex effectively

The prompt below is a starting point for your Codex session. You own the session; expand, adjust, or rewrite as you go. The point is to use Codex as your accelerator on the implementation work, not to follow a recipe. Move with velocity. Treat this as guidance only.

```
Start here:

I am building a working local implementation of a PR-to-commit
mapping approach. I have already completed two things that this
implementation builds on:

1. Research: a structured analysis of how PR-to-commit mapping
   behaves in a specific repository, committed to the skills/webex
   branch of https://wwwin-github.cisco.com/DeepSight/ci-cd.

2. Documentation: a generalized description of the approach,
   committed to the same branch. The documentation states the
   inputs the approach assumes and the outputs it produces.

Help me:
- Read the documentation and translate the stated inputs and
  outputs into a Python module signature
- Read the research and identify the specific extraction details
  the implementation needs (which fields, which API calls,
  which relationship patterns)
- Build the minimum code needed to satisfy the documented
  contract end to end
- Generate a small validation harness that runs the
  implementation against ten representative PRs from the NX
  repository and one historical case
- Keep secrets out using a .env.example pattern

Use the skills/webex branch as the working location. Commit and
push early. Push daily. The goal is a runnable implementation
that I can walk through and explain end to end.
```

Refine the prompt as the implementation takes shape. Once the module signature is settled, switch to a tighter prompt focused on filling in the extraction logic and the validation harness.

### Presentation readiness

The implementation, the research, and the documentation form a connected body of work that you own. You should be able to demonstrate the code running, walk through how it satisfies the documented approach, and explain how the research informed the specific extraction choices. Anyone reviewing the work should leave understanding both what the code does and why it does it that way.

### Common pitfalls

- Building from scratch instead of from the documented approach. The documentation states the inputs and outputs; implement those, do not invent a parallel contract.
- Skipping the validation step. The known historical case is the strongest test that the mapping is correct, not just well-formed.
- Hard-coding credentials, repository names, or paths. The implementation should be portable enough to point at a different repository with a configuration change.
- Letting the implementation drift away from the documentation. If you discover during implementation that the documented contract needs adjustment, update the documentation in the same commit; the two should stay aligned.

### What this issue does NOT cover

- Wiring the implementation into the WebEx bot. Separate issue.
- Wiring the implementation into the build-failure analysis MCP endpoint. Separate workstream.
- Cisco-side deployment of the implementation. Separate workstream.

This issue is the local proving ground. Get the implementation running cleanly here and the downstream integration becomes routine.
