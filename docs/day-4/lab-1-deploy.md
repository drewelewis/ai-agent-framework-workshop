# Lab 1: Deploy to Foundry

**Duration:** ~90 minutes

## Objective

Containerize your Contoso Travel multi-agent system and deploy it as a **hosted agent** on Microsoft Foundry.

---

## Concepts: The Deployment Pipeline

Until now, your agent has been running on your laptop. To make it available to real users, you need to **deploy** it to the cloud. Here’s the pipeline:

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Agent   │    │  Docker  │    │   ACR    │    │ Foundry  │
│  Code    │ →  │  Build   │ →  │   Push   │ →  │  Deploy  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘

1. Your Python code + hosting adapter
2. Build into a Docker container
3. Push to Azure Container Registry
4. Create hosted agent in Foundry → starts container
```

> **New to Docker?** A container is a lightweight, portable package that bundles your code and all its dependencies together so it runs the same way on any machine. See the [Beginner Primer](../BEGINNER-PRIMER.md#docker-concepts-day-4) for a full explanation.

### The Hosting Adapter

The `azure-ai-agentserver-agentframework` package provides the **hosting adapter** — it wraps your agent so it speaks the standard OpenAI Responses API that Foundry expects. Think of it as a translator: Foundry sends requests in a specific format, and the adapter converts them into calls to your agent.

Without the adapter, your agent only runs locally. With it, Foundry can host and manage your agent in the cloud.

---

## Step 1: Prepare Production Code

Navigate to `src/day-4/production/`. This is a consolidated version of your multi-agent system.

### Review the file structure:

```
production/
├── app.py              # Main entry point with hosting adapter
├── agents.py           # All agent definitions (advisor, planner, guide, orchestrator)
├── tools.py            # All tool implementations
├── Dockerfile          # Container definition
├── requirements.txt    # Production dependencies
└── .env.sample         # Environment template
```

### TODO 1: Consolidate Your Agents

Bring your polished agents from Days 1-3 into `agents.py`. Copy your best system prompts, refined tools, and agent configurations.

### TODO 2: Add the Hosting Adapter

In `app.py`, wrap your orchestrator with the hosting adapter:

```python
from azure.ai.agentserver.agentframework import AgentServer
from agents import TravelOrchestrator

# Create the orchestrator (which contains all sub-agents)
orchestrator = TravelOrchestrator()

# Wrap with the hosting adapter for Foundry
server = AgentServer(agent=orchestrator)
app = server.app
```

---

## Step 2: Build the Docker Container

### Review the Dockerfile

The Dockerfile is the recipe Docker uses to build your container. Each line is a step:

```dockerfile
FROM python:3.11-slim          # Start with a base image that has Python installed

WORKDIR /app                    # Set /app as the working directory inside the container

COPY requirements.txt .         # Copy the dependency list into the container
RUN pip install --no-cache-dir -r requirements.txt  # Install Python packages

COPY . .                        # Copy all your code into the container

EXPOSE 8000                     # Document that the app uses port 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]  # Start the server
```

> **Tip:** You don’t need to modify the Dockerfile — just understand that it packages your agent into a portable container.

### Build and Test Locally

```bash
# Build the container
docker build -t contoso-travel:latest .

# Run locally to test
docker run -p 8000:8000 --env-file .env contoso-travel:latest

# Test with a request
curl -X POST http://localhost:8000/responses ^
  -H "Content-Type: application/json" ^
  -d "{\"input\": \"Where should I go for a beach vacation?\", \"model\": \"gpt-4o\"}"
```

> Fix any startup or runtime errors before proceeding to deployment.

---

## Step 3: Push to Azure Container Registry

```bash
# Login to ACR
az acr login --name <your-acr-name>

# Tag the image
docker tag contoso-travel:latest <your-acr-name>.azurecr.io/contoso-travel:v1

# Push to ACR
docker push <your-acr-name>.azurecr.io/contoso-travel:v1
```

Verify the push:
```bash
az acr repository list --name <your-acr-name> -o table
az acr repository show-tags --name <your-acr-name> --repository contoso-travel -o table
```

---

## Step 4: Create the Hosted Agent in Foundry

### Option A: Azure AI Foundry Portal

1. Navigate to [Azure AI Foundry](https://ai.azure.com) → Your project
2. Go to **Agents** → **Create agent** → **Hosted agent**
3. Configure:
   - **Name:** `contoso-travel`
   - **Container image:** `<your-acr>.azurecr.io/contoso-travel:v1`
   - **Environment variables:** Add your `.env` values
4. Click **Create and start**

### Option B: Azure CLI / MCP Tools

The Foundry MCP tools can automate this — your instructor will demonstrate.

---

## Step 5: Test the Deployed Agent

Once the container is running (check status in Foundry portal):

```bash
# Test the deployed agent via Foundry endpoint
curl -X POST "<project-endpoint>/agents/contoso-travel/responses" ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer <your-token>" ^
  -d "{\"input\": \"Plan a trip to Barcelona for next month\", \"model\": \"gpt-4o\"}"
```

Or use the Foundry portal's **Test** tab to chat with your deployed agent.

---

## Step 6: Set Up .foundry Workspace

Initialize the `.foundry` workspace metadata for evaluation and monitoring:

```yaml
# .foundry/agent-metadata.yaml
defaultEnvironment: dev

environments:
  dev:
    projectEndpoint: "https://<your-project>.services.ai.azure.com/api"
    agentName: "contoso-travel"
    azureContainerRegistry: "<your-acr>.azurecr.io"
    testCases:
      - name: "core-travel-queries"
        priority: P0
        dataset: "datasets/core-queries.jsonl"
        evaluators:
          - relevance
          - task_adherence
          - intent_resolution
```

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Docker container builds without errors
- [ ] Container runs locally and responds to requests
- [ ] Image is pushed to ACR
- [ ] Hosted agent is created and running in Foundry
- [ ] Deployed agent responds to test queries via Foundry endpoint
- [ ] `.foundry/agent-metadata.yaml` is configured

**Next:** [Lab 2: Evaluate Your Agent →](lab-2-evaluate.md)
