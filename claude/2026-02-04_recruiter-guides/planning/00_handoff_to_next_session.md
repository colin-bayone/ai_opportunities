# Handoff: Recruiter Guide Development

## Session Summary

This session attempted to improve recruiter guides for 4 roles (Senior AI Solutions Engineer, Automation Engineer, AI Engineer, Agentic AI Engineer). The initial attempts were poor - I was lazy, made factual errors (called LangChain/LangGraph synonyms when they're completely different), removed confirmed stack items (Postgres), and added irrelevant frameworks (BabyAGI).

Colin redirected to do proper research before continuing.

---

## Research Completed

Three research documents are in `/claude/2026-02-04_recruiter-guides/research/`:

1. **01_ai_engineer_landscape_2026.md** - Market context, skill levels, LLM ecosystem, production vs POC signals, common tech stacks, recruiting keywords

2. **02_recruiter_search_strategies.md** - Boolean search practices, synonym expansion, signal vs noise, tiered searching, what non-technical recruiters need

3. **03_cisco_project_context.md** - Technical environment, the 6 capability areas, role differentiation, constraints, success criteria

---

## Research Pattern to Replicate

For each role, the next session should:

1. **Re-read the specific JD** in `/deliverables/jd_*.md`
2. **Cross-reference with project context** (what does this role actually do for Cisco?)
3. **Apply market research** (what distinguishes this level? what are the production signals?)
4. **Think in tiers**: Must-have → Preferred → Nice-to-have
5. **Think in synonyms**: Group related terms for non-technical recruiters
6. **Avoid generic padding**: Only include confirmed or highly relevant items

---

## Confirmed Tech Stack (Do Not Remove)

| Confirmed | Source |
|-----------|--------|
| PostgreSQL + pgvector | Colin confirmed |
| Apache Airflow | JDs, project docs |
| Jenkins | JDs, project docs |
| Bazel | JDs, project docs |
| Claude API | Colin confirmed |
| OpenAI API | Colin confirmed |
| LangChain | JDs |
| LangGraph | JDs |
| Python | Everything |
| FastAPI or Django | JDs |
| Grafana | Project docs |
| On-prem deployment | Project constraint |

---

## Key Learnings from This Session

1. **LangChain ≠ LangGraph** - LangChain is general orchestration, LangGraph is for stateful agent graphs. NOT synonyms.

2. **Senior ≠ Depth** - Tools like LangSmith/LangFuse signal depth of experience, not seniority. Seniority is about demonstrated project outcomes, architecture ownership, mentoring.

3. **Production = business relies on it** - Not about user count. It's reliability, robustness, testing, security. Would be a loss if it went offline. NOT a POC done by one person.

4. **RAG/pgVector is table stakes** for any senior AI engineer in 2026. Missing it is a red flag.

5. **Industries > Companies** for targeting. 100+ employee companies ideal for this role. Don't be rigid about specific company names.

6. **Synonyms are useful** for non-technical recruiters (Claude/Anthropic, OpenAI/GPT), but don't call unrelated things synonyms.

7. **Tiered searching**: AND for must-haves, OR for nice-to-haves. Structure searches in layers.

8. **Don't pad with irrelevant frameworks** like BabyAGI, random vector DBs we're not using, etc.

---

## Current State of Recruiter Guides

Location: `/deliverables/job_descriptions/recruiter_guides/`

All 4 guides exist but the search strings and tech stacks are weak/wrong. They need to be rewritten using the research.

---

## Next Steps for New Session

1. **Go role by role** - Start with Senior AI Solutions Engineer
2. **Ask clarifying questions** before making changes
3. **Propose changes in chat first** - Don't just edit files
4. **Add value** - Don't just parrot back what Colin says
5. **Use the research** - Reference specific findings from the research docs
6. **Be precise** - Use confirmed stack items, don't invent

---

## Colin's Preferences (Observed)

- Hates verbose chat responses - be concise
- Hates generic/lazy work - add actual value
- Prefers targeted questions over "what do you want?"
- Wants collaborative refinement, not blind execution
- Gets frustrated when I make obvious errors or ignore what he said
- Values efficiency - if I'm slower than him doing it alone, something's wrong
