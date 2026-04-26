# 08c - Meeting: BayOne Positioning on the Call

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt
**Source Date:** 2026-04-23 (Travis Millet discovery call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** How each BayOne attendee positioned BayOne on the call, and the framing BayOne left with

---

## Purpose

This file captures how BayOne presented itself to Travis Millet during the call. It is separate from the ask (in `08b`) because the ask is about what Woven wants, while this file is about what BayOne said about itself and about the outcome of that framing.

## Pratik Sharda's Framing

Pratik Sharda led the BayOne framing. His positioning moves:

- **Local Bay Area presence.** Introduced BayOne as a locally based organization.
- **Not a competing product.** Stated explicitly and more than once that BayOne does not have a competing product for this particular opportunity and that BayOne is not in the same category as the 20-plus product vendors that have already approached Travis about AI triage.
- **Staffing and services orientation.** Positioned BayOne as a provider of human resources (the "HL part" in the transcript, intended as "human in the loop") alongside services.
- **Trusted partner status at Woven.** Referenced BayOne's existing status as a preferred partner at Woven across other teams (procurement, ADAS, Arene). Suggested the existing relationship shortens the onboarding overhead compared to a new vendor.
- **Candidate quality differentiator.** Described BayOne's internal technical assessment process, referenced the TechScore tool, and noted that technical candidates are benchmarked before being submitted to the customer.
- **Flexibility.** Described BayOne as nimble on commercial structure and willing to work through a single SOW for multiple resources.
- **Engineering-heavy leadership.** Referenced that BayOne's co-founders and most team members come from engineering backgrounds, framed as a differentiator against staffing firms staffed by non-technical functional recruiters.

The cumulative effect of Pratik's framing was to place BayOne inside the staffing category for this opportunity rather than outside of it. The explicit "we do not have a product" statements closed off any framing that BayOne might compete with the product vendors on the AI side.

## BayOne Technical Lead Framing

The technical lead (Colin Moore) was introduced by Pratik mid-call, described as BayOne's Director of AI. The technical contribution on the call covered the following points:

- Prior background in solid state electrolyte R&D for electric vehicle batteries (acquired by GM) and subsequent AI and reliability engineering work at Coherent in semiconductors, optics, advanced materials, and manufacturing.
- Engineering orientation. Declared a healthy skepticism of 80 percent accuracy claims as insufficient for engineering contexts.
- Framed the triage problem as not strictly binary between AI-only and human-only approaches. Proposed a hybrid architecture:
  - Keep processing deterministic as long as possible before any AI call.
  - Combine methods progressively. Use machine learning and computer vision where appropriate. Reserve multimodal or generative AI for fringe cases at the end of the pipeline.
  - Use this layering to push accuracy toward the 96 to 98 percent range.
- Described a progressive human-to-AI offload model. Start with human-in-the-loop. Progressively offload to AI while maintaining sampling of outputs, modeled after quality assurance on an assembly line.
- Described confidence scoring as track record of correct decisions over time rather than as aggregate model confidence. Framed this as analogous to how human teams build confidence in a colleague.
- Responded to Travis's follow-up questions on fine-tuning, off-the-shelf model usage, and training from human corrections. Indicated BayOne's approach uses off-the-shelf models where cost-effective and trains where necessary. Referenced Vertex AI on Google Cloud as an example of hosted capability that can reduce cost at scale.

The technical content was well-received on the call in the sense that Travis engaged with it, asked follow-up questions, and stated that he enjoys talking to AI companies to compare approaches. However, the engagement did not shift the commercial framing Pratik had established. Travis's takeaway was curiosity, not commercial interest.

## Jesse Smith's Role on the Call

Jesse Smith was on-site with Pratik during the call. Her substantive contribution to the conversation, as captured in the transcript, was minimal. She did not lead framing on any topic during the call.

## The Outcome of BayOne's Positioning

At the end of the call, the positioning of BayOne in Travis's eyes was the following:

- A staffing partner competing with the incumbent staffing vendor for one backfill role.
- A firm with a technical lead who is interesting to talk to but who is not offering a product or a solutions engagement.
- A preferred partner inside Woven from prior relationships, which helps commercial velocity but does not change the category.
- A potential candidate for a portion of the forthcoming 13x scale expansion, with the shape of that future engagement undefined.

This is a pure staffing framing. It reflects the commercial positioning Pratik chose to lead with and the alignment of that positioning with what Travis was actually asking for.

## Internal Consistency of the Framing

The framing is internally consistent. The technical lead's content on hybrid architectures, deterministic layers, and progressive offload did not contradict Pratik's framing; it supplemented it as context. Pratik's "we do not have a product" statements were factually accurate and reflected BayOne's current commercial offering for this specific problem.

## Internal Observation

The framing outcome closed off any path to a solutions engagement on this opportunity. If a solutions engagement was a goal, it would have required a different commercial framing on the call, one that neither BayOne's current offering nor Travis's stated needs supported. The current framing is the accurate one for the state of both sides.

## Open Questions After This File

- Whether Travis's expressed curiosity about BayOne's technical framing ever converts to a commercial interest after his current architecture encounters scaling or accuracy problems.
- Whether Jesse Smith's limited substantive contribution on the call reflects the on-site role (relationship presence, deferred framing to Pratik) or reflects a gap in preparation.
- Whether the 13x scale work, when it lands, goes to BayOne as additional staffing or via a different commercial vehicle.
