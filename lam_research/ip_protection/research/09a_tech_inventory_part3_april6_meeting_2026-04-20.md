# 09a - Technology Inventory Part 3: April 6 Client Meeting (Brad/Mikhail/Daniel)

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (second client meeting)
**Document Set:** 09a (supplementary to Set 09)
**Pass:** Complete extraction of every technology/tool/platform/system mention from this dense client meeting

---

## 1. Compute / Hosting / Infrastructure

- **Kubernetes (on-prem)** (transcribed normally as "Kubernetes"). Mikhail described deployment topology for the prior 18-month effort.
  - Who: Mikhail
  - Context: Lam's internal deployment platform for the prior NER/redaction effort. All selected models were deployed to on-prem Kubernetes except for the Azure AI model.
  - Near-quote (line 75-76): "we initially launched them on the Kubernetes. We didn't even put them anywhere, like we use... anything in a cloud, so to speak, right? We deployed them on Prime and Kubernetes and so forth, while we're evaluating. Azure I, I think that was the only one we didn't, obviously, do that."

- **On-prem servers / "On-Prem" hosting**
  - Who: Mikhail, Colin, Daniel
  - Context: Mikhail's definition of on-prem is "running on the server at our data center versus being on cloud" (line 155). Colin discussed on-prem scenarios (healthcare, ITAR/military, FedRAMP).
  - Near-quote (line 151-152): "the only time I'm ever going to recommend on-prem is in two scenarios exclusively. One, if you're in healthcare or manufacturing... The second is from a security compliance, if there's anything ITAR or military related..."

- **Azure (cloud)** (transcribed as "Asher"/"Azure")
  - Who: Mikhail, Colin
  - Context: Colin asked if Lam has access to deploy on Azure for the POC. Mikhail confirmed they still have access to the prior-project Azure environment (not fully spun down).
  - Near-quote (line 148): "It's Azure, right? So by the way, from the last project, we've only partially spun down the old environment, so we still have access to it"

- **Disconnected / Air-gapped environments (customer fab deployments)**
  - Who: Daniel, Mikhail
  - Context: Daniel raised semi-connected / offline / disconnected-environment possibilities for future. Mikhail clarified this as the "disconnected" case (fab-specific deployments). Out of scope for POC.
  - Near-quote (line 156-157): "to me on-prem is not a disconnect... That's FAP specific deployments. That's direct FAP specific. That is not in scope right now."

- **Edge AI / Edge devices**
  - Who: Daniel
  - Context: Daniel talked about small language models and Edge AI for customer fabs.
  - Near-quote (line 150): "when you say on premises, I have a different definition for that when I think about our customer fads and Edge AI and small language models."

- **Customer clean room / customer fab (customer-resident environments)**
  - Who: Daniel, Brad
  - Context: Clean room explicitly excluded from the current use case (line 27). Daniel referenced approval process with the customer for data exiting clean room.
  - Near-quote (line 154): "Depending on how that data is getting captured in the customer clean room, we can actually go through an approval process with the customer in their data out policy prior to ingestion getting into the enterprise."

- **Hybrid cloud setup**
  - Who: Colin
  - Context: Colin offered to share thoughts on Azure vs. on-prem vs. hybrid setup for the POC.
  - Near-quote (line 147): "I can certainly share the thoughts on Azure versus on-prem versus a hybrid setup"

- **Hyperscalers (general cloud)**
  - Who: Colin
  - Context: Mentioned generically alongside cloud options.
  - Near-quote (line 161): "then you have cloud-based, which is going to use one of the hyperscalers."

- **Lam data center (internal)**
  - Who: Mikhail
  - Context: Mikhail's definition of on-prem = "running on the server at our data center."
  - Line 155.

- **Prior-project environment (still partially running)**
  - Who: Mikhail
  - Context: Old environment from the 18-month effort; hourly data retrieval jobs disabled but environment still up.
  - Near-quote (line 148-149): "we still have access to it, please. Some of, I don't know if we stand on full envelope side of things, but audit aid stuff is all up and running where actually we just disabled the hourly jobs and that's it."

---

## 2. Data Storage / Databases / Data Lakes

- **Structured and unstructured data in Escalation Solver**
  - Who: Mikhail
  - Context: Application contains both structured and unstructured data, plus free-text fields and attachments.
  - Near-quote (line 40): "Inside there there's some I think structured and unstructured data and information and people can type in free text and income so forth you can have attachments"

- **Attachments (document data within Escalation Solver)**
  - Who: Mikhail
  - Context: Attached to escalation records; treated as a future/extended capability for redaction within documents.
  - Near-quote (line 44): "doing reduction within documents that's I'm not I'm gonna say that's the key that's another capability for the future"

