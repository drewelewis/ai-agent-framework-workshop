# Beginner Primer — Key Concepts

This page explains foundational concepts used throughout the workshop. Refer back to it whenever you encounter an unfamiliar term.

---

## Python Concepts

### Virtual Environments

A **virtual environment** is an isolated Python installation just for your project. It keeps your project's packages separate from other projects (and from your system Python), so different projects can use different package versions without conflicts.

```bash
# Create a virtual environment in a folder called ".venv"
python -m venv .venv

# Activate it (you'll see (.venv) in your terminal prompt)
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
```

Once activated, any `pip install` only affects this virtual environment. When you're done, type `deactivate` to exit.

### `.env` Files and `python-dotenv`

An `.env` file stores **configuration values** (like API keys and connection strings) as simple key-value pairs:

```env
PROJECT_ENDPOINT=https://my-project.services.ai.azure.com/api
MODEL_DEPLOYMENT_NAME=gpt-4o
```

**Why use `.env` files?**
- Keeps secrets out of your source code (never commit `.env` to git!)
- Makes it easy to change settings without editing code
- Different environments (dev, staging, production) just use different `.env` files

The `python-dotenv` package loads these values into your code so you can access them with `os.getenv("PROJECT_ENDPOINT")`.

### Classes and Inheritance

In Python, a **class** is a blueprint for creating objects. **Inheritance** lets you create a new class based on an existing one:

```python
# BaseAgent is the "parent" class (provided by the framework)
# Your agent is the "child" class — it inherits all of BaseAgent's behavior
class DestinationAdvisor(BaseAgent):
    def __init__(self):
        # super().__init__() calls the parent's setup method
        super().__init__(
            name="destination-advisor",
            system_prompt="You are a travel expert...",
        )
```

You don't need to be an OOP expert — just know that `super().__init__(...)` passes your settings up to the framework, which handles the rest.

---

## Web & API Concepts

### HTTP Server

An **HTTP server** is a program that listens for requests over the network and sends back responses. When you run your agent, it starts a web server that:

1. Listens on a **port** (e.g., `http://localhost:8000`)
2. Receives messages from users (via HTTP POST requests)
3. Sends those messages to the LLM
4. Returns the LLM's response

**Uvicorn** is the web server software that runs your agent. When you see `Uvicorn running on http://0.0.0.0:8000`, your agent is ready to receive messages.

### API Endpoints

An **endpoint** is a URL that your server responds to. Your agent exposes:

- `POST /responses` — Send a message and get a response

### Testing with `curl`

`curl` is a command-line tool for sending HTTP requests. In this workshop, you use it to send messages to your agent:

```bash
# Windows cmd (^ continues the command on the next line)
curl -X POST http://localhost:8000/responses ^
  -H "Content-Type: application/json" ^
  -d "{\"input\": \"Hello!\", \"model\": \"gpt-4o\"}"
```

> **Tip:** If `curl` commands feel awkward, install the **REST Client** extension in VS Code. Create a file called `test.http` and write:
> ```http
> POST http://localhost:8000/responses
> Content-Type: application/json
>
> {
>   "input": "Hello!",
>   "model": "gpt-4o"
> }
> ```
> Click "Send Request" above the request to test your agent visually.

### JSON

**JSON** (JavaScript Object Notation) is a text format for structured data. APIs use it to send and receive data:

```json
{
  "input": "Find flights to Tokyo",
  "model": "gpt-4o"
}
```

---

## Azure Concepts

### Azure Subscription

An Azure **subscription** is your billing account. All Azure resources you create live inside a subscription, and costs are charged to it.

### Resource Group

A **resource group** is a container that holds related Azure resources together (like a folder). The workshop creates one resource group with all the services you need.

### Azure AI Foundry

**Azure AI Foundry** is Microsoft's platform for building and hosting AI applications. Think of it as a workspace where you:
- Deploy AI models (like GPT-4o)
- Host your agents in production
- Monitor how they're performing

### Azure Container Registry (ACR)

ACR is a private storage service for **Docker container images** (explained below). On Day 4, you push your agent's container to ACR so Foundry can run it.

