# 06 - Incident: IT Security Flag on Namita for Source Code Sharing

**Source:** /cisco/cicd/team/source/week_2026-04-20/day_2026-04-20/namita_incident_disclosure_exchange.md
**Source Date:** 2026-04-20 (incident surfaced morning of; triggering events occurred Friday 2026-04-17)
**Document Set:** 06 (IT security incident, aberration)
**Pass:** Full incident capture, minimal processing per Colin direction

---

## Summary

Namita Ravikiran Mane was flagged by Cisco IT Security (Matt Healy) for sharing four of Justin Joseph's source code files with Vaishali Sonawane (newly onboarding BayOne engineer) via Microsoft Teams on Friday 2026-04-17. Three additional data-handling issues surfaced during IT Security's review. Srinivas Pitta and Anand Singh have called a 15-minute meeting with Colin for later today (2026-04-20) to discuss. Colin has scheduled a 7:30 PST prep call with Namita before that meeting.

## The Four Disclosed Items

### 1. Source Code Sharing (the triggering event)

- **What:** Four source code files belonging to Justin Joseph (Cisco build team)
- **To whom:** Vaishali Sonawane (BayOne engineer, newly onboarding, has signed Cisco NDA)
- **How:** Microsoft Teams chat, initiated from Namita's Cisco-issued laptop
- **When:** During a Friday 2026-04-17 working call between Namita and Vaishali
- **Purpose stated by Namita:** Help Vaishali understand log files and Justin's existing code as part of ramp-up on the build log analysis track
- **Namita's reasoning:** Vaishali is already on the project, Mahaveer Jinka (Cisco procurement) knows BayOne has people joining from India, so sharing with a project teammate did not appear to Namita to be a boundary violation

### 2. Attempted Log File Share (blocked by system)

- **What:** Zipped log files from the temp ADS machine Namita has sole access to
- **To whom:** Vaishali (same Teams session)
- **Outcome:** Share was blocked by Cisco's DLP/security controls; transfer did not complete
- **Significance:** Confirms Cisco's data-loss prevention controls detected and stopped at least one attempt, but source code transfer in item 1 was not blocked

### 3. Cross-Device Transfer of Project Deliverable Document

- **What:** The internal project document the team had prepared for the 2026-04-17 Srinivas presentation (includes WebEx chat scraping content)
- **Movement:** AirDropped from Namita's Cisco laptop to Namita's personal/BayOne laptop
- **Reason:** Namita's monitor was not working during the Friday presentation meeting; she needed to display the doc from her normal working laptop
- **How it surfaced:** Matt Healy saw the document during his review and specifically flagged the WebEx chat scraping content, asking whether Cisco was aware
- **Namita's response to Matt:** Confirmed that BayOne is working with the Cisco team on the scraping work and that it is part of the engagement scope

### 4. Upload of Log Analysis PDF to BayOne GitHub

- **What:** `Log_type_mapping.pdf`, a log analysis document Namita had authored
- **Destination:** BayOne GitHub (outside Cisco environment)
- **Status:** Uploaded; Matt Healy specifically asked her about this upload
- **Significance:** This is the only item that crossed from Cisco environment to an external BayOne-controlled system in a persistent, stored form. The airdrop in item 3 was laptop-to-laptop; this upload is to a hosted external platform.

## People Involved

### New to the engagement

- **Matt Healy** — Cisco IT Security. Conducting the review of the incident. Role and seniority not yet known. Namita is actively in communication with him.

### Existing, directly involved

- **Namita Ravikiran Mane** — BayOne engineer, build log analysis track lead, on Cisco laptop daily. Subject of the security flag. Expressed sincere remorse. Cited good-faith onboarding intent.
- **Vaishali Sonawane** — BayOne engineer, newly onboarding, offshore. Recipient of the shared material. Has signed Cisco NDA (per Colin's note, this is in BayOne's favor).
- **Justin Joseph** — Cisco build team engineer. Owner of the four source code files that were shared. Not yet known whether he has been informed or what his reaction is.
- **Srinivas Pitta** — Cisco Director of Engineering, BayOne's primary technical counterpart. Called the 15-minute meeting for today.
- **Anand Singh** — Cisco Senior Director, executive sponsor. Co-calling the 15-minute meeting. His involvement at this level indicates the incident has reached executive awareness.
- **Mahaveer Jinka** — Cisco procurement. Mentioned by Namita as context (he knows BayOne has India staff joining). Not known whether he is aware of the incident.
- **Colin Moore** — BayOne Director of AI, engagement lead. Managing response. Had previously and specifically cautioned the team not to move client data to BayOne accounts.

## Colin's Position as Communicated to Namita

Three points stated explicitly in Colin's reply:

1. **Prior warning acknowledged.** Colin had specifically cautioned the team earlier not to share client data from client hardware to BayOne accounts. This incident is a violation of that standing guidance.
2. **Final warning.** Colin explicitly stated this is his only warning to Namita. No further violations of this kind will be tolerated.
3. **Contract risk.** Well-intentioned behavior does not neutralize the commercial risk. These types of incidents can lose the contract.

Colin also acknowledged:

- Namita acted in good faith and meant no harm
- Vaishali's signed Cisco NDA is the strongest mitigating factor
- The team should expect a scolding from Srinivas at today's meeting
- The outcome is likely to be manageable ("It will be OK")

## Today's Meeting Structure

- **7:30 PST:** Colin + Namita prep call. Goal: Colin walks into Srinivas/Anand meeting fully informed and able to do damage control.
- **Later today:** Srinivas + Anand + Colin, 15 minutes, topic is this incident.
- **Colin's read on the 15-minute duration:** Mildly positive signal. A longer meeting would suggest greater severity or open-ended concern; a 15-minute window suggests the Cisco side wants to address it directly and move on.

## Risk Surface (Items Requiring Colin to Be Informed Before Meeting)

- Exact nature and sensitivity of Justin's four source code files (proprietary algorithms, credentials, or routine build scripts?)
- Whether Justin has been informed and his personal reaction
- Whether the Log_type_mapping.pdf uploaded to BayOne GitHub contains any Cisco-proprietary data, hostnames, internal paths, or sample log content
- Current status of the BayOne GitHub repository (public, private, who has access)
- Whether Matt Healy has communicated any remediation requirements to Namita
- Whether the WebEx scraping concern raised by Matt in item 3 has been resolved or remains open

## Mitigating Factors in BayOne's Favor

- Vaishali had signed the Cisco NDA at the time of sharing
- One attempted transfer (item 2) was blocked by Cisco DLP, demonstrating Cisco's controls are functioning
- Namita self-disclosed the full picture to Colin rather than minimizing
- Namita is actively cooperating with Matt Healy
- The shared material stayed within individuals under Cisco NDA (items 1, 3); only item 4 crossed to a BayOne-controlled external system
- BayOne has just had contract extension granted on 2026-04-16 by Anand Singh, demonstrating recent executive confidence

## Aggravating Factors

- Colin had previously and specifically warned against exactly this behavior
- Four separate items, not one, meaning this is a pattern of data-handling judgment rather than an isolated slip
- Item 4 (GitHub upload) creates a persistent external artifact that must be reviewed and potentially removed
- The WebEx scraping flag in item 3 re-opens a scope question that Colin had already navigated with Srinivas; having it resurface through IT Security rather than through Srinivas is awkward
