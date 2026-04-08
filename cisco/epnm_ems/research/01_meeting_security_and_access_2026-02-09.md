# 01 - Meeting: Security and Access

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Focused deep dive on security, access, and logistics constraints

---

## 1. Code Must Remain on Cisco Hardware

The most fundamental security constraint established in this meeting is that all code must stay on Cisco-controlled infrastructure. This was not presented as negotiable. The relevant exchange occurs toward the end of the meeting when Colin and Guhan are discussing the practical mechanics of getting started.

The constraint is straightforward: BayOne engineers cannot download Cisco source code to personal machines. All development, exploration, and AI-assisted work must happen on Cisco-provisioned hardware connected to Cisco networks. This has direct implications for the AI tooling approach, because any AI model that processes code must be running within Cisco's infrastructure or be a Cisco-licensed service.

**Key implication:** Colin's methodology (Claude Code, LangGraph agent swarms, knowledge graphs) must be deployable on Cisco hardware or through Cisco-approved cloud services. Personal API keys, personal IDE extensions, or SaaS tools running outside Cisco's perimeter are not acceptable.

---

## 2. Cisco-Licensed AI Tools Required

Guhan made clear that AI tools used on this engagement must be Cisco-licensed, not personal licenses. This distinguishes between, for example, a developer's personal GitHub Copilot subscription and a Cisco Enterprise Copilot license. The exact phrasing in the transcript is garbled by speech-to-text (rendered as something like "coded service point"), but the intent from context is that Cisco has enterprise-licensed AI tooling available and that is what must be used.

**What this means practically:**
- Colin cannot simply install his preferred AI tools on a Cisco laptop and start working
- The AI platform/tools must be whatever Cisco has licensed at the enterprise level
- This may constrain which models (Claude, GPT-4, Gemini, etc.) are available
- Colin's methodology presentation (Claude Code as backbone, LangGraph agents) would need to either run within Cisco's approved tooling or require Cisco to approve/license those specific tools

**Open question:** What specific AI tools does Cisco currently have licensed at the enterprise level? This was not resolved in the meeting. Colin would need to discover this after receiving hardware and access.

---

## 3. NDA Status

The NDA between BayOne and Cisco has been signed. This was confirmed in the meeting as already completed. The NDA appears to cover both Colin and the broader BayOne team that would come on after a POC.

The NDA is referenced in the context of Guhan being comfortable sharing internal details (code architecture, team dynamics, product strategy, customer relationships) during the meeting. He volunteered significant internal context about parallel AI efforts, engineer morale, and product management tensions, which suggests the NDA provided sufficient comfort for an open conversation.

**Key detail:** The NDA was in place before this meeting occurred. It was a precondition that had already been handled, not something negotiated during the meeting.

---

## 4. Cisco Laptop Pending

Colin did not have a Cisco laptop at the time of this meeting. The expected timeline mentioned was 1-2 weeks from the meeting date (February 9, 2026). There is a reference to the unnamed BayOne representative mentioning "a call about hardware in the evening" -- suggesting active follow-up was happening same-day to confirm the exact delivery timeline.

The laptop is a hard dependency for any hands-on work. Without it, Colin cannot:
- Access Cisco source code
- Connect to Cisco's internal network
- Use Cisco-licensed AI tools
- Begin any code exploration or POC work

**Timeline stated:** 1-2 weeks from February 9, meaning expected by approximately February 16-23, 2026.

**Open question:** Whether the laptop timeline was confirmed in the evening call referenced by the BayOne representative. This is not captured in the transcript.

---

## 5. Cisco ID Pending

A Cisco ID (badge/identity credentials) was expected to be issued the same day or shortly after the meeting. This is separate from the laptop -- the Cisco ID would provide building access, network authentication, and identity within Cisco's systems.

The transcript shows Colin physically present at Cisco offices during this meeting, but the reference to needing a badge to connect to displays ("use your setup with the badge then you can connect to it") indicates he did not yet have a Cisco badge at the time of the meeting.

**Key statement from an attendee:** "You can use your setup with the badge then you can connect to it" -- directed at Colin, implying that once he has a badge, he will be able to connect to conference room displays and internal infrastructure.

**Timeline stated:** Expected same day or shortly after February 9.

---

## 6. Wi-Fi and WebEx Connectivity Challenges

The meeting itself was disrupted by connectivity issues. Colin could not connect to Cisco's Wi-Fi network (because he did not yet have credentials/badge). This forced him to use his phone as a connectivity workaround, which limited his ability to share content on the conference room display.

The relevant exchange:

- Colin: "Forgive me for my ignorance, because this is my first time... Is there a plug or am I doing the right thing? Or in WebEx?"
- Colin: "I'm in WebEx and I tried to do connected files."
- Response: "You are connected to..."
- Colin: "I'm on my phone because I don't have the Wi-Fi."
- Response: "Then you need to be in this Wi-Fi."
- Response: "Yeah, but it won't let you connect."

