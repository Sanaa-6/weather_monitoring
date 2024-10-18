from weather_api import fetch_weather_data
from processing import process_weather_data
from alerts import check_temperature_alert

def main():
    city = 'Delhi'  # Change to your desired city
    weather_data = fetch_weather_data(city)
    processed_data = process_weather_data(weather_data)

    if processed_data:
        print(f"Current temperature in {city}: {processed_data['temp']}°C")
        check_temperature_alert(processed_data['temp'], 35)  # Set threshold as needed

if __name__ == '_main_':
    main()