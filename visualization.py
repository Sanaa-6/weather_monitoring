import matplotlib.pyplot as plt

def visualize_weather(data):
    # Create a simple plot for temperature
    plt.bar(['Temperature'], [data['temperature']])
    plt.title('Current Temperature')
    plt.ylabel('Temperature (°C)')
    plt.show()