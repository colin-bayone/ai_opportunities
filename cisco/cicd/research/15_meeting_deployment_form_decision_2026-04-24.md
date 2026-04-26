# 15 - Meeting: Deployment Form Decision

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt
**Source Date:** 2026-04-24 (Friday afternoon Srinivas sync)
**Document Set:** 15 (Sixth Srinivas team meeting)
**Pass:** Focused deep dive on the deployment form decision and the compute-constraint context that shaped it

---

## Why This Decomposition Stands Apart

Of the architectural questions that have surfaced across the Cisco CI/CD engagement to date, the deployment form question carried the highest leverage. It sat at the intersection of three previously separate threads: the issue categorization skill that BayOne demonstrated in earlier sessions, the CAT-MCP integration that was unblocked this week, and the end-of-next-Friday delivery target that Srinivas had set in Main Set 14. The phrase "deployed by next Friday" was deliberately compact, and the compactness left an open question of form. Saurav surfaced this exact open question in the BayOne team standup on the morning of 2026-04-24, and the one-page status deliverable that went out to Srinivas earlier in the afternoon listed it as the fourth item under access and needs-clarity. The Friday Srinivas sync was the resolution point, and Srinivas resolved it with a decision that reaches forward into every subsequent design choice for the next week of work.

## Colin's Framing of the Question

Colin opened the deployment thread by tying it to the categorization skill that BayOne had already shown in a prior session. The relevant lines of the framing were as follows. Colin reminded Srinivas that the team had built a categorization skill and had assembled a set of self-contained HTML dashboard graphics. He then said, "For us to deploy that, kind of two things would be needed. And I think these are upstream of the CAT-MCP, and that's why I'm bringing this here. Because the CAT-MCP would be used to go and resolve those issues and pull the details from them. But that's kind of a catch-22 because the issues need to be categorized first." That phrasing captures the dependency structure precisely. The MCP is the lookup tool, the categorization pass is the upstream classifier, and the dashboard is the consumer of both. Without an answer to where the categorization pass runs and how often, the question of where the dashboard runs cannot be answered either.

Colin then made the menu of options explicit and gave Srinivas the choice. He said the team could implement the categorization layer in Airflow, or in FastAPI, or in any framework available, with the constraint being that it had to be deployable on DeepSight. The honest gap Colin acknowledged was his unfamiliarity with what DeepSight actually supports. He said, "My lack of knowledge here with DeepSight is if it is capable of running background automation tasks that are steadily ongoing, so it's like an observer loop." That sentence was the cleanest possible statement of the open question. If DeepSight runs persistent background workers, then the categorization pass becomes a steady observer loop and the architecture is closer to a streaming pipeline. If DeepSight does not run background workers, or if running them is expensive in a way that BayOne is not yet aware of, then the architecture has to look different.

## Srinivas's Compute Constraint Disclosure

What followed was a moment of unusual candor from Srinivas. Rather than answering the framework question directly, he stepped back and disclosed the underlying constraint that determined which answer was viable. The disclosure is worth quoting closely because it provides context that BayOne would not otherwise have had access to.

Srinivas began with a server count problem, "We're using four of them, right? Three of them. They got three. They ordered four, they got three. I had a challenge. What a problem." He went on to describe a separate conversation with a peer or platform owner, "I told him that they need the server because they have this model thing and what not. I told him that we need to figure it out. How do we get a player on the deep side so that he doesn't bother about the tokenization and other stuff." The reference to a player on the deep side appears to mean placing a model or an inference endpoint inside the DeepSight environment so that downstream consumers do not have to manage tokenization budgets directly.

He then addressed token burn on a parallel project. "any hold of the servers, compute or model thing, we are burning left and right even the premium keys for the FLARE. Because I tried to optimize it when I was doing the FLARE earlier, but it's still burning." FLARE appears to be an internal Cisco project name. The point of the reference was not to brief BayOne on FLARE specifically but to convey that even a premium-tier key allocation on an existing project is consuming tokens faster than the budget can absorb. He made the connection to the new work explicit, "So one way to free up ourselves with our tokens, GPU requirement on the FLARE. Also in the compute, right? We need to bring FLARE on that himself."

