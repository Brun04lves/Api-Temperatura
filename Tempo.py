import requests
from pprint import pprint

API_Key = ''

city = input("Digite a cidade: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"

weather_data = requests.get(base_url).json()

pprint(weather_data)