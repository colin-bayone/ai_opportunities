# Meeting 2 - Verbatim Key Quotes

## Attribution Key
- **[C]** = Colin Moore
- **[M]** = Mani Soundararajan
- **[Z]** = Zahra

---

## Colin's Opening Summary (Cleaned)

> **[C]**: "What I understand so far is that Sephora is right now undertaking a three year EDW project to migrate from some legacy on-prem, but very developed infrastructure over to Databricks, which also includes, of course, the reporting side of the house. And all of your reports right now are a combination of things like Cognos, as well as having some SSAS cubes available to the business users. And those are going to be migrated over to something like ThoughtSpot and Tableau. And there's pipelines that also need to be migrated, something from DataStage, over to more Databricks pipelines, either natively or maybe something else. Some Cognos being retained as well because that transition happens slowly while the data layer is being modernized. And there's probably something there, as well, with a semantic layer that needs to be created and formed."

---

## Mani's Critical Correction

> **[M]**: "You understood it very well. Not everything is being translated to Tableau. And this is NOT a migration initiative. This is completely re-engineering initiative. That's one thing that we are making very clear, and that's why we are not calling this migration but modernization. If it is migrated, it's lift and shift or it's moving the data from here to there or moving something from one place to another place. But in this particular context, it's not just migration. We have to re-engineer that. We have to re-engineer and rewire those things."

**This is the most important clarification in the entire engagement.**

---

## On Retaining Cognos Front-End

> **[M]**: "In most cases, we are trying to retain the front end of it, which is, if it is Cognos, it will remain in Cognos. There is a desire to move to ThoughtSpot or Tableau, but that's not something that we are pursuing right now. The change management is not... it's not so resistant. That's why we're keeping this."

---

## On Track-Based Approach

> **[M]**: "There are thousands of reports in that area. Now, we will not be able to change everything in one shot. So we are approaching this track by track and category by category. We have figured out 3 to 4 different categories of tracks. Finance is the first thing that we have taken. Within Finance, we have figured out. Yes. And at the same time, we have also established certain architectural patterns."

---

## On Tools and Experimentation

> **[M]**: "We are still exploring certain tools, what tools we can use. We know the target, because target is Databricks. We know the source. Now, there are accelerators available. Some Databricks that source, and partners of Databricks have also given certain accelerators. Now, here, the whole team has to figure out which accelerator is going to be the best fit for one case. Someone went with respect to Cognos. Someone went with respect to SQL Server. Someone was good to just get to the code analysis. Each tool has its own strength. Now, the team is assessing... the last couple of months, which particular tool is good and for what, and the pattern has been established."

---

## On Core Governance Table

> **[M]**: "We have important stakeholders everywhere. This team together, regardless where they come from, doesn't matter. But this is the core team. This team establishes what's right to do, how to do it."

> **[M]**: "Databricks has a seat at the table. Microsoft has a seat at the table. Data Platform has a seat at the table."

---

## On Semantic Layer Pragmatism

> **[M]**: "Semantically, we need to check with Grishi on this. In my view, we are not going to address everything as one shot and then later. It's actually an ongoing effort. And we are not going to put too much effort in having common definitions, common terminology. Even try, I'll test. But if that kind of slows down our work in this, then we will not address that. We have to keep making progress. That's important. It's good to have a semantic layer. But if that semantic layer is slowing us down, then we just go ahead and do the engineering implementation."

---

## On Andrew Ho and Semantic Layer

> **[M]**: "Terti and Andrew would be good to do it. They have the right people to do that."

**Key insight for Andrew meeting - he's been named as semantic layer owner.**

---

## Colin's Value Proposition

> **[C]**: "Where AI can help, there's a few places, and this is going to be a combination of things. More traditional ML-based approaches, but also some of the nice agentic features that the organization might be looking at, if that's something of interest."

> **[C]**: "One is something that can help save a lot of people, which is pattern detection, clustering. Looking across reports, a lot of reports tend to have a lot of similarity. And that does allow for patterns to be extracted and found in those reports so that you can then pass it to humans, so that the human is essentially looking at multiple things at once. They're not having to review report by report anymore. They can do this in more aggregate fashion."

> **[C]**: "Even with AI in the picture, you still have to validate. You can't just turn AI loose as much as we'd like to sometimes. It doesn't work. So this helps to reduce the work because we're using more deterministic systems, higher reliability patterns to do this rather than just saying, 'Hey, ChatGPT, look at this report and compare to this and give you some files and output.' We're going a lot deeper than that."

---

## On Colin's Experience

> **[C]**: "My prior organization was about 40,000 employees, about $16 billion annual revenue. And we had AI right next to BI. So those lived in the same house, under the same roof, and under mine and my supervisor's leadership at that time. I was the CTO for the company. And what had happened was we realized early on AI and BI need the same data. Same source of truth for everything leads to people calling us a little bit less on a Saturday saying, 'hey, my report doesn't agree with someone else's report.'"

> **[C]**: "So we undertook the same type of effort, not to Databricks, but this was actually to Snowflake. Similar, exact same type of effort."

---

## Mani's Probing Questions

> **[M]**: "I'm trying to understand what is the value or unique thing that you want to present here."

> **[M]**: "So have you done this before? Do you have any case studies or examples?"

> **[M]**: "I would like to see if you can bring a specific example with certain assumptions. Approximately what would be the cost? So cost wise would depend upon the scope of it."

---

## Colin's Honest Response

> **[C]**: "The only thing I would say is experience. So have you done this before? We know the pain points. We know where things get stuck. We also know, like you said, the balance is tough to find."

---

## Mani's Proposal Requirements

> **[M]**: "What I was saying... I would love seeing what kind of investment you can do. Not just a confidence one, but also what kind of investment that you guys can do. So if you can bring that point of view also in the proposal, that would be good."

> **[M]**: "Maybe one last question. From the proposal standpoint, I can give you maybe 2 different types of proposals... One is to build your confidence because I know we're new to you in this space. So I recognize that. But at the same time, I want to be able to give you some confidence. So if there's something smaller that would be useful to you, then we could do that to start, even if that's a process."

> **[M]**: "Let me see that we do 3 options. Don't overwhelm me with like 7 options, that would be too much. Maybe just restricted to maybe 3 options."

---

## On Pilot Tracks

> **[M]**: "Finance has already progressed. There's maybe another 20, 24 days. So that's kind of almost done."

> **[M]**: "Supply Chain could be one thing. Merchandising, because it's still... you guys, check with Grishi."

---

## On Scheduling

> **[M]**: "Next week is a short week."

> **[M]**: "Wednesday, we have a huge off-site. Thursday, we all are on, like, really off. So next week is not a good time."

> **[M]**: "I would like to come and attend that meeting."

---

## Meeting End Energy (Cleaned - Some Informal Language)

Post-meeting, after Mani left:

> **[Z]**: "That was so good."

> **[Z]**: "That slide was two minutes before."

**Indicates: Meeting exceeded expectations. Colin's preparation paid off even though slides were last-minute refinement.**

---

## Most Important Quotes (Summary)

1. **[M]**: "You summarized it very well. You understood it very well." (Validation)

2. **[M]**: "This is NOT a migration initiative. This is completely re-engineering." (Critical framing)

3. **[M]**: "Terti and Andrew would be good to do it." (Andrew's role)

4. **[M]**: "If that semantic layer is slowing us down, then we just go ahead" (Pragmatism)

5. **[M]**: "Let me see that we do 3 options." (Clear ask)

6. **[M]**: "I would like to come and attend that meeting." (Personal investment)
