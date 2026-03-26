# Claude Agent SDK Research Findings

**Research Date:** February 11, 2026
**Current Year:** 2026
**Researcher:** Claude Code (Sonnet 4.5)

---

## Executive Summary

The **Claude Agent SDK** (formerly Claude Code SDK) is Anthropic's official library for building autonomous AI agents in Python and TypeScript. Released in late 2025, it provides the same agent harness, tools, and context management that power Claude Code, now available for programmatic use in production applications, CI/CD pipelines, and custom automation systems.

Key developments from late 2025 through February 2026:
- **Name change** from "Claude Code SDK" to "Claude Agent SDK" to reflect broader applicability
- **Agent Teams** feature (experimental, shipped with Opus 4.6) enabling multi-agent coordination
- **Native MCP integration** with in-process server support
- **Production-grade features**: automatic context compaction, session management, hooks, and permissions
- **Active development** with TypeScript and Python SDKs maintained by Anthropic

---

## 1. What is the Claude Agent SDK?

### Core Definition

The Claude Agent SDK is a library that brings Claude's autonomous capabilities to Python and TypeScript applications. Unlike the Client SDK (which requires manual tool loop implementation), the Agent SDK handles tool execution automatically through Claude's built-in agent loop.

**Key distinction**: "The Agent SDK gives you Claude with built-in tool execution" rather than requiring developers to implement their own tool orchestration.

### Architecture

The SDK implements a four-stage agent feedback loop:

1. **Gather Context** — Search files, retrieve information, use subagents
2. **Take Action** — Execute via tools, bash scripts, or code generation
3. **Verify Work** — Apply rules, visual feedback, or LLM judgment
4. **Iterate** — Repeat until task completion

### Built-in Tools

The SDK provides immediate access to essential capabilities:

- **File operations**: Read, Write, Edit, and Glob (pattern-based file finding)
- **Command execution**: Bash for terminal commands and scripts
- **Code analysis**: Grep for regex-based content searching
- **Web capabilities**: WebSearch and WebFetch for current information
- **User interaction**: AskUserQuestion for clarifying queries with multiple-choice options

### Installation

**Python:**
```bash
pip install claude-agent-sdk
```
Requirements: Python 3.10+

**TypeScript:**
```bash
npm install @anthropic-ai/claude-agent-sdk
```
Requirements: Node.js 18+ or Bun

The Claude Code CLI comes bundled automatically with both SDKs, eliminating separate installation steps.

---

## 2. How the Agent SDK Relates to Claude Code

### Same Foundation, Different Interfaces

The Agent SDK is the **programmable version** of Claude Code's agent harness:

| Aspect | Claude Code (CLI) | Claude Agent SDK |
|--------|------------------|------------------|
| **Interface** | Interactive terminal | Programmatic API |
| **Use Case** | Development workflows | Production automation |
| **Tools** | Same built-in tools | Same built-in tools |
| **Context** | Manual management | Automatic compaction |
| **Configuration** | CLAUDE.md, skills | Same + Python/TS code |
| **Deployment** | Local developer machine | Servers, CI/CD, containers |

### Shared Configuration System

The SDK leverages Claude Code's filesystem-based configuration when `setting_sources=["project"]` is enabled:

- **Skills** — Reusable agent behaviors from `.claude/skills/`
- **Slash Commands** — Custom commands from `.claude/commands/`
- **Memory Files** — Persistent context from `.claude/memory/`
- **Plugins** — MCP servers and extensions
- **CLAUDE.md** — Project conventions and guidelines

### Agent Teams Integration

Both Claude Code and the Agent SDK support **Agent Teams** (experimental, shipped February 2026 with Opus 4.6), enabling multiple Claude instances to work in parallel with shared task lists and direct messaging.

---

## 3. New Features and Patterns (Late 2025 - February 2026)

### 3.1 Agent Teams (Experimental)

**Release:** February 2026 with Claude Opus 4.6
**Status:** Experimental, disabled by default
**Enable:** Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

#### What It Does

Agent Teams transform Claude Code from a single assistant into a multi-agent orchestration system:

- **Team Lead**: Primary session managing coordination and task assignment
- **Teammates**: Independent Claude Code instances with separate context windows
- **Shared Task List**: Distributed work items with dependency tracking
- **Direct Messaging**: Teammates communicate with each other, not just the lead