- **Hourly data retrieval jobs**
  - Who: Mikhail
  - Context: Batch/ETL jobs that previously extracted data from source systems into the NER environment for evaluation.
  - Near-quote (line 149): "they have data, hourly data retrieval jobs that could get data out of the system"

- **Tool data / recipe / yield data (fab-resident data categories)**
  - Who: Daniel
  - Context: Daniel described sensitive IP categories in the fab (recipe, yield data) vs. shareable tool data.
  - Near-quote (line 158): "If you prove to the customer that you don't have the recipe, their yield data, very sensitive IIP stuff that's been cleansed, that you're just taking the tool data that can be shared."

- **Tool file (structured fab data)**
  - Who: Daniel
  - Context: Referenced as structured data inside the fab. Used as an example of data that is easily segregated without ML.
  - Near-quote (line 160): "if it's structured inside of let's say tool file that that's what we will call the structured data that is easily segregateable elements"

- None additional mentioned (no specific database vendors like SQL Server, Oracle, PostgreSQL, Snowflake, Databricks named).

---

## 3. Programming Languages / Runtimes

- **Python**
  - Who: Colin
  - Context: Cited as example for a simple rule-based/regex script.
  - Near-quote (line 174): "absolutely you can do it with Regex. It's a simple Python script, right?"

- No explicit .NET / JavaScript / Java mention in this transcript. Daniel did not name his team's stack here.

---

## 4. NLP / NER Libraries / Frameworks

- **spaCy** (transcribed as "spacey"/"spaCy")
  - Who: Mikhail (confirmed by Colin as an NLP model)
  - Context: One of the libraries the Lam team actually tried in the prior 18-month effort.
  - Near-quote (line 185): "I think I've mentioned this before right if you have like customer name..." [context]; (line 188): "I mean, it was spacey, it was..." — Mikhail listing what Lam tried.
  - Colin (line 185): "so when you said hugging face, and that's a small language model, and then transformers, like in our case, spaCy, that's an NLP model? That's correct, that's correct."

- **Presidio** (Microsoft PII framework)
  - Who: Mikhail
  - Context: Starting point for the prior effort. Lam began model evaluation "with Presidio models."
  - Near-quote (line 51): "So we started first, now going back to your answer, we started with Presidio models. We took about 12 models on Microsoft."

