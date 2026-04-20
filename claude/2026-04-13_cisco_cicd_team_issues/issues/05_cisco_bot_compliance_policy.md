## Investigate Cisco Bot Compliance Policy and Registration Requirements

### Description

After deploying the Volley bot prototype on the Cisco WebEx environment, Saurav received an email from Cisco IT flagging it as a non-compliant bot. Before any further bot deployment or demos to Srinivas, the team needs to understand the compliance requirements and determine a path forward.

### What Happened

- Saurav deployed a WebEx bot (Volley) on Cisco infrastructure for exploratory testing
- Cisco IT flagged it as non-compliant and required registration with the organization
- The bot policy documents are nested: bot policy links to internet policy, which links to 2-3 more policies, each interlinked with additional policies

### Key Policy Findings So Far

- All bots must be registered with Cisco and submitted for thorough review before deployment
- Group size limitation: bots cannot serve groups with fewer than 2 or more than 100 people
- The NXOI WebEx group has approximately 300+ users, which exceeds the 100-person policy limit
- This is Cisco's internal policy and may have exceptions for internal tools (to be confirmed)

### Tasks

- [ ] Check with Naga and Justin: do they already have registered bots or provisioned access tokens for their Pulse/Scribble work? If so, the team may be able to operate under their existing registration.
- [ ] Review the bot policy documents to understand the registration process and timeline
- [ ] Determine if there is an expedited path for internal development/POC bots vs production bots
- [ ] Document the registration steps and requirements for the team
- [ ] Raise to Srinivas as "help us navigate this" rather than trying to solve it independently. Frame it as: we can show you what we have built, but we need guidance on the compliance path to deploy it.

### Context

- Saurav's bot is already using the Cisco API key for the language model and operating within the Cisco WebEx environment
- The bot is functional (scrapes messages, stores in Postgres, responds to commands)
- This compliance issue does not block development work, but it blocks any demo or deployment to a wider audience

### Acceptance Criteria

- [ ] Bot compliance requirements documented
- [ ] Determined whether Naga/Justin have existing registered bot credentials the team can use
- [ ] Path forward identified (register new bot, use existing credentials, or escalate to Srinivas)
