# 07 - Demo: Architecture and Security Discussion

**Source:** /sephora/edw_modernization/source/edw_demo_4-2-2026_formatted.txt
**Source Date:** 2026-04-02 (Demo Meeting)
**Document Set:** 07 (The Actual Demo)
**Pass:** Focused deep dive on Azure architecture, deployment, and security exchanges

---

## The Pivotal Security Question

### Network Isolation Concern [00:20:17]

The most consequential exchange in the entire demo occurred when Maher Burhan interrupted the discussion of the human review/auto-fix workflow to ask a direct infrastructure security question.

**Maher Burhan [00:20:17]:** "When you when you make calls to these models, whatever model you're using in the background, do you go out of the our network to the public model or you have your private?"

**Maher Burhan [00:20:50]:** "Are you hosted now outside?"

This question reveals that Maher was specifically evaluating whether the system makes external API calls to public model endpoints (e.g., Anthropic's public API, OpenAI's public API) or whether all inference stays within Sephora's network perimeter. For a consultant embedded at a retailer handling customer data, PII, and proprietary business logic in ETL pipelines, this is a threshold question: if the answer had been "public API calls," the engagement would likely face an immediate IT security review barrier.

### Colin's Response: Architecture Diagram [00:20:41 - 00:21:52]

Colin responded by pulling up the architecture diagram -- a deliverable he had prepared but was told he would not need.

**Colin [00:20:52]:** "Someone told me that I wouldn't need this diagram today, but I'm glad I have it."

He then delivered the key assertion:

**Colin [00:20:52 - 00:21:30]:** "There are no calls to anything at this current moment in time that ever go outside of your Azure instance. And in fact, every single thing that we built here is entirely based on Azure exclusively. Even for us, you know, even Postgres, that's the back end for LangGraph in this case, even Postgres right now is running in Azure. So we did that intentionally to make sure that everything is perfectly transferable."

Colin followed up by scrolling through the diagram:

**Colin [00:21:30 - 00:21:52]:** "Every single thing here is already exclusively based in Azure, so there's nothing here that you would need to have any external connections to. Even for us for the POC, we still kept it all production ready, ready to go."

### Maher's Positive Response [00:21:52]

**Maher [00:21:52]:** "OK, that's good."

This brief confirmation is significant because Maher immediately moved forward with a deployment-specific follow-up question rather than raising objections or requesting further documentation. The Azure isolation answer satisfied the security concern.

---

## The VNet Deployment Exchange

### "Deploy It to Your VNet" [00:21:52 - 00:22:12]

Immediately following the Azure isolation confirmation, Maher shifted from "is it secure" to "how do we operationalize it" -- a progression that signals the security answer was sufficient.

**Maher [00:21:52 - 00:22:05]:** "So basically when you're finished with this, you're gonna tell us here, deploy it to your VNet, put it in your subnet and we'll be able to run it. It's not reaching out to anything."

**Colin [00:22:05]:** "That's right. That's right. Completely isolated from the outside."

**Maher [00:22:06]:** "Cool. Thank you."

### Colin's IT Experience Note [00:22:12 - 00:22:34]

Colin proactively offered to share the architecture diagram and acknowledged the IT review dynamic:

**Colin [00:22:12 - 00:22:30]:** "And so the same, the same here, even for the diagram, I will share this 'cause this, I'm sure if there's anyone in IT that wants to know, we've definitely had this conversation before. But generally speaking, that's a good motivator for us. We have less hectic conversations with IT."

**Colin [00:22:30 - 00:22:34]:** "Whenever we use the right platforms from the start, so that's the motivation for us."

This positions the Azure-only architecture as a deliberate strategic decision to reduce IT friction, not an afterthought. The "we've definitely had this conversation before" phrasing signals experience navigating enterprise security review processes at other clients.

---

## Container Deployment Options Discussion

### Maher's Container Architecture Questions [00:27:26 - 00:27:57]

