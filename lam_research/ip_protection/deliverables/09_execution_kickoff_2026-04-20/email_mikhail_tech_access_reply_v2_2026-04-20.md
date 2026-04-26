**To:** Mikhail Krivenko
**Cc:** Anuj Sehgal, Pratik Sharda, Amit Grover, Daniel Harrison
**Subject:** Re: Confidential Information Detection POC — Option A Technology Access

---

Hi Mikhail,

Thank you for the follow-up. To your question on what specific technologies we would need access to, here is the high-level view. Two items would look different between Option A and Option B, and both paths are called out for those. The remaining items are the same regardless of which path is chosen.

Items that would differ between Option A and Option B:

•    Environment access
o    Option A (Lam environment): hardware/PC provisioning by Lam, the ability to reach the needed files/data, plus access to any artifacts from the prior effort that remain in Azure
o    Option B (BayOne environment): BayOne provides its own hardware and working environment; this path may be worth considering if performant hardware provisioning on Lam's side would be constrained
•    Generative AI endpoint
o    Option A: access to Lam's Azure AI Foundry (or comparable Lam-approved or Lam-provided LLM endpoint); BayOne can help provision if Lam does not currently have one in place
o    Option B: BayOne has an existing Azure AI Foundry instance that could be used; this is one option, not a requirement

Items that are the same regardless of path:

•    Data
o    Escalation Solver export of the five free-text fields, the reference lists (customer names, fab identifiers, acronyms, exclusion list), and the existing thumbs-up/down feedback labels
•    Source control
o    Access to a repository on GitHub or Azure DevOps on Lam's instance, whichever is preferred
•    SME coverage
o    Person(s) who can help define detection targets and objectives, address ambiguity, validate results, and own the authoritative reference sources
•    Communication
o    Your team's preference for engagement communications (Slack, Teams, or other)
•    Two LAM ID accounts; one for myself, plus an additional onshore BayOne AI team member

I will be reaching out to Daniel to work through the specifics per your guidance and will copy you on that thread for visibility.

Looking forward to getting started.

All my best,

Colin
