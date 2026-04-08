# 01 - Call Prep: Summary

**Source:** /lam_research/ip_protection/source/lam_call_prep_2026-03-12.txt
**Source Date:** 2026-03-12 (Pre-discovery call preparation document)
**Document Set:** 01 (Call Prep)
**Pass:** Summary

---

## Overview

Document Set 01 decomposes BayOne's pre-call preparation for the Lam Research discovery meeting on March 12, 2026. The call prep is a structured document written by Colin Moore covering company background, known contacts, discovery questions, technical reference material, and Colin's relevant experience points.

## Files in This Set

1. **01_call_prep_people_2026-03-12.md** - Two known Lam contacts (Bradley Estes, Managing Director; Mikhail Krivenko, expected problem presenter) plus CISO Jason Callahan referenced for security culture context. Colin's experience points mapped to the engagement.

2. **01_call_prep_situational_context_2026-03-12.md** - Lam Research profile ($17B revenue, 17,000 employees, wafer fab equipment). Why IP protection is existential: customers are direct competitors, data leakage between fabs is catastrophic. Pre-call knowledge: Azure stack, guardrails "failing," all AI pulled back, 20% error rate target. Working hypotheses about Purview DLP vs. Sentinel confusion and missing custom SITs.

3. **01_call_prep_discovery_strategy_2026-03-12.md** - Eight categories of discovery questions (understanding the failure, tool stack, IP taxonomy, shadow AI, governance structure, what has been tried, leakage vectors, timeline and success). Signals to listen for that distinguish a configuration/governance gap from a genuine custom build requirement.

4. **01_call_prep_technical_reference_2026-03-12.md** - Microsoft stack breakdown (Sentinel, Purview DLP, Azure AI Content Safety, Defender for Cloud Apps). Shadow AI industry statistics. AI governance maturity model (5 stages, Lam assessed at Stage 1-2). Guardrail testing metrics and red teaming tools. Colin's experience mapped to Lam's specific situation.

## Key Themes Going Into the Call

- **Listen first, validate hypotheses through questions, do not assume.** The call format (Lam presents, then Q&A) reinforces this.
- **The 20% error rate is the anchor metric.** Need to clarify what it measures (false negatives, false positives, or combined).
- **Out-of-the-box Microsoft tools likely cannot solve this.** Semiconductor IP (customer names in production context, process parameters, yield data) is not covered by standard SITs.
- **Shadow AI is probably a bigger factor than admitted.** Industry data strongly supports this.
- **Brad controls the engagement structure.** He set the call format. He is deliberate and structured. Do not try to sell. Demonstrate understanding.

## Open Questions for the Call

1. What does "failing" specifically mean? Which tool, which failure mode?
2. What has already been tried and ruled out?
3. What does the IP taxonomy look like? What is sensitive in their context?
4. Who owns AI governance? Is there a formal structure?
5. What is the timeline pressure and success criteria?