Most importantly, he closed with a statement about availability of compute for new work, "for this project, or even for doing myself any R&D, I don't have any compute right now. Because all the existing servers are in production and our hands and legs are getting tired slowly." That sentence is the operational constraint that determines the architecture. There is no spare GPU capacity, no idle servers waiting to host a continuous observer loop, and the premium keys that exist are already being consumed by other work.

The significance of this disclosure goes beyond its technical content. Srinivas chose to share an internal compute and budget problem with a partner who is not, strictly speaking, owed the explanation. That choice indicates that the working relationship has reached a level where shared context is preferred to filtered messaging, and BayOne now carries a responsibility to design within the constraint rather than around it.

## Colin's Probe on IT Servers

Before accepting the constraint as fixed, Colin probed whether IT could provide capacity outside the production server pool. He asked, "can we get it from IT? Things which actually, let's say, we can't scale, but if we have to experiment, the flow is working. Can we get it from IT?" The framing was disciplined. Colin was not asking for production-grade compute, only for an experimentation tier.

Srinivas confirmed IT was technically a path but not a fast one, "IT, the problem is we can get it, but it will not be fast." The conversation then drifted toward a separate channel for the IT and procurement question. Srinivas said, "we can talk offline, but be able to buy the server," and closed with, "Yeah, I think we have to chat separately." The IT path is therefore live but not on the critical path for the next-Friday delivery. It will be addressed as a parallel conversation, and the next-Friday architecture will be designed without depending on it.

## The Deployment Form Decision

Having framed the constraint, Srinivas made the architectural call. The decision came in a sequence of statements that, taken together, establish a two-mode pattern that replaces the central observer loop pattern that BayOne had been considering.

Srinivas said, "For now, we will not create a, what you call, a poller or anything." That single statement is the load-bearing element of the decision. The poller pattern, in which a background process continuously walks through pull requests, classifies them, and writes the results to a store that the dashboard reads, is rejected. He immediately gave the alternative, "Until we figure out the complete problem, we'll do on-demand pull. So if the user says that I'm interested in this thing, we will, from that PR, we'll basically pull it through the MCP and show it to the user." The mode is event-driven. A user request for a specific pull request triggers a single MCP call, which returns the data needed to render the view for that pull request, and the view is rendered for that user only.

The second mode covers the dashboard case, where the data is not tied to a user clicking on a specific pull request but to a recurring view of pull request status. Srinivas said, "So for now, and we don't have to create a, I don't know, maybe we can create a, when we create a dashboard, we can make it a pull method at a low frequency. And so that MCP is not taken down at the same time we have something." The second mode is therefore a low-frequency refresh, not a continuous observer. It exists to keep the dashboard view current but is throttled to a cadence that protects the MCP and the upstream rate limits.

The two-mode pattern that emerges from these statements is clean. Mode one is on-demand pull per pull request, triggered by the user expressing interest in a specific item. Mode two is low-frequency dashboard refresh, scoped to the user's own pull requests, running at a cadence on the order of every thirty minutes. Neither mode requires a central poller. Neither mode requires a steady observer loop. Neither mode requires Cisco to allocate compute that does not exist.

## The API Rate Limit Constraint

Alongside the compute constraint, Srinivas raised a second constraint that further shaped the cadence question. He said, "also we have to keep in mind like so anything we are doing with PR we cannot afford to increase the API calls a lot because there is a limit per hour right I have brought this before as well." The point is that any architectural pattern that increases the rate of calls into the upstream pull request data source would not just slow this engagement, it would impact every other team consuming the same API. The rate limit is shared, not per-tenant.

Colin acknowledged the constraint and tied the dashboard cadence directly to it. He said, "we'll make it very low frequency, like half an hour or something." He then made the connection between the two constraints explicit, "Yeah, not just for the compute, even for the API call limit. Otherwise, we'd start getting issues there. All PRs will be impacted." The thirty-minute cadence is therefore not arbitrary. It is calibrated to two ceilings, the compute ceiling that Srinivas described and the API call ceiling that he had raised in earlier sessions. Both ceilings push in the same direction, which simplifies the design choice.

## Per-User Personalization Architecture

