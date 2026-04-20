# Contoso Travel — Trip Planner Tools (SOLUTION)
# Day 2: Complete tool implementations

from datetime import datetime, timedelta
import random


def search_flights(origin: str, destination: str, date: str) -> dict:
    """Search for available flights between two cities on a specific date.

    Args:
        origin: Departure city or airport code (e.g., 'New York' or 'JFK')
        destination: Arrival city or airport code (e.g., 'Tokyo' or 'NRT')
        date: Travel date in YYYY-MM-DD format
    """
    # Validate date format
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD."}

    # Reject past dates
    if parsed_date.date() < datetime.now().date():
        return {"error": "Cannot search for flights in the past."}

    return {
        "flights": [
            {
                "airline": "Contoso Air",
                "flight_number": f"CA-{random.randint(100, 999)}",
                "departure": f"{date}T08:00:00",
                "arrival": f"{date}T14:30:00",
                "duration_hours": 6.5,
                "price_usd": random.randint(350, 550),
                "class": "Economy",
            },
            {
                "airline": "Azure Airlines",
                "flight_number": f"AZ-{random.randint(10, 99)}",
                "departure": f"{date}T10:15:00",
                "arrival": f"{date}T16:45:00",
                "duration_hours": 6.5,
                "price_usd": random.randint(400, 650),
                "class": "Economy",
            },
            {
                "airline": "Contoso Air",
                "flight_number": f"CA-{random.randint(100, 999)}",
                "departure": f"{date}T22:00:00",
                "arrival": f"{date}T04:30:00",
                "duration_hours": 6.5,
                "price_usd": random.randint(700, 1200),
                "class": "Business",
            },
        ],
        "origin": origin,
        "destination": destination,
        "date": date,
    }


def search_hotels(
    destination: str, check_in: str, check_out: str, budget: str = "mid-range"
) -> dict:
    """Search for hotels at a destination within a budget range.

    Args:
        destination: City name (e.g., 'Tokyo')
        check_in: Check-in date in YYYY-MM-DD format
        check_out: Check-out date in YYYY-MM-DD format
        budget: Budget level - 'budget', 'mid-range', or 'luxury'
    """
    price_ranges = {
        "budget": (40, 80),
        "mid-range": (100, 200),
        "luxury": (250, 600),
    }

    budget_key = budget.lower()
    if budget_key not in price_ranges:
        return {"error": f"Invalid budget level '{budget}'. Use: budget, mid-range, or luxury."}

    price_range = price_ranges[budget_key]

    hotels = [
        {
            "name": f"The {destination} Inn",
            "rating": round(random.uniform(3.5, 4.2), 1),
            "price_per_night_usd": random.randint(*price_range),
            "neighborhood": "City Center",
            "amenities": ["WiFi", "Breakfast", "Airport Shuttle"],
        },
        {
            "name": f"{destination} Grand Hotel",
            "rating": round(random.uniform(4.0, 4.8), 1),
            "price_per_night_usd": random.randint(*price_range),
            "neighborhood": "Historic District",
            "amenities": ["WiFi", "Pool", "Restaurant", "Gym"],
        },
        {
            "name": f"Sakura Suites {destination}",
            "rating": round(random.uniform(3.8, 4.5), 1),
            "price_per_night_usd": random.randint(*price_range),
            "neighborhood": "Entertainment District",
            "amenities": ["WiFi", "Kitchen", "Laundry"],
        },
    ]

    return {
        "hotels": hotels,
        "destination": destination,
        "check_in": check_in,
        "check_out": check_out,
        "budget_level": budget,
    }


def get_weather(city: str, start_date: str, end_date: str) -> dict:
    """Get weather forecast for a city over a date range.

    Args:
        city: City name (e.g., 'Barcelona')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    if end < start:
        return {"error": "End date must be after start date."}

    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Light Rain", "Clear"]
    forecast = []
    current = start

    while current <= end:
        forecast.append(
            {
                "date": current.strftime("%Y-%m-%d"),
                "high_celsius": random.randint(18, 32),
                "low_celsius": random.randint(10, 22),
                "condition": random.choice(conditions),
                "humidity_pct": random.randint(40, 80),
            }
        )
        current += timedelta(days=1)

    return {"city": city, "forecast": forecast}


def calculate_budget(
    flight_cost: float,
    hotel_cost_per_night: float,
    num_nights: int,
    num_travelers: int,
    daily_food_budget: float = 50.0,
    daily_activities_budget: float = 40.0,
) -> dict:
    """Calculate total trip budget with detailed breakdown.

    Args:
        flight_cost: Round-trip flight cost per person in USD
        hotel_cost_per_night: Hotel cost per night in USD (total, not per person)
        num_nights: Number of nights staying
        num_travelers: Number of travelers
        daily_food_budget: Daily food budget per person in USD (default: 50)
        daily_activities_budget: Daily activities budget per person in USD (default: 40)
    """
    flights_total = flight_cost * num_travelers
    hotel_total = hotel_cost_per_night * num_nights
    food_total = daily_food_budget * num_nights * num_travelers
    activities_total = daily_activities_budget * num_nights * num_travelers
    grand_total = flights_total + hotel_total + food_total + activities_total

    return {
        "breakdown": {
            "flights_total": round(flights_total, 2),
            "hotel_total": round(hotel_total, 2),
            "food_total": round(food_total, 2),
            "activities_total": round(activities_total, 2),
        },
        "grand_total": round(grand_total, 2),
        "per_person_total": round(grand_total / max(num_travelers, 1), 2),
        "num_travelers": num_travelers,
        "num_nights": num_nights,
    }
