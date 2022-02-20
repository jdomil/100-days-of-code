import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 36.721275  # Your latitude
MY_LONG = -4.421399  # Your longitude
MY_EMAIL = "smtp.python.100@gmail.com"
MY_PASSWORD = "AbCd_1234"


def iss_above():
    """Returns true if your position is within +5 or -5 degrees of the ISS position."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
    """Returns true if it is nigh time."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    utc_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    utc_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = utc_sunrise + 1
    sunset = utc_sunset + 1
    hour_now = int(datetime.now().hour)

    return sunset <= hour_now <= sunrise


while True:
    time.sleep(60)
    if iss_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nLook up, the ISS is right above you!"
            )
