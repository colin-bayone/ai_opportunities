# 01 - Call Prep: Technical Reference

**Source:** `source/lam_call_prep (1).txt`
**Source Date:** 2026-03-12 (prepared immediately before discovery call)
**Document Set:** 01 (Call Prep)

---

## Microsoft Stack Reference

This was the reference context BayOne had going into the call for understanding Lam's Azure environment.

### Sentinel
- SIEM/SOAR platform
- Aggregates alerts, triggers playbooks
- **Not** a content detection tool
- Key insight: If Lam is relying on Sentinel as their primary guardrail, that's an architecture misunderstanding. Sentinel alerts on events - it doesn't block content.

### Purview DLP
- The actual guardrail layer for content detection
- Detects sensitive content based on Sensitive Information Types (SITs) and sensitivity labels
- Can block Copilot from processing labeled content
- Prompt-based SIT detection was in preview at time of call prep, GA expected late March 2026

### Azure AI Content Safety / Prompt Shields
- Real-time detection of prompt injection, jailbreak attempts, harmful content
- Model-layer protection
- Different purpose than DLP - focused on adversarial attacks, not IP leakage

### Defender for Cloud Apps
- CASB (Cloud Access Security Broker) functionality
- Provides visibility into shadow AI/SaaS usage
- Relevant to the shadow AI dimension of Lam's problem

## Shadow AI Statistics

Industry data referenced in call prep (sources not cited in original):

| Metric | Value |
|--------|-------|
| Organizations reporting unsanctioned AI use | 98% |
| Employees using free-tier AI tools via personal accounts | 68% |
| AI users who copy/paste data into chatbot queries | 77% |
| Organizations that experienced a breach due to shadow AI | 1 in 5 |
| Additional cost of shadow AI breaches vs. standard breaches | $670K |

**Samsung Incident (2023):** Engineers leaked semiconductor source code via ChatGPT - directly analogous to Lam's fear. This was a known reference point.

**Key insight from prep:** The "ban all AI" approach Lam has taken likely drives shadow AI underground rather than eliminating it. One healthcare system that provided approved AI alternatives saw 89% reduction in unauthorized use. This supports the "governance + usability" framing rather than prohibition.

## AI Governance Maturity Model

Framework used to assess Lam's position:

| Stage | Description |
|-------|-------------|
| Stage 1 | Ad-hoc experiments, shadow AI, no inventory |
| Stage 2 | Pockets of success, inconsistent practices |
| Stage 3 | Systematic CoE, governance framework, standards |
| Stage 4 | Integrated across organization |
| Stage 5 | Optimized with continuous monitoring |

**Pre-call assessment:** Lam pulling back ALL AI usage suggests reactive Stage 1-2 maturity. The opportunity is to help them build Stage 3 systematic governance while solving the immediate technical problem.

## Guardrail Testing Reference

### Key Metric: Attack Success Rate (ASR)
Percentage of successful attacks over total attempts.

### Interpreting Lam's "20% Error Rate"
Three possible meanings (needed clarification on the call):
- **False negatives:** 20% of sensitive content getting through (most dangerous)
- **False positives:** 20% of legitimate content being blocked (productivity impact)
- **Combined rate** - blending both types of error

### Testing Tools Available
- Microsoft PyRIT
- Nvidia Garak
- F5 AI Red Team

Note from prep: Many enterprises don't use these systematically. Testing methodology matters as much as the guardrails themselves.
