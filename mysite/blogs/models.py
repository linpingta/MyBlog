#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lib.models import Author


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField()

    def __unicode__(self):
	return self.name

    class Meta:
	ordering = [ 'name' ]


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __unicode__(self):
	return self.title 

    class Meta:
	ordering = [ '-pub_date' ]
   
