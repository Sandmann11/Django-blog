from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/main.html', {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def welcome(request):
    return render(request, 'blog/welcome.html', {})