#### Key Differences from Subagents

| Feature | Subagents | Agent Teams |
|---------|-----------|-------------|
| **Context** | Shared with parent | Isolated per teammate |
| **Communication** | Report back to parent only | Direct peer-to-peer messaging |
| **Coordination** | Parent orchestrates | Self-coordinate via tasks |
| **Cost** | No documented multiplier | 7x in plan mode (official); implementation mode undocumented |
| **Use Case** | Sequential, dependent work | Parallel, independent work |

#### When to Use Agent Teams

**Best for:**
- Parallel research and review from multiple perspectives
- Independent feature development without file conflicts
- Competitive hypothesis testing for debugging scenarios
- Cross-layer changes requiring specialized ownership (frontend/backend/tests)

**Avoid for:**
- Sequential work
- Same-file editing
- Highly dependent tasks
- Budget-constrained projects (7x token cost in plan mode per official docs)

**Recommendation:** Limit to 3-4 teammates maximum for maintainability.

### 3.2 In-Process MCP Servers

**Feature:** Custom tools as Python/TypeScript functions
**Advantage:** No subprocess management overhead

The SDK supports in-process MCP servers over external subprocess servers:

- **Performance**: Direct function calls without inter-process communication
- **Simplicity**: No subprocess lifecycle management
- **Type Safety**: Native language integration
- **Debugging**: Standard debugging tools work

**Example Pattern:**
```python
@tool
def custom_search(query: str) -> str:
    """Search internal documentation"""
    # Implementation runs in-process
    return results
```

### 3.3 Hooks System

**Purpose:** Validation, logging, and behavior transformation

Callback functions at lifecycle points:
- **PreToolUse**: Block dangerous commands, validate parameters
- **PostToolUse**: Log execution, transform outputs
- **SessionStart**: Initialize resources
- **SessionEnd**: Cleanup and reporting

**Security Pattern:**
```python
def security_hook(tool_name, args):
    if tool_name == "Bash" and "rm -rf" in args:
        raise PermissionError("Dangerous command blocked")
```

### 3.4 Session Management

**Features:**
- Maintain context across exchanges
- Resume interrupted sessions
- Fork sessions for exploring alternative approaches
- Checkpoint and rewind capabilities (added late 2025)

**File Checkpointing:**
```python
# Enable checkpointing
client = ClaudeSDKClient(
    enable_file_checkpointing=True
)

# Revert changes to previous state
client.rewind_files(checkpoint_id)
```

### 3.5 Structured Outputs

**Feature:** Validated JSON matching schemas
**Use Case:** Extracting structured data from agent responses

Ensures agents return predictable, parseable data formats for downstream systems.

### 3.6 Extended Context Windows

**Beta Feature:** `context-1m-2025-08-07` for 1M token context on Sonnet 4/4.5

Enables processing entire large codebases or document collections in a single session.

### 3.7 MCP Tool Annotations

**Added:** Late 2025
**Purpose:** Metadata hints for tool behavior

Available annotations:
- `readOnlyHint`: Tool doesn't modify state
- `destructiveHint`: Tool makes irreversible changes
- `idempotentHint`: Multiple calls produce same result
- `openWorldHint`: Tool accesses external systems

**Example:**
```python
@tool(annotations={
    "destructiveHint": True,
    "idempotentHint": False
})
def delete_user(user_id: str):
    # Implementation
    pass
```

---

## 4. Code Examples and Patterns

### 4.1 Basic Query Pattern (Python)

**Use Case:** Simple one-off queries

```python
from claude_agent_sdk import query

async def main():
    async for message in query(
        prompt="What is 2 + 2?",
        allowed_tools=["Bash", "Read"]
    ):
        print(message)
```

### 4.2 Interactive Client Pattern

**Use Case:** Multi-turn conversations

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def main():
    client = ClaudeSDKClient(
        options=ClaudeAgentOptions(
            model="claude-sonnet-4-5-20250929",
            allowed_tools=["Read", "Write", "Bash"],
            max_turns=10
        )
    )

    # Initial message
    async for msg in client.send_message("Analyze this codebase"):
        print(msg)

    # Follow-up
    async for msg in client.send_message("Now fix the bug"):
        print(msg)
```

### 4.3 Custom Tool Pattern

**Use Case:** Domain-specific capabilities

```python
from claude_agent_sdk import ClaudeSDKClient, tool

