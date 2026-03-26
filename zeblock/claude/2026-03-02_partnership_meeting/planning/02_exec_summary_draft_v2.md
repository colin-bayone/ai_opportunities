# Zeblok Partnership: Executive Summary

**Meeting Date:** March 2, 2026
**Attendees:** Mouli Narayanan (CEO, Zeblok), Suraj KP, Priya Kalyanasundaram, Colin Moore
**Prepared by:** Colin Moore, Director of AI

---

## Overview

We met with Mouli Narayanan, founder and CEO of Zeblok Computational, to explore a technology partnership centered on AI infrastructure deployment. The conversation was productive—clear alignment on potential collaboration, genuine personal rapport, and concrete next steps agreed including a target announcement at GTC NVIDIA in mid-March.

**Bottom line:** This is a real opportunity worth pursuing. It positions BayOne beyond staffing and opens a path into defense. However, the value is narrower than the pitch suggests, and we should proceed with clear eyes on where the fit actually is.

---

## About Zeblok

Zeblok is a small company (~20 people) founded in 2019, headquartered at Stony Brook University's tech incubator. Their flagship product, Ai-MicroCloud, is an AI infrastructure platform designed to deploy complete AI/ML environments on-premises, at the edge, or in hybrid cloud configurations.

**Mouli's background:** ~20 years on Wall Street, former Chief Architect at JP Morgan where he built their 10,000-CPU private computing platform before "cloud" was a term. Deep infrastructure credentials, published in IEEE, holds a patent in messaging systems.

**Key technical claims:**
- Deploy a complete AI cloud environment (Kubernetes, storage, DevSecOps) anywhere in minutes—including fully air-gapped
- 75-80% GPU reduction through memory offload to high-bandwidth memory (early benchmarks with unnamed partner)
- Post-quantum cryptography for hub-to-edge communications
- Policy-driven orchestration across hybrid resource pools (on-prem + cloud)

**Business claims:**
- Defense relationships including 3-4 star general access and a TS-cleared advisor
- Portfolio company in a defense-focused AI fund
- ISV partnerships in education (agentic learning), financial services, and quality engineering

---

## Strengths

### 1. Strategic Positioning for BayOne

This partnership directly addresses BayOne's transition from staffing to delivery company. A technology alliance with differentiated AI infrastructure capability—announced at NVIDIA GTC—creates a credible story for existing and prospective customers.

### 2. Defense Market Entry Point

Defense is where Zeblok's value proposition is most compelling. Air-gapped deployment isn't optional for classified or ITAR-controlled workloads—it's required. Zeblok's architecture aligns with these requirements, and their claimed relationships (while unvalidated) suggest active pursuit of this market.

BayOne's advantages here: Colin's prior clearance and defense systems experience (AGL, laser systems), plus our talent engine for recruiting US Persons. Defense work is heavy but "assured business" with strong margins.

### 3. Manufacturing and High-Reliability Systems

Local model hosting makes sense in one specific scenario beyond defense: when you need deterministic, version-locked AI behavior. In manufacturing and engineering systems, you don't want your model auto-updating and changing production behavior. Fixing a model version locally—with no external dependencies—addresses this.

### 4. Mouli's Credibility and Rapport

Mouli is a legitimate technical founder with deep infrastructure experience. The personal chemistry with Suraj was evident, and there's genuine trust forming. This matters for a partnership that will require ongoing collaboration.

---

## Limitations

### 1. Air-Gapped Value is Defense-Specific

The core pitch—"mini Azure that runs anywhere, including air-gapped"—only resonates where air-gapped is actually required. For retail, education, and most enterprise customers, this isn't a selling point. They prefer Azure/AWS, have existing investments, and won't pivot infrastructure for an AI capability.

No one is going to move off Azure because a 20-person startup says their thing is better. For non-defense verticals, what matters is whether Zeblok's agentic tools can operate independently of the full infrastructure stack.

### 2. Local Models Have Narrow Applicability

The GPU reduction claim (75-80%) only matters if you accept the premise that you're running models locally. But local models—open-source Llama, Mistral, etc.—aren't competitive with frontier models (Claude, GPT-4) for most enterprise use cases.

Local hosting makes sense for: (a) defense/classified, (b) manufacturing version-lock, and (c) true edge disconnected scenarios. It doesn't make sense for healthcare (cloud compliance is mature), financial services (same), or general enterprise work.

