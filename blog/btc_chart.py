import requests
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

market = 'BTCUSDT'
tick_interval = '1d'

url = 'https://api.binance.com/api/v3/klines?symbol='+market+'&interval='+tick_interval
data = requests.get(url).json()

df = pd.DataFrame(data)
df = df.drop(columns=[7, 8, 9, 10, 11])
df.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time']

df['open_time'] = [dt.datetime.fromtimestamp(i / 1000.0) for i in df['open_time']]
df['close_time'] = [dt.datetime.fromtimestamp(i / 1000.0) for i in df['close_time']]

# df.index = [dt.datetime.fromtimestamp(i / 1000.0) for i in df['close_time']]
df.index = df['close_time']
df.index.name = 'date'


fig = go.Figure(data=[go.Candlestick(
                x=df.index, 
                open=df.open,
                high=df.high,
                low=df.low,
                close=df.close)])

fig.update_layout(
    title='BTC/USD Price Chart'
)

chart = fig.to_html(full_html=False, default_height=500, default_width=700)

# fig.show()

print(type(chart))