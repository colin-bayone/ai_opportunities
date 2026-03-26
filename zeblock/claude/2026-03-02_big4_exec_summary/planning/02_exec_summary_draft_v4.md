# Zeblok Partnership: Executive Summary

**Meeting Date:** March 2, 2026
**Attendees:** Mouli Narayanan (CEO, Zeblok), Suraj KP, Priya Kalyanasundaram, Colin Moore
**Prepared by:** Colin Moore, Director of AI

---

## Overview

BayOne met with Mouli Narayanan, founder and CEO of Zeblok Computational, to explore a technology partnership centered on AI infrastructure deployment. The conversation was productive, with clear alignment on potential collaboration and concrete next steps agreed, including a target announcement at GTC NVIDIA in mid-March.

**Bottom line:** This is a real opportunity worth pursuing. It positions BayOne beyond staffing and opens a path into defense. However, the value is narrower than the pitch suggests, and BayOne should proceed with a realistic assessment of where the opportunity lies.

---

## About Zeblok

Zeblok is a small company (~20 people) founded in 2019, headquartered at Stony Brook University's tech incubator. Their flagship product, Ai-MicroCloud, is an AI infrastructure platform designed to deploy complete AI/ML environments on-premises, at the edge, or in hybrid cloud configurations.

**Mouli's background:** ~20 years on Wall Street, former Chief Architect at JP Morgan where he built their 10,000-CPU private computing platform before "cloud" was a term. Deep infrastructure credentials, published in IEEE, holds a patent in messaging systems.

**Key technical claims:**
- Deploy a complete AI cloud environment (Kubernetes, storage, DevSecOps) anywhere in minutes, including fully air-gapped
- 75-80% GPU reduction through memory offload to high-bandwidth memory (early benchmarks with unnamed partner)
- Post-quantum cryptography for hub-to-edge communications
- Policy-driven orchestration across hybrid resource pools (on-prem + cloud)

**Business claims:**
- Defense relationships including 3-4 star general access and a TS-cleared advisor
- Portfolio company in a defense-focused AI fund
- ISV partnerships in education (agentic learning), financial services, and quality engineering

---

## Strengths

### 1. Deployment Speed and Automation

Zeblok claims their platform can stand up a complete AI cloud environment (Kubernetes, object storage, DevSecOps, model serving) in minutes rather than weeks. Five years of automation development has gone into reducing the complexity of air-gapped and hybrid deployments. If validated, this is meaningful for customers who need rapid AI capability deployment without lengthy infrastructure projects.

### 2. GPU Efficiency Claims

The 75-80% GPU reduction through memory offload is a significant claim. If accurate, this addresses real pain points: GPU scarcity, power consumption at the edge, and cost. For defense scenarios specifically, where power translates to detectability, this could be a genuine differentiator. Early benchmarks exist with a partner company; validation during platform access will be important.

### 3. Defense Market Alignment

Air-gapped deployment is not optional for classified or ITAR-controlled workloads; it is required. Zeblok's architecture supports disconnected, degraded, and intermittent (DDI) operations, hub-to-edge topology, and claims to be the first platform implementing post-quantum cryptography for edge communications. Their active pursuit of defense (relationships with senior military leadership, TS-cleared advisor, defense-focused AI fund) suggests this is a genuine focus, not an afterthought.

BayOne's fit: Colin's prior clearance and defense systems experience, plus BayOne's talent engine for US Persons, positions the firm well to execute in this vertical.

### 4. Strategic Positioning for BayOne

This partnership directly addresses BayOne's transition from staffing to delivery company. A technology alliance with differentiated AI infrastructure capability, announced at NVIDIA GTC, creates a credible story for existing and prospective customers.

### 5. Manufacturing and High-Reliability Systems

Local model hosting addresses a specific enterprise need: deterministic, version-locked AI behavior. In manufacturing and engineering systems, automatic model updates can change production behavior unpredictably. Fixing a model version locally, with no external dependencies, provides the stability these environments require.

---

## Critical Scope Determination

Zeblok's offering combines three distinct value propositions (air-gapped infrastructure, GPU optimization, and agentic software tools), each of which appeals to a different buyer with different needs:

| Value Proposition | Who Actually Cares | Why |
|-------------------|-------------------|-----|
| **Air-gapped infrastructure** | Defense | Required for classified/ITAR workloads |
| **GPU optimization** | Organizations running local models at scale | Niche; most use cloud models |
| **Agentic software tools** | Broader enterprise | But only if accessible without the rest |

For defense, the full bundle makes sense. These customers need air-gap capability, may benefit from edge optimization, and want integrated solutions. The value propositions align.

For everyone else, the addressable market is narrow. A corporate L&D team wanting AI-powered upskilling does not care about Kubernetes deployments. A retailer exploring AI assistants is not evaluating GPU memory offload. These buyers would simply use Claude via API and proceed with existing solutions.

**The partnership opportunity depends on one question: Can Zeblok's agentic capabilities operate independently of the full Ai-MicroCloud stack?**

