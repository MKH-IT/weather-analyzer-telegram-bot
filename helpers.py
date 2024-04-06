import requests
from decouple import config
from geopy.geocoders import Nominatim


TELEGRAM_API_TOKEN = config("WEATHER_API_TOKEN")


def get_city_name_by_location(latitude: float, longitude: float) -> str:
    """
    Function to get the city name by latitude and longitude.
    """
    geolocator = Nominatim(user_agent="BOT")
    location = geolocator.reverse((latitude, longitude), language="en")
    address = location.raw.get("address", {})
    city_name = (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or address.get("county")
        or "Unknown"
    )
    return city_name


def get_weather_by_city_name(city_name: str) -> dict:
    """
    Function to get the weather information by city name.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": TELEGRAM_API_TOKEN,
        "units": "metric",
    }
    response = requests.get(url, params=params)
    response_payload = response.json()
    result = {
        "temperature": response_payload["main"]["temp"],
        "feels_like": response_payload["main"]["feels_like"],
        "temp_max": response_payload["main"]["temp_max"],
        "temp_min": response_payload["main"]["temp_min"],
    }

    return result


def recommend_based_of_weather(weather_info: dict) -> str:
    """
    Function to prepare the weather recommendation.
    """
    ...
