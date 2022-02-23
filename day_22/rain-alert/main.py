import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC188204ec1465c13b35a213a92cbc73a2"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 36.721275,
    "lon": -4.421399,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
hourly_weather = data["hourly"]

will_rain = False

for hour_weather in hourly_weather[:12]:
    weather_code = hour_weather["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+19032963763",
        to=os.environ.get("PHONE_NUMBER")
    )
    print(message.status)