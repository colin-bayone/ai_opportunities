# Behavioral Hard Rules

**This file is mandatory reading at the start of every Singularity invocation.** The skill gates on this file being read before any work proceeds, the same way it gates on the permission check. The stop hook verifies this file exists.

These rules govern how Claude behaves during skill work. They exist because each one was violated at least once, corrected, and documented. They are not suggestions.

---

**B1. One question at a time in interactive discussion.** During any interactive discussion, clarification, or brainstorming, ask ONE question per response. Not two. Not "one question with three parts." If Claude has multiple questions, pick the most critical one, ask it, and queue the rest for follow-up turns. This does not apply to written follow-ups during transcript processing (see structural rule 5 in SKILL.md). **Why:** Batched questions overwhelm the user and produce thin answers. Corrected at least twice.

**B2. No unilateral filtering during exploration.** When the user instructs Claude to explore, inventory, catalog, or search, surface the complete inventory first and await direction before reading, filtering, or prioritizing. Do not use phrases like "most important," "most relevant," or "let me focus on" unless the user has already provided filtering criteria. If new items are discovered, flag them as new before doing anything else. **Why:** Claude reflexively narrows scope to reduce work even when breadth was the explicit instruction. Corrected once.

**B3. Format transcripts before reading.** When any new raw transcript arrives in `source/`, the FIRST action is to format it with `.claude/skills/singularity/scripts/format_transcript.py`. No exceptions. Reading raw single-line speech-to-text transcripts produces poor comprehension and burns tokens. **Why:** Violated twice during reorganization sessions.

**B4. Read reference documents before describing them.** Never describe the structure or content of a reference document without having read it in the current session. Research agent summaries are not substitutes for reading the source. If the file was read earlier but specifics matter now, re-read it. **Why:** Claude fabricated the structure of a reference document from memory and was materially wrong. Corrected 2026-04-09.

**B5. Verify proposals against the research library.** Before proposing any deliverable, plan, or solution component during Flow 6 (Discussion), verify the proposal against the research library. If a prior set explicitly addressed the topic, the proposal must be consistent with what was established. If unsure, re-read the relevant document. Being corrected on something already in the research library is the worst possible failure mode. **Why:** Claude proposed three POC deliverables that directly contradicted information from prior sets it had already processed. Corrected 2026-04-09.

**B6. Do not reinvent proven structure.** When a prior engagement has an established document structure that the user has pointed to as a reference, replicate that structure. Do not ask whether to use it. Do not propose alternatives. The user already made the decision. Adapt for scope if needed, but do not ask permission to follow a designated template. **Why:** Claude asked whether to follow a structure that had been explicitly designated as the reference. Corrected 2026-04-09.

**B7. Align on structure before producing documents.** Before producing any non-trivial deliverable, propose an outline or structural plan and get user approval. This applies to HTML documents, markdown deliverables, proposals, summaries, and presentations. Skipping to production wastes the user's time reviewing work that may be structurally wrong. The outline step is non-negotiable for anything substantial. **Why:** Claude began writing a full HTML document without aligning on structure. Corrected 2026-04-06.

**B8. Decisions require full context.** When presenting a decision to the user about how to handle a file or folder, ALWAYS include: the full path, the file size, a brief summary of actual content (read the file, do not infer from filename), why the decision is needed, and proposed options with explicit recommendations. Vague references ("the pricing docs," "the CEO file") assume user context they do not have. **Why:** Multiple instances of Claude asking the user to decide about files without providing paths, content, or rationale. Corrected 2026-04-13.

**B9. Do not declare work done prematurely.** Never declare a task complete, wish the user good luck, or offer closing sentiments unless the user has explicitly said the work is finished. Status updates should describe what has just been completed and what is still in progress. Default posture: more work remains until the user signals otherwise. **Why:** Claude repeatedly said "you're set" and "good luck" while the user was still actively working. Corrected 2026-04-06.

**B10. Paraphrase and improve, do not record verbatim.** When capturing user input into research documents, paraphrase into professional prose that preserves substance while improving clarity and completeness. Expand brief statements into full reasoning when context supports it. Remove filler, conversational artifacts, and hyperbole. The captured document should read as considered analysis, not a transcript of casual conversation. **Why:** Claude recorded spoken feedback word-for-word including conversational fragments. Corrected 2026-04-06.

**B11. Verify before assuming files are identical.** Hash comparison is fine for confirming identity. Byte-size comparison is NOT a substitute for content comparison. When in doubt, format both files with the script and read both in full. Clever shell pipelines for token efficiency often fail and waste more tokens than just reading the files. **Why:** Claude assumed two files were duplicates because they were "99 bytes different." Corrected 2026-04-13.

**B12. No duplicate source files.** Source folders contain ONE copy of each unique source material. If a file is functionally identical to an existing one, delete the duplicate. Do not preserve "alternates" or "in case we need them later." Duplicates create future confusion about which version is authoritative. **Why:** Claude proposed keeping a duplicate file "as an alternate copy." Corrected 2026-04-13.

**B13. Provide full context and framing when raising items.** When raising a topic for discussion, provide full context (what was said in the source material, who said it, what it means technically), offer Claude's own perspective and analysis, then ask the user for their take. Terse prompts like "Item X: Topic. What do you think?" are inadequate. Setup should be thorough enough that the user could respond substantively. **Why:** Claude's initial format during a brainstorming session was bare-bones labels with no framing. Corrected 2026-04-06.

**B14. Check language standards across all documents.** When anti-patterns are identified in a deliverable, scan the entire document for the same patterns. Do not just fix the specific instance flagged. Anti-patterns cluster because they come from the same default habits. When a problem is found in one client-facing document, check ALL client-facing documents. Do not rely on grep alone. Read each end to end. **Why:** Claude fixed anti-patterns in one document section while the same issues existed in others. Corrected 2026-04-06.

**B15. Bring perspective to brainstorming, do not interview.** In brainstorming and discussion mode, Claude brings substantive perspective, proposals, and analysis. Asking the user to direct the next topic without offering direction or insight is interviewing, not brainstorming. The user wants a thinking partner who has read the research library and contributes specific, informed ideas. Each exchange leads with Claude's perspective and ends with a focused question. Never "what do you want to discuss next?" **Why:** Claude asked the user to direct brainstorming instead of contributing. Corrected 2026-04-06.

**B16. Confirm before executing after multiple corrections.** When the user has corrected Claude multiple times on an approach in the same conversation thread, Claude must explicitly confirm the final agreed approach and get approval before executing. Do not treat a correction as implicit go-ahead. The more corrections that have occurred, the more important confirmation becomes before acting. **Why:** Claude was corrected three times on the enforcement approach and then immediately started executing without confirming the agreed plan. Corrected 2026-04-13.

---

## Rule Violation Protocol

If the user indicates a rule has been violated (phrases like "you broke a rule," "that violates," "we already discussed this," "I told you not to," or similar), Claude must:

1. **Stop current work immediately.** Do not continue the approach that violated the rule.
2. **Re-read this file** (`references/hard_rules.md`) before responding.
3. **Acknowledge the specific rule violated** by number (e.g., "That violated B2 — no unilateral filtering").
4. **Correct course** based on the rule, then continue.

This is not optional. The re-read ensures Claude's next action is grounded in the rules, not in the same pattern that produced the violation.
