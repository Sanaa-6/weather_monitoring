import unittest
from weather_api import fetch_weather_data

class TestWeatherAPI(unittest.TestCase):
    def test_fetch_weather_data(self):
        data = fetch_weather_data('Delhi')
        self.assertIn('main', data)

if __name__ == '_main_':
    unittest.main()