# 07 - Demo Meeting: Summary

**Source:** /sephora/edw_modernization/source/edw_demo_4-2-2026_formatted.txt
**Source Date:** 2026-04-02 (Demo Meeting)
**Document Set:** 07 (The Actual Demo)
**Pass:** Summary (final document for set)

---

## What This Meeting Was

The culminating demo of the Sephora EDW Modernization engagement. Colin presented a live run of the multi-agent pipeline to Andrew Ho, Grishi, Maher Burhan, Malika Seth, and a new attendee (Vishal Sharma). The pipeline ran end-to-end on Sephora's actual data in approximately 13.5 minutes. The remaining ~40 minutes were intensive Q&A covering validation methodology, architecture, security, scaling, deployment, portability, and next steps.

## Key Outcome

The demo landed. Andrew said "very, very nice" and announced the team will go back, discuss, and determine next steps. This is the first meeting in the engagement that ended without a new gate (no request for another demo, more information, or additional proof). The next action is on Sephora's side.

## Documents in This Set

| File | What It Covers |
|------|---------------|
| `07_demo_people_2026-04-02.md` | All attendees with utterance counts, Vishal Sharma identified as new, dynamics analysis |
| `07_demo_technical_qa_2026-04-02.md` | 29 technical questions in table format with timestamps, answers, and analysis of anticipated vs surprise questions |
| `07_demo_architecture_and_security_2026-04-02.md` | Azure isolation confirmation, VNet deployment exchange, container options, database options, LangSmith positioning, cost numbers, scaling architecture |
| `07_demo_scaling_and_next_steps_2026-04-02.md` | Andrew's "day one" question, Colin's exploration SOW pitch, parallel scaling explanation, closing dynamics parsed word by word |
| `07_demo_new_requirements_2026-04-02.md` | 7 new requirements not in original scope: data reconciliation, migration detection, schema mismatch handling, source-to-target mapping, ADF alternative, portability, sample data reading. 5 of 7 blocked by same thing: no system access. |
| `06-07_changes_2026-04-02.md` | Bridge: demo worked, prep was accurate, Maher validated as predicted, Vishal is new, 7 new requirements surfaced |

## The Five Things That Matter Most

1. **The demo worked and impressed.** Pipeline ran 13.5 minutes on real data. No crashes. Andrew's closing: "Very, very nice. Thank you very much." First meeting with no new gate requested.

2. **Maher was satisfied.** 100 utterances, every predicted question asked and answered. His framing at the end: "This is the transition period. We use it to migrate. When we migrate, we don't need it anymore." He sees the tool as temporary and healthy. The Azure isolation answer killed the security objection in one exchange.

3. **The exploration SOW pitch landed.** Andrew asked "what would be step one?" and Colin delivered the two-week proposal. Andrew responded with "Got it. OK." and moved to wrap-up. No pushback, no counter-proposal, no request for alternatives.

4. **Five of seven new requirements are blocked by the same thing: system access.** Data reconciliation, migration detection, schema mismatch handling, live data reading, and Cognos MCP all need access to Sephora's production systems. This reinforces the exploration SOW as the natural next step. Access implies contract.

5. **Vishal's portability concern is manageable but real.** He explicitly wants Sephora to be able to run the system independently without BayOne. Colin addressed it well (agents are customizable, system is temporary, you keep everything). Maher reinforced the "transition period" framing. But this will need to be addressed clearly in the engagement proposal.

## What Happens Next

The ball is in Sephora's court. Andrew said the team will discuss and determine next steps. Zahra and Neha offered follow-up time the next day including Mani. The commercial conversation (exploration SOW, pricing, access provisioning) is the next phase.

Key actions for BayOne:
- Send the demo package document and architecture diagram to the Sephora team
- Follow up to schedule the session Zahra offered (include Mani)
- Prepare the formal exploration SOW document for when they are ready
- Update the engagement proposal to address the 7 new requirements surfaced in the demo
