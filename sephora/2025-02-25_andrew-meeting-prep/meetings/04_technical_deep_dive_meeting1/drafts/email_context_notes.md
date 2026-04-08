# Email Context Notes - March 30, 2026

Collecting all context before writing the email. Saraf transcript still incoming.

---

## Situation

- Demo was promised Friday, got delayed (Colin pulled into escalation + personal matters)
- Demo is now ready with a video to share
- Visited Sephora HQ last week, met Mani in person
- Mani said vendor selection must happen by end of month (it is March 30th today)
- This email needs to land today

---

## Key Messages to Convey

### 1. Apology for Delay
- Was pulled into an escalation and had to fly back home unexpectedly
- Personal matters
- Keep it brief, not overly apologetic

### 2. Demo Video
- Attaching a web link to demo video
- If it looks blurry: click gear icon and select 1080p, or download it
- Link access is restricted for security since it involves their data
- Additional access can be granted upon request

### 3. In-Person Visit Reference
- Met with Mani at Sephora HQ
- Enjoyed seeing the building, beautiful headquarters
- Mani said they can use existing BayOne contractors at Sephora to get Cognos access
- Colin is positioning that as a post-PoC next step (beyond free demo scope)

### 4. This Was Built Custom for Them
- Not an existing product
- Everything they see was built in the last two weeks
- With more time in a production engagement, it can be even better and custom-tailored to their teams' exact needs

### 5. Demo Availability This Week
- All is ready from our end
- What is their availability for a live demo?

### 6. Azure Deployment Offer
- We could deploy it on Azure with secure credentials
- They could log in and try it themselves as a web application
- Not just watching our screen, actually using it on their own
- Secure access with credentials for specific individuals
- At no cost if they are interested
- Could be ready by Thursday, shared with them Friday

### 7. Local Developer Option
- There is also an option that requires no infrastructure
- Much slower, but enables local developers
- Useful if there is expected lag with IT for a deployed solution
- They mentioned IT lag issues in the past

### 8. Production Quality Even for a PoC
- Even though this is a free PoC, we built it production-style
- Hosted and deployed securely on Azure
- Could be easily ported to their system
- Shows what we can do with more time and production scope

### 9. Cognos / Automation Limitations
- Demo limitation: no access to their on-prem Cognos
- Cannot automate input side (source files) or output side without their environment access
- Still a human-in-the-loop step until we have Cognos access
- Mani suggested using existing BayOne contractors at Sephora for that access
- Colin positions this as immediate next steps post-PoC to build momentum and show fully autonomous in their ecosystem

### 10. Vendor Selection Urgency
- Mani said they need to select a vendor by end of month
- Today is March 30th
- This email essentially solidifies the relationship
- Cannot be overbearing, but needs to be warm, energetic, excited

---

## Tone

- Warm and energetic
- Excited without being overbearing
- Match Colin's natural voice from prior emails
- Happy, confident, forward-looking
- Grateful for the in-person meeting
- Brief apology, not dwelling on delay

---

## From Saurav Conversation (March 30, 2026)

### Critical Intel

**Sephora has told ALL other vendors no.** They are no longer interested in anyone else. If BayOne shows something working, they get the project. Budget numbers must be locked in by end of April.

This is not a competitive situation anymore. This is ours to lose.

### Demo Status

The demo is working and looks great. Colin's words: "This looks like something people pay money for."

What the demo shows:
- File upload with preloaded demo files
- Live activity showing each agent step flowing through
- Orchestrator gate with visible step progression
- Column mapping with match/unmatch counts and confidence scores
- Issues flagged as warnings and infos (never errors, because the orchestrator retries until errors resolve)
- Downloadable output (YAML, SQL, deployment files)
- Approval step with confidence score and human-in-the-loop validation
- Run history with IDs

### Azure Deployment

Saurav suggested deploying it on Azure so Sephora can log in and try it themselves. Colin agreed. Plan is:
- Time-bound credentials (works for a week, then server shuts off)
- Secured with authentication
- Their data is already loaded
- Could be ready by Thursday, shared Friday

### Skills Alternative (No Infrastructure Option)

Saurav also built a lighter version using Claude Code skills:
- Fewer API calls, faster, lower token cost
- But: no self-correcting loop, and skills are readable markdown (IP concern)
- Colin wants to bias toward the architecture solution but mention skills as a fallback for developers who can't wait for IT to deploy infrastructure

### Timeline

- Screen recording: today (send to Sephora as interim)
- Full integrated demo: Thursday/Friday
- Colin is absorbing Saurav's other responsibilities this week to free him up

### Colin's Key Framing Points (verbatim themes)

1. "This is not a product, this is a solution. We will do this custom for whomever needs it."
2. "We would advise against a cookie cutter solution. This is built for you."
3. "Everything they see was built in the last two weeks."
4. "With more time to do this in a production way, it can be even better."
5. "Even as a PoC, we did it production-style."
6. On confidence scores: "97% confidence is not 97% accuracy. The discrepancies are where human-in-the-loop comes in."
7. On issues/warnings: "The moment you show them insights, you've got them. This is a team that does reporting."

---

## Still Waiting On

- Demo video link (Colin will provide)

---

## Recipients

Full Sephora team + BayOne team (same thread as prior emails)
