# Lab 2: Evaluate Your Agent

**Duration:** ~75 minutes

## Objective

Build evaluation datasets, run batch evaluations against your deployed agent, and analyze the results to identify areas for improvement.

---

## Concepts: Why Evaluate?

"It seems to work" isn't good enough for production. Evaluation gives you:

- **Measurable quality** — scores you can track over time
- **Failure patterns** — categorized issues you can fix systematically
- **Regression detection** — know when changes break things
- **Confidence to ship** — data-backed deployment decisions

### Evaluation Architecture

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Test Dataset    │    │  Deployed Agent  │    │   Evaluators     │
│                  │    │                  │    │                  │
│  query +         │ →  │  Processes each  │ →  │  Score each      │
│  expected_       │    │  query           │    │  response        │
│  behavior        │    │                  │    │  (1-5 scale)     │
└──────────────────┘    └──────────────────┘    └──────────────────┘
                                                        │
                                                        ▼
                                                ┌──────────────────┐
                                                │  Results Report  │
                                                │                  │
                                                │  Scores, trends, │
                                                │  failure clusters│
                                                └──────────────────┘
```

---

## Step 1: Create a Test Dataset

Create a JSONL file with representative user queries and expected behaviors.

Save as `data/eval-datasets/core-queries.jsonl`:

```jsonl
{"query": "Where should I go for a beach vacation in December?", "expected_behavior": "Recommends 2-3 warm destinations suitable for December travel, mentions weather, gives budget ranges"}
{"query": "Find flights from New York to Tokyo on March 15, 2026", "expected_behavior": "Calls flight search tool, returns multiple flight options with prices and times"}
{"query": "What's the best ramen in Shibuya?", "expected_behavior": "Uses knowledge base to find specific ramen restaurants in Shibuya with details"}
{"query": "Plan a 5-day trip to Barcelona for 2 people, mid-range budget", "expected_behavior": "Creates structured itinerary with flights, hotels, day-by-day plan, and budget breakdown"}
{"query": "Book me a flight right now!", "expected_behavior": "Asks for clarification (destination, dates) and explains it will present options for confirmation"}
{"query": "What's the best programming language?", "expected_behavior": "Politely redirects to travel topics, stays in character as travel advisor"}
{"query": "Compare Thailand and Vietnam for a food-focused trip", "expected_behavior": "Provides balanced comparison of both destinations focusing on cuisine, with specific dishes and regions"}
{"query": "Is it safe to travel to Japan right now?", "expected_behavior": "Uses current information (Bing grounding) to provide up-to-date travel safety info with sources"}
{"query": "I want to go somewhere but I don't know where", "expected_behavior": "Asks clarifying questions about preferences: budget, climate, activities, travel dates, group size"}
{"query": "Tell me about the Gothic Quarter in Barcelona", "expected_behavior": "Retrieves info from knowledge base about the Gothic Quarter with specific landmarks, restaurants, and tips"}
```

### Dataset Design Principles

| Principle | Example |
|-----------|---------|
| **Cover happy paths** | Standard destination and planning queries |
| **Cover edge cases** | Vague requests, missing information |
| **Cover safety** | Off-topic, prompt injection attempts |
| **Cover all agents** | Queries for Advisor, Planner, and Guide |
| **Cover multi-turn** | Queries that depend on prior context |

---

## Step 2: Set Up Evaluators

Foundry provides built-in evaluators. For Phase 1, use these:

| Evaluator | What It Measures |
|-----------|-----------------|
| `relevance` | Is the response relevant to the query? |
| `task_adherence` | Does the response follow the system prompt instructions? |
| `intent_resolution` | Does the response address the user's actual intent? |
| `indirect_attack` | Is the agent resistant to prompt injection? |

---

## Step 3: Run a Batch Evaluation

### Via Foundry Portal

1. Navigate to **Agents** → your agent → **Evaluate**
2. Upload your dataset (`core-queries.jsonl`)
3. Select evaluators: relevance, task_adherence, intent_resolution
4. Click **Run evaluation**

### Via CLI/MCP Tools

Your instructor may demonstrate using MCP tools for automated eval runs.

---

## Step 4: Analyze Results

### Read the Scores

Each query gets a score (1-5) per evaluator:

| Score | Meaning |
|-------|---------|
| 5 | Excellent — fully meets expectations |
| 4 | Good — minor issues |
| 3 | Acceptable — notable gaps |
| 2 | Poor — significant problems |
| 1 | Fail — completely wrong or harmful |

### Identify Patterns

Look for:
- **Consistent low scores** on specific evaluators → systemic issue
- **Low scores on specific query types** → gap in system prompt
- **Low intent_resolution** → agent misunderstands what users want
- **Low task_adherence** → agent ignores its instructions

### Cluster Failures

Group failing queries (score ≤ 3) by category:

| Cluster | Queries | Root Cause |
|---------|---------|------------|
| Routing failures | Agent answers directly instead of routing | Orchestrator prompt too permissive |
| Missing tools | Agent can't fulfill request | Tool not implemented |
| Format issues | Response doesn't match expected structure | Format instructions unclear |
| Guardrail bypass | Agent goes off-topic | Safety rules insufficient |

---

## Step 5: Document Your Findings

Create a brief evaluation summary:

```markdown
## Evaluation Results — v1

**Date:** [today]
**Dataset:** core-queries.jsonl (10 queries)
**Agent version:** contoso-travel:v1

### Scores
- Relevance: avg 4.2/5
- Task Adherence: avg 3.8/5
- Intent Resolution: avg 4.0/5

### Top Issues
1. [Describe issue #1 and which queries it affects]
2. [Describe issue #2]
3. [Describe issue #3]

### Action Items for v2
1. [Specific prompt change to address issue #1]
2. [Specific prompt change to address issue #2]
```

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Test dataset created with 10+ diverse queries
- [ ] Batch evaluation completed against deployed agent
- [ ] Results analyzed and failure patterns identified
- [ ] At least 3 actionable improvement items documented
- [ ] You understand the evaluation pipeline end-to-end

**Next:** [Lab 3: Optimize & Compare →](lab-3-optimize.md)
