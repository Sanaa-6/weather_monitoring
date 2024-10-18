def process_weather_data(data):
    if data:
        main = data['main']
        weather = data['weather'][0]

        return {
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'condition': weather['main'],
            'timestamp': data['dt']
        }
    return None