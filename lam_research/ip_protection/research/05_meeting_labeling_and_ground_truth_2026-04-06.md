# 05 - Meeting: Labeling and Ground Truth

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Focused deep dive on labeling, ground truth, and data requirements

---

## Overview

The labeling and ground truth discussion was one of the longest and most technically engaged portions of the entire meeting. It began when Colin asked about the "golden set" used in LAM's prior attempt, and it triggered an extended exchange in which Brad asked for more technical depth than on any other topic. The discussion covered why the prior attempt stalled, how labeling actually works in practice, how much data is needed, and whether AI can help create the labeling set. Mikhail was candid about what went wrong, Colin was direct about the consequences, and Brad pushed for concrete specifics throughout.

---

## 1. Colin Introduces the Golden Set Concept

Colin framed the question by explaining the fundamental dependency between training data quality and model output quality. He asked the LAM team what their golden set looked like, using the terms "known good" and "known bad":

> "Whenever we say like training a model... typically we talk about there's the golden set. You know, these are the known good or the known bad, and here's why they're good, here's why they're bad. It's in a way it's labeling, and you can't do training unless you have that... But for any training or even any testing to happen, you have to have some kind of a data set in order to test it out. So what did that look like? What were you using for the kind of the golden set? And what were you looking at for the negative side?"

This was a deliberate and careful setup. Colin was establishing the principle that model accuracy is bounded by training data quality before asking what LAM actually had.

---

## 2. Mikhail's Admission: No Golden Set Existed

Mikhail's response was direct and revealing. He gave three parts to the answer, but the critical admission came first:

> "So there's three answers to that. So we didn't have a golden set because we were told -- or at least I was told -- that we have to do the labeling to create that set."

He then immediately qualified: "Right, wrong, and different. I'm just telling you that." This framing made clear that Mikhail understood this was a problem, but that it was the guidance he received at the time. He was not defensive about it -- he was straightforward that this is what happened and acknowledged it may have been wrong.

What they did instead of a golden set:

- LAM has a list of close to 3,000 acronyms. They filtered out customer-related acronyms and created an exclusion list ("this is totally fine").
- They loaded a list of customer names.
- They loaded a list of FAB locations.

These three lists were the entirety of what the models had to work with. Mikhail explicitly stated: "We didn't create the true golden set that you talked about because what... was communicated, we actually have to take the text and we have to go through the labeling effort, and that would be our golden set. So we're just loading kind of independent things that we have."

---

## 3. Colin's Response: This Fundamentally Limited Their Ceiling

Colin was direct about the consequence, framing it as the probable root cause of the 21% false positive rate:

> "So in that case, that's probably where you hit most of the wall, if I'm being honest, because for that... the output limit of your model is limited to the accuracy of whatever you gave it, and if that's a small set, or if it's not labeled, you're proportionally limited as to what the accuracy of that system can be."

He then stated the principle in its strongest form:

> "You have to have known good, known bad, or else what patterns does the model have to learn at the end of the day. And if you only provide one half of that set, you're still limited. There's a ceiling that you can get because effectively you're blind to what bad looks like. For instance, if you only provide no good. Or you're blind to what okay looks like if you only know what bad looks like."

This was the core technical diagnosis of what went wrong with the prior attempt. Without a properly labeled set containing both positive and negative examples, the models had no reliable basis for learning the distinction between sensitive and non-sensitive content. The acronym lists and customer name lists they loaded amounted to rule-based inputs, not training data.

Colin also made a point of saying that the data set they had "probably only legitimately lends itself to being suitable for a rule-based approach, to be honest." This was a carefully placed observation -- it validated what LAM tried while explaining why it could not have worked for ML or GenAI.

---

## 4. Colin Reframes What Labeling Actually Means

A significant moment in the discussion was Colin correcting the mental model of what labeling entails. He identified that LAM had been thinking about labeling in terms of the most labor-intensive version -- comparable to image annotation in computer vision:

> "Labeling doesn't always have to mean, I think the labeling, you know, in this case, I think it was being talked about more like what we were talking about for computer vision, which is image, tag, human being has to sit there and waste their time."

He reframed it as "bucketing" at a higher level:

> "But for the most part, whenever we're saying otherwise, we're talking about bucketing. Bucketing just as a higher level, you know, this document in general is good. This document in general is not good or known to have some kind of problem with it."

