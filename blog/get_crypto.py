import requests
import time
import pandas as pd


json_data = requests.get('https://api.binance.com/api/v3/ticker/price').json()

df = pd.DataFrame(json_data)

print(df.info())