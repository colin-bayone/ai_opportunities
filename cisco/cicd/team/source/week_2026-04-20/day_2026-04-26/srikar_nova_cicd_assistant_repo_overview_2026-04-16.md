# Nova CI/CD AI Assistant — Repository Overview

## What Is This?

A **conversational AI assistant** for Cisco CI/CD operations that lets engineers query infrastructure, manage bugs, and send notifications via natural language.

**Core intent:** Eliminate manual navigation across multiple systems (Nexus-T, CDETs, Webex) by providing a unified chat interface powered by LLM reasoning and tools.

---

## Core Problem & Scope

### The Problem
Engineers waste time manually:
- Logging into Nexus-T to check job/test status
- Searching CDETs for related bugs
- Copy-pasting results into Webex notifications
- Maintaining context across multiple systems

### The Solution
A **ReAct agent** that:
1. **Understands natural language** — "Show me failed tests for N9K jobs from yesterday"
2. **Routes to the right API** — LLM + RAG prompts + JSON API docs pick correct endpoints
3. **Combines results** — Fetch from Nexus-T, enhance with CDETs data, send to Webex
4. **Maintains context** — Remembers prior queries via Redis session storage

### Scope
- **Users:** Cisco internal engineers / CI/CD teams
- **Primary data source:** Nexus-T (internal test automation) + CDETs (bug tracking) + Webex (communication)
- **Deployment:** Container-based (Podman/Docker compose)
- **Coverage:** ~80% test/job queries, ~10% bug lookups, ~10% notifications

---

## Architecture Overview

### Request Flow
```
Dash UI (port 8501)
    ↓ JWT validation
Gateway (port 8080) — Rate limiting + routing
    ↓
Agent Server (port 8090)
    ↓ ReAct reasoning loop
MCP Server (port 3003) — Thin tool proxy (no secrets)
    ↓
Backend API (port 8082) — Business logic + external integrations
    ↓
External APIs: Nexus-T, CDETs, Webex, Redis
```

### 6-Service Deployment
1. **Redis** (port 6379) — Session & task storage
2. **Backend API** (port 8082) — Business logic, secrets, external calls
3. **MCP Server** (port 3003) — Tool proxy (no business logic)
4. **Agent Server** (port 8090) — ReAct + AI SDK proxy
5. **Gateway** (port 8080) — JWT validation, rate limiting
6. **Frontend** (port 8501) — Dash UI

---

## LLM Agent Setup

### The Agent
- **Type:** `ReActAgent` (1 main agent)
- **Reasoning:** XML-based ReAct loop (thought → action → observation → final_answer)
- **State:** Custom implementation (NOT LangGraph)
- **State management:** Manual conversation history capped at 10 messages, max 10 reasoning iterations

### Primary LLM
- **Model:** Cisco Circuit / Azure OpenAI (`gpt-4o-mini`)
- **Endpoint:** `https://chat-ai.cisco.com`
- **Auth:** Cisco OAuth (client credentials)
- **Token refresh:** Auto-refresh if > 50 minutes old

### Optional LLM Backends
- **GitHub Copilot** — Via AI SDK (chat-only, no tools)
- **OpenAI Codex** — Via AI SDK (code completion)

---

## Tools Connected to the Agent

The ReAct agent has access to **10 tool categories** (15 individual tools):

### Infrastructure (Nexus-T)
- `endpoint_context` — Universal query resolver; uses LLM to pick right API endpoint

### Bug Management (CDETs)
- `find_bug` — Lookup bug by CSC ID
- `create_bug` — File new bugs with structured data

### Webex Communication
- `send_webex_notification_direct` — DM individuals
- `send_webex_notification_room` — Broadcast to team spaces
- `create_webex_team` / `add_webex_team_member` / `create_webex_room`
- `process_webex_query_and_respond` — Query Nexus-T + post to Webex

### Task Management
- `get_all_todos` — List tasks

---

## Job IDs & Data Fetching

### Job IDs ≠ Bug IDs
- **Job IDs** (e.g., 12345) → Nexus-T test automation platform (nxtaas.cisco.com)
- **Bug IDs** (e.g., CSCab12345) → CDETs internal bug tracking

### Where Job Details Come From
| Source | Purpose |
|--------|---------|
| `/api/jobs/` | Current/active jobs (status, submitter, ASIC) |
| `/api/job-history/` | Completed jobs with historical data, timing, success rates |
| `/api/testcase-report?jobid=X` | Individual test case results |
| `/api/nxos-sanity-logs/` | Execution logs & debug traces |

**All internal Cisco infrastructure APIs—NOT GitHub.**

---

## Prompts & System Instructions

### Location: `config/prompts.py`

| Prompt | Purpose | Used By |
|--------|---------|---------|
| **COPILOT_SYSTEM_PROMPT** | Chat-only, no tools | Copilot model |
| **REACT_SYSTEM_PROMPT** | ReAct reasoning with XML tags & tool definitions | ReActAgent |

