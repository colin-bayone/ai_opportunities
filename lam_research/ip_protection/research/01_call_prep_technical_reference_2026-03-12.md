# 01 - Call Prep: Technical Reference

**Source:** /lam_research/ip_protection/source/lam_call_prep_2026-03-12.txt
**Source Date:** 2026-03-12 (Pre-discovery call preparation document)
**Document Set:** 01 (Call Prep)
**Pass:** Technical reference material extraction

---

## Microsoft Stack Reference

### Microsoft Sentinel
- **What It Is:** SIEM/SOAR platform
- **What It Does:** Aggregates alerts, triggers playbooks
- **What It Does NOT Do:** Content detection. It does not block content. It alerts on events.
- **Key Insight:** If Lam is relying on Sentinel as their primary guardrail, that is an architecture misunderstanding. Sentinel can tell you something happened. It cannot prevent it from happening.

### Microsoft Purview DLP
- **What It Is:** The actual guardrail layer for content detection
- **What It Does:** Detects sensitive content based on Sensitive Information Types (SITs) and sensitivity labels. Can block Copilot from processing labeled content.
- **Current State (as of March 2026):** Prompt-based SIT detection is in preview, GA expected late March 2026
- **Key Limitation:** Out-of-the-box SITs cover standard categories (SSN, credit cards, medical records). They do NOT cover semiconductor-specific IP like customer names in production context, process parameters, or yield data.

### Azure AI Content Safety / Prompt Shields
- **What It Is:** Real-time detection at the model layer
- **What It Does:** Detects prompt injection, jailbreak attempts, harmful content
- **Scope:** Model-layer protection, not enterprise content classification

### Defender for Cloud Apps
- **What It Is:** CASB (Cloud Access Security Broker) functionality
- **What It Does:** Provides visibility into shadow AI and SaaS usage
- **Relevance:** Could quantify the shadow AI problem that Lam likely has

## Shadow AI Industry Data

- 98% of organizations report unsanctioned AI use
- 68% of employees use free-tier AI tools via personal accounts
- 77% of AI users copy/paste data into chatbot queries
- 1 in 5 organizations experienced a breach due to shadow AI
- Shadow AI breaches cost $670K more than standard breaches
- **Samsung Incident (2023):** Engineers leaked semiconductor source code via ChatGPT. This is directly analogous to Lam's fear. Same industry, same type of data, same vector.
- **Counter-example:** One healthcare system that provided approved AI alternatives saw 89% reduction in unauthorized use. The fix is enabling, not blocking.

## AI Governance Maturity Model

| Stage | Description | Characteristics |
|-------|-------------|-----------------|
| 1 | Ad-hoc | Shadow AI, no inventory, no governance |
| 2 | Pockets of success | Inconsistent practices, some controlled experiments |
| 3 | Systematic | CoE, governance framework, standards |
| 4 | Integrated | Governance across the organization |
| 5 | Optimized | Continuous monitoring and improvement |

**Assessment:** Lam pulling back ALL AI usage suggests reactive Stage 1-2 maturity. The opportunity for BayOne is to help them build Stage 3 systematic governance while solving the immediate technical problem.

## Guardrail Testing Reference

### Key Metric
- **Attack Success Rate (ASR):** Percentage of successful attacks over total attempts

### Interpreting "20% Error Rate"
The 20% figure could mean:
- **False negatives:** 20% of sensitive content getting through (most dangerous from IP perspective)
- **False positives:** 20% of legitimate content being blocked (productivity impact)
- **Combined rate:** Needs clarification on the call

### Available Red Teaming Tools
- Microsoft PyRIT
- Nvidia Garak
- F5 AI Red Team
- Many enterprises do not use these systematically
- Testing methodology matters as much as the guardrails themselves

## Colin's Relevant Experience Mapping

| Lam's Situation | Colin's Analogous Experience |
|-----------------|------------------------------|
| Semiconductor IP (customer-competitive data) | Coherent Corp (same industry: semiconductor/defense equipment) |
| Regulatory sensitivity | ITAR, CMMC, DFARS, NIST 800-171 at defense primes |
| AI at scale with IP constraints | GenAI deployed to 40,000+ users with governance |
| Shadow AI concerns | Built bidirectional IP protection for China operations |
| Detection/redaction needs | Built data classification layers, early-alert mechanisms, automated intervention |
| Exfiltration risk | Intercepted China-related exfiltration attempt before regulatory consequences |
