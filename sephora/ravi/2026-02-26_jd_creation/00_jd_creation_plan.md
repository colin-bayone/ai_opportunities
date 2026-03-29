# Job Description Creation Plan - Sephora ML/Data Engineering Roles

**Session:** 2026-02-26
**Client:** Sephora (never named in JDs)
**Hiring Manager:** Ravi
**Source Material:**
- `sephora/ravi/ravi-ml-jd.txt` - Ravi's original JD (California-focused, generic in places)
- `sephora/ravi/job_descriptions/jd_ai_engineer_sephora.md` - Our AI Engineer JD (base template)

---

## Overview

Ravi provided a Senior ML Engineer JD that contains two distinct technical tracks blended together:

1. **ML/MLOps Track** - Building, deploying, and optimizing ML models in production
2. **Data Engineering Track** - Data pipelines, ETL, distributed systems, databases

These tracks have significant overlap but also deep specialization. Rather than seeking a "unicorn" who has everything, we will create three targeted JDs:

| JD | Primary Focus | Secondary Focus | Purpose |
|----|---------------|-----------------|---------|
| 1. ML Engineer | ML/MLOps (75%) | Light data engineering (25%) | Core ML talent |
| 2. Data Engineer | Data Engineering (75%) | MLOps context (25%) | Data infrastructure talent |
| 3. Senior ML/Data Engineer | Full stack ML + Data | Comprehensive | Unicorn hire if found |

---

## Workflow Requirements

### Golden Rules
1. **Never edit original files** - All originals remain untouched
2. **Use CP to create working copies** - New files only
3. **Stage all changes for approval** - Nothing goes into JDs without explicit approval
4. **Separate staging files per JD:**
   - `jd_ml_engineer_additions.md` - Proposed additions for ML Engineer JD
   - `jd_ml_engineer_removals.md` - Proposed removals for ML Engineer JD
   - `jd_data_engineer_additions.md` - Proposed additions for Data Engineer JD
   - `jd_data_engineer_removals.md` - Proposed removals for Data Engineer JD
   - `jd_senior_ml_data_engineer_additions.md` - Proposed additions for Unicorn JD
   - `jd_senior_ml_data_engineer_removals.md` - Proposed removals for Unicorn JD

### File Naming Convention
All new JDs will be created in: `sephora/ravi/job_descriptions/`
- `jd_ml_engineer_sephora.md` / `.html`
- `jd_data_engineer_sephora.md` / `.html`
- `jd_senior_ml_data_engineer_sephora.md` / `.html`

### Staging Location
All staging/change files will be created in: `claude/2026-02-26_sephora-hiring/staging/`

---

## Technical Requirements by JD

### JD 1: ML Engineer (ML-focused, light data engineering)

**Primary Technical Requirements (ML/MLOps Track):**
- Python as primary language (Java, C++, Scala acceptable)
- Deep learning frameworks: PyTorch, TensorFlow, Keras
- ML model development, training, validation
- ML deployment and productionization
- Model optimization (ONNX, TF Serving)
- Azure ML, Azure cloud platform (NO AWS mentions)
- MLOps practices: CI/CD for ML, model monitoring, A/B testing
- Feature stores
- LLMs and LLMOps (open source)
- End-to-end ML system ownership

**Secondary Technical Requirements (Light Data Engineering):**
- Familiarity with databases (SQL, NoSQL) - not deep expertise
- Understanding of data pipeline concepts
- Spark and Hadoop as "nice to have" not required
- Basic distributed systems understanding

