import requests

negara1 = str(input('Kode Negara Yang Mau Menukar: '))
negara2 = str(input('Kode Negara Yang Ditukarkan: '))
jumlah = float(input('Jumlah Uang Yang Ditukarkan: '))

key = '64e226ee33ac6ebdfba50575943e071754650daf'

parameters = {"api_key": {key}, "from": {negara1}, "to": {negara2}, "amount": {jumlah}, "format": "json"}

url = "https://api.getgeoapi.com/v2/currency/convert"

response = requests.get(url, parameters)



print(response.json())