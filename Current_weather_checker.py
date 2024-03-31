import requests
import pprint

API_KEY = "b85d27fc432c0776abd1d268b1320839"
city = input('Enter the name of the city(example: Tashkent or tashkent): ')
exclude = input("Enter an option(current, hourly, daily): ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&exclude={exclude}&appid={API_KEY}").json()

pprint.pprint(response, width=100)

Temp = response['main']['temp']