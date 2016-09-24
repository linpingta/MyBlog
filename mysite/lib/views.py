from django.shortcuts import render

from projects.models import Project
from blogs.models import Blog

# Create your views here.
def index(request):
    recent_blogs = Blog.objects.all().order_by('-pub_date')[0:5]
    recent_projects = Project.objects.all().order_by('-pub_date')[0:2]
    context = {
	'recent_blogs': recent_blogs,
	'recent_projects': recent_projects
    }
    return render(request, 'lib/index.html', context=context)
