# Contoso Travel — Orchestrator
# Day 3: Multi-Agent Routing

import os
from dotenv import load_dotenv

load_dotenv()

from agent_framework import BaseAgent, AgentApp


# =============================================================================
# TODO 1: Import sub-agents from agents.py
# =============================================================================
# from agents import destination_advisor, trip_planner, local_guide
# =============================================================================


# =============================================================================
# TODO 2: Define the Orchestrator system prompt
# =============================================================================
# The Orchestrator MUST:
#   - Analyze user intent and route to the correct specialist
#   - Handle greetings and general conversation itself
#   - Coordinate multi-agent requests (e.g., plan + local tips)
#   - Maintain conversation context across agent switches
#   - Require human confirmation for "booking" actions
#   - NEVER answer travel questions directly — always delegate
# =============================================================================
ORCHESTRATOR_PROMPT = """
# TODO: Define your Orchestrator system prompt

# Key sections to include:
# - Available specialists and their capabilities
# - Routing rules (which agent handles what)
# - Multi-agent coordination rules
# - Human-in-the-loop confirmation triggers
# - What the orchestrator handles itself (greetings, clarification)
"""


# =============================================================================
# TODO 3: Create the TravelOrchestrator agent
# =============================================================================
# Build the orchestrator that uses sub-agents as tools.
#
# Example:
#   class TravelOrchestrator(BaseAgent):
#       def __init__(self):
#           from agents import destination_advisor, trip_planner, local_guide
#
#           sub_agents = [destination_advisor, trip_planner, local_guide]
#           agent_tools = [agent.as_tool() for agent in sub_agents]
#
#           super().__init__(
#               name="contoso-travel",
#               description="Contoso Travel AI concierge",
#               system_prompt=ORCHESTRATOR_PROMPT,
#               model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
#               tools=agent_tools,
#           )
# =============================================================================

# Your TravelOrchestrator class here:


# =============================================================================
# TODO 4: Set up the HTTP server
# =============================================================================
# app = AgentApp()
# app.add_agent(TravelOrchestrator())
# =============================================================================

# Your server setup here:


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
