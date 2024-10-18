import matplotlib.pyplot as plt

def plot_weather_data(daily_data):
    # Example function to plot temperature data
    days = list(daily_data.keys())
    temps = [data['temp'] for data in daily_data.values()]

    plt.plot(days, temps)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature Overview')
    plt.show()