With the two-mode pattern established, Srinivas walked Colin through a screen share that demonstrated how the personalization layer of the architecture would work in practice. The vehicle for this is the existing CI/CD app inside the Cisco environment, which Srinivas referenced under the transcribed forms CACDR, CACD app, and CSCD app. The element on screen that mattered was the user identity indicator in the top corner, which shows the logged-in user. Srinivas said, "if you go to PR Insights, you know who logged in because here on the top corner, you know this expertise that I have logged in. So you have the user. I can only see my own related PR related information."

The pattern is straightforward. The CI/CD app already authenticates the user. The user session is therefore a known identity at the moment any dashboard view loads. The dashboard view filters to the user's own pull requests by default. There is no central process running on behalf of all users. The compute cost of populating the dashboard is paid only when a user actually loads it, and only for the pull requests that user has any reason to look at. Srinivas summarized the consequence, "You can just pull user information, throw him whatever the current state, whatever the cat is offering. So that way, it's personalized and go from there."

This pattern matters because it rotates the architecture from a many-to-many model, in which a central process must understand all pull requests for all users, to a one-to-few model, in which each user request involves only the small set of pull requests that user cares about. The compute cost no longer scales with the number of pull requests in the system. It scales with the number of active users at any given moment, which is dramatically smaller.

## Group Concept for Manager Roll-Up

The single weakness of a strictly per-user model is that it does not naturally serve managers, who need a roll-up view across an engineering team rather than a list of their own personal pull requests. Srinivas resolved this with a feature that already exists in the CI/CD app, described as the group concept. He said, "if the user is a manager, we have something called group concept. If I'm a manager, I'll add all my engineers into that group. Then when I click on the PR dashboard link, it will show all the graphs or whatever is, whatever is required related to the PR thing. That way it is customized on a role basis and you don't have to have a central compute and you'll also solve the total problems automatically. So it is never a CI-CD app to do whatever you want."

The group concept is the load-balancing element that allows the architecture to remain decentralized. A manager's view is not constructed by a central poller. It is constructed by the manager configuring their own group, and the system then resolves the group at the moment the dashboard is loaded by pulling the membership and aggregating the members' pull request data. The compute cost is paid by the manager's session, not by a background process. Srinivas described the integration path, "we can tell you what is the group API. And that group will tell, basically, you can pull the information from the Cisco directory. Let's say, it's Anand, right? Group.Anand, or something like that." The group API resolves group membership against the Cisco directory, returns the list of users in the group, and the dashboard then pulls each user's pull request set on demand.

The architectural consequence of combining the per-user model with the group concept is that compute cost scales with active user activity at every level, individual contributor or manager, and never with the size of the underlying pull request universe. This is the property that makes the design viable inside Cisco's compute constraints.

## Colin's Acceptance and Synthesis

Colin's acceptance was direct. He said, "We'll use a user session for the identity. And then, yeah, this sounds good." He then synthesized the rationale, "this is one, actually, it's, I think, let's go with this, because we already did it, and we don't have to reinvent it, or having a central server or anything like this." Srinivas confirmed, "Yeah, that sounds good. That's perfect."

Two things are notable about the acceptance. First, Colin reframed the choice as a build-versus-reuse decision rather than a constraint-compliance decision. The CI/CD app, the user session, and the group concept already exist; BayOne is not being asked to invent infrastructure, only to consume what Cisco has already built. Second, Colin explicitly named the alternative being rejected. The central server pattern is the one that this new design replaces, and that naming is helpful for downstream documentation.

## Architectural Implications for BayOne

Several implications flow from this decision and shape the next week of BayOne's work.

There is no central poller service to build. Whatever effort had been planned for an Airflow DAG, a FastAPI background worker, or an observer loop is redirected. The categorization skill still runs, but inside the request path of either an on-demand pull request lookup or a low-frequency dashboard refresh.

The per-user pull pattern from the CAT-MCP becomes the primary interaction with upstream data. When a user opens a specific pull request view, the backend issues a single MCP call, runs the categorization pass on the returned data, and renders the view. The catch-22 Colin described, in which categorization needed to precede MCP resolution, dissolves because both happen inside the same on-demand request rather than across two separate temporal layers.

