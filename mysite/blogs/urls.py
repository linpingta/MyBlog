from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^tag/(?P<blog_tag>[\w\W]+)/$', views.blog_tag, name='blog_tag'),
    url(r'^blog/(?P<title>[\w\W]+)/$', views.blog, name='blog'),
]
