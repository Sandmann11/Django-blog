from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import requests
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
from binance.client import Client
from . import bin_api


def main(request):
    return render(request, 'blog/main.html', {})


def admin(request):
    return render(request, 'blog/admin.html', {})


def portfolio(request):
    return render(request, 'blog/portfolio.html', {})


def crypto(request):
    json_data = requests.get(
        'https://api.binance.com/api/v3/ticker/price').json()
    # df = pd.DataFrame(json_data)

    btc_price = round(float(json_data[11]['price']), 2)
    eth_price = round(float(json_data[12]['price']), 2)
    xmr_price = round(float(json_data[480]['price']), 2)

    return render(request, 'blog/crypto.html', {
        'btc_price': btc_price,
        'eth_price': eth_price,
        'xmr_price': xmr_price,
        # 'df':df
    })


def crypto_trades(request):
    trades_df = bin_api.latest_trades()
    html_df = trades_df.to_html()

    return render(request, 'blog/crypto_trades.html', {
        'trades_df': trades_df,
        'html_df': html_df,
    })


def crypto_all(request):
    json_data = requests.get(
        'https://api.binance.com/api/v3/ticker/price').json()

    btc_list = []
    eth_list = []
    bnb_list = []
    eur_list = []
    usdt_list = []

    for coin in json_data:
        if coin['symbol'].endswith('BTC'):
            coin['symbol'] = coin['symbol'][slice(3)]
            btc_list.append(coin)

        elif coin['symbol'].endswith('ETH'):
            coin['symbol'] = coin['symbol'][slice(3)]
            eth_list.append(coin)

        elif coin['symbol'].endswith('BNB'):
            coin['symbol'] = coin['symbol'][slice(3)]
            bnb_list.append(coin)

        elif coin['symbol'].endswith('EUR'):
            coin['symbol'] = coin['symbol'][slice(3)]
            coin['price'] = round(float(coin['price']), 2)
            eur_list.append(coin)

        elif coin['symbol'].endswith('USDT'):
            coin['symbol'] = coin['symbol'][slice(-4)]
            coin['price'] = round(float(coin['price']), 2)
            usdt_list.append(coin)

    return render(request, 'blog/crypto_all.html', {
        'btc_list': btc_list,
        'eth_list': eth_list,
        'bnb_list': bnb_list,
        'eur_list': eur_list,
        'usdt_list': usdt_list,
    })


def btc_chart(request):
    market = 'BTCUSDT'
    tick_interval = '1d'

    url = 'https://api.binance.com/api/v3/klines?symbol=' + \
        market+'&interval='+tick_interval
    data = requests.get(url).json()

    df = pd.DataFrame(data)
    df = df.drop(columns=[7, 8, 9, 10, 11])
    df.columns = ['open_time', 'open', 'high',
                  'low', 'close', 'volume', 'close_time']

    df['open_time'] = [dt.datetime.fromtimestamp(i / 1000.0) for i in df['open_time']]
    df['close_time'] = [dt.datetime.fromtimestamp(i / 1000.0) for i in df['close_time']]

    df.index = df['close_time']
    df.index.name = 'date'

    fig = go.Figure(data=[go.Candlestick(
                    x=df.index,
                    open=df.open,
                    high=df.high,
                    low=df.low,
                    close=df.close)])

    fig.update_layout(
        title='BTC Historic Price Chart'
    )

    chart = fig.to_html(full_html=False, default_height=800,
                        default_width='100%')

    return render(request, 'blog/btc_chart.html', {
        'chart': chart
    })


class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['-created_date']


class PostText(DetailView):
    model = Post
    # context_object_name = 'post'
    template_name = 'blog/post_text.html'


class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_add.html'
    # fields = '__all__'


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    # fields = ['title', 'title_tag', 'lead', 'text']


class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')


class CategoryAdd(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blog/category_add.html'
    fields = '__all__'
