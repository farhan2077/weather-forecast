import requests
import os
from dotenv import load_dotenv

os.system('cls')
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("WEATHER FORECAST")
print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")


input_city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={os.getenv('API_KEY')}&q={input_city}&units={'metric'}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    city = data['name']
    weather_description = data['weather'][0]['description']
    temperature = (data["main"]["temp"])

    print(
        f"📰 It is curently {temperature} °C outside and {weather_description} in {city}")
else:
    print("🚨 An error occurred. Check entered city name or try again later.")
