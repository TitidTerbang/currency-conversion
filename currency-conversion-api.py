import requests
import json
from addict import Dict


negara1 = str(input('Kode Negara Yang Mau Menukar: '))
negara2 = str(input('Kode Negara Yang Ditukarkan: '))
jumlah = int(input('Jumlah Uang Yang Ditukarkan: '))

key = '64e226ee33ac6ebdfba50575943e071754650daf'

parameters = {"api_key": {key}, "from": {negara1}, "to": {negara2}, "amount": {jumlah}, "format": "json"}

url = "https://api.getgeoapi.com/v2/currency/convert"

response = requests.get(url, parameters)
data = response.json()
dict = Dict(data)

# print(data)
# print(data['rates']['SGD']['rate']) <-- contoh cara mengambil data
print('Dari', data.get('amount'), data.get('base_currency_code'), 'Anda Mendapatkan', data['rates']['SGD']['rate_for_amount'], data['rates']['SGD']['currency_name'])