The workaround was for Colin to send a PDF document via Teams, which Guhan then pulled up on the display. This is a minor but telling detail: even basic meeting logistics (screen sharing, document presentation) require Cisco network access, which requires Cisco credentials, which Colin did not yet have.

**Practical impact:** Colin's methodology presentation (the code modernization approach with knowledge graphs, agent swarms, etc.) had to be shared as a PDF via Teams rather than presented directly, which may have limited the depth of the walkthrough.

---

## 7. Team NDA/Hardware Requirements

The security constraints apply not just to Colin but to the entire BayOne team that would work on this engagement. This was referenced in the context of scaling beyond the POC.

Colin stated: "For the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go."

The implication is that each BayOne team member joining the engagement would need:
- Individual NDA execution
- A Cisco-provisioned laptop
- A Cisco ID/badge
- Access to Cisco-licensed AI tools

**Open question:** How long does the hardware provisioning pipeline take for additional team members? If the POC succeeds and Guhan wants to scale quickly, the 1-2 week hardware timeline per person could become a bottleneck. This was not discussed in the meeting.

---

## 8. Cloud Instances for Testing

There is a brief mention of cloud infrastructure in the context of Cisco's Azure HD platform (likely Azure Hybrid or Azure-based development platform). Guhan stated: "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that."

This was referenced in the context of the agentic AI platform being built by Meryl's team, not directly as infrastructure for the EPNM-to-EMS conversion work. However, it establishes that Cisco does have cloud instances available for development and testing purposes.

**Open question:** Whether the EPNM-to-EMS conversion work would have access to cloud instances for testing, or whether all testing must occur on local Cisco hardware. The distinction matters for Colin's methodology, which involves running multiple AI agents that may require significant compute resources.

**Open question:** Whether "Azure HD" is Azure Hybrid Developer, Azure DevOps, or another Azure-based platform. The transcript's speech-to-text rendering is ambiguous.

---

## 9. No Downloading Code to Personal Machines

This is the corollary to constraint #1 but worth stating explicitly. The prohibition is not just about where code runs -- it is about code never leaving Cisco's infrastructure at any point. This means:

- No cloning repositories to personal laptops
- No copying code snippets to external tools for analysis
- No using personal SaaS-based AI tools (e.g., ChatGPT web interface, personal Claude account) to analyze code
- No exfiltrating code via email, messaging, or file transfer to non-Cisco systems

This constraint is consistent with standard enterprise security for a company of Cisco's size handling proprietary network management software, but it has specific implications for AI-assisted development workflows where developers often paste code into external AI interfaces.

---

## 10. Physical Access and On-Site Logistics

The meeting took place in person at Cisco offices. Several logistical details emerged:

- **Conference rooms:** Guhan mentioned that a preferred room with "four nice chairs and also a couch" was taken, so they used an alternate room.
- **Display connectivity:** Conference room displays require a Cisco badge to connect. Without a badge, presenters cannot share their screen directly.
- **Colin's physical presence:** Colin stated he would be "here for the next two weeks" and available "in and out, including today." This establishes that Colin was physically located at or near Cisco offices for an extended period, which is relevant for logistics planning.
- **Unnamed BayOne representative** was also physically present and facilitated logistics.

**Key logistics detail:** The 3:00 PM follow-up session with Guhan's team lead was scheduled during this meeting. Guhan stated: "I can introduce and then you can walk through" -- meaning Guhan would make the introduction and then let Colin present his methodology in more technical depth.

---

## Summary of Open Questions and Unresolved Items

1. **What specific AI tools does Cisco have licensed at the enterprise level?** This determines whether Colin's preferred toolchain (Claude Code, LangGraph) can be used or must be substituted.

2. **Was the Cisco laptop delivery timeline confirmed in the evening call?** The BayOne representative referenced a follow-up call about hardware.

3. **How long does hardware provisioning take for additional team members?** If the POC succeeds, scaling the team requires each person to go through the same provisioning pipeline.

4. **Are cloud instances available for the EPNM-to-EMS conversion work specifically?** Cisco has Azure-based infrastructure, but it is unclear if this engagement would have access to it.

5. **What network/VPN access is required for remote work?** Colin mentioned being based in Pennsylvania and working remotely. Once he has a Cisco laptop, does he need VPN access to work from Pennsylvania, or must all work be done on-site?

6. **What are the specific restrictions on AI tool usage within Cisco's security perimeter?** For example, can Cisco-approved tools make external API calls to model providers, or must everything run on-premises?

7. **Does Guhan's team have existing CI/CD infrastructure that would need to be used, or can Colin set up new pipelines on the Cisco hardware?** This relates to how the AI agent swarm would be deployed and run.
