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

ORIGIN_CITY_IATA = "LON"

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

    if flight_details is None:
        continue

    if destination["lowestPrice"] >= flight_price:
        message = f"Low price alert! Only €{flight_details.price} to fly from " \
                  f"{flight_details.origin_city}-{flight_details.origin_airport} " \
                  f"to {flight_details.destination_city}-{flight_details.destination_airport} " \
                  f"from {flight_details.out_date} to {flight_details.return_date}."
        if flight_details.max_stopovers > 0:
            message += f"\nFlight has {flight_details.max_stopovers} stop over, via {flight_details.via_city}."

        notification_manager.send_sms(message)

