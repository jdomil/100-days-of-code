from twilio.rest import Client
import os

ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]

class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, flight_details):
        message = self.client.messages.create(
            body=f"Low price alert! Only €{flight_details.price} to fly from "
                 f"{flight_details.origin_city}-{flight_details.origin_airport} "
                 f"to {flight_details.destination_city}-{flight_details.destination_airport} "
                 f"from {flight_details.out_date} to {flight_details.return_date}.",
            from_="+19032963763",
            to="PHONE_NUMBER"
        )
        print(message.sid)