He emphasized that it does not have to be a large effort: "That doesn't have to be a big thing, so it depends upon how you do it." This was important because Mikhail had earlier mentioned that the labeling effort was estimated at over 1,000 man-hours, which was cost-prohibitive. Colin was signaling that the approach they were told to follow was unnecessarily heavy.

---

## 5. Brad Requests More Technical Detail

Brad explicitly asked for deeper technical specifics. This was the point where he moved from listening mode to active engagement on the labeling topic:

> "That's probably more technical than you want to answer for that. Well, actually, I do want a little bit more technical answers. I'm actually more specifically about this good bet, right?"

Brad then grounded the question in their specific context:

> "We use the five fields, right, to see if this fab ID and the customer name is present. And we do, we actually still do have already a UI, which actually gives you a thumbs up, thumbs down if the system is doing it properly or not. So the extension of is it true or not, it's already built in."

This was significant because Brad revealed that they already have an evaluation mechanism in place -- a UI with thumbs up/thumbs down feedback. He then asked the core quantitative question:

> "How much of that data do we have to go through? So I'm not talking 140 page documents, I'm talking five fields. What statistically significant amount of effort would we need to go through? A thousand five fields, so like five thousand total fields, or we talk in tens of thousands, like what are we really talking here?"

---

## 6. Colin's Answer: The Giraffe and Car Analogy for Data Separability

Colin answered Brad's quantitative question by explaining that there is no fixed number -- it depends on data separability. He used the giraffe/car analogy:

> "So let's say, for instance, you're showing someone a picture of a giraffe in a car. Very obvious to say which one's which. And if you were to give them another picture, you could very clearly say which is which. The reason why you don't need as many examples in that case is because you have good distinction, good separation between those two groups of good versus bad."

He then explained the inverse:

> "But whenever you have two things that are very close to each other, the more close they are, the more samples you need to recognize patterns."

He then gave the 20,000 benchmark for the hardest cases:

> "Generally speaking, if things are very close to each other, a good benchmark to kind of put yourself out is at least 20,000 samples is usually where we stay at. But that is not really a meaningful number because it truly depends upon what you're talking about. Is it giraffes and cars? It's way easier for me to separate. But if it's, let's say, a picture of the front and back of a quarter, that's way more similar to each other, so I need more images."

---

## 7. EDA as the Method to Determine Sample Sufficiency

Colin explained that the way to determine the actual required sample size is through Exploratory Data Analysis (EDA):

> "That's something that we can do with exploratory data analysis before we start a project. We would look at all the available information and see how similar it is to one another. The more similar it is, statistically, the more samples I need in order to generate meaningful co-relationships and patterns that can be derived out. If they're completely different things or if they're easily distinguishable, then I need less."

Later, when asked directly whether the existing ~1,000 thumbs up/thumbs down examples would suffice, Colin circled back to EDA as the definitive method:

> "If we take that, we can do then that statistical analysis that's just an exploratory data analysis, which is to say, how similar is the data among the classes? How consistent is it within one class? And then we can say, is this enough, or is this going to be something that's not enough based on what happens? But that's something we can tell you with certainty from EDA."

This was a critical point -- Colin committed that EDA would produce a definitive answer about data sufficiency, not guesswork.

---

## 8. Techniques to Reduce Labeling Burden

Colin offered multiple techniques to reduce the human labeling effort:

### Auto-Categorization

> "Certainly there's ways to automate that process as well... It takes me usually less than a day to build something that can do this auto categorization with some human in the loop aspect to it."

He repeated this later: "We can help you. Like I said earlier, it takes me usually less than a day to build something that can do this auto categorization with some human in the loop aspect to it."

### Generating Synthetic Known-Bad

> "There's other techniques that we have that can even take existing content and generate known bad from the bad already, so we can improve that set and limit the amount of human labeling that's actually needed."

### Rule-Based Flagging to Reduce Scope

> "There's also things that can be added in from a rule-based approach so that you don't have to have as many. Because sometimes there's little things that flag that I can look for... to generate more samples."

### Human-AI Agreement Loop (Production Sampling)

Colin described how even large-scale model training (he referenced Gemini specifically) uses a sampling approach analogous to manufacturing quality control:

> "If you had a product line with a thousand pieces coming off a minute, what are you going to do? Can you check each and every piece? Well, maybe, depending upon what the product is. But more generally speaking, people are going to take and down-sample from that. Let's say just do every, you know, if there's a thousand parts a minute, check every hundredth part and see if those ones are okay."

