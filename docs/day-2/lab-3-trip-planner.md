# Lab 3: Trip Planner Agent

**Duration:** ~105 minutes

## Objective

Build a complete **Trip Planner** agent that combines all Day 2 skills: multiple tools, Bing Grounding, and structured itinerary output.

---

## The Goal

The Trip Planner should be able to handle:

> "Plan a 5-day trip from San Francisco to Tokyo for 2 people in March 2026. We like food tours, temples, and nightlife. Budget is mid-range, around $3000 per person total."

And produce a structured, actionable itinerary with flights, hotels, and a day-by-day plan.

---

## Step 1: Add the Budget Calculator Tool

Open `src/day-2/trip-planner/tools.py` and implement the budget calculator:

```python
# TODO: Implement calculate_budget tool
# It should accept:
#   - flight_cost: float
#   - hotel_cost_per_night: float
#   - num_nights: int
#   - num_travelers: int
#   - daily_food_budget: float (default: 50)
#   - daily_activities_budget: float (default: 40)
#
# Return a breakdown:
#   - flights_total
#   - hotel_total
#   - food_total
#   - activities_total
#   - grand_total
#   - per_person_total
```

---

## Step 2: Craft the Trip Planner System Prompt

Your Trip Planner needs a more sophisticated prompt than the Destination Advisor. It should:

```
You are the Trip Planner for Contoso Travel. You create detailed, actionable trip
itineraries by searching for real flights, hotels, and local information.

## Planning Process
1. Gather requirements: destination, dates, travelers, budget, interests
2. Search for flights and present options
3. Search for hotels matching the budget
4. Check weather for the travel dates
5. Use web search for local events, tips, and current requirements
6. Create a day-by-day itinerary
7. Calculate and present the total budget breakdown

## Itinerary Format
Present the final itinerary as:

### ✈️ Trip: [Origin] → [Destination]
**Dates:** [start] to [end] | **Travelers:** [n] | **Budget:** [category]

#### Flights
[Flight details from search results]

#### Accommodation
[Hotel details from search results]

#### Day-by-Day Itinerary
**Day 1 - [Date]: [Theme]**
- Morning: [activity]
- Afternoon: [activity]
- Evening: [activity]
- 🍽️ Food tip: [local restaurant/cuisine suggestion]

[Repeat for each day]

#### 💰 Budget Breakdown
[Budget calculator results in a clean table]

#### ⚠️ Important Notes
[Visa requirements, travel advisories, cultural tips from Bing]
```

---

## Step 3: Wire Everything Together

Update `src/day-2/trip-planner/app.py`:

1. Import all tools from `tools.py`
2. Create the `TripPlanner` agent with all tools registered
3. Include Bing Grounding
4. Set up the HTTP server

---

## Step 4: Test the Complete Flow

Start your agent and test with a full planning request:

```
Plan a 5-day trip from San Francisco to Tokyo for 2 people,
March 10-15, 2026. We love street food, temples, and anime.
Mid-range budget, about $3000 per person.
```

**Verify:**
- [ ] Agent searches for flights
- [ ] Agent searches for hotels
- [ ] Agent checks weather
- [ ] Agent uses Bing for current info (visa, events)
- [ ] Agent calculates budget
- [ ] Output follows the structured itinerary format
- [ ] Agent calls multiple tools before generating the final response

---

## Step 5: Multi-Turn Planning

Test a multi-turn conversation:

1. "I want to plan a trip to Italy"
2. Agent should ask: When? How many people? Budget? Interests?
3. "Next June, just me, mid-range budget, I love history and wine"
4. Agent should start planning
5. "Actually, can you change the hotel to something cheaper?"
6. Agent should adjust while keeping the rest of the plan

---

## Step 6: Add Your Custom Tool (Challenge)

Add one creative tool to your Trip Planner. Ideas:

| Tool | Description |
|------|-------------|
| `get_visa_requirements` | Check visa needs based on passport country + destination |
| `convert_currency` | Real-time currency conversion |
| `get_packing_list` | Generate a packing list based on destination + weather |
| `find_local_phrases` | Essential phrases in the local language |
| `estimate_taxi_fare` | Estimate taxi/ride costs from airport to hotel |

---

## ✅ Checkpoint

Before finishing Day 2, confirm:

- [ ] Trip Planner has 4+ tools (flights, hotels, weather, budget + yours)
- [ ] Bing Grounding provides real-time information
- [ ] Full itinerary generation works end-to-end
- [ ] Multi-turn conversations maintain context
- [ ] Budget breakdown is accurate
- [ ] Your custom tool works and the agent uses it appropriately

**Next:** [Day 3 — Make It Smart →](../day-3/README.md)
