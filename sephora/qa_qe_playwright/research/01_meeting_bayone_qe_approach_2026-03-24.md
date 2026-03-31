# 01 - Meeting: BayOne QE Approach

**Source:** /sephora/qa_qe_playwright/source/vabhav_3_24_2026.txt
**Source Date:** 2026-03-24 (Introductory meeting / discovery conversation)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on BayOne's QA/QE methodology as presented by Colin

---

## 1. Colin's Background and Positioning

Colin Moore introduced himself as BayOne's head of AI. Before BayOne, he was at Coherent Corp (~40,000 people, ~$8B revenue) where he "grew up from the ground their whole AI practice." He started the AI COE there, "originally got the team together, ended up having a team of about 120 people globally" doing work across engineering, legal, finance, and other domains.

At BayOne, he is "establishing these core competencies for us in AI." He emphasized the pace of change: "it does change maybe not even since the beginning of the year, but maybe since last week."

**Key positioning statement on QA/QE:** "Our philosophy right now is kind of practice like we play, be our first customer to ourselves. So even when we're developing things internally, we have fully automated QA/QE. So that's an easy thing for us. It's not like a product we're selling. We're kind of just taking what we do and doing it for [clients]."

---

## 2. Deterministic-First Philosophy

Colin articulated a core design principle that governs everything in his QE approach:

> "For anything that I do, you'll find that the approach is first deterministic as much as I can. Bring in AI last as a rule because it's kind of like the telephone game. There's a certain amount of reliability that you can and cannot get out of AI systems. And I don't like seeing numbers that are 80 percent. I like 97 plus."

This is the foundational philosophy. AI is layered on top of deterministic processes, not used as the starting point. The rationale is explicitly about reliability: AI introduces variability ("telephone game"), so you minimize the surface area where that variability can compound.

**Target threshold:** "97% plus" -- not 80%. This was stated as a hard line.

**Practical implication:** "The trick is to keep it deterministic as far as you can, and then agentic at the end. If you keep it that way, then you can make sure that the flow is happening repeatedly, reliably, without really having to worry too much."

---

## 3. State Graph Mapping of the Codebase

The first step in Colin's methodology is autonomous, deterministic exploration of the codebase to produce a state graph:

> "What we do with the approach is to get a map, essentially, of the code base. Every part of it. We explore it."

> "We deterministically explore the code base first, we get this mapped out. And we actually just -- this is an autonomous process that goes and makes essentially a state graph of what's going on here."

**What the state graph captures:**
- Dependency mapping between modules ("what modules talk to each other")
- CVEs / library vulnerabilities ("even things where we're seeing like CVs, any libraries that are used")
- Dead code identification ("we usually do that as a first step to also help to identify dead code")

**Cross-purpose utility:** Colin noted this state graph step is not exclusive to QA/QE work. "Even if it's not a QA/QE project, we do that because sometimes, like for a modernization project, we're trying to convert from one language to a completely different framework or language. I want to know what I don't have to do first. Simplify that problem."

This suggests the state graph is a reusable asset -- the same exploration feeds modernization planning, test generation, and dependency analysis.

---

## 4. CI/CD Pipeline Integration with State Graph

The state graph plugs directly into CI/CD pipelines to enable targeted, change-aware testing:

> "Once we have the state graph, that plugs in very nicely with CI/CD pipelines. So that means that whenever new things happen or change, now I can adjust my tests accordingly. I know what to start when."

> "CI/CD plugging into a state graph to keep this all tracked. So that means if a file changed, you know, maybe this file change or maybe this set of file changes -- what unit tests need to be run here?"

**The key value proposition:** Rather than running the full test suite on every change, the state graph maps file changes to the specific tests that are relevant. This is change-aware, dependency-informed test targeting.

---

## 5. Coverage Model: Recursive Downstream Dependencies

Colin challenged the conventional understanding of "coverage" with a pointed question:

> "What does coverage actually mean? That's a fun question to ask."

His answer redefines coverage beyond function-level testing:

