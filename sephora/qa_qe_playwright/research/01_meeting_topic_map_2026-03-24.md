# 01 - Meeting: Topic Map

**Source:** /sephora/qa_qe_playwright/source/vabhav_3_24_2026.txt
**Source Date:** 2026-03-24 (Introductory meeting / discovery conversation)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Sephora QE Current State
- Vaibhav's background (Walmart Labs, e-commerce migration, Azure, now QE)
- AI mandate since August 2025
- AMP (Agentic Micro Pod) model transition
- Selenium-to-Playwright migration (POCs complete, new development on Playwright)
- Platform evolution: DataIQ -> Claude/Advent -> Nova (homegrown, LiteLLM-based)
- QE COE team under Deepika (~5 people)
- Gaps: visual QA, translations/localization, ADA compliance, mobile farms

### 2. Sephora Agent Strategy
- QE agents across lifecycle phases (acceptance criteria validation, test case generation, automation, CICD)
- Unified knowledge base initiative (single source across all functions)
- MCP server integration requirement for all tools
- Relevancy testing for agentic workflow outcomes
- Trust and confidence scoring challenges
- Metrics and decision-making support
- "Leads becoming decision-makers, not engineers"

### 3. BayOne QE Approach (Colin's Presentation)
- Deterministic-first philosophy ("bring in AI last")
- State graph mapping of codebase (autonomous exploration)
- CICD pipeline integration with state graph
- Coverage model (recursive downstream dependencies, not just function coverage)
- Playwright as core framework + multi-model strategy (Claude 90%, Gemini for visual, minimal OpenAI)
- Agent evaluation like people evaluation (reinforcement learning from human feedback)
- Observability and transparency for agent performance
- "System autonomy" over "autonomous systems"

### 4. Staffing Opportunities
- Deepika's open agentic AI roles (~$120/hr onsite, flexibility possible)
- Vaibhav's hiring philosophy ("give me a star, I'll find the role")
- Offshore/nearshore/onsite dynamics and 6-12 month nearshore shift
- AMP model driving co-location requirements
- Colin's screening as differentiator
- Prior candidate submissions (Santosh, Raghav, the "purple squirrel")

### 5. Upskilling and Training
- BayOne training for all new hires (AI engineering baseline)
- Incubation model concept (work + learn simultaneously)
- Vaibhav's concern: offshore not upskilling at speed
- Upskilling existing teams as a service offering
- "Staying on the cutting edge" advisory value

## Approved File Plan

| File | Agent Focus |
|------|------------|
| `01_meeting_sephora_qe_current_state_2026-03-24.md` | Sephora's QE journey, current tools, gaps, organizational structure |
| `01_meeting_sephora_agent_strategy_2026-03-24.md` | Agent lifecycle, knowledge base, trust/confidence, Nova platform |
| `01_meeting_bayone_qe_approach_2026-03-24.md` | Colin's methodology, state graph, coverage, multi-model, observability |
| `01_meeting_staffing_opportunities_2026-03-24.md` | Deepika roles, rates, hiring philosophy, geographic strategy |
| `01_meeting_upskilling_and_training_2026-03-24.md` | Training offerings, incubation model, advisory value |
| `01_meeting_summary_2026-03-24.md` | Final summary referencing all files (written last, by main session) |
