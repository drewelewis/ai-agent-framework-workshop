# Day 3 — Make It Smart

**Theme:** RAG, Multi-Agent Orchestration & Advanced Patterns

## Learning Objectives

By the end of Day 3, you will:

- Understand Retrieval-Augmented Generation (RAG) and why it matters
- Build a knowledge index from travel content
- Create a Local Guide agent powered by RAG
- Design and implement multi-agent orchestration
- Build an Orchestrator that routes to specialist agents
- Implement human-in-the-loop confirmation patterns

## Schedule

| Time | Lab | Description |
|------|-----|-------------|
| 9:00–9:15 | **Day 2 Recap** | Review, Q&A, showcase Trip Planner itineraries |
| 9:15–10:45 | **[Lab 1: RAG & Knowledge Index](lab-1-rag-knowledge.md)** | Build a knowledge base and create the Local Guide agent |
| 10:45–11:00 | *Break* | |
| 11:00–12:00 | **[Lab 2: Multi-Agent Design](lab-2-multi-agent.md)** | Design the multi-agent architecture and agent communication |
| 12:00–1:00 | *Lunch* | |
| 1:00–2:45 | **[Lab 3: The Orchestrator](lab-3-orchestrator.md)** | Build the Orchestrator that routes to specialist agents |
| 2:45–3:00 | *Break* | |
| 3:00–4:00 | **Lab 4: Integration & Testing** | Wire everything together, test end-to-end flows |

## Key Concepts Introduced

### RAG (Retrieval-Augmented Generation)

RAG is a pattern that enhances LLM responses with relevant information retrieved from your own data:

```
User: "What's the best ramen spot in Shibuya?"
  │
  ▼
Search your knowledge index → Find relevant travel guide chunks
  │
  ▼
LLM receives: system prompt + retrieved context + user question
  │
  ▼
Response grounded in YOUR curated data (not just LLM training data)
```

**Why RAG instead of fine-tuning?**
- Your data stays current (just update the index)
- No expensive model retraining
- Full control over what information the agent can access
- Easier to debug ("the agent said X because it found Y in the index")

### Multi-Agent Architecture

Instead of one massive agent that tries to do everything, you build **specialized agents** that collaborate:

```
                    ┌──────────────────┐
                    │   Orchestrator   │
                    │  (routes intent) │
                    └────────┬─────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
     ┌────────────┐ ┌────────────┐ ┌────────────┐
     │ Destination│ │    Trip    │ │   Local    │
     │  Advisor   │ │  Planner  │ │   Guide    │
     │  (Day 1)   │ │  (Day 2)  │ │  (Day 3)  │
     └────────────┘ └────────────┘ └────────────┘
```

**Benefits:**
- Each agent is simpler and more focused
- Easier to test, debug, and improve individually
- Different agents can use different models or configurations
- Scales better — add new agents without changing existing ones

### Human-in-the-Loop

Some actions shouldn't be automated. The agent should pause and ask for confirmation before:
- Booking flights or hotels (committing money)
- Sending notifications
- Modifying reservations

## Starter Code

- **Local Guide:** [`src/day-3/local-guide/`](../../src/day-3/local-guide/)
- **Orchestrator:** [`src/day-3/orchestrator/`](../../src/day-3/orchestrator/)

## What's Next?

In [Day 4](../day-4/README.md), you'll **deploy** the full multi-agent system to Microsoft Foundry, **evaluate** its quality, and **optimize** its performance.
