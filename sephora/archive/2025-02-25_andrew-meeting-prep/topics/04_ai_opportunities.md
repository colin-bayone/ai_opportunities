# AI Opportunities - Comprehensive Analysis

## AI Needs Explicitly Stated by Sephora

### Need #1: Batch Report Processing
> "If we go report by report, it will take a long time for us. So we are saying what would be an easier way, what would be the right way, efficient way... can we do something like maybe if we do this, we can finish off three reports at one shot... we can finish off like six reports at one shot, so we can expedite the delivery."
> — Mani, Meeting 1

**What They Want:**
- Process multiple reports simultaneously
- Pattern-based grouping
- Template extraction
- Multiplied throughput

**AI Approach:**
- Clustering algorithms to group similar reports
- Template detection across report families
- Batch re-engineering pipelines
- Automated categorization

### Need #2: Codebase Analysis
> "AI would itself would kind of proactively come and tell us, 'these things are actually something to watch out for.' It will tell us where all actually it will analyze the codebase and then say, okay, these are all the places for us to mind for."
> — Mani, Meeting 1

**What They Want:**
- Automated code scanning
- Hidden logic surfacing
- Dependency mapping
- Risk identification
- Proactive alerting

**AI Approach:**
- LLM-based code analysis
- Static analysis for dependencies
- Pattern matching for business rules
- Risk scoring algorithms
- Anomaly detection

---

## Colin's Proposed AI Value Areas (Meeting 2)

### Area 1: Pattern Detection & Clustering

**Description:**
> "Looking across reports, a lot of reports tend to have a lot of similarity. And that does allow for patterns to be extracted and found in those reports so that you can then pass it to humans, so that the human is essentially looking at multiple things at once. They're not having to review report by report anymore. They can do this in more aggregate fashion."
> — Colin, Meeting 2

**Techniques:**
- Algorithmic clustering (traditional ML)
- GenAI for pattern recognition
- Hybrid approach recommended

**Benefits:**
- Reduces cognitive load on SMEs
- Enables batch review
- Identifies consolidation opportunities
- Accelerates throughput

**Mani's Response:** Positive alignment ("exactly what we are approaching")

### Area 2: Code & Business Logic Extraction

**Description:**
> "To surface that business logic, to show those dependency maps, to show all these reports, even who are users for what, or what information are they sharing? Could these be consolidated? Do we have multiple reports just because maybe there's not a proper hierarchy?"
> — Colin, Meeting 2

**Capabilities:**
- SQL extraction from Cognos
- Business rule identification
- Dependency visualization
- User/report mapping
- Consolidation recommendations

**Benefits:**
- Reveals hidden logic
- Maps tribal knowledge
- Identifies redundancy
- Reduces modernization scope

**Mani's Response:** Aligned with their needs

### Area 3: Automated Mapping & Validation

**Description:**
> "Even with AI in the picture, you still have to validate. You can't just turn AI loose as much as we'd like to sometimes. It doesn't work. So this helps to reduce the work because we're using more deterministic systems, higher reliability patterns to do this rather than just saying, 'Hey, ChatGPT, look at this report and compare to this and give you some files and output.' We're going a lot deeper than that."
> — Colin, Meeting 2

**Approach:**
- Deterministic + AI hybrid
- High-reliability validation patterns
- Source-to-target mapping automation
- Parity checking tools

**Benefits:**
- Reduces manual validation burden
- Higher confidence in automated work
- Exception-based human review
- Faster iteration cycles

**Mani's Response:** Appreciated the pragmatic, not-just-ChatGPT approach

### Area 4: Accelerated Modernization Work

**Description:**
> "Assist with Databricks pipelines. Offload repetitive tasks from Sephora SMEs. Support teams during modernization without slowing BAU work."
> — Colin summary

**Capabilities:**
- Pipeline re-engineering assistance
- Transformation logic conversion
- Testing automation
- Performance optimization suggestions

**Benefits:**
- SME bandwidth freed
- BAU continues uninterrupted
- Faster pipeline migration
- Quality maintained

---

## AI Tools Already in Use at Sephora

| Tool | Type | Status | Source |
|------|------|--------|--------|
| Databricks AI tools | Platform-native | In use/evaluating | Mani, Meeting 2 |
| Lutra | AI/Automation | In use | Mani, Meeting 2 |
| Flow | AI/Automation | In use | Mani, Meeting 2 |
| Partner accelerators | Various | Evaluated | Mani, Meeting 2 |

**Implication:** BayOne must integrate with, not replace, existing tools

---

## Sephora's AI Strategy Context

