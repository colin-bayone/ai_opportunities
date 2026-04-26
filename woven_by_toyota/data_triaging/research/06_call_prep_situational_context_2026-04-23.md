# 06 - Call Prep: Situational Context

**Source:** Engagement research library (Sets 01-05)
**Source Date:** 2026-04-23 (prepared immediately before discovery call)
**Document Set:** 06 (Call Prep for Travis Millet Discovery Call)
**Pass:** Situational context, people, what we know, what we do not

---

## Meeting Logistics

- **Date and time:** Thursday, 2026-04-23 at 3:30 PM PST
- **Format:** Virtual (Microsoft Teams assumed)
- **BayOne attendance:** Colin Moore (remote), Jesse Smith (on-site), Pratik Sharda (attendance not explicitly confirmed in writing; assume on-site or remote supporting)
- **Woven attendance:** Travis Millet confirmed. Whether anyone else joins is unknown at time of prep.

## Company Profile

Woven by Toyota is Toyota's autonomous vehicle subsidiary, positioned to help Toyota catch up to Tesla and next-generation EV makers on software-defined automotive architecture. The company grew out of the TRI-AD (Toyota Research Institute Advanced Development) entity established in 2018, was renamed Woven by Toyota in 2023, and has absorbed approximately 150 researchers transferred from Toyota Research Institute as well as 300 plus engineers from the 2021 Level 5 acquisition. Much of the Palo Alto team sits at 900 Arastradero. Travis's geographic context is almost certainly Palo Alto.

The key recent milestones that matter for this call:

- **Arene shipped in production in May 2025.** The 2026 Toyota RAV4 is the first Toyota vehicle with Arene. This is a major public inflection point. Before May 2025, Woven's data volumes were test-fleet bounded. Now they have production fleet data flowing in alongside test fleet data.
- **Woven City officially launched in September 2025.** Active data collection environment and AV testing site.
- **April 22, 2026 (yesterday).** Toyota and Woven announced a major AI stack including Woven City AI Vision Engine, Integrated ANZEN System, Infra Hub, and Data Fabric. Travis may reference this. Colin should be aware it exists without needing to discuss it in depth.
- **April 2025 Waymo partnership.** Arene plus Waymo stack for personally owned AVs, positioned against Tesla.

## Org Structure Relevant to This Call

Public org pillars at Woven:

- Arene (Campeau)
- AD and ADAS (Dushyant Wadivkar)
- Cloud and AI (Jack Yan)
- Woven City (Daisuke Toyoda)
- Enterprise Technology (Kishore Kondragunta)

Where Travis's Technical Operations Engineering team sits within this structure is not publicly confirmed. Most plausible parents are AD and ADAS or Cloud and AI.

## Key People

### Travis Millet (the call counterparty)

- **Current title:** Manager of Technical Operations Engineering, Woven by Toyota
- **Prior role:** Senior Triage Operations Lead, Toyota Research Institute
- **Earlier career:** Air Force Test Center, flight test engineering background (noted for context only; not a reference point BayOne should cite)
- **Reports to:** Steve Lauziere (Director of Engineering or Senior Manager, ex-Argo AI, ex-Ford AV)
- **Profile:** Precision engineering and safety-first background, methodical, expected to be skeptical of hype, focused on operational reliability and throughput
- **Expected team shape:** Peer Triage Manager roles at Woven publicly describe approximately seven Core Triagers reporting to a Senior Manager under an SLA driven operations structure. Travis's team likely fits this shape.
- **Public footprint:** Minimal. No discoverable published talks, podcasts, blog posts, or patents. He operates in the low-signal mode typical of automotive OEM operations managers.
- **Historical BayOne engagement:** Travis has not previously given BayOne much time per Jesse. The procurement sponsor who met Pratik at lunch is acting as the unlock for this call.

### John Lim (Woven-side champion per Jesse)

- **Role:** New contingent workforce program manager at Woven (plausible formal title: Indirect Procurement Manager, Contingent Workforce)
- **Certification:** CCWP (Certified Contingent Workforce Professional)
- **Career arc:** Long tenure in managed service provider and vendor management work (Beeline, WorkforceLogic, Deutsche Bank, McGraw-Hill, BNP Paribas, Volt, CIT, CareFirst, Zoox, and most recently either Applied Materials or Applied Intuition)
- **Role in this opportunity:** Procurement gatekeeper. Controls supplier panel, VMS, rate cards, commercial terms. Can accelerate or veto supplier access to Travis Millet.
- **BayOne relationship:** Per Jesse, John Lim knows BayOne. Specifics of that prior relationship are not documented.
- **Note:** Whether John Lim attends this call in person is not confirmed.

