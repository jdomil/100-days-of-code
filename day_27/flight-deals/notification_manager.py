from twilio.rest import Client
import os

ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]

class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+19032963763",
            to="PHONE_NUMBER"
        )
        print(message.sid)
