# 01 - Meeting: AI Opportunities and Engagement Approach

**Source:** /sephora/edw_modernization/source/mani_meeting1_2026-02_formatted.txt
**Source Date:** 2026-02 (Initial Discovery Call with Mani)
**Document Set:** 01 (Mani Meeting 1)
**Pass:** Focused deep dive on AI opportunities and Mani's guidance for engagement approach

---

## 1. AI Use Case #1: Legacy Cognos Codebase Analysis

Mani described this use case in detail when discussing the EDW Modernization challenge. The core problem: Sephora has 15-20 years of accumulated reports built in legacy technologies (IBM Cognos, SQL Server). The queries powering these reports are "very deep inside the code" (line 186), and manual review of the codebase would be impractical at scale.

**Mani's exact framing (paraphrased from speech-to-text, lines 185-192):**

> If you look at Cognos, there are 15-20 years of implementation. The queries are very deep inside the code. If somebody has to go through that manually, it will take years for us to even finish --- forget starting, but finishing will take a long time. We are looking for AI to come and help --- look at the codebase, and AI would itself proactively come and tell us: these things are something to watch out for. It will analyze the codebase and say, these are all the places for us to mind for.

**What Mani is asking for specifically:**

- Automated analysis of the legacy Cognos codebase
- AI that proactively surfaces risks, anomalies, and "things to watch out for" rather than requiring humans to know what questions to ask
- Identification of all the places in the codebase that need attention --- essentially a comprehensive audit that would be impossible to perform manually within the project timeline
- This is not just code migration; it is code comprehension at scale --- understanding what thousands of legacy reports actually do, how their queries are structured, and where the complexity and risk lives

**Scale of the problem:** Thousands of reports, accumulated over 15-20 years, across multiple business domains (finance, supply chain, stores, e-commerce). The reports span IBM Cognos and SQL Server technologies.

## 2. AI Use Case #2: Accelerating Report Migration

Mani described the current report-by-report migration approach as too slow for the project timeline (lines 176-178).

**Mani's exact framing (paraphrased from speech-to-text, lines 176-178):**

> If we go report by report, it will take a long time. What would be an easier way, an efficient way? Instead of going report by report, can we do something like --- if we do this, we can finish off three reports at one shot. Or we can finish off six reports at one shot. So we can expedite the delivery.

**What Mani is asking for specifically:**

- A way to batch-migrate reports rather than converting them one at a time
- Moving from sequential (one-by-one) to parallel processing --- finishing 3 or 6 reports simultaneously
- The goal is to compress a three-year timeline (currently planned through 2028) into two years or less (finish by 2027 or early 2028, per lines 81-83)
- His team is already experimenting with Databricks to find the "right tool" for this, but has not solved it yet

**Context on the migration target:** Reports are being re-engineered from Cognos/SQL Server into modern technologies. The target stack is Databricks for data, with Tableau in some areas, ThoughtSpot in some areas, and Cognos retained in some areas (but pointed at the new Databricks data platform instead of the old database).

## 3. Databricks AI Tools --- What Is Already in Play

Mani mentioned that Databricks is "already coming up with AI-oriented tools" (line 183) and that Sephora has "asked Databricks to come with recommendations" (line 194).

**Key signals:**

- Databricks is actively pitching AI tooling to Sephora for this modernization effort
- Sephora is receptive and has explicitly asked Databricks for AI recommendations
- Mani's team is "experimenting" with these capabilities (line 193) but has not settled on a solution
- This means BayOne/Colin would be entering a space where Databricks is already a trusted advisor --- the proposal needs to complement or outperform what Databricks is offering, not duplicate it

**Competitive positioning implication:** Colin needs to understand what Databricks is bringing to the table (likely Databricks AI/ML features, possibly Databricks Assistant or code analysis tooling) and position BayOne's AI approach as additive --- either covering gaps Databricks cannot address (such as Cognos-specific codebase analysis, which is outside Databricks' core competency) or offering a more tailored, hands-on solution versus Databricks' general-purpose tooling.

