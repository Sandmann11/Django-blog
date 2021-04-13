from django.shortcuts import render, get_object_or_404
from .models import Post

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

# def homepage(request):
#     return render(request, 'blog/main.html', {})

def admin(request):
    return render(request, 'blog/admin.html', {})