After the demo workflow walkthrough, Maher returned to the architecture diagram to ask detailed deployment questions. His questions were specific and technically informed, consistent with someone who manages or advises on Azure infrastructure.

**Maher [00:27:26 - 00:27:45]:** "So these are the component that you will have. So you can deploy this as a container either to container service or AKS and you need Azure database or do you need the database post SQL database or?"

**Maher [00:27:57]:** "So all the components you have here. Basically this is what you need to deploy this application, right?"

### Colin's Component-by-Component Breakdown [00:27:59 - 00:29:22]

Colin walked through each component in the architecture:

**FastAPI Container (Required):**
**Colin [00:27:59 - 00:28:24]:** "Fast API as a container app, absolutely needed. We have these all set up as Docker Compose images for you that can already be deployed if you wanted it like even for us. It's a deploy script, CI/CD automation built into these for us."

**Dashboard Container (Optional, for UI):**
**Colin [00:28:24 - 00:28:43]:** "Fast API is here, the dashboard AKA the actual UI itself. If you want a UI and you don't want to use it natively in VS Code, then dashboard can be here as just a separate other container just as a viewpoint."

This reveals an alternate deployment path: the system can be operated directly from VS Code without the web dashboard, meaning the UI container is optional.

**Worker Container (Optional, for Scale):**
**Colin [00:28:43 - 00:29:03]:** "The other two containers, if you wanted them, or excuse me, would be just a fast API worker container. So if you wanted to do this at a scale and we were throttling for any reason, we do have a worker container with Celery that you could bring into this. It does increase cost, but it also increases your concurrency."

**Scaling Options -- AKS vs. Container Apps:**
**Colin [00:29:03 - 00:29:17]:** "Without overloading the server and with Azure it's scale up, scale down. So we can do it with AKS. We can do it with Azure Container Apps natively and just use their own scaling with KEDA scaling. Both will work fine for this."

This positions AKS and Azure Container Apps as interchangeable for this workload, giving Sephora the choice to use whichever they already have standardized in their environment. KEDA (Kubernetes Event-Driven Autoscaling) was specifically named as the Container Apps native scaling mechanism.

---

## Database Options Discussion

### Maher's Database Requirement Question [00:27:45 - 00:29:57]

**Maher [00:27:45]:** "Do you need the database post SQL database or do you need it?"

**Colin [00:29:17 - 00:29:22]:** "And then for the database, do we need it? Not really."

### Three Database Options Presented [00:29:22 - 00:29:58]

**Option 1 -- PostgreSQL (Default):**
The POC uses PostgreSQL running in Azure. It stores run history and LangGraph state.

**Option 2 -- SQLite:**
**Colin [00:29:22 - 00:29:35]:** "We can have it, or you can use SQLite, or you can use a different database that you might already have, deployed on Azure that you'd want to put this on. It doesn't have to be an additional cost."

**Maher [00:29:32]:** "So can you use SQLite container inside? OK, so all right, nice."

**Colin [00:29:35 - 00:29:58]:** "Yes, yes, yes, yes, yeah. Now of course the downside to SQLite is that it's a single threaded database, so it doesn't have quite as much concurrency as the others do, but we even have ways around that. We could do parquet files and then a SQLite at the end and that way you know the application doesn't get bogged down."

**Option 3 -- Existing Database:**
Colin explicitly stated they could use an existing Azure-hosted database that Sephora already operates, eliminating any additional database cost entirely.

### What This Exchange Reveals

Maher was probing for the minimum infrastructure footprint. Each question sought to reduce the number of new Azure resources Sephora would need to provision: Can we skip the dedicated database? Can we use what we already have? This suggests either cost sensitivity for infrastructure provisioning, a desire to minimize the IT review/approval surface area, or both.

---

## LangSmith: Optional Observability Tool

### Colin's LangSmith Positioning [00:30:01 - 00:30:53]

Colin positioned LangSmith carefully, acknowledging its external hosting while defusing the security concern:

