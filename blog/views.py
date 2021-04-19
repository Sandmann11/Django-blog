from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import requests


# Create your views here.
def main(request):
    return render(request, 'blog/main.html', {})    

def admin(request):
    return render(request, 'blog/admin.html', {})

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'

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


def portfolio(request):
    return render(request, 'blog/portfolio.html', {})


def crypto(request):
    json_data = requests.get('https://api.binance.com/api/v3/ticker/price').json()
    
    btc_price = round(float(json_data[11]['price']), 2)
    eth_price  = round(float(json_data[12]['price']), 2)
    xmr_price = round(float(json_data[480]['price']), 2)

    return render(request, 'blog/crypto.html', {
        'btc_price':btc_price,
        'eth_price':eth_price,
        'xmr_price':xmr_price
        })