- If yes → BayOne has a defense play (full stack) and a broader enterprise play (agentic tools on existing infrastructure)
- If no → This is primarily a defense-focused partnership, and positioning for retail/education is aspirational

This must be clarified in the follow-up call before scoping the opportunity.

---

## Supporting Considerations

### Market Fit by Vertical

| Vertical | Fit | Notes |
|----------|-----|-------|
| Defense | Strong | Full stack required; clear alignment |
| Manufacturing | Strong | Version-locked models, high-reliability systems |
| Retail | Narrow | Value only in agentic tools, not infrastructure |
| Education | Narrow | Value only in agentic tools, not infrastructure |

Zeblok referenced an education partnership, but this is with Stony Brook University, where they are incubated. That is a convenient pilot, not market validation. Broader education and retail opportunities depend on the unbundling question above.

### Local Models and GPU Economics

The GPU efficiency claims (75-80% reduction) apply specifically to local model hosting, and local model hosting serves a specific set of use cases.

In 2026, frontier model capability is commoditized. Organizations expect Opus 4.5-class performance as the baseline, and cloud providers deliver it with integrated tooling, continuous updates, and rapid feature velocity. Local models (Llama, Mistral, fine-tuned variants) can achieve strong performance for specific tasks, but maintaining feature parity with cloud ecosystems over time requires substantial ongoing investment. It is straightforward to match a capability at a point in time; it is difficult to sustain that parity as cloud providers continuously evolve. Recent developments like Manus or open-source alternatives may perform well in isolation, but organizations evaluating long-term AI strategy consider whether these will stand the test of time.

Local model hosting makes sense for organizations with specific requirements: air-gap mandates, version-lock needs, or regulatory constraints that preclude cloud. For everyone else, frontier models via cloud are the practical default. The comparison is not Zeblok versus Azure; a typical enterprise would simply use Claude via API.

This is not a criticism of local models or Zeblok's technology. Each approach has its fit. The point is clarity on which customers actually need on-prem AI infrastructure.

### Competitive Landscape

Air-gapped AI infrastructure is an established market with validated demand:

| Player | Notes |
|--------|-------|
| **Microsoft Azure Local** | Disconnected operations GA Q1 2026 |
| **Google Distributed Cloud** | IL6 authorized, US Air Force & Navy deployments |
| **D2iQ Kubernetes Platform** | FIPS 140-2 validated, Lockheed/Northrop partnerships |
| **Rancher Government Solutions** | DISA STIG validated, tactical edge deployments |

This validates market demand. It also means Zeblok's differentiation needs to be specific: speed of deployment, GPU efficiency, ISV ecosystem, or partnership model. A company of Zeblok's size succeeds through focus and execution, which is where a delivery partner like BayOne adds value.

### Defense Execution

Defense is a credible target market, but execution requires more than relationships: established prime partnerships, past performance references, US Persons throughout the delivery chain, and certifications (CMMC, FIPS 140-2, etc.).

This is where BayOne contributes. BayOne brings delivery capacity, US Persons talent, and experience in regulated environments. The partnership is mutually reinforcing: Zeblok brings the platform and relationships, BayOne brings the execution capability.

---

## Questions for Follow-Up

| Question | Why It Matters |
|----------|----------------|
| Can agentic tools run standalone on existing customer infrastructure? | Determines addressable market beyond defense |
| Any delivered defense contracts or named prime partnerships? | Validates defense execution capability |
| Current certification status (FIPS 140-2, CMMC mapping, SOC 2)? | Affects timeline for defense opportunities |
| What investment is required for the Innovation Lab? | Informs commitment level |

---

## Agreed Next Steps

| Action | Owner | Timeline |
|--------|-------|----------|
| Execute mutual NDA | Both parties | Immediate |
| Platform access for Colin | Zeblok | Within days |
| Follow-up call on investment sizing | Both parties | TBD |
| Target announcement | Both parties | GTC NVIDIA, mid-March |

**Proposed structure:** "Bay One Innovation Lab powered by Zeblok Labs," a co-development environment in Bay Area, initially focused on retail vertical with clear path to defense.

---

## Recommendation

**Proceed. This partnership offers mutual value.**

Zeblok has built a technically differentiated platform with clear applicability in defense and high-reliability environments. What they need is delivery capacity, customer relationships, and execution muscle, which is exactly what BayOne brings. BayOne needs a technology story that positions the firm beyond staffing, which is exactly what Zeblok offers.

**Immediate actions:**
- Execute NDA and obtain platform access for Colin's technical evaluation
- Clarify standalone tool availability in follow-up sizing call
- Confirm defense delivery track record and certification status
- Proceed with GTC announcement as planned

**Focus areas:**
- Defense is the strongest fit; pursue with appropriate investment in US Persons and clearance pathways
- For retail and education, position around agentic capabilities rather than infrastructure
- Use the Innovation Lab as a proving ground before broader customer rollout

This partnership advances BayOne's strategic direction. The key is matching positioning to where the value actually is: defense and specialized manufacturing for the full stack, agentic tools for broader enterprise.
