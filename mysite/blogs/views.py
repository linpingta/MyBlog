#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext

from elasticsearch import Elasticsearch

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

def test(request):
    return render_to_response('blogs/form.html', context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST':
	search_word = request.POST['search_word']
	es = Elasticsearch()
	res = es.search(index="linpingta-blog", body={
		"query": {	
			"match":{
				"title": search_word
			}
		}
	})
	blogs = []
	print "Got %d Hits" % res["hits"]["total"]
	for hit in res['hits']['hits']:
		title = hit['_source']['title']
		blog = Blog.objects.get(title=title)
		blogs.append(blog)
    	context = { 'blogs': blogs }
    	return render_to_response('blogs/search_result.html', context=context)
    else:
	return HttpResponseRedirect('/blogs/')
