import requests

key = '64e226ee33ac6ebdfba50575943e071754650daf'

parameters = {"api_key": {key}, "from": "EUR", "to": "IDR", "amount": 1, "format": "json"}

url = "https://api.getgeoapi.com/v2/currency/convert"

response = requests.get(url, parameters)

print(response.json())