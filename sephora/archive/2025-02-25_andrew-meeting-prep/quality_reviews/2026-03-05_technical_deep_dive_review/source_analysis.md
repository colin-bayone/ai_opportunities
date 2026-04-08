# Source Analysis

## Document Purpose

This document is a screen-share presentation framework for a technical deep-dive meeting with Sephora's technical leads (Andrew Ho, Grishi Chakraborty, and Mahair the enterprise architect). It serves as:
1. A conversation guide if the meeting stalls
2. A demonstration of BayOne's understanding and preparation
3. A vehicle to steer toward getting environment access for a POC

## Source Materials Analyzed

### Meeting 3 Transcript (Andrew Ho & Grishi Chakraborty)
Key stakeholder statements that inform this document:

**Grishi's pain points:**
- SSAS to Databricks connector with Excel pivot table preservation
- Agent automation for Cognos report re-engineering
- Agent automation for DataStage pipeline migration
- Schema mapping accuracy issues with current Claude usage

**Andrew's vision:**
- Agent swarm with orchestration to compress 3-year timeline to 1.5 years
- Spend upfront on agents rather than manual contractors
- Acknowledged no vendor has a pre-built package

**Technical context:**
- Cognos version 10.2/10.3 (very old, on-premises)
- DataStage (not latest version, on-premises)
- Target: Databricks
- Current AI usage: 30% efficiency gain with Claude, but manual workflow

### Prior Meetings (Mani Soundararajan)
- Three-year EDW re-engineering program (not migration)
- Finance track underway, continuing through end of year
- Semantic layer goal for tool agnosticism
- SME bandwidth is the core constraint

## Key Claims in Document

1. **Cognos/DataStage integration is feasible** via SDK, Content Store, dsjob/dsexport
2. **Confidence scoring is based on human feedback loops**, not AI guessing
3. **Deterministic foundation first** reduces AI error surface area
4. **Knowledge graph persists learnings** across tracks
5. **Guardrails prevent infinite loops** with human escalation

## Audience Considerations

- **Grishi:** Technical gatekeeper, wants to see proof, appropriately skeptical
- **Andrew:** Vision owner, transparent about vendor shopping
- **Mahair:** Enterprise architect, will probe architecture decisions

Document must be defensible under technical scrutiny while not over-explaining internal architecture.

## Tone Requirements

- Confident but not overselling
- Technical depth available but not forced
- Prepared but collaborative (not prescriptive)