- **Hugging Face Transformers library / "transformers"** (see also #5)
  - Who: Mikhail
  - Context: One of the three finalist models in the prior effort. Colin noted that Transformers is the architectural backbone for nearly everything except IBM models; likely they used sentence-transformers.
  - Near-quote (line 52): "so transformers, which one from hugging face flare, and I mean, I can look it up, but there were one more."
  - Colin (line 188): "probably what you try was sentence Transformers, if I had to guess, as well."

- **Flair (NLP library)** (transcribed as "flare")
  - Who: Mikhail
  - Context: One of the three finalist models selected. Mikhail explicitly named it later: "we did pick one of the hugging face, right? I remember Flair was the one that we picked" (line 155).
  - Near-quote (line 52): "so transformers, which one from hugging face flare"

- **Sentence Transformers**
  - Who: Colin
  - Context: Colin suggested as what Lam likely used. Also referenced as a possible on-prem-hostable NLP option.
  - Near-quote (line 181): "something like sentence transformers as well"
  - Near-quote (line 188): "probably what you try was sentence Transformers, if I had to guess"

- **TF-IDF** (transcribed correctly)
  - Who: Colin
  - Context: Example of a classic NLP technique usable cheaply/on-prem.
  - Near-quote (line 181): "things like TFIDF, for example. You can use these to your advantage so that you save in terms of speed and as well as cost."

- **Regex / rule-based pattern matching**
  - Who: Colin
  - Context: First layer of the recommended "deterministic" stack.
  - Near-quote (line 174): "if you are using something that has a Regex capability, absolutely you can do it with Regex. It's a simple Python script"

- None other named (no NLTK, Stanza, Stanford NER explicitly mentioned).

---

## 5. Machine Learning / Deep Learning Frameworks

- **Hugging Face** (platform + library ecosystem, often conflated with Transformers)
  - Who: Mikhail, Colin
  - Context: Mikhail identified one of the three finalist models as coming from Hugging Face. Colin stated he's "a big proponent of hugging face. I contribute all the time on hugging face" (line 153).
  - Near-quote (line 52): "which one from hugging face flare"
  - Near-quote (line 153): "I love them. I'm a big proponent of hugging face. I contribute all the time on hugging face."

- **Transformers (architecture)**
  - Who: Colin
  - Context: Architectural backbone of modern models.
  - Near-quote (line 188): "Transformers is the architecture that is the backbone for pretty much everything except for the IBM models."

- **Mixture of Experts (MoE) — Mistral MoE**
  - Who: Colin
  - Context: Colin identified Lam's prior "run all three models in parallel and reconcile" pattern as a modified take on Mixture of Experts; references Mistral MoE as the hot architecture 18 months ago.
  - Near-quote (line 182): "That's a modified take on mixture of experts, which is probably if it's 18 months ago, that was the hot architecture of that time with Mistral MOE."

- No explicit PyTorch / TensorFlow / scikit-learn / ONNX mention in this transcript.

---

## 6. Pre-trained Models / LLMs / Specific Model Names

- **"12 models on Microsoft" (from Presidio / Microsoft ecosystem) narrowed to 5, then to 3**
  - Who: Mikhail
  - Context: The 12-to-5-to-3 model down-selection process Mikhail ran.
  - Near-quote (line 51): "We took about 12 models on Microsoft. We've looked at them. We narrowed down to three. We narrowed down to five and then to three."

- **The three finalist models (before swap):**
  1. A Transformers model (unnamed specific)
  2. A Hugging Face / Flair model (Flair was the pick)
  3. A third that Mikhail could not recall on the call ("I'm just not going to come to me right now")
  - Near-quote (line 52-54): "so transformers, which one from hugging face flare, and I mean, I can look it up, but there were one more... Then I think it was Transformers and it was... I'm just not going to come to me right now for whatever reason."

- **Revised final three (after swap):**
  - One Presidio-family model was dropped and **Azure AI (an Azure-hosted model)** was added.
  - Near-quote (line 53): "we actually narrowed it down to three, then removed one and added Azure AI. That's one of the Azure models."

- **GPT-4.0 / ChatGPT models** (transcribed as "GPD 4.0")
  - Who: Colin
  - Context: Colin asked why Lam didn't use the standard large models at the time; notes GPT-4.0 was the standard then.
  - Near-quote (line 71-72): "like, at that point, it would have been GPD 4.0? Is there a reason for that?"
  - Azure AI Foundry "has access to things like, for instance, the newest GPT models from chat GPT" (line 71).

- **Claude / Anthropic models**
  - Who: Colin
  - Context: Mentioned as among the "newest cloud models" available through Azure AI Foundry; also referenced generically as an enterprise LLM provider.
  - Near-quote (line 71): "the newest cloud models, pretty much everything except for Gemini"
  - Near-quote (line 62): "each of these large language models and any of these enterprise solutions based on Antropic or OpenAI or any of the others"

- **OpenAI models**
  - Who: Colin
  - Context: Cited as enterprise LLM option; Azure OpenAI mentioned as the early name for Azure AI Foundry.
  - Near-quote (line 70): "it started out Azure opening I Then it moved to Azure AI then now most recently its Azure AI foundry"
  - Near-quote (line 62): "Antropic or OpenAI or any of the others"

- **Gemini (Google)**
  - Who: Colin
  - Context: Explicitly the one LLM Azure AI Foundry does NOT have access to. Colin also cited personal awareness of Gemini training.
  - Near-quote (line 71): "pretty much everything except for Gemini"
  - Near-quote (line 100): "I'll bring up Gemini training that's something I'm very aware of personally"

- **IBM models**
  - Who: Colin
  - Context: Called out as the exception to "Transformers-backbone" models.
  - Near-quote (line 188): "Transformers is the architecture that is the backbone for pretty much everything except for the IBM models."

- **Small Language Models (SLMs)**
  - Who: Daniel, Colin
  - Context: Daniel wants to keep SLM/Edge compatibility open for future. Colin pushed back — SLMs only make sense on-prem / air-gapped.
  - Near-quote (line 152-153): "There's no actual reason to use small language models unless you're doing on-prem. They're actually more expensive to run on cloud infrastructure... unless there's a real business reason that you guys tell us, hey, we need to use SLMs... I'm probably not going to even look at them in their direction."

- **BERT / RoBERTa** — NOT explicitly named in this transcript.
- **LamGPT** — NOT confirmed in this transcript (no explicit "LamGPT" mention found).

---

## 7. Generative AI Services / APIs

- **Azure OpenAI** (old name)
  - Who: Colin
  - Context: Original name for Azure AI Foundry before two renames.
  - Near-quote (line 70): "it started out Azure opening I Then it moved to Azure AI"

- **Azure AI / Azure AI Foundry**
  - Who: Mikhail (uses "Azure AI"), Colin (clarifies Foundry)
  - Context: The platform Lam used for the Azure-hosted model in their finalist set. Colin calls it the current name.
  - Near-quote (line 70): "now most recently its Azure AI foundry"
  - Near-quote (line 62): "We used Azure AI as the primary"
  - Near-quote (line 148): deployment target option; (line 150) "AI Foundry has compatibility with Edge AI and these small language models."

- **Anthropic API**
  - Who: Colin
  - Context: Named as enterprise LLM option.
  - Near-quote (line 62): "based on Antropic or OpenAI or any of the others"

- **OpenAI API**
  - Who: Colin
  - Context: Same reference.
  - Near-quote (line 62): "based on Antropic or OpenAI or any of the others"

- **ChatGPT / GPT models**
  - Who: Colin
  - Context: "newest GPT models from chat GPT" accessible via Azure AI Foundry (line 71).

- No AWS Bedrock, Google Vertex AI, or Cohere mentions in this transcript.

---

## 8. Application(s) Being Worked On

- **Escalation Solver** (Lam's homegrown escalation management application — POC target)
  - Who: Mikhail, Brad
  - Context: Primary target application for the POC. Homegrown, has own security, contains structured + unstructured data, supports attachments, troubleshooting, closure reports, follow-up actions (design changes, procedure changes, tech articles).
  - Near-quote (line 40-41): "we have an escalation system. It's a platform... it's homegrown built. There's got some security built into it and so forth ASM which is applications security manager with switch which manages some of the people in the profiles"
  - Near-quote (line 46): "Application name is escalation solver."
  - Near-quote (line 41-42): workflow: field engineer on install/maintenance/upgrade → work order; if unresolved in 8 hours → escalation petition.

- **Redaction Service (standalone)**
  - Who: Mikhail
  - Context: Lam built the prior NER work as a standalone service independent of any application, callable for detection or redaction.
  - Near-quote (line 50-51): "We've actually built this as a standalone service. We did not build it into the application... call it a reduction service, you can just pass in and get detection or you pass in and you get redacted text back as well."

- **Thumbs-up/thumbs-down labeling UI**
  - Who: Mikhail
  - Context: Existing UI that already captures human validation ("is the system doing it properly or not"); produces ~1,000 labeled feedback points.
  - Near-quote (line 105): "we actually still do have already a UI, which actually gives you a thumbs up, thumbs down if the system is doing it properly or not."
  - Near-quote (line 166): "So I think we have about a thousand... Which is a thumbs up, thumbs down."

- **Self-help search / Q&A application (future use case)**
  - Who: Colin (recalling prior meeting)
  - Context: One of the two use-case families from previous discussion.
  - Near-quote (line 18-19): "one for something to help enable self-search and self-help search. That means... the Q&A side of things."

- **Field service technician escalation entry points (other applications beyond Escalation Solver)**
  - Who: Colin
  - Context: Second use-case family; any other competitor/tools with similar usage.
  - Near-quote (line 19).

---

## 9. Lam Internal Tools / Systems

- **ASM — Application Security Manager** (part of Escalation Solver security stack)
  - Who: Mikhail
  - Context: Lam's internal application security manager that manages user profiles in Escalation Solver.
  - Near-quote (line 40): "ASM which is applications security manager with switch which manages some of the people in the profiles"

- **Work order system / installed maintenance / upgrade workflow system**
  - Who: Mikhail
  - Context: Field engineer work-order process feeding into escalations.
  - Near-quote (line 42): "they're required to create a work order. And if they run into an issue and they can't solve it within eight hours, they're required to open up and escalate petition"

- **Engineering design change system / procedure change system / tech articles / follow-up actions**
  - Who: Mikhail
  - Context: Escalation closure reports can generate downstream actions into these systems.
  - Near-quote (line 41): "either engineering design changes, procedure changes, it could be tech articles, it could drive ongoing actions."

- **Lam acronym list** (~3,000 acronyms)
  - Who: Mikhail
  - Context: Exclusion list loaded into the NER pipeline.
  - Near-quote (line 80): "LAMP has a list of acronyms. We went through exercise to create a list of acronyms, and then from close to 3,000"

- **Customer list** (internal reference data)
  - Who: Mikhail
  - Context: Loaded as exclusion/reference data for detection.
  - Near-quote (line 80-81): "We loaded the list of customers."

- **Fab / location list**
  - Who: Mikhail
  - Context: Loaded as reference data.
  - Near-quote (line 81): "we loaded the list of FAPs, you know, whatever we had from a location."

- **MABC / "MA Data Center" — E10 data / "big EI project"**
  - Who: Mikhail
  - Context: Referenced as an existing Lam initiative handling data-out flows from the fab. ("Big EI project right now.")
  - Near-quote (line 157-158): "what you're talking about is like like MABC, right? Which is MA Data Center, getting the E10 data out. Right, because that's a big EI project right now."

- **Milux / Orion teams**
  - Who: Daniel, Brad/Mikhail
  - Context: Internal team names. Majority of the supporting IT capacity is with Milux Orion, currently committed to "COS" work.
  - Near-quote (line 202): "The majority of this outside of a Milux is Orion, so just FYI. They're working on COS"

- **COS** (internal project/system Orion is focused on)
  - Who: Daniel
  - Context: Named as a supercritical current project consuming Orion team capacity.
  - Line 202.

- **GSNO / GFSO** (Lam internal organization)
  - Who: Brad (self-introduced as "director of engineering in our GFSO area"), Mikhail (refers to "GSNO" — likely same transcription variant).
  - Context: Brad's org; also cross-functional involvement.
  - Near-quote (line 11): "I'm director of engineering in our GFSO area"
  - Near-quote (line 76-77): "this was done with the engineering, IT team, and the GSNO."

- **Knowledge and Advanced Services teams** (internal Lam group)
  - Who: Mikhail
  - Context: Part of the prior-project team.
  - Near-quote (line 77): "it wasn't just the Knowledge and Advanced Services teams, but we were driving the technology department."

- **JIRA / Confluence / ServiceNow** — NOT explicitly mentioned in this transcript (despite being common).

---

## 10. Identity / Access / Security Systems

- **LAM ID (Lam identity/credential)**
  - Who: Colin
  - Context: Colin notes everyone else on the call has a LAM ID; Colin does not, and will need one for access.
  - Near-quote (line 192): "everyone here but me has a LAM ID for things. But if we wanted to do things, that would also be something that would be a great thing to do early."

- **Application-level security (Escalation Solver profiles)**
  - Who: Mikhail
  - Context: ASM manages people/profiles within Escalation Solver.
  - Line 40.

- **NDAs and security evaluations (process)**
  - Who: Mikhail
  - Context: 18 months ago, evaluations of LLM vendors were ongoing.
  - Near-quote (line 73): "we were still going through NDAs and security evaluations of blood models and what services we were going to allow within our ecosystem."

- **SLW — Statement of Work paperwork process** (transcribed "SLW," probably "SOW")
  - Who: Brad
  - Context: Lam's legal/paperwork flow before engagement.
  - Near-quote (line 197-198): "there's gotta be an SLW put in place... That usually takes a week or so"

- No explicit Okta / Active Directory / SSO / VPN / MFA / Jason Callahan / zero-trust reference in this transcript.

---

## 11. Microsoft / Azure Ecosystem

- **Azure** — see Category 1.
- **Azure AI / Azure AI Foundry** — see Category 7.
- **Azure OpenAI** (former name) — see Category 7.

- **Microsoft Purview**
  - Who: Colin
  - Context: Cited as an enterprise-scale alternative to hand-built regex. "Imagine Regex at scale and distributed across applications."
  - Near-quote (line 174-176): "there's also enterprise tooling for that, like Microsoft Purview... Using things like Purview, which is essentially like imagine RidgeX at scale and distributed across applications is really helpful"

- **"Presidio" (Microsoft PII framework)** — see Category 4.

- **Microsoft (as LLM vendor)**
  - Who: Mikhail
  - Context: Named alongside Anthropic/OpenAI.
  - Near-quote (line 62): "any of the others, including Microsoft"

- No explicit SharePoint, Teams, M365, Power Platform, Azure DevOps mention in this transcript.

---

## 12. Third-Party Vendors / Consultants Mentioned

- **BayOne Solutions / "Bay One"**
  - Who: Colin (self-introduction)
  - Context: Colin is director of AI / head of AI at BayOne.
  - Near-quote (line 8): "I'm director of AI, head of AI here at Bay One."

- **Coherent Corporation** (Colin's prior employer, Santa Clara-based)
  - Who: Colin
  - Context: Colin cites a similar production system he built there running ~3 years.
  - Near-quote (line 8-10): "I came from Coherent Corporation, which is... down the road based in Santa Clara... That's a production system that's been running for, I think, about three years now."
  - Also line 184: Coherent reference: "at Coherent, this was something that 40,000 people are using every day. And that's something that also got deployed to aerospace and defense."

- **RoboFlow**
  - Who: Colin
  - Context: The one commercial labeling tool Colin endorses — for computer vision / manufacturing defect recognition.
  - Near-quote (line 144): "The only one that is, you know, contrary to that is in computer vision applications using something like RoboFlow. It's really, really helpful if you're doing manufacturing for defect recognition"

- **FedRAMP** (US government cloud certification)
  - Who: Colin
  - Context: Reference to prior work where on-prem was required.
  - Near-quote (line 152): "when we were doing FedRAMP, it had to be on-prem"

- **Samsung**
  - Who: Colin
  - Context: Used as a hypothetical example of a customer-name word to redact.
  - Near-quote (line 90): "let's say the word that you want to redact... like Samsung"

- **Aerospace and defense (industry)**
  - Who: Colin
  - Context: Where his layered architecture was also deployed.
  - Line 184.

- **Capgemini** — NOT explicitly mentioned in this transcript (though flagged as a watch-term, it did not appear).
- **Accenture / Deloitte / Cohere** — not mentioned.

---

## 13. Reference Data / Lists / Datasets

- **Lam acronym list** (~3,000 items) — see Category 9.

- **Exclusion list** (customers + non-sensitive acronyms)
  - Who: Mikhail
  - Context: Derived from acronym list after removing customer names.
  - Near-quote (line 80): "we removed things that were customers and basically said, this is an exclusion list, this is totally fine."

- **Customer name list** — see Category 9.

- **Fab / location list** — see Category 9.

- **Five data fields (the test corpus)**
  - Who: Mikhail
  - Context: Five free-text fields from Escalation Solver used as the test surface; character count between 5,000-40,000 ("somewhere between 5,000 and 4,000 characters"). Targeting two entity types: customer name + fab.
  - Near-quote (line 43-48).

- **Problem statement field (one of the five)**
  - Who: Mikhail
  - Context: Free-text "plasma arcing issue at..." example.
  - Near-quote (line 44-45).

- **~1,000 thumbs-up/thumbs-down labels** (existing)
  - Who: Mikhail
  - Context: Existing labeled feedback in the UI.
  - Near-quote (line 166): "So I think we have about a thousand."

- **No golden set / labeled corpus**
  - Who: Mikhail
  - Context: Explicit: Lam was told labeling would take >1,000 man-hours and was deemed cost-prohibitive; no true golden set was created.
  - Near-quote (line 69): "our estimates was over a thousand hours, man hours to send direct. Just straight up labeling effort and that was cost prohibited"

- **20,000 samples as rough EDA benchmark**
  - Who: Colin
  - Context: Rule of thumb for close-class binary classifiers.
  - Near-quote (line 109): "a good benchmark to kind of put yourself out is at least 20,000 samples is usually where we stay at."

- **Acronyms loaded for training** (not labels)
  - Who: Mikhail
  - Context: Models were "trained" with acronyms and exclusion lists but not with labeled text.
  - Near-quote (line 69): "We did not train those models. We trained them with our acronym, we trained them with exclusion list."

---

## 14. Methodology / Algorithms Mentioned

- **Parallel model reconciliation algorithm (Lam's prior approach)**
  - Who: Mikhail
  - Context: All three finalist models called in parallel; a reconciliation algorithm merged outputs (not one-model-vs-other; concurrent call + reconcile).
  - Near-quote (line 63): "we had a reconciliation algorithm, which would actually not call one versus the other. It would call all three in parallel and then reconcile between the two."
  - Observed result: false positive rate dropped from 21% → 17% with this approach; accuracy ~90%.

- **Mixture of Experts (MoE)** — see Category 5.

- **Layered / "layers of an onion" architecture (Colin/BayOne methodology)**
  - Who: Colin
  - Context: The recommended approach — deterministic layer first, ML/NLP second, Gen AI last. Linear gating (not parallel voting).
  - Near-quote (line 176-184): "The first layer of this is what I call is the deterministic layer... The second wave is the heavier wave... Let's give it to the gen AI model next for the final one... this is intentionally linear."

- **Deterministic layer (Tier 1)**
  - Who: Colin
  - Context: Regex / rule-based / lookup tables / pattern matching. Flags candidate matches; does not decide.
  - Near-quote (line 177-179).

- **ML / NLP layer (Tier 2)**
  - Who: Colin
  - Context: Cheaper, on-prem-hostable; sentence transformers, TF-IDF, etc.
  - Near-quote (line 180-181).

- **Gen AI layer (Tier 3, edge-cases only)**
  - Who: Colin
  - Context: Final arbitration for edge cases where lower layers disagree.
  - Near-quote (line 182-184).

- **Transfer learning** (concept)
  - Who: Colin
  - Context: Model behavior on unseen-but-similar inputs.
  - Near-quote (line 123-124): "Transfer learning describes the model's performance on those things... If I know how to do this, for instance, I know how to drive a car, can I drive a truck?"

- **Binary classifier**
  - Who: Colin
  - Context: "good vs bad is just a binary classifier" (line 107).

- **Exploratory Data Analysis (EDA)**
  - Who: Colin
  - Context: Pre-project analysis of inter-class similarity to estimate sample counts needed.
  - Near-quote (line 108, 168): "we can do then that statistical analysis that's just an exploratory data analysis, which is to say, how similar is the data among the classes?"

- **Pre-training / post-training**
  - Who: Pat (BayOne)
  - Context: Modern training paradigm; thumbs-up/down feeds post-training loops.
  - Near-quote (line 114): "they are now, earlier it used to be just training of data, labeling and all. Now they're calling it pre-training, post-training."

- **Ground truth**
  - Who: Colin
  - Context: Defined technically; AI cannot self-validate as ground truth.
  - Near-quote (line 98-99): "fundamentally ground truth, AI cannot say that AI is correct. Not possible."

- **ML metrics: F1, accuracy, recall, precision**
  - Who: Mikhail, Colin
  - Context: Mikhail used recall/precision; Colin noted all are co-related.
  - Near-quote (line 55-56, 130).

- **Fine-tuning (and the caveat against it at small scale)**
  - Who: Colin
  - Context: Warning that fine-tuning needs large, reliable labeled data; otherwise overfitting.
  - Near-quote (line 121).

- **Data augmentation — "generate known bad from the bad already"**
  - Who: Colin
  - Context: Technique to expand labeled sets.
  - Near-quote (line 110): "there's other techniques that we have that can even take existing content and generate known bad from the bad already"

- **Human-in-the-loop / auto-categorization tooling (Colin builds himself)**
  - Who: Colin
  - Context: Colin's preferred approach to labeling — custom-built in <1 day.
  - Near-quote (line 143, 164).

- **Tiered labeling taxonomy (Tier 1 word-only, Tier 2 word+document, Tier 3 word+document+human reason)**
  - Who: Colin
  - Context: Framework Colin proposed.
  - Near-quote (line 169-172).

- **Target metrics for the prior POC**: MVP ≤5% false positives; ultimate ≤1% false positives. Achieved 21% FPR → 17% FPR with reconciliation; ~90% accuracy.
  - Near-quote (line 61-66).

---

## 15. Communication / Collaboration Tools

- None explicitly named in this transcript (no Slack/Teams/Outlook/SharePoint/Box references).

---

## 16. Development / Operational Tooling

- No Git/GitHub/Bitbucket/Jenkins/CI-CD/IDE explicitly named in this transcript.

---

## 17. Compliance / Standards / Frameworks Referenced

- **ITAR** (International Traffic in Arms Regulations)
  - Who: Colin
  - Context: One of the two legitimate on-prem motivations.
  - Near-quote (line 152): "if there's anything ITAR or military related"

- **FedRAMP** — see Category 12.

- **Healthcare / HIPAA-adjacent** (referenced by analogy)
  - Who: Colin
  - Context: "healthcare or manufacturing and this is critical to production" cited as legitimate on-prem case.
  - Line 151.

- **GDPR / CCPA / SOC2 / CMMC / NIST 800-171 / ISO** — NOT explicitly mentioned in this transcript.

- **Customer data-out policy** (Lam/customer governance process)
  - Who: Daniel
  - Context: Approval process required before fab-side data can flow back to enterprise.
  - Near-quote (line 154): "approval process with the customer in their data out policy prior to ingestion getting into the enterprise."

- **Clean room policies**
  - Who: Brad
  - Context: Clean room explicitly excluded from current use case.
  - Line 27.

- **Lam internal policy: "no customer confidential information in Escalation Solver"**
  - Who: Mikhail
  - Context: Explicit policy; redaction POC is about enforcing this.
  - Near-quote (line 48): "there is a definitive policy in that application not to enter customer confidential information."

---

## 18. Equipment / Hardware

- **Customer fab equipment** — generic reference.
  - Near-quote (line 42): work orders for "installed maintenance upgrade" on fab equipment.

- **Servers at Lam data center** — see Category 1.

- **No explicit GPU / workstation / laptop / edge-device-model mentions in this transcript.**

---

## 19. Anything Else / Uncategorized

- **Semiconductor industry context**
  - Who: Pat
  - Context: Pat estimates fewer than 50 enterprise-level semiconductor organizations have this exact problem — hence no commercial off-the-shelf solution exists.
  - Near-quote (line 118-119): "I can name, there would be less than 50 enterprise-level organizations who would need this problem statement."

- **Model decision metrics used for selection: performance + initial accuracy**
  - Who: Mikhail
  - Context: Lam's original selection criteria. Business/governance parameters were NOT part of the selection.
  - Near-quote (line 56): "Performance accuracy was the number one way we started."

- **"Effective before efficient" (Brad's engineering principle)**
  - Who: Brad
  - Context: Quoted as a recurring principle.
  - Near-quote (line 56): "you have to be effective before you can be efficient."

- **Lock-maker-and-thief analogy** — Colin's framing for why pure rule-based approaches hit a ceiling.
  - Line 178.

- **Airport baggage-scanner analogy** — Colin's framing for the deterministic layer flagging items for human review.
  - Line 179.

- **Giraffe-vs-car / front-vs-back-of-quarter analogies** — Colin's framing for inter-class distinguishability & sample-size requirements.
  - Lines 106-109.

- **"40,000 users" (Coherent) / aerospace & defense deployment** — Colin's reference deployments of the layered architecture.
  - Line 184.

- **Plasma arcing issue** (example problem statement text)
  - Who: Mikhail
  - Context: Example of the kind of free text a field engineer types into Escalation Solver.
  - Near-quote (line 45): "I'm having a plasma arcing issue at, and you start accepting my customer site"

- **Field engineer workflow: install / maintenance / upgrade → work order → 8-hour resolution SLA → escalation petition** — Escalation Solver context.
  - Line 42.

- **Proposal / POC timeline terms discussed**
  - Colin commits: proposal by Wed (tentative) / Fri (firm); POC ≈ 2 weeks from data access; Lam thumbs-up/down by following Friday. SLW paperwork ~1 week.
  - Lines 199-205.

- **LAM's prior effort timing: "18 months ago"**
  - Who: Mikhail
  - Context: Effort conducted ~Oct 2024 given April 2026 date.
  - Line 58.

- **BayOne internal tool "V1"**
  - Who: Pat
  - Context: Pat said BayOne has done this internally for V1 itself with an existing tool.
  - Near-quote (line 129): "We have done it internally for V1 itself. We have our own tool. Colin has already well done a lot of interface."

---

## Summary of Unique Technologies Catalogued

Core technical stack (prior Lam effort — "what was tried"):
- Presidio (Microsoft PII framework) — starting point
- 12 initial candidate models on Microsoft → narrowed to 5 → narrowed to 3 → final 3 = Transformers model + Flair (Hugging Face) + Azure AI (swapped in late)
- spaCy (NLP model library — used)
- Hugging Face (model source)
- Flair (selected NLP library)
- Rule-based layer added later
- Deployed on: on-prem Kubernetes (for non-Azure models) + Azure (for Azure AI model)
- Parallel-reconciliation algorithm (modified Mixture-of-Experts)
- Reference lists: ~3,000 acronyms, customer list, fab list
- Thumbs-up/down UI (~1,000 labels)
- No golden set (labeling deemed 1,000+ man-hours; cost prohibitive)
- Targets: ≤5% FP (MVP), ≤1% FP (ultimate) | Achieved 21% → 17% FP, ~90% accuracy

Technologies Colin referenced / recommended:
- Azure AI Foundry (Azure OpenAI → Azure AI → Azure AI Foundry)
- OpenAI / Anthropic / GPT-4.0 / Claude / Gemini / IBM models
- Microsoft Purview (enterprise regex-at-scale)
- Regex / Python
- Sentence Transformers, TF-IDF, HuggingFace (on-prem-friendly)
- Mistral MoE (historical reference)
- RoboFlow (commercial labeling, computer vision only)
- FedRAMP (prior on-prem context)

Lam internal systems named:
- Escalation Solver (POC target application)
- ASM (Application Security Manager)
- MABC / MA Data Center / E10 data flows (big EI project)
- Milux / Orion (internal teams), COS (Orion's current project)
- GSNO / GFSO (Brad's org)
- Knowledge and Advanced Services teams
- LAM ID (identity credential)
- Tool file / tool data / recipe / yield data (fab data categories)

Environment tiers distinguished:
- Cloud (Azure/hyperscalers)
- On-prem (data center servers)
- Disconnected / air-gapped (customer-fab-resident, out of POC scope)

Unique named technologies/systems in this transcript: approximately **60+ distinct items** (libraries, models, services, applications, internal systems, reference data sets, methodologies, compliance frameworks, hardware, and industry references combined).

---

## Notable Absences (Watch Terms NOT Found in This Transcript)

- "LamGPT" — not mentioned
- "Capgemini" / "Kaptima" / "Gapsium" — not mentioned
- BERT / RoBERTa — not explicitly named
- en_core_web_lg or other spaCy model IDs — not named
- Presidio analyzer/anonymizer sub-components — not itemized
- Jason Callahan / zero-trust — not mentioned
- JIRA / Confluence / ServiceNow / SharePoint / Teams — not mentioned
- GDPR / CCPA / SOC2 / CMMC / NIST 800-171 — not mentioned
- AWS Bedrock / Google Vertex AI / Cohere — not mentioned
- Specific GPU hardware — not mentioned

(These absences are informative: they identify terms to probe for in follow-up conversations, since Mikhail likely has more detail available in JIRA or email that he could not recall live.)