**Colin [00:30:01 - 00:30:53]:**
- **Optional:** "LangSmith is optional. That's only for people that really want to dig their teeth into, you know, what's specifically going on in the language model side."
- **Scope:** "Every single prompt, every single call to a language model, every single bit of output. That comes from these. You can see with LangSmith."
- **Free:** "That is completely free open source for you. That's something that would just come by default."
- **SSO-authenticated:** "Can come through your single sign on as well."
- **Toggle on/off:** "This can be turned off or turned on. It's a simple environment variable to turn it off or on."
- **External hosting acknowledged:** "Technically LangSmith is hosted externally, but it authenticates through SSO, so you still have that enterprise protection there."
- **Self-hosting option:** "Or you can just turn it off and or you could host it yourself in a different container if you wanted."
- **Analogy:** "It's just an observability tool, though it's not anything critical for function. Think of like Grafana similar to that, but for language models."

### The Four-Option Hierarchy for LangSmith

Colin effectively offered four escalating options:
1. **Turn it off entirely** -- Environment variable toggle, zero external connections.
2. **Use hosted LangSmith with SSO** -- External service, but enterprise-authenticated.
3. **Self-host LangSmith** -- Deploy it in another container within the Azure environment.
4. **Use the built-in UI** -- The demo already showed LangSmith-equivalent tracing information on the front end (execution log, agent detail views).

This layered approach let Maher (and any future IT security reviewer) choose their comfort level without losing the observability capability.

### Maher's Response [00:30:53]

**Maher [00:30:53]:** "OK. OK. Yeah. OK."

No objection raised. The SSO and toggle-off options appeared to satisfy the concern.

---

## Vishal's FastAPI and Orchestration Questions

### Why FastAPI? [00:31:01 - 00:31:29]

**Vishal Sharma [00:31:01]:** "So this fast API, what exactly are handled here? Like is it like parsing? It's handling AI calls? It's handling like orchestration? Like why can't we use ADF right?"

Maher interjected to answer before Colin:

**Maher [00:31:16]:** "That's the engine, I believe. That's the... this is Python, right? The Python library."

**Maher [00:31:23]:** "Yeah, it is in Python. OK, it's a Python package. That's the API."

### Colin's Clarification [00:31:29 - 00:31:57]

**Colin [00:31:29 - 00:31:57]:** "Yes, that's right. That's right. And for the AI model hosting and access, those are all coming from Azure AI Foundry. But the orchestrator, the thing that's making the calls, parsing, running those deterministic steps, that is all this fast API server and fast API is just what we picked. For our stack, we can adapt to pretty much anything in case there's a preference."

Key distinction made: FastAPI is the orchestration engine (making calls, parsing, running deterministic steps). Azure AI Foundry is the model hosting layer. FastAPI does not host models.

### ADF (Azure Data Factory) as Alternative Orchestrator [00:31:57 - 00:32:07]

**Vishal [00:31:57]:** "So for orchestration, if you want to use ADF for example, we can do that, correct?"

**Colin [00:32:02]:** "Yeah, yeah. We would just have to know what you want and we can build around that, no problem."

This exchange signals that Vishal (and possibly the broader Sephora data engineering team) already uses ADF for pipeline orchestration and is evaluating whether the BayOne system can integrate into their existing toolchain rather than introducing a new orchestration layer.

---

## Cost Numbers Discussed

### Worker Container Cost [00:51:07 - 00:51:37]

**Colin [00:51:07 - 00:51:37]:** "Realistically, in fast API, we're running some very quick Python scripts. There's no throttling that I can see with something that's a reasonably equipped container app instance. So this is something that you're probably not gonna get bottlenecked by, but if you did, all you'd do is set up Celery, set up workers that would increase your cost marginal. We're talking when I say cost, we're talking probably an extra $20.00 a month to run the service for the duration that it's online. So $20 Max is the ceiling and then you could, you know, it's just a matter of how much you want to scale."

- **Worker container cost:** ~$20/month per worker container (ceiling estimate)

### Redis Cost [00:51:55 - 00:52:15]

