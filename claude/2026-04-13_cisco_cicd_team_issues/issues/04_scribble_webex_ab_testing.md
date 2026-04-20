## Design and Execute Scribble vs WebEx Transcription A/B Testing

### Description

Srinivas wants the team to evaluate whether Scribble (Whisper-based transcription) provides meaningful value over the built-in WebEx meeting transcription. This is not just a quality comparison; it needs to consider downstream AI usability, cost, and scale implications.

### Background

- Scribble uses Whisper (and PanNote) to transcribe audio files locally on a developer machine
- WebEx already provides built-in meeting transcription at no additional cost
- Srinivas framed this as parallel work: evaluate both approaches, see which delivers better results
- The real question is not just "which transcription is more accurate" but "does the accuracy difference matter for downstream AI processing, and at what cost"

### Testing Framework (Multi-Tier)

**Tier 1: Raw Transcription Quality**
- [ ] Obtain the same meeting's transcript from both sources (request Friday 2026-04-10 Srinivas call transcript from Naga via Scribble; extract WebEx transcript of the same meeting)
- [ ] Compare side-by-side for: speaker identification accuracy, technical jargon accuracy, proper nouns and names, overall readability

**Tier 2: Downstream AI Usability**
- [ ] Feed both transcripts to an LLM for the same task (e.g., extract action items, generate summary)
- [ ] Compare output quality: does the LLM produce meaningfully different results from each transcript?
- [ ] Test whether simple prompt engineering (e.g., "this is a speech-to-text transcript with potential errors, use common sense") bridges any quality gap

**Tier 3: Prompt Engineering Compensation**
- [ ] Create a glossary lookup table of commonly mistranscribed terms (Cisco jargon, team member names, product names like DeepSite, Bazel, etc.)
- [ ] Test whether providing this glossary as context to the LLM eliminates the accuracy difference between the two transcription sources
- [ ] Measure: if WebEx + glossary produces equivalent AI output to Wispr, the accuracy premium of Wispr is effectively zero for this use case

**Tier 4: Cost and Scale Analysis**
- [ ] Document Wispr hosting requirements (compute, storage, concurrency limitations)
- [ ] Determine: if Wispr runs locally, how many concurrent transcriptions can it handle? (Likely: one at a time per instance)
- [ ] Calculate: what would it cost to run Wispr at organizational scale vs using the existing free WebEx transcription?
- [ ] Consider: if multiple teams each spin up their own Wispr instance, they are processing the same meeting audio redundantly. A centralized approach is architecturally superior.

### Quick Start

Request the Scribble transcript of the Friday Srinivas call from Naga. Compare against the WebEx transcript of the same meeting. This can begin even without DeepSite repo access.

### Key Framing (for Srinivas)

Present findings as data, not opinions. If Wispr is 10% more accurate but costs significantly more and cannot scale, let the numbers speak. If prompt engineering closes the gap, show that. The goal is to give Srinivas the information to make an informed decision, not to argue for one approach.

### Acceptance Criteria

- [ ] At least one meeting transcript compared across both sources
- [ ] Tier 1 and Tier 2 results documented
- [ ] Cost and scale considerations documented
- [ ] Recommendation drafted with supporting evidence
