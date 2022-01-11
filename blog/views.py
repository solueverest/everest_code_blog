from django.shortcuts import render
from .models import Blog


def home(request):
    blog1 = Blog.objects.all()
    return render(request, 'blog/home.html', {'blog1': blog1})


def blogs(request):
    blog1 = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blog1': blog1})


def about(request):
    return render(request, 'blog/about.html')
