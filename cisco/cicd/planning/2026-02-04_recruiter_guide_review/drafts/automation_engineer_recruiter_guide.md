# Recruiter Guide: Automation Engineer

**On-site San Jose, CA | Client-facing | CI/CD + Integration Focus**

---

**Helpful for pre-screening:** If your screening call is on Teams, please enable transcription and share the transcript afterward. This helps our technical team review candidates more effectively. Not required, but appreciated!

---

## Must-Have Skills

| Skill | What This Means |
|-------|-----------------|
| **4+ years software engineering, 3+ years CI/CD** | Has built pipelines and automation, not just used them as a developer |
| **Apache Airflow experience** | Airflow is a workflow tool that schedules and runs tasks in sequence. They should have built workflows ("DAGs") in it, not just used dashboards |
| **Jenkins experience** | Jenkins runs automated builds and tests. They should have configured pipelines or built integrations with it, not just clicked "run" |
| **Python backend development** | Comfortable building APIs, data pipelines, and backend services in Python |
| **SQL and database skills** | Can design database tables, write complex queries, work with PostgreSQL |
| **Integration experience** | Has connected multiple systems together - pulling data from one, transforming it, pushing to another |
| **Strong communicator** | Clear writing, comfortable explaining technical systems to others |

## Nice-to-Have Background

| Skill | What This Means |
|-------|-----------------|
| **Bazel or similar build tools** | Bazel is a build system used at large companies. Also: Gradle, Buck, Pants |
| **Grafana dashboards** | Built monitoring dashboards to visualize system health |
| **GitHub APIs / webhooks** | Automated things based on GitHub events (PRs, commits, etc.) |
| **On-prem deployment** | Deployed systems in corporate data centers, not just cloud services |
| **Platform engineering background** | Worked on internal tools that help other developers be more productive |
| **Working with legacy systems** | Comfortable integrating with old, poorly-documented systems |

## Strong Signals

- Built integrations between multiple CI/CD systems (not just used one tool)
- Has worked on "developer productivity" or "platform engineering" teams
- Experience at companies with 100+ engineers (enough scale to have real CI/CD complexity)
- Comfortable with incomplete documentation - can figure things out
- Uses AI coding tools daily (Claude Code, Cursor, Copilot)
- Has debugged issues that span multiple systems

## Warning Signs

- Only used CI/CD as a developer (ran pipelines) but never built or configured them
- Can't explain what Airflow does or when you'd use it vs other tools
- Only worked in brand-new ("greenfield") environments - no legacy integration experience
- Uncomfortable when things aren't well documented
- Vague about what they personally built vs what the team built
- No experience working with people outside their immediate team

## Screening Questions

### "Describe an Airflow DAG you built. What did it do and why did you choose Airflow?"

**Weak answer:** Can't describe a specific DAG. Gives vague answers like "it ran some jobs." Doesn't know why Airflow was chosen vs other options.

**Good answer:** Describes a specific workflow with details - what tasks ran, in what order, what happened if something failed. Can explain why Airflow made sense for that use case (scheduling, dependencies, retries, etc.).

---

### "Tell me about a time you had to integrate with a system that had poor documentation. How did you figure it out?"

**Weak answer:** Can't recall a specific situation. Or says they just asked someone else to do it. Or got frustrated and gave up.

**Good answer:** Tells a specific story - how they explored the system (reading code, testing APIs, tracing logs), what they tried that didn't work, how they eventually figured it out. Shows persistence and problem-solving.

---

### "What's the difference between Airflow and Jenkins? When would you use each?"

**Weak answer:** Can't explain the difference, or thinks they're the same thing. Gives a textbook definition without real understanding.

**Good answer:** Explains that Jenkins is for CI/CD (build/test/deploy triggered by code changes) while Airflow is for scheduled workflows and data pipelines (time-based or dependency-based). Can give examples of when each makes sense.

---

### "Tell me about a time you had to debug an issue that involved multiple systems. How did you track down the problem?"

**Weak answer:** Can't recall a specific situation. Or just says "I looked at the logs."

**Good answer:** Walks through a specific debugging journey - which systems were involved, how they narrowed down where the problem was, what tools they used (logs, metrics, tracing), how they confirmed the fix worked.

---

### "Can you explain [most complex thing on their resume] to me like I'm not technical?"

**Weak answer:** Uses jargon, gets frustrated, or can't simplify it.

**Good answer:** Uses plain language and analogies. Checks if you're following. Patient and clear. (You can evaluate this directly.)

---

## LinkedIn Search Strings

### Layer 1 — Narrow (Start Here)

```
("Airflow" OR "Apache Airflow") AND ("Jenkins") AND Python AND (built OR developed OR integration)
```

### Layer 2 — Broader (If Layer 1 is too narrow)

```
("Platform Engineer" OR "DevOps Engineer" OR "Build Engineer" OR "CI/CD Engineer" OR "Release Engineer") AND Python AND (Airflow OR Jenkins OR "pipeline")
```

### Layer 3 — Widest Net

```
("software engineer" OR "backend engineer") AND Python AND ("CI/CD" OR "automation" OR "pipeline" OR "Jenkins" OR "Airflow") AND (integration OR built OR developed)
```

### Communication Filter (Add to any layer)

```
AND (consulting OR "client-facing" OR stakeholder OR "cross-functional")
```

## Synonym Groups

Use OR between these in searches - they're related tools or mean similar things:

**Workflow Orchestration:**
`(Airflow OR "Apache Airflow" OR Prefect OR Dagster OR Luigi OR "Argo Workflows" OR Temporal)`

**CI/CD Systems:**
`(Jenkins OR "GitHub Actions" OR "GitLab CI" OR CircleCI OR BuildKite OR TravisCI)`

**Build Systems:**
`(Bazel OR Gradle OR Buck OR Pants OR Make OR "build system")`

**Database:**
`(PostgreSQL OR Postgres OR MySQL OR "SQL Server")`

## Tech Stack Keywords

**Must-Have (Search for these):**
- Python
- Airflow / Apache Airflow
- Jenkins
- CI/CD
- PostgreSQL
- API integration
- data pipeline

**Nice-to-Have (Bonus points):**
- Bazel
- Grafana
- GitHub Actions
- Docker
- Kubernetes
- ETL
- monitoring
- observability

## What to Look for in Work History

| Look For | Why It Matters |
|----------|---------------|
| **Company size 100+ employees** | Smaller companies often don't have complex CI/CD - not enough scale |
| **Built automation, not just used it** | Many developers use CI/CD but never configured or built pipelines |
| **Integration or platform team experience** | Shows they've connected systems, not just worked in one silo |
| **Experience with messy/legacy systems** | Our client has mature enterprise systems - not everything is new and clean |
| **Some client or stakeholder interaction** | This role is 15% client-facing - they need to communicate with external teams |
