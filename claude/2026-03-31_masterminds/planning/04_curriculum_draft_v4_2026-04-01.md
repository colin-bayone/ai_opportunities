# Curriculum Draft v4

**Topic:** Artificial Intelligence, Productivity, Growth, and Evolution
**Audience:** Non-technical professionals (accounting, law, insurance, financial planning)

---

## Profile Slide

Who Colin Moore is and what he does. Full professional framing, not limited to the group context.

- Director of AI at BayOne Solutions
- Background spanning biomedical engineering, chemical process engineering, EV battery R&D (GM), and enterprise AI
- Built and led an AI Center of Excellence at a global manufacturer (30+ engineers, 60+ AI initiatives, $30M+ annual impact)
- Architected enterprise AI platforms serving 40,000+ users
- Advised legal, compliance, and cybersecurity teams on AI deployment risks
- The practical thread: has worked across industries from manufacturing to defense to consumer tech, always focused on real outcomes, not hype

This slide establishes credibility without being a resume. The point is that this perspective comes from building and deploying AI in the real world, across many industries, at scale.

---

## Section 1. What AI Actually Is

**Goal:** Build a shared vocabulary. Stop "AI" from being one blurry thing. Start broad, funnel toward Gen AI.

### The Three Branches

**Machine Learning**
Systems that learn patterns from data to make predictions or decisions. The oldest and most quietly embedded branch.

Examples they already encounter:
- Credit card fraud detection (flags unusual transactions in real time)
- Netflix and Spotify recommendations
- Email spam filtering
- Insurance risk scoring and underwriting models
- Financial forecasting and anomaly detection
- "People who bought X also bought Y"

**Computer Vision**
Systems that interpret visual information. Often combined with ML.

Examples they already encounter:
- Face unlock on their phone
- Tesla Autopilot and self-driving technology
- Medical imaging (detecting tumors, reading X-rays)
- Check deposit via phone camera
- Security cameras with person/vehicle detection
- License plate readers at toll booths

**Generative AI and Language Models**
The newest branch and the one getting all the attention. Systems that generate text, images, code, or other content. ChatGPT, Claude, Gemini.

This is where we go deeper:
- How language models actually work (pattern recognition on text at massive scale, not thinking)
- Why they are good at what they are good at (synthesis, summarization, drafting, reformatting)
- Why they struggle where they struggle (math, factual accuracy, domain-specific precision)
- The "closed circuit" concept: constrained input produces reliable output, open-ended roaming produces noise
- The difference between consumer tools (ChatGPT free tier) and enterprise/professional-grade tools

### Ground Truth and Training Data

A slide that connects how models learn to why their outputs look the way they do. Make this a fun, accessible exercise.

**What is ground truth?**
Ground truth is the verified, accepted correct answer that a model is trained against. In medicine, ground truth might be a biopsy result. In fraud detection, ground truth is whether a transaction was actually fraudulent. In language models, ground truth is the massive body of text the model learned from: books, articles, websites, code, conversations.

**How this shapes the model:**
- A language model's "knowledge" is the statistical patterns in its training data. It does not know things the way a person knows things. It has learned what words tend to follow other words in what contexts, across billions of examples.
- This means the model reflects the training data's strengths AND its weaknesses. If the training data contains biases, outdated information, or errors, the model carries those forward.
- When a model draws a conclusion or makes a connection between two seemingly unrelated things, it is doing so because that pattern existed in the training data. Sometimes that connection is insightful. Sometimes it is a statistical artifact that has no real-world validity.

**The fun exercise:**
Walk through an example where the same question gets a different answer depending on how it is framed, or where the model confidently connects two things that feel related but are actually coincidental. Use this to show that ground truth in language models is "what the training data says" and not "what is objectively true." That distinction is everything.

### When AI Gets It Wrong: Five Failure Modes

A dedicated slide that reframes the entire "AI hallucinates" conversation. Five distinct categories:

**1. True Hallucination**
The model fabricates something with no basis in any input or training data. It invents a legal citation, a statistic, a person who does not exist, a study that was never published. This is the failure mode that gets the headlines. It happens because language models are generating plausible-sounding sequences, not retrieving verified facts.

**2. Inaccuracy from Training Data or Provided Documents**
The model faithfully reproduces information that was wrong in what it was given. The training data contained an error, or the user uploaded a document with a mistake, and the model reflected it back. This is not hallucination. This is garbage in, garbage out. The model did exactly what it was supposed to do with bad input.

**3. Logical Incoherence from the User**
The user asked a bad question, gave contradictory instructions, or framed something in a way that led the model down the wrong path. The AI gave back exactly what was asked for. The user just asked wrong. This is the most common and least discussed failure mode.

