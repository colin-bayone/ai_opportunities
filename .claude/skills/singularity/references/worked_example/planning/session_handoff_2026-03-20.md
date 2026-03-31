# Session Handoff: 2026-03-20

**Purpose:** This document was written at the end of a Claude Code session so the next session can pick up exactly where we left off without repeating mistakes or rediscovering what's already done.

---

## What Happened This Session

### Phase 1: Folder Structure and Methodology (COMPLETED)

We established the full decomposition approach for the Lam Research engagement:

1. Created the session folder `claude/2026-03-20_lam-research/` with subfolders: `source/`, `research/`, `planning/`, `decisions/`, `progress/`
2. Designed a **blockchain-style documentation system** (append-only, numbered chronologically, never edit old docs)
3. Created a **dual people-tracking system**: per-set people docs in `research/` (blockchain) + living `org_chart.md` at session root (always current)
4. Defined summary documents, bridge documents, and processing order

All methodology is documented in `research/00_methodology_2026-03-20.md`.

### Phase 2: Call Prep Decomposition - Document Set 01 (COMPLETED)

Fully decomposed the call prep document (`source/lam_call_prep (1).txt`) into 5 files:

| File | Status |
|------|--------|
| `research/01_call_prep_situational_context_2026-03-12.md` | Done |
| `research/01_call_prep_discovery_strategy_2026-03-12.md` | Done |
| `research/01_call_prep_technical_reference_2026-03-12.md` | Done |
| `research/01_call_prep_people_2026-03-12.md` | Done |
| `research/01_call_prep_summary_2026-03-12.md` | Done |

Also created `org_chart.md` at session root (populated with call prep knowledge).

### Phase 3: Meeting Transcript Decomposition - Document Set 02 (PARTIALLY COMPLETED)

Started processing the meeting transcript (`source/lam_meeting_3122026.txt`).

**Completed:**

| File | Status |
|------|--------|
| `research/02_meeting_people_2026-03-12.md` | Done - people on the call, roles, sentiment |
| `research/02_meeting_topic_map_2026-03-12.md` | Done - Pass 1 high-level topic identification |

**NOT completed - the 5 deep dive files:**

| File | Status |
|------|--------|
| `02_meeting_technical_use_cases_2026-03-12.md` | NOT WRITTEN |
| `02_meeting_what_was_tried_2026-03-12.md` | NOT WRITTEN |
| `02_meeting_infrastructure_and_access_2026-03-12.md` | NOT WRITTEN |
| `02_meeting_business_opportunity_2026-03-12.md` | NOT WRITTEN |
| `02_meeting_speaker_dynamics_2026-03-12.md` | NOT WRITTEN |

**Also not completed (depends on deep dives being done first):**
- Org chart update (with meeting transcript learnings)
- Bridge document (`01-02_changes.md`)
- Summary (`02_meeting_summary_2026-03-12.md`)

### Phase 4: Agent Permissions Investigation (COMPLETED - IMPORTANT)

We attempted to run the 5 deep dives as parallel agents. **All 5 agents failed to write files** due to a permissions bug. This derailed the session significantly. Here is what we learned:

#### The Bug
- `mode: "bypassPermissions"` on spawned agents does NOT actually bypass permissions for Write, Edit, or Bash tools
- This is reportedly GitHub Issue #29110
- Agent Teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) do NOT solve this either - teammates inherit the same broken permission model

#### What We Tried
1. `mode: "bypassPermissions"` on agents - **FAILED**, still prompts
2. Added `"Write($CLAUDE_PROJECT_DIR/claude/**)"` to `permissions.allow` in `.claude/settings.local.json` - **SEMI-WORKS**: the write goes through but the user is STILL prompted to approve each write interactively
3. `mode: "acceptEdits"` on agents - **FAILED**, still prompts
4. Agent Teams research - no fix available there either

#### The Current State: Semi-Auto Mode
- Agents CAN write files, but the user must click "Yes" to approve each write in the chat UI
- This is acceptable as a fallback: the agent does the analysis and produces the file, the user just approves
- It is NOT fully autonomous
- The `Write($CLAUDE_PROJECT_DIR/claude/**)` permission IS in `settings.local.json` and should stay there

#### What NOT to Do
- Do NOT try to extract agent output from `/tmp` output files with Python scripts. This was attempted and is brittle and ugly.
- Do NOT fall back to "I'll just write the files myself" as a workaround for agent failures. The user explicitly rejected this approach multiple times. The whole point is agents doing the work.
- Do NOT suggest doing the deep dives sequentially in the main session. The user was very clear this is not acceptable and explicitly forbade it.

#### Files to Clean Up
There are test files in `research/` that should be deleted:
- `_agent_write_test.md`
- `_agent_write_test_2.md`

---

