Implement Django issue using multi-agent orchestration with document-based communication and adaptive model selection.

  ## Input

  You will receive an issue number or description from the user.

  ## Workflow

  ### Phase 0: Initialize & Git Setup

  1. Create workflow state in `.django-workflow/issue-{number}/`
  2. Ask user: "Would you like to sync with main before starting? (yes/no)"
  3. Spawn **git-operations-handler** agent:
     Task(
       subagent_type="git-operations-handler",
       description="Git setup for issue",
       prompt="Execute git setup operation for issue {issue_number}.
       Workflow directory: .django-workflow/issue-{number}/
       Sync with main: {user_choice}
       Write output to git-state.md",
       model="haiku"
     )
  4. Read summary from `.django-workflow/issue-{number}/git-state.md` (first 20 lines only)
  5. Extract: branch name, issue state, issue title
  6. If issue CLOSED: Follow git agent's recommendations, WAIT for user decision
  7. Display to user: "✅ Branch created: {branch_name}"

  ### Phase 1-2: Discovery (Parallel Execution)

  Spawn TWO agents in PARALLEL using Promise.all or multiple Task calls in same message:

  [Task 1] documentation-explorer agent
  [Task 2] library-validator agent (if you create this agent)

  **Documentation Explorer:**
  Task(
    subagent_type="docs-explorer",
    description="Explore documentation",
    prompt="Find and validate documentation for issue: {issue_title}
    Search patterns: {extract keywords from issue}
    Workflow directory: .django-workflow/issue-{number}/
    Write output to documentation-findings.md",
    model="haiku"
  )

  Wait for BOTH to complete, then:
  1. Read `.django-workflow/issue-{number}/documentation-findings.md` (first 20 lines)
  2. Display to user: "✅ Documentation explored: {key_finding}"

  ### Phase 4: Planning (CRITICAL - Use Opus!)

  1. Spawn **django-implementation-planner** agent:
     Task(
       subagent_type="django-implementation-planner",
       description="Create implementation plan",
       prompt="Create detailed implementation plan for Issue #{issue_number}

   Issue Title: {title}
   Issue Body: {body}

   Documentation Summary:
   {paste first 20 lines from documentation-findings.md}

   Library Summary:
   {if available, paste summary}

   Workflow directory: .django-workflow/issue-{number}/
   Write output to implementation-plan.md

   CRITICAL: This plan will be shown to user for approval.
   Make it comprehensive, clear, and actionable.",
   model="opus"  // Use Opus for superior planning!
     )

  2. Read `.django-workflow/issue-{number}/implementation-plan.md` (READ FULL FILE, not just summary!)
  3. Display ENTIRE plan to user
  4. Ask user: "Approve this implementation plan? (yes/no/revise)"
  5. **WAIT for user response** - DO NOT PROCEED without approval
  6. If revise: Ask what to change, re-spawn planning agent
  7. If no: Stop workflow
  8. If yes: Continue to next phase

  ### Phase 4.5: Create Draft PR

  1. Spawn **git-operations-handler** agent:
     Task(
       subagent_type="git-operations-handler",
       description="Create draft PR",
       prompt="Execute create_pr operation.
       Workflow directory: .django-workflow/issue-{number}/
       PR title: Draft: {issue_title}
       PR body: Work in progress for Issue #{issue_number}
       Draft: true
       Write output to git-state.md",
       model="haiku"
     )
  2. Read git-state.md for PR URL
  3. Display to user: "✅ Draft PR created: {pr_url}"

  ### Phase 5: Implementation

  **Note:** For initial version, use a single implementation pass. Future: spawn multiple agents for service/view/template

  1. Display to user: "Starting implementation based on approved plan..."
  2. Follow the implementation plan step by step:
  - Create directories and files as specified
  - Implement service layer
  - Create views
  - Add templates
  - Update URLs and settings
  3. After each logical unit (e.g., service layer complete):
  - **ALWAYS use git-operations-handler agent for commits**:
    ```
    Task(
      subagent_type="git-operations-handler",
      description="Commit {unit name}",
      prompt="Execute commit operation.
      Workflow directory: .django-workflow/issue-{number}/
      Commit message: {descriptive message from plan}
      Update git-state.md with commit info",
      model="haiku"
    )
    ```
  - Never use direct `git commit` commands
  4. Write progress to `.django-workflow/issue-{number}/implementation-log.md`

  **IMPORTANT:** If you encounter doubts or edge cases during implementation:
  - Pause implementation
  - Ask user for clarification with specific options
  - Wait for response
  - Document decision
  - Continue with user's guidance

  ### Phase 6: Testing

  1. Run manual tests as defined in plan
  2. If POC: Document that automated tests are not included
  3. Write results to `.django-workflow/issue-{number}/test-results.md`

  ### Phase 7: Final Review

  1. Check Django Team Standards checklist from plan
  2. Verify all files created/modified
  3. Write checklist to `.django-workflow/issue-{number}/final-checklist.md`
  4. Display to user: "Review complete. All standards met."

  ### Phase 8: Finalize PR

  1. **Final commit using git-operations-handler:**
     ```
     Task(
       subagent_type="git-operations-handler",
       description="Final commit and push",
       prompt="Execute commit operation with all remaining changes.
       Workflow directory: .django-workflow/issue-{number}/
       Commit message: {final commit message summarizing all changes}
       Then execute push operation to sync with remote.
       Update git-state.md",
       model="haiku"
     )
     ```

  2. Ask user: "Ready to convert Draft PR to Ready for Review? (yes/no)"

  3. If yes:
  - Generate comprehensive PR description from all workflow documents
  - **Use gh CLI to update PR** (no direct git commands):
    ```bash
    gh pr edit {pr_number} --body "{comprehensive PR description}"
    gh pr ready {pr_number}
    ```

  4. Display PR URL to user

  5. Display cost summary:
     ✅ Implementation Complete!
     💰 Total Cost: ${total}
     ⏱️ Duration: {time}
     🔗 PR: {url}

  **Git Operations Summary:**
  - ✅ All git operations performed via git-operations-handler agent
  - ✅ No direct git commands used
  - ✅ All state tracked in git-state.md

  ## Cost Tracking

  Throughout workflow, track costs in `.django-workflow/issue-{number}/workflow-state.json`:

  ```json
  {
    "cost_tracking": {
   "total_tokens": 95000,
   "total_cost": 0.62,
   "breakdown": {
     "git": {"tokens": 5000, "cost": 0.005},
     "documentation_explorer": {"tokens": 25000, "cost": 0.025},
     "planning": {"tokens": 30000, "cost": 0.45}
   }
    }
  }

  ## Error Handling & User Clarification

  **If any agent fails:**
  1. Display error to user with full context
  2. Ask: "Retry / Skip / Abort?"
  3. If retry: Re-spawn agent once with same parameters
  4. If skip: Continue with warning and document in workflow-state.json
  5. If abort: Stop workflow, preserve all state in .django-workflow/

  **If any agent requests clarification:**
  1. Agent will pause and present options/questions
  2. Display agent's question to user clearly
  3. WAIT for user response (do not assume or auto-select)
  4. Pass user's decision back to agent
  5. Agent resumes with user's guidance
  6. Document decision in workflow-state.json

  **Common scenarios requiring clarification:**
  - Ambiguous requirements in issue
  - Multiple valid technical approaches
  - Edge cases that cannot be auto-planned
  - Security or compliance decisions
  - Breaking changes to existing code
  - New dependency requirements

  Resuming Interrupted Workflows

  If .django-workflow/issue-{number}/workflow-state.json exists:
  1. Ask user: "Found existing workflow. Resume from {current_phase}? (yes/no)"
  2. If yes: Load state and continue from current phase
  3. If no: Start fresh (archive old workflow)

  Key Principles

  1. Minimal Context: Read only first 20 lines of agent outputs (except planning)
  2. User Approvals: Always wait for approval at critical points
  3. Parallel When Possible: Phase 1-2 agents run concurrently
  4. Document Everything: All state in .django-workflow/
  5. Use Right Models: Haiku for simple, Opus for planning, Sonnet for implementation
  6. Cost Conscious: Track and display costs throughout

  Output to User

  Keep user informed at each phase:
  - "🤖 Starting Phase X: {name}"
  - "✅ {agent} complete: {key finding}"
  - "⏳ Waiting for {agent}..."
  - "❓ {question requiring approval}"
  - "💰 Current cost: ${amount}"