**Soft Skills (from our template + Ravi's):**
- End-to-end ownership mentality
- Hands-on, boots-on-ground work ethic
- Strong communication (technical and non-technical audiences)
- Proactive, self-directed
- Fast-paced environment comfort
- Collaborative with Product, Engineering, Data Science, Business teams

**Experience Level:**
- 2+ years ML systems in production
- 5+ years software engineering
- Python proficiency required

---

### JD 2: Data Engineer (Data engineering-focused, MLOps context)

**Primary Technical Requirements (Data Engineering Track):**
- Python, Scala (Java acceptable)
- Hadoop ecosystem
- Apache Spark
- Kafka
- Data pipelines and ETL
- Workflow management tools
- Databricks
- Kubernetes
- Databases: SQL (various), NoSQL
- Distributed systems and service-oriented architectures
- API design
- Azure cloud platform (NO AWS mentions)
- Azure HDInsights, Analytics Platform System

**Secondary Technical Requirements (MLOps Context):**
- Understanding of ML pipeline concepts
- Familiarity with feature stores
- Basic understanding of model deployment
- Data preparation for ML systems
- Monitoring and logging for ML systems

**Soft Skills:**
- Same as ML Engineer

**Experience Level:**
- 5+ years software/data engineering
- 2+ years data pipeline/ETL work
- Cloud platform experience (Azure)

---

### JD 3: Senior ML/Data Engineer (Unicorn - Comprehensive)

**Full Technical Requirements (Everything):**

*ML/MLOps:*
- Deep learning frameworks: PyTorch, TensorFlow, Keras
- ML model development, training, validation, deployment
- Model optimization: ONNX, MLEAP, TF Serving
- Azure ML
- MLOps: CI/CD for ML, monitoring, A/B testing, automated testing
- Feature stores (build and operationalize)
- LLMs and LLMOps
- Real-time and batch ML systems

*Data Engineering:*
- Hadoop, Spark, Hive, MapReduce
- Kafka
- Databricks
- Data pipelines and workflow management
- ETL processes
- Databases: SQL, NoSQL, Azure SQL Server

*Infrastructure:*
- Azure cloud (comprehensive): HDInsights, APS, Azure Management Portal, Azure ML, Azure SQL
- Kubernetes
- Distributed systems
- Service-oriented architectures
- API design (including API Graph)

*Languages:*
- Python (required)
- Scala, Java, C++ (strong plus)
- R (nice to have)

**Experience Level:**
- 5+ years software engineering
- 3+ years ML systems in production
- 2+ years data engineering
- Demonstrated end-to-end ownership

**Title Consideration:**
- "Senior ML/Data Engineer" or "Staff ML Engineer" or "ML Platform Engineer"

---

## What to Borrow from Ravi's JD

### Tone/Language Elements
- "Technology-agnostic polymath" concept (adapt for our voice)
- "Lifelong journey of learning and exploration" attitude
- "Hands-on technical role"
- "End-to-end" emphasis (appears multiple times)
- "Operationalize" and "productionalize" terminology
- Collaboration emphasis: Product, Engineering, Data Scientists, Business

### Exciting Initiatives (adapt generically - NO Sephora mention)
- Generative AI use cases for product discovery
- Personalized recommendation engines (in-store and online)
- Customer segmentation
- Next-best offer prediction

### Specific Technical Items to Include
- Batch and real-time algorithms
- Monitoring, logging, automated testing, performance testing, A/B testing
- Scalable, efficient, automated processes
- Code review practices
- Iterative, continual-release environment

---

## What to Keep from Our AI Engineer JD

### Structure
- Position Overview (two paragraphs)
- Key Responsibilities with percentages
- Required Qualifications with subheadings
- Preferred Qualifications
- Application Process
- About BayOne Solutions

### Tone Elements
- "Elite, fast-paced team"
- "Lives and breathes" passion language
- Proactive ownership emphasis
- "Doesn't wait for direction"
- Strong communication emphasis

### Generic Elements
- Fortune 500 company framing
- Remote (Offshore) positioning
- BayOne branding and boilerplate
- Equal Opportunity Employer statement

---

## What to Remove from Our AI Engineer JD (for these new roles)

- AI pair programming tool focus (Claude Code, Cursor, GitHub Copilot)
- Claude Code skills, agents, sub-agents
- Claude Agent SDK
- "AI-Assisted Development & Tooling" responsibility bucket
- Prompt engineering emphasis
- AI tooling landscape evaluation

These are specific to the AI Engineer role for the other Sephora team. The ML/Data roles have different technical focus.

---

## Execution Order

### Phase 1: Analysis & Staging
1. ✅ Read Ravi's JD
2. ✅ Create this plan document
3. Create staging folder structure
4. Create analysis document comparing Ravi's JD to ours (language, tone, gaps)

### Phase 2: ML Engineer JD
1. CP `jd_ai_engineer_sephora.md` → `jd_ml_engineer_sephora.md`
2. Create `jd_ml_engineer_additions.md` with proposed additions
3. Create `jd_ml_engineer_removals.md` with proposed removals
4. **AWAIT APPROVAL**
5. Apply approved changes
6. Create HTML version

### Phase 3: Data Engineer JD
1. CP `jd_ai_engineer_sephora.md` → `jd_data_engineer_sephora.md`
2. Create `jd_data_engineer_additions.md` with proposed additions
3. Create `jd_data_engineer_removals.md` with proposed removals
4. **AWAIT APPROVAL**
5. Apply approved changes
6. Create HTML version

### Phase 4: Senior ML/Data Engineer JD (Unicorn)
1. CP `jd_ai_engineer_sephora.md` → `jd_senior_ml_data_engineer_sephora.md`
2. Create `jd_senior_ml_data_engineer_additions.md` with proposed additions
3. Create `jd_senior_ml_data_engineer_removals.md` with proposed removals
4. **AWAIT APPROVAL**
5. Apply approved changes
6. Create HTML version

### Phase 5: Final Review
1. Review all three JDs for consistency
2. Ensure no Sephora mentions
3. Ensure no AWS mentions
4. Verify Azure-only cloud references
5. Final approval

---

## Open Questions for Colin

1. **Title for JD 3:** "Senior ML/Data Engineer" vs "Staff ML Engineer" vs "ML Platform Engineer"?
2. **Experience levels:** Are the years I've outlined appropriate, or adjust?
3. **Ravi's "exciting initiatives":** Include generic versions of these in Position Overview, or keep it more abstract?
4. **Degree requirement:** Ravi mentions "University or advanced degree" - include this or keep experience-focused?

---

## Files Created This Session

| File | Location | Purpose |
|------|----------|---------|
| `00_jd_creation_plan.md` | `claude/2026-02-26_sephora-hiring/` | This planning document |

---

*Last Updated: 2026-02-26*
