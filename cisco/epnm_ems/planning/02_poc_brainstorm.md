# POC Proposal Brainstorm - Working Notes

**Status:** In progress
**Last updated:** Feb 21, 2026

---

## Core Tension

We need to demonstrate capability without:
- Over-committing on free work
- Appearing unconfident or effort-averse
- Picking screens that explode in scope due to hidden dependencies

---

## Key Constraints

1. **We've never seen the code or any screens** - flying blind on complexity
2. **"Backend isn't set up yet" for some screens** - red flag for scope creep
3. **10 screens is too much for free work** - need to scope down diplomatically
4. **Their team has limited time** - can't rely on heavy pairing

---

## Screen Selection Strategy

**Who should choose:** Cisco SMEs propose candidates, we verify during exploration

**Why this approach:**
- They know which screens have manageable interdependencies
- They know which are representative vs. edge cases
- We validate feasibility once we can see the code
- Shared ownership of scope decisions

**What we don't know yet:**
- Screen categories in play:
  - [ ] Data entry forms
  - [ ] Control panels
  - [ ] Reports
  - [ ] Dashboards
  - [ ] Configuration wizards
  - [ ] Real-time monitoring views
  - [ ] Other?

**Category matters because:**
- Data entry forms → relatively self-contained, good POC candidates
- Dashboards with live data → streaming/websocket complexity
- Reports → may have heavy backend aggregation logic
- Control panels → may touch many backend services

---

## Risk Factors to Screen For

When Cisco proposes screens, we should ask/verify:

1. **Interdependencies** - Does this screen pull from multiple services/tables?
2. **Backend state** - Is the backend logic already in EMS, or does it need to be built?
3. **Real-time requirements** - Static data vs. streaming/polling?
4. **External integrations** - Does it talk to other Cisco systems?
5. **Complexity tier** - Is this representative or an outlier?

---

## Discussion Notes

### Colin (Feb 21):
- 10 screens is too much for free - need to scope down
- Let them propose, we verify feasibility during exploration
- Nervous about "backend isn't set up yet" comment - don't want scope to explode
- Don't want to appear unconfident or effort-averse
- Category of screen matters - we don't know the distribution yet
- Their SMEs are best positioned to identify low-risk candidates until we see code
- Need to understand: is this mostly forms? dashboards? reports?

**On two-phase approach:**
- Loves the Exploration → Conversion split
- Phase 1 can be quick and is gated by access + engineer collaboration
- Some Phase 1 work can happen while waiting for laptop
- Need to phrase this very clearly in proposal - partnership, not hedging

**On timeline:**
- POC is 4 weeks total, timer starts when we have repo access
- Can frame as "max 4 weeks once we have repo access"
- Don't sound unconfident - this is normal procedure
- Cisco should provide screen examples and criteria upfront
- Push them to frame first part of work; we validate feasibility

**On flywheel/acceleration:**
- Need to explain WHY it gets faster, not just assert it
- Custom agents built for THIS codebase = tangible proof
- Conversion itself is <1 day once patterns established
- Most of 4 weeks is one-time exploration/setup
- Can't just say "it gets faster" - sounds like pipe dream
- Show concrete mechanism: codebase analysis → pattern library → custom agents → parallel execution

**On POC boundary:**
- Clear line between POC and paid engagement
- POC = free investment that becomes foundation for paid work
- Colin solo for POC (fastest for simplicity)
- Paid = team scale, parallel streams, multiplicative speedup
- POC pace is the floor, not the ceiling

---

## Open Questions for Cisco

1. What categories of screens are we talking about? (forms, dashboards, reports, etc.)
2. For the screens you'd prioritize, is the backend logic already in EMS or does it need conversion too?
3. Which screens would your team consider "representative but not the most complex"?
4. Are there screens that are relatively self-contained vs. ones with heavy cross-dependencies?

---

## POC Structure: Two-Phase Approach

### The Rationale

**Problem:** We're proposing a POC for work we've never seen. Picking screens blind risks:
- Choosing something with hidden complexity that blows up scope
- Appearing to under-deliver if we hit unexpected dependencies
- Cisco feeling like they picked "wrong" if a screen turns out to be an outlier

