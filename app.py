import requests


url = "Enter url here"
api_key = "Enter api key here"
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "location": "NYC"
}
response = requests.get(url, headers=headers, params)
businesses = response.json()["businesses"]
names = [business["name"] for business in businesses if business["rating"] > 4.5 ]
print(names)