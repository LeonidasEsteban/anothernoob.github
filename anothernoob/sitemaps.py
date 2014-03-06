from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from library.models import Articles

from datetime import datetime

class ArticlesSitemap(Sitemap):
	changefreq = 'never'
	priority = 0.8

	def items(self):
		return Articles.objects.all()

	def lastmod(self, obj):
		return obj.date

	def location(self, obj):
		return '/article/%s/%s' % (obj.url_slug, obj.id)

class SiteSitemap(Sitemap):
	priority = 1
	def __init__(self, names):
		self.names = names

	def items(self):
		return self.names

	def changefreq(self, obj):
		return 'hourly'

	def lastmod(self, obj):
		return datetime.now()

	def location(self, obj):
		return reverse(obj)