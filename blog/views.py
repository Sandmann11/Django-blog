from django.shortcuts import render
from .models import Post

# Create your views here.
def main(request):
    return render(request, 'blog/main.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {})

# def homepage(request):
#     return render(request, 'blog/main.html', {})

def admin(request):
    return render(request, 'blog/admin.html', {})