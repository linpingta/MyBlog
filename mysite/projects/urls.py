from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='project_index'),
    url('^(?P<project_name>[\w\W]+)/$', views.project, name='project'),
]
