import requests
import time

r = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT')

# base_url = 'https://api.binance.com/api/v3/'
# btc_ticker = 'avgPrice?symbol=BTCUSDT'
# eth_ticker = 'avgPrice?symbol=ETHUSDT'
# xmr_ticker = 'avgPrice?symbol=XMRUSDT'

api_data = r.json()

def btc_rate():
    btc_price = api_data['price']
    return round(float(btc_price), 2)

print(f'Status Code: {r.status_code}')
print(btc_rate())

