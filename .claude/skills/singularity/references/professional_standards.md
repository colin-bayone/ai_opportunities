# Professional Document Standards

Standards for Big Four consulting quality documents. These are what TO DO, complementing anti-patterns (what to avoid).

---

## Table of Contents

1. [Document Structure](#document-structure)
2. [Voice and Tone](#voice-and-tone)
3. [Headers and Sections](#headers-and-sections)
4. [Technical Content](#technical-content)
5. [Proposals and Deliverables](#proposals-and-deliverables)
6. [Tables and Lists](#tables-and-lists)
7. [Closings and Next Steps](#closings-and-next-steps)

---

## Document Structure

### Required Sections for Proposals

1. **Executive Summary** - 2-3 paragraphs maximum, covers what/why/outcome
2. **Problem Statement** - What challenge is being addressed
3. **Proposed Approach** - How the work will be done
4. **Scope and Timeline** - What's included, what's not, when
5. **Investment/Pricing** - Cost structure
6. **Assumptions and Dependencies** - What must be true
7. **Risk Factors** - Potential issues and mitigations
8. **Next Steps** - Clear actions with owners

### Section Ordering

- Lead with what matters to the reader (their problem, the outcome)
- Technical details come after business context
- Assumptions and risks near the end, before next steps
- Keep appendices for deep technical reference

---

## Voice and Tone

### Organizational Voice

| Avoid | Use |
|-------|-----|
| "I will deliver..." | "BayOne will deliver..." |
| "My approach..." | "The proposed approach..." |
| "I'm confident that..." | "This methodology has proven..." |
| "Colin will lead..." | "A senior BayOne resource will lead..." |

### Confident Without Arrogant

| Avoid | Use |
|-------|-----|
| "We might be able to..." | "BayOne will..." |
| "Hopefully this works..." | "This approach has succeeded in similar engagements." |
| "We're the best at this." | "BayOne has executed similar conversions across [specific examples]." |

### Direct Statements

| Avoid | Use |
|-------|-----|
| "It could be argued that..." | "The evidence shows..." |
| "One might consider..." | "Consider..." or just state the point |
| "It's worth noting that..." | State the point directly |

---

## Headers and Sections

### Header Style

| Avoid | Use |
|-------|-----|
| "The Flywheel Effect" | "Acceleration Mechanism" |
| "The Math" | "Staffing and Velocity Model" |
| "Why This Matters" | "Business Impact" |
| "Getting Started" | "Implementation Approach" |
| "What's Next?" | "Next Steps" |

### Header Hierarchy

- `#` - Document title only
- `##` - Major sections
- `###` - Subsections
- `####` - Rarely needed, consider restructuring

### Consistency

- Use parallel structure across headers at the same level
- Noun phrases preferred: "Technical Requirements" not "What We Need Technically"
- No punctuation in headers (no colons, question marks)

---

## Technical Content

### Demonstrate Understanding

Show you understand the specific technology:

| Weak | Strong |
|------|--------|
| "We'll convert the UI" | "Dojo widgets manage their own lifecycle and state in ways that must be mapped to Angular's component model and dependency injection system." |
| "The code is complex" | "After 15 years of evolution, the system exhibits tight coupling between UI components and backend services." |

### Concrete Over Abstract

| Weak | Strong |
|------|--------|
| "We have experience" | "BayOne has executed similar conversions including C# to Rust and Spring to Go." |
| "Results will improve" | "Per-screen velocity improves as pattern application replaces pattern discovery." |
| "This is efficient" | "Cut proposal writing time from 3 hours to 45 minutes." |

### Qualify Appropriately

When uncertain, be precise about what you know:

| Overconfident | Appropriately Qualified |
|---------------|------------------------|
| "EPNM uses DataGrid extensively" | "Example pattern mappings (illustrative; actual patterns will be identified during codebase exploration)" |
| "This will take 2 weeks" | "Estimated duration: 2 weeks from code access" |

---

## Proposals and Deliverables

### Success Criteria

Always include explicit success criteria:

> This proof-of-concept will be considered successful if:
> 1. Two to three representative screens are fully converted and functional
> 2. Backend logic supporting these screens is implemented
> 3. Automated visual validation confirms behavioral equivalence
> 4. A documented pattern library enables estimation of remaining scope

### Scope Boundaries

Be explicit about what's included AND excluded:

**Included:**
- 2-3 representative screens
- End-to-end conversion including backend logic
- Automated visual validation

**Excluded:**
- Additional screens beyond agreed scope
- New backend services (gaps will be documented)
- Production deployment

### Investment Framing

| Avoid | Use |
|-------|-----|
| "This is free" | "BayOne is providing this proof-of-concept at no cost to Cisco as a demonstration of capability." |
| "We'll do it for free" | "This represents BayOne's investment in demonstrating capability." |

---

## Tables and Lists

### When to Use Tables

- Comparing options or approaches
- Mapping patterns (old to new)
- Phase/timeline breakdowns
- Feature comparisons

### Table Structure

- Clear headers
- Consistent column alignment
- Brief cell content (expand in prose if needed)
- Notes column for qualifications

Example:
| EPNM Pattern | EMS Equivalent | Notes |
|--------------|----------------|-------|
| Dojo DataGrid | Angular Material table | May require endpoint modification |

### When to Use Lists

- Sequential steps (numbered)
- Non-sequential items (bulleted)
- Requirements or criteria

### List Best Practices

- Parallel structure across items
- Complete sentences or consistent fragments, not mixed
- 3-7 items typical; longer lists need subgroups

---

## Closings and Next Steps

### Professional Closings

| Avoid | Use |
|-------|-----|
| "Happy to discuss!" | "BayOne welcomes the opportunity to discuss any aspect of this proposal." |
| "Let us know!" | "Please contact [name] with questions." |
| "Looking forward to hearing from you!" | "BayOne is prepared to begin upon approval." |

### Next Steps Format

Always include:
1. Specific actions
2. Owners (which party)
3. Dependencies
4. Timeline if applicable

Example:
> **Next Steps**
> 1. **Hardware delivery:** BayOne will confirm date and notify Cisco upon receiving access
> 2. **Initial context:** Cisco team identifies candidate screens for consideration
> 3. **Repository access:** Upon hardware readiness, BayOne requires access to EPNM and EMS codebases
> 4. **Kickoff:** Brief synchronization to align on priorities and introduce relevant SMEs

---

## Checklist Before Delivery

### Mechanical

- [ ] No em-dash overuse (max 5 in entire document)
- [ ] No contractions in formal sections
- [ ] No first-person pronouns
- [ ] No emojis
- [ ] Consistent header capitalization
- [ ] Tables have clear headers

### Content

- [ ] Executive summary captures key points
- [ ] Success criteria are explicit
- [ ] Scope boundaries are clear (included AND excluded)
- [ ] Timeline has concrete milestones
- [ ] Assumptions documented
- [ ] Risks acknowledged with mitigations
- [ ] Next steps have owners and actions

### Tone

- [ ] Organizational voice throughout
- [ ] Confident without arrogant
- [ ] Technical depth demonstrates understanding
- [ ] No AI anti-patterns (check reference)
- [ ] Would a Big Four consultant send this?
