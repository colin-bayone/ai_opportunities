# POC Proposal Version Comparison

**Purpose:** Verify no useful content was lost between versions

---

## Version Summary

| Version | Lines | Status |
|---------|-------|--------|
| v1 (03_poc_proposal_draft.md) | 94 | Original draft - too brief, lacked technical depth |
| v2 (05_poc_proposal_v2.md) | 264 | Added technical depth but unprofessional tone |
| v3 (05_poc_proposal_v3.md) | 310 | Professional rewrite preserving v2 content |

---

## Content Preservation Check: v2 → v3

### Technical Context

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| EPNM: monolithic Java, Dojo/JavaScript frontend | Lines 38-44 | ✓ |
| 15+ years evolution, tight coupling, implicit contracts | Lines 38-42 | ✓ |
| Tribal knowledge / accumulated complexity | Line 42 ("institutional knowledge embedded") | ✓ |
| Dojo widget system, declarative markup, data binding | Line 44 | ✓ |
| Semantic vs syntactic conversion distinction | Line 44 | ✓ |
| EMS: microservices, Angular frontend | Lines 48-52 | ✓ |
| Service boundaries, API contracts, reactive state | Lines 50-52 | ✓ |
| RxJS, observables vs Dojo data stores | Line 52 | ✓ |

### Vertical Work Concept

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| Selva quote reference ("if frontend doesn't exist...") | Line 56 (paraphrased without name) | ✓ |
| 5-step conversion process | Lines 60-64 | ✓ |
| Data flow, backend logic, EMS mapping, Angular UI, validation | Lines 60-64 | ✓ |

### Experience References

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| C# to Rust conversion | Line 66 | ✓ |
| Spring to Go conversion | Line 66 | ✓ |
| Thick-client to web | Line 66 | ✓ |
| Legacy .NET to embedded C++ | Line 306 | ✓ |

### Phase 1: Exploration

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| ~1 week from code access | Line 74 | ✓ |
| Deliverable: analysis document | Line 75 | ✓ |
| Claude Code for exploration | Line 81 | ✓ |
| Screen inventory and categorization | Line 83 | ✓ |
| Dependency graphs | Line 84 | ✓ |
| Complexity indicators | Line 85 | ✓ |
| Pattern identification | Line 86 | ✓ |
| Collaborative screen selection with SMEs | Lines 88-92 | ✓ |
| Selection criteria (4 items) | Lines 98-101 | ✓ |

### Phase 2: Conversion

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| ~3 weeks from screen selection | Line 107 | ✓ |
| Agent architecture (LangGraph) | Line 112 | ✓ |
| Architect Agent description | Line 114 | ✓ |
| Engineer Agent description | Line 116 | ✓ |
| Foreman Agent description | Line 118 | ✓ |
| Judge Agent description | Line 120 | ✓ |
| Agent tooling (grep, static analysis, tests) | Line 122 | ✓ |
| Structured handoffs | Line 122 | ✓ |

### Pattern Library

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| Full pattern table | Lines 128-133 | ✓ |
| Dojo DataGrid → Angular Material | Line 130 | ✓ |
| Dojo Dialog → Angular Material dialog | Line 131 | ✓ |
| Direct service injection → HTTP client + RxJS | Line 132 | ✓ |
| Pub/sub → event emitters / RxJS subjects | Line 133 | ✓ |

### Visual Validation

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| Playwright for visual testing | Line 139 | ✓ |
| Baseline screenshots | Line 141 | ✓ |
| Visual regression flagging | Line 143 | ✓ |
| Side-by-side comparison | Line 144 | ✓ |

### Gap Analysis

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| New microservices that don't exist | Line 152 | ✓ |
| API extensions needed | Line 153 | ✓ |
| UX compromises | Line 154 | ✓ |
| Explicit documentation, Cisco decides | Line 156 | ✓ |