> "When we say coverage for a unit test, does that just mean that it's testing out all the functions or should it also test the things that it touches that could be downstream dependencies recursively? It has to be that. Because otherwise it's not a good unit test at the end of the day."

**Coverage = recursive downstream dependency testing**, not just function-level assertion coverage. A unit test that covers all branches of a function but ignores what that function's output feeds into is, by this definition, incomplete.

---

## 6. Standards-Setting for Unit Tests

Colin identified standards as a critical and difficult problem:

> "Writing the unit test too is usually where standards come into the picture, which is tough because that varies greatly across all organizations, even within organizations, even within teams."

**BayOne's role:** "We can help to set those standards first early on, at least the first pass that you get to guide the unit test and the way that they're created."

This positions BayOne as establishing the baseline conventions before test generation begins -- the deterministic foundation that agents then follow.

---

## 7. Edge Case Feedback Loop

When tests miss something, the system captures that failure and feeds it back:

> "If we find things weren't caught, those immediately have to go back to a part of the system to say this is an edge case that we didn't catch. Next time the situation comes up, even not this exact situation, look out for it. Let's make sure we have coverage here."

This is a learning loop. Not just for the exact edge case, but generalized: "even not this exact situation" -- the system should recognize similar patterns in the future.

---

## 8. Central Framework and Accumulating Knowledge

> "The point is that it all has to be a central framework so that it always keeps benefiting."

Colin emphasized this is not a large-team effort:

> "It sounds like it's a lot, but it's not. This is something that I do with two other people. So it's not like it's a big team that has to do this. The trick is to bring it all together."

**"Two other people"** -- Colin does this with a team of three total. This is a significant claim about the leverage of the approach.

**Harmonization argument:** "If you can harmonize the upstream process with testing, finally testing is getting the respect it deserves. It's no longer just an add-on that we say, oh, we have to do this at the end, but it's a true part of the CI/CD process. If you can get that in harmony, then everything else becomes much faster and starts to iterate as a result."

**Growth dynamics:** "Usually with an organization, it's tough to get it started, but once it's started, generally speaking, the more projects you do, they're fairly aligned. Maybe it's the same tools, maybe it's the same stack, same standards. So once that initial pain is done, much easier as you go."

---

## 9. Playwright as Core Framework

Colin was emphatic about the Selenium-to-Playwright transition:

> "Moving from Selenium to Playwright. It'll be night and day."

> "Playwright, not that Selenium was a bad framework, but Selenium days you're used to sticking long delays and things, essentially. Things take forever because you have to wait. There's some uncertainty there. Playwright is so much better, and it works so much better for AI as well."

**Key advantages cited:**
- Eliminates the delay/wait problems endemic to Selenium
- Works significantly better with AI agents
- Microsoft-native (relevant for Azure environments)
- Supports mobile testing ("mobile testing, also it can be done with Playwright, so there's no difference there")
- Handles password-protected/authenticated flows ("even for things that are a little bit more strict, like for instance things that are password protected that you can't get behind, that's still fine")

**Ease of test generation:** "The Playwright side of it, writing those tests, I don't want to say it's easy, but it is the easiest part by far. Easy to the point where we have an agent that writes playbooks for everyone else to run, and it's that kind of easy."

**Azure alignment:** "If you're, for instance, like an Azure house where everything's on Microsoft Azure, perfect. Playwright is from Microsoft anyway. So there's very, very good visual understanding tools within Azure. So everything gets hosted there. All maintained in one place. IT department's happy with us. Cybersecurity's happy with us. We're not coming in with a separate tool or product. It's built on what the company already uses."

This is a deliberate positioning strategy: the approach uses the client's existing hyperscaler stack, not a separate product. "Analogs are true for GCP and AWS too. Our approach is always going to be those kind of hyperscaler first."

---

## 10. Multi-Model Strategy

Colin described a pragmatic, best-tool-for-the-job approach to model selection:

> "Playwright is the secret sauce for the actual testing, even from the UI testing angle. Bringing that in with visual understanding models, that's where we usually have to mix from the grab bag a little bit with the models."

