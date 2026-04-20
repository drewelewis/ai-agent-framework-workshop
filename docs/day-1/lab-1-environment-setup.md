# Lab 1: Environment Setup

**Duration:** ~90 minutes

## Objective

Set up your complete development environment and provision the Azure resources needed for the workshop.

---

## Step 1: Verify Prerequisites

Confirm all tools are installed:

```bash
python --version          # 3.10+
az --version              # 2.60+
azd version               # any recent version
docker --version          # any recent version
```

> **Stuck?** See [PREREQUISITES.md](../../PREREQUISITES.md) for installation links.

---

## Step 2: Authenticate with Azure

```bash
# Login to Azure CLI
az login

# Verify your subscription
az account show --query "{name:name, id:id}" -o table

# Login to Azure Developer CLI
azd auth login
```

> If you have multiple subscriptions, set the correct one:
> ```bash
> az account set --subscription "<your-subscription-id>"
> ```

---

## Step 3: Provision Azure Infrastructure

From the **workshop root** directory:

```bash
cd ai-agent-framework-workshop

# Initialize azd (select your environment name, e.g., "contoso-travel-dev")
azd init

# Provision all resources
azd up
```

This creates:
- **Azure AI Foundry** project
- **Azure AI Services** (multi-service — includes GPT-4o access)
- **Azure Container Registry** (used on Day 4)
- **Azure AI Search** (used on Day 3)
- **Application Insights** (used on Day 4)

> ⏱️ Provisioning takes approximately 5–10 minutes.

**Save the output values** — you'll need `PROJECT_ENDPOINT` and other settings.

---

## Step 4: Deploy a Model

You need a GPT-4o model deployment in your Foundry project.

```bash
# List available models
az cognitiveservices model list \
  --resource-group <your-rg> \
  --name <your-ai-services-name> \
  --query "[?model.name=='gpt-4o'].{name:model.name, version:model.version}" \
  -o table
```

If no deployment exists, create one through the Azure AI Foundry portal:

1. Navigate to [Azure AI Foundry](https://ai.azure.com)
2. Open your project
3. Go to **Models + endpoints** → **Deploy model**
4. Select **gpt-4o** → Deploy
5. Note the **deployment name** (e.g., `gpt-4o`)

---

## Step 5: Set Up Your Day 1 Project

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

# Navigate to Day 1 starter code
cd src/day-1/destination-advisor

# Install dependencies
pip install -r requirements.txt

# Create your environment file
copy .env.sample .env
```

---

## Step 6: Configure Environment Variables

Edit `src/day-1/destination-advisor/.env` with your values:

```env
PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api
MODEL_DEPLOYMENT_NAME=gpt-4o
```

> **Where to find these:**
> - `PROJECT_ENDPOINT` — From `azd up` output, or Azure AI Foundry portal → Project → Overview
> - `MODEL_DEPLOYMENT_NAME` — The name you gave your GPT-4o deployment

---

## Step 7: Verify Setup

Run the verification script:

```bash
python -c "
from dotenv import load_dotenv
import os
load_dotenv()
endpoint = os.getenv('PROJECT_ENDPOINT')
model = os.getenv('MODEL_DEPLOYMENT_NAME')
print(f'Endpoint: {endpoint}')
print(f'Model: {model}')
assert endpoint, 'PROJECT_ENDPOINT not set!'
assert model, 'MODEL_DEPLOYMENT_NAME not set!'
print('Environment configured successfully!')
"
```

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Azure resources are provisioned
- [ ] GPT-4o model is deployed
- [ ] Virtual environment is activated
- [ ] Dependencies are installed
- [ ] `.env` file is configured with valid values

**Next:** [Lab 2: Your First Agent →](lab-2-first-agent.md)
