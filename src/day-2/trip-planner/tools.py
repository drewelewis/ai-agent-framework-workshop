# Contoso Travel — Trip Planner Tools
# Day 2: Build tools that your agent can call

from datetime import datetime


# =============================================================================
# TODO 1: Implement search_flights
# =============================================================================
# Search for available flights between two cities.
#
# Parameters:
#   origin (str): Departure city or airport code
#   destination (str): Arrival city or airport code
#   date (str): Travel date in YYYY-MM-DD format
#
# Returns:
#   dict with "flights" list, each containing:
#     airline, flight_number, departure, arrival, price_usd, class
#
# Requirements:
#   - Validate date format (YYYY-MM-DD)
#   - Reject past dates
#   - Return 2-3 simulated flight options with varied prices/times
# =============================================================================
def search_flights(origin: str, destination: str, date: str) -> dict:
    """Search for available flights between two cities on a specific date."""
    # TODO: Implement this tool
    pass


# =============================================================================
# TODO 2: Implement search_hotels
# =============================================================================
# Search for hotels at a destination.
#
# Parameters:
#   destination (str): City name
#   check_in (str): Check-in date YYYY-MM-DD
#   check_out (str): Check-out date YYYY-MM-DD
#   budget (str): One of "budget", "mid-range", "luxury"
#
# Returns:
#   dict with "hotels" list, each containing:
#     name, rating (1-5), price_per_night_usd, neighborhood, amenities[]
#
# Requirements:
#   - Filter results by budget level
#   - Return 2-3 options per budget level
#   - Include neighborhood info (helps with itinerary planning)
# =============================================================================
def search_hotels(destination: str, check_in: str, check_out: str, budget: str = "mid-range") -> dict:
    """Search for hotels at a destination within a budget range."""
    # TODO: Implement this tool
    pass


# =============================================================================
# TODO 3: Implement get_weather
# =============================================================================
# Get weather forecast for a destination.
#
# Parameters:
#   city (str): City name
#   start_date (str): Start date YYYY-MM-DD
#   end_date (str): End date YYYY-MM-DD
#
# Returns:
#   dict with "forecast" list, each containing:
#     date, high_celsius, low_celsius, condition, humidity_pct
#
# Requirements:
#   - Return one entry per day in the date range
#   - Use realistic weather data for the destination/season
# =============================================================================
def get_weather(city: str, start_date: str, end_date: str) -> dict:
    """Get weather forecast for a city over a date range."""
    # TODO: Implement this tool
    pass


# =============================================================================
# TODO 4: Implement calculate_budget
# =============================================================================
# Calculate total trip budget with breakdown.
#
# Parameters:
#   flight_cost (float): Cost per person for flights
#   hotel_cost_per_night (float): Cost per night for hotel
#   num_nights (int): Number of nights
#   num_travelers (int): Number of travelers
#   daily_food_budget (float): Daily food budget per person (default 50)
#   daily_activities_budget (float): Daily activity budget per person (default 40)
#
# Returns:
#   dict with:
#     flights_total, hotel_total, food_total, activities_total,
#     grand_total, per_person_total
# =============================================================================
def calculate_budget(
    flight_cost: float,
    hotel_cost_per_night: float,
    num_nights: int,
    num_travelers: int,
    daily_food_budget: float = 50.0,
    daily_activities_budget: float = 40.0,
) -> dict:
    """Calculate total trip budget with detailed breakdown."""
    # TODO: Implement this tool
    pass