**Model allocation:**
- **Claude: ~90% of usage.** "We love Claude. We use Claude for about 90% of things."
- **Gemini: Visual understanding.** "Gemini tends to do a lot better job with visual understanding."
- **OpenAI: Minimal.** "Very few with OpenAI, but that's a different story."

> "We don't have to pick. So, you know, some agents are using Claude, some are with Gemini."

**Agent-checking-agent pattern:** "The best thing is that you can have agents check on other agents, too. So even when the agents are messing up, you don't have to waste a human's time to go and look at this and say, that was junk."

**Practical example of visual understanding benefit:** "Co-honor those days where you're doing some UI testing and a button position moves, then the test fails. It was just because it relocated. We should visually understand that enough." (Note: "Co-honor" is likely a transcription error -- Colin is saying something like "Gone are those days" or "Remember those days.")

---

## 11. Agent Evaluation Framework

This was one of the longest and most detailed sections of Colin's presentation. He described a human-centric evaluation philosophy.

### 11.1 Evaluate Agents Like People

> "The best way, even whenever you're trying to think of like what an agent should do, because that's one of my favorite interview questions to ask people -- how do you decide when to split into two agents? What's that trade-off point? The answer is just like people."

> "Even with scoring or evaluating AI, how do we as people look at other people, and how do we assess if I trust you to do this? And it's the same thing. If you take those ideas, put them in a bottle, and feed them to AI, or feed them to the system that governs AI."

### 11.2 Agents Should Not Assess Themselves or Each Other

> "The trick is to not let an agent ever assess itself. And it's also true to not have an agent assess another agent. They have this very oscillating behavior where they either go very, very, very overwhelmingly positive, everything's perfect all the time, or polar opposite, everything's awful all the time. It's not good."

This is a strong claim: agent self-evaluation and peer-evaluation are fundamentally unreliable. The solution is human-defined KPIs.

> "Having clear KPIs almost like you would for a person that are there for an agent to matter."

### 11.3 The Person Analogy for Reliability Scoring

Colin gave a vivid example:

> "I know this person, I assign them a task, I assign them every time on Friday. They say they'll have it done for me next Wednesday. It has never been done on next Wednesday. It's always the next week, maybe. Well, what would you give them in terms of a reliability score? It's the same kind of question to ask an agent."

### 11.4 Proportional Response to Mistakes

> "A lot of the times I've seen, 99% of everything's perfect, and then that one mistake happens, and it's like, oh, the agent's awful. Technically, yes, but technically not, just like it was a person. What would we do if it was a person? Hopefully pull them aside and say, here's what happened. So what do we do in that for an agent? Well, we give them better instructions for the next time. We improve the tools. This is always an iterative process, always."

### 11.5 No Out-of-the-Box Solution Exists

> "There's no out-of-the-box solution. If I do it, if OpenAI does it, if Anthropic does it, there's no out-of-the-box solution. It's going to be 100% or even close, ready to go. But the trick is to evaluate them like you evaluate people."

---

## 12. Confidence and Reinforcement Learning from Human Feedback

Colin described the confidence-building mechanism in detail:

### 12.1 The Mechanism

> "How we do it, it's very, very simple. It goes like this. At first, humans have to be in the loop a lot. But humans, this is essentially reinforcement learning in a much simpler way."

> "When we say confidence, all that really means is that the agent has done a good thing repeatedly, consistently, a number of times. And the human has given a green light for those number of times. We can set a threshold as to whatever you'd like."

**What confidence means concretely:**
- Agent performs an action
- Human reviews and approves (or rejects)
- Repeated successful approvals build a pattern library
- "That means that the agent has some positive reinforcement to know that this is a good pattern, and it has reference to those patterns, so it's kind of how it can look back at its notes before it goes and approaches a new problem."
- Same mechanism works in the negative direction

### 12.2 Human-in-the-Loop Threshold Decreasing Over Time

> "After that goes on, at a certain point, human doesn't need to be in the loop anymore. And the human only needs to come into the loop whenever that agent makes a mistake again to say, why was this?"

The human involvement follows a curve: heavy at first, decreasing as trust builds, with re-engagement triggered by failures.

### 12.3 Why Humans Must Stay for Course Correction

