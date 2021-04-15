import requests
import time

r = requests.get('https://api.binance.com/api/v3/ticker/price')

# base_url = 'https://api.binance.com/api/v3/'
# btc_ticker = 'avgPrice?symbol=BTCUSDT'
# eth_ticker = 'avgPrice?symbol=ETHUSDT'
# xmr_ticker = 'avgPrice?symbol=XMRUSDT'

json_data = r.json()

# def btc_rate():
#     btc_price = json_data['price']
#     return round(float(btc_price), 2)

# print(f'Status Code: {r.status_code}')
# print(btc_rate())

# print(json_data)