# Day 2 — Make It Useful

**Theme:** Tool Calling & Real-World Grounding

## Learning Objectives

By the end of Day 2, you will:

- Understand how LLM tool/function calling works
- Build custom tools that your agent can invoke
- Connect your agent to live data via Bing Grounding
- Build a Trip Planner agent that creates structured itineraries
- Handle tool errors gracefully and validate inputs

## Schedule

| Time | Lab | Description |
|------|-----|-------------|
| 9:00–9:15 | **Day 1 Recap** | Review, Q&A, showcase interesting prompts from Day 1 |
| 9:15–10:45 | **[Lab 1: Tool Calling](lab-1-tool-calling.md)** | Understand tool schemas, build your first tools, handle the tool-call loop |
| 10:45–11:00 | *Break* | |
| 11:00–12:00 | **[Lab 2: Bing Grounding](lab-2-bing-grounding.md)** | Connect your agent to live web data for real-time information |
| 12:00–1:00 | *Lunch* | |
| 1:00–2:45 | **[Lab 3: Trip Planner Agent](lab-3-trip-planner.md)** | Build the complete Trip Planner with multiple tools and structured output |
| 2:45–3:00 | *Break* | |
| 3:00–4:00 | **Lab 4: Custom Tool Challenge** | Add your own creative tool to the Trip Planner |

## Key Concepts Introduced

### Tool Calling (Function Calling)

LLMs can't browse the web, call APIs, or access databases on their own. **Tool calling** lets you give the LLM a menu of functions it can invoke. The flow:

```
User: "Find flights from NYC to Tokyo in March"
  │
  ▼
LLM sees available tools → decides to call search_flights(origin="NYC", dest="TYO", date="2026-03")
  │
  ▼
YOUR CODE executes the function → returns results
  │
  ▼
LLM receives results → generates a natural language response
```

The LLM **never executes code** — it only decides *which* tool to call and *what arguments* to pass. Your code handles execution.

### Tool Schema

Each tool is defined by a JSON schema that tells the LLM:
- **name:** What the tool is called
- **description:** What it does (critical for the LLM to choose correctly)
- **parameters:** What arguments it accepts, their types, and which are required

### Bing Grounding

A built-in Foundry capability that gives your agent access to live Bing search results. Instead of building a web scraper, you connect the agent to Bing and it can answer questions with current information.

## Starter Code

Your Day 2 starter code is in [`src/day-2/trip-planner/`](../../src/day-2/trip-planner/).

## What's Next?

In [Day 3](../day-3/README.md), you'll add **RAG** (Retrieval-Augmented Generation) and build a **multi-agent orchestrator** that routes to specialist agents.
