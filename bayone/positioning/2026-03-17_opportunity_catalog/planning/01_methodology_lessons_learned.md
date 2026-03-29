# Methodology Lessons Learned - Opportunity Catalog Discovery

**Date Started:** 2026-03-17
**Purpose:** Document what works and what doesn't for large-scale discovery work. Foundation for future skill development.

---

## LESSON 1: Don't Search for What You Don't Know Exists

### What Went Wrong (Initial Attempt)

**Bad Approach:**
1. Told Explorer agents to "scan folders" and "find work streams/initiatives"
2. Agents likely used Grep/keyword search for terms like "project," "initiative," "work stream"
3. Found prominent/obvious items (e.g., NX-OS CI/CD) and stopped
4. Missed 4-5 other projects entirely
5. No file-by-file reading = no auditability = no source references
6. Conflated hierarchy (client → projects → work streams)

**Why It Failed:**
- **You can't search for what you don't know exists**
- If a project isn't keyword-searchable or has a name you don't know, you'll never find it
- Grep is useless for discovery - it's only good when you already know what you're looking for
- Summarization happened too early (before comprehensive reading)
- No traceability to source files

**Symptoms of This Failure:**
- Missing major projects/opportunities
- Can't cite where information came from
- Numbers/timelines/facts appear "pulled out of ass"
- User can't audit or verify findings

---

## CORRECTED METHODOLOGY: Read First, Organize Later

### Core Principle
**READ EVERYTHING. Don't search. Don't assume. Don't keyword hunt.**

### Phase 1: Complete Inventory
- List EVERY .md and .txt file in relevant areas
- Don't skip folders that seem unimportant
- Create complete file manifest before reading
- Prioritize folders user explicitly mentions

### Phase 2: Sequential File-by-File Reading (NO SEARCHING)
- Read each file completely, start to finish
- Don't grep, don't keyword search - just READ
- Take notes while reading:
  - What projects are mentioned?
  - What are they called?
  - What's the scope?
  - Who are the stakeholders?
  - What technologies are involved?
  - What's the status?
- Record which file you're reading (for auditability)

### Phase 3: Project Identification (Understand Hierarchy)
**Hierarchy:** Client → Projects → Work Streams

**What is a PROJECT?**
- A distinct initiative with its own scope, deliverables, stakeholders
- May have its own budget, timeline, engagement
- Example: "NX-OS CI/CD Pipeline Enhancement," "UI Conversion," "SOW for Nexus Switches"

**What is NOT a project (it's a work stream)?**
- Sub-components within a project
- Example: "Developer Box," "Branch Health," "Gate Failures" (these are work streams within NX-OS CI/CD project)

**What is an OPPORTUNITY?**
- Multiple projects can exist under one client engagement
- Example: Cisco has NX-OS CI/CD project, UI Conversion project, SOW projects, etc.

### Phase 4: Auditable Documentation
For each project found, document:
- **Project Name** (what it's called)
- **Source Files** (with full paths where it's mentioned)
- **Core Description** (1-2 sentences, what is it?)
- **Key Stakeholders** (names and roles)
- **Technologies/Scope** (core tech stack, high-level scope)
- **Status** (active, planned, completed, on hold)
- **Work Streams** (if relevant for internal docs, but NOT for CEO-level)

### Phase 5: CEO-Level Synthesis (Digestible, Not Granular)
For CEO one-pagers:
- Focus on PROJECTS, not work streams
- High-level overview: what it is, why it matters, core tech
- Digestible summaries (1-3 sentences per project)
- Technical is fine, but not granular implementation details
- Show breadth of engagement (how many projects)

---

## EXECUTION PATTERN: Explorer Agents

### How to Use Explorer Agents Correctly

**DO:**
- Give them specific file lists to read
- Instruct: "Read these files completely, don't search"
- Ask: "List every project mentioned with the file where you found it"
- Request file-by-file notes
- Launch 3 agents in parallel with divided file lists

**DON'T:**
- Tell them to "scan" or "search"
- Give vague instructions like "find work streams"
- Assume they'll find everything without reading
- Let them summarize before reading everything

**Agent Prompt Template:**
```
Read the following files completely (do NOT use grep/search):
- [file list]

For each file, note:
1. File path
2. Projects mentioned (distinct initiatives, not sub-tasks)
3. Project description
4. Stakeholders
5. Technologies/scope
6. Status

Return findings file-by-file. Do NOT summarize until you've read all files.
```

---

## KEY PRINCIPLES FOR DISCOVERY WORK

1. **Read Everything First** - Don't search, don't assume, don't skip
2. **Understand Hierarchy** - Client → Projects → Work Streams
3. **Make It Auditable** - Always cite source files
4. **Separate Discovery from Synthesis** - Find everything, then organize
5. **CEO ≠ Technical Detail** - High-level overview, not implementation granularity
6. **Parallel ≠ Concurrent Search** - Run agents in parallel, but each reads their full file list
7. **User Guidance Wins** - When user points to folders/files, prioritize those first

---

## ANTI-PATTERNS TO AVOID

❌ **"Scan folders for keywords"** → Read files completely instead
❌ **"Find work streams"** → Find projects, work streams are sub-components
❌ **Early summarization** → Read everything, then synthesize
❌ **No source citations** → Always cite file paths
❌ **Search-based discovery** → Can't find what you don't know to search for
❌ **One agent for everything** → Divide files across 3 parallel agents
❌ **Treating work streams as projects** → Understand the hierarchy

---

## FUTURE ADDITIONS

This section will be updated as we encounter more issues, bottlenecks, or methodology improvements during this engagement.

### 2026-03-17 - Noise in Discovery (Other Clients in Transcripts)

**What happened:**
When reading Cisco meeting transcripts, agents found references to OTHER clients (Coherent, Bases, Walmart, Talent AI, Palantir, Adobe) because they were mentioned in conversation context. For example, Rahul2 transcript discussed BayOne's other engagements as examples/context.

**What we learned:**
- Meeting transcripts contain "noise" - mentions of other projects/clients for context
- Must distinguish between:
  - **Client projects** (what we're researching)
  - **Context mentions** (other clients referenced for comparison/examples)
  - **Infrastructure** (platforms mentioned but not separate projects)
- Clearly label these categories in findings to avoid confusion

**How we adjusted:**
- Create separate sections in findings:
  - "CLIENT PROJECTS" (actual engagements)
  - "INFRASTRUCTURE (Context Only)" (platforms/tools, not projects)
  - "PROPOSED BUT NOT CONFIRMED" (discussions, not engagements)
  - "NOT BAYONE SCOPE" (explicitly excluded)
  - "OTHER CLIENTS FOUND IN FILES" (noise from transcripts)
- This prevents mixing unrelated clients into target client's catalog

**Implication for synthesis:**
When creating CEO one-pagers or catalogs, ONLY include actual client projects. Context mentions should be filtered out during synthesis phase.

---

**Status:** Active document - add to this as we learn more
**Future Use:** Foundation for discovery skill development