**Maher [00:51:42]:** "That's why you were mentioning that the database, if we have a, you know the scalable database, then it'll be much better than having container running inside the Azure Container Apps, right?"

**Colin [00:51:55 - 00:52:15]:** "Both in terms of performance and persistence. So if you and the other one that would come in if you really wanted to take the training wheels off of this is throw Redis into the mix. Redis again does add on some cost. It's about $30 a month when you deploy an Azure at this... this tier."

- **Redis cost:** ~$30/month at the tier appropriate for this workload

### Total Infrastructure Cost Implication

Colin presented the infrastructure costs as minimal and incremental:
- Base system: FastAPI container + optional dashboard container + SQLite (or existing database) = near-zero additional infrastructure cost
- Scaling tier: Add Celery worker ($20/month) + Redis ($30/month) = ~$50/month total for full concurrency
- These figures deliberately exclude the Azure AI Foundry model costs (token-based), which are the primary expense

---

## Scaling and Concurrency Discussion

### Andrew Ho's Scale Question [00:48:39 - 00:50:32]

Andrew Ho asked whether the system could handle the full scope of Sephora's migration (many tables, many ETL jobs, many reports) or whether it was limited to processing one or two at a time.

**Andrew [00:48:39 - 00:50:32]:** "The flow that you've shown today, I'm assuming that it's not just like a one or two report at a time or one or two tables at a time like you know it can scale. And run in parallel with multiple tables, multiple reports... So how do I... your flow and your processes it's gonna allow us to if I want to tackle maybe the first thing is, OK, run a pilot, just pick one business area and then you convert that... Then once we've proven that this is really it works... I want to run it full scale."

### Colin's Scaling Architecture [00:50:32 - 00:53:03]

**Colin [00:50:32 - 00:50:51]:** "The exclusive thing that we are constrained by in terms of parallelism is the compute. So basically that is determined exclusively by effectively what you want for this fast API."

**Colin [00:51:01 - 00:51:07]:** "That's why I brought up workers because fast API... this is already pretty lean because really the only heavy lifting is not even happening here, it's actually happening in Foundry. So those language model calls."

This is an important architectural point: the FastAPI layer is lightweight because the compute-intensive work (LLM inference) happens on Azure AI Foundry's infrastructure. The FastAPI container mainly orchestrates, routes, and runs deterministic Python scripts.

### Celery Workers for Horizontal Scaling

Colin explained the Celery worker pattern:
- Workers handle concurrent pipeline executions.
- Each worker can process a separate pipeline run independently.
- Scaling is horizontal: add more workers for more concurrent pipelines.
- The constraint moves from FastAPI to Azure AI Foundry's token quotas and rate limits.

### Orchestrator of Orchestrators [00:52:15 - 00:52:49]

Colin described the full-scale architecture as layered orchestration:

**Colin [00:52:15 - 00:52:49]:** "A really easy way to think is to say. Imagine there's one more layer above this that is the orchestrator of the orchestrators. And imagine this just takes this, copies and pastes it up above and says do all these in parallel with each other this and then at the human end of it you would just see your dashboard view at the end. Which would be a collective of all these things across reports."

**Colin [00:52:49 - 00:53:03]:** "So yeah, so scaling, no problem. This is built to be concurrent as much as the compute has appetite for."

### Maher's Database Scaling Connection [00:51:42]

Maher connected the earlier database discussion to scaling:

**Maher [00:51:42]:** "That's why you were mentioning that the database, if we have a, you know the scalable database, then it'll be much better than having container running inside the Azure Container Apps, right?"

Colin confirmed: "Both in terms of performance and persistence."

This shows Maher was tracking the architectural implications across the conversation: SQLite works for a single pipeline at small scale, but at full scale with concurrent workers, a proper database (PostgreSQL or an existing Azure-hosted database) becomes important for both performance and data persistence.

---

## Docker and CI/CD Readiness

### Docker Compose Images [00:27:59 - 00:28:27]

