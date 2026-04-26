# 12 - Meeting: Build Log Architecture Proposal (As Presented to Srinivas)

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-13/day_2026-04-17/srinivas-and-team_4-17-2026_formatted.txt
**Source Date:** 2026-04-17 (Friday afternoon Srinivas meeting)
**Document Set:** 12 (Third Srinivas team meeting)
**Pass:** Focused deep dive on BayOne's proposed build log architecture (pre-redirect)

---

## Overview

This decomposition captures the second major agenda item of the 2026-04-17 Srinivas team meeting: the build log analysis and triage architecture that Namita presented on behalf of the BayOne team. The presentation was the culmination of the architecture work developed across Set 02a, 02b, and 02c (Namita's build log analysis investigations), Set 03_sync and Set 04_sync (team architecture syncs), and Set 04e (Namita's proposed architecture). Set 05 prep staged the slide-by-slide delivery, with specific revisions including the removal of summarization from the B2 parse block, the addition of the cycle arrow on B4, an Airflow defense, and a star-schema positioning posture. The material documented below represents what BayOne brought into the room; Srinivas's sharp pivot to a knowledge graph requirement at the tail end is captured in a separate decomposition file (`12_meeting_knowledge_graph_redirect_2026-04-17.md`).

The architecture presentation was materially compromised by WebEx screen-sharing instability. Namita's share failed multiple times, Colin's share failed as well, and the team ultimately resorted to sending the architecture image to Srinivas so that he could share it from his end. The disruption ate into the wall clock and pressured the team to compress the architectural walkthrough, which meant that several intended talking points (Airflow orchestration rationale, star-schema data model posture) did not get full air time during the live delivery.

## Set-up and Existing Automation Context

Namita opened the architecture section by framing the week's investigation. She noted that the BayOne team had "spent this past week inside the build system understanding and getting hands-on experience with the access logs using the temp ADS machine." She credited Justin directly, noting that they had "very useful calls and productive calls with Justin who understand the current Python pipeline." This framing was important because it positioned the proposed architecture not as a greenfield design exercise but as a targeted response to limitations Namita had observed in the pipeline Justin was already operating.

Before Namita could advance to the architecture diagram, Justin surfaced a clarifying question that anchored the entire discussion: "what do you mean when you say existing automation, any augmentation we need to do here?" Justin then described his own in-flight work, explaining that he was "working on triage" and that build errors produce "pretty big logs right now." He was working on "simplifying them to just get the errors, basically, and then providing context like, hey, you should fix different errors, then trying that out." Justin noted that for compile errors "the tool is pretty good at fixing those compile issues in the code," but that his pipeline was not yet deployed.

This exchange effectively established the baseline. The existing pipeline is a Python-based log analysis tool that extracts errors, calls an LLM with limited context, and emits suggestions. It is not yet in production. BayOne's proposed architecture is intended to both subsume and extend this work.

## Limitations of the Existing Pipeline

Namita's review of the Python pipeline surfaced three limitations, which she presented as the motivating problem set for the new architecture.

The first limitation was coverage. Namita explained that "it captures only a subset of errors. The file selection is based on the modification type and the backward scan. So it misses context that is available in the logs." In other words, the heuristic that picks which files to inspect systematically excludes material that could inform the diagnosis.

The second limitation was persistence. Namita observed that "every analysis result is written to the temp workstation. But let us say we want to review it after a few days to see which errors occurred and which ones did we solve and which fix did we apply. So that we are not able to gain. So we would like to store it in our current work." The current pipeline is effectively stateless with respect to the history of analysis results; there is no durable store that would let the team revisit past failures and learn from them.

The third limitation was traceability. Namita noted that there is "no traceability. LLM suggests a fix and the fix gets applied, and there is no record connecting that fixed back to that particular or specific error that caused it. So we cannot audit the system or learn from it over time." This is the audit-trail gap: suggestions and fixes enter the workflow without a durable link back to the originating error signal, which forecloses any data-driven improvement of the system.