**Solution:** Split into Exploration + Conversion phases. This:
- Makes Cisco a partner in scope decisions (not us dictating limits)
- Protects both parties from bad screen selection
- Lets us demonstrate rigor and methodology, not just output
- Positions us as thoughtful consultants, not just coders

**Key framing:** We're not saying "we can only do 2" - we're saying "let's make sure we pick the right ones together."

---

### Phase 1: Exploration & Screen Selection

**What:** Analyze codebase, categorize screens by complexity, identify 2-3 good POC candidates collaboratively with Cisco SMEs.

**Deliverable:** Analysis document + recommended screens with rationale

**Gating factors:**
- Code access (Cisco laptop or approved alternative)
- Collaboration with their engineers (context, priorities)

**Good news:** Some of this can start before laptop arrives:
- Initial conversations with SMEs about screen categories
- Understanding their prioritization criteria
- Reviewing any documentation they can share
- Setting up tooling and approach

---

### Phase 2: Conversion & Demonstration

**What:** Convert agreed screens from EPNM → EMS, end-to-end (UI + backend)

**Deliverables:**
- Working code (deployed/demoed in EMS)
- Documented conversion process (repeatable pattern)
- Estimation model (extrapolate from POC to full scope)

**Why this sequence works:**
- Phase 1 validates feasibility before committing to specific screens
- Phase 2 has clear, agreed scope - no surprises
- Both phases demonstrate value (analysis + execution)

---

## The Flywheel: Why It Accelerates

**The Problem to Avoid:** "2-3 screens took 4 weeks? That means 200 screens = 200+ weeks!"

**The Truth:** The POC is front-loaded with one-time work. The actual conversion, once running, is less than a day per screen. The 4 weeks is mostly investment that never repeats.

### The Mechanism (Why It Actually Gets Faster)

| Work | One-Time? | What It Produces |
|------|-----------|------------------|
| Codebase exploration | Yes | Knowledge graph mapping architecture, relationships, patterns |
| Pattern identification | Yes | "EPNM pattern X → EMS pattern Y" conversion library |
| Custom agent development | Yes | AI agents tuned to THIS codebase, encoding nuances and tribal knowledge |
| Workflow design | Yes | Validated, repeatable conversion process |
| Screen conversion | Per screen | Apply known patterns, run trained agents |
| Testing/validation | Per screen | Gap analysis, fixes |

### The POC Investment

The heavy lifting we do for free during the POC:
- Full codebase analysis and mapping
- Custom agents built specifically for EPNM→EMS conversion
- Validated conversion patterns
- Documented workflow

**This is the foundation for the real work.** If Cisco proceeds to a paid engagement, they're not starting from zero - they're starting with infrastructure already in place.

### Post-POC Acceleration

Once patterns are locked and agents are built:
- Each screen is execution against known patterns (not discovery)
- Multiple team members can run the same playbook in parallel
- No stepping on each other because the approach is codified
- Colin's solo POC pace is the *floor*, not the ceiling

### The Staffing Story

- **POC:** Colin solo, sequential work = slowest possible pace (but establishes everything)
- **Paid:** Team members + parallel streams = multiplicative speedup
- **The math:** POC proves per-screen velocity. Team scale multiplies it.

### Key Phrasing

> "The POC establishes the infrastructure - codebase analysis, custom agents tuned to your architecture, validated conversion patterns. That's the investment we're making. Once it's in place, each additional screen is execution against known patterns, and multiple team members can run in parallel."

> "This is heavy lifting we're doing for free during the POC. It forms the foundation for the real work should you choose to proceed."

---

## POC Scope Options

*To be developed as discussion continues*

| Option | Screens | Risk | Demonstrates |
|--------|---------|------|--------------|
| A | ? | ? | ? |
| B | ? | ? | ? |
| C | ? | ? | ? |

---

---

## Formatting Rules (Hard Rules)

**Hyphens and slashes:** No space before. Space after is OK.
- Wrong: `system - architecture`
- Right: `system- architecture`
- Right: `system-architecture` (no spaces at all also OK)

This applies to em-dashes used as separators in prose.

---

## Next Steps

- [ ] Continue brainstorm with Colin
- [ ] Develop scope options
- [ ] Draft proposal language