He explained that this human-AI agreement monitoring helps speed up labeling over time: "Until there's an alarm bell ringing saying human and AI are agreeing or are seeing the same, then you can proceed that way. That helps to speed up labeling, for sure, but you can't start out that way. You have to build that approach and build that trust."

---

## 9. The Three-Tier Labeling Framework

Brad asked a sharp follow-up question that drew out the most detailed technical explanation of the session:

> "When you say this good or bad data, does it help flag the entire thing? Or does it help flag contextually the actual violating text?"

Colin responded with a three-tier framework:

### Tier 1: Word Level, No Context

> "Tier one is just the -- let's say the word itself. And as you correctly said, it doesn't have context. So you might end up with a lot of false positives there."

This is the simplest labeling: flagging individual words or tokens without any surrounding document context. It is the least effort but produces the highest false positive rate because there is no way to distinguish between a sensitive mention and a benign one.

### Tier 2: Word Plus Document Context, No Human Explanation

> "Tier 2 is to say this text plus the document that contained it. Nothing else. No human labeling, no explanation as to why. But that does give more context because you're saying this word was a problem within this document context. What that context is, up for the model to figure out."

Colin described this as the most accessible tier in practice: "Usually that category two is the most accessible because you'll know usually what the file name was at the bare minimum and what the thing was flagged. If I have those two, I can access that document. As long as those documents are accessible, we can usually get enough out of that contextually speaking in order to help aid training."

### Tier 3: Word Plus Document Plus Human Reasoning

> "Tier 3 is where you actually are giving some kind of a human judgment call. This text was bad in this document because of this."

Colin described this as: "The most work, but by far the most valuable, especially for language model training."

---

## 10. Mikhail Confirms: Their Prior Approach Jumped Straight to Tier 3

The three-tier framework immediately clarified what went wrong with LAM's prior labeling approach. Mikhail connected the dots:

> "And that's what our problem was. One for number 3, right off the bat."

Colin confirmed that this was backward: "Right, right. Yeah, usually number 2 first, and then within number 2, you subset of that to get number 3."

Mikhail then stated their preference going forward: "We'd be definitely one for first." This indicated that the LAM team understood the framework and wanted to start at the appropriate entry point rather than repeating the mistake of attempting the most labor-intensive approach first.

The 1,000+ man-hour labeling estimate that Mikhail had described earlier now had clear context -- LAM had been told they needed Tier 3 labeling (human judgment annotations on every example) as the prerequisite for creating a golden set, which was cost-prohibitive and caused the entire effort to stall.

---

## 11. Brad's Question: Can AI Help Create the Labeling Set?

Brad raised the question of whether AI itself could be used to bootstrap the labeled data set:

> "I almost think that there is some type of -- and I'm just going to use the general AI -- in this case, AI tool to help create this set."

This came after Saurav mentioned that post-training techniques (like the existing thumbs up/thumbs down UI) could be leveraged.

### Colin's Nuanced Answer on Ground Truth

Colin addressed this carefully by establishing the fundamental constraint of ground truth:

> "So fundamentally ground truth, AI cannot say that AI is correct. Not possible. You can train a model to have a certain accuracy... It's like the telephone game. Any model that's trained downstream from that can only then therefore be a ceiling of 97%. It's never possible that it could exceed that. And when I say 97... it's not even close to that usually. That's probably closer to that 80%. You know, past 20% false positives that you're seeing. That's what I mean."

He then explained how AI can eventually help, but with constraints:

> "You can eventually have an AI help, but even with that we have a lot of different techniques that we would employ to do that at scale."

He used the manufacturing sampling analogy to explain how human-AI collaboration works: the AI and human review the same samples, and as long as they agree, the AI's contributions can be trusted. But you cannot start with AI doing the labeling -- you have to build that trust first through verified agreement.

The key principle Colin established: the accuracy of any downstream model is bounded by the accuracy of whatever labeled it. If an AI with 80% accuracy creates your training set, your model's ceiling is 80%. Ground truth must originate from human verification.

---

## 12. Mikhail's Intuition About Rule-Based Combination Flagging

Brad also shared an intuition about using rules to detect combinations of sensitive elements, which Mikhail had been developing:

