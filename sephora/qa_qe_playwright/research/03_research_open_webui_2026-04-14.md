# 03 - Research: Open WebUI

**Source:** Web research (openwebui.com, docs.openwebui.com, GitHub)
**Source Date:** 2026-04-14
**Document Set:** 03 (Working Discussion)
**Pass:** Background research on Open WebUI to understand Sephora's in-house portal reference

---

## What Open WebUI Is

Open WebUI is an open-source, self-hosted AI chat platform. It is essentially a ChatGPT alternative that organizations can deploy internally, giving their teams a familiar chat interface for interacting with LLMs without sending data to external providers.

It is MIT-licensed, has over 290 million downloads, and has been backed by A16z's Open Source AI Grant, Mozilla Builders 2024, and GitHub Accelerator 2024.

## Core Purpose

Open WebUI provides a web-based interface for organizational LLM access. Users interact with it the same way they would interact with ChatGPT: type a prompt, get a response, upload documents, have conversations. The key difference is that it runs on the organization's own infrastructure and connects to the organization's own models.

## Key Features

- **Model-agnostic.** Supports Ollama (for local models), OpenAI-compatible APIs, Anthropic, vLLM, and other providers. Organizations can connect any model backend.
- **RAG (Retrieval-Augmented Generation).** Built-in RAG with support for 9 vector databases and multiple content extraction engines. Users can upload documents and chat with them.
- **Agent and model builder.** Users can create custom characters, agents, and model configurations through the web interface.
- **Tool and function calling.** Supports tool use and function calling through pipelines.
- **Enterprise features.** Custom branding, SLA support, long-term support versions for organizational deployments.
- **Deployment options.** Docker, Python (pip/uv), Kubernetes, desktop app (experimental).
- **Offline-capable.** Designed to operate entirely offline when paired with local model hosting.

## What Open WebUI Is NOT

Open WebUI is not a QE testing tool, not an agentic automation platform, not a visual QA system, and not a workflow orchestrator. It is a chat interface for LLMs. It does not run Playwright tests, manage test playbooks, perform visual comparisons, or orchestrate CI/CD pipelines.

## Relevance to Sephora Engagement

Vaibhav mentioned in the April 9 meeting that Sephora is "building an in-house Open WebUI equivalent portal." This means Sephora is building their own organizational AI chat interface, similar to how many enterprises deploy internal ChatGPT alternatives for their workforce.

This is a completely separate initiative from the visual QA platform. The two serve different purposes:
- **Sephora's Open WebUI equivalent:** General-purpose AI chat for the organization
- **Visual QA platform (BayOne engagement):** Purpose-built agentic testing and validation system

The two could integrate with each other. For example, a user could query the chat interface for test results, or the chat platform could surface insights from the QA system. But they are fundamentally different products serving different needs.

## Implication for the Proposal

The visual QA platform BayOne is building is a long-term asset for Sephora. It is not an interim tool that gets replaced by their Open WebUI portal. If Sephora wants the two systems to talk to each other, BayOne can design the API layer with that integration in mind and work alongside Sephora's team to define compatibility specs. But the QA platform stands on its own.

---

Sources:
- [Open WebUI GitHub](https://github.com/open-webui/open-webui)
- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI Home](https://openwebui.com/)

---

*This is a blockchain-style document. It will not be edited after creation.*
