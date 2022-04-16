import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents temperature extract from timeanddate.com/weather webpage.
    """
    def __init__(self, country, city):
        self.country = country.lower()
        self.city = city.lower()

    def get(self):
        request = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
        content = request.text
        extractor = Extractor.from_yaml_file("temperature.yaml")
        return float(extractor.extract(content)['temp'].replace('\xa0°C', ""))
