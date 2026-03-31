# 01 - Meeting: Summary

**Source:** /sephora/qa_qe_playwright/source/vabhav_3_24_2026.txt
**Source Date:** 2026-03-24 (Introductory meeting / discovery conversation)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Summary of all files in Set 01

---

## Meeting Overview

Introductory meeting between BayOne (Colin Moore, Zahra, Neha, Rahul Bobbili) and Vaibhav from Sephora's QE organization. The conversation covered two parallel tracks: outcome-based project work (QA/QE automation using generative AI and Playwright) and staffing/augmentation opportunities.

## Files in This Set

| File | Focus |
|------|-------|
| `01_meeting_people_2026-03-24.md` | All attendees, mentioned individuals, dynamics, relationships |
| `01_meeting_topic_map_2026-03-24.md` | Topic identification and approved file plan |
| `01_meeting_sephora_qe_current_state_2026-03-24.md` | Sephora's QE journey, tools, gaps, AMP model, platform evolution |
| `01_meeting_sephora_agent_strategy_2026-03-24.md` | QE agents across lifecycle, knowledge base, trust/confidence, Nova platform |
| `01_meeting_bayone_qe_approach_2026-03-24.md` | Colin's methodology: deterministic-first, state graph, Playwright, multi-model, observability |
| `01_meeting_staffing_opportunities_2026-03-24.md` | Deepika's roles, rates, hiring philosophy, geographic strategy |
| `01_meeting_upskilling_and_training_2026-03-24.md` | Training offerings, incubation model, advisory value |

## Key Takeaways

### Sephora's Position
- QE has been the "slowest horse in the race" but has made tremendous progress in the last two years
- AI mandate since August 2025: no option for non-AI approaches on anything new
- Entire SDLC is being "agenticized" from requirements through deployment
- Transitioning to AMP (Agentic Micro Pod) model: lean 2-3 person teams, small/frequent enhancements
- Migrating from Selenium to Playwright (POCs done, new development already on Playwright)
- Platform evolution: DataIQ (cost) -> Claude/Advent -> Nova (homegrown, LiteLLM, built by Nikhil's team)
- QE COE under Deepika (~5 people) owns the agent roadmap
- Identified gaps: visual QA, translations/localization, ADA compliance, mobile farms
- 2026 roadmap already exceeded: Q3 deliverables completed by March

### Trust and Confidence (Central Theme)
- Vaibhav described trust in agents as "a big hurdle we have to cross together"
- Current trust level: 40-50% range, the jump to 60-80% requires thorough human review
- Computing a composite trust index remains unsolved ("How do you compute 4.8? I don't know")
- Colin presented a reinforcement learning approach: human approvals build agent track record, threshold for human-in-the-loop decreases over time
- Strong alignment between both sides on this philosophy

### BayOne's Positioning
- Deterministic-first philosophy resonated with Vaibhav
- State graph approach to codebase mapping (dependency mapping, dead code detection, targeted test triggering)
- Playwright expertise is directly relevant (Microsoft-native, AI-friendly)
- Multi-model strategy (Claude ~90%, Gemini for visual) aligns with Sephora's tool-agnostic approach
- Agent evaluation framework (like evaluating people) addressed Vaibhav's trust concerns directly
- Colin's technical depth and screening ability positioned as key differentiators

### Staffing Opportunities
- Deepika has open agentic AI roles (~$120/hr onsite, flexibility exists, working with HR on rates)
- Vaibhav will place strong talent even without a defined open role
- Geographic shift predicted: offshore -> nearshore (South America, Canada) in 6-12 months
- AMP model forces co-location, driving nearshore/onsite premium
- Remote onshore at nearshore rates is an attractive option (Central/Eastern time zones)
- Budget holders beyond Deepika: Ashweta, Lakshmi, Priyanka (QE leads)
- Colin's screening provides quality assurance that aligns with Vaibhav's interview philosophy

### Training and Upskilling
- BayOne training for all new hires (AI engineering baseline)
- Incubation model: work + learn simultaneously, alternative to contract-to-hire
- Upskilling existing teams as a service offering
- Vaibhav confirmed need: "not just creating agents, you have to be able to use and orchestrate them"
- Offshore upskilling speed gap is a real concern driving geographic decisions

## Open Questions and Next Steps

1. **Deepika's roles** - Are they filled? Need to reconnect now that she is back from PTO
2. **Nearshore/offshore candidates** - Vaibhav asked to see resumes; Colin-screened candidates ready to send
3. **Outcome-based project** - Vaibhav is open to a starter project ("even if it's small, even if it's just to test us out"). No specific scope defined yet
4. **Nova platform** - What is the timeline? What does this mean for BayOne's tooling choices?
5. **AMP model status** - Is it live? Which teams? Implications for QE team structure?
6. **Trust index** - Vaibhav wants to solve this. BayOne has a framework. Natural collaboration point
7. **Upskilling** - Is there appetite for formal training engagement beyond staffing?
8. **CDW project** - Mentioned as needing a completely different team. What is it?

## Immediate Actions for BayOne

1. Send Colin-screened candidates to Vaibhav (nearshore and offshore)
2. Reconnect with Deepika on open COE roles
3. Determine if a small outcome-based project can be scoped for QE automation
4. Consider a strategy discussion (Set 02) to define BayOne's approach to this engagement