### Acceleration Mechanism (Flywheel)

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| One-time investment table | Lines 168-174 | ✓ |
| Codebase exploration → knowledge graph | Line 170 | ✓ |
| Pattern identification → conversion library | Line 171 | ✓ |
| Agent development → custom agents | Line 172 | ✓ |
| Workflow design → quality gates | Line 173 | ✓ |
| Tooling setup → Playwright infrastructure | Line 174 | ✓ |
| Per-screen work table (first vs subsequent) | Lines 180-186 | ✓ |
| Staffing model explanation | Lines 190-200 | ✓ |
| Parallel execution capability | Line 196 | ✓ |
| "Multiplies that baseline" | Line 200 | ✓ |

### Scope and Timeline

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| 2-3 screens | Line 208 | ✓ |
| End-to-end including backend | Line 209 | ✓ |
| 4 weeks from code access | Line 215 | ✓ |
| Week-by-week timeline table | Lines 217-220 | ✓ |
| Can start before laptop arrives | Line 222 | ✓ |
| Exclusions (3 items) | Lines 226-228 | ✓ |

### Investment Model

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| POC: Zero cost to Cisco | Line 236 | ✓ |
| POC: Single senior resource | Line 237 | ✓ |
| POC: Sequential execution | Line 238 | ✓ |
| Paid: Team scale | Line 243 | ✓ |
| Paid: Parallel streams | Line 244 | ✓ |
| Foundation transfers to paid | Line 248 | ✓ |

### Security

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| Cisco hardware | Line 284 | ✓ |
| Cisco-licensed AI | Line 285 | ✓ |
| No code leaves infrastructure | Line 286 | ✓ |
| NDA executed | Line 287 | ✓ |
| Already onboarded with Anand's team | Line 289 | ✓ |

### Next Steps

| v2 Content | v3 Location | Preserved? |
|------------|-------------|------------|
| Laptop arrival notification | Line 295 | ✓ |
| Screen identification before access | Line 296 | ✓ |
| Repository access needed | Line 297 | ✓ |
| Kickoff sync with SMEs | Line 298 | ✓ |
| Preliminary analysis first week | Line 300 | ✓ |

---

## Content Added in v3 (Not in v2)

| Addition | Location | Rationale |
|----------|----------|-----------|
| Problem Statement section | Lines 18-30 | Professional proposals require formal problem framing |
| Success Criteria | Lines 24-30 | Missing from v2; standard for proposals |
| Assumptions and Dependencies | Lines 252-265 | Standard consulting proposal section |
| Risk Factors table | Lines 269-276 | Standard consulting proposal section |

---

## Content Modified (v2 → v3)

| v2 Phrasing | v3 Phrasing | Reason for Change |
|-------------|-------------|-------------------|
| "This is not a skinning exercise" | "beyond typical UI modernization efforts" | Slang removed |
| "tribal knowledge baked into" | "institutional knowledge embedded within" | Colloquial language removed |
| "This isn't about X- it's about Y" | "This conversion effort therefore requires" | AI anti-pattern removed |
| "The Flywheel Effect" | "Acceleration Mechanism" | Blog-style header removed |
| "The Math" | "Staffing and Velocity Model" | Casual header removed |
| "I'm working solo" | "BayOne will staff...with a single senior resource" | First person removed |
| "Happy to discuss" | "BayOne Solutions welcomes the opportunity to discuss" | Casual closer removed |
| "We're not asking you to take our word" | Removed entirely | Defensive/casual language |
| "heavy lifting" | "foundational work" / "infrastructure" | Colloquialism removed |

---

## Verification: No Substantive Content Removed

All technical details, methodology explanations, timeline commitments, scope definitions, agent descriptions, pattern tables, and strategic framing from v2 are present in v3.

The only removals were:
1. Casual/colloquial language
2. First-person pronouns
3. Blog-style rhetorical devices
4. "Isn't X, it's Y" constructions
5. Excessive em-dashes

**Conclusion:** v3 preserves all substantive content from v2 while applying professional consulting proposal conventions.
