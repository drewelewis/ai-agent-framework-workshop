# Contoso Travel — Production Deployment (SOLUTION)
# Day 4: Consolidated multi-agent system for Foundry

import os
from dotenv import load_dotenv

load_dotenv()

from azure.ai.agentserver.agentframework import AgentServer
from agents import TravelOrchestrator

orchestrator = TravelOrchestrator()
server = AgentServer(agent=orchestrator)
app = server.app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
