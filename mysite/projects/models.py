#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lib.models import Author


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    url = models.URLField()
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    SOURCE_CHOICES = (
	('STUDY',u'上学期间项目'),
	('WORK', u'工作相关项目'),
	('LIFE', u'业余时间项目'),
    )
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)

    def __unicode__(self):
	return self.name

    class Meta:
	ordering = [ 'pub_date' ]
