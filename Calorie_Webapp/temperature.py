import requests
from selectorlib import Extractor


class Temperature:
    """
    Represents temperature extract from timeanddate.com/weather webpage.
    """
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def scrape(self):
        request = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
        content = request.text
        extractor = Extractor.from_yaml_file("./temperature.yaml")
        raw_content = extractor.extract(content)
        return raw_content

    def get(self):
        """ Cleans out the scraped content"""
        scraped_content = self.scrape()
        return scraped_content['temp'].replace("\xa0°C", "")
