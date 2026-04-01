# 02 - Meeting: AI in Professional Services

**Source:** /masterminds/source/meeting1_3_1_2026/meeting1.txt
**Source Date:** 2026-03-01 (Kickoff Meeting)
**Document Set:** 02 (First Masterminds Meeting)
**Pass:** Focused deep dive on AI discussion, tools, concerns, and legislation

---

## 1. How the AI Discussion Emerged

The AI topic surfaced organically during the group's discussion of what each member hopes to accomplish through the mastermind. Zac (Saunders) identified AI as a topic of interest across the group's disciplines. Colin (Moore) had already been introduced as "Director of AI for BayOne Solutions," and his presence made AI a natural focal point. The discussion then cascaded through multiple speakers, each contributing their own experiences, fears, and use cases before converging on PII concerns and legislation.

---

## 2. Zac Saunders: Confluence's AI Committee and Zox

### AI Committee at Confluence

Zac disclosed that Confluence Financial has established a formal internal AI focus committee. He described it as separate from their Investment Advisory Committee (which already uses AI for data analytics). Key details:

- **Committee members:** Zac stated he is on it "with Gregory Weimer and four other associates" -- six people total.
- **Gregory Weimer** is one of the two co-founders of Confluence (the other being Jim Wilding).
- **Purpose:** "What we're looking at is how can we help make our associates' jobs more efficient."
- **Scope of inquiry:** They are evaluating software that could integrate with their existing technology stack. Zac specifically named **Salesforce** (CRM), **Black Diamond** (portfolio reporting / custodian platform), and unspecified custodians as systems they are looking at for potential AI integration.
- **Posture:** Exploratory but cautious. Not yet deploying broadly. Evaluating what is available and whether it fits within their existing workflows.

### Zox: Voice-to-Text Meeting Summarization

Zac described a specific tool the firm is close to adopting:

- **Tool name:** Zox (transcribed as "Zox" -- likely the product name; may also be "Zocks" or similar given speech-to-text ambiguity).
- **Category:** AI voice-to-text summarization tool, specifically designed for the financial services industry.
- **Key distinction:** "It's not an audio recording" -- Zac emphasized this. The tool converts speech to text in real time but does not retain audio recordings.
- **Client authorization required:** "The client has to give authorization. Hey, is it okay if we record our review meeting today?" Zac framed this as a consent-based process, noting explicitly that they explain to the client it is not audio recording.
- **Template-based output:** "If I give it a template in the tool, it'll then summarize everything." Zac described providing category headers such as "estate planning, tax items, financial plan, portfolio" and the tool synthesizes the conversation and recommendations into those categories.
- **Time savings:** "Instead of me spending an hour and a half post-meeting, people were spending like 25 minutes post-meeting to do their summaries." This is a reduction from approximately 90 minutes to 25 minutes of post-meeting administrative work.
- **Current adoption:** "Two colleagues currently use it" at Confluence. The broader firm has not yet rolled it out.
- **Acknowledged limitations:** "Sometimes it's too much information" -- Zac noted that the tool can over-generate content, requiring the advisor to edit down.
- **Business case framing:** Zac connected the productivity gain to capacity: "If a typical advisor, let's just say they serve 125 households, by utilizing technology to be more productive, maybe they can service 150 households." He linked this to revenue growth and margin improvement.

### Zac's AI Posture

**Pragmatic and cautiously enthusiastic.** Zac is personally engaged (sits on the AI committee, is evaluating tools), but his language is measured. He frames AI in terms of productivity and efficiency, not transformation. He is highly sensitive to PII risks (see Section 6 below). He explicitly said he looks forward to Colin's guidance on the AI topic.

---

## 3. Ryan Brody: Lexis Nexis AI and Claude for Personal Productivity

### Lexis Nexis AI in Legal Practice

Ryan provided the most detailed account of AI use in a specific professional tool:

- **Platform:** Lexis Nexis (referred to as "Lexus Nexus" in transcript -- standard speech-to-text error for the legal research platform LexisNexis).
- **Capabilities Ryan described:**
  - Real-time case law aggregation: "It pulls every single case around the country into their software."
  - AI-powered legal research: "You can have it do research for you."
  - AI-generated briefs: "You can have it write briefs for you."
  - AI-generated pleadings: "You can have it write pleadings for you."
- **Ryan's assessment:** He acknowledged the capabilities but immediately pivoted to the risks.

### Lawyers Getting Disciplined for Unchecked AI Output

Ryan described a pattern of professional discipline across the legal profession:

