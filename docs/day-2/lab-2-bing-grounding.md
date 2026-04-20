# Lab 2: Bing Grounding

**Duration:** ~60 minutes

## Objective

Connect your agent to **Bing Grounding** so it can answer questions with live, real-time information from the web — like current travel advisories, real-time events, and seasonal information.

---

## Concepts

### Why Grounding Matters

LLMs are trained on data up to a cutoff date. They can't know:
- Current travel advisories or visa changes
- Today's exchange rates
- Upcoming festivals or events
- Recent hotel or airline reviews

**Bing Grounding** gives your agent live web search capabilities, grounding its responses in current information.

### How It Works

```
User: "Are there any travel advisories for Thailand right now?"
  │
  ▼
Agent → Bing Search → Current results from gov websites
  │
  ▼
LLM synthesizes search results into a coherent answer with citations
```

---

## Step 1: Enable Bing Grounding in Foundry

1. Navigate to [Azure AI Foundry](https://ai.azure.com)
2. Open your project
3. Go to **Models + endpoints**
4. Check if a **Grounding with Bing Search** connection exists
5. If not, add one:
   - Click **Add connection**
   - Select **Grounding with Bing Search**
   - Follow the setup wizard

---

## Step 2: Add Bing Grounding to Your Agent

Update your Trip Planner to include Bing Grounding as a tool. The Agent Framework integrates with Foundry's built-in Bing tool:

```python
from agent_framework import BaseAgent, BingGroundingTool

class TripPlanner(BaseAgent):
    def __init__(self):
        bing_tool = BingGroundingTool(
            connection_name="bing-grounding"  # Your Foundry connection name
        )

        super().__init__(
            name="trip-planner",
            description="Plans trips with real-time information",
            system_prompt=SYSTEM_PROMPT,
            model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
            tools=[search_flights, search_hotels, get_weather, bing_tool],
        )
```

---

## Step 3: Update System Prompt for Grounding

Add instructions for when to use web search:

```
## Web Search Guidelines
- Use Bing search for: current travel advisories, visa requirements, local events,
  exchange rates, and any time-sensitive information
- Always cite your sources when using web search results
- If search results conflict, mention the discrepancy
- Prefer official sources (government travel sites, embassy pages) for safety info
```

---

## Step 4: Test Grounded Responses

Test prompts that require current information:

1. "What are the current entry requirements for Japan?"
2. "Are there any festivals in Barcelona in June 2026?"
3. "What's the current exchange rate for USD to Thai Baht?"
4. "Is it safe to travel to [country] right now?"

Compare the grounded responses vs. what the agent would say without Bing access.

---

## Step 5: Grounding Best Practices

### Do:
- ✅ Use grounding for time-sensitive information
- ✅ Have the agent cite sources
- ✅ Combine grounding with custom tools (e.g., search Bing for advisories, then search flights)

### Don't:
- ❌ Rely on Bing for everything — it adds latency
- ❌ Use grounding for static knowledge the LLM already has
- ❌ Trust grounding results without asking the LLM to validate them

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Bing Grounding is connected in your Foundry project
- [ ] Agent uses web search for current information
- [ ] Responses include source citations
- [ ] Agent chooses between Bing and custom tools appropriately

**Next:** [Lab 3: Trip Planner Agent →](lab-3-trip-planner.md)