**4. Outdated Information**
The model's training data has a cutoff date. It may give a confident answer based on information that was accurate when it was trained but has since changed. Tax law, case law, insurance regulations, financial products. All of these change frequently. The model does not know what it does not know about events after its training window.

**5. Personal Bias**
The user disagrees with the output, but the output is not actually wrong. This is the most uncomfortable one to talk about. Sometimes a model produces an answer that conflicts with a person's beliefs, preferences, or assumptions, and the instinct is to call it an error. It is important to distinguish between model bias (the model reflecting skewed training data) and human bias (the person rejecting a correct answer because they do not like it). Both exist. They are different problems with different solutions.

**Why this matters:** Three of these five failure modes are about the human side, not the AI. One is about the training data's age. Only one is the AI genuinely making things up. This reframes the reliability conversation entirely and gives people a vocabulary for diagnosing what actually went wrong instead of just saying "AI hallucinated."

### Segue: Gamma AI Live Demo

Between Section 1 and Section 2, a live demonstration using gamma.app. Generate a set of slides on the spot to show the room exactly how AI can produce something that looks polished and professional but falls apart the moment you scrutinize the content.

This serves multiple purposes:
- Visual, immediate proof of what hallucination and false confidence look like in practice
- Shows how easy it is to produce something that feels impressive but is indefensible
- Demonstrates that AI output requires verification, not blind trust
- Sets up the "what works and what does not" discussion in Section 2
- Fun, interactive moment that breaks up the presentation

The point is not to throw shade at Gamma specifically. It is to use a tool that everyone can visualize and test themselves as a concrete example of why human judgment remains essential.

### Why the Distinction Matters

Knowing which branch fits which problem is the first step to cutting through noise. A recommendation engine is not the same tool as a document summarizer. When someone pitches "AI" for your business, the first question is always "which kind?"

---

## Section 2. How It Works in Practice

**Goal:** Show real applications across their industries. 70/30 mix of lived experience and case studies (Colin brings specific examples) plus general industry examples.

### The 60/40 Reality

Every professional's work splits roughly into two buckets:
- The required work (scheduling, note-taking, reporting, formatting, data entry, routine correspondence)
- The value work (judgment, counsel, relationship building, creative problem solving, client trust)

AI absorbs the first bucket so professionals spend more time on the second. Not replacement. Reallocation toward the work that clients actually pay a premium for.

### Industry Walk-Through

Colin will supply specific case studies, some of which are directly relevant to the industries in the room. Structure will be a mix of "here is something I built or worked on" and "here is what is working in your field right now."

**Accounting and Tax**
- [Case studies and examples TBD]

**Legal and Estate Planning**
- [Case studies and examples TBD]

**Insurance and Risk Management**
- [Case studies and examples TBD]

**Financial Planning and Wealth Management**
- [Case studies and examples TBD]

### What Works and What Does Not (Yet)

Honest, grounded assessment.

Reliable today:
- Summarization of content you provide to it
- Drafting from templates or structured inputs
- Reorganizing and reformatting information
- Brainstorming and ideation
- First-pass review and analysis of documents

Still rough:
- Domain-specific accuracy (insurance policy language, tax code nuance, legal citation)
- Math and numerical reasoning
- Anything requiring empathy, judgment, or client trust
- Open-ended research without guardrails

### The AI Audit

A simple mental framework for evaluating any AI output. Four questions that take 10 seconds and catch the vast majority of failure modes:

1. **Who wrote the input?** Did you give it clear, specific instructions, or did you ask a vague question and hope for the best?
2. **What data did it have?** Was it working from documents you provided, or was it drawing from general training data?
3. **When was it trained?** Could this answer be outdated based on the model's training cutoff?
4. **Is this a fact claim or a synthesis?** Is the model asserting something verifiable, or is it combining ideas in a way that needs your judgment?

Something they can literally write on a sticky note and keep next to their screen.

---

## Section 3. Resilience

**Goal:** Address the real anxiety head-on. Is AI coming for their jobs? How will it change their business? Not cheerleading, not doomsday. Real industry insights and clear-eyed perspective.

### The Replacement Question

Address it directly rather than dancing around it. Real data, real stories from the industry about what has actually happened in professions that have adopted AI, not what pundits predicted would happen.

Key perspectives:
- What actually happened in fields that adopted early (radiology, legal discovery, financial analysis)
- The pattern that repeats: the tool augments the practitioner, the practitioner who uses the tool outperforms the one who does not
- The gas lamp lighter analogy (natural technological evolution, not catastrophe)
- What kinds of work are genuinely at risk vs. what kinds become more valuable

