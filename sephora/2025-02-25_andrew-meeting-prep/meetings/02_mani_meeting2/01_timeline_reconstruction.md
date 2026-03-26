# Meeting 2 - Timeline Reconstruction

## Chronological Flow of Discussion

### Opening: Colin's Summary (0:00-8:00 estimated)

1. **Colin opens** with summary of his understanding:
   - Three-year EDW project
   - Migration from legacy on-prem to Databricks
   - Reports: Cognos + SSAS cubes
   - Target: ThoughtSpot and Tableau
   - Pipelines: DataStage to Databricks
   - Cognos retained during transition (change management)
   - Semantic layer being formed

2. **Colin identifies pain points**:
   - Huge scale to tackle
   - All data pipelines need migration
   - Organizational knowledge at risk
   - Logic preservation critical
   - Need for smooth transition
   - Staffing model support needed

3. **Colin asks**: "Am I on the right track?"

---

### Section 1: Mani's Validation & Clarification (8:00-15:00 estimated)

4. **Mani validates**: "You summarized it very well. You understood it very well."

5. **Mani makes critical clarification**:
   > "This is NOT a migration initiative. This is completely re-engineering. That's why we are not calling this migration, but modernization."

   - Not lift-and-shift
   - Have to re-engineer and rewire
   - Most cases: retain front-end (Cognos stays)
   - No push for ThoughtSpot/Tableau yet
   - Change management friction being minimized

6. **Colin acknowledges**: "That's a good start."

---

### Section 2: Architecture & Patterns Discussion (15:00-25:00 estimated)

7. **Colin asks** about architecture assistance needs

8. **Mani explains track-based approach**:
   - Category by category (Finance, Supply Chain, Merchandising, Stores)
   - Finance is Track 1
   - Architectural patterns established for Finance
   - Accelerators evaluated and selected
   - "Pattern has been established"
   - Other tracks (Merchandising) not yet detailed

9. **Mani describes team structure**:
   - Core cross-functional working group
   - Databricks has seat at table
   - Microsoft has seat at table
   - Data Platform team involved
   - Store Engineering involved
   - "This team establishes what's right to do, how to do it"

10. **Mani emphasizes team investment**:
    - "Deep efforts have gone in the last 3 months"
    - Patterns established
    - Accelerators selected
    - Roadmap sequencing defined

---

### Section 3: Semantic Layer Discussion (25:00-30:00 estimated)

11. **Colin asks** about semantic layer maturity

12. **Mani's response** - pragmatic approach:
    - "Not going to address everything as one shot"
    - Ongoing effort
    - Won't let semantic work slow down modernization
    - "If semantic layer is slowing us down, we just go ahead with engineering"
    - Prefers progress over perfection

13. **Mani names owners**:
    > "Terti and Andrew would be good to do it. They have the right people to do that."

---

### Section 4: AI Tools Discussion (30:00-35:00 estimated)

14. **Colin asks** about existing AI tools/initiatives

15. **Mani's response**:
    - Team is using AI to accelerate
    - Mentions: Lutra, Flow, and others
    - "More details Grishi might have already told you"

---

### Section 5: Colin's Presentation (35:00-50:00 estimated)

16. **Colin shares screen** - AI-assisted EDW approach

17. **Colin presents challenge slide**:
    - Lots of reports, KPIs
    - Common definitions needed
    - Disparate systems consolidation
    - Tribal knowledge in legacy systems
    - SMEs valuable but constrained
    - Mapping validation time-consuming

18. **Colin presents AI value areas**:

    **Area 1: Pattern Detection & Clustering**
    - Look across reports for patterns
    - Reduce cognitive load on SMEs
    - Enable aggregate review (not report-by-report)
    - Hybrid: algorithmic + GenAI

    **Area 2: Code & Business Logic Extraction**
    - Surface SQL/business rules
    - Dependency mapping
    - Identify consolidation opportunities
    - "Could these be consolidated?"

    **Area 3: Automated Mapping & Validation**
    - Deterministic + AI methods
    - Reduce manual "line-by-line" validation
    - Higher reliability patterns
    - Risk-based automation (some auto, some human)

    **Area 4: Accelerated Modernization Work**
    - Assist with Databricks pipelines
    - Offload repetitive tasks
    - Support teams during transition
    - Don't slow BAU work

19. **Colin offers staffing support** alongside solutions work

---

### Section 6: Engagement Discussion (50:00-60:00 estimated)

20. **Colin proposes starting points**:
    - Finance pilot (already well-defined)
    - Or untouched track for fresh start
    - Can extend methodology once proven

21. **Mani asks**: "What is the unique value you bring?"

22. **Colin responds**:
    - Direct experience doing this before
    - Know the pain points
    - Know where things get stuck
    - Can work with existing AI strategy (not siloed)

23. **Mani asks** for case studies

24. **Colin offers** to share:
    - Patter case study
    - Evaluator case study
    - Custom connector work

25. **Mani asks** about cost/timeline assumptions

---

### Section 7: Proposal Requirements (60:00-70:00 estimated)

26. **Mani requests 3 proposal options**:

    **Option 1: Small confidence-builder**
    - Prove capability quickly
    - Scoped slice

    **Option 2: Co-delivery model**
    - Sephora owns architecture
    - BayOne supports implementation + AI

    **Option 3: Larger partnership**
    - Flexible staffing
    - Rotating specialists

27. **Mani specifies proposal requirements**:
    - Clear assumptions
    - Estimated cost range
    - Where acceleration happens
    - Integration with existing AI strategy
    - Case studies included

28. **Pilot track discussion**:
    - Finance almost done (~20-24 days left)
    - Merchandising suggested
    - Supply Chain possible
    - "Propose a few options"

---

### Section 8: Logistics & Close (70:00-75:00 estimated)

29. **Zahra proposes** in-person follow-up

30. **Mani's schedule**:
    - Next week fully blocked (short week, offsite Wednesday, all-hands Thursday)
    - Prefers week after next
    - Wants to attend personally

31. **Colin confirms** flexibility:
    - Based in Pittsburgh
    - Will travel for meetings
    - Remote or in-person as needed

32. **Zahra mentions** Cisco engagement context

33. **Mani appreciates** consistent on-site presence

34. **Meeting ends** on very positive note

---

## Key Transition Points

| Time (est.) | Transition | Significance |
|-------------|-----------|--------------|
| ~8 min | Colin summary → Mani validation | Confirmed understanding correct |
| ~15 min | Validation → Architecture deep-dive | Moved to specifics |
| ~25 min | Architecture → Semantic layer | Revealed pragmatic approach |
| ~35 min | Discussion → Presentation | Colin took control with visuals |
| ~50 min | Presentation → Engagement models | Moved to "how to work together" |
| ~60 min | Models → Proposal requirements | Mani specified exactly what he wants |
| ~70 min | Requirements → Logistics | Scheduled follow-up |

---

## Meeting Arc

```
Opening     → Validation  → Deep Dive   → Presentation → Requirements → Close
(Summary)     (Aligned!)    (Details)     (AI Value)     (3 Options)    (Next Steps)
    |             |             |             |               |              |
 Prepared     Credibility   Technical    Demonstrated    Clear Ask      Positive
              Established   Exchange     Capability      Defined        Momentum
```

## Momentum Assessment

Meeting started positive and **built throughout**. No dips in energy or engagement. Ended at highest point with clear next steps and Mani wanting to personally attend follow-up.
