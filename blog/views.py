from django.shortcuts import render
from .models import  Blog


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html',{'blogs':blogs})



