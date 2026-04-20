# Day 4 — Ship It

**Theme:** Production Deployment, Evaluation & Optimization

## Learning Objectives

By the end of Day 4, you will:

- Containerize your multi-agent system for Foundry deployment
- Deploy a hosted agent to Microsoft Foundry
- Build evaluation datasets and run batch evaluations
- Analyze evaluation results and cluster failures
- Optimize agent prompts using eval-driven insights
- Compare agent versions before and after optimization
- Understand CI/CD and monitoring for production agents

## Schedule

| Time | Lab | Description |
|------|-----|-------------|
| 9:00–9:15 | **Day 3 Recap** | Review, Q&A, demo multi-agent routing |
| 9:15–10:45 | **[Lab 1: Deploy to Foundry](lab-1-deploy.md)** | Containerize, push to ACR, create hosted agent |
| 10:45–11:00 | *Break* | |
| 11:00–12:15 | **[Lab 2: Evaluate Your Agent](lab-2-evaluate.md)** | Build test datasets, run evaluations, analyze results |
| 12:15–1:00 | *Lunch* | |
| 1:00–2:30 | **[Lab 3: Optimize & Compare](lab-3-optimize.md)** | Optimize prompts from eval results, deploy v2, compare |
| 2:30–2:45 | *Break* | |
| 2:45–3:30 | **Lab 4: Production Readiness** | CI/CD, monitoring, responsible AI, cost management |
| 3:30–4:00 | **Workshop Wrap-Up** | Review journey, Q&A, next steps |

## Key Concepts Introduced

### Hosted Agents on Foundry

Your agent runs as a container on Microsoft Foundry. The **hosting adapter** wraps your agent to serve the OpenAI Responses API:

```
Your Agent Code + Hosting Adapter → Docker Container → ACR → Foundry Hosted Agent
```

### Agent Evaluation

Production agents need measurable quality. Evaluation uses:
- **Test datasets:** Representative user queries with expected behaviors
- **Evaluators:** Automated judges (built-in and custom) that score responses
- **Batch eval:** Run your dataset against the deployed agent and get scores

### Prompt Optimization

Use evaluation results to improve your agent:
1. Run evaluation → identify weak areas
2. Cluster failures → understand patterns
3. Optimize prompt → address failure patterns
4. Redeploy → run evaluation again
5. Compare versions → keep the better one

## Starter Code

Your Day 4 production code is in [`src/day-4/production/`](../../src/day-4/production/).

## What You'll Walk Away With

A production-deployed, evaluated, and optimized multi-agent travel platform on Microsoft Foundry — plus the skills to build your own AI solutions from scratch.
