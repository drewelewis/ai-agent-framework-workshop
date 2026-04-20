# Lab 3: Optimize & Compare

**Duration:** ~90 minutes

## Objective

Use your evaluation results to optimize the agent's prompts, deploy a v2, and compare it against v1 to verify improvement.

---

## The Optimization Loop

```
┌─────────────────┐
│ Evaluate (v1)   │
│ Score: 3.8 avg  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Analyze failures│
│ Cluster patterns│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Optimize prompts│
│ Address issues  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Deploy v2       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluate (v2)   │
│ Score: 4.3 avg  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Compare v1 ↔ v2│
│ Keep winner     │
└─────────────────┘
```

---

## Step 1: Review Your Evaluation Findings

From Lab 2, you identified failure patterns. Common issues you might have found:

| Issue | Root Cause | Prompt Fix |
|-------|-----------|------------|
| Agent answers travel Qs directly | Orchestrator routing too loose | Add "NEVER answer travel questions — always route" |
| Responses too long/short | No length guidance | Add "Keep responses between 100-300 words" |
| Missing budget info | Advisor doesn't ask | Add "Always ask about budget before recommending" |
| Format inconsistent | Format rules unclear | Add explicit format template with examples |
| Guardrail bypass | Safety rules too vague | Add specific examples of attacks and responses |

---

## Step 2: Optimize Your Prompts

Apply targeted fixes to your system prompts based on evaluation data.

### Optimization Principles

1. **Be specific, not general** — "Always include budget" beats "Be helpful"
2. **Add examples of failures** — Show the agent what NOT to do
3. **Prioritize high-impact fixes** — Fix the issues that affect the most queries
4. **Make one change at a time** — So you can measure what worked

### Example: Improving Task Adherence

**Before:**
```
You are a travel advisor. Help users plan trips.
```

**After:**
```
You are the Destination Advisor for Contoso Travel.

## Response Requirements (ALWAYS follow)
1. ALWAYS ask about budget before recommending destinations
2. ALWAYS include exactly 3 destination options
3. For each destination, ALWAYS include:
   - Best months to visit
   - Average daily cost (budget/mid/luxury)
   - One unique experience
   - One honest drawback
4. NEVER recommend destinations without asking about:
   - Travel dates
   - Group size
   - Activity preferences
```

---

## Step 3: Deploy v2

After updating your prompts in `agents.py`:

```bash
# Rebuild with changes
docker build -t contoso-travel:v2 .

# Tag and push
docker tag contoso-travel:v2 <your-acr>.azurecr.io/contoso-travel:v2
docker push <your-acr>.azurecr.io/contoso-travel:v2

# Update the hosted agent to use v2
# Via Foundry portal: Agents → contoso-travel → Update container image
```

---

## Step 4: Evaluate v2

Run the **exact same dataset** against v2:

1. Same `core-queries.jsonl` file
2. Same evaluators (relevance, task_adherence, intent_resolution)
3. Record results

---

## Step 5: Compare Versions

### Side-by-Side Comparison

| Evaluator | v1 Score | v2 Score | Change |
|-----------|----------|----------|--------|
| Relevance | 4.2 | ? | ? |
| Task Adherence | 3.8 | ? | ? |
| Intent Resolution | 4.0 | ? | ? |
| **Average** | **4.0** | **?** | **?** |

### Per-Query Comparison

For queries that scored poorly in v1, check if v2 improved:

| Query | v1 Score | v2 Score | Fixed? |
|-------|----------|----------|--------|
| "Book me a flight!" | 2 | ? | ? |
| "What's your name?" | 3 | ? | ? |

### Decision: Keep or Revert?

- **v2 better overall AND no regressions** → Keep v2, continue iterating
- **v2 better overall BUT regressions on some queries** → Fix regressions → v3
- **v2 worse or neutral** → Revert to v1, try different optimization approach

---

## Step 6: Production Readiness Discussion

Now that you've experienced the full lifecycle, let's discuss production considerations:

### Monitoring
- Set up Application Insights for trace collection
- Monitor response latency, token usage, and error rates
- Alert on quality regressions (eval score drops)

### CI/CD for Agents
```
Code Change → Build → Deploy to Staging → Run Evals → 
If pass → Deploy to Production
If fail → Block deployment, alert team
```

### Cost Management
- Monitor token consumption per agent
- Consider using smaller models for simple routing (Orchestrator)
- Cache frequent responses where appropriate

### Responsible AI
- Regular evaluation for bias and fairness
- Content safety filters (built into Foundry)
- User feedback loop for continuous improvement
- Transparency about AI limitations

---

## Step 7: Celebrate! 🎉

You've completed the full AI agent development lifecycle:

```
Day 1: Learned AI concepts → Built first agent → Mastered prompt engineering
Day 2: Added tool calling → Connected live data → Built Trip Planner
Day 3: Implemented RAG → Designed multi-agent system → Built Orchestrator
Day 4: Deployed to Foundry → Evaluated quality → Optimized with data
```

You now have the skills to build production AI solutions with the Microsoft Agent Framework.

---

## ✅ Final Checkpoint

- [ ] Prompts optimized based on evaluation data
- [ ] v2 deployed to Foundry
- [ ] v2 evaluated with the same dataset
- [ ] v1 vs v2 comparison documented
- [ ] You can explain the optimization loop
- [ ] You understand production monitoring and CI/CD for agents
- [ ] You have a working, deployed, evaluated AI travel platform!

---

## What's Next?

### Continue Learning
- [Microsoft Agent Framework Documentation](https://github.com/microsoft/agent-framework)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Foundry Samples Repository](https://github.com/azure-ai-foundry/foundry-samples)

### Challenge Ideas
- Add a **Flight Tracker** agent with real-time status
- Implement **multi-language support** (system prompts in different languages)
- Build a **Feedback Loop** that captures user ratings
- Create **custom evaluators** for domain-specific quality (Phase 2)
- Add **conversation memory** with persistent storage
