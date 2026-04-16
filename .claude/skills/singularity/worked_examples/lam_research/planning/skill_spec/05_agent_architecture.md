# Agent Architecture

## Overview

The skill uses spawned agents for parallelizable work, primarily the per-topic deep dives during transcript processing. Each agent reads the full transcript with a single focus and produces one output file. This is the primary performance optimization in the skill.

## When to Use Agents

### Use Agents For

- **Per-topic deep dives.** After the topic map is created and approved, each topic gets its own agent. All agents run in parallel.
- **Research lookups.** When external information needs to be researched (e.g., Azure AI Foundry capabilities, Microsoft Purview documentation) in the context of the problem statement.
- **Re-exploration of existing docs.** When a specific detail needs to be found across multiple research files (e.g., "find all mentions of Azure services across all 02 files").

### Do Not Use Agents For

- **The people file.** This is done in the main session because it requires reading the org chart first and updating it after.
- **The topic map (Pass 1).** This is done in the main session because it produces the list of topics that agents will be dispatched for.
- **The summary document.** This synthesizes across all files in the set and must be written after all agents complete.
- **The bridge document.** This requires reading across two sets and is done in the main session.
- **The org chart update.** This requires reading the current org chart and all per-set people information.
- **Deliverables.** These require synthesis and user interaction.

## Agent Prompt Template for Deep Dives

Each agent needs a complete, self-contained prompt because agents start fresh with no context. The prompt must include:

```
You are writing a detailed decomposition document from a meeting transcript.
Read the transcript, then write one focused output file.

**Your focus:** [ONE specific topic]

**Read this file:** [path to transcript]

**Context from Pass 1 topic map (so you know what to look for):**
[Bullet points summarizing what the topic map identified for this topic]

**What to capture in exhaustive detail:**
[Specific list of what to look for and extract]

Be exhaustive. Quote or closely paraphrase key statements. Don't summarize - decompose.

**IMPORTANT:** This transcript is speech-to-text and full of transcription errors.
Use common sense to interpret garbled words.

**Write your output to:** [exact file path]

Use this header format:
[header template]
```

### Key Elements of the Agent Prompt

1. **The transcript path.** The agent reads the full transcript itself.
2. **The topic focus.** Exactly one topic per agent.
3. **Context from the topic map.** Bullet points so the agent knows what to look for without re-discovering it.
4. **Exhaustive detail instructions.** "Quote or closely paraphrase. Don't summarize, decompose."
5. **Speech-to-text warning.** Agents must apply common-sense interpretation.
6. **Exact output file path.** The agent writes directly to the `/<client_name>/<opportunity_name>/research/` folder.
7. **Header template.** Consistent formatting across all files.

## Agent Spawn Configuration

### Permission Mode

```javascript
mode: "bypassPermissions"
```

This is required for agents to write files without prompting the user. It works in conjunction with the Write permission in settings (see Prerequisites).

### Parallel Execution

All per-topic agents should be spawned in a single message with multiple tool calls:

```
// Spawn all 5 agents in ONE message
Agent(topic1_prompt)
Agent(topic2_prompt)
Agent(topic3_prompt)
Agent(topic4_prompt)
Agent(topic5_prompt)
```

This maximizes parallelism. The agents run concurrently and return results as they complete.

### Agent Names

Give each agent a short, descriptive name in the `description` field:

```
description: "Deep dive: technical use cases"
description: "Deep dive: what was tried"
description: "Deep dive: infrastructure and access"
```

## Permission Setup

### Required Permission

The following must be in `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Write($CLAUDE_PROJECT_DIR/**)"
    ]
  }
}
```

This grants agents write access to the entire project directory. It must be this broad because engagement folders are created at the project root (`/<client_name>/<opportunity_name>/`) and client/opportunity names vary.

With this permission and `mode: "bypassPermissions"` on agent spawns, agents write files fully autonomously with zero user approval prompts.

### Mandatory Startup Check

**Every time singularity is invoked, before doing ANY work, it must verify that agents can write files.** This is a hard gate. If the check fails, the skill stops and tells the user how to fix it.

The check:

1. Read `.claude/settings.local.json`
2. Verify that the `permissions.allow` array contains a Write permission that covers the project root. Acceptable patterns:
   - `Write($CLAUDE_PROJECT_DIR/**)`  (preferred, covers everything)
   - `Write($CLAUDE_PROJECT_DIR/<specific_client>/**)` (acceptable if the client folder is known)
3. If the permission is missing or too narrow:
   - Tell the user: "Singularity requires agents to write files autonomously. The Write permission in `.claude/settings.local.json` needs to cover the engagement folder. I need to add `Write($CLAUDE_PROJECT_DIR/**)` to the permissions. May I do that?"
   - If the user approves, add the permission
   - If the user declines, explain that the skill cannot function without it and stop

