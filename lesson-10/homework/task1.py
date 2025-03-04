import requests

API_KEY = "03abef9e375c97088fbbce46d78778fc"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")

else:
    print("Error fetching data. Please check your API key and city name.")