- "We get these disciplinary newsletters from all over the country."
- "Lawyers everywhere are getting in huge trouble by judges and stuff like that because they're submitting things without checking sites."
- **Specific failure mode:** "They're submitting pleadings with bad law, with stuff that it..." (trails off). The clear implication is that AI-generated legal documents contain fabricated case citations or incorrect legal reasoning, and lawyers are submitting them to courts without verification.
- Ryan characterized the current state of legal AI as: "There's a lot of miss. There's a lot of areas. There's a lot of -- it's clunky."

### Where AI Works Well (Ryan's Experience)

Despite the risks, Ryan identified specific patterns where AI performs well:

- **Document analysis with constrained scope:** "If you upload a document and say hey, give me ten takeaways, it's unbelievable." Zac agreed with this from the financial side.
- **Closed-circuit tasks:** "You give it sort of like a closed circuit type thing where it's not scouring the internet for a zillion different things, it's great with that."
- **Generative tasks with parameters:** "I've given it tasks. Create me something with these parameters and it spits you out something pretty workable and nicely."
- **Bad at open-ended factual work:** Both Ryan and Zac agreed: "It's bad at math. It's bad at looking at case law sometimes."

### Claude for Outlook and Coding Tasks

Ryan disclosed personal use of Claude (Anthropic's AI assistant):

- "I was trying to just play with Claude, just trying to get it to... and it gave me all these different steps, codes to put in for Outlook and all these different things."
- **Context:** Ryan was trying to build efficiency tools or automation for his practice, using Claude to generate code or configuration steps for Microsoft Outlook.
- This is notable as a direct mention of Claude by name as a tool in active personal use by a group member.

### Ryan's AI Posture

**Pragmatic and clear-eyed.** Ryan is not fearful but is acutely aware of the professional risks. He frames AI as inevitable ("It's going to move into the legal world more and more") but anchors his confidence in the irreplaceability of human judgment: "The family wants to work with a trusted attorney." He explicitly stated: "I'm not terrified of it. I think that people were terrified of the printing press. They were terrified of the computer, the internet, and we can just learn how to work beside it to make ourselves better. It's not as scary as what we all think."

---

## 4. Derek Aller: Policy Review AI Experiments and Wife's AI Use at Blank Rome

### AI for Insurance Policy Reviews (Failure Case)

Derek described an active attempt to use AI for insurance work that encountered accuracy problems:

- **Use case:** Using AI to perform policy reviews on smaller commercial accounts.
- **Method:** "We've been trying to incorporate it for smaller business to do policy reviews, and even though we're uploading it and including the entire policy, there's still some errors that are located within."
- **Business rationale:** "If it's a $5,000 premium account, you don't want your account manager spending an hour and a half reviewing a renewal whenever you have a $250,000 account renewing in the next couple of days." The goal was to triage lower-value work so human attention could focus on high-value accounts.
- **Outcome:** Not yet reliable enough for production use. Derek described it as "something that we would love for it to be utilized on a daily basis" -- implying it is not yet there.
- **Proofreading experience:** "I use it to proofread some emails, and it's like... I'm proofreading the proofread. Sometimes I'm like, that's not -- I can't have it say that because that's not how this policy reacts." The AI fails to understand insurance-specific language and policy mechanics.

### Wife's AI Use at Blank Rome (Success Case)

Derek provided a secondhand but detailed account of successful AI use in large law firm litigation:

- **Person:** Derek's wife, a legal project manager at **Blank Rome** (transcribed as "Blank Roam" -- this is the law firm Blank Rome LLP).
- **Her background:** Has an informational science minor from Duquesne University.
- **Use case:** She "utilizes it to help create client-facing portals" and has been "empowered to do the coding and everything for that."
- **Context:** Large litigation cases. Derek gave an example (without confirming specifics, noting "she doesn't tell me that stuff") of something like "a shell pollution case" with "a reserve of a hundred million dollars on the case."
- **What the portal does:** Allows clients to "go on, check in, and really go -- this partner and these associates worked 10 hours last week on it." It provides litigation spending transparency and case tracking.
- **Assessment:** Derek described it as "really cool" and noted the firm has empowered her to use AI for this purpose -- suggesting institutional buy-in at Blank Rome for AI-assisted development.

### Derek's AI Posture

**Enthusiastic but encountering friction.** Derek wants AI to work for his business (the policy review use case shows genuine effort to integrate it), but has hit real accuracy problems. He is honest about the limitations. He frames his relationship with AI through the lens of fear management: "I think having you [Colin] kind of talk us off the ledge every once in a while." He acknowledged the natural human fear response: "There's a level of ignorance. We just naturally fear something immediately."

---

## 5. Colin Moore: AI Framing, Philosophy, and Offer to Advise

### AI as a Tool, Not a Replacement

Colin delivered the most sustained philosophical framing of AI in the meeting. Key statements, closely paraphrased:

- **On hype vs. reality:** "This whole news pitch that it's the super intelligent, sentient, terminator thing -- complete fabrication for marketing hype, because otherwise how do you get those really nice contracts? If not everyone believes that the world's going to change tomorrow... it's been years and what do you see? Has this great replacement actually started? No."
- **On post-COVID job losses attributed to AI:** "I think there was some clearing of the driftwood that was going to happen anyway after COVID, but that was all that it was. It wasn't machines taking over, taking people's jobs."
- **On the 60/40 split:** "I find about 60% of my job is the mundane, the things that I have to do -- like have to show up to meetings, maybe each meeting adding value, but they're like the boring things. And then the remaining 40% is the actual creative value-added stuff that something else can't do. And that's straight up with AI at the same time. You want AI to come in and do all the boring stuff for you so you can focus on the really good stuff."
- **Specific mundane examples:** "You shouldn't have to focus on summarizing after meetings or putting reports together or even just keeping your schedule intact. That's stuff that we can offload."
- **On replacement:** "You'll never hear me saying people are going to get replaced by AI. I think people that fail to adapt to it will, in the same way that there's no one that lights gas lamps on the streets anymore. So that's not a scary thing. That's a natural technological evolution."

### On Hallucination and Misinformation

Colin directly addressed the hallucination concern that had been raised:

- "People like to say hallucination. I'm like, have you used Google?"
- "People act like this is a spouting dragon over here. And I'm like, it was the same thing."
- **Historical comparison:** "I remember, decade, we even had library class to learn how to look for misinformation or how to cite sources. People still weren't doing that. We can blame it all we want. That was still happening. Now it's just easier for it to happen and more visible because it's a hype topic."
- **On the lawyer discipline cases:** "No one would have even cared to hear about that if that was 20 years ago. They would have been like, that's weird. I probably shouldn't do that. But now it's a hype topic."
- **On human responsibility:** "People are always going to skip steps or be lazy. That's not necessarily the AI's fault."

### Colin's Offer to Advise on Safe Tools

When the PII discussion arose, Colin made a direct offer to the group:

- "I can at least help by telling you which ones are okay and which ones aren't. Because there's some that aren't. There's some that are okay."
- He referenced people with the opposite mindset: "There's other ones that I'm like, people... exactly the opposite of the mindset here. It's like, 'who would even read it anyway?' And I'm like..." (trails off, implying that attitude is dangerous).

### Colin's Framing of AI Consulting Market

Colin also described the broader AI consulting landscape:

- "Consulting solutions, AI in general, we are very hammer-looking-for-nail. Like, that's just how it is."
- "You probably see that if you have LinkedIn, you go to messages and there's 300 guys trying to pitch you, and they pull a percentage number out of nowhere."
- "AI is probably the most BS-prone of a field that's going on right now."
- He positioned himself as a counterweight: "The good thing is I can also help to keep that on track. So if there's questions about it, what's coming up, what's really going on, not just what's in the news or what am I reading."

### Colin's AI Posture

**Informed advocate with grounded skepticism of hype.** Colin is the most technically immersed member of the group. He is enthusiastic about AI's potential but actively works to deflate hype and ground expectations. He frames AI as a productivity tool, not a transformative force, and is sensitive to the fear it generates in other professionals. He positions himself as a resource for the group on both the opportunity and risk sides.

---

## 6. PII Concerns: The Enterprise vs. Consumer Tool Discussion

This was a distinct segment of the AI discussion, initiated by Zac and joined by multiple speakers.

### Zac's Concern

Zac raised the PII issue directly:

- "One area that we're sensitive in terms of artificial intelligence, whether it's Copilot, ChatGPT, Gemini, any of those things, Claude, is personally identifiable information."
- **Enterprise vs. consumer distinction:** "Unless it's an enterprise system, generally speaking. And I use that term loosely because you know what that means." He then admitted uncertainty: "I don't know what that means. I know it's enterprise within the organization. Everything is contained."
- **Current practice at Confluence:** "But there's even a sense of cautious internally with us of putting any PII information that's even in the enterprise system until we fully understand what this really works."
- **How they use AI now:** "When we do use it, usually just general information. There's no client stuff that we're putting in there. It's just mostly general... theoretical."
- **Example of safe usage:** "Like, what do you think I should do about that? And it's like, oh, you should reference this. Okay, I already got that part."

### Tools Named in the PII Context

Zac explicitly named the following AI tools as ones where PII sensitivity applies:

1. **Microsoft Copilot**
2. **ChatGPT** (OpenAI)
3. **Gemini** (Google)
4. **Claude** (Anthropic)

### Derek's Agreement

Derek affirmed the same posture: "I'm with you on it, so I'm terrified of putting... Yeah, I don't want to put people's info in there."

### Colin's Offer to Differentiate Safe Tools

Colin responded to the PII concern with a practical offer:

- "I can at least help by telling you which ones are okay and which ones aren't."
- He warned about a cavalier attitude he has seen elsewhere: people with "exactly the opposite of the mindset" who dismiss PII risks.
- He then made a half-joking but pointed referral: "I think there's some people in this room that would love to talk to you a little bit later when you need an attorney, because the fines for this are getting heavier and heavier."

### Implicit Action Item

Colin's offer to advise the group on which AI tools are safe for PII constitutes an informal action item. No formal follow-up was scheduled during the meeting, but the offer was clearly received and acknowledged.

---

## 7. Legislation and Compliance Discussion

Colin transitioned directly from the PII discussion into a broader framing of AI regulation and compliance.

### Specific Frameworks and Standards Named

Colin named the following:

1. **SOC 2** -- Service Organization Control 2, the compliance framework for service providers managing customer data. Colin referenced it as something "that is going to come into effect, has already come into effect to start to govern" AI usage.
2. **ISO 42001** -- The international standard for AI management systems (published 2023). Colin named it explicitly in the context of emerging AI governance frameworks.
3. **ISO 27001** -- The international standard for information security management systems. Colin paired it with ISO 42001, noting both apply "for IT and for systems and stuff."

### Colin's Framing of the Regulatory Landscape

- **Pace of change:** "That is something that you always hear people say, it's changing so fast. Absolutely the legislation side of AI is changing."
- **Opportunity framing:** "Where it's fun is that's a lot of opportunity on the table because people are panicking. You have large corporations, small ones, I'm sure, the same that are rushing to say, hey, we just did this thing. Is that okay?"
- **Practical value of AI for compliance itself:** "This new legislation came out, how do I understand 5,000 pages of legislation? Easy, we can do that." (Referring to using AI to parse and summarize regulatory documents.)
- **Forward-looking framing:** Colin connected the legislation discussion to the group's future planning: "It's also a good place to even share for that, as you were saying in the beginning, the future plan. What this looks like as we go forward in the 2030s. What is changing? How will that affect big, small business?"
- **General principle behind regulation:** "Usually it's fairly standard across the board. It's basically don't be evil with the things that come up. People complain about them because that's why it makes life a little bit harder. You have another hoop to jump through. But at the end of the day, it's a very good thing to be aware of so you can feel confident using the tools."
- **Ferrari metaphor:** "It's like a throttle limiter on a Ferrari. You want to know how far you can go until that needle ticks red. So that's where you want to stay out of."

---

## 8. OpenAI / Anthropic / Pentagon News Discussion

A brief but notable exchange occurred about recent AI industry news, initiated by Derek:

- **Derek's reference:** "The recent, you know, the Anthropic and the Department of Defense news is wild."
- **Correction in conversation:** Someone asked "Did they switch or something?" and Colin (or another speaker) clarified it was **OpenAI**, not Anthropic: "So they switched to ChatGPT and then ChatGPT basically got snowballed or sandbagged by people almost immediately."
- **Specific data points cited:**
  - "750% increase in uninstalls" (for ChatGPT)
  - "250-something percent decrease in downloads" (for ChatGPT)
  - The cause: OpenAI "signed something with the Pentagon that said we're allowed to spy on Americans."
- **Group reaction:** The speaker characterized public reaction as predictable: "Who would have thought that that would be unpopular?"
- **Commentary on OpenAI's positioning:** "For all their profit -- puts out there like, yeah, we're not going to -- white knight -- stay. Oh, don't worry, we will." This is a garbled transcript of someone criticizing OpenAI's shift from its original nonprofit, safety-first positioning to a profit-driven stance that now includes defense contracts.

### Significance

This exchange reveals the group's awareness of AI industry dynamics beyond just tool usage. The OpenAI/Pentagon story was used as a trust signal -- reinforcing Zac's PII concerns and validating the group's cautious approach to which AI vendors to trust with sensitive data.

---

## 9. The "Fear vs. Tool" Framing Across Speakers

Multiple speakers contributed to a recurring theme of AI fear versus AI as a practical tool. This was not a single discussion but a thread woven throughout:

| Speaker | Statement (closely paraphrased) | Posture |
|---------|-------------------------------|---------|
| **Zac** | "I'm not being naive to say it's going to replace me, but the really great advisors that use it as a tool to make me more productive or provide growth... people are still going to want judgment, counsel, advice." | Pragmatic |
| **Ryan** | "I'm not terrified of it. People were terrified of the printing press. They were terrified of the computer, the internet, and we can just learn how to work beside it." | Historically grounded, calm |
| **Ryan** | "Everyone's pretty terrified of it. But I still think that the family wants to work with a trusted attorney." | Acknowledges industry fear, rejects it personally |
| **Derek** | "There is like a fear because it's just like anything else. There's a level of ignorance. We just naturally fear something immediately." | Self-aware about the fear response |
| **Derek** | "Having you [Colin] kind of talk us off the ledge every once in a while." | Values Colin as a stabilizing voice |
| **Colin** | "I always tell people it's a tool. It's just a tool. This whole news pitch that it's the super intelligent, sentient, terminator thing -- complete fabrication for marketing hype." | Dismissive of existential AI fears |
| **Colin** | "You'll never hear me saying people are going to get replaced by AI. I think people that fail to adapt to it will." | Nuanced -- not replacement, but adaptation pressure |
| **Colin** | "Be cautious, be grounded, and not to be scared, but to be informed about it." | Prescriptive -- information over fear |

### Consensus Position

The group reached an informal consensus: AI is a tool, not a threat, but must be used carefully. No one in the room expressed unqualified enthusiasm or unqualified fear. The dominant posture was **pragmatic caution with openness to adoption**, anchored by Colin's technical grounding.

---

## 10. Complete Tool and Platform Inventory

| Tool / Platform | Mentioned By | Context |
|----------------|-------------|---------|
| **Zox** | Zac | Voice-to-text meeting summarization for financial services; under evaluation at Confluence |
| **LexisNexis** (AI features) | Ryan | Legal research, brief writing, pleading writing; in active use at his firm |
| **Claude** (Anthropic) | Ryan, Zac | Ryan: personal use for Outlook/coding tasks. Zac: named in PII concern list |
| **ChatGPT** (OpenAI) | Multiple | Named in PII concern; referenced in Pentagon/DoD news discussion |
| **Microsoft Copilot** | Zac | Named in PII concern list |
| **Google Gemini** | Zac | Named in PII concern list |
| **Salesforce** | Zac | Existing CRM at Confluence; potential AI integration target |
| **Black Diamond** | Zac | Portfolio/custodian platform at Confluence; potential AI integration target |

---

## 11. Summary of Each Member's AI Posture

| Member | Role | AI Posture | Key Detail |
|--------|------|-----------|------------|
| **Zac Saunders** | Wealth Manager, Confluence | Pragmatic, cautiously enthusiastic | On AI committee; evaluating Zox; highly sensitive to PII |
| **Ryan Brody** | Estate Attorney, Strasburg McKenna | Pragmatic, historically grounded | Uses LexisNexis AI and Claude; aware of discipline risks; not fearful |
| **Derek Aller** | Insurance Broker, Simpson McCrady | Enthusiastic but encountering friction | Tried AI for policy reviews (accuracy issues); wife successfully uses AI at Blank Rome |
| **Colin Moore** | Director of AI, BayOne Solutions | Informed advocate, hype-deflator | Frames AI as tool; offers to advise on safe tools; knowledgeable on legislation |
| **Phil Sardis** | CPA, own firm | Listener on AI topic | Did not contribute AI-specific commentary; no posture discernible |

---

## 12. Action Items and Offers (AI-Specific)

1. **Colin offered to advise the group on which AI tools are safe for PII.** No formal follow-up scheduled, but the offer was acknowledged and well-received.
2. **Zac's AI committee at Confluence** is an ongoing initiative; future updates to the group are likely as their evaluation of Zox and other tools progresses.
3. **AI as a recurring topic** was implicitly agreed upon. Zac noted he "wrote that down" as one of the group's focus areas. Colin's presence ensures it will be a standing topic.
4. **Legislation and compliance** was flagged by Colin as a future discussion area -- "what this looks like as we go forward in the 2030s."
