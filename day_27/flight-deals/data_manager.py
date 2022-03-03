import requests
import os

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self) -> list:
        get_response = requests.get(url=SHEETY_ENDPOINT)
        get_response.raise_for_status()
        content = get_response.json()
        self.destination_data = content["prices"]
        return self.destination_data

    def update_sheet(self):
        for city in self.destination_data:
            update_url = f"{SHEETY_ENDPOINT}/{city['id']}"
            update_config = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_response = requests.put(url=update_url, json=update_config)
            print(update_response.text)

