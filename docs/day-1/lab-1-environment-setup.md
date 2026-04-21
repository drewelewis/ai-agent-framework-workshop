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

You can check for available models via the CLI, but the **portal approach below is easier for beginners**.

<details>
<summary>CLI option (advanced)</summary>

```bash
az cognitiveservices model list \
  --resource-group <your-rg> \
  --name <your-ai-services-name> \
  -o table
```
Look for `gpt-4o` in the output.
</details>

If no deployment exists, create one through the Azure AI Foundry portal:

1. Navigate to [Azure AI Foundry](https://ai.azure.com)
2. Open your project
3. Go to **Models + endpoints** → **Deploy model**
4. Select **gpt-4o** → Deploy
5. Note the **deployment name** (e.g., `gpt-4o`)

---

## Step 5: Set Up Your Day 1 Project

First, create a **virtual environment** — an isolated Python installation for this workshop so its packages don't interfere with anything else on your system.

> **New to virtual environments?** See the [Beginner Primer](../BEGINNER-PRIMER.md#virtual-environments) for a fuller explanation.

```bash
# Create a virtual environment in a folder called ".venv"
python -m venv .venv

# Activate it — you should see (.venv) appear in your terminal prompt
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
```

Now navigate to the Day 1 starter code and install its dependencies:

```bash
cd src/day-1/destination-advisor
pip install -r requirements.txt
```

Finally, create your environment file. This is where your project-specific settings (like your Azure endpoint) are stored, separate from your code:

```bash
copy .env.sample .env           # Windows
# cp .env.sample .env           # macOS/Linux
```

---

## Step 6: Configure Environment Variables

Open `src/day-1/destination-advisor/.env` in your editor and fill in your values:

```env
PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api
MODEL_DEPLOYMENT_NAME=gpt-4o
```

> **What is a `.env` file?** It's a simple text file that stores configuration values as `KEY=value` pairs. Your code reads these at startup using the `python-dotenv` package. This keeps secrets out of your source code. See the [Beginner Primer](../BEGINNER-PRIMER.md#env-files-and-python-dotenv) for more detail.

> **Where to find these values:**
> - `PROJECT_ENDPOINT` — From the `azd up` output you saved in Step 3, or go to the Azure AI Foundry portal → Your Project → Overview
> - `MODEL_DEPLOYMENT_NAME` — The name you chose when deploying GPT-4o (usually just `gpt-4o`)

---

## Step 7: Verify Setup

Run the verification script to confirm everything is configured:

```bash
python ../../verify_setup.py
```

You should see your endpoint and model name printed, followed by "Everything looks good!" If you see errors, double-check your `.env` file.

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Azure resources are provisioned
- [ ] GPT-4o model is deployed
- [ ] Virtual environment is activated
- [ ] Dependencies are installed
- [ ] `.env` file is configured with valid values

**Next:** [Lab 2: Your First Agent →](lab-2-first-agent.md)
