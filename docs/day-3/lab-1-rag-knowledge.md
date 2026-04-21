# Lab 1: RAG & Knowledge Index

**Duration:** ~90 minutes

## Objective

Build a **Local Guide** agent that answers detailed questions about destinations using your own curated travel content, powered by RAG (Retrieval-Augmented Generation).

---

## Concepts: How RAG Works Under the Hood

### The RAG Pipeline

```
1. INDEXING (one-time setup)
   Travel guides → Chunk into passages → Generate embeddings → Store in search index

2. RETRIEVAL (every query)
   User question → Generate embedding → Search index → Top-K relevant chunks

3. GENERATION (every query)
   System prompt + Retrieved chunks + User question → LLM → Grounded response
```

### Embeddings
An embedding converts text into a list of numbers (a vector) that captures its **meaning**. Texts with similar meanings produce similar vectors — like GPS coordinates for ideas.

| Text | Meaning Cluster |
|------|----------------|
| "best sushi in Tokyo" | food + Tokyo |
| "top Japanese restaurants" | food + Japan ← similar! |
| "cheap flights to Barcelona" | travel + Barcelona ← different |

This lets RAG search find relevant content by meaning, not just keyword matching. For example, searching for "where to eat ramen" can find a chunk titled "Best Noodle Shops in Shibuya" even though the words are different.

> **Want more detail?** See the [Beginner Primer](../BEGINNER-PRIMER.md#embeddings).

### Chunking
Long documents are split into smaller pieces (chunks) so the search can find specific relevant passages rather than entire documents.

---

## Step 1: Review the Travel Content

Check `data/travel-guides/`. You'll find sample travel guides for several destinations:

```
data/travel-guides/
├── tokyo-guide.md
├── barcelona-guide.md
├── bangkok-guide.md
└── rome-guide.md
```

These contain neighborhood guides, food recommendations, cultural tips, and practical travel info.

---

## Step 2: Create the Knowledge Index

### Option A: Azure AI Foundry Portal (Recommended)

1. Navigate to [Azure AI Foundry](https://ai.azure.com) → Your project
2. Go to **Data + indexes** → **New index**
3. Select **Azure AI Search** as the index type
4. Upload the files from `data/travel-guides/`
5. Configure:
   - **Chunking:** Default (1024 tokens with 128 token overlap)
   - **Embedding model:** `text-embedding-ada-002` or `text-embedding-3-small`
6. Create the index and wait for processing

### Option B: Azure CLI

```bash
# Create the search index with the travel guide data
az ai project index create \
  --name "contoso-travel-guides" \
  --project-endpoint "<your-project-endpoint>" \
  --data-source "data/travel-guides/" \
  --embedding-model "text-embedding-3-small"
```

---

## Step 3: Build the Local Guide Agent

Open `src/day-3/local-guide/app.py` and implement the Local Guide.

### TODO 1: Configure the Knowledge Index Connection

```python
from agent_framework import BaseAgent, KnowledgeIndexTool

knowledge_tool = KnowledgeIndexTool(
    index_name="contoso-travel-guides",
    description="Search travel guides for detailed destination information including neighborhoods, food, culture, and practical tips",
)
```

### TODO 2: Write the Local Guide System Prompt

```
You are the Local Guide for Contoso Travel — think of yourself as a knowledgeable
friend who's lived in every city. You provide insider tips, local recommendations,
and cultural context that tourists usually miss.

## How You Work
- Search the travel knowledge base for relevant information
- Combine knowledge base results with your general knowledge
- Always cite which travel guide your information comes from
- If the knowledge base doesn't have info on a destination, say so clearly

## Response Style
- Conversational and enthusiastic
- Include specific names (restaurants, streets, landmarks)
- Add practical tips (how to get there, what to wear, when to go)
- Mention approximate costs in local currency AND USD
- Flag tourist traps and suggest alternatives
```

### TODO 3: Create the Agent and Server

Wire up the agent with the knowledge tool and start the HTTP server.

---

## Step 4: Test RAG Responses

Start the Local Guide and test:

1. **Direct knowledge retrieval:**
   "What are the best ramen shops in Tokyo?"

2. **Specific neighborhood:**
   "Tell me about the Gothic Quarter in Barcelona"

3. **Practical tips:**
   "How do I get from Bangkok airport to Khao San Road?"

4. **Not in knowledge base:**
   "What should I do in Sydney?" (should acknowledge it doesn't have specific guide info)

---

## Step 5: Compare RAG vs. No-RAG

Temporarily disable the knowledge tool and ask the same questions. Notice:

- **With RAG:** Specific restaurant names, street addresses, local tips from your guides
- **Without RAG:** Generic recommendations from LLM training data — may be outdated or generic

This demonstrates the value of RAG.

---

## Step 6: Understand Chunk Relevance

When the agent searches the knowledge base, it retrieves the most relevant chunks. Add logging to see what's being retrieved:

```python
# In your agent's tool handler or callback, log retrieved chunks
print(f"Retrieved {len(chunks)} chunks for query: '{query}'")
for i, chunk in enumerate(chunks):
    print(f"  Chunk {i+1} (score: {chunk.score:.3f}): {chunk.text[:100]}...")
```

This helps debug cases where the agent gives poor answers — often it's a retrieval problem, not a generation problem.

---

## ✅ Checkpoint

Before moving on, confirm:

- [ ] Knowledge index is created with travel guide content
- [ ] Local Guide agent retrieves relevant chunks for travel questions
- [ ] Responses cite information from the knowledge base
- [ ] Agent honestly reports when it doesn't have specific information
- [ ] You understand the RAG pipeline: chunk → embed → search → generate

**Next:** [Lab 2: Multi-Agent Design →](lab-2-multi-agent.md)
