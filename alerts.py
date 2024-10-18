def check_temperature_alert(current_temp, threshold):
    if current_temp > threshold:
        print(f"Alert! Temperature exceeded {threshold}°C: Current Temp: {current_temp}°C")