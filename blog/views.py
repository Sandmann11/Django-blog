from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import requests
import pandas as pd



# Create your views here.
def main(request):
    return render(request, 'blog/main.html', {})    

def admin(request):
    return render(request, 'blog/admin.html', {})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

def crypto(request):
    json_data = requests.get('https://api.binance.com/api/v3/ticker/price').json()

    coin_list = []
    for coin in json_data:
        coin_list.append(coin)

    df = pd.DataFrame(coin_list)

    btc_price = round(float(json_data[11]['price']), 2)
    eth_price  = round(float(json_data[12]['price']), 2)
    xmr_price = round(float(json_data[480]['price']), 2)

    return render(request, 'blog/crypto.html', {
        'btc_price':btc_price,
        'eth_price':eth_price,
        'xmr_price':xmr_price,
        'coin_list':coin_list,
        'df':df
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