**Colin [00:27:59 - 00:28:24]:** "We have these all set up as Docker Compose images for you that can already be deployed if you wanted it like even for us. It's a deploy script, CI/CD automation built into these for us."

Key claims:
- Docker Compose definitions already exist for all components.
- CI/CD automation is already built (deploy scripts exist).
- The system is deployable as-is, not requiring additional containerization work.

---

## Vishal's Portability and Independence Concern

### Can Sephora Run This Without BayOne? [00:34:32 - 00:36:02]

**Vishal [00:34:32]:** "And you use YAML like plus that kind of SEL capability right here, right? So like what if you see suppose in future we decide to stop using that platform like what will be our options in that case?"

**Vishal [00:35:03 - 00:35:18]:** "Because we want to make sure that you know we can run something fully in our environment like without your system as well. So that you know, we're sure that in case we want to move, we want to change it in the future. So that capability should be supported."

### Colin's Response on Customization and Ownership [00:35:18 - 00:36:02]

**Colin [00:35:18 - 00:36:02]:** "You could look at this and say I could do it way better, you know, and all I will do is I'll give you the effectively the default versions of them. Anything like these are fully customizable. If you want to add on new ones, we have... typically we have a configuration screen so that you can go and create your own if you'd want. Now can I be accountable for how well those perform? Of course not, but at least the possibility will be there. So if you want to add in custom agents, different steps, have different types of outputs, or even just tweak little things in here, you can always do that and there will always be a, you know, go back to defaults version."

### Maher's Framing: Transition Tool, Not Permanent Dependency [00:36:02 - 00:36:31]

Maher reframed the entire engagement scope:

**Maher [00:36:02]:** "Yeah, I mean, yeah, this is the transition period. Basically we use it to migrate. When we migrate, we don't need it anymore. We are in our platform, yeah."

**Colin [00:36:13]:** "Yes, exactly. Exactly. If we do a good job, then this means that this is temporary for you, right?"

**Maher [00:36:17]:** "Yeah, yeah, exactly. That's the plan, basically migrate. And when we migrate, we're running in Databricks. Yeah, that's the goal."

This exchange is strategically significant: Maher is explicitly positioning the tool as a migration accelerator with a finite lifespan, not a permanent platform. This framing reduces the risk perception (no long-term vendor dependency) and aligns with the self-service/handoff model Colin's AI practice advocates.

---

## Architecture Diagram: Component Summary

Based on Colin's walkthrough and the exchanges, the architecture diagram shown during the demo contained the following Azure-hosted components:

| Component | Required? | Role |
|---|---|---|
| FastAPI Container | Yes | Orchestration engine, deterministic steps, API routing |
| Dashboard Container | Optional | Web UI for pipeline monitoring, human review, downloads |
| Celery Worker Container | Optional | Horizontal scaling for concurrent pipeline executions |
| PostgreSQL / SQLite / Existing DB | One required | Run history, LangGraph state persistence |
| Redis | Optional | Message broker for Celery workers at scale |
| Azure AI Foundry | Yes | Model hosting (Claude Opus, Claude Sonnet) -- all calls stay within Azure |
| LangSmith | Optional | Observability/tracing for LLM calls (can be self-hosted, SSO, or disabled) |

---

## What This Tells Us About Sephora's IT and Security Posture

### Inference from Maher's Questions

1. **Network perimeter is a hard boundary.** Maher's first infrastructure question was about whether model calls leave the network. This was asked before any question about cost, performance, or features. Network isolation is the gating criterion.

2. **VNet/subnet deployment is the expected model.** Maher's immediate follow-up described deployment as "deploy it to your VNet, put it in your subnet." This is how Sephora expects applications to be provisioned -- within their existing Azure networking infrastructure, not as standalone SaaS.

3. **Sephora already operates Azure infrastructure.** Maher's questions about AKS, Azure Container Apps, and Azure databases were asked fluently and without clarification, indicating familiarity with these services and likely existing provisioning in the Sephora Azure environment.