### Marketing AI Task Force
> "We are similar to what you guys have done. We also have a marketing AI focused task force. This task force will be in the front foot working and partnering with enterprise-wide AI task force we have."
> — Mani, Meeting 1

### Agentic AI Interest
> "We are coming up with completely like agentic AI and all those things. So that will be a new required skill set."
> — Mani, Meeting 1

**Implication:** Sephora has broader AI ambitions; EDW modernization AI should connect to this

---

## What Mani Asked For in AI Proposal

| Requirement | Mani's Words | Priority |
|-------------|--------------|----------|
| Integration with existing AI | "How AI integrates with existing strategy" | High |
| Avoiding silos | "Avoiding silos" | High |
| Practical not hype | (Implicit in validation discussion) | High |
| Case studies | "Do you have examples?" | High |
| Cost quantification | "What kind of investment?" | High |

---

## AI Opportunities Matrix

| Opportunity | Sephora Need | BayOne Capability | Competition | Priority |
|-------------|--------------|-------------------|-------------|----------|
| Pattern clustering | High (explicit ask) | High (Colin's expertise) | Medium (Databricks has tools) | **High** |
| Code analysis | High (explicit ask) | High | Medium | **High** |
| Mapping automation | High (implied) | Medium-High | Medium | **High** |
| Validation acceleration | Medium (acknowledged) | High (deterministic approach) | Low | **Medium** |
| Pipeline re-engineering | Medium | Medium | High (Databricks native) | **Medium** |
| Semantic layer AI | Low (pragmatic approach) | Medium | Low | **Low** |

---

## Competitive Positioning on AI

### Databricks Position
- Has seat at governance table
- Native AI tools available
- Partner ecosystem with accelerators
- "Already asked Databricks for recommendations"

### BayOne Differentiation
| Aspect | Databricks | BayOne |
|--------|------------|--------|
| Platform | Owns the platform | Platform-agnostic |
| Focus | Broad platform capabilities | Specific modernization AI |
| Approach | Tool-centric | Methodology-centric |
| Experience | Product company | Consulting + implementation |
| Integration | Their tools | Integrates with any tools |
| Commitment | Account management | Dedicated engagement |

### Key Differentiator
> "The only thing I would say is experience. We know the pain points. We know where things get stuck."
> — Colin, Meeting 2

**Not:** Better AI technology
**Rather:** Experience applying AI to this specific problem

---

## AI Approach Principles (From Colin)

### Hybrid Over Pure AI
> "This is going to be a combination of things. More traditional ML-based approaches, but also some of the nice agentic features."
> — Colin, Meeting 2

### Deterministic Over Probabilistic (Where Possible)
> "We're using more deterministic systems, higher reliability patterns to do this rather than just saying, 'Hey, ChatGPT, look at this report.'"
> — Colin, Meeting 2

### Human-in-the-Loop
> "You can't just turn AI loose as much as we'd like to sometimes. It doesn't work."
> — Colin, Meeting 2

### Practical Outcomes Focus
- Not AI for AI's sake
- Measurable acceleration
- Reduced burden, not replaced humans
- Integrated with existing tools

---

## AI Pilot Opportunities

### Option A: Pattern Detection Pilot
- Focus: Report clustering for batch processing
- Data: Cognos report inventory
- Outcome: Grouped reports by template/pattern
- Value: Enables batch re-engineering
- Track: Any track with sufficient volume

### Option B: Code Analysis Pilot
- Focus: Business logic extraction from Cognos
- Data: Sample Cognos reports (complex ones)
- Outcome: Extracted business rules, dependencies
- Value: Accelerates SME review
- Track: Finance (almost done, can compare to manual results)

### Option C: Mapping Validation Pilot
- Focus: Source-to-target parity checking
- Data: Completed Finance track mappings
- Outcome: Automated validation vs. manual
- Value: Proves time savings for future tracks
- Track: Finance (can use as proof point)

### Recommended Pilot
**Option A (Pattern Detection)** on **Merchandising or Supply Chain track**
- Fresh track (not yet started)
- Can prove value from beginning
- No comparison to "we already did this manually"
- Clean methodology demonstration

---

## Questions to Answer About AI

### For Grishi/Andrew Meeting
1. What AI tools have you tried that disappointed?
2. What's working well with Lutra/Flow?
3. What's Databricks specifically proposing for AI?
4. Where do you see biggest AI acceleration potential?
5. What would success look like for an AI pilot?

### For Proposal Development
1. What report volume is available for pilot?
2. Can we access sample Cognos reports for analysis?
3. What's the governance process for new AI tools?
4. Who needs to approve AI methodology changes?
5. What security/compliance constraints exist?
