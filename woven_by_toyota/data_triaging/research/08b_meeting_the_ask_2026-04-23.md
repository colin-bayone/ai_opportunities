# 08b - Meeting: The Ask and Sourcing Constraints

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt and /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/toyoya.pdf
**Source Date:** 2026-04-23 (discovery call and JD shared during the call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** Focused deep dive on the commercial ask and sourcing constraints

---

## 1. Executive Framing

The Woven by Toyota discovery call surfaced two distinct asks with very different commercial shapes. The first is a concrete, near-term, single-headcount backfill against an existing open requisition. The second is a substantially larger scale expansion that Woven has not yet shaped on its own side. The backfill is what is actually on the table right now. The scale expansion is a possibility that Travis Millet described in transparent terms as still being worked out internally. For BayOne the practical conversation is about the backfill, the rate card that accompanies it, and the structural difficulty of meeting the qualification profile in the job description at the rate Woven is prepared to pay through its incumbent staffing channel.

The balance of this document decomposes that picture in exhaustive detail.

## 2. The Immediate Ask

### 2.1 Single-headcount backfill on the existing triage team

Travis Millet leads a twelve-person triage team at Woven by Toyota. During the call he confirmed that one person has departed and that the opening now under discussion is a direct backfill of that seat rather than net new capacity. In his words, he framed it as an opportunity for BayOne to compete head-to-head with the staffing vendor Woven has historically used, against a single open requisition that already has an active job description.

Key facts pinned down during the call:

- The role is one seat, not a package of seats.
- The role is a backfill for an attrition departure.
- The role sits inside Travis's existing twelve-person team, not a new org.
- Woven has one unnamed incumbent agency already working the same requisition.
- Travis explicitly consented to a head-to-head submission from BayOne against the incumbent agency, provided it can be arranged without requiring a separate meeting to set it up.
- Travis is not personally conducting interviews on this requisition. His guidance was that BayOne should not reach out directly to other people on his team, and that he would handle routing on his side.
- A mutual non-disclosure agreement between Woven and BayOne is already in place, as acknowledged on the call, which allows the JD and requisition details to move between the parties without additional paperwork.

### 2.2 Functional description of the role

Cross-referencing what Travis said on the call with the written job description, the role is a software quality assurance or system quality assurance position, despite the title "Triage Operations Specialist" used on the HireArt posting. Programming ability is not required to perform the work. Travis was explicit that whatever technical skill a successful candidate brings will be used, but that the core function does not demand software development.

The day-to-day tools described in the job description and referenced on the call include:

- JIRA for ticket workflow and bug management
- JQL for querying JIRA
- SQL for pulling from dashboards and data filters
- Third-party and proprietary internal tooling as part of the triage workflow
- In-house AI triage tool (Woven is the builder, not a consumer, of that tool)

Core responsibilities per the job description map cleanly to what Travis described verbally:

- Analyze complex streams of information, including logs, video files, and sensor data, to triage issues detected during autonomous vehicle drives.
- Interface with field operations and core engineering teams to communicate issues and understand the overall autonomous driving platform.
- Create and continuously monitor expert-level bug reports for use with the in-house AI triage tool.
- Help maintain dashboards and data filters in JIRA and SQL used to gather test scenarios.
- Provide scripting support to help automate the triage process.
- Maintain documentation of the triaging process and the self-driving system.

The baseline requirements are modest: experience as a test engineer (software quality assurance or other) triaging complex systems, strong written and verbal communication, and a customer-focused, organized, meticulous working style.

### 2.3 Team context observed on the call

Travis noted in passing that the educational background of his existing twelve-person team skews toward anthropology, psychology, and sports medicine rather than engineering. He framed this as a direct consequence of the rate: at the fifty-three to sixty-two dollar per hour band, it is difficult for him to attract people with technical or engineering degrees, so he has taken what he could get from the incumbent channel. This is a material signal about the actual hiring pattern on the team, distinct from the aspirational profile expressed in the preferred qualifications section of the job description.

## 3. The Forward Ask (Deferred)

### 3.1 The thirteen-times scale target

Travis described a planned thirteen-times increase in triage volume. The current team of twelve processes approximately six thousand to seven thousand tickets per month. The expected volume in the post-expansion state is approximately one hundred thousand tickets per month. The target date he gave for that volume was mid-July 2026.

### 3.2 Rationale for the expansion

Woven is building an in-house AI-based auto-triage tool. By Travis's own description that tool is working "forty percent of the time," with performance improving and models improving as the industry evolves. He expressed genuine optimism about the trajectory but was equally explicit that the product is not mature enough to carry the full load at scale. The human-based expansion is Woven's buffer against a scenario in which the AI tool does not catch up in time. He framed the logic as not wanting to back up an AI system with another AI system, hence the preference for human capacity as the hedge.

### 3.3 Shape of the expansion is still being figured out

This is the single most important point in the forward ask. Travis was direct that Woven has not yet decided how the expansion will be sourced. Specific language he used was that they are "still trying to figure out the best way forward" on that thirteen-times increase, including how many additional people, who those people are, and whether the channel is contractor or vendor. Woven has evaluated roughly twenty-three vendors, split between offshore human labor pools and AI-only solutions, and has concluded that neither group fits the dynamic nature of the triage work as Woven performs it.

The forward ask is therefore not a live commercial opportunity today. It is a deferred planning conversation. Winning the backfill does not automatically convert to the scale work, and Travis did not promise that it would. At the same time, the backfill is the realistic on-ramp into that conversation, because it is the only concrete transaction on the table in the current window.

### 3.4 Internal-only context on expansion timing

The stated target of mid-July 2026 is approximately twelve weeks from the call date. Given that Woven has not resolved its own sourcing shape, has not published requisitions against the expansion, and has not selected vendors for it, the timeline is aggressive relative to the planning posture. This is not something to raise with Travis on the current call or in follow-up. It is a risk to note internally when BayOne is considering how much capacity to reserve against a possible scale engagement.

## 4. Sourcing Constraints

### 4.1 Pay rate

The job description specifies fifty-three dollars to sixty-two dollars per hour as the expected pay amount. Travis acknowledged the same range on the call and explicitly framed it as the constraint that shapes who he can realistically hire. In his own words, at that rate it is difficult to attract candidates with engineering or technical degrees. The rate is a standard Bay Area contract quality assurance rate, not an engineering rate.

### 4.2 Geographic preference

The job description lists the location as Palo Alto, California, with a work environment designated as remote. The commitment language at the bottom of the job description is more specific: the position is available to candidates local to the Bay Area. Travis's verbal description added important nuance beyond the written text. His current handshake agreement with the Woven human resources function allows the hiring manager discretion on remote versus in-office for the triage team. The practical pattern he described is:

- Woven's full-time employees have returned to the office three days per week under a recent policy shift.
- Travis described "seeing a huge snap to come back to the office" and flagged uncertainty about when or whether the flexibility for contractors will be retracted.
- To hedge against a future retraction, Travis only looks at physical candidates in the Palo Alto or Ann Arbor areas when bringing people onto the team directly, so that if remote is withdrawn the team can still report in.
- Vendor-delivered capacity is treated differently. Travis said he does not require the same physical proximity for people delivered through a vendor relationship where he does not see faces or names.
- At present remote work is acceptable for this requisition.

For BayOne the practical implication is that candidates located in Palo Alto or Ann Arbor carry a durability advantage over candidates located elsewhere, even though the current posting says remote is allowed.

### 4.3 Visa and corporate structure restrictions

The job description states explicitly that the staffing organization is not able to sponsor visas or employ corporation-to-corporation. This rules out a meaningful slice of the Bay Area contract labor pool and forces BayOne to work from candidates who are either United States citizens, lawful permanent residents, or on visas that do not require sponsorship for the contract duration. Corporation-to-corporation is likewise off the table, meaning subcontracted candidates operating through their own entities cannot be placed into this seat through the incumbent channel.

### 4.4 Contract length

The job description specifies a six-month contract. This is a meaningful signal. It is long enough to matter financially and to justify relocation in some cases, but not long enough to justify a candidate leaving a permanent role on the hope of conversion. Travis did mention conversion to full-time employee as a possibility during the broader conversation about the three-resources framing, but the written contract length is six months on its face.

### 4.5 Schedule

The job description lists nine in the morning to five in the afternoon Pacific time, with flexibility on the hours worked daily. Travis also mentioned that the team meets each morning for thirty to sixty minutes to cover the changes from the previous day, which functionally anchors candidates to a Pacific-aligned working day even when nominally remote.

### 4.6 Japanese fluency as a preferred qualification

The job description lists fluency in Japanese as a preferred qualification. Travis corroborated the underlying reason on the call: he works with a Japan counterpart function, which reflects the Toyota parent company relationship and the fact that Woven operates as a subsidiary with meaningful reporting and coordination into Japan. Japanese fluency therefore has operational meaning on this team, not merely decorative value in the job description.

## 5. The Structural Qualifications-Versus-Rate Mismatch

### 5.1 The preferred qualifications describe an AI-literate engineer

The preferred qualifications section of the job description, taken as a set, describes a substantially more senior and more specialized profile than the baseline requirements imply. The list includes:

- Familiarity with JIRA and Confluence
- Experience using Python, terminal scripts, git, and SQL
- Ability to create and expand Python scripts for productivity reports and visualizations
- Prior experience in autonomous or robotic systems
- Experience calling AI agents via application programming interface
- Fluency in Japanese

Read together, this is not a generalist quality assurance contractor profile. It is an engineer who is fluent in Python scripting, has been exposed to autonomous vehicle or robotics domains, has worked with AI agent application programming interfaces in some capacity, and ideally speaks Japanese. That profile, on the open Bay Area market, does not typically transact at fifty-three to sixty-two dollars per hour. It transacts well above that band, often in the low six figures on an annualized basis or the equivalent contract rate.

### 5.2 The baseline requirements describe a commodity quality assurance contractor

The required section, in contrast, is a standard test engineer profile with communication skills and organized work habits. That profile does transact in the fifty-three to sixty-two dollar band on the Bay Area contract market.

### 5.3 The sourcing problem this creates

The gap between the baseline required profile and the preferred profile is the entire source of the sourcing problem. Travis has confirmed in his own words that his current team was hired against the baseline profile, not the preferred profile, because the rate does not attract the preferred profile on the open market. An incumbent generalist staffing pool, working a standard contingent search at standard contingent margins, will naturally deliver to the baseline and not to the preferred qualifications.

From BayOne's perspective, this is the structural opening in the opportunity. Travis is not unhappy with the function his current team performs, but he has been unable to meet the stated aspirational profile through his existing channel. A differentiated submission that disproportionately hits the preferred qualifications is the principal route for BayOne to demonstrate value on a head-to-head basis against the incumbent.

### 5.4 Implications for BayOne's candidate strategy

Given the structural picture above, the most effective candidate strategy for the backfill is the following:

- Prioritize candidates who land above the baseline requirements on at least two of the preferred qualification axes, rather than the single cheapest candidate who clears the baseline.
- Treat Japanese fluency as the highest-leverage differentiator. It is operationally useful because of the Japan counterpart function, it is rare in the Bay Area quality assurance contract pool, and it directly addresses a dimension the incumbent channel is unlikely to source against.
- Treat autonomous vehicle or robotics domain exposure as the second-highest-leverage differentiator. It shortens ramp and it speaks to the nature of the work in a way a generalist quality assurance contractor cannot.
- Treat Python and SQL fluency as a near-baseline expectation for BayOne submissions, not as a preferred qualification to flag for bonus credit. The incumbent channel may deliver candidates without these; BayOne can differentiate by delivering candidates who have them as a given.
- Be prepared for the possibility that strong candidates on the preferred axes will cost more than the posted band can absorb. If so, the commercial conversation about rate accommodation is a legitimate follow-up, framed around the profile Woven actually wants rather than the profile the rate card implies.

### 5.5 Why the incumbent channel struggles here

The incumbent staffing vendor, identified in the internal-only section below, operates a generalist staffing platform. Its natural pool is broad, high-velocity, and priced to a standard contingent margin. That pool does include some candidates who hit preferred qualifications, but it does not systematically filter for Japanese fluency or for autonomous vehicle domain experience at the Bay Area quality assurance contract rate. The mismatch is not a critique of the incumbent. It is a structural property of any generalist pool operating at a commodity rate against a specialist qualifications list.

## 6. What Was Not Asked For

This framing is load-bearing for BayOne's positioning. Travis did not ask for any of the following:

- A software solution, tool, or product from BayOne.
- A proof of concept or pilot of a BayOne triage capability.
- Advisory engagement on the in-house AI triage tool.
- A managed services offering.
- A statement of work for a body of outcomes-based work.
- Design, architecture, or build services of any kind.

The BayOne technical lead did offer an angle on the artificial intelligence architecture conversation during the call, speaking to deterministic classifier layering, human-in-the-loop confidence modeling, and progressive offload from human to machine. Travis engaged with that content and expressed interest in the ideas, but the engagement did not convert to a request for advisory work, and Travis and the BayOne commercial lead both returned the conversation to the three-resources framing and the backfill specifically. Travis was explicit that he is one of the architects of the in-house AI triage tool and that he enjoys the technical conversation because he gets to benchmark against what other companies are doing. That is useful rapport and useful relationship capital. It is not a commercial ask.

The commercial ask on the table today is staffing. That is what Travis invited BayOne to compete against the incumbent on. BayOne's positioning documents for this opportunity should be built around that reality and should resist the temptation to expand the ask into a solutions or advisory frame that Travis did not make.

## 7. Internal-Only Context on the Incumbent

The following content is internal to BayOne only. It was inadvertently disclosed through the job description Travis shared into the meeting chat after he had verbally declined to name the incumbent on the call. It is not to be treated as general-circulation information and must not appear in any client-facing material.

- The job description Travis shared is posted through HireArt and carries the HireArt branding at the top of the document.
- The document states that "HireArt is helping our client find a highly skilled Triage Operations Specialist."
- The commitment section at the bottom of the document states that "this is a full-time, six-month contract position staffed via HireArt."
- The benefits section lists "Employer (HireArt) Subsidized Healthcare Benefits," which confirms that HireArt is the employer of record for the contract.
- On the call Travis began to say that he was not supposed to disclose which supplier Woven uses and caught himself mid-sentence. His verbal framing was that the posting was with "one unnamed undisclosed agency."

The combination of these facts establishes HireArt as the incumbent staffing vendor and as the employer of record for the contract. BayOne should carry that forward as competitive intelligence in its internal planning. BayOne should not name HireArt to Travis, should not reference HireArt in any written deliverable that might reach Woven, and should not suggest to Travis that its identity is known. Travis's attempt to hold the name back was deliberate, and respecting that posture is load-bearing for trust.

The practical use of this information internally is limited to shape. HireArt is a platform-style contingent staffing operator with a generalist engineering and operations pool. Knowing the incumbent helps BayOne understand what kind of submissions the incumbent is likely delivering and where the gaps are relative to the preferred qualifications profile in the job description.

## 8. Open Questions Specific to This Topic

The following questions are open coming out of the discovery call and will shape how BayOne executes against the backfill and positions for any forward work.

1. Who conducts interviews on this requisition, given that Travis stated he is not doing the interviewing himself?
2. What is the evaluation criteria being applied by the actual interviewer or interviewers, and how do those criteria weight baseline requirements against preferred qualifications?
3. What is the process for a head-to-head submission on a requisition that is already live with the incumbent agency, specifically whether BayOne submits directly to Travis, to a Woven talent function, or through a parallel HireArt-style channel?
4. How will the thirteen-times scale work be routed when Woven resolves its internal shape question? Specifically, will it be offered to the current incumbent as an extension of the existing framework, distributed across multiple vendors, or opened to a competitive process?
5. Does the Japan counterpart function have its own sourcing channels or vendor relationships, and if so, is a Japanese-fluent submission from BayOne relevant to that channel as well as to Travis's team in Palo Alto?
6. If BayOne brings a candidate whose market rate exceeds the sixty-two dollar per hour ceiling because that candidate actually lands the preferred qualifications, is there room to negotiate the rate, or is the band a hard floor and ceiling set by the incumbent staffing framework?
7. Is there a single master statement of work structure Woven uses for contract headcount, as Travis hinted when he mentioned "one single big statement of work for ten anonymous forks," and if so does that structure apply to BayOne's participation or would a separate instrument be required?
8. What is the anticipated duration beyond the six-month contract term, and is conversion to full-time employment at Woven a realistic outcome for strong performers?
9. Are there non-obvious disqualifiers in Woven's own internal screening, such as prior employment at specific competitors in the autonomous vehicle space, that BayOne should filter for before submitting?
10. How does Woven want the physical presence question handled in the submission packet, given the current remote allowance and the uncertainty about whether that allowance will be retracted?