Namita also flagged an additional concern that sits adjacent to those three limitations. She noted that "even when the LLM is being called, I believe it is with [limited] context. So then the data or the system actually has [limited information]." The exact phrasing here is unclear in transcript, but the point is that the LLM's inputs are impoverished, which degrades the quality of its output regardless of the model's capabilities.

## The "Simple First" Principle

Before walking into the architecture diagram, Namita articulated the governing principle for the design. She stated: "keep in mind that always keep the things simple first. So every design decision in the system is about doing the cheapest things that works and only escalating when it is really necessary so that we can cut down on cost." This is the principle Colin had been coaching toward throughout the Set 07 and Set 08 sessions, and Namita delivered it as the design philosophy that structures every downstream choice in the pipeline.

The "simple first" principle has two operational implications that thread through the architecture. First, it justifies starting with deterministic, cheap classifiers (regex, structural parsing, lookup tables) before reaching for ML models, and reaching for ML models before reaching for LLMs. Second, it justifies batch-scheduled ingestion before event-driven ingestion, structured chunking before semantic summarization, and persisted records before exotic storage models. In every component, the principle directs the team to pick the simplest thing that works and to escalate only when measured behavior demands it.

## Ingestion Component (B1)

The first architecture block, labeled B1 in the Set 05 prep, is the ingestion layer. Namita described it as the component that "will start by reading the logs." The logs themselves live on an NFS (Network File System) path, while the accompanying metadata (build number, timestamp, and build status of pass or fail) lives in a MySQL database. She clarified that there are "two NFS locations specifically for CV and CI," referring to the continuous delivery and continuous integration build products respectively.

The initial scope targets Bazel logs only, which was confirmed in prior sets and restated here. The ingestion mode is scheduled batch: "the ingestion happens in a scheduled batch manner around every 15 to 30 minutes so that we can help which helps us, helps it to keep it simpler as well as predictable." Namita explicitly flagged the future evolution path: "in future we can move towards event based triggering." The choice to start with polling rather than events is a direct application of the "simple first" principle; scheduled batch reads are trivial to implement, trivial to monitor, and bounded in their failure modes.

The output of the ingestion component is a structured record. Namita described it as capturing "which logs files were found, what were their paths and so on," combined with the metadata pulled from MySQL. This structured record becomes the input to the parse component.

## Parse Component (B2)

The second architecture block, B2, is the parse component. This block was materially revised in the Set 05 prep: the earlier conception included a summarization step, which was removed because summarization requires LLM spend and therefore violates the classification cascade by forcing expensive inference before the deterministic tiers have had a chance to route the work.

Namita described B2's function simply: "once the logs are ingested, this parse component will break them into manageable pieces, into various chunks." She gave a concrete magnitude: Bazel builds produce "a lot of files, like around 40 or more individual files per build." These files are huge, and "a single language model cannot handle such huge files."

The chunking output format was articulated as a set of JSON objects. Namita described creating "a JSON object with the file, the error, the column number, error code, and so on. So anything that failed, only the failed error record, right? Not everything." The key shift here is that the parse component is not a semantic transformer. It is a structural extractor that produces records corresponding to failed or error lines. No summarization. No embedding. No LLM calls. The output is a deterministic, structured representation of the error content extracted from the raw build log.

## File Size Context from Justin

Justin provided important clarifying detail on the actual size and format of the logs being ingested. When Colin asked about the full build log size, Justin responded: "I have seen around 50 MB as well." He distinguished between the full console output and the individual error logs: "just passing the full log, that is like a console output, full log, right? And the individual dead logs are there as well, which need to be looked at for any failure. There could be multiple error logs."