## What Needs to Happen Next

### Immediate: Resume the 5 Deep Dive Agents

Re-run the 5 parallel agents for the meeting transcript deep dives. Each agent:
- Reads the transcript (`source/lam_meeting_3122026.txt`) with ONE topic focus
- Writes its output file to `research/`
- The user will be prompted to approve each write (semi-auto mode) - this is expected and acceptable

The 5 agents and their topics (from `02_meeting_topic_map_2026-03-12.md`):

1. **Technical Use Cases** -> `02_meeting_technical_use_cases_2026-03-12.md`
   - The two use cases (self-help search + ask for help/escalation)
   - Detection vs. redaction distinction with all technical details
   - False positive requirements, performance constraints

2. **What Was Tried** -> `02_meeting_what_was_tried_2026-03-12.md`
   - Models tried (Transformers, SpaCy, Azure AI), results (20% -> 17% false positive)
   - Rule-based models abandoned (spelling variations)
   - 1,000+ hour labeling exercise paused
   - Why generative AI was NOT tried (unstructured output concern)
   - Colin's assessment (20% = out-of-the-box ChatGPT)

3. **Infrastructure & Access** -> `02_meeting_infrastructure_and_access_2026-03-12.md`
   - System landscape (fragmented, on-prem + cloud, LamGPT, Copilot, 6+ search systems)
   - No unified data lake
   - IAM program (~2 years, not robust), ASM, employee categories
   - Over-restriction mechanics

4. **Business Opportunity** -> `02_meeting_business_opportunity_2026-03-12.md`
   - Engagement appetite, approach preferences (rapid prototyping, incremental)
   - Brad's ownership structure (end-to-end)
   - ROI framing (feedback loop, escalation cost)
   - Deal signals, next steps
   - NOTE: transcript cuts off mid-answer on "high value targets" question

5. **Speaker Dynamics** -> `02_meeting_speaker_dynamics_2026-03-12.md`
   - Brad as room controller, Mikhail as precise translator
   - Colin's moments (20%/ChatGPT hit, unified control plane, redirect on IAM)
   - Key tensions and alignments
   - Power dynamics, unspoken signals

### After Deep Dives Complete
1. Update `org_chart.md` with everything learned from the meeting transcript
2. Write the bridge document: `01-02_changes.md` (what changed between call prep assumptions and what was actually said)
3. Write the summary: `02_meeting_summary_2026-03-12.md`

### Ongoing: Skill Notes
The file `planning/skill_notes.md` is a running collection of do's/don'ts for the future "code meeting decomposition" skill. The user provides guidance as we work and expects it captured immediately. The Transcript Processing section has guidance already. There is a placeholder for more notes that will come as we do the actual deep dives.

Key skill note to add: the agent permissions situation and the semi-auto mode workaround.

---

## File Inventory

### Session Root
```
claude/2026-03-20_lam-research/
├── org_chart.md                    (living document - needs update after 02 deep dives)
├── planning/
│   ├── skill_notes.md              (running do's/don'ts for skill creation)
│   └── session_handoff_2026-03-20.md  (THIS FILE)
├── research/
│   ├── 00_methodology_2026-03-20.md
│   ├── 01_call_prep_situational_context_2026-03-12.md
│   ├── 01_call_prep_discovery_strategy_2026-03-12.md
│   ├── 01_call_prep_technical_reference_2026-03-12.md
│   ├── 01_call_prep_people_2026-03-12.md
│   ├── 01_call_prep_summary_2026-03-12.md
│   ├── 02_meeting_people_2026-03-12.md        (DONE)
│   ├── 02_meeting_topic_map_2026-03-12.md     (DONE)
│   ├── _agent_write_test.md                   (DELETE)
│   └── _agent_write_test_2.md                 (DELETE)
├── decisions/
├── progress/
└── source/
    ├── lam_call_prep (1).txt
    └── lam_meeting_3122026.txt
```

### Settings Change Made
In `.claude/settings.local.json`, we added:
```json
"Write($CLAUDE_PROJECT_DIR/claude/**)"
```
to the `permissions.allow` array. This enables agents to write files under `claude/` (with user approval prompt - semi-auto mode).

---

## User Preferences (Critical - Do Not Violate)

- **Do NOT suggest doing deep dives sequentially in the main session.** The user explicitly rejected this multiple times and considers it unacceptable. Agents do the analysis work.
- **Do NOT try to extract agent output from temp files with scripts.** This was tried and the user called it "hokey" and a failure.
- **Always ask the user before proceeding with an alternative approach.** The user was very frustrated by Claude repeatedly suggesting approaches after being told no.
- **Capture skill notes immediately** when the user gives guidance. Don't wait.
- **The user controls when to resume the transcript work.** Do not bring it up unprompted.
