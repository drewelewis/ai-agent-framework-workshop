# Contoso Travel — Sub-Agent Definitions
# Day 3: All specialist agents used by the Orchestrator

import os
from dotenv import load_dotenv

load_dotenv()

from agent_framework import BaseAgent


# =============================================================================
# TODO 1: Define the Destination Advisor (from Day 1)
# =============================================================================
# Recreate your Day 1 agent here with the polished system prompt.
# This agent has NO tools — it uses only the LLM's knowledge.
#
# class DestinationAdvisor(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="destination-advisor",
#             description="Recommends travel destinations based on preferences, budget, and interests",
#             system_prompt=ADVISOR_PROMPT,
#             model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
#         )
# =============================================================================

ADVISOR_PROMPT = """
# TODO: Paste your polished Day 1 system prompt here
"""

# Your DestinationAdvisor class here:


# =============================================================================
# TODO 2: Define the Trip Planner (from Day 2)
# =============================================================================
# Recreate your Day 2 agent with all tools.
# Import tools from a shared location or redefine them here.
#
# Tools needed: search_flights, search_hotels, get_weather, calculate_budget
# =============================================================================

PLANNER_PROMPT = """
# TODO: Paste your polished Day 2 system prompt here
"""

# Your TripPlanner class here:


# =============================================================================
# TODO 3: Define the Local Guide (from Day 3 Lab 1)
# =============================================================================
# Include the knowledge index tool for RAG.
#
# from agent_framework import KnowledgeIndexTool
# =============================================================================

GUIDE_PROMPT = """
# TODO: Paste your Local Guide system prompt here
"""

# Your LocalGuide class here:


# =============================================================================
# Instantiate agents for import by the Orchestrator
# =============================================================================
# destination_advisor = DestinationAdvisor()
# trip_planner = TripPlanner()
# local_guide = LocalGuide()
