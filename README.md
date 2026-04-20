# Contoso Travel — AI Agent Framework Workshop

A 4-day hands-on workshop that takes developers from zero AI experience to building, deploying, and optimizing a production-grade multi-agent travel platform on Microsoft Foundry using the Microsoft Agent Framework.

## What You'll Build

**Contoso Travel** — an AI-powered trip planning platform with multiple specialized agents:

| Agent | Purpose | Day |
|-------|---------|-----|
| **Destination Advisor** | Recommends travel destinations based on preferences | Day 1 |
| **Trip Planner** | Searches flights/hotels, builds itineraries using tool calling | Day 2 |
| **Local Guide** | Answers questions about destinations using RAG over travel content | Day 3 |
| **Orchestrator** | Routes user requests to the right specialist agent | Day 3 |
| **Production Deployment** | Full system deployed, evaluated, and optimized on Foundry | Day 4 |

## Workshop Schedule

| Day | Theme | Key Concepts |
|-----|-------|-------------|
| [Day 1](docs/day-1/README.md) | **Hello, Agent** | AI fundamentals, Agent Framework, prompt engineering |
| [Day 2](docs/day-2/README.md) | **Make It Useful** | Tool calling, Bing Grounding, structured outputs |
| [Day 3](docs/day-3/README.md) | **Make It Smart** | RAG, multi-agent orchestration, human-in-the-loop |
| [Day 4](docs/day-4/README.md) | **Ship It** | Containerization, Foundry deployment, evaluation, optimization |

## Repository Structure

```
ai-agent-framework-workshop/
├── docs/                        # Lab guides for each day
│   ├── day-1/                   # Foundations & first agent
│   ├── day-2/                   # Tools & grounding
│   ├── day-3/                   # RAG & multi-agent
│   └── day-4/                   # Production deployment
├── src/                         # Starter code (with TODOs)
│   ├── day-1/destination-advisor/
│   ├── day-2/trip-planner/
│   ├── day-3/local-guide/
│   ├── day-3/orchestrator/
│   └── day-4/production/
├── solutions/                   # Complete reference solutions
│   ├── day-1/
│   ├── day-2/
│   ├── day-3/
│   └── day-4/
├── data/                        # Sample data for RAG & eval
│   ├── travel-guides/
│   └── eval-datasets/
├── infra/                       # Azure infrastructure (Bicep)
├── PREREQUISITES.md             # Setup checklist
└── azure.yaml                   # Azure Developer CLI config
```

## How to Use This Workshop

1. **Read [PREREQUISITES.md](PREREQUISITES.md)** and complete all setup before Day 1
2. **Each day** has its own folder under `docs/` with a README overview and numbered labs
3. **Starter code** in `src/` contains scaffolded files with `# TODO` markers for you to complete
4. **Solutions** in `solutions/` provide complete reference implementations — try before peeking!
5. **Each lab builds on the previous** — complete them in order

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd ai-agent-framework-workshop

# Set up Python environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

# Install Day 1 dependencies
cd src/day-1/destination-advisor
pip install -r requirements.txt

# Copy and configure environment
copy .env.sample .env
# Edit .env with your values

# Start the lab guides
# Open docs/day-1/README.md
```

## License

This workshop is provided for educational purposes.
