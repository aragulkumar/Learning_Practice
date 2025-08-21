
import requests
import json

api_key = "38dd5e26531ace1b2e22f8847b713403"
location = input("enter city/district name :")
url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"

response = requests.get(url)
data = response.json()

temperature = data['current']['temperature']
humidity = data['current']['humidity']
wind_speed = data['current']['wind_speed']
wind_direction = data['current']['wind_dir']

print(f"Live weather in {location}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} mph")
print(f"Wind Direction: {wind_direction}")