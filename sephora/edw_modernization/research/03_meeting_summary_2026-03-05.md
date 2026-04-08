# 03 - Meeting: Summary

**Source:** /sephora/edw_modernization/source/andrew-girishi-meeting1_formatted.txt
**Source Date:** 2026-03-05 (Andrew/Grishi Meeting)
**Document Set:** 03 (Andrew/Grishi Meeting)
**Pass:** Summary (final document for set)

---

## What This Meeting Was

Colin's first meeting with Andrew Ho and Grishi, the strategic and execution owners of the EDW modernization. This was the conversation that moved from executive buy-in (Mani, Sets 01-02) to technical validation. Colin presented the same AI-assisted approach but at a deeper technical level, and for the first time faced pointed technical questions about feasibility.

## Key Outcome

Andrew and Grishi both independently demanded a demo/POC before committing. This demand is what drove the entire next phase of the engagement: the technical deep dive with Malika (Set 04), the Track A/Track B scoping, and ultimately the demo being given today. The meeting also revealed that Sephora is already using Claude for SQL conversion (~30% efficiency gain) but needs full automation, and that they are talking to multiple vendors.

## Documents in This Set

| File | What It Covers |
|------|---------------|
| `03_meeting_people_2026-03-05.md` | Colin, Andrew, Grishi dynamics. Malika emerges as the enterprise architect. |
| `03_meeting_pain_points_and_current_state_2026-03-05.md` | Two major pain points (SSAS/Excel connector, DataStage agent), 30% Claude efficiency, scale numbers (6000+ reports), finance track correction |
| `03_meeting_agentic_architecture_discussion_2026-03-05.md` | The technical DNA: orchestrator+judge pattern, schema mapping 3-step workflow, knowledge graph flywheel, MCP, LangGraph, deterministic-first approach |
| `03_meeting_feasibility_concerns_2026-03-05.md` | Old Cognos 10.2/10.3, old DataStage, agent connectivity to on-prem, "wild thinking or real?" |
| `03_meeting_next_steps_and_demo_ask_2026-03-05.md` | Demo for next Thursday, deep dive with Malika, three-tier engagement model, competitive vendor context |
| `02-03_changes_2026-03-05.md` | Bridge: technical team enters, pain points surface, MCP and LangGraph named, competition explicit |

## Critical Takeaways

1. **Sephora's technical team arrived at the same agentic vision independently.** Andrew articulated multi-agent orchestration before Colin pitched it. This is not BayOne selling a concept. This is alignment.

2. **The 30% efficiency gain is the baseline to beat.** Grishi's team already gets 30% from Claude on SQL conversion alone. BayOne's solution needs to demonstrate dramatically more than that, especially on the manual steps (navigation, extraction, re-integration) that Claude alone cannot automate.

3. **The demo is the gating requirement.** Nothing moves forward without a working demonstration. Both Andrew ("is the wild thinking real?") and Grishi ("I want to see agents working") were explicit. This is why the demo matters so much.

4. **Finance track timeline was corrected.** Grishi said it "will go through end of this year," contradicting Mani's "20 more days" from Set 02. The execution owner has a more conservative (and likely more accurate) view than the executive.

5. **MCP and LangGraph were named.** Colin introduced MCP for tool integration and LangGraph for orchestration. These are exactly what Saurav built the demo with. The technical approach discussed in this meeting is the technical approach being demonstrated today.

6. **Competition is real but undefined.** Andrew said "we've been talking to a lot of different vendors" and acknowledged "no one has a pre-built package." By Set 05, we learn Sephora told all other vendors no.

## What Happens Next

The technical deep dive with Malika/Sergey (Set 04) where actual materials are shared, Track A (Cognos MCP) and Track B (ETL/DataStage) are defined, and the demo scope is agreed upon.
