import requests
import os
from dotenv import load_dotenv

os.system('cls')
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("WEATHER STATUS")
print("⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅")


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={os.getenv('API_KEY')}&q={city}&units={'metric'}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    name = data['name']
    weather = data['weather'][0]['description']
    temperature = (data["main"]["temp"])

    print(
        f"It's {temperature} °C outside and the weather is {weather} in {name}")
else:
    print("🚨 An error occurred. Check entered city name or try again later.")
