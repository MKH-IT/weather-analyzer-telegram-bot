from geopy.geocoders import Nominatim


def get_city_name_by_location(latitude: float, longitude: float) -> str:
    """
    Function to get the city name by latitude and longitude.
    """
    geolocator = Nominatim(user_agent="BOT")
    location = geolocator.reverse((latitude, longitude), language='en')
    address = location.raw.get('address', {})
    city_name = address.get('city') or address.get('town') or address.get('village') or address.get('county') or 'Unknown'
    return city_name


def get_weather_by_city_name(city_name: str) -> dict:
    """
    Function to get the weather information by city name.
    """
    ...


def recommend_based_of_weather(weather_info: dict) -> str:
    """
    Function to prepare the weather recommendation.
    """
    ...