### Azure AI Search

A search service that powers **RAG** (Day 3). It stores your travel guide content as searchable chunks, so your agent can look up specific information.

---

## AI Concepts

### Tokens

LLMs don't read words — they read **tokens**. A token is roughly ¾ of a word:

| Text | Approximate Tokens |
|------|-------------------|
| "Hello" | 1 token |
| "San Francisco" | 2 tokens |
| A 500-word essay | ~375 tokens |

Everything has a token cost: your system prompt, the user's message, and the agent's response. Models have a **context window** (maximum tokens per conversation), so keeping prompts concise matters.

### System Prompt vs. User Message

- **System prompt**: Instructions you write that tell the LLM how to behave. Sent with every conversation but hidden from the user.
- **User message**: What the user types.

The LLM sees both: `[system prompt] + [user message]` → generates response.

### Tool Calling

LLMs can't access databases, APIs, or the internet on their own. **Tool calling** is the mechanism where:

1. You tell the LLM about available functions (tools)
2. The LLM decides when to call them and with what arguments
3. **Your code** runs the function and returns results to the LLM
4. The LLM uses the results to form a response

The framework handles this automatically — you just write normal Python functions and pass them to your agent. The framework reads your function's name, docstring, and parameter types to tell the LLM what the tool does.

### RAG (Retrieval-Augmented Generation)

RAG lets your agent answer questions using **your own data** instead of just its training data:

1. Your documents are split into chunks and stored in a search index
2. When a user asks a question, the most relevant chunks are retrieved
3. Those chunks are included in the prompt so the LLM can reference them

**Analogy:** It's like giving someone an open-book exam instead of asking them to answer from memory.

### Embeddings

An **embedding** converts text into a list of numbers (a vector) that captures its meaning. Texts with similar meanings have similar embeddings — like GPS coordinates for ideas.

| Text | Embedding (simplified) |
|------|----------------------|
| "best sushi in Tokyo" | [0.8, 0.3, 0.9, ...] |
| "top Japanese restaurants" | [0.7, 0.3, 0.8, ...] ← similar! |
| "flight to Barcelona" | [0.1, 0.9, 0.2, ...] ← different |

This is how RAG search finds relevant chunks by meaning, not just keyword matching.

---

## Docker Concepts (Day 4)

### What is Docker?

Docker lets you package your application and all its dependencies into a **container** — a lightweight, portable box that runs the same way everywhere.

**Why Docker?**
- "Works on my machine" → works everywhere
- Your agent, its Python packages, and configuration are all bundled together
- Foundry runs your container in the cloud

### Dockerfile

A **Dockerfile** is a recipe that tells Docker how to build your container:

```dockerfile
FROM python:3.11-slim          # Start with a Python base image
WORKDIR /app                    # Set the working directory
COPY requirements.txt .         # Copy dependency list
RUN pip install -r requirements.txt  # Install dependencies
COPY . .                        # Copy your code
EXPOSE 8000                     # Declare the port
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]  # Start command
```

### Key Docker Commands

```bash
docker build -t my-app .        # Build a container image from the Dockerfile
docker run -p 8000:8000 my-app  # Run the container, mapping port 8000
docker push registry/my-app     # Upload the image to a registry (like ACR)
```

---

## Common Troubleshooting

### "Module not found" error
Your virtual environment isn't activated, or you haven't installed dependencies:
```bash
.venv\Scripts\activate          # Activate first
pip install -r requirements.txt # Then install
```

### "Address already in use" error
Another process is using port 8000. Either stop it or use a different port:
```bash
python app.py --port 8001
```

### `curl` gives garbled output on Windows
Use PowerShell's `Invoke-RestMethod` instead (shown in the labs), or pipe curl output through `python -m json.tool` for formatting.

### Agent doesn't respond / hangs
- Check the terminal running your agent for error messages
- Verify your `.env` file has the correct `PROJECT_ENDPOINT` value
- Make sure your Azure model deployment is active

### Docker build fails
- Is Docker Desktop running?
- Are you in the correct directory (with the Dockerfile)?
- Check for typos in the Dockerfile
