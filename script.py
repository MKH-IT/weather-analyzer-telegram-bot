import requests
from decouple import config

API_KEY = config("WEATHER_API_TOKEN")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=samarkand&appid={API_KEY}&units=metric")
print(response.json())
print(type(response.json()))

class WeatherRecomendationEngine:
    def __init__(self, temperature, condition):
        self.temperature == temperature
        self.condition == condition

    def recomend_activity(self):
        if self.condition.lower == 'sunny':
            if self.temperature > 25:
                return "Go for a swiming!"
            elif 15 <= self.temperature <=25:
                return "Have a picnic in the park."
            else:
                return "You can go for a walk. It`s nice weather today!"
        elif self.condition.lower == 'rainy':
            if self.temperature > 15:
                return "It`s rainy. Don`t forget to bring umbrella with you!"
            else:
                return "Watch a movie and enjoy a cozy day at home."
        elif self.condition.lower == 'snowy':
            if self.temperature > 0:
                return "Build a snowman or have a snowball fight!"
            else:
                return "Stay warm indoors and enjoy a hot drink."
        else:
            return "Stay at home. It`s too cold outdor!"
        
    def recomendation_clothing(self):
        if self.temperature > 25:
            return "Wear light and breathable clothes like shorts and t-shirts."
        elif 15 <= self.temperature <= 25:
            return "Wear comfortable clothes like jeans and a light jacket."
        elif 5 <= self.temperature <= 15:
            return "Wear warm clothes like sweaters and coats."
        elif self.temperature < 5:
            return "Bundle up with heavy winter clothing like coats, scarves, and gloves."
        else:
            return "No specific recommendations for this temperature."


        