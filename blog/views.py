from django.shortcuts import render, get_object_or_404
from .models import  Blog


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html',{'blogs':blogs})

def details(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html',{'blog':blog})



