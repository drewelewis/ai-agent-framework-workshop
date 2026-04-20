# Contoso Travel — Production Deployment
# Day 4: Consolidated multi-agent system for Foundry

import os
from dotenv import load_dotenv

load_dotenv()


# =============================================================================
# TODO 1: Import and configure the hosting adapter
# =============================================================================
# The hosting adapter wraps your agent to serve the Foundry Responses API.
#
# from azure.ai.agentserver.agentframework import AgentServer
# from agents import TravelOrchestrator
#
# orchestrator = TravelOrchestrator()
# server = AgentServer(agent=orchestrator)
# app = server.app
# =============================================================================

# Your hosting adapter setup here:


# =============================================================================
# Fallback: local development server
# =============================================================================
# When running locally (not in Foundry), you can use the AgentApp directly.
# The hosting adapter is only needed for Foundry deployment.
#
# Uncomment this for local development:
# from agent_framework import AgentApp
# from agents import TravelOrchestrator
# app = AgentApp()
# app.add_agent(TravelOrchestrator())
# =============================================================================


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
