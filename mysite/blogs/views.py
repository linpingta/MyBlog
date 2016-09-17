#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from models import Blog, Tag

# Create your views here.
def index(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    tags = Tag.objects.all().order_by('name')
    context = { 'blogs': blogs, 'tags' : tags }
    return render(request, 'blogs/index.html', context=context)

def blog_tag(request, blog_tag):
    blogs_with_tag = Blog.objects.filter(tags__name=blog_tag).order_by('-pub_date')
    tags = Tag.objects.all().order_by('name')
    context = { 'blogs': blogs_with_tag, 'tags' : tags }
    return render(request, 'blogs/index.html', context=context)
    
def blog(request, title):
    blog = get_object_or_404(Blog, title=title)
    return render(request, 'blogs/blog.html', {'blog':blog})
