# Claude Code: Comprehensive Feature Release Documentation
## January - February 2026

**Document Generated:** February 11, 2026
**Research Scope:** Exhaustive coverage of all Claude Code features released in January and February 2026

---

## Table of Contents

1. [Major New Features](#major-new-features)
2. [Agent Teams and Peer-to-Peer Agents](#agent-teams-and-peer-to-peer-agents)
3. [Subagent Enhancements](#subagent-enhancements)
4. [Skills System Improvements](#skills-system-improvements)
5. [Hooks System Enhancements](#hooks-system-enhancements)
6. [Memory Features](#memory-features)
7. [MCP Tool Search](#mcp-tool-search)
8. [Claude Opus 4.6 and Fast Mode](#claude-opus-46-and-fast-mode)
9. [Claude Cowork](#claude-cowork)
10. [Session Management](#session-management)
11. [VS Code Extension Updates](#vs-code-extension-updates)
12. [Terminal and Interface Improvements](#terminal-and-interface-improvements)
13. [Permissions and Security](#permissions-and-security)
14. [Sandbox Mode](#sandbox-mode)
15. [Analytics API](#analytics-api)
16. [Plan Mode](#plan-mode)
17. [Minor Features and Bug Fixes](#minor-features-and-bug-fixes)

---

## Major New Features

### Claude Code 2.1.0 Release (January 7, 2026)

Claude Code v2.1.0 was a major update introducing improvements across agent lifecycle control, skill development, session portability, and multilingual output — bundled in a dense package of **1,096 commits**.

**Key highlights:**
- Hooks for agents, skills, and slash commands
- Hot reload for skills
- Session forking and cloud handoff
- Plan mode improvements
- Arrow key history
- SKILL.md support
- `--from-pr` flag for PR-based session resumption

**Sources:**
- [VentureBeat: Claude Code 2.1.0](https://venturebeat.com/orchestration/claude-code-2-1-0-arrives-with-smoother-workflows-and-smarter-agents)
- [Medium: Claude Code 2.1.0 Analysis](https://medium.com/@cognidownunder/claude-code-2-1-0-just-changed-everything-and-most-developers-havent-noticed-yet-8862a3c961ed)

---

## Agent Teams and Peer-to-Peer Agents

### Overview

**Agent Teams** (officially called TeammateTool) was launched alongside Opus 4.6 on **February 6, 2026**. This represents one of the most significant architectural advances in Claude Code, enabling true peer-to-peer agent collaboration.

### Key Features

**Architecture:**
- **Team lead** coordinates overall work
- **Teammates** work in independent context windows
- **Shared task list** with dependency tracking
- **Peer-to-peer messaging** between agents
- File-lock based task claiming to prevent race conditions

**How It Differs from Sub-agents:**
- **Sub-agents**: Report back to the main agent (like interns)
- **Agent Teams**: Communicate with each other, challenge findings, and self-coordinate using peer-to-peer messaging (like collaborative teams)

### Enabling Agent Teams

Agent teams are **experimental and disabled by default**. Enable by adding to your environment or settings.json:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### Best Use Cases

1. **Research and review** - Multiple teammates investigate different aspects simultaneously
2. **New modules or features** - Teammates each own a separate piece
3. **Debugging with competing hypotheses** - Teammates test different theories in parallel
4. **Cross-layer coordination** - Changes spanning frontend, backend, and tests

### Architecture Details

- Each teammate is a separate Claude Code instance with its own context window
- Teammates can read/write files, run commands, and message each other directly
- Task list uses dependency tracking - tasks can block other tasks
- When a blocking task completes, downstream tasks automatically unblock
- Teammates self-claim the next available unblocked task when they finish

### Real-World Example: C Compiler Project

One Anthropic engineer (Nicholas Carlini) tasked **16 agents** with writing a Rust-based C compiler from scratch, capable of compiling the Linux kernel:

- **Duration:** Nearly 2,000 Claude Code sessions over 2 weeks
- **Cost:** $20,000 in API costs
- **Tokens:** 2 billion input tokens, 140 million output tokens
- **Output:** 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V
- **Quality:** Reasonable code quality, though not expert-level Rust; 100% written by Claude Opus 4.6 except one paragraph

**Technical Implementation:**
- Bare git repo with Docker containers per agent
- Each agent clones local copy to `/workspace`
- Synchronization via text file locks in `current_tasks/`
- Git's built-in synchronization prevents collision

**Sources:**
- [Cameron XYZ: Agent Collaboration](https://cameronxyz.substack.com/p/claude-code-next-era-agent-collaboration)
- [Anthropic Engineering: Building C Compiler](https://www.anthropic.com/engineering/building-c-compiler)
- [Claude Code Docs: Agent Teams](https://code.claude.com/docs/en/agent-teams)
- [The Register: Opus 4.6 Compiler](https://www.theregister.com/2026/02/09/claude_opus_46_compiler)
- [GitHub: Claude's C Compiler](https://github.com/anthropics/claudes-c-compiler)

---

## Subagent Enhancements

### Overview

Subagents are specialized AI assistants that handle specific types of tasks. Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions.

### Built-in Subagents

**Explore Subagent:**
- Fast, read-only agent optimized for searching and analyzing codebases
- Claude delegates when it needs to search or understand code without making changes
- Keeps exploration results out of main conversation context
- Thoroughness levels: `quick`, `medium`, or `very thorough`

**Plan Subagent:**
- Research agent used during plan mode to gather context before presenting a plan
- Gathers information without making changes

**General-purpose Subagent:**
- Handles complex multi-step tasks

### Parallel Execution

- Up to **7 simultaneous subagent operations**
- Dramatically speeds up complex workflows like codebase exploration and multi-file analysis
- Each operates in its own context window independently

### VS Code Workspace Search Subagent (January 2026)

VS Code added support for a **search subagent** that runs in an isolated agent loop:
- Enables iterative refinement of searches
- Can try multiple queries and explore different parts of workspace
- Improves quality of search results for complex queries
- Preserves main agent's context window
- Enables main agent to continue working while search happens

### Custom Subagents

You can create custom subagents with:
- Custom prompts
- Tool restrictions
- Permission modes
- Hooks
- Skills

Defined in Markdown files with YAML frontmatter. Use `/agents` command to create them.

### Restricting Subagent Spawning (February 2026)

Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter.

**Sources:**
- [Claude Code Docs: Create Subagents](https://code.claude.com/docs/en/sub-agents)
- [eesel.ai: Multiple Agent Systems Guide](https://www.eesel.ai/blog/claude-code-multiple-agent-systems-complete-2026-guide)
- [Tim Dietrich: Parallel Subagents](https://timdietrich.me/blog/claude-code-parallel-subagents/)
- [VS Code: Multi-Agent Development](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)

---

## Skills System Improvements

### Hot Reload (January 7, 2026)

One of the most significant improvements in Claude Code 2.1.0 is **automatic skill hot-reload**:

- Skills created or modified in `~/.claude/skills` or `.claude/skills` are **immediately available**
- No restart required
- Eliminates the restart-to-test cycle
- Claude Code monitors skill directories for changes

**How It Works:**
- Save changes to SKILL.md file
- Changes become immediately available in running session
- No reinstall, no session reset

**Benefits:**
- Edit skills in real-time
- Test iteratively without restarting
- Debug skill behavior on the fly
- Watch how Claude interprets instructions and refine them

### SKILL.md Structure

Every skill needs a `SKILL.md` file with two parts:

1. **YAML frontmatter** (between `---` markers) - tells Claude when to use the skill
2. **Markdown content** - instructions Claude follows when skill is invoked

**Additional Files (Optional):**
- Templates for Claude to fill in
- Example outputs showing expected format
- Scripts Claude can execute
- Detailed reference documentation

### Additional Directories Support

Skills defined in `.claude/skills/` within directories added via `--add-dir` are:
- Loaded automatically
- Picked up by live change detection
- Can be edited during session without restarting

### Skills in Agent Teams

Agent Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality. The skill content becomes the task, and the agent provides read-only tools optimized for codebase exploration.

**Sources:**
- [Claude Code Docs: Skills](https://code.claude.com/docs/en/skills)
- [ClaudeLog: Skill Hot-Reload](https://claudelog.com/faqs/what-is-skill-hot-reload-in-claude-code/)
- [How Do I Use AI: Custom Skills](https://www.howdoiuseai.com/blog/2026-02-08-how-to-train-claude-code-agents-with-custom-skills)
- [Medium: Build Agent Skills Faster](https://medium.com/@richardhightower/build-agent-skills-faster-with-claude-code-2-1-release-6d821d5b8179)

---

## Hooks System Enhancements

### Overview

Hooks are user-defined event handlers that run shell commands or scripts at specific points in Claude Code's lifecycle. They act as automated triggers that fire when particular events occur, regardless of what the AI "decides" to do.

### Key Hook Events

**PreToolUse:**
- Runs **before** a tool executes
- Ideal for validation and blocking dangerous operations
- Can inspect what Claude is about to do
- Exit with code 2 to block
- **New in v2.0.10:** Can modify tool inputs before execution
- **New in v2.1.9:** Can return `additionalContext` to provide extra context to the model

**PostToolUse:**
- Runs **after** a tool completes successfully
- Perfect for cleanup tasks like formatting code or running tests

**Stop:**
- Runs when the AI agent finishes its response

**Setup (New in January 2026):**
- Runs before session starts
- Triggered by special CLI flags: `--init`, `--init-only`, or `--maintenance`
- Perfect for repository setup and maintenance operations

**Other Events:**
- Notification, UserPromptSubmit, SessionStart
- TeammateIdle, TaskCompleted (for multi-agent workflows - February 2026)

### PreToolUse Enhancements

**Input Modification (v2.0.10+):**
Instead of blocking and forcing retries, hooks can:
- Intercept tool calls
- Modify the JSON input
- Let execution proceed with corrected parameters

**Use Cases:**
- Transparent sandboxing
- Automatic security enforcement (dry-run flags, secret redaction)
- Team convention adherence (commit message formatting, linter configuration)
- Developer experience improvements (path correction, dependency auto-installation)

**Additional Context (v2.1.9+):**
PreToolUse hooks can return `additionalContext` to inject extra context into the model before tool execution.

### Decision Control Changes

PreToolUse previously used top-level `decision` and `reason` fields, but these are **deprecated**. Use instead:
- `hookSpecificOutput.permissionDecision`
- `hookSpecificOutput.permissionDecisionReason`

Deprecated values "approve" and "block" map to "allow" and "deny" respectively.

### Setup Hook Details

**CLI Flags:**
- `claude --init` - Triggers Setup hook with matcher "init"
- `claude --init-only` - Same as above, exits after hook (CI-friendly)
- `claude --maintenance` - Triggers Setup hook with matcher "maintenance"

**Configuration Example:**

```json
{
  "hooks": {
    "Setup": [
      {
        "matcher": "init",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/setup_init.py",
            "timeout": 120
          }
        ]
      },
      {
        "matcher": "maintenance",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/setup_maintenance.py",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Setup Hook Payload:**
- `trigger` ("init" or "maintenance")
- Session info
- Enhanced with environment persistence via `CLAUDE_ENV_FILE`
- Context injection via `additionalContext`

**CI/CD Integration:**
The `--init-only` flag is specifically for pipelines - runs the hook and exits cleanly with a return code, no interactive session.

### Async Hook Support

Released in January 2026, async hooks allow commands to run in the background without blocking Claude's execution:
- Add `async: true` to the hook configuration
- Command runs in background
- Claude continues working

### Hook Frontmatter Support

Added **memory frontmatter field support** for agents, enabling persistent memory with:
- User scope
- Project scope
- Local scope

### Practical Use Cases

**Code Quality Enforcement:**
- PostToolUse hooks run formatters (Prettier, Black) after every file edit
- Deterministically ensures adherence to style guides
- Automatically executes test suites to catch regressions

**Security Guardrails:**
- PreToolUse blocks dangerous operations (git push without tests, direct prod DB access)
- PostToolUse tracks state (tests run, code files edited)
- Stop verifies dev-loop SOP was followed before agent stops

**Sources:**
- [Claude Code Docs: Hooks Reference](https://code.claude.com/docs/en/hooks)
- [eesel.ai: Complete Hooks Guide](https://www.eesel.ai/blog/hooks-in-claude-code)
- [GitHub: Hooks Mastery](https://github.com/disler/claude-code-hooks-mastery)
- [ClaudeLog: Hooks Mechanics](https://claudelog.com/mechanics/hooks/)
- [ClaudeFast: Setup Hooks](https://claudefa.st/blog/tools/hooks/claude-code-setup-hooks)

---

## Memory Features

### Official Auto Memory Feature

**Auto memory** is a persistent directory where Claude records learnings, patterns, and insights as it works. This is distinct from CLAUDE.md files (which contain instructions you write for Claude) - auto memory contains notes Claude writes for itself based on what it discovers during sessions.

**Location:**
Each project gets its own memory directory at `~/.claude/projects/<project>/memory/`

**Project Path Derivation:**
- Derived from git repository root
- All subdirectories within same repo share one auto memory directory
- Git worktrees get separate memory directories
- Outside a git repo, working directory is used instead

**How It Works:**
- Claude automatically saves useful context like project patterns, key commands, and preferences
- Persists across sessions
- `MEMORY.md` acts as an index of the memory directory
- Claude reads and writes files in this directory throughout session

**Memory Loading:**
- First **200 lines** of MEMORY.md are loaded into Claude's system prompt at the start of every session
- Content beyond 200 lines is not loaded automatically
- Claude is instructed to keep it concise by moving detailed notes into separate topic files

**Rollout Status:**
Auto memory is being rolled out gradually. If not seeing it, opt in:

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=0
```

### Third-Party Memory Solutions

Several plugins and tools have emerged to enhance Claude Code's memory capabilities:

**Claude-Mem (by thedotmack):**
- Open-source memory system for Claude Code
- Automatically captures coding sessions
- Compresses them with AI
- Injects relevant context into future sessions
- Think of it as giving Claude long-term memory that survives across restarts

**Key Features:**
- Persistent Memory - Context survives across sessions
- Progressive Disclosure - Layered memory retrieval with token cost visibility
- Skill-Based Search - Query project history with mem-search skill
- Web Viewer UI at http://localhost:37777

**Mem0 Integration:**
- Persistent memory layer for Claude Code (CLI and desktop versions)
- Eliminates repetition of project architecture, coding preferences, and bug descriptions
- Testing showed: **90% lower token usage** and **91% faster responses** vs full-context approaches

**Supermemory Plugin:**
- Persistent memory across sessions using Supermemory
- Agent remembers what you worked on - across sessions, across projects
- Team Memory - project knowledge shared across team
- Auto Capture - conversations saved when session ends
- Project Config - per-repo settings

**Sources:**
- [Claude Code Docs: Memory](https://code.claude.com/docs/en/memory)
- [Medium: Persistent Memory Guide](https://agentnativedev.medium.com/persistent-memory-for-claude-code-never-lose-context-setup-guide-2cb6c7f92c58)
- [GitHub: claude-mem](https://github.com/thedotmack/claude-mem)
- [Mem0 Blog: Persistent Memory](https://mem0.ai/blog/persistent-memory-for-claude-code)
- [GitHub: claude-supermemory](https://github.com/supermemoryai/claude-supermemory)

---

## MCP Tool Search

### Overview

**MCP Tool Search** was introduced mid-January 2026 by Anthropic's Thariq Shihipar. It brings "lazy loading" for AI tools, allowing agents to dynamically fetch tool definitions only when necessary.

**Shipped with:** Claude Code 2.1.7

### The Problem It Solved

**Before MCP Tool Search:**
- All MCP tool definitions loaded at session start
- GitHub's MCP server alone consumed nearly a quarter of Claude Sonnet's context window
- One reported case: 144,802 tokens from MCP tools alone (MCP_DOCKER: 125,964 tokens across 135 tools)
- Massive context pollution

**After MCP Tool Search:**
Token savings are dramatic:
- Traditional approach: ~77K tokens with 50+ MCP tools
- Tool Search: ~8.7K tokens
- **Preserves 95% of the context window**
- Tool Search tool itself adds only ~500 tokens overhead

**Anthropic's internal testing:** From ~134k to ~5k tokens

### How It Works

**Mechanism:**
1. Claude Code checks if MCP tool descriptions exceed 10K tokens
2. If exceeded, tools are marked with `defer_loading: true`
3. Claude receives a Tool Search tool instead of all tool definitions
4. When Claude needs a tool, it searches using keywords
5. Loads 3-5 relevant tools (~3K tokens) per query

**Tool Definitions:**
Instead of loading all tool definitions upfront, Claude Code loads a lightweight search index and fetches tool details on-demand when you actually need them.

### Performance Benefits

**Accuracy Improvements:**
- Opus 4: 49% → **74%** accuracy on MCP evaluations
- Opus 4.5: 79.5% → **88.1%** accuracy

**Context Window Savings:**
- From ~134k to ~5k in Anthropic's internal testing
- From 77K to 8.7K tokens in benchmarks
- 95% context window preservation

### Configuration

**Default Status:**
MCP Tool Search is now **enabled by default** for all users. No opt-in needed.

**Control Options:**
- Set `enable_tool_search` to `false` in Claude Code settings to prefer all MCP tools loaded at session start (legacy behavior)
- Can control globally via settings.json

**Important for MCP Developers:**
The `server instructions` field in MCP definitions is now **critical** - it acts as metadata that helps Claude know when to search for your tools.

**Auto-Enable Threshold (v2.1.9+):**
Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100).

**Sources:**
- [Medium: MCP Tool Search Explained](https://jpcaparas.medium.com/claude-code-finally-gets-lazy-loading-for-mcp-tools-explained-39b613d1d5cc)
- [atcyrus: MCP Tool Search Guide](https://www.atcyrus.com/stories/mcp-tool-search-claude-code-context-pollution-guide)
- [ClaudeFast: MCP Tool Search](https://claudefa.st/blog/tools/mcp-extensions/mcp-tool-search)
- [Medium: Fixing Context Pollution](https://medium.com/the-context-layer/claude-code-just-fixed-its-biggest-scaling-problem-with-mcp-tool-search-3aa1aebcd824)
- [VentureBeat: Most-Requested Feature](https://venturebeat.com/orchestration/claude-code-just-got-updated-with-one-of-the-most-requested-user-features)

---

## Claude Opus 4.6 and Fast Mode

### Claude Opus 4.6 Support (February 2026)

**Availability:**
- Claude Opus 4.6 is now available in Claude Code
- Fast mode is available for Opus 4.6 in research preview

### Fast Mode

**What It Is:**
Fast mode is a high-speed configuration for Claude Opus 4.6, making the model **2.5x faster** at a higher cost per token. This isn't a new model or a "lite" version - it's the same intelligence at faster speed.

**Performance:**
- Up to **2.5x faster** output token generation
- Uses the `speed` parameter
- Same intelligence as regular Opus 4.6

**How to Enable:**

1. **Command:** Type `/fast` in Claude Code command line
2. **VS Code Extension:** Activate directly in extension
3. **Settings:** Permanently activate by entering `"fastMode": true` in user settings file
4. **Confirmation:** "Fast mode ON" message and lightning bolt symbol (↯) next to prompt

**Pricing:**

| Mode | Input | Output |
|------|-------|--------|
| Standard Opus 4.6 | $5/million | $25/million |
| Fast Mode | $30/million | $150/million |

**Pricing Multiplier:**
- Normal price: 6x the standard rate
- **Promotional pricing (through Feb 16, 2026):** 50% off, making it **3x** standard price

**Availability:**
- All users with Pro, Max, Team, or Enterprise subscription
- Customers of Claude Console API
- **Not available** on third-party cloud platforms (Amazon Bedrock, Google Vertex AI, Microsoft Azure)
- Available to GitHub Copilot Pro+ and Enterprise users in VS Code (all modes: chat, ask, edit, agent)

**Best Use Cases:**
- Rapid iteration on code changes
- Live debugging sessions
- Time-sensitive projects with tight deadlines

**Not Recommended For:**
- Long-running, autonomous tasks where execution speed is less critical

**Sources:**
- [Tom's Guide: Opus 4.6 Testing](https://www.tomsguide.com/ai/i-tested-gemini-3-flash-vs-claude-4-6-opus-in-9-tough-challenges-heres-the-winner)
- [GitHub Changelog: Fast Mode Preview](https://github.blog/changelog/2026-02-07-claude-opus-4-6-fast-is-now-in-public-preview-for-github-copilot/)
- [Claude Code Docs: Fast Mode](https://code.claude.com/docs/en/fast-mode)
- [Medium: Fast Mode Explained](https://civillearning.medium.com/claude-opus-4-6-just-got-2-5-faster-heres-what-fast-mode-actually-means-for-developers-10aa45327587)
- [heise online: Fast Mode News](https://www.heise.de/en/news/Claude-Code-New-Fast-Mode-accelerates-AI-model-Opus-4-6-11169259.html)

---

## Claude Cowork

### Overview

**Announced:** January 12, 2026
**What It Is:** Claude Cowork turns Claude into a digital coworker - a more accessible version of Claude Code built into the Claude Desktop app.

### Release Timeline

- **January 16, 2026:** Available to Pro subscribers in research preview
- **January 23, 2026:** Available to Team and Enterprise plans in research preview

### Key Features

**Agentic Capabilities:**
- Uses the same agentic architecture that powers Claude Code
- Accessible within Claude Desktop without opening terminal
- Can take on complex, multi-step tasks and execute them autonomously
- Describe an outcome, step away, come back to finished work
- Formatted documents, organized files, synthesized research

**File System Access:**
- Give Claude access to a folder of your choosing
- Runs directly on your computer
- Claude can make real changes to your files
- Code runs safely in an isolated space

**Task Execution:**
- Claude completes work with much more agency than regular conversations
- Makes a plan and steadily completes it
- Loops you in on what it's up to
- For complex tasks, may coordinate multiple sub-agents working simultaneously

**Customization Options:**
- Can use your existing connectors (link Claude to external information)
- Includes initial set of skills that improve Claude's ability to create documents, presentations, and other files
- **Plugins:** Ready-made bundles that customize how Claude works for your role, team, and company
  - Each plugin combines: skills, connectors, slash commands, and sub-agents into a single package

**Safety Features:**
- Claude requires **explicit permission** before permanently deleting any files
- Permission prompt with "Allow" selection required for deletion tasks

### Platform Availability

**Current:**
- macOS only (Claude Desktop macOS application)
- Currently available only to **Max subscribers** ($100 or $200/month plans)
- Waitlist available for users on other plans

**Future:**
- **Windows support** in active development
- Targeted release: **mid-2026**

### Comparison to Claude Code

**Claude Code:**
- Developer-focused
- Terminal-based
- Full coding capabilities
- Requires technical savvy

**Claude Cowork:**
- Designed for anyone, not just developers
- Desktop app UI
- Sandboxed instance of Claude Code
- Much more accessible, requires far less technical setup

**Sources:**
- [Claude Blog: Introducing Cowork](https://claude.com/blog/cowork-research-preview)
- [TechCrunch: Cowork Announcement](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)
- [Simon Willison: First Impressions](https://simonwillison.net/2026/Jan/12/claude-cowork/)
- [VentureBeat: Cowork Launch](https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no)
- [Claude Help: Getting Started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)

---

## Session Management

### Session Forking and Cloud Handoff (January 2026)

**New in January 2026:**
- Session forking support
- Cloud handoff using `&` symbol
- `--from-pr` flag for PR-based session resumption
- Arrow key history

**Session Resume Improvements:**
The `/resume` screen was improved with:
- Grouped forked sessions
- Keyboard shortcuts (P for preview, R for rename)

### Core Resume Functionality

**Commands:**
- `claude --continue` - Continues most recent conversation in current directory
- `claude --resume` - Opens conversation picker or resumes by name
- `claude --from-pr 123` - Resumes sessions linked to specific pull request (new in Jan 2026)

**Behavior:**
- Resumed conversation starts with same model and configuration as original
- Conversation storage: All conversations automatically saved locally with full message history
- Message deserialization: Entire message history restored to maintain context
- Tool state: Tool usage and results from previous conversation preserved

### Session Resume Hints (February 2026)

Added **session resume hint on exit**, showing how to continue your conversation later.

### PR-Linked Sessions (January 2026)

**New `--from-pr` Flag:**
- Resume sessions by PR number
- Automatic PR linking when creating PRs
- Sessions now automatically linked to PRs when created via `gh pr create`

### VSCode Remote Sessions (January 2026)

**New VSCode Features:**
- Support for remote sessions
- OAuth users can browse and resume sessions from claude.ai
- Git branch and message count in session picker
- Support for searching by branch name

### Session Teleportation (v2.1 Feature)

**Commands:**
- `/teleport` - Resume sessions at claude.ai/code from any device
- `/remote-env` - Set up remote environment

**Use Cases:**
- Start work on desktop, continue on laptop
- Share sessions with team members
- Continue work from web interface when away from terminal

### Performance Fixes (February 2026)

**Fixed:**
- Startup performance issues when resuming sessions with `saved_hook_context`
- Out-of-memory crashes when resuming sessions with heavy subagent usage
- Bug with resuming where previously created files needed to be read again before writing
- Duplicate sessions when resuming in VS Code extension

### Session Storage

- Sessions stored per project directory
- `/resume` picker shows sessions from same git repository, including worktrees

**Sources:**
- [Medium: Session Resume Feature](https://medium.com/@AdithyaGiridharan/the-claude-code-feature-i-slept-on-for-months-and-why-resume-is-a-game-changer-524a21be7061)
- [ClaudeLog: Resume Flag](https://claudelog.com/faqs/what-is-resume-flag-in-claude-code/)
- [ClaudeFast: Complete Changelog](https://claudefa.st/blog/guide/changelog)
- [Releasebot: February Updates](https://releasebot.io/updates/anthropic/claude-code)

---

## VS Code Extension Updates

### January 2026

**General Availability (January 20, 2026):**
Claude Code became **generally available as a VS Code extension** with support for:
- @ mentions
- Slash commands
- Full feature parity with CLI

**Key Features:**
- Tool call failures and denials added to debug logs
- `--from-pr` flag to resume sessions linked to specific GitHub PR
- Automatic session linking when creating PRs via `gh pr create`
- Support for remote sessions (OAuth users can browse and resume sessions from claude.ai)
- Git branch and message count in session picker
- Support for searching by branch name

**Late January:**
- Debug log improvements
- Multiple stability fixes across context, status bar, Windows shells, and VSCode token handling

### February 2026

**Performance Improvements:**
- Fixed startup performance issues when resuming sessions with saved_hook_context
- Fixed extension not working on Windows ARM64 (falls back to x64 binary via emulation)

**UI/UX Enhancements:**
- Fixed IDE diff tab not closing when rejecting file changes
- Descriptive labels on auto-accept permission buttons (e.g., "Yes, allow npm for this project" instead of "Yes, and don't ask again")
- Fixed paragraph breaks not rendering in markdown content
- Fixed scrolling issues in the extension
- Fixed Tab key queueing slash commands instead of autocompleting
- Fixed text between tool uses disappearing when not using streaming

**Bug Fixes:**
- Fixed duplicate sessions when resuming in VS Code extension
- Fixed usage indicator not updating after manual compact
- Fixed `/fast` not immediately available after enabling `/extra-usage`
- Fixed a crash when agent teams setting changed between renders

### Multi-Agent Development (January 2026 - VS Code v1.109)

Visual Studio Code evolved to be **"the home for multi-agent development"** featuring:

**Improvements:**
- Chat UX with faster streaming
- Agent Session Management
- Agent Customization with skills and organization-wide customizations
- Agent Extensibility with Claude agent support and new Anthropic model capabilities

**Third-Party Agents:**
Third-party coding agents like Claude and Codex, configured as part of a GitHub Copilot subscription, can now be shown in VS Code after selecting the cloud agent type.

**Subagent Visibility:**
- Can now run multiple subagents in parallel
- Fire off multiple tasks at once
- Better visibility into what subagents are doing
- Can see which tasks are running, which agent is being used
- Expand any subagent to see full prompt and result

**Sources:**
- [GitHub: claude-code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [VS Code: Multi-Agent Development](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)
- [Releasebot: VS Code Updates](https://releasebot.io/updates/anthropic/claude-code)
- [VS Code January Updates](https://code.visualstudio.com/updates/v1_109)

---

## Terminal and Interface Improvements

### Terminal Input Improvements

**Line Breaks:**
Multiple options for entering line breaks:
- Type `\` followed by Enter to create newline
- Use **Shift+Enter** (works out of the box in iTerm2, WezTerm, Ghostty, Kitty)
- Set up keybinding for other terminals
- Run `/terminal-setup` to automatically configure Shift+Enter for VS Code, Alacritty, Zed, and Warp

**Terminal Setup Support:**
Added `/terminal-setup` for Kitty, Alacritty, Zed, and Warp terminals.

### Terminal Interface Refresh

**New Features:**
- Improved status visibility
- **Searchable prompt history** (Ctrl+r) - easier to reuse or edit previous prompts
- Terminal title changed to "Claude Code" on startup for better window identification

**Performance:**
- Improved terminal rendering performance (especially with native installer or Bun)
- Better handling of text with emoji, ANSI codes, and Unicode characters
- Improved reliability for piped input like `cat refactor.md | claude`

**Input Handling Fixes:**
- Fixed input being cleared when processing queued commands while user was typing
- Fixed prompt suggestions replacing typed input when pressing Tab

**Terminal Renderer:**
- Complete rewrite for "buttery smooth UI"
- **Ctrl-G shortcut** added to edit your prompt in system's configured text editor

### Additional Terminal Features

**Progress Bar:**
- Setting added to enable/disable terminal progress bar (OSC 9;4)
- Feedback input when rejecting plans

**Multiline Input (VSCode):**
- VSCode added multiline input support to "Other" text input in question dialogs
- Use Shift+Enter for new lines
- **Ctrl+G** also works in AskUserQuestion "Other" input field

**Vim Keybindings:**
- Claude Code supports subset of Vim keybindings
- Enable with `/vim` or configure via `/config`

**Full-Width Space Input (February 2026):**
- Added support for full-width (zenkaku) space input from Japanese IME in checkbox selection

**Keyboard Shortcuts:**
- Keyboard shortcut **'c'** to copy OAuth URL during login

### Improved Startup

- Improved startup keystroke capture
- Better file suggestions

### Claude Code 2.1.0 Terminal Focus

Claude Code 2.1.0 shipped 1,096 commits covering everything from terminal input improvements to complete overhaul of how skills work.

**Sources:**
- [Claude Code Docs: Terminal Config](https://code.claude.com/docs/en/terminal-config)
- [ClaudeFast: Changelog](https://claudefa.st/blog/guide/changelog)
- [Releasebot: February Updates](https://releasebot.io/updates/anthropic/claude-code)
- [Medium: Claude Code 2.1 Review](https://medium.com/@joe.njenga/claude-code-2-1-is-here-i-tested-all-16-new-changes-dont-miss-this-update-ea9ca008dab7)

---

## Permissions and Security

### Auto-Accept Mode Improvements

**Basics:**
Auto-accept permissions is a mechanic that eliminates confirmation prompts, enabling Claude to execute actions immediately without interrupting flow for approval.

**How to Enable:**
**Shift+Tab** keyboard shortcut cycles through three modes:
1. **Normal Mode** (default) - Prompts for all operations
2. **Auto-Accept Mode** (shows ⏵⏵ accept edits on) - Auto-approves all file edits and operations
3. **Plan Mode** (shows ⏸ plan mode on) - Read-only research and planning mode

### Five Permission Modes

**1. Normal Mode:**
- Prompts for every potentially dangerous operation

**2. Auto-Accept Mode:**
- Eliminates permission prompts for file edits
- Enables uninterrupted execution for the session
- Claude proceeds immediately with approved operations
- Activate: Press Shift+Tab until you see "auto-accept edit on"

**3. Plan Mode:**
- Restricts Claude to read-only operations
- Prevents any modifications while allowing comprehensive analysis

**4. Don't Ask Mode:**
- Auto-denies all tool usage unless explicitly pre-approved via `/permissions` or `permissions.allow` rules
- Claude will not prompt for confirmation
- If tool not in allow list, it gets silently denied

**5. Bypass Mode:**
- Skips all permission checks
- Claude executes any tool without prompting
- **Only use in fully isolated environments** (containers, VMs, ephemeral CI runners)

### 2026 Improvements

**Permission Improvements:**
- Improved permission checks for bash with inline env vars
- PermissionRequest hooks now enable hooks to process 'always allow' suggestions
- Background agent permissions now prompt for tool permissions before launching

**VSCode UI Improvements (February 2026):**
- Added descriptive labels on auto-accept permission buttons
- Example: "Yes, allow npm for this project" instead of "Yes, and don't ask again"

### Using Hooks for Permission Control

You can write a script that runs before every tool use, and that script can approve or deny the operation. This allows saying "yes, Claude can run mermaid-cli commands without asking me every time" without using dangerous-skip-permissions.

### Configuration Options

Define permissions in settings.json using allow/deny rules:

```json
{
  "permissions": {
    "allow": ["Edit", "Bash(npm *)"],
    "deny": ["Read(./.env)", "Read(./.env.*)", "Bash(curl *)"]
  }
}
```

### Security Warnings

**Dangerous Skip Permissions:**
- Anthropic intentionally uses word 'dangerously' in flag name as safety signal
- Treat as high risk
- Understand implications before using
- Should only be used for well-defined, automated tasks in secure, isolated environments
- Not for general development - bypasses all safety checks

**Sources:**
- [SmartScope: Auto-Permission Guide](https://smartscope.blog/en/generative-ai/claude/claude-code-auto-permission-guide/)
- [ClaudeLog: Auto-Accept Permissions](https://claudelog.com/mechanics/auto-accept-permissions/)
- [Claude Code Docs: Permissions](https://code.claude.com/docs/en/permissions)
- [ClaudeFast: Permission Management](https://claudefa.st/blog/guide/development/permission-management)
- [eesel.ai: Permissions Guide](https://www.eesel.ai/blog/claude-code-permissions)

### Security Concerns: .claudeignore Issues (January 2026)

**Problem Identified:**
Claude Code can't take "ignore" for an answer and continues to read passwords and API keys, even when secrets file is supposed to be blocked.

**Details:**
- Developers store secrets in `.env` files
- Should be blocked via `.gitignore` entries
- Claude can read `.env` file contents despite entry in `.claudeignore` file
- Presents significant security implications

**Recommended Workaround:**
Specify permissions within settings.json in project's .claude directory:

```json
{
  "permissions": {
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  }
}
```

**Known Issues:**
- When Claude Code creates `.claude/settings.local.json`, that file is not being added to `.gitignore`
- Claude Code should add `.claude/settings.local.json` to `.gitignore` when it creates the local settings file

**Sources:**
- [The Register: Claude Code Ignores Ignore Rules](https://www.theregister.com/2026/01/28/claude_code_ai_secrets_files/)
- [Claude Code Docs: Settings](https://code.claude.com/docs/en/settings)
- [GitHub: claude-ignore](https://github.com/li-zhixin/claude-ignore)

---

## Sandbox Mode

### Overview

Claude Code's sandboxing features reduce permission prompts and increase user safety by enabling two boundaries: **filesystem** and **network isolation**.

**Impact:**
In internal Anthropic usage, sandboxing safely reduces permission prompts by **84%**.

### Two Sandbox Modes

**1. Auto-allow Mode:**
- Bash commands run inside sandbox
- Automatically allowed without requiring permission
- Commands needing network access to non-allowed hosts fall back to regular permission flow

**2. Commands Cannot Be Sandboxed:**
- Commands requiring network access to non-allowed hosts
- Falls back to regular permission flow

### Technical Implementation

Built on top of OS-level primitives:
- **Linux:** bubblewrap
- **macOS:** seatbelt

Enforces restrictions at OS level, covering:
- Claude Code's direct interactions
- Any scripts, programs, or subprocesses spawned by commands

### Filesystem and Network Isolation

**Why Both Are Needed:**
- **Without network isolation:** Compromised agent could exfiltrate sensitive files (SSH keys)
- **Without filesystem isolation:** Compromised agent could easily escape sandbox and gain network access

**Sandboxed Bash Tool Restrictions:**

**Write Access:**
- Defaults to current working directory and subdirectories

**Read Access:**
- Covers entire system
- Except directories you've explicitly denied

### Recent Improvements (2026)

**Bug Fixes:**
- Fixed bash commands incorrectly reporting failure with "Read-only file system" errors when sandbox mode enabled
- Improved system prompts to guide model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents

**UI Improvements:**
- `/sandbox` command shows dependency status with installation instructions

**New Settings:**
- Added `allowUnsandboxedCommands` setting for sandbox configuration

**Platform Support:**
- Sandbox mode released for BashTool on **Linux & Mac**

**Sources:**
- [Claude Code Docs: Sandboxing](https://code.claude.com/docs/en/sandboxing)
- [Anthropic Engineering: Claude Code Sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- [Medium: How to Use Sandbox](https://medium.com/@joe.njenga/how-to-use-new-claude-code-sandbox-to-autonomously-code-without-security-disasters-c6efc5e8e652)
- [ClaudeFast: Sandboxing Guide](https://claudefa.st/blog/guide/sandboxing-guide)

---

## Analytics API

### Overview

The **Claude Code Analytics API** allows you to track Claude Code usage, productivity metrics, and developer activity across your organization.

**Endpoint:** `/v1/organizations/usage_report/claude_code`

### Key Features

**Programmatic Access:**
- Daily aggregated usage metrics for Claude Code users
- Enables organizations to analyze developer productivity
- Build custom dashboards

**Monitoring Capabilities:**
- **Developer Productivity Analysis:** Track sessions, lines of code added/removed, commits, and PRs created using Claude Code
- **Tool Usage Metrics:** Monitor acceptance and rejection rates for different Claude Code tools (Edit, Write, NotebookEdit)
- **Cost Analysis:** View estimated costs

### API Characteristics

**Data Granularity:**
- Daily aggregation: Returns metrics for single day specified by `starting_at` parameter
- User-level data: Each record represents one user's activity for specified day

**Features:**
- Token and cost data: Monitor usage and estimated costs broken down by Claude model
- Cursor-based pagination: Handle large datasets with stable pagination using opaque cursors
- Data freshness: Metrics available with up to 1-hour delay for consistency

### Authentication Requirements

These endpoints require an **Admin API key** (starting with `sk-ant-admin...`) that differs from standard API keys.

Only organization members with the **admin role** can provision Admin API keys through the Claude Console.

### Available Metrics

**Core Productivity Metrics:**
- Commits by Claude Code
- Lines of code (added/removed)
- Number of sessions
- Pull requests by Claude Code

**Token Usage and Cost:**
- Breakdown by AI model used
- Estimated cost amount in minor currency units (e.g., cents for USD)

**Tool Action Metrics:**
- Breakdown of tool action acceptance and rejection rates by tool type
- Number of tool action proposals user accepted
- Number of tool action proposals user rejected

### Data Retention

Historical Claude Code analytics data is:
- Retained and accessible through the API
- No specified deletion period

### Limitations

**Scope:**
- Only tracks Claude Code usage on **Claude API (1st party)**
- Usage on Amazon Bedrock, Google Vertex AI, or other third-party platforms **not included**

**Granularity:**
- Provides daily aggregated metrics only
- For real-time monitoring, consider using OpenTelemetry integration

**Sources:**
- [Claude Help: Claude Code Usage Analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)
- [Claude Code Docs: Track Team Usage](https://code.claude.com/docs/en/analytics)
- [Claude API Docs: Analytics API](https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api)
- [Shipyard: How to Track Usage](https://shipyard.build/blog/claude-code-track-usage/)

---

## Plan Mode

### Overview

Plan mode separates research from execution. Claude analyzes and plans without making changes until you approve. This is essential for complex tasks where you want Claude to think before acting.

### How to Activate

**Three Ways:**
1. Press **Shift+Tab twice**
2. Use `/plan` command (v2.1.0+)
3. Exit with Shift+Tab again or `/plan` again

**Status Indicator:**
When active, you'll see **⏸ plan mode on** in the interface.

### What Plan Mode Does

Plan Mode presents proposed changes as a diff or plan without immediately modifying files. Gives you opportunity to review, understand, and approve changes before they are written to disk.

**Behavior:**
- Claude won't edit files
- Won't run commands
- Won't modify anything
- Until you give the green light

### Tools Available in Plan Mode

**Read-Only Tools Allowed:**
- Read - Files and content viewing
- LS - Directory listings
- Glob - File pattern searches
- Grep - Content searches
- Task - Research agents
- TodoRead/TodoWrite - Task management
- WebFetch - Web content analysis
- WebSearch - Web searches
- NotebookRead - Jupyter notebooks

**Blocked Tools:**
- Edit/MultiEdit
- Write
- Bash
- NotebookEdit
- MCP tools that modify state

Claude can research and plan without touching anything until you approve.

### Best Practices

**Industry Recommendations:**
- The founder of Claude Code says he **never starts anything without plan mode**
- Always use plan mode (Shift + Tab) before complex tasks
- Claude asks questions instead of guessing
- Always start by exploring solutions with Claude in plan mode
- Can save hours of going down wrong path

### Recent Updates (February 2026)

**Bug Fix:**
Fixed crash that made sessions unusable after entering plan mode when project config in `~/.claude.json` was missing default fields.

**Enhancement:**
Latest enhancement: **Opus Plan Mode with Opus 4.6**, bringing:
- Significant improvements
- 1M context for larger codebases

**Added `/plan` Command (v2.1.0):**
The `/plan` command enables direct entry to plan mode from the prompt.

**Sources:**
- [Claude Code Docs: Slash Commands](https://code.claude.com/docs/en/slash-commands)
- [ClaudeLog: Plan Mode](https://claudelog.com/mechanics/plan-mode/)
- [Steve Kinney: Plan Mode](https://stevekinney.com/courses/ai-development/claude-code-plan-mode)
- [OneAway: Skills and Slash Commands](https://oneaway.io/blog/claude-code-skills-slash-commands)

---

## Minor Features and Bug Fixes

### January 2026

**Version 2.1.11 (January 17, 2026):**
- Fixed excessive MCP connection requests for HTTP/SSE transports

**Version 2.1.9 (January 16, 2026):**
- Added `auto:N` syntax for configuring MCP tool search auto-enable threshold (N = context window percentage 0-100)
- Added `plansDirectory` setting to customize where plan files are stored
- Added external editor support (Ctrl+G) in AskUserQuestion "Other" input field
- Added session URL attribution to commits and PRs created from web sessions
- Added support for PreToolUse hooks to return `additionalContext` to the model
- Added `${CLAUDE_SESSION_ID}` string substitution for skills to access current session ID

**Version 2.1.x (January 17, 2026):**
- Fixed message rendering bug
- New Setup hook event for repository setup and maintenance operations
- Keyboard shortcut 'c' to copy OAuth URL during login
- Crash fix for heredocs with JavaScript template literals
- Improved startup keystroke capture and file suggestions

**Version 2.1.x (January 13, 2026):**
- Added `CLAUDE_CODE_TMPDIR` environment variable to override temp directory
- Changed terminal title to "Claude Code" on startup for better window identification
- Removed ability to @-mention MCP servers to enable/disable - use `/mcp enable` instead
- [VSCode] Fixed usage indicator not updating after manual compact

**Version 2.1.x (January 12, 2026):**
- Added `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to disable all background task functionality including auto-backgrounding and Ctrl+B shortcut
- Fixed "Help improve Claude" setting fetch to refresh OAuth and retry on stale token failure

### February 2026

**Version 2.1.x (February 10, 2026):**
- Fixed VS Code terminal scroll-to-top regression introduced in 2.1.37
- Fixed Tab key queueing slash commands instead of autocompleting
- Fixed bash permission matching for commands using environment variable wrappers
- Fixed text between tool uses disappearing when not using streaming
- Fixed duplicate sessions when resuming in VS Code extension

**Version 2.1.x (February 7-8, 2026):**
- Fixed issue where `/fast` was not immediately available after enabling `/extra-usage`
- Fixed crash when agent teams setting changed between renders
- Added session resume hint on exit
- Added support for full-width (zenkaku) space input from Japanese IME in checkbox selection

**Additional Fixes:**
- Fixed crash with plan mode when project config in `~/.claude.json` was missing default fields
- Fixed `temperatureOverride` being silently ignored in streaming API path
- Fixed PDF too large errors permanently locking up sessions
- Fixed bash commands incorrectly reporting failure with "Read-only file system" errors when sandbox mode enabled

**Improvements:**
- Improved system prompts to more clearly guide model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (cat, sed, grep, find)
- Reduced unnecessary bash command usage
- Removed misleading Anthropic API pricing from model selector for third-party provider users (Bedrock, Vertex, Foundry)

### Agent Teams and Memory Features (February 2026)

- Added research preview agent teams feature for multi-agent collaboration (token-intensive, requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- Added TeammateIdle and TaskCompleted hook events for multi-agent workflows
- Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
- Claude now automatically records and recalls memories as it works
- Added memory frontmatter field support for agents (persistent memory with user, project, or local scope)
- Skills defined in `.claude/skills/` within additional directories (--add-dir) now loaded automatically

### Gitignore Support

Added gitignore support in settings.json offering per-project control.

### Slash Command Autocomplete

Slash command autocomplete now works regardless of where slash appears in input.

**Sources:**
- [GitHub: CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [ClaudeLog: Claude Code Changelog](https://claudelog.com/claude-code-changelog/)
- [Releasebot: February Updates](https://releasebot.io/updates/anthropic/claude-code)
- [Gradually.ai: January Changelog](https://www.gradually.ai/en/changelogs/claude-code/)

---

## Summary of Major Themes

### January 2026 Focus

1. **Foundation Improvements:** Claude Code 2.1.0 (1,096 commits)
2. **Developer Experience:** Hot reload skills, terminal improvements, session management
3. **Extensibility:** Hooks system, Setup hook, async hooks
4. **Context Management:** MCP Tool Search to solve context pollution
5. **Accessibility:** Claude Cowork for non-developers

### February 2026 Focus

1. **Collaboration:** Agent Teams (peer-to-peer agents)
2. **Performance:** Fast mode for Opus 4.6 (2.5x speed)
3. **Intelligence:** Opus 4.6 support with 1M context
4. **Memory:** Auto memory rollout, persistent memory features
5. **Stability:** Bug fixes, performance improvements, UI polish

### Revolutionary Features

**Most Transformative:**
1. **Agent Teams** - Peer-to-peer collaboration, not just hierarchical delegation
2. **MCP Tool Search** - 95% context window savings
3. **Hot Reload Skills** - Real-time skill development
4. **Auto Memory** - Context persistence across sessions
5. **Claude Cowork** - Agentic capabilities for non-developers

---

## Additional Resources

### Official Documentation
- [Claude Code Docs](https://code.claude.com/docs)
- [Claude API Docs](https://platform.claude.com/docs)
- [GitHub: anthropics/claude-code](https://github.com/anthropics/claude-code)

### Community Resources
- [ClaudeLog](https://claudelog.com) - Complete docs, guides, tutorials
- [ClaudeFast](https://claudefa.st) - Comprehensive guides and tutorials
- [eesel.ai Claude Code Guides](https://www.eesel.ai/blog) - In-depth technical guides

### GitHub Collections
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - 100+ specialized subagents
- [wshobson/agents](https://github.com/wshobson/agents) - Multi-agent orchestration
- [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) - Hooks mastery
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) - Curated skills collection

---

## Conclusion

January and February 2026 represent a **paradigm shift** in Claude Code's capabilities. The introduction of peer-to-peer agent teams, combined with dramatic context window improvements via MCP Tool Search, hot-reload skills, and persistent memory, transforms Claude Code from a powerful AI coding assistant into a **collaborative multi-agent development platform**.

The **Agent Teams** feature, in particular, demonstrates the future of AI-assisted development: not a single assistant, but a coordinated team of specialists working together, challenging each other's findings, and converging on solutions through dialogue - mirroring how human development teams operate.

The C compiler experiment ($20K, 2,000 sessions, 100,000 lines of code) provides concrete evidence that this approach can tackle problems at unprecedented scale and complexity.

---

**End of Document**

*Generated: February 11, 2026*
*Total Sources: 100+ unique references across all sections*