4. **Minimal new resource provisioning is preferred.** Maher probed whether the database was required, whether SQLite could substitute, and whether existing databases could be reused. This suggests either a procurement process for new Azure resources or a preference for fitting into existing allocated infrastructure.

5. **IT review is anticipated.** Colin's comment about sharing the architecture diagram "in case anyone in IT wants to know" and Maher's VNet question both anticipate that an IT security review will occur before production deployment. The diagram was prepared as a deliverable for this purpose.

6. **ADF is a known orchestration tool internally.** Vishal's unprompted question about replacing FastAPI with ADF suggests Sephora's data engineering team already uses Azure Data Factory, and any new tool must either integrate with or justify its existence alongside ADF.

### Inference from Vishal's Questions

7. **Sephora wants to own and operate independently.** Vishal explicitly asked about running the system "fully in our environment like without your system as well." This is a vendor independence requirement, not a casual question.

8. **Maher aligned on transitional framing.** By characterizing the tool as a "transition period" migration accelerator that becomes unnecessary after migration completes, Maher reduced the perceived risk of adopting BayOne's tooling. No long-term lock-in concern.

---

## Timeline of All Infrastructure and Security Exchanges

| Timestamp | Speaker | Topic | Key Detail |
|---|---|---|---|
| 00:13:12 | Colin | LangSmith introduction | "The observer back end for LangGraph" |
| 00:14:24 | Maher / Colin | LangSmith availability | Both LangSmith and the front-end dashboard would be available to Sephora |
| 00:20:17 | Maher | **Network security question** | "Do you go out of the our network to the public model or you have your private?" |
| 00:20:52 | Colin | **Azure isolation answer** | "There are no calls to anything that ever go outside of your Azure instance" |
| 00:21:52 | Maher | **VNet deployment** | "Deploy it to your VNet, put it in your subnet and we'll be able to run it" |
| 00:22:05 | Colin | Isolation confirmation | "Completely isolated from the outside" |
| 00:22:12 | Colin | IT review readiness | Will share architecture diagram, "we've definitely had this conversation before" |
| 00:27:26 | Maher | Container deployment options | AKS vs. Azure Container Apps |
| 00:27:45 | Maher | Database requirement | PostgreSQL required or optional? |
| 00:28:24 | Colin | Docker Compose images | "CI/CD automation built into these" |
| 00:28:43 | Colin | Worker containers with Celery | Optional, for concurrency scaling |
| 00:29:03 | Colin | AKS vs. Container Apps | "Both will work fine... KEDA scaling" |
| 00:29:22 | Colin | Database options | PostgreSQL, SQLite, or existing database |
| 00:29:35 | Colin | SQLite concurrency limitation | Single-threaded; parquet files as workaround |
| 00:30:01 | Colin | LangSmith positioning | Optional, free, SSO, env variable toggle, self-hostable |
| 00:31:01 | Vishal | FastAPI role question | "Why can't we use ADF?" |
| 00:31:29 | Colin | FastAPI vs. Foundry | FastAPI = orchestrator; Foundry = model hosting |
| 00:31:57 | Vishal | ADF as alternative | Colin confirmed it could work |
| 00:34:32 | Vishal | Platform independence | "What if in future we decide to stop using that platform?" |
| 00:35:03 | Vishal | Full self-sufficiency | "We can run something fully in our environment without your system" |
| 00:36:02 | Maher | Transitional framing | "This is the transition period... when we migrate, we don't need it anymore" |
| 00:50:51 | Colin | Scaling architecture | Constraint is compute, not the orchestrator |
| 00:51:07 | Colin | Worker cost | ~$20/month per worker container |
| 00:51:42 | Maher | Database and scaling link | Scalable database better than embedded SQLite at scale |
| 00:51:55 | Colin | Redis cost | ~$30/month for Azure Redis at required tier |
| 00:52:15 | Colin | Orchestrator of orchestrators | Layered orchestration for full-scale parallel execution |
