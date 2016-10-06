#-*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :

''' build blog index for search'''

__author__ = 'linpingta@163.com' 

import os,sys
os.environ.setdefault(
	"DJANGO_SETTINGS_MODULE", "mysite.settings"
)
import subprocess
import time
import re
import logging

import django
django.setup()

from elasticsearch import Elasticsearch
from elasticsearch import helpers

from lib.models import Author
from blogs.models import Blog, Tag


if __name__ == '__main__':

	es = Elasticsearch()

	# create index
	if False:
		blogs = Blog.objects.all()	
		actions = []
		count = 0
		for blog in blogs:
			tags = []
			#for tag in blog.tags:
			#	tags.append(tag.name)
			print blog.id, blog.title.encode("utf-8")
			action = {
				"_index": "linpingta-blog",
				"_type": "article",
				"_id": blog.id,
				"_source": {
					"title": blog.title,
					"content": blog.content,
					"tags": tags,
					"author": blog.author.name
				}
			}
			actions.append(action)
			count = count + 1
			if count > 500:
				helpers.bulk(es, actions)
				actions = []
				count = 0

		if count > 0:
			helpers.bulk(es, actions)

	# make query
	res = es.search(index="linpingta-blog", body={
		"query": {	
			"match":{
				"content": u"python"
			}
		}
	})
	print "Got %d Hits" % res["hits"]["total"]
	print type(res['hits']['hits'])
	for hit in res['hits']['hits']:
    		print ("%(tags)s %(author)s: %(title)s" % hit["_source"]).encode("utf-8")
