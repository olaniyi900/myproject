from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Olaniyi Ajayi',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': 'August 27, 2018'
    },

    {
        'author': 'Sandra Osas',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': 'August 29, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
