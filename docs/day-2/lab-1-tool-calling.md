# Lab 1: Tool Calling

**Duration:** ~90 minutes

## Objective

Understand how LLMs call tools and build your first set of custom tools for the Trip Planner agent.

> **New to tool calling?** See the [Beginner Primer](../BEGINNER-PRIMER.md#tool-calling) for a high-level overview.

---

## Concepts: The Tool-Call Loop

Tool calling isn't a single step — it's a **loop**:

```
1. User sends message
2. LLM receives message + list of available tools
3. LLM decides: respond directly OR call a tool
4. If tool call:
   a. LLM outputs: tool name + arguments (JSON)
   b. Your code executes the function
   c. Your code sends the result back to the LLM
   d. LLM may call another tool (go to 3) or respond
5. LLM generates final response using all tool results
```

Key insight: The LLM may call **multiple tools** in sequence or even in parallel before generating a response.

---

## Step 1: Understanding Tool Schemas

A tool is defined by its schema. Here's an example:

```python
{
    "type": "function",
    "function": {
        "name": "search_flights",
        "description": "Search for available flights between two cities on a specific date",
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {
                    "type": "string",
                    "description": "Departure city or airport code (e.g., 'New York' or 'JFK')"
                },
                "destination": {
                    "type": "string",
                    "description": "Arrival city or airport code (e.g., 'Tokyo' or 'NRT')"
                },
                "date": {
                    "type": "string",
                    "description": "Travel date in YYYY-MM-DD format"
                }
            },
            "required": ["origin", "destination", "date"]
        }
    }
}
```

> **Pro tip:** The `description` fields are critical. The LLM uses them to decide *when* and *how* to call each tool. Vague descriptions → wrong tool choices.

---

## Step 2: Build Your First Tool

Open `src/day-2/trip-planner/tools.py`. You'll implement several travel tools.

### TODO 1: `search_flights` Tool

This tool simulates a flight search. In a real application, you'd call an airline API.

```python
def search_flights(origin: str, destination: str, date: str) -> dict:
    """Search for available flights between two cities."""
    # For the workshop, we return simulated data
    # In production, this would call a real flight API
    return {
        "flights": [
            {
                "airline": "Contoso Air",
                "flight_number": "CA-201",
                "departure": f"{date}T08:00:00",
                "arrival": f"{date}T14:30:00",
                "price_usd": 450,
                "class": "Economy"
            },
            {
                "airline": "Azure Airlines",
                "flight_number": "AZ-55",
                "departure": f"{date}T10:15:00",
                "arrival": f"{date}T16:45:00",
                "price_usd": 520,
                "class": "Economy"
            },
            {
                "airline": "Contoso Air",
                "flight_number": "CA-205",
                "departure": f"{date}T22:00:00",
                "arrival": f"{date}T04:30:00+1",
                "price_usd": 890,
                "class": "Business"
            }
        ],
        "origin": origin,
        "destination": destination,
        "date": date
    }
```

### TODO 2: `search_hotels` Tool

Build a hotel search tool that accepts destination, check-in date, check-out date, and budget level.

### TODO 3: `get_weather` Tool

Build a weather forecast tool that accepts a city and date range.

---

## Step 3: Register Tools with the Agent

In `app.py`, register your tools with the agent by passing them in the `tools` list:

```python
from tools import search_flights, search_hotels, get_weather

class TripPlanner(BaseAgent):
    def __init__(self):
        super().__init__(
            name="trip-planner",
            description="Plans trips by searching flights, hotels, and weather",
            system_prompt=SYSTEM_PROMPT,
            model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
            tools=[search_flights, search_hotels, get_weather],
        )
```

> **How does the LLM know about the JSON schema?** You might notice we’re passing plain Python functions, not the JSON schema shown in Step 1. The Agent Framework **automatically generates** the tool schema from your function’s:
> - **Name** → becomes the tool name
> - **Docstring** → becomes the tool description
> - **Parameter names and type hints** → become the parameter schema
>
> This is why good docstrings and type hints on your tool functions are critical — they’re what the LLM reads to decide how to call your tools.

---

## Step 4: Test Tool Calling

Start your agent and test with prompts that should trigger tool calls:

1. **Single tool:** "Find flights from Seattle to Barcelona on June 15, 2026"
2. **Multiple tools:** "Plan a trip from NYC to Tokyo, March 10-17, 2026. I need flights and hotels."
3. **No tools needed:** "What's the best time to visit Japan?" (should answer from knowledge)

Observe in the logs which tools are being called and with what arguments.

---

## Step 5: Handle Edge Cases

Test and handle these scenarios:

1. **Missing info:** "Find me a flight to Paris" (no origin, no date — agent should ask)
2. **Invalid input:** "Find flights on yesterday" (past dates)
3. **Tool errors:** What happens if a tool throws an exception?

Add input validation to your tools. You’ll need to import `datetime` (and `timedelta` and `random` for generating simulated data):

```python
from datetime import datetime, timedelta
import random

def search_flights(origin: str, destination: str, date: str) -> dict:
    # Validate date format
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD."}

    # Validate not in the past
    if parsed_date.date() < datetime.now().date():
        return {"error": "Cannot search for flights in the past."}

    # ... rest of implementation
```

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] You can explain the tool-call loop in your own words
- [ ] `search_flights` tool works and returns structured data
- [ ] `search_hotels` tool works with budget filtering
- [ ] `get_weather` tool returns forecast data
- [ ] The agent calls the right tool based on the user's question
- [ ] Tools validate their inputs and return helpful errors

**Next:** [Lab 2: Bing Grounding →](lab-2-bing-grounding.md)
