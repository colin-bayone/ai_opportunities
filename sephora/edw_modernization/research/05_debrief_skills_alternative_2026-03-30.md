# 05 - Debrief: Skills-Based Alternative

**Source:** /sephora/edw_modernization/source/saurav_colin_3302026.txt
**Source Date:** 2026-03-30 (Internal Debrief)
**Document Set:** 05 (Saurav/Colin Debrief)
**Pass:** Focused deep dive on the Claude Code skills alternative and strategic positioning

---

## 1. What Saurav Built

Saurav revealed during the debrief that in addition to the full LangGraph-based agent architecture with its Streamlit front end, he built a parallel implementation of the same EDW migration pipeline using Claude Code skills and the Anthropic API directly. He described it as living on a separate git branch ("Azure land chain or land or something" — the exact branch name was unclear in the transcript, line 691).

The skills-based version performs the same end-to-end workflow as the full architecture: it takes source and target DDL files, runs the migration pipeline (parsing, schema mapping, deterministic validation gates, SQL generation), and produces the same outputs including warnings and confidence scores. Saurav demonstrated that the last run produced a 9.6 (presumably a confidence or quality score comparable to the architecture version's output) along with the same type of warnings the architecture generates (lines 718-719).

**Key statement (lines 703-706):** "We have this here as a skill support AW and we have like the same workflow which we are doing over there. There in the whole migration pipeline, the same things we can do with the skills as well and I've tried it."

The implementation uses a single Claude Code skill that encodes the migration workflow. The skill performs deterministic checks and orchestrates the pipeline steps, but instead of using LangGraph's agent orchestration layer, it relies on the Anthropic API called through Claude Code's skill execution model.

---

## 2. Performance Comparison: Skills vs. Architecture

Saurav provided a direct comparison on three metrics, all favoring the skills version.

**Key statement (lines 704-706):** "It takes like what you call lesser total number of API calls in total, plus like the time itself is also low plus the token cost is also [lower] than like our agent orchestration."

| Metric | Skills Version | Architecture Version |
|---|---|---|
| Total API calls | Fewer | More (multi-agent orchestration overhead) |
| Execution time | Faster | Slower |
| Token cost | Lower | Higher |
| Accuracy | ~95% (Colin's characterization, line 744) | Higher (with retry loops) |

The performance advantages are structural: the skills version avoids the overhead inherent in multi-agent orchestration. Each agent in the architecture version requires its own API calls for reasoning, coordination, and state management. The skills version collapses that into a more direct pipeline with fewer round-trips.

Colin later quantified the accuracy gap when framing the strategic positioning: "Skills around, you know, 95%" (line 744). The architecture version achieves higher accuracy specifically because of its self-correcting retry loop, which the skills version lacks.

---

## 3. The Self-Correcting Loop Limitation

This is the critical technical gap between the two implementations and the primary reason Colin biases toward the architecture solution.

Saurav explained the limitation in detail. In the full architecture, when deterministic validation gates fail (for example, a column mapping check fails or a SQL syntax validation does not pass), the LangGraph orchestrator loops back and retries — regenerating the failing output until the deterministic checks pass. This is the "Flanders loop" they joked about (lines 659-665): "Just go again, again, again, again until it's right."

The skills version has no such mechanism.

**Key statement (lines 753-760):** "If suppose the files itself changes by a lot and these deterministic gates start failing, then there is no wrap loop which can go ahead and salvage that situation. It will always like be out of bounds for most of the time. So it does not have like self correcting actions on itself."

Saurav elaborated further at lines 765-771: "This is something if we want to do similar in airflow also. So we can create the same kind of like orchestration and it will run like similarly all the time, but it does not have that option of like if anything major goes wrong it can loop back and get a correct solution out."

The practical implication: the skills version works reliably when the input files conform to expected patterns. When inputs deviate significantly — unusual DDL structures, unexpected naming conventions, edge cases in the source schemas — the deterministic validation gates will flag failures, but the system cannot recover on its own. A human would need to intervene, adjust the input, or manually correct the output. The architecture version handles these edge cases autonomously through iterative refinement.

This is the difference between 95% accuracy and higher: the architecture's retry loops catch and fix the remaining 5% of cases where the first-pass generation does not satisfy the deterministic validation criteria.

---

## 4. No Distributed or Parallel Processing

Colin identified a second structural limitation: the skills version cannot perform distributed or parallel processing the way the architecture can.

**Key statement (lines 743-744):** "The problem with this skill as well is that, you know, you can't do this in a giant distributed way. We are using a wink wink for that because I think you could figure out [a way to do that]."

The architecture version, built on LangGraph with fan-out patterns, can process multiple schemas, tables, or migration units in parallel. Saurav confirmed this in the demo walkthrough — the fan-out step is deterministic and fast (line 361). The skills version processes sequentially, which means that while it is faster per individual unit (fewer API calls, less overhead), it cannot scale horizontally across many migration units simultaneously.

For Sephora's use case — potentially thousands of reports and hundreds of tables — parallel processing is not optional. The architecture's ability to fan out across multiple agents working concurrently is a production requirement, not a nice-to-have.

Colin acknowledged that Saurav could probably figure out a way to add parallelism to the skills version ("I think you could figure out way to do that"), but this was stated as a theoretical possibility, not a planned effort.

---

## 5. IP Exposure: Skills as Readable Markdown

Colin raised a business risk that does not exist with the architecture solution.

**Key statement (lines 729-730):** "Skills are tough because the fact that skills are plainly readable markdown files."

Claude Code skills are stored as markdown files in a project's directory structure. Anyone with access to the project — including the client — can open and read the full content of every skill. This means that the migration methodology, the deterministic validation logic, the prompt engineering, and the workflow orchestration encoded in the skill are all exposed as plain text.

For the architecture version, the logic lives in Python code (LangGraph graphs, agent definitions, validation functions) deployed on infrastructure that BayOne controls. The client interacts with it through a front end; they do not see the internal implementation.

**The IP concern:** If BayOne delivers the skills version to Sephora, Sephora's developers could read the skills, understand the methodology, and replicate it without BayOne. The architecture version protects BayOne's intellectual property by keeping the implementation behind a deployment boundary.

This is a consulting engagement risk, not a technical limitation. The skills work. But delivering them hands the client the recipe, not just the meal.

---

## 6. The Self-Updating Skills Concept (Deferred)

Saurav raised a forward-looking possibility inspired by OpenClaude (an open-source project where Claude Code agents update their own context files).

**Key statement (lines 777-783):** "Something like which OpenClaude did that it just goes ahead and automatically updates its own context or its own files. We can do something similar to the skill sets here that whenever it comes around like a new discovery or any new kind of problem, after solving it, just go add and update that into the skill so it knows how to tackle that next time."

The concept: if the skills version encounters a new edge case and a human resolves it, the skill could automatically update its own instructions to handle that pattern in the future — a form of automated learning at the prompt/instruction level rather than at the model level.

Both Colin and Saurav immediately agreed not to pursue this.

**Key statement (line 787):** Colin: "Not yet. Not yet. Anyway, definitely for that."

This was a technically interesting idea that both recognized as premature. It introduces risks (skills modifying themselves could degrade quality, introduce inconsistencies, or create unpredictable behavior) and complexity that is not justified at the demo stage. It remains a documented possibility for a future phase if the skills approach is ever elevated to a primary delivery mechanism.

---

## 7. Colin's Strategic Positioning Decision

Colin made a clear strategic call: bias toward the architecture solution, keep skills as a documented fallback.

**Key statement (lines 736-738):** "So the IP sensitivity of that, if you think about it, it puts us at a disadvantage with skills. So we actually in a way want to bias people to want the more architectural solution, but just say that the skills are always there if you want to."

His reasoning combined multiple factors:

1. **IP protection** — The architecture keeps BayOne's methodology behind a deployment boundary. Skills expose it as readable text.
2. **Higher accuracy** — The architecture's self-correcting loop produces higher accuracy than the skills version's single-pass approach.
3. **Production scalability** — The architecture supports distributed parallel processing required for Sephora's volume (thousands of reports). Skills do not.
4. **Engagement value** — The architecture is a larger, more complex engagement. It positions BayOne as a solutions partner, not a tools vendor. Colin explicitly framed the engagement earlier in the call (lines 413-414): "This is not a product, this is a solution and we will do this custom for whomever needs it."

The skills version is not being discarded. Colin positioned it as a complementary offering: "Just say that the skills are always there if you want to" (line 738).

---

## 8. How to Position Skills to Sephora

Based on the discussion, the skills version maps to a specific client need: developers who cannot wait for IT to deploy infrastructure.

**The scenario:** Sephora's IT team takes time to provision Azure infrastructure, set up authentication, configure networking, and deploy the full architecture. During that lag — which could be weeks or months — developers are stuck waiting. The skills version gives them something they can use immediately with nothing more than Claude Code and Anthropic API access.

**Key statement from Saurav (lines 724-726):** "If they want like just a wrapper around something so we can also provide them with this kind of skill also and they don't want to go into architecture too much."

The positioning framework:

| | Skills Version | Architecture Version |
|---|---|---|
| **Label** | Developer toolkit / interim solution | Production platform |
| **Audience** | Individual developers during IT provisioning lag | Data engineering team at scale |
| **Deployment** | Claude Code + Anthropic API key | Azure infrastructure (LangGraph, databases, front end) |
| **Time to value** | Immediate | Weeks (infrastructure provisioning) |
| **Accuracy** | ~95% (single-pass) | Higher (self-correcting loops) |
| **Scale** | Sequential, single-user | Parallel, multi-user, distributed |
| **IP risk** | High (readable markdown) | Low (deployed behind front end) |
| **Engagement size** | Smaller (delivery + handoff) | Larger (build + deploy + support) |

This creates two engagement options for Sephora:

1. **Lightweight / fast:** Deliver skills to developers now, let them start migrating immediately with human oversight on the ~5% of cases the single-pass approach does not fully resolve. Lower cost, faster start, but the client owns the methodology.

2. **Production-grade:** Build and deploy the full architecture on Azure with the Streamlit front end, self-correcting loops, parallel processing, run history, and the full dashboard Saurav demonstrated. Higher cost, longer timeline, but BayOne retains IP and the client gets a production system that scales.

Colin's clear preference is option 2, with option 1 available as either a bridge during infrastructure provisioning or a fallback if Sephora's budget or timeline does not support the full architecture.

---

## 9. Technical Details: How the Skills Version Works

Based on what Saurav showed and described, the skills implementation has the following characteristics:

- **Single skill file** — One Claude Code skill (markdown file) that encodes the full migration pipeline workflow
- **Anthropic API direct** — Uses the Anthropic API rather than LangGraph's agent orchestration layer
- **Deterministic checks preserved** — The same validation gates (column mapping verification, SQL syntax validation, confidence scoring) run in the skills version
- **Same output format** — Produces warnings, confidence scores (9.6 shown in the demo), and migration outputs comparable to the architecture version
- **No front end** — Runs in the terminal through Claude Code, not through a Streamlit or HTML dashboard
- **No database** — No run history, no persistent state across runs (unlike the architecture version which stores runs in a database and displays them on the dashboard)
- **No retry mechanism** — If a deterministic gate fails, execution stops or produces a lower-confidence result; there is no automated loop-back

The skills version is essentially the same pipeline logic flattened from a multi-agent orchestration graph into a single-agent sequential workflow with deterministic validation checkpoints. The trade-off is simplicity and speed at the cost of resilience and scale.
