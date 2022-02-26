import requests
from datetime import *
import os

# API Keys to move to environment
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
BEARER_TOKEN = os.environ['BEARER_TOKEN']
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# My constants
GENDER = "male"
WEIGHT = 60
HEIGHT = 172
AGE = 28

# User input
exercise = input("What exercise did you do today?: ")

# Natural config
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_config = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

# Natural request
sheet_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_config, headers=headers)
result = sheet_response.json()
exercises = result["exercises"]

# Today's date
today = datetime.now()

# Sheety post
sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
for exercise in exercises:
    sheety_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_headers)
    print(sheet_response.text)
