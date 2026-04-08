# LinkedIn Search String Reference

**Purpose:** Properly constructed, tested search strings for each role. Use these as the basis for recruiter guide search string sections.

**Important:** These are starting points. Always test in LinkedIn Recruiter before finalizing.

---

## Search String Construction Rules

### Boolean Basics
- **AND** = both terms must appear (narrows results)
- **OR** = either term can appear (broadens results)
- **NOT** or **-** = exclude term (filters out noise)
- **Parentheses** = group terms together
- **Quotes** = exact phrase match

### Common Mistakes to Avoid
1. Not quoting multi-word phrases: `AI engineer` matches "AI" and "engineer" separately
2. Missing parentheses: `A OR B AND C` is ambiguous
3. Using hobbyist frameworks: AutoGPT, CrewAI, BabyAGI are toys, not production tools
4. Forgetting negative modifiers: -recruiter -sales -manager removes noise
5. Making Layer 1 too narrow: If it returns 0 results, it's useless

---

## Senior AI Solutions Engineer

**Role context:** Onshore San Jose, client-facing, builds AI-powered features for CI/CD pipeline (chat interfaces, failure diagnosis, dashboards). Needs strong communication skills.

### Layer 1 — Narrow (Start Here)

```
("AI engineer" OR "ML engineer" OR "LLM engineer") AND Python AND (LangChain OR LangGraph OR "RAG" OR "retrieval augmented") AND (production OR shipped OR deployed)
```

**What this finds:** AI/ML engineers with LLM orchestration experience who have shipped to production.

**Expected results:** 50-200 profiles

### Layer 2 — Broader Titles

```
("AI engineer" OR "ML engineer" OR "solutions engineer" OR "applied scientist" OR "senior software engineer") AND Python AND (LLM OR "large language model" OR "generative AI" OR Claude OR OpenAI)
```

**What this finds:** Expands to adjacent titles and broader AI/LLM keywords.

**Expected results:** 200-1000 profiles

### Layer 3 — Widest Net

```
("software engineer" OR "backend engineer" OR "full stack") AND Python AND ("generative AI" OR LLM OR GPT OR ChatGPT OR Claude) AND (API OR backend OR production) -recruiter -sales -manager
```

**What this finds:** General software engineers with any generative AI exposure.

**Expected results:** 1000+ profiles

### Communication Filter (Add to Any Layer)

```
AND (consulting OR "client-facing" OR stakeholder OR presented OR "cross-functional" OR "customer success")
```

**Why:** This role is 25% client-facing. Filter for people with communication experience.

### AI Tools Filter (Add to Any Layer)

```
AND ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI" OR "AI-assisted development")
```

**Why:** AI pair programming is a must-have. This surfaces candidates who actively use these tools.

---

## Automation Engineer

**Role context:** Onshore San Jose, client-facing (15%), builds CI/CD integrations with Airflow, Jenkins, Bazel. Focus on connecting systems and data pipelines.

### Layer 1 — Narrow (Start Here)

```
("Apache Airflow" OR Airflow) AND Jenkins AND Python AND (integration OR automation OR pipeline OR built OR developed)
```

**What this finds:** People with both Airflow AND Jenkins experience who build things.

**Expected results:** 30-150 profiles

### Layer 2 — Broader Titles

```
("Platform Engineer" OR "DevOps Engineer" OR "Build Engineer" OR "CI/CD Engineer" OR "Release Engineer" OR "Infrastructure Engineer") AND Python AND (Airflow OR Jenkins OR pipeline OR automation)
```

**What this finds:** Expands to job titles common in this space.

**Expected results:** 150-500 profiles

### Layer 3 — Widest Net

```
("software engineer" OR "backend engineer") AND Python AND ("CI/CD" OR automation OR pipeline OR Jenkins OR Airflow) AND (integration OR built OR developed) -QA -tester -"test automation" -SDET
```

**What this finds:** General engineers with CI/CD exposure. Excludes QA/test roles.

**Expected results:** 500+ profiles

### Communication Filter (Add to Any Layer)

```
AND (consulting OR "client-facing" OR stakeholder OR "cross-functional")
```

**Why:** This role is 15% client-facing.

### AI Tools Filter (Add to Any Layer)

```
AND ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI" OR "AI-assisted")
```

**Why:** Must-have requirement per JD.

---

## AI Engineer (Offshore)

**Role context:** Remote/offshore, builds chat interfaces and dashboards, works with LLMs for conversational AI features. Reports to Senior AI Solutions Engineer.

### Layer 1 — Narrow (Start Here)

```
("AI engineer" OR "LLM engineer" OR "ML engineer") AND Python AND (LangChain OR LangGraph OR "RAG" OR "retrieval") AND (chat OR conversational OR dashboard) AND (production OR shipped)
```

**What this finds:** AI engineers with chat/dashboard experience who have shipped.

**Expected results:** 30-100 profiles

### Layer 2 — Broader Titles

