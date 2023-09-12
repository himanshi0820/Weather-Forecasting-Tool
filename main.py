import argparse
import requests
import pyfiglet
from simple_chalk import chalk

API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

weather_icons = {
    #day icons
    "01d": "☀️ ",
    "02d": "⛅ ",
    "03d": "☁️ ",
    "04d": "☁️ ",
    "09d": "🌧️ ",
    "10d": "🌩️ ",
    "11d": "⛈️ ",
    "13d": "❄️ ",
    "50d": "🌨️ ",
    #night icons
    "01n": "🌙 ",
    "02n": "☁️ ",
    "03n": "☁️ ",
    "04n": "☁️ ",
    "09n": "🌧️ ",
    "10n": "🌩️ ",
    "11n": "⛈️ ",
    "13n": "❄️ ",
    "50n": "🌨️ ",
}

# Construct api url with query parameters
parser = argparse.ArgumentParser(description="Check the weather for a country/city")
parser.add_argument("country", help="The country/city to check the weather for")
args = parser.parse_args()
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error : Unable to retrieve weather information"))
    exit()

# parsing the json response from the api and extract the weather information
data = response.json()

# Get information from response
temperature = data["main"]["temp"]
feels_like = data['main']["feels_like"]
min_temp = data["main"]["temp_min"]
max_temp = data["main"]["temp_max"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

#construct the output with weather icons
weather_icon = weather_icons.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Minimun Temperature: {min_temp}°C\n"
output += f"Maximum Temperature: {max_temp}°C\n"
output += f"Feel like: {feels_like}°C\n"

#print the output
print(chalk.green(output))
