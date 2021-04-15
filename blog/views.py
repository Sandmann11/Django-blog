from django.shortcuts import render, get_object_or_404
from .models import Post
import requests

# Create your views here.
def main(request):
    return render(request, 'blog/main.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_text(request, pk):
    postText = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_text.html', {'postText':postText})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

def admin(request):
    return render(request, 'blog/admin.html', {})

def crypto(request):
    json_data = requests.get('https://api.binance.com/api/v3/ticker/price').json()
    
    btc_symbol = json_data[11]['symbol'][:3]
    btc_price = round(float(json_data[11]['price']), 2)
    eth_symbol = json_data[12]['symbol'][:3]
    eth_price  = round(float(json_data[12]['price']), 2)
    xmr_symbol = json_data[480]['symbol'][:3]
    xmr_price = round(float(json_data[480]['price']), 2)

    return render(request, 'blog/crypto.html', {
        'btc_symbol':btc_symbol, 
        'btc_price':btc_price,
        'eth_symbol':eth_symbol,
        'eth_price':eth_price,
        'xmr_symbol':xmr_symbol,
        'xmr_price':xmr_price
        })