import requests
from datetime import *

USERNAME = "jdomil"
TOKEN = "Lj66PFXhVFV86r2T"


pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Coding minutes",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=graph_endpoint, headers=headers, json=graph_config)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "39"
}

# response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "15"
}

# response = requests.put(url=update_endpoint, headers=headers, json=update_config)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
