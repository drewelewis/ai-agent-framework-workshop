# Lab 3: The Orchestrator

**Duration:** ~105 minutes

## Objective

Build the **Orchestrator** agent that routes user requests to the right specialist (Destination Advisor, Trip Planner, or Local Guide) and combines their responses into a unified experience.

---

## Step 1: Set Up the Project

Navigate to `src/day-3/orchestrator/` and set up the project:

```bash
cd src/day-3/orchestrator
pip install -r requirements.txt
copy .env.sample .env           # Windows
# cp .env.sample .env           # macOS/Linux
```

Edit `.env` with your Azure values (same ones you’ve been using).

Review the starter files:

| File | Purpose |
|------|---------|
| `app.py` | Main application — Orchestrator agent and server |
| `agents.py` | Sub-agent definitions (imports from Day 1 & 2) |
| `tools.py` | Tool implementations — copy your implementations from Day 2, or implement the TODOs here |
| `requirements.txt` | Dependencies |

> **Important:** The orchestrator’s Trip Planner agent needs the tool functions you built in Day 2. The `tools.py` file has TODO stubs — either implement them fresh or copy your working implementations from `src/day-2/trip-planner/tools.py`.

---

## Step 2: Define the Sub-Agents

Open `src/day-3/orchestrator/agents.py` and define all three specialist agents.

You'll bring together your work from Days 1 and 2, plus the new Local Guide:

```python
# Each agent is self-contained with its own prompt and tools
destination_advisor = DestinationAdvisor()  # Day 1 — no tools, just a great prompt
trip_planner = TripPlanner()                # Day 2 — flights, hotels, weather, budget tools
local_guide = LocalGuide()                  # Day 3 — RAG-powered knowledge search
```

---

## Step 3: Build the Orchestrator

Open `src/day-3/orchestrator/app.py` and implement the Orchestrator.

### TODO 1: Create the Orchestrator class

```python
class TravelOrchestrator(BaseAgent):
    def __init__(self):
        # Import sub-agents
        from agents import destination_advisor, trip_planner, local_guide

        # Convert sub-agents to tools
        sub_agents = [destination_advisor, trip_planner, local_guide]
        agent_tools = [agent.as_tool() for agent in sub_agents]

        super().__init__(
            name="contoso-travel",
            description="Contoso Travel AI concierge — routes to specialist agents",
            system_prompt=ORCHESTRATOR_PROMPT,
            model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
            tools=agent_tools,
        )
```

### TODO 2: Write the Orchestrator System Prompt

Craft a prompt that handles:
- Intent detection and routing
- Multi-agent coordination for complex requests
- Graceful handling of ambiguous requests
- Conversation continuity across agent switches

### TODO 3: Set up the server

```python
app = AgentApp()
app.add_agent(TravelOrchestrator())
```

---

## Step 4: Test Routing

Start the Orchestrator and verify routing works:

| Test Query | Expected Route |
|------------|---------------|
| "Where should I go in December?" | → Destination Advisor |
| "Find me flights to Rome" | → Trip Planner |
| "What's the best pizza in Naples?" | → Local Guide |
| "Plan a trip to Tokyo, I love anime" | → Trip Planner (primary) + Local Guide (enhance) |
| "Hello!" | → Orchestrator responds directly |
| "Thanks for the help!" | → Orchestrator responds directly |

---

## Step 5: Test Multi-Agent Coordination

Test complex queries that require multiple agents:

### Test 1: Discovery → Planning
```
User: "I want to go somewhere tropical in February"
→ Orchestrator → Destination Advisor → responds with suggestions

User: "Thailand sounds great! Plan a 7-day trip from LA"
→ Orchestrator → Trip Planner → creates itinerary

User: "What's the best street food in Bangkok?"
→ Orchestrator → Local Guide → answers from knowledge base
```

### Test 2: Combined Request
```
User: "Plan a trip to Barcelona and tell me about the food scene"
→ Orchestrator → Trip Planner (logistics) → Local Guide (food details)
→ Orchestrator combines into unified response
```

---

## Step 6: Human-in-the-Loop (Challenge)

Add a confirmation step for high-stakes actions. When the Trip Planner "finds" flights, the Orchestrator should present options and ask the user to confirm before "booking."

```python
# In your orchestrator prompt, add:
"""
## Confirmation Required
When the Trip Planner returns flight or hotel options, present them
to the user and ask for explicit confirmation before proceeding.

Format:
"I found these options for you:
[options]
Would you like to proceed with option X, or should I look for alternatives?"
"""
```

Test it:
1. "Book me a flight to Paris" → Should present options, not auto-"book"
2. "Yes, option 2" → Should confirm the selection
3. "Actually, find something cheaper" → Should search again

---

## Step 7: End-to-End Integration Test

Run through a complete user journey:

```
1. "Hi! I'm planning my first international trip"
   → Orchestrator greets, asks about preferences

2. "I want somewhere warm, good food, not too expensive"
   → Routes to Destination Advisor

3. "Thailand sounds amazing! Can you plan a 5-day trip from NYC?"
   → Routes to Trip Planner (flights, hotels, itinerary)

4. "What's the best area to stay in Bangkok for nightlife?"
   → Routes to Local Guide (RAG search)

5. "Those flights look good, let's go with the morning one"
   → Orchestrator confirms selection

6. "Give me a packing list for Bangkok in March"
   → Routes appropriately (Trip Planner custom tool or Local Guide)

7. "Thanks for all the help!"
   → Orchestrator responds warmly
```

---

## ✅ Checkpoint

Before finishing Day 3, confirm:

- [ ] Orchestrator correctly routes to all three specialist agents
- [ ] Complex requests trigger multiple agents in sequence
- [ ] Conversation context is maintained across agent switches
- [ ] Human-in-the-loop confirmation works for "booking" actions
- [ ] End-to-end user journey works smoothly
- [ ] Each agent contributes its specialty to the overall experience

**Next:** [Day 4 — Ship It →](../day-4/README.md)
