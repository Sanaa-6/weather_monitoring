def process_weather_data(data):
    # Extract relevant information from the API response
    temperature = data['main']['temp']
    condition = data['weather'][0]['description']
    return {
        'temperature': temperature,
        'condition': condition
    }