One nuance worth noting: data isolation via local hosting can actually be a liability. If Anthropic leaks your data, you have legal recourse. If your local setup breaches, you sue yourself.

### 3. Conflation of Three Different Businesses

Zeblok's pitch blends three distinct value propositions:

| Layer | What It Is | Who Buys It |
|-------|-----------|-------------|
| Infrastructure | "Mini Azure"—K8s, storage, deployment automation | IT/Platform teams |
| Hardware Optimization | GPU memory offload, resource efficiency | ML Engineering |
| Agentic Software | ISV partnerships, solution-oriented AI tools | Business/Functional teams |

These have different buyers, sales cycles, and competitive dynamics. When we take this to a customer, we need clarity on what exactly we're selling. For retail, we likely want the agentic tools without the infrastructure baggage.

### 4. Competitive Landscape is Crowded

Zeblok is not alone in air-gapped AI infrastructure. The market includes:

| Competitor | Backing | Defense Credentials |
|------------|---------|---------------------|
| **Microsoft Azure Local** | Hyperscaler, GA Q1 2026 | Government cloud, sovereign requirements |
| **Google Distributed Cloud Air-Gapped** | Hyperscaler | IL6 authorized, US Air Force & Navy contracts |
| **D2iQ Kubernetes Platform (Gov)** | Independent (~300 employees) | FIPS 140-2 validated, Lockheed/Northrop/SAIC partnerships |
| **Rancher Government Solutions** | SUSE subsidiary | Only K8s with DISA STIG, U-2 aircraft edge deployment |
| **Domino Data Lab** | Enterprise MLOps | DoD customers, Navy accredited systems |

The hyperscalers are entering this space with vastly more resources. Zeblok's differentiation will need to be sharper than "we do air-gapped"—possibly speed of deployment, GPU efficiency, or specific ISV integrations.

### 5. Defense Claims Need Validation

Mouli mentioned access to 3-4 star generals, a TS-cleared advisor, and "projects starting imminently in county US space." These are relationships and intentions, not delivered contracts.

The defense market is hard. It requires: established prime contractor relationships, actual past performance, US Persons throughout the stack, and certifications (CMMC, FedRAMP, FIPS 140-2). Knowing people is different from winning and executing contracts.

If Zeblok has delivered to an actual defense customer or has a named prime partnership, that changes the calculus. We should ask.

---

## Key Questions to Resolve

1. **Lock-in:** What is the minimum infrastructure required for Zeblok's tools to operate? Can agentic capabilities run standalone on customer's existing Kubernetes, or do they require the full Ai-MicroCloud substrate? This determines whether we can sell to non-defense customers.

2. **Defense validation:** Have they delivered on an actual defense contract? Any named prime contractor partnerships or past performance we can reference?

3. **Certification status:** What do they have today—FIPS 140-2 validated crypto? CMMC mapping? SOC 2? Or is this planned/aspirational?

---

## Agreed Next Steps

| Action | Owner | Timeline |
|--------|-------|----------|
| Execute mutual NDA | Both parties | Immediate |
| Platform access for Colin | Zeblok | Within days |
| Follow-up call on investment sizing | Both parties | TBD |
| Target announcement | Both parties | GTC NVIDIA, mid-March |

**Proposed structure:** "Bay One Innovation Lab powered by Zeblok Labs"—co-development environment in Bay Area, initially focused on retail vertical with clear path to defense.

---

## Recommendation

**Proceed with cautious optimism.**

This partnership has genuine strategic value. It positions BayOne beyond staffing, opens defense as a market, and gives us a differentiated technology story. The leadership rapport is real, and the timing—with GTC as a milestone—creates useful urgency.

At the same time, be clear-eyed: the air-gapped infrastructure value is narrow (defense + manufacturing), local models don't solve most enterprise AI needs, and Zeblok faces serious competition from hyperscalers entering this space.

**Suggested posture:**
- Colin evaluates the platform hands-on once access is granted
- Clarify the lock-in question in the follow-up sizing call
- Ask directly about defense delivery track record
- Pursue the GTC announcement as a low-commitment formalization while we validate the opportunity

The pivot from staffing is worth pursuing. Defense is worth pursuing. Just don't overcommit before the key questions are answered—and be prepared that the realistic opportunity may be narrower than the pitch suggests.