@tool
def check_database_status() -> str:
    """Check if database is healthy"""
    # Implementation
    return "Database: Healthy"

async def main():
    client = ClaudeSDKClient(
        custom_tools=[check_database_status]
    )

    async for msg in client.send_message("Is the database healthy?"):
        print(msg)
```

### 4.4 Hooks Pattern for Security

**Use Case:** Prevent dangerous operations

```python
from claude_agent_sdk import ClaudeSDKClient, Hook

def security_hook(context) -> None:
    if context.tool_name == "Bash":
        dangerous_patterns = ["rm -rf", "sudo", "dd if=/dev/zero"]
        if any(p in context.args.get("command", "") for p in dangerous_patterns):
            raise PermissionError(f"Blocked dangerous command")

client = ClaudeSDKClient(
    hooks=[
        Hook(
            type="pre_tool_use",
            callback=security_hook,
            matcher={"tool": "Bash"}
        )
    ]
)
```

### 4.5 Subagent Pattern

**Use Case:** Specialized, isolated tasks

```python
from claude_agent_sdk import ClaudeSDKClient

async def main():
    client = ClaudeSDKClient()

    # Spawn subagent for research
    research_result = await client.spawn_subagent(
        prompt="Research best practices for database indexing",
        allowed_tools=["WebSearch", "WebFetch"]
    )

    # Use results in main agent
    async for msg in client.send_message(
        f"Apply these practices: {research_result}"
    ):
        print(msg)
```

### 4.6 Multi-Agent Research Pattern

**Source:** [claude-agent-sdk-demos/research-agent](https://github.com/anthropics/claude-agent-sdk-demos)

**Architecture:**
1. Main agent decomposes complex request into subtasks
2. Spawns multiple researcher subagents concurrently
3. Each subagent investigates specialized aspect
4. Main agent aggregates findings into synthesized report

**Use Case:** Comprehensive analysis requiring multiple perspectives

### 4.7 Email Agent Pattern

**Source:** [claude-agent-sdk-demos/email-agent](https://github.com/anthropics/claude-agent-sdk-demos)

**Features:**
- IMAP integration for incoming email monitoring
- Agentic search through email history
- Autonomous triage, response, and action execution

**Deployment:** Long-running session with proactive monitoring

### 4.8 Session Forking Pattern

**Use Case:** Explore alternative approaches

```python
# Main session
main_client = ClaudeSDKClient()

# Fork for experimentation
alt_client = main_client.fork_session()

# Try different approach without affecting main session
async for msg in alt_client.send_message("Try approach B"):
    print(msg)

# If successful, merge or switch
```

---

## 5. Best Practices (2026)

### 5.1 Architecture Patterns

#### Orchestrator + Specialists

**Rule:** Give each subagent one job; let an orchestrator coordinate.

**Pattern:**
```
Orchestrator (planning, delegation, state)
├── Specialist A (research)
├── Specialist B (implementation)
└── Specialist C (testing)
```

**Limits:** 3-4 subagents maximum for maintainability

#### Permission Management

**Principle:** Treat tool access like production IAM

- Start from deny-all; allowlist only necessary tools
- Require explicit confirmations for sensitive actions (git push, infrastructure changes)
- Block dangerous commands (rm -rf, sudo)

**Example:**
```python
ClaudeAgentOptions(
    allowed_tools=["Read", "Grep"],  # Read-only
    require_confirmation=["Bash", "Write"],
    blocked_patterns=["rm -rf", "sudo"]
)
```

#### Context Management

**Strategies:**
1. **Isolate per-subagent context** — Don't share everything
2. **Orchestrator maintains compact state** — Global plan, not every detail
3. **Use CLAUDE.md** — Encode project conventions, standards
4. **Periodic pruning** — Reset or summarize during long sessions
5. **Retrieval over dumping** — Pull relevant context, don't load everything

**Built-in:** The SDK's `compact` feature automatically summarizes when approaching context limits

### 5.2 Tool Design

**Principle:** Tools are the primary building blocks of execution

- Tools are prominent in Claude's context window
- Design for discoverability and clarity
- Use clear names and descriptions
- Optimize for context efficiency

**Good:**
```python
@tool
def search_customer_by_email(email: str) -> dict:
    """Find customer record by email address"""
