# Lab 2: Multi-Agent Design

**Duration:** ~60 minutes

## Objective

Design the multi-agent architecture for Contoso Travel and understand how agents communicate and collaborate.

---

## Concepts: Why Multi-Agent?

### The Monolith Problem

A single agent with a huge system prompt trying to do everything:
- 🔴 Prompt becomes unwieldy (thousands of tokens of instructions)
- 🔴 Conflicting instructions ("be brief" vs. "be detailed for itineraries")
- 🔴 Hard to test — one change can break unrelated behaviors
- 🔴 All tools loaded always — LLM gets confused choosing from 20+ tools

### The Multi-Agent Solution

Specialized agents, each focused on one job:
- 🟢 Focused system prompts → better performance
- 🟢 Each agent only has its own tools → fewer wrong choices
- 🟢 Test and improve agents independently
- 🟢 Swap out one agent without affecting others
- 🟢 Different agents can even use different models

---

## Step 1: Design the Architecture

Our Contoso Travel system has four agents:

```
┌─────────────────────────────────────────────────────────────┐
│                     ORCHESTRATOR                            │
│  "I understand your intent and route to the right expert"  │
│                                                             │
│  Capabilities:                                              │
│  - Intent classification                                    │
│  - Agent routing                                            │
│  - Conversation continuity                                  │
│  - Human-in-the-loop gating                                │
└──────┬─────────────────┬─────────────────┬─────────────────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ DESTINATION │  │    TRIP     │  │   LOCAL     │
│  ADVISOR    │  │  PLANNER   │  │   GUIDE     │
│             │  │             │  │             │
│ • Recommend │  │ • Flights   │  │ • RAG       │
│ • Compare   │  │ • Hotels    │  │ • Insider   │
│ • Inspire   │  │ • Weather   │  │   tips      │
│             │  │ • Budget    │  │ • Culture   │
│             │  │ • Itinerary │  │ • Food recs │
│  No tools   │  │  5+ tools   │  │  Knowledge  │
│             │  │             │  │  index      │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## Step 2: Define Agent Responsibilities

Document clear boundaries for each agent:

| User Says | Route To | Why |
|-----------|----------|-----|
| "Where should I go for my honeymoon?" | Destination Advisor | Discovery / recommendation |
| "Find flights to Barcelona" | Trip Planner | Specific travel logistics |
| "What's the best neighborhood in Rome?" | Local Guide | Destination-specific knowledge |
| "Plan a 5-day trip to Tokyo" | Trip Planner → Local Guide | Planning + local details |
| "Hello!" / "Thanks!" | Orchestrator | General conversation |

---

## Step 3: Agent Communication Patterns

### Pattern 1: Sequential Routing
User → Orchestrator → Agent A → Orchestrator → User

The simplest pattern. Orchestrator picks one agent per turn.

### Pattern 2: Sequential Multi-Agent
User → Orchestrator → Agent A → Agent B → Orchestrator → User

Orchestrator chains multiple agents. "Plan a trip to Tokyo" might go:
1. Trip Planner (flights, hotels, itinerary skeleton)
2. Local Guide (fill in restaurant and activity details)

### Pattern 3: Human-in-the-Loop
User → Orchestrator → Agent A → Orchestrator → User (confirm?) → Agent A → Orchestrator → User

Agent pauses and asks for user approval before proceeding.

---

## Step 4: Implement Agent-as-Tool Pattern

In the Microsoft Agent Framework, sub-agents can be exposed as tools to the Orchestrator:

```python
from agent_framework import BaseAgent

class Orchestrator(BaseAgent):
    def __init__(self, sub_agents: list[BaseAgent]):
        # Each sub-agent becomes a tool the orchestrator can call
        agent_tools = [agent.as_tool() for agent in sub_agents]

        super().__init__(
            name="orchestrator",
            description="Routes travel queries to specialist agents",
            system_prompt=ORCHESTRATOR_PROMPT,
            model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
            tools=agent_tools,
        )
```

The `as_tool()` method wraps an agent as a callable tool, using the agent's name and description to help the orchestrator choose correctly.

---

## Step 5: Design the Orchestrator Prompt

The orchestrator's system prompt is the most critical in the system:

```
You are the Orchestrator for Contoso Travel. You DO NOT answer travel questions
yourself. Instead, you determine the user's intent and route to the right specialist.

## Available Specialists
- **destination-advisor**: For destination recommendations, comparisons, inspiration
- **trip-planner**: For flights, hotels, itineraries, budgets, logistics
- **local-guide**: For neighborhood tips, food recommendations, cultural insights

## Routing Rules
1. Analyze the user's message to determine intent
2. Route to the MOST relevant specialist
3. For complex requests, route to trip-planner first, then enhance with local-guide
4. For greetings and general chat, respond yourself
5. Always summarize the specialist's response in a conversational way

## Multi-Agent Requests
If a request needs multiple specialists:
1. Call the primary specialist first
2. Enhance with secondary specialist(s)
3. Combine and present a unified response

## NEVER
- Answer travel questions directly (always delegate)
- Route vague requests without asking clarifying questions
- Call multiple specialists simultaneously for the same aspect
```

---

## Step 6: Conversation Context

The Orchestrator needs to maintain conversation context across agent switches:

- If the user discussed Tokyo with the Destination Advisor, then asks "book flights there" → Orchestrator should route to Trip Planner with "Tokyo" context
- If Trip Planner suggested a hotel in Shibuya, and user asks "what's near there?" → Route to Local Guide with "Shibuya" context

This happens naturally if the Orchestrator includes conversation history in its context.

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] You can diagram the multi-agent architecture
- [ ] Each agent has clear, non-overlapping responsibilities
- [ ] You understand the agent-as-tool pattern
- [ ] Orchestrator routing logic is clear
- [ ] You understand how conversation context flows between agents

**Next:** [Lab 3: The Orchestrator →](lab-3-orchestrator.md)
