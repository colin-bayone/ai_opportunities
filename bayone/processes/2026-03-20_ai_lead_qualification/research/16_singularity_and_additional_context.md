# Singularity Discussion & Additional Context (Mar 11, 2026)

## Context
This is a transcript between Colin and Pallavi (his developer). The first ~55 minutes covers TalentAI permissions architecture (not relevant to the framework). The remainder covers Singularity and Colin's articulation of the sales problems to his team member. Colin has noted that Singularity is an enabler for the framework, not the framework itself.

---

## Singularity: What It Is

An internal Django application that Colin is building to be "one place for everything" related to AI solutions opportunities. It's being built by stripping TalentAI down to a base Django starter app and adding new functionality.

### Core Components

**1. Project Intake Form**
- Simple form where sales enters a new opportunity
- Required fields: client name, internal team owner, general description, supporting documentation
- AI layer validates completeness: "You're 90% complete. Still need a little bit more information before we send this off to the AI team."
- Transparency about what's missing
- Explicit rule: "Don't reach out to them on the side because they're not going to answer"

**2. Black Hole (Document Upload Portal)**
- Generic upload area per project for any file type (PDFs, transcripts, PowerPoints, images, audio)
- Chronological timeline of uploads
- Everything goes to Azure Blob Storage
- Sales can continuously add context while qualification is in progress
- Creates the documentation trail that currently doesn't exist

**3. AI Qualification Engine**
- AI reviews all uploaded documents and project context
- Assesses whether the opportunity is qualified for AI team involvement
- Identifies what's still missing
- When qualified, generates a detailed AI-generated breakdown for Colin's team to review
- Colin's team then decides whether to proceed

**4. Grounded Slide Generation**
- HTML-based slides generated from real project context and real capabilities
- Uses structured markdown documents of BayOne's 7 actual solution areas
- AI selects the relevant capabilities for the specific client and meeting
- Brand-aligned templates and UI controls ensure consistent quality
- Exported to PowerPoint as screenshots (avoids PowerPoint XML complexity)
- Solves both the "ugly slides" problem and the "fabricated content" problem

**5. Case Study Generation**
- Same grounding approach: generated from actual project data, not ChatGPT hallucinations
- HTML to PDF conversion
- Only based on real, completed work

---

## Colin's Problem Articulation (To His Developer)

Colin distilled the problems into a very clean framework for Pallavi:

### Problem A: Sales doesn't know how to sell AI
- "Every single conversation they have in any way with anyone at any level, they come to me and say, can you get on the next call?"
- Most aren't real opportunities or are misattributed

### Problem B: After calls, sales doesn't provide enough information
- Colin gets messages like "Tailored Brands VP and three senior directors are ready for us to meet them via Teams on Friday. Please let me know if this works."
- No context about who the people are, what their roles are, what the company does, what they're interested in
- Colin then has to do 3x the work to get the information on paper

### Problem C: How to keep everything up to date
- Projects, context, leadership updates, slides, case studies
- Currently a manual, painful process where Colin is the bottleneck for all content

---

## Additional Incidents and Patterns Mentioned

### The California Assumption (New Incident)
Sales called Colin at 4pm his time asking if he was in California. He's in Pittsburgh, Pennsylvania, on the opposite coast. They wanted him to be at an in-person meeting the next day. They'd known about it since Tuesday but only told him the day before. No calendar invite had been shared. Colin told them to reschedule.

**Reinforces:** Pattern 5 (committing Colin's time without asking), Pattern 9 (no minimum information), and a new element: **geographic assumptions with zero coordination.**

### The Manufacturing/TechScore Incident (New)
Sales was meeting with a manufacturing client and tried to pitch TechScore (a hiring/recruitment product). Colin: "They're manufacturing. They don't care about hiring. What does that even mean?"

**Reinforces:** Pattern 17 (kitchen sink presentations) and Problem 5 (AI literacy gap / inability to match capabilities to client context).

### Fabricated Case Studies: The Full Process Exposed
Colin confirmed the exact workflow to his developer:
1. Salesperson goes to ChatGPT
2. Types "I have an upcoming meeting with Walmart, generate me a case study"
3. ChatGPT produces something made up (not based on BayOne's actual work)
4. Salesperson saves it
5. **Time passes and they forget that's how the case study was created**
6. They present it to a client as real
7. Then they send Colin the email: "Are you ready with this Walmart-scale chatbot?"

Colin: "We just made up metrics. We can't. I never told it any of that. There's no way it could know any of this."

### Gamma AI Abuse
Sales team is using Gamma.ai to generate slide decks. The output looks polished but contains completely fabricated claims. Colin demonstrated live: a generated deck claimed "Deploy agents in under 5 minutes" and "Sephora grade AI instantly" with made-up metrics.

Colin: "I'm very close to just banning this at Bay One for things like Gamma."

---

## Colin's Enforcement Philosophy

### "They need something from us. We don't need something from them."
This is the leverage point. Sales needs:
- Slides and presentation materials
- Technical expertise on calls
- Case studies and use cases
- Qualification and scoping of opportunities

Colin's new approach: none of these things happen unless the process is followed. Singularity becomes the gate.

### Key Quotes
- "If you wanna have a meeting about a project, I'm not gonna get on that meeting unless you've done this part first."
- "I'm not gonna write you slides unless they come from this [Singularity]."
- "If they don't use it, then don't. But I'm not gonna write you slides unless they come from this."
- "I even told Suresh, our new CEO. I talked to him and I was like, I just want you to give me the green light to say whatever I say goes."

### Start Small, Iterate
- Project ingestion (just a form with minor AI features) first
- Get people using it
- Roll out incrementally
- "No stakeholders other than me" for timeline
- "It's ready when it's ready"

---

## Implications for Framework

1. **Singularity is the enforcement mechanism.** The framework defines the rules; Singularity enforces them digitally. Sales can't bypass the process if the process is built into the tool they need to use.

2. **The upload-first approach solves the documentation problem.** Instead of asking sales to write detailed briefs (which they won't do), let them upload whatever they have. AI does the heavy lifting of extracting and organizing.

3. **Grounded content generation solves the fabrication problem.** If slides and case studies can only be generated from real project data in the system, sales can't fabricate. The tool physically prevents it.

4. **Progressive qualification.** The "90% complete, need more info" approach is smarter than a hard gate. Sales can start adding context before qualification is complete, which means the process feels less like a blocker and more like a helper.

5. **Leverage-based adoption.** Sales needs slides and technical support. Colin controls both. The framework doesn't have to rely on compliance; it can rely on incentives.

6. **Capacity reality.** Colin is handing TalentAI off to Ambar's team specifically to free his team for solutions work. The framework needs to account for this capacity shift.