```

**Avoid:**
```python
@tool
def find_stuff(query: str, type: str, filters: dict) -> list:
    """Search for things"""  # Too vague
```

### 5.3 Verification Strategies

**Three approaches:**

1. **Rules-Based Feedback**
   - Linting, validation constraints
   - Fast, deterministic
   - Example: Run pytest after code changes

2. **Visual Feedback**
   - Screenshots, renders for UI tasks
   - Human-in-the-loop validation
   - Example: Capture browser screenshot after UI change

3. **LLM-as-Judge**
   - Secondary model evaluation
   - Nuanced quality assessment
   - Example: Check if documentation is clear and accurate

### 5.4 Production Deployment

#### Hosting Patterns

**Ephemeral Sessions:**
- Create container per task, destroy afterward
- Best for: Bug investigation, invoice processing
- Cost: ~$0.05/hour running

**Long-Running Sessions:**
- Persistent instances, always available
- Best for: Email triage, high-frequency chatbots
- Consideration: Resource management, cost

**Hybrid Sessions:**
- Ephemeral containers hydrated with history/state
- Best for: Intermittent user interactions needing context
- Balance: Cost efficiency + context preservation

#### System Requirements

- Python 3.10+ or Node.js 18+
- **Recommended allocation:** 1 GiB RAM, 5 GiB disk, 1 CPU
- Outbound HTTPS access to `api.anthropic.com`

#### Sandbox Providers

**Options:**
- Modal Sandbox
- Cloudflare Workers
- E2B (code execution sandboxes)
- Fly Machines
- Vercel Sandbox
- Self-hosted: Docker, Firecracker

#### Security & Isolation

**Critical:** Run inside sandboxed container environment

**Provides:**
- Process isolation
- Resource limits
- Network control
- Ephemeral filesystems

### 5.5 Configuration Management

#### CLAUDE.md as Constitution

**The single most important file** for Claude Code/Agent SDK effectiveness

**Should contain:**
- Project conventions and coding standards
- Test commands and procedures
- Directory layout and architecture
- Common pitfalls and solutions
- Build and deployment instructions

**Effect:** Agents converge on shared standards, reducing drift

#### Settings Sources

```python
ClaudeAgentOptions(
    setting_sources=["project"]  # Load .claude/ config
)
```

Inherits:
- Skills (`.claude/skills/`)
- Commands (`.claude/commands/`)
- Memory (`.claude/memory/`)
- MCP servers

### 5.6 Error Handling

**SDK-Specific Exceptions:**
- `CLINotFoundError`: Claude CLI not found
- `ProcessError`: Command execution failed
- `CLIJSONDecodeError`: Invalid JSON from CLI
- `ClaudeSDKClient`: Base error

**Pattern:**
```python
try:
    async for msg in client.send_message(prompt):
        print(msg)
except ProcessError as e:
    # Handle execution failure
    logger.error(f"Process failed: {e}")
except CLIJSONDecodeError as e:
    # Handle communication issue
    logger.error(f"Invalid response: {e}")