Justin also clarified the CI behavior: "For the CI builds, the logs will always get copied over, whether it is a pass or fail. But the logs format should be the same for both." This means that the pipeline can rely on a consistent file layout regardless of build outcome, which simplifies the ingestion contract. Justin further distinguished between the full build log and the pruned error log: "we create a pruned error log file that should show up. The relevant errors so that that is in the senior building as well as the skinny build. So those are much smaller." The pruned error log is the more focused artifact that the classifier tiers are expected to operate on.

Justin cited a concrete example: a successful PI build had "600 make all the some all the bill dogs [build logs] combined." This provides a directional size reference for dimensioning the pipeline's throughput expectations.

## Srinivas's Skeptical Questions on Chunking Basis

Srinivas pressed the team on the chunking logic, returning repeatedly to a single core question: what exactly is being chunked, and on what basis. He asked first "What is your data input? What is your data input here?" and then, after clarification, pressed further: "I still did not get the input like that." When Namita indicated that the input is the build log, Srinivas asked pointedly: "is it the console log adjusting or is it the backend log?"

The clarifying answer from the team was that the input is the full build log, which Srinivas quantified for himself at "300 to 500 k lines." He then returned to the chunking question directly: "when you say chunk, what does that mean? I want to understand."

Namita's response, reinforced by Colin, was that the chunking is structural rather than size-based: "there is some structure to those files. Those files are not random. So the chunking would be based on those structures." Colin elaborated: "it is saying that based on the content within some demarcation within that file that is predictable based upon the logs that we have seen so far, we can now separate this out into individual subcomponents of that log." Justin also confirmed the team's intent in his own words: "chunking means to separate it out into its individual components so that those themselves can be classified."

Srinivas did not appear fully satisfied by the verbal explanation. The team deferred a concrete example: Colin committed that "Nimida [Namita] already had that. So we can present that to you on Monday. So you can see exactly how we would split it up." The chunking exemplar is one of the Monday deliverables the team now owes.

## Three-Tier Classification Cascade

After the parse component feeds structured error records downstream, the classification cascade takes over. Namita pointed to the diagram and described three tiers: Tier 1 (visible in purple), Tier 2 (intermediate), and Tier 3 (LLM as last resort). The cascade embodies the "simple first" principle: the cheapest classifier runs first, and only records it cannot handle are escalated.

Per the Set 05 prep, Tier 1 is regex and lookup-based deterministic classification, Tier 2 is lightweight ML or NLP techniques, and Tier 3 is the LLM. The intent is to push as much volume as possible toward Tier 1, where marginal cost per classification is effectively zero. The Set 05 prep specifically added a cycle arrow on the B4 block, intended to visually convey the feedback loop: as the system accumulates classified records and validated fixes, it should feed that labeled data back into Tier 1's deterministic rules (or a Tier 2 model), migrating volume away from Tier 3 over time.

Srinivas's question "what is your data input here?" was asked specifically at this junction, confirming that the chunked error records produced by B2 are the inputs to Tier 1. The tier boundary is therefore: parse produces JSON error records, Tier 1 attempts deterministic classification, and the cascade escalates only the residue that deterministic methods cannot handle.

## Proposed Architecture Principles

The architecture as framed to Srinivas rested on four principles beyond "simple first." The first is a clean pipeline separation: ingestion, then parse, then classification cascade, then action. Each stage has a well-defined input and output, which makes the system inspectable and testable.

The second principle is modularity. Each tier in the classification cascade is swappable, which means the team can upgrade Tier 2 (for example, swap a simple NLP classifier for a transformer-based classifier) without reworking B1, B2, or the Tier 3 LLM integration.

The third principle is observability. One of the explicit responses to the "no persistence" limitation in the existing pipeline is to store analysis results durably. This is what makes "review it after a few days to see which errors occurred and which ones did we solve" feasible.

The fourth principle is traceability. The durable store connects each LLM suggestion back to the source error, the source build, and (ideally) the resulting fix outcome. This is the audit trail that was missing from the existing pipeline, and it is also the substrate that enables the feedback loop on B4.

