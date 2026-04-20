# Decisions Log

Last updated after: Team Set 04 (2026-04-16)

| # | Decision | Rationale | Decided By | Date | Source |
|---|----------|-----------|------------|------|--------|
| 1 | Focus on Bazel logs, not Gmake (per Justin recommendation) | Gmake is legacy (nx_main), Bazel is the future (nx_dev). Justin said Gmake logs will be outdated. | Justin, endorsed by Colin | 2026-04-10 | Team 01 |
| 2 | Raise Divakar conflict with Srinivas rather than resolving directly | Srinivas overrules Divakar. Better to get air cover early than hide the issue. | Colin | 2026-04-10 | Team 01 |
| 3 | Frame existing Cisco work (Justin's scripts, Naga's tools) as POCs, not finished products | If it is not in production and people do not depend on it, it is a POC. This positions BayOne to show "what production looks like." | Colin | 2026-04-10 | Team 01 |
| 4 | Do not commit to architecture publicly until logs are inspected firsthand | Architecture decisions should follow understanding, not precede it. Colin explicit: "don't say rearchitecture if you can't talk deeply." | Colin | 2026-04-10 | Team 01 |
| 5 | Weekly Friday standup structure established | General updates, sub-team round-robin, blockers, then Srinivas meeting prep. | Colin | 2026-04-10 | Team 01 |
| 6 | Ask Srinivas to clarify Scribble scope (custom transcription vs. WebEx native) | WebEx already has transcription. Additional cost and complexity of Whisper needs business justification. | Colin/Saurav | 2026-04-10 | Team 01 |
| 7 | Offer Gmake-to-Bazel migration assistance to Srinivas as potential additional scope | Two different build systems for dev vs. prod is significant code debt. Easy win if Cisco is interested. | Colin | 2026-04-10 | Team 01 |
| 8 | Two-tier repo model: ci-cd team repo (official/pristine) vs. personal repos (R&D) | Keeps official deliverables organized and client-visible; personal spaces for experimentation. Srinivas guided this structure. | Colin/Srinivas | 2026-04-15 | Team 02 |
| 9 | Separate manual documentation from API automation as parallel tracks | Manual transcript download available now (Namita demonstrated); API automation is long-term Task 2 goal. One should not block the other. | Colin | 2026-04-16 | Team 02 |
| 10 | Three-diagram architecture framework: current state, problems/recommendations, future state | Plus a master unified vision across all apps. Current state must be grounded in code, not hand-waving. | Colin | 2026-04-16 | Team 04 |
| 11 | Go to Srinivas with recommendations, not questions | "We are the experts here. Here's our recommendation. Pick from the menu." Present batch/real-time/polling options. | Colin | 2026-04-16 | Team 04 |
| 12 | Human-in-the-loop for all AI fixes initially | Classify bugs by severity/criticality/complexity. Never let AI decide if something is complex. Build confidence score from approved past fixes. | Colin | 2026-04-16 | Team 04 |
| 13 | Tool disclosure policy: never mention Claude, say Copilot | Colin will handle all tool attribution questions with Srinivas. | Colin | 2026-04-16 | Team 04 |
