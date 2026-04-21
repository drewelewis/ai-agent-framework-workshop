# Day 1 — Hello, Agent

**Theme:** Foundations — from zero AI knowledge to a running agent

## Learning Objectives

By the end of Day 1, you will:

- Understand core AI/LLM concepts without needing a math background
- Have a fully configured development environment
- Build and run your first AI agent using the Microsoft Agent Framework
- Apply prompt engineering techniques to control agent behavior
- Understand the `.foundry/` workspace structure

## Schedule

| Time | Lab | Description |
|------|-----|-------------|
| 9:00–10:30 | **[Lab 1: Environment Setup](lab-1-environment-setup.md)** | Provision Azure resources, configure your dev environment, deploy your first model |
| 10:30–10:45 | *Break* | |
| 10:45–12:00 | **[Lab 2: Your First Agent](lab-2-first-agent.md)** | Scaffold and run a Destination Advisor agent using the Microsoft Agent Framework |
| 12:00–1:00 | *Lunch* | |
| 1:00–2:30 | **[Lab 3: Prompt Engineering](lab-3-prompt-engineering.md)** | Master system prompts, personas, guardrails, and output formatting |
| 2:30–2:45 | *Break* | |
| 2:45–4:00 | **Lab 4: Open Exploration** | Experiment with prompts, try edge cases, challenge your agent |

## Key Concepts Introduced

### What is an LLM?
A Large Language Model is a program trained on vast amounts of text that predicts "what comes next." Think of it as an extremely sophisticated autocomplete — but one that can reason, follow instructions, and generate structured responses.

### Tokens
LLMs don't read words — they read **tokens** (roughly ¾ of a word). Everything has a token cost: your instructions, the user's question, and the agent's response. Understanding tokens helps you design efficient agents.

### System Prompt
The **system prompt** is your primary control mechanism. It's a set of instructions sent to the LLM before every conversation that defines *who* the agent is, *what* it can do, and *how* it should behave. You'll spend significant time crafting these.

### Microsoft Agent Framework
An open-source Python/C# SDK for building AI agents. It provides:
- A `BaseAgent` class to define agent behavior
- Built-in support for tool calling, multi-turn conversations, and streaming
- A hosting adapter for deploying to Microsoft Foundry

### Microsoft Foundry
Azure's platform for hosting, managing, and monitoring AI agents in production. Think of it as "Azure App Service, but purpose-built for AI agents."

## Starter Code

Your Day 1 starter code is in [`src/day-1/destination-advisor/`](../../src/day-1/destination-advisor/).

> **First time with Python or cloud development?** Read the [Beginner Primer](../BEGINNER-PRIMER.md) before starting — it explains virtual environments, `.env` files, HTTP servers, and other concepts you’ll encounter today.

## What's Next?

In [Day 2](../day-2/README.md), you'll add **tool calling** to your agent — enabling it to search flights, check weather, and build real itineraries.
