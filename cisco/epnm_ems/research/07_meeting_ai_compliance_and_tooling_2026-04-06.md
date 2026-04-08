# 07 - Meeting: AI Compliance and Tooling

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on AI compliance and tooling discussion

---

## 1. How the Topic Was Introduced

The AI compliance and tooling discussion did not arise organically from the technical walkthrough. It was introduced by Selva after the team had finished walking through the EPNM screens and the conversation shifted to logistics -- access provisioning, repository groups, and NDA status. Selva explicitly surfaced it as an outstanding concern from Ramesh:

> "I think Ramesh also had some questions about what AI tools, what AI software will be used and what kind of compliance we need to be aware of."

This positions the discussion as a gating concern. Ramesh, who is US-based (unlike the rest of Praveen's team in India), had been waiting to raise this. He acknowledged connectivity issues at the start of his question: "As such, because I was shifting the new home, right? The internet is not good. I'm not sure I'm getting connectivity. Can you guys hear me?"

---

## 2. Ramesh's Questions

Ramesh asked a direct, well-structured question about AI tool compliance. His concern was specifically about code exposure -- that Cisco proprietary source code would be accessible to whatever AI tools BayOne uses, and he needed to understand the security posture. His question, closely paraphrased from the transcript:

> "The AI tools, agents that you are using today -- are they Cisco-compliant? Because we will be exposing Cisco's code to the tools. So how is your operating structure? That's what I want to understand. Like, are these tools something local, like Claude Code or Cursor, something like that, or are they different? If they are hosted on some cloud, you will be exposing this code there. I want to know how you are operating -- your environment."

The question has three distinct dimensions:

1. **Tool identity:** What specific AI tools are being used?
2. **Compliance status:** Are those tools Cisco-approved?
3. **Architecture:** Are the tools local or cloud-based, and if cloud-based, does that mean Cisco code is being sent to external servers?

Ramesh's framing shows familiarity with the general landscape -- he name-drops Claude Code and Cursor as examples, and he understands the fundamental concern about code exfiltration to cloud-hosted AI services. This is not a vague worry; it is a specific, informed question about data residency and tool authorization.

---

## 3. Colin's Response: The CICD Engagement Precedent

Colin's response was detailed and began by establishing precedent rather than defending the tooling abstractly. He immediately invoked the existing Cisco engagement:

> "So let me say one thing first to start this out. So we are currently active. Me and about four other people are active on a different project for Cisco. That's the NX-OS CI/CD pipeline work. We're working with Srinivas Pita and Anand Singh."

This is a strategic framing choice. Rather than explaining the tooling architecture from scratch and then arguing it is compliant, Colin establishes that BayOne already has a proven operating model within Cisco's security perimeter. The CICD engagement serves as a live reference point -- BayOne is not proposing an untested approach but extending an approach that Cisco has already sanctioned.

The specific people named (Srinivas Pita and Anand Singh) are the Cisco contacts on that engagement. Naming them provides Ramesh and the team with internal verification points -- they can confirm the operating model independently through those contacts.

**Key claim from Colin:** "For that work, we already have certain things Cisco-provisioned for us."

---

## 4. Colin's Response: The Tooling Architecture

Colin then laid out the specific tools and their deployment model in two parts:

### 4a. Claude Code -- Cisco-Issued

> "Every single thing we do for this will be done number one on Cisco hardware and number two with Cisco-issued accounts. So for us, what that looks like from an architecture perspective is Claude Code -- we use for development. We'll use the Cisco-issued Claude Code."

This is an important distinction. Colin is not saying he will use a personal Claude Code license or a BayOne-purchased Claude Code license. He is saying the Claude Code instance itself is Cisco-issued -- meaning Cisco has procured and authorized this tool at the enterprise level, and BayOne uses it through Cisco's provisioning. The data flow stays within Cisco's authorized channels.

### 4b. LangGraph -- Local Execution

> "Number two, for the actual deployment, that is LangGraph, and that is local. So that is also living and breathing on, for the moment, my Cisco-issued laptop."

LangGraph is the orchestration framework for AI agent workflows. Colin's point here is that LangGraph does not require external cloud infrastructure -- it runs locally on the Cisco-issued laptop. This addresses Ramesh's specific concern about code being "hosted on some cloud" and exposed externally.

The phrase "for the moment" is notable -- it suggests that LangGraph may eventually move to Cisco-hosted infrastructure (a VM or server) rather than staying on a laptop, but the key architectural property (local execution, not external cloud) would remain the same.

### 4c. Explicit Negation of Third-Party Tools

Colin then explicitly ruled out external tools:

> "We won't bring in any kind of external third-party or cloud-based tools aside from the Cisco-provided Claude Code for this."

This is a clean, unambiguous commitment. The tooling architecture for this engagement consists of exactly two components: Cisco-issued Claude Code and locally-running LangGraph. Nothing else.

---

## 5. Ramesh's Confirmation

Ramesh confirmed his understanding by paraphrasing back what Colin said:

> "Claude Code and LangGraph, that's what I heard. That will be your major tools as such."

Colin confirmed: "Correct. That's right."

Ramesh then added a follow-up confirmation about authorization:

> "All from Cisco authorized accounts, as you said, right?"

Colin confirmed again: "Yes."

This exchange demonstrates that Ramesh was satisfied with the answer. He did not push back, did not ask follow-up questions about specific data flows or model providers, and did not raise concerns about LangGraph's architecture. The precedent of the CICD engagement and the clear two-tool architecture appears to have been sufficient.

---

## 6. Selva's Reinforcement of Cisco Policy

Immediately after Ramesh's confirmation, Selva added a broader policy statement:

> "That's a good point that Ramesh is saying. It's part of any engagement here. We're not allowed to use Cisco code on anything that's outside of our... I mean, the approved AI tools that we get access to is the only thing that we use on our code. Which you are aware of and you mentioned."

Selva's statement does three things:

1. **Validates Ramesh's question** as appropriate and important ("that's a good point")
2. **States the policy universally** -- this is not specific to BayOne, it applies to all engagements; no Cisco code may be used with non-approved AI tools
3. **Acknowledges Colin already addressed it** -- "which you are aware of and you mentioned"

This positions the policy as a standing Cisco requirement, not a special restriction being imposed on BayOne. It normalizes the constraint and closes the discussion by confirming alignment.

---

## 7. Colin's Extended Compliance Commitments

After Selva's policy statement, Colin volunteered additional commitments that went beyond Ramesh's question. This extended response covers several areas:

### 7a. DeepSeek Awareness

> "Even things like DeepSeek right now -- we're also helping out certain of us with DeepSeek as well. So we have good understanding of what AI compliance looks like at Cisco."

This is a revealing reference. DeepSeek is a Chinese-developed AI model that has been the subject of significant security and compliance debate in enterprise environments due to data sovereignty concerns. Colin's mention of DeepSeek demonstrates two things:

1. BayOne has direct experience with Cisco's AI compliance boundaries, including awareness of tools that are controversial or restricted
2. Colin is signaling that his team understands the nuances of AI tool compliance, not just the broad strokes

The phrase "we're also helping out certain of us with DeepSeek" is ambiguous in the transcript -- it may mean BayOne is helping Cisco personnel evaluate or use DeepSeek within compliance boundaries, or it may mean some BayOne team members have exposure to DeepSeek through other work. The key takeaway is that Colin is demonstrating awareness of the compliance landscape beyond just the tools he plans to use.

### 7b. Library Installation Gating

> "Even the libraries that are used -- those are not able to be touched unless we get those approved first."

This extends the compliance commitment beyond AI tools to the software supply chain. Colin is saying that even installing Python libraries, npm packages, or other dependencies requires approval. This addresses a subtler version of the code-exposure risk: even if the AI tools are compliant, introducing unapproved libraries could create vulnerabilities or data leakage paths.

### 7c. Colin as Gatekeeper

> "So I'm kind of the master gatekeeper. Of course for the POC, it's just me. But even if we choose to go with the full-scale engagement, still that same gatekeeping will be there."

Colin explicitly positions himself as the single point of accountability for compliance. During the POC, this is trivially enforced because Colin is the only person working. For the full engagement, he commits to maintaining the same gate -- no team member can independently install software, add libraries, or use unauthorized tools.

> "But yes, absolutely strictly Cisco-issued. And there's no way for my team to override that."

The phrase "no way for my team to override that" is a strong commitment. It implies either a technical control (permissions, access restrictions) or a process control (Colin must approve all tool and library additions) that prevents individual team members from circumventing the policy.

### 7d. Transparency Commitment

> "We'll be very transparent about what we're using and how we're using it."

This is a softer commitment but important for the trust dynamic. Colin is offering visibility into the tooling, not just compliance. The Cisco team can audit what tools are in use at any time.

---

## 8. POC Staffing Context

Ramesh confirmed staffing implications:

> "So presently, it will be only you working on the project?"

Colin confirmed this is the case for the POC. He then added that for the larger scope engagement, additional people would come on, and they would be "effectively Cisco employees for the duration of the engagement, all NDA signed, all other items taken care of on Cisco side."

This matters for compliance because it establishes that the security model scales: every BayOne team member gets the same treatment as Colin -- Cisco hardware, Cisco-issued accounts, Cisco-approved tools only. The compliance posture is not a special arrangement for one person; it is the engagement model.

---

## 9. Connection to Earlier Security Discussions

This compliance discussion builds on security constraints established in the February 9, 2026 discovery meeting (Document Set 01). In that meeting, the following was established:

- All code must remain on Cisco hardware
- AI tools must be Cisco-licensed, not personal licenses
- NDA was already signed
- Cisco laptop provisioning was pending (1-2 week timeline)
- No downloading code to personal machines under any circumstances

The April 6 discussion confirms that these constraints have been operationalized. Colin now has Cisco hardware, Cisco-issued accounts, and is actively working under these constraints on the CICD engagement. What was theoretical in February is now a demonstrated operating model.

Several open questions from the February discussion are implicitly resolved:

- **"What specific AI tools does Cisco have licensed?"** -- Answer: Claude Code, at minimum
- **"Can Colin's preferred toolchain (Claude Code, LangGraph) be used?"** -- Answer: Yes, Claude Code is Cisco-issued; LangGraph runs locally and does not require Cisco licensing
- **"Must everything run on-premises?"** -- Answer: Claude Code appears to be cloud-based but Cisco-authorized; LangGraph runs locally

---

## 10. Open Questions and Unresolved Items

1. **DeepSeek role and status at Cisco.** Colin referenced DeepSeek in the context of AI compliance awareness, but did not specify whether DeepSeek is approved, restricted, or under evaluation at Cisco. The reference was used to demonstrate compliance sophistication, not to propose DeepSeek as a tool for this engagement. However, the nature of BayOne's involvement with DeepSeek at Cisco is unclear.

2. **Claude Code data flow specifics.** Colin stated Claude Code is "Cisco-issued," and this was accepted without further probing. The specific architecture -- whether Cisco has a private Claude instance, whether code is sent to Anthropic's servers under an enterprise agreement, or whether there is some other arrangement -- was not discussed. Ramesh's question about cloud exposure was answered at the policy level (Cisco-authorized) rather than the technical level (where does the data actually go).

3. **Library approval process.** Colin referenced a gating process for library installation but did not describe the mechanism. Is this a formal Cisco change management process? A BayOne-internal control? How long does approval take? For the POC (Colin only), this is self-governed. For the full engagement, the process needs to be explicit.

4. **LangGraph eventual hosting.** Colin said LangGraph is "for the moment" on his Cisco-issued laptop. If it moves to a server or VM, does that require additional Cisco approval? Would it move to Cisco-hosted infrastructure, or could it move to a cloud instance? This was left open.

5. **Ramesh's ongoing oversight role.** Ramesh asked the compliance questions, but it is unclear whether he has an ongoing compliance oversight function for this engagement or whether this was a one-time due-diligence check. His US location (same as Colin) and his specific focus on this topic suggest he may have a security or compliance responsibility within Praveen's team.

6. **Cross-engagement tool sharing.** Colin referenced the CICD engagement as precedent and offered to share details (with Srinivas's permission) about testing approaches. The degree to which tool configurations, access credentials, or infrastructure can be shared between the CICD and EPNM-to-EMS engagements is not established. They are presumably separate Cisco projects with potentially separate access controls.

---

## 11. Summary of Commitments Made

| Commitment | Speaker | Scope |
|---|---|---|
| All work on Cisco hardware | Colin | POC and full engagement |
| All accounts Cisco-issued | Colin | POC and full engagement |
| Claude Code via Cisco-issued license only | Colin | POC and full engagement |
| LangGraph runs locally (no external cloud) | Colin | POC and full engagement |
| No external third-party or cloud-based tools | Colin | POC and full engagement |
| Library installations require approval | Colin | POC and full engagement |
| Colin is sole gatekeeper for tool compliance | Colin | POC and full engagement |
| Full transparency on tools used | Colin | POC and full engagement |
| Team members treated as Cisco employees (NDA, hardware, accounts) | Colin | Full engagement |
| Approved AI tools only -- standing Cisco policy | Selva | Universal (all engagements) |
