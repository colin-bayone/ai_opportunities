# 01 - Call Prep: Situational Context

**Source:** /lam_research/ip_protection/source/lam_call_prep_2026-03-12.txt
**Source Date:** 2026-03-12 (Pre-discovery call preparation document)
**Document Set:** 01 (Call Prep)
**Pass:** Situational context extraction

---

## Company Profile

- **Company:** Lam Research
- **Revenue:** $17B+
- **Employees:** Approximately 17,000
- **HQ:** Fremont, CA
- **Core Products:** Wafer fabrication equipment (etch, deposition, clean)
- **Key Customers:** TSMC, Samsung, Intel, Micron, SK Hynix
- **Industry Position:** Critical to AI chip manufacturing

## Why IP Protection Is Existential for Lam

Lam's customers are direct competitors with each other. Lam sees production data from TSMC, Samsung, Intel, and Micron simultaneously. If Customer A's yield data leaked to Customer B, the consequences are:

1. **Business relationship destruction.** These are multi-billion dollar relationships built on trust that proprietary data stays compartmentalized.
2. **Regulatory and antitrust exposure.** Sharing competitive production data between semiconductor fabs could trigger antitrust investigation.
3. **Industry position risk.** Lam's value proposition depends on being a trusted neutral party that serves all fabs. Lose that trust, lose the business model.

This is not a "nice to have" security improvement. This is an existential business risk.

## What We Know Pre-Call

### Technology Stack
- Azure stack: AI Foundry and Microsoft Sentinel confirmed
- Current guardrails are "failing" to Lam's expectations
- They have pulled back ALL AI and GenAI usage due to IP concerns
- Goal: Get error rate below 20% before production deployment

### Working Hypotheses (Not to Be Presented as Fact)
1. "Failing guardrails" likely means Purview DLP, not Sentinel. Sentinel is SIEM (aggregates alerts, triggers playbooks). It does not block content. If Lam is relying on Sentinel as their primary guardrail, that is an architecture misunderstanding.
2. Microsoft's out-of-the-box Sensitive Information Types do not cover semiconductor IP. Customer names, process parameters, yield data are not standard SIT categories.
3. Custom SIT configuration is non-trivial and likely not fully implemented.
4. Shadow AI may be a bigger factor than Lam is admitting. Industry data shows 98% of organizations report unsanctioned AI use.

### The "Ban All AI" Signal
Lam pulling back ALL AI usage is a strong signal:
- It suggests reactive Stage 1-2 governance maturity (ad-hoc experiments, no systematic framework)
- Banning drives shadow AI underground rather than eliminating it (one healthcare system that provided approved alternatives saw 89% reduction in unauthorized use)
- The Samsung incident (2023) where engineers leaked semiconductor source code via ChatGPT is directly analogous to Lam's fear

## Call Format

Per Bradley Estes' email, the call follows a strict three-step format:
1. Lam presents their problem statement
2. Q&A session
3. BayOne goes away and comes back with a response/approach

The prep document explicitly coaches: "This is discovery. Let them present. Your job is to listen, ask smart questions that draw out information, and demonstrate you understand their world without making assumptions."