```

### 5.7 Cost Management

**Token Multipliers:**
- Single agent: 1x baseline
- Subagent: No documented multiplier
- Agent Team: 7x in plan mode (official); implementation mode undocumented

**Optimization Strategies:**
1. Use subagents for focused tasks, not general assistance
2. Limit agent teams to truly parallel work
3. Set `max_turns` to prevent infinite loops
4. Use compact/summarization aggressively
5. Prefer retrieval over loading full context

### 5.8 Testing & Improvement

**Key Questions:**
1. Does misunderstanding indicate missing contextual information?
2. Can repeated failures be addressed through formal verification rules?
3. Are available tools sufficient, or should alternatives be added?
4. Does performance vary with new features? (Build representative test sets)

**Approach:**
- Experiment aggressively in safe environments
- Deploy conservatively in production
- Build representative test sets
- Iterate based on failure patterns

---

## 6. Subagents vs Agent Teams: Detailed Comparison

### Communication Architecture

**Subagents:**
- Run within single session
- Report back to parent only
- No peer-to-peer communication
- Synchronous: parent waits for subagent completion

**Agent Teams:**
- Separate Claude Code sessions
- Direct messaging between teammates
- Shared task list for coordination
- Asynchronous: teammates work in parallel

### Context Management

**Subagents:**
- Share parent's context window
- Inherit conversation history
- Compact, efficient memory usage

**Agent Teams:**
- Isolated context per teammate
- Load same project config (CLAUDE.md, MCPs)
- No shared conversation history
- Communication via task files and messages only

### Use Case Decision Matrix

| Scenario | Use Subagents | Use Agent Teams |
|----------|---------------|-----------------|
| Sequential tasks | ✓ | |
| Same-file editing | ✓ | |
| Highly dependent work | ✓ | |
| Quick, focused reports | ✓ | |
| Parallel research | | ✓ |
| Independent features | | ✓ |
| Competing hypotheses | | ✓ |
| Cross-layer changes | | ✓ |
| Budget-constrained | ✓ | |

### Customization

**Subagents (via `.claude/agents/` files):**
- Tool restrictions
- Permission modes
- Scoped hooks
- Persistent memory
- Preloaded skills
- Custom models

**Agent Teams:**
- Currently inherit all from project config
- Cannot customize per-teammate (as of Feb 2026)
- **Gap identified:** No way to create specialized teammates with different tool access

### Current Limitations (Agent Teams)

**As of February 2026:**
1. No session resumption with in-process teammates
2. Potential task status lag
3. Slow shutdown procedures
4. Single-team-per-session restriction
5. Teammates cannot spawn additional teams or subagents
6. No per-teammate customization (all inherit same config)

### Practical Recommendations

**From community feedback (Shipyard, Eesel, others):**

1. **Start with subagents** for most work
2. **Reserve agent teams** for:
   - Large, genuinely parallel tasks
   - Multiple independent perspectives needed
   - Budget allows higher token cost (7x in plan mode per official docs)
3. **Make agents critical and honest**:
   - Override agreeable default behavior
   - Tell agents "be realistic" and "be critical"
4. **Limit scope**: 3-4 agents maximum
5. **Monitor costs**: Track token usage per teammate

---

## 7. Third-Party Tools and Frameworks

### 7.1 Claude-Flow

**URL:** [https://github.com/ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)
**Description:** The leading agent orchestration platform for Claude

**Features:**
- Intelligent multi-agent swarms
- Coordinate autonomous workflows
- Conversational AI systems
- Enterprise-grade architecture
- Distributed swarm intelligence
- RAG integration
- Native Claude Code support via MCP protocol
- Ranked #1 in agent-based frameworks

### 7.2 Gas Town

**Creator:** Steve Yegge
**Description:** Agentic IDE likened to "Kubernetes for AI agents"

**Architecture:**
- **Mayor agent**: Breaks down tasks, spawns designated agents
- **Polecats**: Execute tasks in parallel
- **Witness**: Monitors overall progress

**Philosophy:** Structured, opinionated multi-agent management

### 7.3 Multiclaude

**Creator:** Dan Lorenc
**Description:** Multi-agent orchestrator with "Brownian ratchet" philosophy

**Approach:** Always pushing forward — as long as CI tests pass, every PR gets merged

### 7.4 Microsoft Agent Framework Integration

**Integration:** Claude Agent SDK + Semantic Kernel

**Features:**
- Built-in tools
- Function tools
- Streaming
- Multi-turn conversations
- Permission modes
- MCP servers in Python

**Use Case:** Enterprise .NET + Python hybrid agent systems

### 7.5 Shipyard

**URL:** [https://shipyard.build](https://shipyard.build)
**Focus:** Multi-agent orchestration for Claude Code in 2026

**Insights:** Documented patterns for improving subagent effectiveness, critical evaluation strategies

---

## 8. Hidden Features and Experimental Capabilities

### 8.1 TeammateTool Discovery

**Source:** Binary analysis by community (Dec 2025)
**Status:** Fully implemented, feature-flagged off

**Discovery:** Researchers ran `strings` on Claude Code binary and found:
- **TeammateTool**: Multi-agent orchestration system
- **13 operations** for agent management
- Directory structures for team coordination
- Environment variables for configuration

**Patterns Found:**
- Leader: Orchestrates overall work
- Swarm: Parallel execution
- Pipeline: Sequential handoffs
- Watchdog: Monitors and intervenes

**Similarity:** Nearly identical architecture to Gas Town (Mayor/Polecats/Witness)

**Impact:** Community discovered official multi-agent capability months before announcement, indicating Anthropic's long-term investment in this architecture

### 8.2 Context Window Experiments

**Beta Features:**
- `context-1m-2025-08-07`: 1M token context window
- Enables processing entire large codebases
- Not yet generally available (as of Feb 2026)

### 8.3 Agent Teams Display Modes

**Two modes:**

1. **In-process**: All teammates in main terminal, navigate with Shift+Up/Down
2. **Split panes**: Individual terminal panes per teammate
   - Requires: tmux or iTerm2 with Python API enabled
   - Better visibility but more complex setup

---

## 9. Timeline of Major Releases

| Date | Event | Significance |
|------|-------|--------------|
| **Late 2025** | Claude Code SDK released | Initial programmatic agent capabilities |
| **Dec 2025** | TeammateTool discovered | Community finds hidden multi-agent system |
| **Late 2025** | File checkpointing added | Rewind capabilities for safer experimentation |
| **Late 2025** | MCP tool annotations | Metadata hints for tool behavior |
| **Jan 2026** | Renamed to Agent SDK | Reflects broader vision beyond code |
| **Feb 2026** | Agent Teams shipped | Official multi-agent coordination (Opus 4.6) |
| **Feb 2026** | TypeScript SDK updated | Latest commits to both SDKs |

---

## 10. Community Resources and Learning

### Official Documentation

- [Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Quickstart Guide](https://platform.claude.com/docs/en/agent-sdk/quickstart)
- [Python SDK Reference](https://platform.claude.com/docs/en/agent-sdk/python)
- [Hosting Guide](https://platform.claude.com/docs/en/agent-sdk/hosting)
- [Agent Teams Docs](https://code.claude.com/docs/en/agent-teams)

### GitHub Repositories

- [Python SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [TypeScript SDK](https://github.com/anthropics/claude-agent-sdk-typescript)
- [Demo Repository](https://github.com/anthropics/claude-agent-sdk-demos)

### Community Guides

- [The Complete Guide to Building Agents with Claude Agent SDK](https://nader.substack.com/p/the-complete-guide-to-building-agents) (Nader Dabit)
- [Claude Agent SDK Best Practices for AI Agent Development](https://skywork.ai/blog/claude-agent-sdk-best-practices-ai-agents-2025/) (Skywork AI)
- [Claude Code Multiple Agent Systems: Complete 2026 Guide](https://www.eesel.ai/blog/claude-code-multiple-agent-systems-complete-2026-guide) (Eesel AI)
- [Agent Teams vs Sub-Agents: Key Differences](https://www.geeky-gadgets.com/agent-teams-token-usage/) (Geeky Gadgets)
- [From Tasks to Swarms: Agent Teams in Claude Code](https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/) (alexop.dev)
- [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) (Shrivu Shankar)

### Integration Examples

- [DataCamp Tutorial: Create Agents Using Claude Sonnet 4.5](https://www.datacamp.com/tutorial/how-to-use-claude-agent-sdk)
- [Promptfoo: Claude Agent SDK Testing](https://www.promptfoo.dev/docs/providers/claude-agent-sdk/)
- [KDnuggets: Getting Started Guide](https://www.kdnuggets.com/getting-started-with-the-claude-agent-sdk)

---

## 11. Key Takeaways for Implementation

### When to Use Claude Agent SDK

**Ideal Scenarios:**
1. **Production automation** requiring autonomous file/command operations
2. **CI/CD pipelines** with code analysis, test generation, or fix suggestions
3. **Custom applications** needing conversational AI with tool execution
4. **Email/ticket triage** with proactive monitoring and responses
5. **Research workflows** requiring web search and synthesis
6. **Code generation** with verification and testing

**Not Ideal For:**
1. Simple Q&A without tool needs (use Client SDK)
2. Highly interactive UIs (use Client SDK with custom tool loop)
3. Budget-constrained projects (Agent Teams use 7x tokens in plan mode per official docs)

### Subagents vs Agent Teams Decision

**Use Subagents When:**
- Tasks are sequential or dependent
- Working on same files
- Need compact context
- Budget-sensitive
- Quick focused work

**Use Agent Teams When:**
- Genuinely parallel work
- Multiple perspectives needed
- Independent file/module ownership
- Budget allows higher cost (7x in plan mode per official docs)
- Long-running research or analysis

**Default:** Start with single agent or subagents; graduate to teams only when clearly beneficial

### Production Checklist

- [ ] Sandbox environment configured (Docker, E2B, etc.)
- [ ] Security hooks for dangerous commands
- [ ] Permission allowlist defined
- [ ] Error handling implemented
- [ ] Logging and monitoring in place
- [ ] Cost tracking enabled
- [ ] Max turns limit set
- [ ] Context compaction strategy defined
- [ ] CLAUDE.md created with project conventions
- [ ] Representative test sets built
- [ ] Deployment pattern selected (ephemeral/long-running/hybrid)

### Anti-Patterns to Avoid

1. **Permission sprawl**: Don't grant all tools by default
2. **Unbound loops**: Always set `max_turns`
3. **Ignoring CLAUDE.md**: This is your agent's constitution
4. **Over-teaming**: More than 4 agents creates coordination overhead
5. **Shared context abuse**: Don't dump everything into agent context
6. **No verification**: Always validate agent outputs (rules/visual/LLM)
7. **Production experiments**: Test in sandboxes first

---

## 12. Future Directions and Open Questions

### Identified Gaps (as of Feb 2026)

1. **Per-teammate customization in Agent Teams**
   - Currently all teammates inherit same config
   - Cannot restrict tools or permissions per teammate
   - Community request: [GitHub Issue #24316](https://github.com/anthropics/claude-code/issues/24316)

2. **Session resumption for Agent Teams**
   - In-process teammates can't resume after interruption
   - Long-running teams difficult to maintain

3. **Nested teams**
   - Teammates cannot spawn their own teams or subagents
   - Limits hierarchical orchestration patterns

4. **Cost transparency**
   - No built-in token tracking per agent/teammate
   - Difficult to optimize without visibility

### Emerging Patterns

**Multi-agent architectures are evolving toward:**
- **Specialized experts** with restricted tool access
- **Orchestrator + workers** as standard pattern
- **Verification agents** that validate other agents' work
- **Competitive evaluation** (multiple agents, best result wins)

### Anthropic's Direction

**Evidence of long-term commitment:**
- TeammateTool implementation discovered months before announcement
- Consistent SDK updates (active development Feb 2026)
- Integration with MCP ecosystem
- Production-grade features (context compaction, permissions, hooks)
- Documentation and demo repositories

**Likely roadmap (speculation based on gaps):**
- Per-agent configuration in teams
- Better cost tracking and optimization tools
- Hierarchical multi-agent patterns
- More sandbox provider integrations
- Enhanced debugging and observability

---

## 13. Recommendations for Cisco CI/CD Project

### Relevance Assessment

The Claude Agent SDK has **high relevance** for Cisco's NX-OS CI/CD pipeline improvements:

#### Applicable Use Cases

1. **PR Analysis Agent**
   - Autonomous review of pull requests
   - Pattern: Single agent with Read, Grep, Bash tools
   - Deployment: Ephemeral session per PR

2. **Failure Attribution with Agent Teams**
   - Research agent coordinating multiple specialists
   - Pattern: Orchestrator + (log analyzer + test analyzer + code analyzer)
   - Each teammate investigates different failure dimension
   - Synthesis produces comprehensive diagnosis

3. **Self-Healing Automation**
   - Long-running agent monitoring pipeline
   - Pattern: Watchdog + specialist fixers
   - Hooks for safety (no auto-merge without approval)

4. **Developer Box AI Assistant**
   - Interactive debugging help
   - Pattern: Single agent with custom tools for NX-OS specifics
   - CLAUDE.md with Cisco coding standards

#### Implementation Strategy

**Phase 1: Single Agent Exploration**
- Start with simple PR analysis agent
- Build representative test set from real NX-OS PRs
- Establish safety patterns (hooks, permissions)
- Measure token costs and effectiveness

**Phase 2: Subagent Patterns**
- Add specialized subagents (log analysis, test diagnosis)
- Maintain orchestrator pattern (3-4 max)
- Iterate on CLAUDE.md with NX-OS conventions

**Phase 3: Agent Teams (if justified)**
- Only if failure attribution genuinely benefits from parallel perspectives
- Budget assessment (7x token cost in plan mode per official docs)
- Monitor for coordination overhead

#### Technical Considerations

**Infrastructure:**
- Sandbox: Self-hosted Docker (compliance requirements)
- Hosting: Hybrid sessions (on-demand with state)
- Authentication: Anthropic API key via Azure Key Vault

**Cost Control:**
- Set `max_turns` based on task type
- Use compact/summarization aggressively
- Track per-agent token usage
- Start with small test set, expand gradually

**Security:**
- Hooks to block dangerous bash commands
- Permission allowlists per agent role
- Audit logging for all tool executions
- No auto-merge without human approval

#### Skills/Reference Docs Integration

The Agent SDK's `setting_sources=["project"]` feature means:
- Existing `.claude/skills/` can be loaded by agents
- `django-forge` patterns could be adapted for NX-OS
- Research agent pattern similar to needed failure analysis

**Adaptation Strategy:**
- Study `django-forge` multi-agent coordination
- Extract general patterns (orchestrator, specialists, synthesis)
- Create NX-OS-specific skills (test parser, log analyzer)
- Build `CLAUDE.md` with Cisco conventions

---

## Sources

### Official Anthropic Resources
- [Agent SDK Overview](https://platform.claude.com/docs/en/agent-sdk/overview)
- [Agent SDK Quickstart](https://platform.claude.com/docs/en/agent-sdk/quickstart)
- [Agent SDK Python Reference](https://platform.claude.com/docs/en/agent-sdk/python)
- [Agent SDK Hosting Guide](https://platform.claude.com/docs/en/agent-sdk/hosting)
- [Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)
- [Building Agents with Claude Agent SDK (Blog)](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)
- [GitHub: claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- [GitHub: claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript)
- [GitHub: claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos)

### Community Resources
- [The Complete Guide to Building Agents with Claude Agent SDK](https://nader.substack.com/p/the-complete-guide-to-building-agents)
- [Claude Agent SDK Best Practices (Skywork AI)](https://skywork.ai/blog/claude-agent-sdk-best-practices-ai-agents-2025/)
- [Claude Code Multiple Agent Systems Guide (Eesel AI)](https://www.eesel.ai/blog/claude-code-multiple-agent-systems-complete-2026-guide)
- [Agent Teams vs Sub-Agents (Geeky Gadgets)](https://www.geeky-gadgets.com/agent-teams-token-usage/)
- [From Tasks to Swarms (alexop.dev)](https://alexop.dev/posts/from-tasks-to-swarms-agent-teams-in-claude-code/)
- [How I Use Every Claude Code Feature (Shrivu Shankar)](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)
- [Claude Code Swarms (Addy Osmani)](https://addyosmani.com/blog/claude-code-agent-teams/)
- [Shipyard: Multi-agent Orchestration](https://shipyard.build/blog/claude-code-multi-agent/)
- [Claude Code's Hidden Multi-Agent System (Paddo.dev)](https://paddo.dev/blog/claude-code-hidden-swarm/)

### Third-Party Frameworks
- [GitHub: claude-flow](https://github.com/ruvnet/claude-flow)
- [GitHub: agents (wshobson)](https://github.com/wshobson/agents)
- [Claude Agent SDK + Microsoft Agent Framework](https://devblogs.microsoft.com/semantic-kernel/build-ai-agents-with-claude-agent-sdk-and-microsoft-agent-framework/)

### Tutorials and Guides
- [DataCamp: Claude Agent SDK Tutorial](https://www.datacamp.com/tutorial/how-to-use-claude-agent-sdk)
- [Promptfoo: Claude Agent SDK Provider](https://www.promptfoo.dev/docs/providers/claude-agent-sdk/)
- [KDnuggets: Getting Started](https://www.kdnuggets.com/getting-started-with-the-claude-agent-sdk)
- [Helply: Step by Step Guide](https://helply.com/blog/create-ai-agent-using-claude-agent-sdk)

### Community Discussions
- [Claude Code Swarm Orchestration Skill (GitHub Gist)](https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea)
- [Claude Code Multi-Agent Orchestration System (GitHub Gist)](https://gist.github.com/kieranklaassen/d2b35569be2c7f1412c64861a219d51f)
- [Complete Guide to Building Agents (GitHub Gist)](https://gist.github.com/dabit3/93a5afe8171753d0dbfd41c80033171d)
- [Feature Request: Custom Agent Definitions (GitHub Issue)](https://github.com/anthropics/claude-code/issues/24316)

---

**Document Version:** 1.0
**Last Updated:** February 11, 2026
**Next Review:** As new SDK versions released
