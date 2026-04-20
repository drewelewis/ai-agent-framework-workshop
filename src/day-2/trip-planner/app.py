# Contoso Travel — Trip Planner
# Day 2: Tool Calling & Bing Grounding

import os
from dotenv import load_dotenv

load_dotenv()

from agent_framework import BaseAgent, AgentApp


# =============================================================================
# TODO 1: Import your tools from tools.py
# =============================================================================
# Import the tool functions you'll build in tools.py:
#   from tools import search_flights, search_hotels, get_weather, calculate_budget
# =============================================================================


# =============================================================================
# TODO 2: Define the Trip Planner system prompt
# =============================================================================
# Your prompt should instruct the agent to:
#   - Gather trip requirements before planning
#   - Use tools to search for flights, hotels, and weather
#   - Use Bing Grounding for current travel info
#   - Produce a structured day-by-day itinerary
#   - Calculate and present a budget breakdown
#   - Include safety/visa info from web search
# =============================================================================
SYSTEM_PROMPT = """
# TODO: Define your Trip Planner system prompt here
"""


# =============================================================================
# TODO 3: Create the TripPlanner agent
# =============================================================================
# Build the agent class with:
#   - name: "trip-planner"
#   - All tools from tools.py
#   - Bing Grounding (optional — requires Foundry connection)
#   - The system prompt above
#
# Example:
#   class TripPlanner(BaseAgent):
#       def __init__(self):
#           super().__init__(
#               name="trip-planner",
#               description="Plans trips with flights, hotels, weather, and budgets",
#               system_prompt=SYSTEM_PROMPT,
#               model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
#               tools=[search_flights, search_hotels, get_weather, calculate_budget],
#           )
# =============================================================================

# Your TripPlanner class here:


# =============================================================================
# TODO 4: Set up the HTTP server
# =============================================================================
# app = AgentApp()
# app.add_agent(TripPlanner())
# =============================================================================

# Your server setup here:


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
