#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Project

# Create your views here.
def index(request):
    work_projects = Project.objects.filter(source='WORK').order_by('-pub_date')
    life_projects = Project.objects.filter(source='LIFE').order_by('-pub_date')
    study_projects = Project.objects.filter(source='STUDY').order_by('-pub_date')
    context = {
	'work_projects': work_projects,
	'life_projects': life_projects, 
	'study_projects': study_projects
    }
    return render(request, 'projects/index.html', context=context) 

def project(request, project_name):
    project = get_object_or_404(Project, name=project_name)
    return render(request, 'projects/project.html', {'project':project})
