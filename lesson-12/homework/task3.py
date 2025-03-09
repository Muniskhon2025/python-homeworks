import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "https://www.demoblaze.com/"
LAPTOPS_URL = "https://www.demoblaze.com/#"

def get_laptop_data():
    laptops = []
    page = 1
    
    while True:
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='card-block')
        
        if not items:
            break
        
        for item in items:
            name = item.find('h4', class_='card-title').text.strip()
            price = item.find('h5').text.strip()
            description = item.find('p', class_='card-text').text.strip()
            
            laptops.append({
                "name": name,
                "price": price,
                "description": description
            })
        
        next_button = soup.find('button', id='next2')
        if not next_button:
            break
        page += 1
    
    return laptops

# Scrape data
laptop_data = get_laptop_data()

# Save data to JSON file
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptop_data, f, indent=4)

print("Laptop data saved to laptops.json")
