## Prepare WebEx/Scribble Architecture Documentation for Friday Srinivas Meeting

### Description

Saurav and Srikar need to prepare architecture documentation covering the WebEx scraping (Pulse) and transcription (Scribble) workstream for the Friday meeting with Srinivas. This is the primary deliverable expected from the WebEx team this week.

### What Srinivas Wants to See

Srinivas has been asking "how are you going to do this?" The team has gathered information, met with Naga and Justin, and explored the WebEx APIs. Now the documentation needs to show a clear approach, not just a summary of what was learned.

### Deliverable Components

**1. Current-State Architecture Diagram**
- What Naga has built today with Pulse (WebEx scraper to DB, no downstream use case)
- What Naga has built today with Scribble (local Whisper script, not integrated, not deployed)
- Show these plainly and factually; do not editorialize. Let the diagram speak for itself.

**2. Proposed Future-State Architecture Diagram**
- Unified service layer approach: WebEx data extraction as a shared service, not per-developer scripts
- Components: scraper/service app, database, MCP layer, downstream applications (bots, agents, analysis)
- OAuth-based data isolation (user-level access control, not bot-level blanket access)
- Show how the same service layer can support multiple use cases (chat analysis, meeting summaries, action item extraction, compliance monitoring)

**3. Considerations Document**
- A/B testing plan for Scribble vs WebEx transcription (reference issue #4)
- Scale and cost implications of Wispr at organizational level
- Bot compliance policy and registration path (reference issue #5)
- Scope clarification: Srinivas scoped us to WebEx focus; Naga proposed expanding to email, GitHub, etc. Recommendation: deliver WebEx first, expand later.

### Tone and Framing

- Architecture decisions are presented as preliminary explorations, not finalized plans. Use language like "initial assessment" and "areas we are continuing to investigate."
- Do not criticize existing Cisco work directly. Show current state vs proposed state and let the comparison speak.
- Do not present ideas as commitments. If something is not yet validated, say so.
- Do not include individual names from the Cisco team in deliverables.

### Dependencies

- Architecture working session with Colin is planned for this week (before Friday)
- Singularity training session for presentation generation is planned

### Acceptance Criteria

- [ ] Current-state architecture diagram complete
- [ ] Proposed future-state architecture diagram complete
- [ ] Considerations document drafted
- [ ] Colin has reviewed before Friday meeting
- [ ] Presentation slides generated (after Singularity training)
