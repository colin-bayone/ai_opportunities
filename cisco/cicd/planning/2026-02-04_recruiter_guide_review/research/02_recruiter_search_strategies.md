# Recruiter Search Strategies for AI/ML Engineers

## Boolean Search on LinkedIn

### What Works
- **Parentheses are critical** - Always use to specify order of operations
- **Uppercase operators required** - AND, OR, NOT must be capitalized
- **Quote exact phrases** - Use straight quotation marks for "machine learning engineer"
- **Avoid unsupported operators** - No + or - symbols, no wildcard asterisks

### Limitations
- Character limits around 2,000 characters (free/Premium)
- LinkedIn caps the number of AND/OR operators
- No time-based filtering for job titles
- No wildcard support (but auto-handles stemming)
- Results limited to 1,000 per search
- Stop words ("by", "in", "with") ignored

### 2026 Trend
AI-powered search is replacing traditional Boolean. Modern tools interpret concepts (understanding "Django" relates to "Python"). Reduces sourcing time 70%+.

---

## Synonym Expansion Strategy

### Principles
1. Minor differences have major impact - a single dash can multiply results 25x
2. Include common misspellings: `(engineer OR enginer OR engineeer)`
3. Add abbreviations: `("natural language processing" OR NLP)`
4. Research actual profiles - see how candidates actually write skills
5. Consider foreign terms if searching globally

### Example Synonym Groups for AI Roles

**Titles:**
```
("machine learning engineer" OR "ML engineer" OR "data scientist" OR "applied scientist" OR "AI engineer" OR "artificial intelligence engineer")
```

**Core Skills:**
```
(Python OR "Python 3") AND ("machine learning" OR ML OR "deep learning" OR "neural networks")
```

**LLM Providers (synonyms for recruiters):**
```
(Claude OR Anthropic) - same company
(OpenAI OR GPT OR "GPT-4" OR ChatGPT) - same provider
```

**Frameworks:**
```
(TensorFlow OR PyTorch OR Keras OR "scikit-learn" OR sklearn)
```

### For Non-Technical Recruiters
Present as pre-built blocks:
```
TITLE_GROUP = (...)
LANGUAGE_GROUP = (...)
FRAMEWORK_GROUP = (...)

Basic search: TITLE_GROUP AND LANGUAGE_GROUP
Advanced: TITLE_GROUP AND LANGUAGE_GROUP AND FRAMEWORK_GROUP
```

---

## Signal vs. Noise

### High False Positive Terms
- "AI" alone - too broad
- Generic: "data", "analytics", "automation"
- Academic-only: coursework mentions without practical application
- "Data Scientist" - title inflation (many are actually data analysts)
- Buzzword-stuffed resumes

### More Precise Terms
- Specific frameworks/versions: "TensorFlow 2.x", "PyTorch 1.x"
- Production keywords: "model deployment", "production ML", "MLOps", "model serving"
- Kaggle credentials: Grandmaster, competition winner, medal
- Specific problem domains: "recommender systems", "fraud detection", "time series"
- Research: arXiv, NeurIPS, ICML publications

---

## Tiered Searching

### Structure Searches in Layers

**Layer 1 - Must-Have Core (all ANDs):**
```
("machine learning engineer" OR "ML engineer")
AND (Python OR "Python 3")
AND ("machine learning" OR "deep learning")
```

**Layer 2 - Add Framework Requirements:**
```
[Layer 1] AND (TensorFlow OR PyTorch OR Keras)
```

**Layer 3 - Broaden Titles/Skills:**
```
("ML engineer" OR "data scientist" OR "applied scientist")
AND Python
AND ("machine learning" OR "deep learning" OR "predictive modeling")
AND (TensorFlow OR PyTorch OR Keras OR "scikit-learn")
```

### Workflow
1. Start narrow (Layer 1) - if too few results, expand
2. Move to Layer 2/3 gradually
3. Use LinkedIn's filter dropdowns for "Must have" vs "Can have" vs "Doesn't have"

### Decision Tree for Recruiters
- **Try first**: Core role + Python + ML keywords
- **If <20 results**: Add framework alternatives (OR)
- **If <50 results**: Expand role titles
- **If still struggling**: Remove framework requirement

---

## What Non-Technical Recruiters Need

### Simplified Technical Context (one-page cheat sheet)
1. What the role actually does in plain English
2. Key skill translations (Python = programming language, etc.)
3. Red flags to watch for
4. Green flags to watch for

### Screening Questions That Work

1. "Tell me about a project where you built and deployed a machine learning model. Walk me through it from start to finish."
   - Listen for: specific steps, tools mentioned, what went wrong, how they measured success

2. "Can you explain [their most complex project] to me like I'm not a technical person?"
   - Tests communication skills, patience, cross-functional ability

3. "What specific version of [tool they listed] have you used most recently?"
   - Vague answers = shallow expertise

4. "Tell me about a time your model failed in production. What happened?"
   - Tests real production experience, problem-solving, honesty

5. "How did you measure whether your model was working correctly over time?"
   - Tests understanding of evaluation, monitoring, production practices

### Collaboration with Technical Teams
- Pre-screen resumes to identify must-review candidates
- Create role-specific assessments
- Join for 15-minute technical deep-dive
- Debrief with recruiter on what they heard

### Context for Better Screening
- Example projects from your company
- Day-in-the-life description
- Team structure context
- Success metrics
- Collaboration expectations
