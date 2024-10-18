from weather_api import fetch_weather_data
from processing import process_weather_data
from alerts import check_alerts
from visualization import visualize_weather

def main():
    # Fetch weather data
    data = fetch_weather_data()
    # Process the data
    processed_data = process_weather_data(data)
    # Check for alerts
    check_alerts(processed_data)
    # Visualize data
    visualize_weather(processed_data)

if __name__ == "_main_":
    main()