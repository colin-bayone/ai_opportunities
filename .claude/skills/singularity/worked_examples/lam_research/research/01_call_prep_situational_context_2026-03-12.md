# 01 - Call Prep: Situational Context

**Source:** `source/lam_call_prep (1).txt`
**Source Date:** 2026-03-12 (prepared immediately before discovery call)
**Document Set:** 01 (Call Prep)

---

## Company Profile

- **Lam Research** - $17B+ revenue, ~17,000 employees
- HQ: Fremont, CA
- Core business: Wafer fabrication equipment (etch, deposition, clean)
- Key customers: TSMC, Samsung, Intel, Micron, SK Hynix
- Critical role in AI chip manufacturing supply chain

## Why IP Protection Is Existential for Lam

Lam occupies a unique and dangerous position: they see production data from customers who are direct competitors with each other. TSMC, Samsung, Intel, and Micron are all Lam customers, and Lam has visibility into their respective production processes.

If Customer A's yield data leaked to Customer B:
- Catastrophic business relationship damage
- Potential regulatory/antitrust consequences
- Loss of the trusted-vendor position that their entire business model depends on

This is not a nice-to-have compliance exercise. It is existential.

## What We Knew Going In

From prior emails and a transcript (exact sources referenced in call prep):

- Lam is on Azure stack: AI Foundry + Microsoft Sentinel
- Current guardrails are "failing" to their expectations
- They have pulled back ALL AI and GenAI usage organization-wide due to IP concerns
- Their stated goal: get error rate below 20% before production deployment

## Working Hypotheses (Pre-Call)

These were BayOne's working theories going into the call - explicitly flagged as unvalidated:

1. **"Failing guardrails" likely means Purview DLP, not Sentinel.** Sentinel is SIEM (aggregates alerts, triggers playbooks). It does not do content detection. If Lam thinks Sentinel is their guardrail, that's an architecture misunderstanding.

2. **Microsoft's out-of-the-box Sensitive Information Types don't cover semiconductor IP.** Customer names, process parameters, yield data, fab designations - none of these are in Microsoft's standard SIT library.

3. **Custom SIT configuration is non-trivial and likely not fully implemented.** Building custom SITs that handle the variation in semiconductor terminology (Fab11, F11, fab-11, FAP space 11) requires significant effort.

4. **Shadow AI may be a bigger factor than admitted.** Industry data: 98% of organizations report unsanctioned AI use, 68% of employees use free-tier tools via personal accounts. Lam's "ban all AI" approach likely pushes usage underground.

## Key Contacts

**Bradley Estes** - Managing Director, Knowledge & Advanced Services
- Background: Progressed from Product Support Manager to Senior Director of Knowledge Management
- Focus: Knowledge governance, information governance, product support
- Role in this engagement: Decision maker. Knowledge Management = how information flows through the org. He owns the problem space.

**Mikhail Krivenko** - Head of Product
- Expected to present the technical problem statement on the call

**Daniel** - Technical Lead
- Not yet met at time of call prep
- Expected to be the follow-up contact for deeper technical discussion

## Security Posture Context

From Lam's CISO Jason Callahan (public quote): "We are operating from the zero-trust point of view. But we all share intellectual property. Fundamentally, we as security people don't trust encryption."

This signals: Lam is a security-sophisticated organization. They've already tried things. They understand the tension between enabling productivity and protecting IP. This is not a naive client.

## Colin's Relevant Experience

BayOne's positioning going into this call rested on Colin Moore's direct experience in analogous environments:

- **Detection & redaction systems:** Built data classification layers, early-alert mechanisms, automated intervention. Detection systems for restricted technical data, drawings, controlled information. Intercepted an exfiltration attempt (China-related) before regulatory consequences.

- **Governance frameworks:** Primary advisor to Legal, Compliance, Cybersecurity on AI governance. Deployed GenAI to 40,000+ users while navigating ITAR, CMMC, DFARS, NIST 800-171. Experience with defense primes (Raytheon, Northrop Grumman) - similarly sensitive environments.

- **Shadow AI:** Built bidirectional IP protection for China operations. Core philosophy: the fix isn't blocking, it's enabling the right tools with proper controls. Governance + usability, not governance vs. usability.

- **Industry overlap:** Direct relevant experience from Coherent Corp in the same semiconductor equipment industry.
