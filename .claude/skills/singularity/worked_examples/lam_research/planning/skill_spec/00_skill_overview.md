# Skill Overview: Engagement Decomposition

## What This Skill Does

This skill processes consulting engagement materials (meeting transcripts, call prep documents, internal debriefs, emails, and working discussions) into a structured, chronological, append-only documentation system that preserves the full arc of an engagement's discovery and thinking.

The output is a research library that any future Claude session or team member can read forward through and fully reconstruct the state of the engagement, including what was known at each point, what changed between events, and what the current understanding is.

## When to Use This Skill

- A new consulting engagement begins and source materials need to be organized
- A meeting transcript needs to be decomposed into detailed, structured documents
- Internal debriefs or follow-up conversations need to be captured
- A working discussion between the user and Claude needs to be documented as it happens
- Client-facing deliverables need to be drafted from the research library

## What Makes This Different from Meeting Notes

Meeting notes summarize. This skill decomposes. The difference:

- **Meeting notes:** "They discussed two use cases and mentioned they tried ML models."
- **This skill:** Separate files for each use case with every technical detail, a separate file for what was tried with exact results and failure modes, a separate file for speaker dynamics and trust signals, a people file with sentiment analysis, and a summary that ties it all together.

The goal is exhaustive capture with purposeful organization, not summarization.

## Core Principles

1. **Blockchain style.** Documents are numbered chronologically and never edited after creation. New understanding goes in new documents that reference back to earlier ones.

2. **Multi-pass processing.** Transcripts are read multiple times, each pass focused on a single topic. Documentation is written after each pass, not accumulated and dumped at the end.

3. **Parallel agent execution.** Per-topic deep dives are dispatched as separate agents running in parallel. Each agent reads the full transcript with a single focus and writes one file.

4. **Dual people tracking.** A per-event people document captures what was learned about people from that specific event (append-only). A living org chart is always current (the one exception to append-only).

5. **Ask, then process.** The skill asks the user what files to create beyond the standard ones. Different meetings warrant different breakdowns. The user knows what matters.

6. **Deliverables flow from research.** Client-facing documents are drafted from the research library, not from raw transcripts. The research library is the single source of truth.

## Skill Components

| Component | Purpose |
|-----------|---------|
| Session setup | Create engagement folder structure, initialize `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` |
| Source processing | Multi-pass transcript decomposition with parallel agents |
| People tracking | Dual system: per-event docs + living org chart |
| Bridge documents | What changed between document sets |
| Summary documents | Quick-reference overview of each set |
| Discussion mode | Capture working discussions between user and Claude |
| Deliverables pipeline | Draft client-facing documents from research |
| Research agents | Look up external information in context of the problem |

## Engagement Output Location

The skill writes all engagement output to:

```
/<client_name>/<opportunity_name>/
```

This is a top-level project folder (e.g., `/lam_research/ip_protection/`). The skill itself lives at `.claude/skills/singularity/`.

## Prerequisites

### Mandatory Permission Check (Runs Every Invocation)

The skill performs a hard gate check at startup. Before doing ANY work, it reads `.claude/settings.local.json` and verifies that agents have write access to the project root:

```json
{
  "permissions": {
    "allow": [
      "Write($CLAUDE_PROJECT_DIR/**)"
    ]
  }
}
```

If this permission is missing, the skill stops and asks the user for permission to add it. Without it, agents cannot write files, which breaks the entire parallel processing workflow. This is non-negotiable.

### WebSearch Permission

The skill also requires WebSearch permission for research agents. Verify that `"WebSearch"` is in the `permissions.allow` array. If missing, ask to add it.