### Naoki

- **Role:** Coordination contact for the discovery call. Pratik presented the AI framing to Travis via Naoki.
- **Profile:** Full name, title, and department not established.

### Adjacent Woven Names (Not on the Call)

- **Suigen Koide** - Head of DevBoost, GenAI, and MLOps. Owns AutoTriage (the ML platform system, not the operational workforce).
- **Alborz Alavian** - Senior Engineering Manager, quoted in the Woven Union.ai case study.
- **Steve Lauziere** - Travis's manager, not directly in this conversation.

## What We Know Going In

- Woven collects large volumes of telemetry and sensor data from vehicle testing: driving paths, anomalies, visuals. Added in April 2026 is production-fleet data from RAV4 customers.
- They operate AutoTriage, a GenAI plus human-in-the-loop system that reportedly absorbs approximately 50 percent of ADAS triage volume at 80 percent accuracy. Published metrics include 34,000 engineer-hours saved and $2.2M reported savings.
- They run Union.ai (managed Flyte) for orchestration. Published metrics include 20x faster ML iteration and $1M plus annual savings.
- They are a publicly named Encord annotation customer.
- They have a dedicated Data Annotation and Labeling Engineering team per open job postings.
- An SOW for three to four people on data triaging is incoming, originated from a lunch Pratik had with a senior procurement leader at Woven.
- The client has not brought up AI as a framing. Pratik recognized the AI angle and presented it to Travis via Naoki.

## What We Do Not Know

- Whether Travis's openness to the AI angle has been explicitly confirmed back to BayOne (Colin's Condition 4 from the pre-call emails)
- Whether Travis is aware of the discovery framing (Colin's Condition 3)
- The specific scope of the incoming 3-4 person SOW: augmentation, surge, integration, QA, or something else
- What specific data Travis's workforce is labeling and to what taxonomy
- Where Travis's team reports in the Woven org structure
- Whether anyone else from Woven will attend

## What Colin Brings

- **Direct AI engineering and data science depth.** Not a sales engineer. Builds the systems.
- **Prior experience in adjacent industries.** Semiconductor equipment (Coherent Corp), retail Salesforce, Oracle Cloud.
- **Engagement model experience.** The three BayOne models (full managed, hybrid collaboration, pure staffing) and their variable-split variants, operationalized across multiple engagements.
- **Pattern recognition for the labeling vs correlation vs root cause distinction.** Not a guess from this engagement; a framework from prior work.
- **Experience with hybrid human plus AI workflows.** Direct experience with the class of work Woven would benefit from even within Travis's operational mandate (active learning loops, pre-labeling with foundation models, QA instrumentation, edit-distance telemetry).

## Things to Watch For During the Call

- Whether Travis knows this is a discovery call or thinks it is a pitch or a meet-and-greet
- Whether Travis references the April 22 Woven City AI stack announcement
- Whether Travis talks about AutoTriage or ML platform work at all, or restricts the conversation entirely to his operational workforce
- Whether Travis volunteers any pain around quality, throughput, inter-vendor consistency, onboarding, or feedback loops to the ML platform team (these are operational solutions territory)
- Whether John Lim joins the call
- Any procurement-process signaling (VMS, rate cards, contingent workforce channel) that would indicate the engagement is being routed through pure time-and-materials staffing
- Whether Travis has a visible job spec or structured ask (suggests advanced staffing framing; less room for conversion)

## Condition Status at Time of Prep

- **Condition 1 (no follow-up work before April 28):** In effect. Jesse acknowledged.
- **Condition 2 (no materials or slides expected):** In effect. Jesse acknowledged.
- **Condition 3 (Travis aware of discovery framing):** Jesse committed to confirm with Naoki before the call. Status unverified at time of prep.
- **Condition 4 (Travis openness to AI angle confirmed):** Jesse committed to confirm with Naoki before the call. Status unverified at time of prep.