## 4. Mani's Explicit Instructions for Engagement Approach

This is perhaps the most critical section for how Colin should prepare. Mani gave clear, direct guidance on what he expects from the AI engagement (lines 157-162).

**Mani's instruction (paraphrased from speech-to-text, lines 157-162):**

> Since you have already been working with [Sephora] for a long time, you know the tech stack and all that. So if that person comes with a little bit of groundwork done --- instead of coming and asking "hey, what is this? What are you guys doing?" --- that person can come with groundwork, talking to the teams, and then coming with a certain proposal. That would be great. That would be a very productive discussion.

**What this means for Colin's approach:**

- Do NOT come with a blank-slate discovery posture. Mani explicitly does not want to sit through "what is this, what are you guys doing" questions.
- DO come with groundwork already completed --- leverage BayOne's existing institutional knowledge of Sephora's tech stack, org structure, and project landscape.
- DO come with a proposal ready to present --- not an abstract capabilities pitch, but a concrete recommendation for how AI can address the specific use cases Mani described.
- Talk to the teams (Grishi, Andrew Ho, others) before meeting with Mani to gather technical details.
- The bar is: walk in prepared, present a proposal, have a "productive discussion" about implementation --- not an introductory meeting.

**Zahra's reinforcement of this (lines 213-214):**

> Maybe we can come back with a one-pager or something for you to take a look at, and then further meetings around it.

Zahra committed to delivering a one-pager or POC before the next meeting. This sets the expectation that Colin will produce a tangible artifact (one-pager, proposal, or POC) as the entry point for the AI conversation.

## 5. How BayOne Positioned Colin and the AI Practice

Zahra and the BayOne team made several specific claims about Colin and the AI practice during this meeting. These create expectations that Colin needs to fulfill.

**Claims made to Mani:**

- "We hired a director of AI" (line 2) --- Colin was introduced at the leadership level
- Zahra called Colin "our AI genius" (line 213)
- "He's absolutely great and [we've] gotten really good feedback" (line 152)
- "This guy's brilliant" (line 167)
- Colin "builds something for BayOne" --- specifically an AI employee portal (lines 208-212), described as tools available to BayOne employees for education on AI capabilities
- Colin built "Recruiting 2.0" (line 351) --- automating recruiting processes using AI, described as a major use case
- Projects completed for Lam Research ("Lamo," line 167) --- described as an AI project that took about three months end-to-end
- Projects completed for Cisco ("C school," line 352)
- Colin's team sits in India (line 348) and provides well-vetted AI talent

**Expectation this creates:** Mani is expecting someone with deep, proven AI implementation experience who can walk in with a solution, not someone still learning the problem space. The "genius" framing is high-risk/high-reward --- it sets the bar very high but also creates strong initial credibility.

## 6. Marketing AI Task Force Structure

Mani described an AI task force within his marketing organization (lines 92-93).

**Structure as described:**

- Sephora has an enterprise-wide AI task force
- Mani's marketing organization has its own marketing-specific AI task force
- The marketing AI task force operates at the "front foot" --- meaning it leads and drives adoption
- It partners with the enterprise-wide AI task force
- The marketing AI task force's role includes training all other team members in Mani's organization on AI

**Where it sits organizationally:** Under Andrew Ho's area. Mani listed "influencer marketing, media marketing, and marketing AI" as all falling under Andrew Ho (lines 108-109). This means Andrew Ho is the organizational home for marketing AI initiatives.

**Implication for Colin:** Andrew Ho is a key stakeholder for any AI work in Mani's org. If Colin is going to propose AI solutions for the EDW modernization, he may also want to understand what the marketing AI task force is already doing to avoid overlap and to find synergies.

## 7. "Full Stack with AI" as a New Hiring Profile

Mani signaled a shift in hiring requirements (lines 330-331, 338, 340-346).

**Mani's exact framing (paraphrased from speech-to-text):**

