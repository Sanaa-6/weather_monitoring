import requests

API_KEY = 'your_api_key'  # Replace 'your_api_key' with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None