The dashboard refresh cadence is set at approximately every thirty minutes, scoped to the user's own pull requests for individual contributors and to the group's pull requests for managers. This cadence is calibrated to the API rate limit ceiling rather than to a user experience target.

The manager group API integration becomes a discrete work item. BayOne needs to call the group API against the Cisco directory, resolve group membership at dashboard load time, and aggregate per-user pull request data across the resolved set. The transcribed example, Group.Anand, suggests a dotted naming scheme tied to a manager's identity. Confirmation of the exact interface will come from Srinivas's team.

The backend should be designed as a service application platform, transcribed in the source as SAP, with pluggable user interface and bot frontends. The same backend that serves the CI/CD app dashboard view can serve the WebEx bot. Both consume the same on-demand and low-frequency pull paths into the CAT-MCP. The personalization layer, user session for individuals and group concept for managers, applies identically across both frontends. The term SAP should be confirmed in writing with Srinivas rather than assumed.

LLM routing for the categorization pass runs initially through the circuit API token that BayOne already has access to, with DeepSight credentials substituted in once they are issued.

## Why This Decision Is the Most Consequential of the Week

The deployment form question was the single open architectural item most likely to cause the next-Friday delivery target to slip. Without the decision Srinivas made in this meeting, BayOne would have been pushed in several wrong directions simultaneously. A central poller service would have consumed compute that Cisco does not have available, surfacing as a deployment failure either on the temp ADS or against any other server pool. The API call rate would have crossed the per-hour ceiling and would have impacted every other team consuming the same upstream data, creating a cross-team incident on top of the missed delivery. The WebEx bot frontend and the CI/CD app frontend would have been built against separate backends, doubling the integration and testing surface. Deployment onto the temporary ADS, which is the fallback path while the permanent ADS access remains stuck with Mahavir, would not have fit because the temporary ADS does not have capacity to host a long-running observer loop alongside the user-facing components.

With the decision in place, all of these failure modes are routed around. The user session and group concept eliminate central compute. The on-demand and low-frequency pattern stays inside the API rate limit ceiling. The single backend serves both the CI/CD app and the WebEx bot through pluggable frontends. The deployment fits on the temporary ADS without a large compute allocation, which means that the parallel conversation with Mahavir about permanent ADS access does not block the next-Friday demonstration.

## Forward Action Items

Several items for next week's work follow directly from the decision.

Design the backend as a service application platform with pluggable user interface and bot frontends. Confirm the Cisco-internal term for this pattern with Srinivas in writing.

Implement user session identity in the dashboard so that the default view is filtered to the logged-in user's pull requests.

Integrate the group API against the Cisco directory for manager roll-up views. Confirm the exact group API interface, the naming scheme, and the resolution semantics with Srinivas's team.

Route LLM calls through the circuit API token initially. Substitute DeepSight credentials into the same routing layer when they are issued.

Set the dashboard refresh cadence at approximately every thirty minutes. Validate this cadence against the documented per-hour API rate limit once that limit is confirmed in writing. Adjust if the math requires a longer interval.

Implement the on-demand pull path through the CAT-MCP for individual pull request views. Run the categorization pass inline within the request path rather than as a precondition step.

## Context for Future Re-Reading

This decision replaces the Airflow-orchestrated observer-loop pattern that had been implicit in BayOne's prior architectural sketches and in the tools Colin offered to Srinivas at the start of the meeting. The new pattern is event-driven rather than scheduled. The trigger for any compute work is either a user request, in the on-demand mode, or a low-frequency timer in the dashboard refresh mode. There is no continuous background worker, no central queue of pull requests waiting to be classified, and no shared state that all users read from. The pattern fits Cisco's actual constraints and is easier to deploy on the constrained temporary ADS while the permanent ADS access remains pending.

The decision should be revisited if any of three conditions change. First, if Cisco's compute pool expands through the IT path Colin probed or through the procurement conversation Srinivas deferred, then a low-rate observer loop could be added as a supplement. Second, if the per-hour API rate limit is raised, the thirty-minute dashboard cadence can be tightened. Third, if the categorization workload grows to the point that on-demand inline classification becomes a latency problem, a small amount of pre-computed classification could be added back, scoped only to recently active pull requests, without reverting to a full central poller. None of these conditions are present in the current week.
