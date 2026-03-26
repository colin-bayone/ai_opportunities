# Lam Research - Client Research

**Date:** 2026-03-17
**Research Method:** File-by-file reading
**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/source/ai_opportunities_catalog (1).md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/source/ai_opportunities_catalog.md

---

## PROJECT: Custom NER/Redaction for IP Protection

**Type:** Custom AI / NLP / IP Protection
**Status:** Discovery call completed 3/12/2026, follow-up with technical lead Daniel expected

### Description
Lam Research has pulled back all AI and GenAI usage organization-wide due to IP concerns. Their customers (TSMC, Samsung, Intel, Micron, SK Hynix) are direct competitors with each other, and Lam sees production data from all of them. A leak between customers would be catastrophic. They need a custom detection and redaction layer to protect sensitive information before safely re-enabling AI tools for their workforce.

### Two Use Cases

**Use Case 1: Self-Help Search**
Users search knowledge bases for troubleshooting. Over-restriction blocks useful cross-customer solutions. A Samsung solution exists but an Intel user can't see it because it's restricted. Goal is to surface solutions without leaking customer-specific IP.

**Use Case 2: Escalation / Ask for Help**
Users open tickets, describe problems, and attach transcripts. They inadvertently include customer names, fab numbers, and sensitive details in unstructured text. This breaks into two sub-problems:
- Real-time detection at input (must be fast, 2-5 seconds, under 1% false positive rate)
- Batch redaction before data enters the general knowledge pool (accuracy matters more than speed)

### What They've Tried
- Transformer models, SpaCy, Azure AI models, rule-based models
- Best result: 17% false positive rate (Azure AI model), far from under 1% target
- 1000+ hours of labeling paused due to cost and maintenance burden
- Core difficulty: Spelling variations and Lam-specific patterns (Fab11, F11, fab-11, FAP space 11, etc.)

### Why This Is Hard
Lam's IP environment is extremely locked down. Dedicated routers per machine globally, everything through VPN, machines fully encrypted and isolated. Their customers are competitors with each other, and Lam sees production data from all of them.

### Colin's Assessment
Lam is extremely early in their journey and technically infantile in this area. They need a data plane desperately and have not even investigated Microsoft Purview at all. They tried intern-level classification and don't seem to understand the difference between classification versus redaction. Prior venture with Accenture failed. This is a ripe opportunity to be plucked - they simply need to either use enterprise tools or have a quick understanding with us on the right approach.

**Colin's Technical Approach:** Undecided at this point. Would pursue with actual enterprise-grade tools, as they have not even begun pursuing this properly yet.

Colin has direct relevant experience from Coherent Corp in the same industry.

### Stakeholders
**Lam Research:**
- Bradley Estes (Managing Director, Knowledge & Advanced Services) - Decision maker with authority
- Mikhail Krivenko (Head of Product)
- Daniel (Technical Lead, not yet met)

**BayOne:**
- Colin Moore (Director of AI)
- Pratik Sharda
- Surej KP
- Amit Grover

### Technologies
- Current tech stack: Azure (AI Foundry, Purview)
- Extremely locked-down security: Dedicated routers, VPN-only, full encryption, closed-loop machines

### Budget/Timeline
- Budget: Not yet confirmed, but Brad indicated he has latitude
- Timeline: Follow-up meeting being scheduled with Daniel
- Status: Discovery completed 3/12/2026

### Opportunity Size
Potentially significant. Real technical problem with well-defined success metric. Client is sophisticated and driving engagement structure properly.

### Process Note
There is friction with the sales team because of a failure to set expectations and communicate. This has been raised up to the appropriate persons at this point, but still is something to keep an eye on. Communication and scheduling around this opportunity have had friction.

### Qualification Assessment
- Decision maker with authority: Yes (Brad owns full lifecycle from business case to execution)
- Confirmed problem statement: Yes (specific, articulated, with measurable failure criteria)
- Budget: Not yet confirmed, but Brad indicated latitude
- Revenue potential: Medium to large depending on scope
- Colin's domain fit: Strong (direct experience building similar systems at Coherent in same industry)
