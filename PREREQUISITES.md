# Prerequisites

Complete **all** items below before Day 1 of the workshop.

## Required Accounts

- [ ] **Azure Subscription** — with permissions to create resources ([Free trial](https://azure.microsoft.com/free/))
- [ ] **GitHub Account** — for accessing samples and (optionally) source control

## Required Software

| Tool | Version | Install |
|------|---------|---------|
| **Python** | 3.10+ | [python.org](https://www.python.org/downloads/) |
| **VS Code** | Latest | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Azure CLI** | 2.60+ | [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) |
| **Azure Developer CLI (azd)** | Latest | [Install azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) |
| **Docker Desktop** | Latest | [docker.com](https://www.docker.com/products/docker-desktop/) |
| **Git** | Latest | [git-scm.com](https://git-scm.com/downloads) |

## Required VS Code Extensions

- [ ] **Python** (ms-python.python)
- [ ] **AI Toolkit** (ms-windows-ai-studio.windows-ai-studio)
- [ ] **Azure Tools** (ms-vscode.vscode-node-azure-pack)
- [ ] **Docker** (ms-azuretools.vscode-docker)

## Azure Resources (Provisioned Day 1)

The following resources will be created during the workshop. Your subscription must allow:

- **Azure AI Foundry** project (for agent hosting and model access)
- **Azure AI Services** (multi-service resource)
- **Azure Container Registry** (for Day 4 deployment)
- **Azure AI Search** (for Day 3 RAG)
- **Application Insights** (for Day 4 observability)

> **Estimated cost:** Approximately $5–15 for the full workshop using pay-as-you-go pricing. Delete resources after the workshop to stop charges.

## Pre-Workshop Setup Steps

### 1. Verify Python Installation

```bash
python --version
# Should show 3.10 or higher
```

### 2. Log into Azure

```bash
az login
az account show
# Verify correct subscription is selected
```

### 3. Log into Azure Developer CLI

```bash
azd auth login
```

### 4. Verify Docker

```bash
docker --version
docker info
# Ensure Docker Desktop is running
```

### 5. Clone This Repository

```bash
git clone <repo-url>
cd ai-agent-framework-workshop
```

### 6. Create Python Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install --upgrade pip
```

### 7. Provision Azure Infrastructure

```bash
azd init
azd up
```

This provisions all required Azure resources. Note the outputs — you'll need them for `.env` files.

## Verify You're Ready

Run this checklist:

```bash
python --version          # 3.10+
az --version              # 2.60+
azd version               # any recent version
docker --version          # any recent version
git --version             # any recent version
```

All five commands should succeed. If any fail, install the missing tool before Day 1.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `python` not found | Try `python3` or add Python to PATH |
| Azure login fails | Run `az login --use-device-code` |
| Docker not running | Start Docker Desktop application |
| Permission denied on Azure | Contact your subscription admin for Contributor role |