> "That's something that technically, yes, you could have an agent resolve within itself, but should you? Probably not, because it's not going to be able to course correct. They tend to simplify. They tend to go off-road. You still want a human expertise and insight to say, that wasn't right. Here's what we should be doing instead."

**Key claim:** Agents "tend to simplify" and "tend to go off-road" when attempting self-correction. Human expertise is structurally necessary for course corrections, not just a nice-to-have.

### 12.4 Optional Periodic Human Review

> "Some people like to have more control, so they'll even have human, just like we would do if we were to fine-tuning a model, you'd have a human check that output periodically."

### 12.5 The Chef Analogy

Colin described the evolution of the human role:

> "You almost transition from a sous chef or a line chef to the master executive chef for the kitchen. You're walking around tasting everyone else's stuff. You're not actually cooking yourself. That's a good place to be."

---

## 13. Observability and Transparency ("Harness Engineering")

Colin emphasized this as a commonly missed element:

> "The transparency side, observability. That's something that gets missed. How is my team doing? And not just how's my team doing, but how are my agents doing?"

He referenced the term "harness engineering" with some skepticism about industry terminology:

> "I think there's this new silly term harness engineering. I always roll my eyes at these. It's a new term every conference that happens. Every time there's an NVIDIA GTC, new terms."

**But the substance matters:** "Where it matters for you is, do the agents do what you want them to do? If they're flagging things, why?"

### 13.1 Mature System Edge Case Analysis

> "After the system's mature enough, it's really, really interesting to see what those edge cases are. Is this because it's being too strict? Is it because we're wrong? We're trying to do this testing, and it is fundamentally something wrong with what we're doing. What are those actual reasons why things fail after the system is stable?"

### 13.2 Traceability

> "For agentic systems, having that kind of observability of them, what's going on all the time, so that it's traceable, is really, really important, especially for testing. Because if some error occurs over here and it should have been caught upstream, why didn't we catch that?"

### 13.3 Upstream-Downstream Error Sync

> "That kind of a loop to have those two things in sync with each other is all part of this kind of -- I don't want to say autonomous system, but system autonomy, more so. So the system can organically keep itself fed in with new information as time goes."

---

## 14. "System Autonomy" vs. "Autonomous Systems"

Colin made a deliberate terminological distinction:

> "I don't want to say autonomous system, but system autonomy, more so."

The difference: An "autonomous system" implies a monolithic agent operating independently. "System autonomy" implies a system of components (deterministic + agentic + human) that collectively achieves autonomous behavior while remaining traceable and governable. The autonomy is a property of the system's design, not of any individual agent.

---

## 15. Computer Vision PhD Stat (Consistency Argument)

Colin used a specific statistic to argue for the consistency advantage of automated systems:

> "There's a funny thing in computer vision that comes. I love this stat. Professional PhD researchers given computer vision task to label, is this a giraffe or is this a car? The best of the best is 92%. Giraffe versus a car. Why? Because they're given 10,000 images to label and people get lazy. And people eventually start going..."

The point: Even for trivially easy tasks, human consistency degrades at scale. The "best of the best" (PhD-level computer vision researchers) top out at 92% accuracy on a task that should be near-100%. The failure is not intelligence -- it is attention and consistency.

> "With agents, with automated or deterministic systems, the consistency angle to them, if you allow that to happen..."

This directly supports the "97% plus" target: agents can exceed human consistency on repetitive tasks, provided the framework supports it.

---

## 16. Human Augmentation, Not Replacement

Colin explicitly positioned his approach as augmentation:

> "From my standpoint, I'm not here to take anyone's job away. More so, say, we can't do anything in the QA/QE space without that kind of very tribal knowledge that is there."

> "Instead of you saying, I'm going to get replaced, say, I can do now the work of 20 people, because I have access to these tools, and I can use them well. And I know how to refine them because I'm an expert in the space."

> "For me, it's not about just saying everyone gets gone and now it's an agent team. More so is a very collaborative approach with them."

He added a caveat: "That's my internal view anyway, but I won't tell anyone else how to do their thing."

