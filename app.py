import requests
from twilio.rest import Client

# API Get
# url = "Enter url here"
# api_key = "Enter api key here"
# headers = {
#     "Authorization": "Bearer " + api_key
# }
# params = {
#     "location": "NYC"
# }
# response = requests.get(url, headers=headers, params=params)
# businesses = response.json()["businesses"]
# names = [business["name"] for business in businesses if business["rating"] > 4.5 ]
# print(names)

# Twilio phone number
# account_sid = "Enter your security id here"
# auth_token = "Enter Authentication token here"
#
# client = Client(account_sid, auth_token)
#
# call = client.messages.create(
#     to="...",
#     from_="...",
#     body="This is our first message"
# )