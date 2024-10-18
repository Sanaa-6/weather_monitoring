def check_alerts(data):
    temperature = data['temperature']
    if temperature > 35:
        print("Alert: High temperature!")