```
("software engineer" OR "full stack" OR "backend engineer") AND Python AND (LLM OR "generative AI" OR OpenAI OR Claude) AND (FastAPI OR Django OR React OR "Next.js") AND (chat OR dashboard OR "user interface")
```

**What this finds:** Full-stack developers with LLM and UI experience.

**Expected results:** 100-400 profiles

### Layer 3 — Widest Net

```
("software engineer" OR developer) AND Python AND ("generative AI" OR LLM OR GPT OR ChatGPT OR OpenAI) AND (API OR backend OR frontend) -"data scientist" -research -intern -junior
```

**What this finds:** General developers with generative AI exposure.

**Expected results:** 400+ profiles

### AI Tools Filter (Add to Any Layer)

```
AND ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI")
```

### Offshore Location Filter (If needed)

```
AND (India OR Bangalore OR Hyderabad OR Pune OR Chennai OR Mumbai OR Delhi OR "remote")
```

---

## Agentic AI Engineer (Offshore)

**Role context:** Remote/offshore, builds autonomous/self-healing systems for CI/CD. Systems that take real actions (retry failed jobs, auto-remediate). Safety and governance focus.

### Layer 1 — Narrow (Start Here)

```
("AI engineer" OR "ML engineer" OR "platform engineer" OR SRE) AND Python AND (autonomous OR "self-healing" OR "auto-remediation" OR "automated recovery" OR "incident automation") AND (production OR deployed)
```

**What this finds:** Engineers who have built systems that take autonomous action in production.

**Expected results:** 20-80 profiles

### Layer 2 — Broader (Add Agentic Keywords)

```
("software engineer" OR "SRE" OR "site reliability" OR "platform engineer" OR "DevOps") AND Python AND (LangGraph OR "function calling" OR "tool calling" OR "tool use" OR agent) AND (automation OR orchestration OR pipeline)
```

**What this finds:** Expands to SRE/platform roles and agentic AI patterns.

**Expected results:** 80-300 profiles

### Layer 3 — Widest Net

```
("software engineer" OR "backend engineer" OR "platform engineer") AND Python AND (LLM OR "generative AI" OR automation) AND (Jenkins OR Airflow OR "CI/CD" OR pipeline OR "build system") -"customer support" -recruiter -sales
```

**What this finds:** Engineers at the intersection of AI and CI/CD.

**Expected results:** 300+ profiles

### CI/CD Context Filter (Important for this role)

```
AND (Jenkins OR Airflow OR "CI/CD" OR pipeline OR "build system" OR "release engineering")
```

**Why:** This role specifically builds self-healing for CI/CD pipelines. Candidates with CI/CD context are more relevant.

### AI Tools Filter (Add to Any Layer)

```
AND ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI")
```

### Offshore Location Filter (If needed)

```
AND (India OR Bangalore OR Hyderabad OR Pune OR Chennai OR Mumbai OR Delhi OR "remote")
```

---

## Common Filters for All Roles

### Exclude Noise

```
-recruiter -"talent acquisition" -sales -"account executive" -manager -director -VP -"vice president"
```

**When to use:** When results include too many non-engineering roles.

### Experience Level

```
AND (senior OR staff OR principal OR lead OR "5+ years" OR "7+ years")
```

**When to use:** When results include too many junior candidates.

### Production Focus

```
AND (production OR shipped OR deployed OR "went live" OR launched OR released)
```

**When to use:** When results include too many researchers or prototype builders.

---

## Testing Your Search Strings

### Step 1: Run in LinkedIn Recruiter
Copy the search string exactly and run it.

### Step 2: Check Result Count
- 0 results = too narrow, remove constraints
- 10-50 results = good for Layer 1
- 50-200 results = good for Layer 2
- 200+ results = appropriate for Layer 3
- 5000+ results = too broad, add constraints

### Step 3: Spot Check Profiles
Open 5-10 profiles from results. Ask:
- Are these the right type of person?
- Do they have relevant experience?
- Are there obvious mismatches?

### Step 4: Iterate
If results are poor, adjust:
- Too few results → remove an AND clause or broaden terms
- Wrong results → add negative modifiers or change keywords
- Too many results → add another AND clause

---

## Framework Guidance for Searches

### Legitimate Multi-Agent Frameworks (Use These)

| Framework | Notes |
|-----------|-------|
| LangGraph | Production-ready, widely adopted for agentic workflows |
| CrewAI | Legitimate multi-agent framework with real adoption |

### Experimental Projects (Avoid These)

| Framework | Why to Avoid |
|-----------|--------------|
| AutoGPT | Viral experiment, not production-ready |
| BabyAGI | Toy project, minimal real-world usage |
| AgentGPT | Web-based toy, not enterprise |
| SuperAGI | Experimental, limited adoption |

### Work Pattern Keywords (Always Valuable)

Search for these regardless of framework: "function calling", "tool calling", "tool use", "autonomous", "self-healing"

**Important:** Framework-specific searches can surface relevant candidates, but always verify production experience during screening. Someone who built demos is not the same as someone who shipped to production.
