# Contoso Travel — Destination Advisor
# Day 1: Your First Agent

import os
from dotenv import load_dotenv

load_dotenv()

# --- Agent Framework Imports ---
from agent_framework import BaseAgent, AgentApp


# =============================================================================
# TODO 1: Define your system prompt
# =============================================================================
# Write a system prompt that establishes:
#   - Identity: Who is this agent? (name, role, personality)
#   - Capabilities: What can it do? (recommend destinations, compare options)
#   - Constraints: What should it NOT do? (book flights, make up prices)
#   - Tone: How should it communicate? (friendly, professional)
#   - Format: How should responses be structured? (bullet points, categories)
#
# Tip: Start simple and iterate! You'll refine this in Lab 3.
# =============================================================================
SYSTEM_PROMPT = """
# TODO: Replace this with your system prompt
# Example:
# You are the Destination Advisor for Contoso Travel...
"""


# =============================================================================
# TODO 2: Create the Agent Class
# =============================================================================
# Create a class that extends BaseAgent.
# Configure it with:
#   - name: "destination-advisor"
#   - description: a short description of what this agent does
#   - system_prompt: the SYSTEM_PROMPT variable above
#   - model: read from MODEL_DEPLOYMENT_NAME env var
#
# Example:
#   class DestinationAdvisor(BaseAgent):
#       def __init__(self):
#           super().__init__(
#               name="destination-advisor",
#               description="...",
#               system_prompt=SYSTEM_PROMPT,
#               model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
#           )
# =============================================================================

# Your agent class here:


# =============================================================================
# TODO 3: Set up the HTTP server
# =============================================================================
# Create an AgentApp instance and register your agent.
#
# Example:
#   app = AgentApp()
#   app.add_agent(DestinationAdvisor())
#
# Then add the main entry point to run the app.
# =============================================================================

# Your server setup here:


# --- Entry Point ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
