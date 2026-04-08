# 06c - Gap Resolution Decisions

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-02
**Document Set:** 06c (Supplementary to Set 06)
**Context:** Colin's decisions on how to handle each gap identified in 06b
**Note:** Originally numbered Set 03c. Renumbered to 06c during Singularity reorganization (2026-04-07).

---

## High Priority -- Decisions Made

### 1. Estimation model in Phase 1 Discovery
**Decision:** Add it. The estimation model (conversion velocity data, per-screen effort calibration) is a key discovery deliverable. Guhan specifically asked for this to make customer delivery commitments. It belongs in Phase 1's included items.

### 2. Customer-transparent equivalence
**Decision:** RESOLVED. Strengthened language to "seamless and indistinguishable from the original EPNM interface" and "UX preservation, not UX redesign." Applied to Phase 3 description and Phase 4 visual validation bullet.

### 3. Human review as final line of defense
**Decision:** RESOLVED. Reframed as "human-in-the-loop review" within the agentic workflow. Added as a bullet in Phase 4: "architectural oversight and quality verification at every stage of the agentic workflow, with human engineers reviewing all AI-generated output." Positioned alongside 100% AI-generated code, not as a contradiction to it.

### 4. Focus on missing functionality (scope boundary)
**Decision:** RESOLVED. Did NOT draw a hard line. Instead, framed scope as "approximately 240 to 260 screens as identified through collaborative prioritization." Added: "BayOne will accommodate reasonable variance from this estimate within the engagement. Significant changes to the screen count or complexity beyond what is identified during discovery would be addressed through the change request process." Also added a discovery deliverable: "Inventory of screens already ported to EMS vs. screens remaining in EPNM only, ensuring no duplication of existing work."

### 5. Fix defensive "protects both parties" language
**Decision:** RESOLVED. Removed the "protects both BayOne and Cisco" line entirely. Replaced with scope framing and reasonable variance language. No longer defensive.

---

## Medium Priority -- Pending Discussion

### 6. Flywheel / acceleration mechanism
**Colin's note:** Important, especially in the context of the estimation model. The flywheel (early screens are slower, later screens accelerate as patterns and tooling mature) directly supports the estimation model because it means the POC conversion rate is conservative -- actual production rates will be faster.

**Pending:** How prominent should this be? A sub-point under the estimation model? Its own bullet? A note in the conversion phase?

### 7. Identification of what has already been ported
**Pending:** Does this go in Discovery as a specific deliverable ("inventory of what exists in EMS vs. what does not") or is it implied by "screen inventory with complexity classification"?

### 8. Domain-specific validation weight
**Pending:** Guhan's domain gap concern was his single biggest question. Currently mentioned in passing in QE. Should it be elevated? How?

### 9. Test coverage gap analysis as tooling output
**Pending:** Colin mentioned during the meeting that the judge agent identifies where tests SHOULD exist but don't. Should this be called out in the tooling phase?

### 10. UX preservation vs. redesign distinction
**Pending:** Prior porting involved UX redesign. This effort explicitly preserves EPNM UX. Should the breakdown call this out? It's a subtle but important distinction.

---

## Lower Priority -- Pending Discussion

### 11. Blockchain-style documentation system
**Pending:** This is an internal methodology detail. Probably not needed in a client-facing breakdown. But the concept of "persistent knowledge that grows with each screen" is valuable for the client to understand.

### 12. Agent architecture detail
**Pending:** The four-agent model (architect, engineer, foreman, judge) was presented to Guhan and he engaged with it. Is it worth a brief mention in the tooling phase, or is "purpose-built agents" sufficient?

### 13. Claude Code to LangGraph progression
**Pending:** Probably too technical for a pricing breakdown. Skip unless Colin disagrees.

### 14. Documentation state assessment
**Pending:** Implied by "limited design documentation." Probably not a separate line item.

### 15. Screen categorization by type
**Pending:** Already partially covered by "complexity classification." Could be expanded to mention types (reports, dashboards, configuration, monitoring) if desired.

### 16. Categorical miss detection
**Pending:** Interesting concept (failures are large and detectable, not subtle) but may be too much detail for this document.