### What Changes and What Does Not

The human elements that AI cannot replicate and that become more valuable as AI handles the routine:
- Trust and relationships (clients hire people, not algorithms)
- Judgment in ambiguous situations
- Empathy and emotional intelligence
- Accountability (someone has to sign off, advise, and stand behind the recommendation)
- Cross-disciplinary synthesis (connecting dots across fields, exactly what this group does)

### The Cost of Waiting vs. The Cost of Doing It Wrong

Frame the adoption decision honestly for an audience that advises clients on risk for a living.

**The cost of waiting:**
- Competitors who adopt first gain efficiency advantages that compound over time
- Client expectations are shifting. People are starting to expect faster turnaround, more personalized communication, and proactive insights.
- The learning curve exists whether you start now or start in two years. Starting now means the curve is gentler.

**The cost of doing it wrong:**
- PII exposure from using the wrong tool the wrong way
- Bad output that damages client trust
- Over-reliance on AI for tasks that still need human judgment
- Wasted time and money on tools that do not fit the actual workflow

Neither extreme is the answer. The smart move is deliberate, informed experimentation. Not transformation overnight, not avoidance.

### The Adaptation Mindset

Not about becoming technical. About developing the instinct for when AI helps, when it doesn't, and when to ask. The professionals who thrive are not the ones who learn to code. They are the ones who learn to ask better questions and verify the output.

### What I Wish Someone Told Me

A personal moment. Something from Colin's own experience where the gap between AI promise and AI reality was visceral. A real story, not a framework. Could be from the Coherent days, from early BayOne work, or from advising a client. The kind of thing that only someone who has actually built and deployed these systems can share.

[Colin to supply specific anecdote]

---

## Section 4. Getting Real

**Goal:** Practical guide for walking out of this room and doing something useful. Compliance, tools, myths, and specific things they can try.

### Compliance and PII Privacy

- When it is safe to put client information into AI tools and when it is not
- What "enterprise" actually means in practice
- The distinction between tools that train on your data and tools that do not
- Quick framework: if you would not put it in an email to the wrong person, do not put it in a consumer AI tool
- Specific guidance on the major platforms (ChatGPT, Claude, Gemini, Copilot)

### Responsible Use of Common Tools and Platforms

- Quick rundown of the major tools, what each is good at, where each falls short
- Free tier vs. paid tier differences (not just features, but data handling)
- When to use which tool for which task
- The verification habit: always check the output before acting on it

### The Vendor Pitch Filter

Three questions to ask anyone pitching an AI solution for your business:

1. **What data does it need access to?** If the answer is vague or "everything," that is a red flag.
2. **Where is that data stored and who can see it?** Cloud, on-premise, third-party. Who has access. Whether your data trains their model.
3. **What happens when it is wrong?** Every AI system will produce errors. The question is whether the system is designed for a human to catch them before they reach a client.

These are not technical questions. They are due diligence questions, the same kind of scrutiny these professionals already apply to any vendor or partner.

### Myth-Busting

Address the common misconceptions directly:
- "AI is going to replace [my profession] in 5 years"
- "AI is too unreliable to use for anything serious"
- "If I use AI, my work product is somehow lesser"
- "AI understands what I am saying" (it does not, and that is OK)
- "The free version is basically the same as the paid version"
- How to tell hype from real value (if someone is pitching you AI, what questions to ask)

### Business Applications They Can Use Now

Specific, actionable things beyond document work:
- Marketing and outreach (drafting campaigns, refining messaging, client newsletters)
- Social media and thought leadership content
- Competitive research and market intelligence
- Proposal and pitch preparation
- Internal process documentation
- Client onboarding materials

### Where and How to Get Started

- Start with one repetitive task, not a reinvention of your practice
- Pick the right tool for that task
- Set a 30-day experiment with a clear goal
- Evaluate honestly and expand or pivot

---

## Q&A

Open floor.

---

## Live Segues and Interactive Moments

These are not slides but presenter-driven moments that can be deployed where the flow calls for them:

1. **Gamma AI demo** (between Section 1 and Section 2): Generate slides live, show the gap between polish and substance
2. **Tool comparison** (Section 4): If the room has laptops or phones, quick live comparison of the same prompt across ChatGPT, Claude, and Gemini to show how different tools handle the same question differently
3. **"Ask me anything" checkpoints**: Brief pauses between sections to take a question or two rather than saving everything for the end
4. **Ground truth exercise** (Section 1): Walk through a live example where framing changes the answer, showing that ground truth in language models is "what the training data says" not "what is objectively true"