**Why this is mandatory:** The entire skill depends on parallel agents writing research files. Without this permission, every agent write prompts the user for approval, which defeats the purpose of parallel execution and breaks the workflow. This was learned through painful trial and error.

### How It Was Validated

The pptx-extractor skill at `.claude/skills/pptx-extractor/` confirmed that agents can write files autonomously when the Write permission is properly configured in settings.local.json. The same pattern applies here.

## Post-Agent Workflow

After all agents complete:

1. **Read all agent output files.** The main session reads every file the agents produced to understand the full picture.
2. **Write the synthesis files.** Summary, bridge document, org chart update. These require cross-file understanding that agents cannot provide individually.
3. **Inform the user.** Report what was created and the current state of the document set.

## Error Handling

If an agent fails to write a file:
- Do NOT fall back to writing the file in the main session. The user explicitly rejected this pattern.
- Do NOT attempt to extract agent output from temp files with scripts.
- Report the failure and ask the user how to proceed.

## Research Agents

Research agents are a distinct agent type from deep-dive agents. They perform external research using WebSearch and WebFetch, and they write their findings directly to the engagement folder. They are first-class citizens in the skill, not an afterthought.

### What Research Agents Do

- **Technology research:** Investigate unfamiliar technologies, frameworks, platforms, or services mentioned in meetings or source material. Example: "What is Microsoft Purview and what are its capabilities for sensitive information detection?"
- **Company research:** Background on client companies, competitors, market position, recent news. Example: "What does Lam Research do in the semiconductor industry?"
- **Benchmark research:** Industry benchmarks, market rates, competitive pricing, best practices. Example: "What do legacy UI modernization projects typically cost?"
- **Validation:** Verify technical claims made in meetings against current documentation. Example: "Does Azure AI Foundry support custom sensitive information types?"
- **Domain exploration:** Understand unfamiliar domains the client operates in. Example: "How do semiconductor fab naming conventions work?"

### Research Agents Write Their Own Files

Research agents write their findings directly to `/<client_name>/<opportunity_name>/research/` or `/<client_name>/<opportunity_name>/planning/` depending on the content:

- **Technology and domain research** → `/<client_name>/<opportunity_name>/research/<set>_research_<topic>_<date>.md`
- **Glossary updates** → `/<client_name>/<opportunity_name>/planning/glossary_<date>.md`
- **Benchmark data** → `/<client_name>/<opportunity_name>/pricing/benchmarks_<topic>_<date>.md` (when pricing-related)

Each research agent is spawned with `mode: "bypassPermissions"` and writes autonomously, same as deep-dive agents.

### Parallel Research

Multiple research agents can run in parallel when there are several independent topics to investigate. This is common when:

- Processing a transcript that references multiple unfamiliar technologies
- Preparing for a discovery call and needing background on several topics
- Building a pricing model and needing market benchmarks across categories

Example: After a meeting mentions Azure AI Foundry, Microsoft Purview, and SpaCy NER, three research agents can be spawned simultaneously, each investigating one technology and writing its own output file.

### Research Agent Prompt Template

```
You are a research agent for a consulting engagement. Your job is to deeply
investigate a specific topic and write a comprehensive research document.

**Your research topic:** [TOPIC]

**Context from the engagement:** [BRIEF CONTEXT about why this topic matters]

**Research instructions:**
1. Use WebSearch to find current, authoritative information
2. Focus on: capabilities, limitations, pricing (if relevant), how it relates
   to the engagement context
3. Distinguish between facts and marketing claims
4. Note the date of your sources (prefer recent over old)

**Write your findings to:** [exact file path]

Use this header format:
# <Set Number> - Research: <Topic>

**Source:** Web research
**Date:** <today's date>
**Document Set:** <set number>
**Context:** <why this research was needed>

---

[Your findings here]
```

### When to Launch Research Agents

Research agents can be launched at any point:

- **During source processing:** When unfamiliar terms or technologies are encountered in a transcript or document
- **During discussion mode:** When the user raises a topic that needs external validation
- **During pricing:** When market benchmarks are needed
- **During deliverable creation:** When a claim needs verification before putting it in a client-facing document
- **Proactively:** The skill should offer to research when it detects unfamiliar terms. Ask the user: "I noticed several Azure services mentioned that I could research in parallel. Want me to spawn research agents for Azure AI Foundry, Microsoft Purview, and Azure AI Search?"

### Research Output Quality

Research agents must:
- Cite sources (URLs or document names)
- Distinguish between verified facts and claims
- Note when information may be outdated
- Flag conflicting information from different sources
- Write in the same professional, detailed style as deep-dive agents

## Agent Count Considerations

There is no fixed number of agents per set. The number depends on the topic map:

- A simple meeting might warrant 3 agents
- A complex discovery call might warrant 5-7 agents
- An internal debrief might warrant 2-3 agents

The topic map determines the count. The user approves the proposed file list before agents are spawned.
