# Speaker Notes: Meeting 2 (Rama)

Quick reference for who said what.

---

## Rama (Test Manager, Nexus Dashboard)

### On the Problem Scale

> "We will have almost 30,000, 40,000 test suites or test cases on every day, daily basis."

> "25,000 for one [group]... like you have six other groups everybody running it's almost 60,000 tests being run."

> "Almost 10 engineers are looking into, or 12 engineers are looking into each line, each day."

### On Analysis Pain

> "Running is okay. Running, yes, we can build so many equipment and repeat the test and everything. Analysis is the key thing. That is where the time is spent."

> "The results will begin. But the result somebody needs to analyze and say, hey, why they are fit, why the quality is bad, and provide the subjective analysis. That's where engineers are spending time."

> "If they're failed, if the high percentage failed, then they go cranky, right? Oh, I need to look and find analysis for everything."

### On What AI Could Do

> "If there is some AI tool which can look into the results, okay, this is the part, it is impacting these many, 2000 test cases. Right away it came to a point, rather than manual, spending manual analysis."

> "So if the tools are there, it is more effective. It saves the time. And teams can spend time on the complex ones."

### On Op-Ex

> "Regression analysis is one of the costly functions. Where our op-ex is being a little bit overspent, we want to manage it better or use that bandwidth to develop automation or do something else."

### On Selective Regression

> "Yes, that is the selective regression. We call SRT, selective regression testing. This is based on the code changes what you make."

### On UI Automation Pressure

> "Milesh is asking me... they said, Rama, you need to move the needle on the UI automation, right? Now, everything is API based... But UI also very important."

> "UAE [UI automation] is not impossible, but it is a more laborious work."

### On UI Change Impact

> "For example, they made one change, simple change on the UI, certainly it required me almost 4,000 scripts I have to modify."

### On Theme Changes

> "Previously used to have a black and white... Now they are changing everything is the black. Same thing, UI screens also... then what happens is most of our scripts we need to re-validate."

### On Correlation Complexity

> "How you correlate, there is... you are using three different products to the three different entities and one entity... that symptom is being reflected on the UI."

### On the Relationship to Arun's Work

> "Arun Kumar's work is network product validations... switches. Your switches has its own functionality... the functional conformance."

> "For me, it's different. Nexus Dashboard is a little different. My intention is to send, kick in that CLI... My job will be done, that's it. As long as I kick in that CLI, I don't care whether these people are doing the same job or not."

### Closing

> "Sure. We will look forward. Looking forward to it as well."

---

## Colin Moore (BayOne)

### On Test Selection (Probing)

> "Usually one of the bottlenecks that we could solve, but it doesn't sound like it's a problem, is even just the selection of the test suites. What to run? You have all these tests to run. Do you need to run that many?"

### On Failure Hierarchy

> "Sometimes it's a repeat error that's flagged, but it was already covered by this up here. It's kind of just noise at that point. If you fix this one, it fixes the downstream."

> "On the other hand, sometimes you have ones that are more... edge cases among themselves, where this is happening because this one, so there's a dependency more than there's a hierarchy."

### On Graph Topology Solution

> "One thing that we do to start out that work is we build essentially a graph topology of the space... something that's multi-dimensional."

> "Here's the relationship, here's my entire code base. Here's the relationships that files have amongst each other. Maybe it's a library. So if I want to see what files a library touches... How do I know what impact that will have?"

> "The trick to it is to not do it ad hoc. So for us, what we do is we'll preserve that, and it's state-aware. So whenever the code changes, the graph changes."

> "If you have this graph and it's live updating as the code changes, even if it's on a specific developer's branch, because 90% of the graph is the same, now you can say, because this changed, here are the ones that are relevant."

### On Crossover with CI/CD Project

> "This is actually good, because this is part of what we're doing already for Arun's team."

> "There's also work that we aren't actively doing right now that we propose to Nilesha's group... about code-based modernization... for unit test generation and coverage."

### On Demo Offer

> "For that second and third use case, that's a fun one we can actually demo to you. So we've got some really cool [solutions], because I know it's kind of brittle, almost. There's always a testing. It's brittle to do UX, UI testing."

### On Next Steps

> "If we came back and we had some ideas to share, I can always do that."

> "We know a little bit now about Cisco's stack and the internal ways to do this. So [solutions will] already have that informed in there."

---

## Rahul Bobbili (BayOne Delivery)

### Facilitating Introduction

> "If you're available, we'll get you connected to our AI person."

> "He's Colin. I don't want to take it around, so that's why I said, let's speak offline."

### Setting Context

> "So, the thing is probably they're trying to take help of AI to automate because they have higher resources back in India to do this regression testing."

> "They wanted to understand, to see how AI can help them out."

### Checking Understanding

> "Probably, he got the thing, right? He can recommend something once he analyzes it."

---

## Sentiment Summary

**Rama:** Practical, data-driven, clearly frustrated with analysis burden but optimistic about AI solutions. Appreciated Colin's technical depth ("I got what you mentioned").

**Colin:** Technically engaged, immediately saw crossover with existing work. Offered concrete solutions rather than vague promises.

**Rahul:** Effective facilitator, made the introduction happen organically during the site visit.
