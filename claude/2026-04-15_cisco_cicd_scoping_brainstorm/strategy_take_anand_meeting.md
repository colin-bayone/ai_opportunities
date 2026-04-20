# Strategy Take — Anand Meeting (April 15, 2026)

---

## The Two Problems (Do Not Conflate)

**Problem A: The price was wrong from day one.** Rahul Sharma set it without analysis. This is a BayOne internal problem. Anand does not care about BayOne's margin issues.

**Problem B: Cisco changed the scope and caused massive delays.** This is documented, legitimate, and the strongest card to play.

If these get smashed together into one ask, Anand will see through it. The scope story has to come first. The money follows from it.

---

## What Srinivas Claimed Was in Place vs. What Actually Exists

These are the concrete things that were represented as ready for BayOne to build on top of, which turned out to not exist or be far less complete than described:

1. **DeepSight CI/CD Application.** Srinivas said Rui was building a CI/CD app on DeepSight that was 2-3 weeks from launch (as of Feb 17). BayOne was supposed to pick it up and extend it. As of April 15, it is still not deployed. Not delayed by a week. Still not deployed two months later. The entire engagement was scoped around building on top of this app.

2. **MCP Infrastructure.** Srinivas described an MCP architecture where databases already had MCPs or were close to having them. Justin has a basic MCP with a few tool calls (latest QA rate, most recent build, sanity results). That is it. The rest do not exist. BayOne is now expected to create MCPs from scratch for data sources they were told were already instrumented.

3. **Database Access and APIs.** Srinivas positioned the backend data layer as accessible. In practice, Anupma (DevEx) is guarded about exposing databases and redirected every discussion offline. The CAT databases (likely Cassandra) have no exposed APIs for BayOne to use. Justin's MySQL is the only one that is actually accessible. The "unified data layer" that the six deliverables assumed existed does not exist.

4. **Airflow Integration Point.** The original scoping assumed BayOne would plug into existing Airflow infrastructure. When Colin asked Divakar about Airflow (Divakar was identified as the contact), Divakar said he has nothing to do with Airflow. The actual Airflow SME has still not been identified as of April 15.

5. **WebEx Tooling (Naga's Work).** Srinivas directed BayOne to build a WebEx scraper and recording transcriber, saying Naga had existing code they could start from. When Srikar met with Naga, the scope of Naga's work was unclear, expanded beyond the original directive, and had no defined end goal. There was no clean handoff point.

6. **Access and Onboarding Process.** Not a deliverable, but a prerequisite for all work. Srinivas and Anand both implied that once the SOW was signed, access would follow quickly. In reality: no onboarding process exists, GitHub Enterprise requires a 3-4 hour training prerequisite plus separate provisioning, ADS Linux machines require a separate request through a different team, VPN requires yet another process, and Duo MFA had a blocking issue that required an IT case. Each of these took weeks, not days.

7. **Cisco Engineer Availability.** Anand said in January that BayOne would have a Cisco engineer with bandwidth to partner during discovery. Divakar was supposed to be that person but was pulled in multiple directions, was absent for weeks, and when he returned, showed territorial friction about BayOne's scope overlapping with his team's work.

---

## Meeting Participants (BayOne Side)

- **Colin Moore** — technical lead, will speak to scope and technical state
- **Neha** — present, supportive
- **Zahra Syed** — present, manages commercial relationship with Anand

Anuj and Amit are not on this call despite inserting themselves into the prep meeting earlier today. They have not been involved since December.

---

## Recommended Approach for Today

### Lead with scope and timeline reality, not money.

Get Anand to acknowledge:
1. The prerequisites BayOne was told would be in place were not in place (specific examples above)
2. Srinivas redirected deliverables from the original A-F to precursor work
3. Access delays are Cisco-caused and ongoing (documented in WebEx messages)
4. The quarterly timeline needs to reset based on when work actually started (late March)

### Then the money conversation becomes natural.

"Given all of this, here is what next quarter actually looks like." Negotiating from documented facts, not from "our math was wrong."

### The number.

Colin's math: $125K/quarter without his cost loaded in gives ~40% margin and works. The chaotic internal meeting produced $168-178K, but that number came from a meeting where nobody could agree on load factors and the formulas were giving different answers.

Target range: $125-150K. This is within the range Anand originally discussed with Zahra. It does not trigger the "why did this double" alarm. It works for BayOne's actual costs.

### What to ask for beyond money.

An access SLA. Something concrete: "Within X days of a request, provisioning will be completed." Without this, adding more money and more people accomplishes nothing because the bottleneck is access velocity, not team capacity.

### What not to do.

- Do not lead with the money number before establishing the delay and scope narrative
- Do not expose the internal costing confusion
- Do not let Cisco frame the conversation as "BayOne has not delivered"
- Do not conflate the pricing problem with the scope problem
