import requests

API_KEY = 'your_api_key'  # Replace with your actual API key

def fetch_weather_data(city='Delhi'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()