---

## 17. Statefulness of Testing and Throwaway Work

Colin identified a core challenge in QA/QE automation:

> "The trick is to do it at scale. And especially because with testing in QA/QE, you have effectively a moving target. There's a statefulness to testing. And that's where I think we can definitely help the most so that there is a lot of throwaway work. It has to be because what happens when the code changes, you no longer need those tests or maybe they need refreshed or something."

The state graph and CI/CD integration directly address this: they make the "throwaway" intelligent rather than wasteful by knowing which tests are affected by which changes.

---

## 18. ADA Compliance and Persona-Based Testing

Colin mentioned a specific testing use case involving agent identity:

> "Even from the QA perspective, you can give an identity to an agent, even if you're doing ADA compliance testing. Here are the strict requirements for this specific compliance, and maybe there's also a persona that you give to an agent."

This suggests agents can be given both technical requirements (ADA compliance rules) and user personas to simulate how different types of users would interact with the application. "And it works very well with Playwright."

---

## 19. Framework Maturity Threshold

Colin mentioned a maturity bar for tools:

> "There's a certain, even for us internally, there's a certain threshold that must be met for maturity of tool to be able to use it. I'm not a version 0.3 type. 1.0, I need this to have crossed its path into this."

This is relevant for Sephora, who may be evaluating various tools: BayOne's approach requires production-grade tooling, not beta experiments.

---

## 20. Business Outcome Focus

Colin pushed back against technology-driven goals:

> "Don't focus on the buzzword part of the outcome. Focus on the real business outcome that you want. So is your goal to get to 100% agentic QA/QE? No. Your goal is to get to the velocity and the quality that you want. The rest is just secondary."

> "If there was a magic rock that fell from space and said, oh, plug this into the process and everything works perfectly, you wouldn't even care about AI anymore."

> "The outcome drives. Don't let the mechanism of the outcome drive what you want the outcome to be."

---

## 21. Framework as the Growth Bottleneck

Colin made a diagnostic claim about when progress plateaus:

> "The framework has to be there in order to support that growth, or else it will kind of get capped out. If you ever see a cap forming, that's because of the framework, not because of the models. It's just like us with people."

If improvement flatlines, the problem is structural (the framework), not the AI models themselves. This is a significant assertion -- it means investing in framework quality (the deterministic layer, the state graph, the feedback loops) yields more than investing in better models.

---

## 22. Vaibhav's Response and Alignment Points

Vaibhav (Sephora QE lead) responded positively and echoed several of Colin's themes:

### 22.1 Trust as the Central Challenge

> "It's very difficult to gauge at this point of time because it is a lot of human in the loop in order to even increase that trust confidence from 60 to 80 percent -- it's a big step initially. You'll say 40-50 percent, agents are doing great work, but that 50 to 60 jump will come after you've thoroughly reviewed what your agents are doing and slowly you develop more trust."

> "I'm right now in my thought process trying to build that process of establishing trust."

### 22.2 Quality Umbrella Expansion

> "Quality is no longer output driven. Quality is there in every different realm of SDLC. Quality of the stories that are created, quality of the code, not the bugs and all, but just the quality, testing, quality of testing, and quality of deployment, everything is under me in terms of quality umbrella."

> "My job is becoming tougher because I was just testing code. Now I'm being asked to test every single outcome of every single phase."

### 22.3 Trust Index Problem

Vaibhav described the scoring challenge from his side:

> "To incorporate that together and then come up with a trust index and yeah look we are good 4.8 out of 5. How do you compute 4.8? I don't know."

This is the exact problem Colin's reinforcement-learning-from-human-feedback approach addresses.

### 22.4 Common Knowledge Base Initiative

Vaibhav described a parallel initiative at Sephora:

> "One other big initiative that we're currently working is establishing a common knowledge base, which is something that every single function can work out of."

He gave a specific example of why siloed knowledge bases fail:

> "We were capturing as part of QE and we were capturing meeting minutes or whiteboard drawings, making it part of the knowledge base, while other agent had no clue about some discussion that happened. So the development was not based on the newly created design, but we were testing out of that design."