> We are coming up with completely agentic coding and AI and all those things. That will be a new required skill set. Full stack with AI could be one of the pipelines that you can build.

He then suggested BayOne prepare two types of candidate profiles:
1. Full stack with AI
2. AI-oriented data processing

Mani said his team would send BayOne the specific profile descriptions so they could start building a talent pipeline (line 346-347).

**Signals:**

- "Agentic coding" specifically mentioned --- Mani is aware of and interested in agentic AI patterns
- This is not a vague future aspiration; he framed it as an active hiring need for 2026
- He wants the pipeline built proactively, before specific requisitions open
- This creates a secondary revenue opportunity for BayOne beyond the consulting engagement --- staffing AI-skilled engineers

## 8. Budget and Investment Signals

While Mani did not provide explicit AI budget numbers, several signals indicate willingness to invest:

**Positive signals:**

- The EDW Modernization is described as a three-year project (lines 75, 81) with an existing plan through 2028 --- this is a major, funded initiative, not speculative
- Mani is already experimenting with AI solutions and has asked Databricks for AI recommendations (line 194) --- budget has been allocated or at least contemplated for AI tooling
- Multiple hiring streams are active across all four of Mani's direct reports' teams (Ram, Andrew Ho, Grishi, Rizwan) --- headcount budget is flowing
- Mani's openness to nearshore rates ($75/hour range) and his stated ceiling for onsite ($105-115/hour, with $120 no longer acceptable) provides clear rate parameters
- The "full stack with AI" pipeline request indicates he is planning to hire for AI capabilities, not just explore them
- Mani wants to compress a three-year project into two years or less --- he is motivated to invest in acceleration tools

**Caution signals:**

- Databricks is already in the room as a trusted advisor on AI tooling --- BayOne needs to differentiate
- Mani wants to see prepared proposals, not exploratory discovery --- he is not going to fund open-ended exploration
- Rate pressure is real and trending downward --- any AI engagement will need to be priced competitively

## 9. Timeline Signals for AI Work

- EDW Modernization has "already started" as of this meeting (line 76), with the plan running through 2028
- The team is "still experimenting" with AI approaches (line 193) --- no solution has been locked in yet
- Finance department (specifically business planning) is the first department being migrated (lines 203-206) --- this is where a POC would have the most immediate relevance
- Mani wants a proposal brought to him, not a discovery meeting --- suggesting he is ready to evaluate and act, not just discuss
- Zahra committed to getting Colin in front of Mani "sometime in the new year" (line 2) --- the clock is ticking on delivering that prepared proposal

## 10. Summary: What Colin Needs to Prepare

Based on Mani's explicit and implicit guidance, Colin should prepare the following before any meeting:

1. **A concrete proposal for Cognos codebase analysis using AI** --- demonstrating how AI can ingest a large legacy Cognos codebase, understand the query structures buried in the code, and proactively surface risks, complexity, and areas requiring attention. This is the highest-signal use case Mani described.

2. **A concrete proposal for batch report migration acceleration** --- showing how AI can enable migrating 3-6 reports simultaneously instead of one at a time, compressing the three-year timeline. This needs to account for the heterogeneous target stack (Databricks, Tableau, ThoughtSpot, and retained Cognos).

3. **Awareness of what Databricks is already offering** --- so the proposal complements rather than competes with Databricks' AI tooling. Position BayOne's AI practice as filling gaps Databricks cannot (especially Cognos-specific analysis, which is legacy technology outside Databricks' AI tool focus).

4. **A tangible artifact** --- one-pager, proposal document, or POC. Mani and Zahra both expect something concrete, not a slide deck of capabilities.

5. **Prior conversations with Grishi and Andrew Ho** --- Mani explicitly said "talking to the teams" should happen before the meeting with him. These conversations should gather the technical specifics needed to make the proposal credible.

6. **Understanding of the marketing AI task force** --- to identify whether there are additional AI opportunities beyond EDW modernization, and to demonstrate breadth of understanding of Mani's organization.
