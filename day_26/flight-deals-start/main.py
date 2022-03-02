#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "AGP"

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city['iataCode'] = flight_search.find_city(city['city'])

    data_manager.update_sheet()

tomorrow = datetime.today() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight_details = flight_search.find_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    try:
        flight_price = flight_details.price
    except AttributeError:
        flight_price = float('inf')

    if destination["lowestPrice"] >= flight_price:
        notification_manager.send_sms(flight_details)

