from bs4 import BeautifulSoup

# Load the HTML content (assuming the file is named weather.html)
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract weather data
weather_data = []
for row in soup.find_all("tr")[1:]:  # Skipping header row
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temp = int(columns[1].text.strip().replace("°C", ""))
    condition = columns[2].text.strip()
    weather_data.append((day, temp, condition))

# Display weather data
print("5-Day Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")

# Find the day with the highest temperature
max_temp_day = max(weather_data, key=lambda x: x[1])
print(f"\nDay with the highest temperature: {max_temp_day[0]} ({max_temp_day[1]}°C)")

# Find days with "Sunny" condition
sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
print("\nDays with Sunny condition:", ", ".join(sunny_days))

# Calculate average temperature
avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
print(f"\nAverage Temperature for the week: {avg_temp:.2f}°C")
