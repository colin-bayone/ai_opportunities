# Document Critique: Technical Deep Dive Framework

## Overall Assessment

**Verdict: NEEDS REVISION**

The document is substantively strong with good technical content and clear structure. However, it contains several AI writing patterns that need correction before it reads like a Big Four deliverable.

---

## Issue Categories

### 1. Contrastive Rhetorical Framing (HIGH PRIORITY)

The most frequent issue. Multiple instances of "not X, it's Y" or "rather than X, Y" patterns.

| Line | Text | Issue | Fix |
|------|------|-------|-----|
| 9 | "this is **not** a lift-and-shift **but** a complete rebuild" | Classic contrastive frame | "This is a complete rebuild of data pipelines and reporting assets for a modern architecture." |
| 38 | "These are **not** theoretical - **they are** documented, supported integration methods" | Defensive framing | "These are documented, supported integration methods used in enterprise environments for years." |
| 99 | "Agent automation **does not mean** humans disappear." | Negative framing | "Agent automation shifts human effort from mechanical tasks to judgment calls." |
| 140 | "confidence is **not** AI guessing. **It's** pattern recognition" | Contrastive emphasis | "Confidence scores reflect pattern recognition based on human feedback." |
| 182 | "automation with guardrails, **not** a black box" | Contrastive | "automation with guardrails and full visibility" |
| 190 | "**Rather than** having agents figure out how to connect each time" | Rather-than pattern | "MCP provides stable, reliable interfaces instead of connection improvisation." |
| 207 | "capability gained, **not** dependency created" | Contrastive | "capability gained without ongoing dependency" |
| 233 | "Make changes with confidence **rather than** discovering broken reports" | Rather-than pattern | "Make changes with confidence, knowing downstream impact in advance." |

---

### 2. Contractions (MEDIUM PRIORITY)

Found in several places where formal tone is expected.

| Line | Text | Fix |
|------|------|-----|
| 89 | "agents work better when **they're** more specific" | "agents work better when they are more specific" |
| 159 | "insights from one report **don't** inform the next" | "insights from one report do not inform the next" |

---

### 3. Em-Dash Usage (LOW PRIORITY)

Count: 6 em-dashes (guideline suggests max 5)

| Line | Text | Recommendation |
|------|------|----------------|
| 25 | "integration perspective - mature, well-documented" | Replace with colon: "integration perspective: mature, well-documented" |
| 52 | "this burden - surfacing decisions" | Replace with comma or restructure |
| 140 | "confidence score - but confidence is not" | Period and new sentence |
| 159 | "independent - insights from one report" | Period and new sentence |

---

### 4. Blog-Style Headers (LOW PRIORITY)

Some headers use casual or catchy phrasing.

| Line | Current | Professional Alternative |
|------|---------|-------------------------|
| 46 | "The Semantic Layer Goal" | "Semantic Layer Architecture" |
| 50 | "The Core Constraint" | "Resource Constraints" |
| 97 | "Keeping Humans in the Loop" | "Human Oversight Model" |
| 247 | "Start Small, Prove Value" | "Proof-of-Concept Approach" |
| 255 | "Build on Your Infrastructure" | "Infrastructure Integration" |

---

### 5. Colloquial Language (LOW PRIORITY)

| Line | Text | Professional Alternative |
|------|------|-------------------------|
| 44 | "piecemeal approach" | "fragmented workflow" or "manual step-by-step process" |
| 48 | "No more 'my number versus your number' disputes" | "Eliminates discrepancies between report outputs" |
| 104 | "black box" | "opaque system" or "system without visibility" |
| 182 | "black box" (again) | Same fix |
| 194 | "improvising" | "ad-hoc connection logic" |

---

### 6. Rhetorical Questions (LOW PRIORITY)

| Line | Text | Fix |
|------|------|-----|
| 87 | "If we imagine this work being done without AI, what roles would exist?" | "The design models agent roles after traditional team structures." |

---

### 7. Universal Claims (MINOR)

| Line | Text | Issue |
|------|------|-------|
| 221 | "Twenty years of accumulated logic" | Unverified specific claim; consider "Years of accumulated logic" |
| 241 | "Organizations accumulate redundant reports over time" | Generalization; consider "Large organizations often accumulate..." |

---

## Content Preservation Notes

**No substantive content should be removed.** All fixes are style/tone adjustments:
- Technical claims about Cognos SDK, Content Store, DataStage tools: KEEP
- Schema mapping methodology (3 phases, confidence routing, knowledge graph): KEEP
- Failure handling and guardrails: KEEP
- All capability descriptions: KEEP
- Discussion topics: KEEP

---

## Section-by-Section Status

| Section | Status | Notes |
|---------|--------|-------|
| Our Understanding | Needs revision | 2 contrastive frames, 1 colloquial |
| Key Technical Challenges | Good | Minor style tweaks |
| Agent Orchestration Approach | Needs revision | 1 contraction, 1 rhetorical question, blog-style header |
| Schema Mapping Methodology | Needs revision | Contrastive framing in confidence section |
| Tool Integration Strategy | Needs revision | Multiple "rather than" patterns |
| Acceleration Capabilities | Good | Minor universal claim |
| Implementation Approach | Needs revision | Blog-style headers, 1 rather-than pattern |
| Discussion Topics | Good | No issues |

---

## Fix Priority Order

1. **Contrastive framing** - Remove all "not X, it's Y" and "rather than" patterns (8 instances)
2. **Contractions** - Expand all contractions (2 instances)
3. **Blog-style headers** - Formalize header text (5 instances)
4. **Colloquial language** - Replace casual terms (5 instances)
5. **Em-dashes** - Reduce and replace with appropriate punctuation (4 reductions needed)
6. **Rhetorical question** - Rewrite as statement (1 instance)

---

## Verdict

**NEEDS REVISION** - The document is 85% there but has identifiable AI patterns that would be caught by a careful reader. Primary issue is contrastive framing throughout. After one revision pass applying the fixes above, this should achieve PASS status.