### Service Prompts: `services/nova.py`

| Prompt | Purpose |
|--------|---------|
| **API_PROMPT** | Route queries to relevant API documentation |
| **RAG_PROMPT** | Generate API endpoints from natural language |
| **HISTORY_PROMPT** | Context-aware endpoint generation using chat history |

---

## LLM Response Format

- **Not JSON directly** — LLM returns **text with XML tags**
- **Streaming as JSON events** — Each reasoning step yielded as `{"type": "thought"/"action"/"observation"/"final_answer", "content": "..."}`
- **Chat history saved** — Via Redis (last 3 interactions for context)

---

## State Management

- **NO LangGraph** — LangGraph is in requirements but unused
- **Custom ReAct loop** — Manual conversation list management
- **Fresh agent per session** — But pulls prior history from Redis for context
- **New chat at each request** — Resets iteration counter, loads prior interactions

---

## Observability & Monitoring

### Built-in Tracking: `TelemetryTracker`
```python
class TelemetryTracker:
    - total_queries (count)
    - total_tokens (usage)
    - total_cost (calculated)
```

### Logging
- Standard Python `logging` module
- Logs to stdout/files
- Tracks: token usage, session events, errors, warnings

### Limitations
- NO external monitoring (Sentry, Datadog, Prometheus)
- NO real-time dashboards
- NO alerting system
- NO distributed tracing

---

## Vector DB & Caching

- **NO vector databases** — No ChromaDB, Pinecone, FAISS
- **NO embeddings** — Not used anywhere
- **Redis simple cache** — Exact query hash matching (SHA256)
- **Commented-out similarity search** — Vector-based search code was disabled

---

## CI/CD Pipeline

### Pre-Merge (Dev)
- Jenkins job: `dev-pre-merge.jenkinsfile`
- Builds PyInstaller binaries
- Smoke tests in temporary container
- Does NOT push to registry

### Post-Merge (Prod)
- Jenkins job: `prod-post-merge.jenkinsfile`
- Builds binaries, archives to NFS
- Deploys into container as image
- Pushes to production registry with date tag

---

## Key Files

| Path | Purpose |
|------|---------|
| `backend/agent.py` | ReActAgent class, reasoning loop |
| `backend/circuit.py` | LLMClient, Cisco Circuit integration |
| `backend/nova_mcp_server.py` | MCP tool wrappers |
| `backend/backend_api.py` | Business logic, external API calls |
| `backend/gateway.py` | JWT validation, rate limiting, routing |
| `config/prompts.py` | System prompts for agents |
| `services/nova.py` | Nexus-T API routing & endpoint generation |
| `config/chat_history.py` | Redis session storage |
| `frontend/telemetry_tracker.py` | Simple usage telemetry |
| `docker/docker-compose.yml` | 6-service architecture |

---

## Dependencies

**Key packages:**
- `fastapi` — API framework
- `langchain` — LLM orchestration
- `langchain_openai` — Azure OpenAI integration
- `fastmcp` — MCP protocol server
- `dash` — Frontend UI
- `redis` — Session storage
- `requests` — HTTP calls

---

## Summary

| Aspect | Details |
|--------|---------|
| **Agents** | 1 (ReActAgent) |
| **Models** | 3 (Cisco Circuit primary; Copilot/Codex optional) |
| **Prompts** | 5 (2 system + 3 service-level) |
| **Tools** | 15 (Nexus-T, CDETs, Webex, Tasks) |
| **Reasoning** | ReAct with XML tags, custom state management |
| **State** | Redis + in-memory conversation history |
| **Observability** | Python logging + custom TelemetryTracker |
| **External Tools** | None (no Sentry, Datadog, etc.) |
| **Vector DB** | None (simple hash-based caching) |

---

## Getting Started

1. **Setup:**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure:**
   - Copy `.env.example` → `.env`
   - Fill in Cisco OAuth credentials, Nexus-T credentials, Webex token

3. **Run (Docker):**
   ```bash
   bash scripts/run.sh  # Single container
   docker-compose up -d  # 6-service deployment
   ```

4. **Access:**
   - Dash UI: `http://localhost:8501`
   - Gateway: `http://localhost:8080`
   - MCP Server: `http://localhost:3003`

---

## Quick Reference

**User asks:** "What's the status of job 12345?"

**Flow:**
1. Frontend sends to Gateway (with JWT)
2. Gateway validates token, routes to Agent Server
3. Agent Server initializes ReActAgent
4. ReActAgent thinks → calls `endpoint_context` tool
5. MCP Server proxies to Backend API
6. Backend API authenticates with Nexus-T, fetches job data
7. Agent formats response in Markdown + tables
8. Response streamed back as SSE events
9. Dash UI renders final answer

**Result:** Real-time job status with test breakdown, Jenkins link, NxTaaS URL—all in chat.