The insight: "If the dev agent knows how the QE agent is going to test the code, then that expectation will be built into the development itself. The testing improves and vice versa."

---

## 23. Sephora Context (Relevant to QE Approach)

Several details from Vaibhav's introduction provide context for how BayOne's approach would fit:

- **Migration from Selenium to Playwright:** Already in progress. "We've done all POCs and new automation development using Playwright." Aligns perfectly with Colin's Playwright-first position.
- **AMP model (Agentic Micro Pod):** Sephora is moving from regular pod structure to AMP -- "a very lean team working on very, very small enhancements, small and frequent enhancements, which basically means that you're churning code on a very regular basis and that demands equally stronger fast-paced testing as well."
- **QE COE team:** Led by Deepika, ~5 people. Small team with a roadmap that maps to what Vaibhav described.
- **Platform stack:** Azure-based ("Microsoft Cloud Platform in Azure"). This is the perfect fit for Playwright (Microsoft-native) as Colin noted.
- **Tool evolution:** Started with Copilot, then Claude via Avent platform, now building homegrown system called "Nova" based on LiteLLM.
- **Gaps Vaibhav identified:** Visual QA, translations/localization testing, ADA compliance testing, mobile farms.

---

## Open Questions and Unresolved Points

1. **State graph implementation details:** Colin described the concept but did not detail the specific tooling or technology used to generate the state graph. How is the autonomous exploration implemented? What format does the state graph take?

2. **"Two other people" -- who?** Colin said he does this with two other people. Their roles and expertise were not specified in this conversation.

3. **Cost model for UI testing at scale:** Colin mentioned this can be "heavy in terms of cost" depending on implementation (screenshot processing, visual understanding tokens), and said "that can also be optimized." The optimization details were not discussed.

4. **Specific metrics for the 97% target:** What exactly is measured at 97%? Test pass rate? Coverage percentage? Agent accuracy on test generation? This was stated as a target but not precisely defined.

5. **Deepika's hire status:** There was discussion about whether Deepika had filled her agentic QE role. Status was unclear at the time of the meeting. BayOne had sent candidates; budget and rate concerns (around $120/hr for onsite) were mentioned.

6. **Integration with Sephora's Nova platform:** No discussion of how BayOne's framework would integrate with or complement Sephora's homegrown Nova system.

7. **MCP requirement:** Vaibhav mentioned "anything that we are touching needs to have an MCP server" for workflow integration. Colin did not address this directly in the QE discussion.

8. **Confidence threshold specifics:** Colin said "we can set a threshold as to whatever you'd like" for the reinforcement learning mechanism, but did not describe default thresholds or how they have calibrated these in practice.

---

## Summary of BayOne QE Methodology (Synthesis)

Colin's approach can be decomposed into a layered architecture:

**Layer 1 (Deterministic Foundation):**
- Autonomous codebase exploration producing a state graph
- Dependency mapping, dead code detection, vulnerability scanning
- Unit test standards definition

**Layer 2 (Integration):**
- State graph plugged into CI/CD pipelines
- File-change-to-test-target mapping
- Recursive downstream dependency coverage model

**Layer 3 (Agentic):**
- Playwright-based test generation and execution
- Multi-model strategy (Claude ~90%, Gemini for visual, minimal OpenAI)
- Agent-checking-agent patterns
- Persona-based and compliance-aware testing

**Layer 4 (Evaluation and Learning):**
- Human-in-the-loop reinforcement (RLHF-style, simplified)
- Confidence built through repeated human-approved successes
- Edge case feedback loop into central framework
- Decreasing human involvement threshold over time

**Layer 5 (Observability):**
- Traceable agent behavior ("harness engineering")
- Mature-system edge case analysis
- Upstream-downstream error correlation
- Human-vs-agent parity measurement

**Governing Principles:**
- "System autonomy" not "autonomous systems"
- Evaluate agents like people
- Never let agents self-assess or peer-assess
- Business outcomes drive, not technology
- Framework quality determines the ceiling, not model quality
- 97%+ target, not 80%
- Three-person team delivers this (high leverage)