A secondary principle is reusability. Colin stated earlier in the meeting that "whatever we do here will be repeatable too because I am sure this can be transferred and I am sure we would want to do it more than just one time as well. So we will make sure that anything we do is it would be reused. We will build a system like that." The architecture is intended to be a chassis, not a single-shot build.

## Architecture Presentation Interruptions

The live delivery of the architecture diagram was repeatedly interrupted by WebEx screen-sharing failures. At one point Namita said directly: "You are not sharing, sorry. Keep suddenly shutting me off. Can you see that?" Colin attempted to take over screen sharing and encountered the same failure. After multiple attempts, Colin proposed a recovery: "here is what I am going to do. Let me send you the picture. And why do you not share this on your screen? I do not know what is going on with mine. They will at least get us through this. This is an important one. I do not want to keep interrupting you."

Srinivas accommodated the delay with a time-boxed commitment: "I can spend a few more minutes. Let us finish this." The effect, however, was that the team lost several minutes of substantive time and had to compress the walkthrough. Topics that had been fully prepped (notably the Airflow orchestration rationale and the star-schema data model posture) did not receive the air time they were scheduled for in the Set 05 prep.

## Airflow Orchestration Wrapper

Per the Set 05 prep, Airflow was defended as the orchestration wrapper for the pipeline. The rationale is that Cisco is already running Airflow, which means using it lowers the cost of integration and operational hand-off to Cisco's own teams. In practice, the Airflow detail did not come up during the meeting; the screen-sharing failures and the compressed wall clock ate the airtime that would have hosted this discussion. The topic is carried forward to the Monday session.

## Data Model and Star Schema Posture

Per the Set 05 prep, the star schema data model was positioned as a "non-die-on-hill" item, meaning the team had a preferred design but was willing to accept Cisco's direction rather than defend the schema aggressively. As with Airflow, the data model discussion did not come up during the live meeting due to the compressed time. It is also carried forward.

## Knowledge Graph Redirect Trigger

At the tail end of Namita's architecture walkthrough, immediately after the chunking logic exchange, Srinivas pivoted sharply: "Okay, let us actually I want to understand a little bit this, but the key thing here, right, we need to create some kind of a knowledge graph." He then extended the point: "Without a knowledge graph you go to AI you get junk and this project will be another year project."

Namita and Colin accepted the redirect without pushback and committed to presenting a knowledge graph treatment on Monday. The full substance of the redirect (the call graph analogy, the "what to build" reference, the dependency tree rationale, the explicit criticism of "jumping to chunking") is captured in the separate decomposition file `12_meeting_knowledge_graph_redirect_2026-04-17.md`. For the purposes of this decomposition, the redirect functions as the terminating event of the build log architecture presentation: Srinivas effectively rerouted the conversation away from the pipeline Namita had designed and toward an upstream structural artifact (the knowledge graph) that he considers a prerequisite.

## Summary

What BayOne brought into the 2026-04-17 meeting was a coherent, principled build log analysis architecture. Namita's framing was grounded in concrete limitations of the existing Python pipeline (coverage, persistence, traceability), governed by an explicit "simple first" design principle, and structured as a clean ingestion-parse-cascade-action pipeline. The proposed pipeline ingests Bazel logs and MySQL metadata on a 15 to 30 minute schedule, parses logs into JSON error records without summarization, and routes those records through a three-tier classification cascade that escalates to LLMs only as a last resort. Observability, traceability, modularity, and reusability round out the framing.

The live delivery was compromised by WebEx failures and compressed by time pressure, leaving several prepped topics (Airflow, star schema) undiscussed. The core of the architecture did reach Srinivas, and he pressed appropriately on the chunking basis and the data input definition. His ultimate redirect to a knowledge graph requirement reset the design conversation and is handled in a separate decomposition document. What this document captures is the architecture BayOne presented, which stands on its own as the baseline against which the Monday follow-up and any future Cisco-directed revisions will be measured.
