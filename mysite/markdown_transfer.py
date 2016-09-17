#-*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :

''' transfer Octopress to blog'''

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

from lib.models import Author
from blogs.models import Blog, Tag


def _iterate_dirs(markdown_dirs, logger):
	markdown_files = []
	for subdir, dirs, files in os.walk(markdown_dirs):
		[ markdown_files.append(os.path.join(subdir, file)) for file in files if file.endswith('markdown') ]
	return markdown_files

def _extract_blog_meta(blog_file, logger):
	title = ''
	pub_date = ''
	category_names = []
	with open(blog_file, 'r') as fp_r:
		while 1:
			line = fp_r.readline()
			if not line.strip():
				break
			if 'title' in line:
				result = re.findall('title: "(.*)"', line)
				title = result[0] if result else ''
			if 'date' in line:
				result = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', line)
				pub_date = result[0] if result else ''
			if 'categories' in line:
				result = re.findall('\[(.*)\]', line)
				if result:
					category_names = result[0].split(',')
	return (title, pub_date, category_names)

def _transfer_markdown_to_html(blog_file, logger):
	content = subprocess.check_output("pandoc -f markdown -t html %s" % blog_file, shell=True)
	return content


if __name__ == '__main__':

	Blog.objects.all().delete()
	Tag.objects.all().delete()

	basepath = os.getcwd()
	logging.basicConfig(filename=os.path.join(basepath, 'logs/transfer_pandoc_markdown_to_html.log'), level=logging.DEBUG,
		format = '[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
		datefmt = '%a, %d %b %Y %H:%M:%S'
		)
	logger = logging.getLogger('TransferPandocMarkdownToHtml')

	author = Author.objects.get(name=u'褚桐')
	cur_time=time.strftime("%Y-%m-%d", time.localtime())

	markdown_dirs = '/home/test/markdown_to_html'
	blog_files = _iterate_dirs(markdown_dirs, logger)
	#blog_files = [ os.path.join(markdown_dirs, '2016-08-20-tools-project.markdown') ]
	for blog_file in blog_files:
		(title, pub_date, category_names) = _extract_blog_meta(blog_file, logger)
		if not title:
			logger.error('blog_file %s with no title defined' % blog_file)
			continue
		content = _transfer_markdown_to_html(blog_file, logger)

		if not pub_date:
			pub_date = cur_time
		logger.info('blog_file %s with title[%s] categories[%s] pub_data[%s]' % (blog_file, title, str(category_names), str(pub_date)))

		tags = Tag.objects.all()
		categories = []
		for category_name in category_names:
			category_name_s = category_name.strip()
			try:
				category = tags.get(name=category_name_s)
			except:
				category = Tag(
					name=category_name_s,
					count=1,
				)
			else:
				category.count = category.count + 1
			finally:
				category.save()
				categories.append(category)

		blog = Blog.objects.create(
			title=title,
			content=content,
			pub_date=pub_date,
			author=author
		)
		blog.save()
		[ blog.tags.add(category) for category in categories ]
