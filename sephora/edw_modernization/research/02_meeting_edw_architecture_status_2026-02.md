# 02 - Meeting: EDW Architecture and Current Status

**Source:** /sephora/edw_modernization/source/mani_transcript2_formatted.txt
**Source Date:** 2026-02 (Colin's First Meeting with Mani)
**Document Set:** 02 (Mani Meeting 2)
**Pass:** Focused deep dive on EDW architecture status and what's established vs open

---

## 1. Critical Framing: Re-engineering, Not Migration

Mani made an emphatic correction at the top of the meeting that defines how this entire effort must be understood. Colin opened with a summary that used the word "migrate," and Mani immediately reframed.

**Key statement (lines 20-22):** "This is not a migration initiative. This is completely re-engineering. That's one thing that we are making very clear, and that's why you are not calling this migration — [it's] modernization."

**Why it matters (lines 23-26):** Migration implies lift-and-shift — moving data or code from one place to another. In this context, the team is re-engineering and rewiring the underlying logic. The back-end systems, queries, data pipelines, and business logic are all being rebuilt, not moved.

**Front-end exception (lines 27-29):** In "most cases," the front-end reporting interface is being retained. If a report runs in Cognos today, it will remain in Cognos — but everything underneath it (the data source, the queries, the pipelines) is rebuilt against the new Databricks platform. There is "a desire to move to ThoughtSpot or Tableau, but that's not something that we are pursuing" actively (line 29). The change management burden of switching end-user interfaces is being deliberately avoided.

---

## 2. What Is Architecturally Complete

Mani was clear that the foundational architectural work is done. The team has spent the prior three months in deep effort to establish patterns that will govern the entire modernization.

### 2a. Architectural Patterns — Established and Final

**Key statement (lines 106-108):** "The architectural factor is not going to change. Those parts are very well established. They'll apply those patterns" to each subsequent category — merchandising, supply chain, stores.

**Key statement (line 72):** "We, at the same time, actually, also have established certain architectural patterns."

The patterns were established through work on the finance track (the first category). These patterns are now considered locked. When subsequent categories are taken on, the team will apply the same patterns — they will not revisit architectural decisions. Mani described this reuse as "really beautiful" (line 111).

### 2b. Target Platform — Decided

**Key statement (lines 74-75):** "We know the target, because target is Databricks. We know the sources."

There is no ambiguity about the target data platform. Databricks is the destination. The source systems (SQL Server, legacy databases feeding Cognos) are also well understood.

### 2c. Roadmap — Done

**Key statement (lines 97-102):** "Roadmap is kind of done. Which category comes first? Which category comes next? Which category comes third? That part has been figured. At the overall modernization level, yes, that is kind of done."

The sequencing of which business categories will be modernized and in what order has been determined. The roadmap covers the full scope of the multi-year effort.

### 2d. The Cross-Functional "Table" — Assembled

**Key statement (lines 118-125):** "We have a table, we have important stakeholders. Databricks has a seat at the table. Microsoft has a seat at the table. Data platform has a seat at the table. They're from different angles and places. This team together, regardless where they come from, this is the core team. This team establishes what's right to do, how to do it."

This is a cross-functional governance body that includes:
- **Databricks** — the target platform vendor
- **Microsoft** — likely due to Azure infrastructure, SQL Server legacy, or both
- **Data platform team** — Sephora's internal data platform organization
- **Data engineering team** — referenced separately (line 380: "people from data engineering team")

This core team makes architectural decisions collectively. Patterns and tool selections are ratified through this group. Mani described "lots of efforts" over "the last 3 months" to get this body functional and aligned (lines 116-117).

### 2e. Finance Category — Fully Scoped

**Key statement (lines 85-87):** "Within finance, we have figured out. Yes, what reports, how many reports, what reports to sunset, what reports have to exactly re-engineer. Those things have been figured out."

For finance specifically, the team has completed:
- Full inventory of reports
- Triage decisions (which reports to sunset vs. re-engineer)
- Scoping of the re-engineering work

---

## 3. Finance Track: First and Nearly Complete

Finance is the first category track taken on, and it is the most advanced.

**Key statement (lines 369-370):** "Finance has already progressed. There's maybe another 20-odd days. So that's kind of like almost done."

This places finance approximately 20 working days from completion as of the meeting date (February 2026). The finance track has served a dual purpose: delivering the first production-ready modernized category, and establishing the reusable architectural patterns for all subsequent categories.

**What "done" means for finance:** The reports inventory is complete, sunset/re-engineer decisions are made, the back-end re-engineering is well advanced, and the patterns emerging from this work are now locked for reuse.

---

## 4. Category Tracks and Roadmap Structure

### Categories Identified

Mani named the following business categories (lines 69-70):
- **Finance** — first track, nearly complete
- **Supply chain** — named as a possible next candidate
- **Merchandising** — named explicitly, "would not come forth yet" (line 88)
- **Stores** — referenced as a pattern application target (line 110)

He indicated "3 to 4 different categories of tracks" (line 68) but also referenced "so many different tracks of categories" — suggesting the major groupings may number more than four when fully enumerated.

### Three Tracks Taken, Three Not Yet Started

**Key statement (lines 103-105):** "They already have another 3 tracks that we have taken, those 3 tracks are also [well along]. Those tracks that we have not taken, so there are three [more] — we don't know what we [will] do. When we come to that, they will again go into the more details."

This gives a picture of 6 total tracks:
- **3 tracks in progress** (including finance as the most advanced)
- **3 tracks not yet started** — these will receive detailed scoping only when the team reaches them in the roadmap sequence

For the untouched tracks, the team has "a general idea" but will not commit to detailed scoping until they come up in sequence. The architectural patterns, however, will transfer directly.

### Next Up After Finance

Mani considered supply chain as a candidate for the next focus (line 373: "Supply chain could be one thing"). Merchandising was also mentioned but characterized as not yet ready to come forward (line 88).

---

## 5. Accelerators Being Evaluated

Mani described multiple accelerators under evaluation, sourced from both Databricks and Databricks partners.

**Key statement (lines 76-82):** "There are accelerators available — some from Databricks, and partners of Databricks have also given certain accelerators. The whole team has to figure out which accelerator is going to be the best fit. Someone is good with respect to [Cognos conversion]. Someone is good with respect to SQL Server, and someone is good to just get to the code analysis. Each tool has a strength. The team is assessing, or they have assessed the last couple of months, which particular tool is good, and the pattern has been established."

Key observations:
- **Multiple accelerators** are being evaluated, not just one
- **Different accelerators excel at different things**: some are strong at Cognos report conversion, some at SQL Server migration, some at code analysis
- **Sources**: both Databricks itself and Databricks ecosystem partners
- **Assessment timeline**: "the last couple of months" — this evaluation has been happening in parallel with the finance track work
- **A pattern has been established**: the team has already determined which accelerator to use for which purpose

**Specific tool mentioned (lines 82-83):** "After that pattern, for example... Flow is something that we have already started."

The transcription is garbled here, but Mani referenced a specific tool or accelerator called something like "Flow" that the team has already begun using. This could be a Databricks-native tool, a partner accelerator, or a workflow orchestration tool. The exact identity would need to be confirmed with the team.

---

## 6. Team Institutional Knowledge

Mani was emphatic about the quality and depth of the team doing this work.

**Key statement (lines 92-95):** "This team is the best team we can have because they know the reports, they know in and out. They've been [working on this] the last three, four, five, six years. Some people are there for more than 5 years."

**Key statement (lines 95-96):** "We call it legacy, but I feel... they have specialized expertise in the tools."

Mani pushed back on the "legacy" framing. He views the team's deep knowledge of the existing systems not as a liability but as a core asset. These are not people stuck in old technology — they are the institutional memory that makes the re-engineering possible. They know what every report does, why it exists, and what the business depends on.

This institutional knowledge is what allows the team to make triage decisions (sunset vs. re-engineer) and ensures that business logic is not lost during re-engineering.

---

## 7. Semantic Layer — Pragmatically Deferred

Colin asked specifically about the semantic layer (common data definitions across the organization). Mani's answer was pragmatic and revealing.

**Key statement (lines 134-143):** "Semantically, we are not going to address that everything as a one shot... It's virtually an ongoing effort. We are not going to put too much effort in having common definitions, common terminology. If that kind of slows down our work, then we will not [pursue] that. We have to keep making progress. That's important. It's good to have a semantic layer. But if that semantic layer is slowing us down, then we just go ahead and put the engineering implementation."

**Key statement (lines 145-150):** Mani deferred the decision on the semantic layer to Grishi ("she"). If Grishi feels confident she can define the layer and the physical parts of what goes into it without slowing things down, Mani would support it. Otherwise, they skip it and keep moving.

**Key statement (lines 159-160):** "I think Grishi and Andrew would be good to do it. They have the right people to do that."

The semantic layer is:
- **Acknowledged as valuable** — Mani does not dispute its importance
- **Explicitly deprioritized** — if it threatens velocity, it gets deferred
- **Owned by Grishi and Andrew** — if pursued, these are the people who would define it
- **Not blocking the modernization** — the team will proceed with engineering implementation regardless

Colin noted this as a potential AI opportunity (lines 176-182): a semantic layer is particularly powerful if the company is pursuing agentic AI workflows, because it provides the structured definitions that agents need. If AI can help iterate on the semantic layer quickly, it could be built without the slowdown Mani fears.

---

## 8. Existing AI Tools in Use

Colin asked about existing AI tools being used to accelerate the effort.

**Key statement (lines 167-171):** "The team is using AI to accelerate. What exact tools they're using — it's a couple of tools that they use, and also 'low is Australia' and other tools that they are using. Those two are something that comes to my head right now. More details, Grishi might have already told you."

The transcription is severely garbled here. Possible interpretations:
- **"low is Australia"** could be a reference to an AI coding assistant like **Cody** (by Sourcegraph, which has Australian operations) or **GitHub Copilot**
- **"a couple of tools"** — at minimum two AI tools are actively in use by the team
- **Mani deferred to Grishi** for the specific details, suggesting Grishi is closer to the day-to-day tool usage

What is clear: the team is already using AI tools to assist with the modernization work. They are not starting from zero with AI adoption. Any proposal from BayOne would need to complement or build on top of what is already in place.

---

## 9. What Is Still Open or Undecided

### 9a. Front-End Reporting Tool Selection (Open but Deprioritized)

There is a "desire" to move to ThoughtSpot or Tableau (line 29), but this is not being actively pursued. Cognos is being retained as the front-end in most cases. The front-end tool question is open but not blocking — it is deferred in favor of the back-end re-engineering.

### 9b. Specific Tool Selection for Some Use Cases (Partially Open)

While the team has assessed accelerators and established patterns for which tool handles which purpose (lines 81-82), Mani still said "we are still exploring certain tools" (line 73). This suggests that while the major patterns are locked, some edge cases or specific use cases may still have open tool decisions.

### 9c. Detailed Scoping for Non-Finance Categories (Open)

For the three tracks not yet started, there is only "a general idea" (line 91). Detailed scoping — which reports to sunset, which to re-engineer, how many, what dependencies — will happen only when each category comes up in sequence. The architectural pattern transfers, but the report-level decisions do not.

### 9d. Semantic Layer (Open, May Stay Open)

As described in Section 7, the semantic layer is acknowledged but deferred. Whether it gets built at all during the modernization depends on Grishi's assessment of whether it can be done without slowing the team down.

### 9e. BayOne's Role and Engagement Model (Open)

Mani laid out several possible engagement structures (lines 378-382, 449-453):
- **Option A:** BayOne takes an entire category end-to-end
- **Option B:** Architecture and design done together with the core team, BayOne handles implementation
- **Option C:** A smaller confidence-building engagement first

Mani asked for exactly **three options** in the proposal (line 449: "Maybe just restricted to maybe three options"), with different categories potentially assigned to different engagement models. He also wanted to see flexibility in staffing models — not everyone needs to be full-time (lines 444-448).

---

## 10. Technical Architecture Details (What Can Be Inferred)

While Mani did not provide a full technical architecture diagram, the following can be assembled from his statements and Colin's summary:

### Source Systems (Being Re-engineered Away From)
- **IBM Cognos** — legacy reporting platform, 15-20 years of accumulated reports and queries
- **SQL Server** — legacy database platform underpinning reporting (referenced as "SQL Server" in Colin's summary, line 3; "CPO server" in Mani's garbled reference, line 79)
- **SSAS cubes** — Colin referenced these in his opening summary (line 3), and Mani did not correct it
- **DataStage** — Colin referenced pipeline migration from DataStage (line 5), uncorrected by Mani

### Target Platform
- **Databricks** — sole target data platform, confirmed multiple times
- **Azure** — implied by Microsoft's "seat at the table"; Databricks on Azure is the likely deployment model

### Front-End (Retained/Evolving)
- **Cognos** — retained as front-end in most cases, re-pointed to Databricks back-end
- **ThoughtSpot** — desired but not actively pursued
- **Tableau** — desired but not actively pursued

### Pipeline Architecture
- Pipelines are being rebuilt (not migrated) — this is part of the re-engineering mandate
- Specific pipeline technology on the target side not named, but Databricks-native orchestration is implied

---

## 11. Timeline Indicators and Milestones

| Indicator | Detail | Source Line |
|---|---|---|
| Architecture patterns | Established, will not change | 106-108 |
| Finance track status | ~20 working days from completion | 369-370 |
| Roadmap (category sequencing) | Done | 97-102 |
| Accelerator assessment | Done ("the last couple of months") | 81-82 |
| Cross-functional table | Assembled and functional | 118-125 |
| Time invested in foundation | 3 months of "deep efforts" | 116-117 |
| Tracks in progress | 3 | 103 |
| Tracks not yet started | 3 | 104-105 |
| Semantic layer | Deferred / conditional on Grishi | 134-150 |
| Proposal meeting | Planned for 2 weeks out (short week + offsite intervened) | 400-418 |

---

## 12. Key Quotes (Corrected for Transcription Errors)

**On re-engineering vs. migration:**
> "This is not a migration initiative. This is completely re-engineering. That's one thing that we are making very clear, and that's why you are not calling this migration — [it's] modernization. If it is migration, it's lift-and-shift or it's moving data from here to there. But in this context, it's not just migration. We have to re-engineer. We have to re-engineer and rewire these things." (lines 20-26)

**On what is established:**
> "The architectural factor is not going to change. Those parts are very well established." (lines 106-107)

**On the roadmap:**
> "Roadmap is kind of done. Which category comes first? Which category comes next? Which category comes third? That part has been figured." (lines 97-99)

**On finance status:**
> "Finance has already progressed. There's maybe another 20-odd days. So that's kind of like almost done." (lines 369-370)

**On the cross-functional table:**
> "We have a table, we have important stakeholders. Databricks has a seat at the table. Microsoft has a seat at the table. Data platform has a seat at the table. This team together, regardless where they come from — this is the core team. This team establishes what's right to do, how to do it." (lines 118-125)

**On the team's institutional knowledge:**
> "This team is the best team we can have because they know the reports, they know in and out. They've been [here] the last three, four, five, six years. Some people are there for more than 5 years." (lines 92-95)

**On accelerators:**
> "There are accelerators available — some from Databricks, and partners of Databricks have also given certain accelerators. Each tool has a strength. The team is assessing which particular tool is good, and the pattern has been established." (lines 76-82)

**On the semantic layer:**
> "We are not going to put too much effort in having common definitions, common terminology. If that kind of slows down our work, then we will not [pursue] that. We have to keep making progress. That's important. It's good to have a semantic layer. But if that semantic layer is slowing us down, then we just go ahead and put the engineering implementation." (lines 136-143)

**On existing AI tool usage:**
> "The team is using AI to accelerate. What exact tools they're using — it's a couple of tools that they use... Those two are something that comes to my head right now. More details, Grishi might have already told you." (lines 167-171)

**On three months of foundation work:**
> "Lots of efforts have gone the last 3 months. Deep efforts have gone on." (lines 116-117)

**On engagement model flexibility:**
> "One option is for you to take it entirely. Second is same piece of work — the architecture and design [done] together. People coming from different angles and places. The architectural design is kind of done by the [core] team, and then you can take the implementation." (lines 379-382)