> "If you have like customer name on itself, it's not such a bad thing if there's nothing else with it. If you have fab ID, it's probably fine. Once you start to stick things together is where you start to get into the issue, right?"

He suggested a practical approach:

> "I think even having some type of rule around, hey, if any of these show up in any combination of a new or a three or something like that, you gotta flag it as there's something wrong... you could almost run it against some type of rule set or something."

Colin validated this: "You're correct. I think that's exactly right on that."

This intuition aligned precisely with the layered architecture Colin would present later in the meeting -- using deterministic rule-based approaches as the first layer to flag suspicious content before passing it to more expensive AI models for contextual judgment.

---

## 13. Post-Training and RLHF-Style Feedback Loops

Saurav introduced the concept of post-training and RLHF-style feedback loops, connecting them to the existing thumbs up/thumbs down UI:

> "The trainings have improved in the last few years. They are now, earlier it used to be just training of data, labeling and all. Now they're calling it pre-training, post-training. So for example, this thumbs up and down, which is already there that you mentioned in your UI, it's kind of an aspect of the post-training where you can improve on it, and you can utilize that thumbs up, thumbs down, and we can put it in the right way of the ML side."

This positioned the existing evaluation UI as not just a validation tool, but as a potential source of ongoing training signal -- a continuous improvement loop rather than a one-time labeling effort. The implication was that LAM already has the infrastructure for this kind of feedback mechanism; it just needs to be connected to the right training pipeline.

---

## 14. The Existing ~1,000 Examples

Brad and Mikhail confirmed that they already have approximately 1,000 thumbs up/thumbs down evaluations from their existing UI:

> Brad: "We still have a tool to do this thumbs up, thumbs down. To me, even those five fields, I would treat them as the same thing, right? Because it's just five text fields. So I think we have about a thousand."

When asked whether this would suffice, Colin deferred to EDA (see Section 7) rather than giving a premature yes or no. He did acknowledge that the existing data is valuable but that sufficiency depends on the statistical properties of the data itself.

Saurav reinforced that the quantity is not a fixed threshold: "It's not a pre-pose. It's a continuous loop. It's just the more you have, the better your data is."

---

## 15. Contradictions in Source Data

Colin raised an additional concern about ground truth reliability -- the possibility that the labeled data itself might contain contradictions:

> "Let's say you do have a document that's been approved, 140 pages or something. If it's contradictory, was something that was said to be bad... there's content that was flagged as bad over here, but it's still present in a good document. That's something we can find out, too. Because that is probably the most common case where the source of truth itself isn't very truthful. And so improving that fundamentally increases the entire baseline of the system."

He described this as "a pretty easy exercise to do," suggesting it would be one of the early activities in any engagement.

---

## Summary of Key Findings from This Section

| Finding | Detail |
|---|---|
| **Root cause of prior failure** | No golden set existed. The team was told they needed full Tier 3 labeling (1,000+ man-hours) to create one, which was cost-prohibitive, so they never created it. |
| **What they used instead** | Three lookup lists: acronym exclusions, customer names, FAB locations. These were rule-based inputs, not labeled training data. |
| **Consequence** | Model accuracy was fundamentally bounded by the input quality. The 21% false positive rate was a direct result. |
| **Colin's diagnosis** | The data set they had "probably only legitimately lends itself to being suitable for a rule-based approach." |
| **Three-tier framework** | Tier 1 (word only), Tier 2 (word + document context), Tier 3 (word + document + human reasoning). LAM jumped to Tier 3 and stalled. |
| **Recommended starting point** | Tier 1 first, then Tier 2 with subsetting to Tier 3 as needed. |
| **Existing assets** | ~1,000 thumbs up/thumbs down evaluations from existing UI. |
| **Data sufficiency method** | EDA determines required sample size based on class separability. |
| **20,000 sample benchmark** | Applies only when data is highly similar between classes. Less similar data needs fewer samples. |
| **Ground truth principle** | AI cannot validate AI. Downstream model accuracy is bounded by the accuracy of whatever created its training set. |
| **Labeling burden reduction** | Auto-categorization tools (less than a day to build), synthetic known-bad generation, rule-based flagging, human-AI agreement loops. |
| **Combination flagging** | Brad/Mikhail's intuition that individual elements are benign but combinations are sensitive aligns with Colin's layered architecture. |
| **Post-training signal** | Existing thumbs up/thumbs down UI can serve as RLHF-style continuous feedback loop. |
