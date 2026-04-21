# Lab 2: Your First Agent

**Duration:** ~75 minutes

## Objective

Build and run a **Destination Advisor** agent that recommends travel destinations based on user preferences. This is your first AI agent — built with the Microsoft Agent Framework.

---

## Concepts

### How an Agent Works

```
User Message → System Prompt + User Message → LLM → Response → User
```

1. The user sends a message ("I want a beach vacation in December")
2. Your agent combines the **system prompt** (instructions) with the user's message
3. The LLM processes everything and generates a response
4. The response is returned to the user

### Agent Framework Architecture

```
┌─────────────────────────────────┐
│          Your Agent             │
│  (extends BaseAgent)           │
│                                 │
│  ┌───────────────────────────┐ │
│  │     System Prompt         │ │
│  │  "You are a travel..."    │ │
│  └───────────────────────────┘ │
│  ┌───────────────────────────┐ │
│  │     invoke() method       │ │
│  │  Handles each message     │ │
│  └───────────────────────────┘ │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│         HTTP Server             │
│   (OpenAI Responses API)       │
│   POST /responses               │
└─────────────────────────────────┘
```

---

## Step 1: Explore the Starter Code

Open `src/day-1/destination-advisor/` and review the files:

| File | Purpose |
|------|---------|
| `app.py` | Main application — your agent definition and HTTP server |
| `requirements.txt` | Python dependencies |
| `.env.sample` | Environment variable template |

---

## Step 2: Implement the Agent

Open `src/day-1/destination-advisor/app.py`. You'll see a scaffolded agent with `# TODO` markers.

### TODO 1: Define the System Prompt

Find the `SYSTEM_PROMPT` variable and write instructions for your Destination Advisor. A good system prompt should include:

- **Identity:** Who is the agent? (e.g., "You are Contoso Travel's destination advisor")
- **Capabilities:** What can it do? (recommend destinations, compare options)
- **Constraints:** What should it NOT do? (don't book flights, don't make up prices)
- **Tone:** How should it communicate? (friendly, professional, enthusiastic about travel)
- **Format:** How should responses be structured? (use bullet points, include key facts)

**Example starter prompt:**

```
You are the Destination Advisor for Contoso Travel, an enthusiastic and knowledgeable
travel expert. Your role is to help travelers discover their perfect destination.

When recommending destinations, always include:
- Best time to visit
- Average temperature
- One unique experience only found there
- A rough budget category (Budget / Mid-Range / Luxury)

Be conversational and enthusiastic, but honest about drawbacks.
Never make up specific prices or flight times.
If asked about bookings, explain that the Trip Planner agent handles that.
```

### TODO 2: Create the Agent Class

Implement the `DestinationAdvisor` class that extends `BaseAgent`. This means your agent **inherits** all the framework’s built-in behavior (handling messages, connecting to the LLM, etc.) and you just provide the configuration:

> **New to classes?** See the [Beginner Primer](../BEGINNER-PRIMER.md#classes-and-inheritance) for a quick explanation.

```python
class DestinationAdvisor(BaseAgent):
    def __init__(self):
        super().__init__(
            name="destination-advisor",
            description="Recommends travel destinations based on preferences",
            system_prompt=SYSTEM_PROMPT,
            model=os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4o"),
        )
```

### TODO 3: Set Up the HTTP Server

Configure the agent to run as an HTTP server — this lets you send messages to your agent over the network:

```python
app = AgentApp()
app.add_agent(DestinationAdvisor())
```

> **What’s an HTTP server?** It’s a program that listens for incoming requests (like messages from users) and sends back responses. Your agent will listen on `http://localhost:8000`. See the [Beginner Primer](../BEGINNER-PRIMER.md#http-server) for more detail.

---

## Step 3: Run Your Agent

```bash
cd src/day-1/destination-advisor
python app.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Uvicorn** is the web server that runs your agent. When you see this output, your agent is running and ready to receive messages at `http://localhost:8000`.

> To stop the server, press `Ctrl+C` in the terminal.

---

## Step 4: Test Your Agent

Open a **new terminal** (keep the agent running in the first one) and send a test request.

Choose whichever method you’re most comfortable with:

### Option A: curl (Windows cmd)

The `^` character lets you split a long command across multiple lines in cmd:

```bash
curl -X POST http://localhost:8000/responses ^
  -H "Content-Type: application/json" ^
  -d "{\"input\": \"I want a relaxing beach vacation in December for about a week. I like snorkeling and local food.\", \"model\": \"gpt-4o\"}"
```

### Option B: PowerShell

```powershell
$body = @{
    input = "I want a relaxing beach vacation in December for about a week. I like snorkeling and local food."
    model = "gpt-4o"
} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/responses" -Method Post -ContentType "application/json" -Body $body
```

### Option C: VS Code REST Client (Recommended for beginners)

Install the **REST Client** extension in VS Code, then create a file called `test.http` with:

```http
POST http://localhost:8000/responses
Content-Type: application/json

{
  "input": "I want a relaxing beach vacation in December for about a week. I like snorkeling and local food.",
  "model": "gpt-4o"
}
```

Click **Send Request** above the `POST` line to test your agent.

> **Tip:** See the [Beginner Primer](../BEGINNER-PRIMER.md#testing-with-curl) for more on API testing.

---

## Step 5: Experiment with Conversations

Try these prompts and observe how your agent responds:

1. **Specific request:** "I want to see the Northern Lights but I hate cold weather"
2. **Comparison:** "Compare Thailand and Bali for a honeymoon"
3. **Edge case:** "Book me a flight to Paris" (should politely redirect)
4. **Vague request:** "I want to go somewhere" (should ask clarifying questions)
5. **Off-topic:** "What's the best programming language?" (should stay on topic)

---

## Step 6: Iterate on Your System Prompt

Based on your experiments, refine your system prompt:

- Did the agent stay in character?
- Were responses the right length?
- Did it handle edge cases gracefully?
- Was the tone appropriate?

Make changes to `SYSTEM_PROMPT`, restart the server, and test again.

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Agent starts without errors
- [ ] Agent responds to travel questions with relevant recommendations
- [ ] Agent politely handles off-topic or out-of-scope requests
- [ ] You've iterated on the system prompt at least twice

**Next:** [Lab 3: Prompt Engineering →](lab-3-prompt-engineering.md)
