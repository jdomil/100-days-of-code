import requests
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.locations_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        self.search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        self.headers = {
            "apikey": TEQUILA_API_KEY
        }

    def find_city(self, city: str) -> str:
        location_params = {
            "term": city,
            "location_types": "city"
        }
        find_response = requests.get(url=self.locations_endpoint, params=location_params, headers=self.headers)
        find_response.raise_for_status()
        city_data = find_response.json()
        return city_data['locations'][0]['code']

    def find_flight(self, origin_city, destination_city, from_time, to_time ):
        flight_params = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 1,
            "curr": "EUR",
            "max_stopovers": 0
        }
        search_response = requests.get(url=self.search_endpoint, headers=self.headers, params=flight_params)

        try:
            data = search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data

