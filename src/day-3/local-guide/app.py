# Contoso Travel — Local Guide
# Day 3: RAG-Powered Destination Knowledge

import os
from dotenv import load_dotenv

load_dotenv()

from agent_framework import BaseAgent, AgentApp


# =============================================================================
# TODO 1: Set up the Knowledge Index Tool
# =============================================================================
# Connect to the Azure AI Search knowledge index you created with the travel
# guide content.
#
# Example:
#   from agent_framework import KnowledgeIndexTool
#
#   knowledge_tool = KnowledgeIndexTool(
#       index_name="contoso-travel-guides",
#       description="Search travel guides for detailed info about destinations",
#   )
# =============================================================================

# Your knowledge index tool here:


# =============================================================================
# TODO 2: Define the Local Guide system prompt
# =============================================================================
# Your prompt should instruct the agent to:
#   - Search the knowledge base for relevant information
#   - Provide insider tips and local recommendations
#   - Cite which travel guide the information comes from
#   - Be honest when it doesn't have specific info
#   - Include practical details (costs, transport, timing)
# =============================================================================
SYSTEM_PROMPT = """
# TODO: Define your Local Guide system prompt
"""


# =============================================================================
# TODO 3: Create the LocalGuide agent
# =============================================================================
# Build the agent with:
#   - name: "local-guide"
#   - The knowledge index tool
#   - The system prompt above
#
# Example:
#   class LocalGuide(BaseAgent):
#       def __init__(self):
#           super().__init__(
#               name="local-guide",
#               description="Answers detailed destination questions using curated travel guides",
#               system_prompt=SYSTEM_PROMPT,
#               model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
#               tools=[knowledge_tool],
#           )
# =============================================================================

# Your LocalGuide class here:


# =============================================================================
# TODO 4: Set up the HTTP server
# =============================================================================
# app = AgentApp()
# app.add_agent(LocalGuide())
# =============================================================================

# Your server setup here:


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
