#encoding:utf-8

from django.db import models
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from athumb.fields import ImageWithThumbsField
from suit_redactor.widgets import RedactorWidget
from taggit_autosuggest.managers import TaggableManager

import os
from uuid import uuid4

def upload_image(path):
		def wrapper(instance, filename):
				ext = filename.split('.')[-1]
				if instance.pk:
						filename = '{}.{}'.format(instance.pk, ext)
				else:
						filename = '{}.{}'.format(uuid4().hex, ext)
				return os.path.join(path, filename)
		return wrapper

class File(models.Model):
		upload = models.FileField(upload_to=upload_image("news/content/"))
		date_created = models.DateTimeField(default=timezone.now())
		is_image = models.BooleanField(default=True)

class Articles(models.Model):
		title = models.CharField(max_length = 140, verbose_name = 'título', help_text = 'máximo 140 caracteres')
		summary = models.CharField(max_length = 200, verbose_name = 'resumen', help_text = 'máximo 200 caracteres' )
		"""cover = ImageWithThumbsField(upload_to='articles/covers', thumbs=(
						('128x128', {'size': (128, 128)}),
						('60x60', {'size': (60, 60)}),
						('80x1000', {'size': (80, 1000)}),
						('front_page', {'size': (120, 1000)}),
						('medium', {'size': (161, 1000)}),
						('large', {'size': (200, 1000)}),
				), help_text = 'tamaño de imagen 1920x1080')"""
		cover = models.ImageField(upload_to = upload_image('articles/covers'), verbose_name = 'portada', help_text = 'ratio 16:9, de preferencia 1920x1080')
		content = models.TextField(verbose_name = 'contenido')
		source = models.TextField(verbose_name = 'fuente', help_text = 'enlaces separados por ,')
		tags = TaggableManager()
		date = models.DateTimeField(default = timezone.now(), verbose_name = 'fecha de publicación');
		url_slug = models.SlugField(max_length = 140, verbose_name = 'slug', help_text = 'url generada automáticamente')
		author = models.ForeignKey(User, null=True, blank=True, verbose_name = 'autor')
		promoted = models.BooleanField(verbose_name = 'promocionado')
		published = models.BooleanField(verbose_name = 'publicado', help_text = 'solo para editores')
		
		class Meta:
				verbose_name = 'noticia'
				
		def __unicode__(self):
				return self.title

		def as_json(self):
			return dict(
				id = self.id,
				url_slug = self.url_slug,
				cover = self.cover.url,
				title = self.title,
				summary = self.summary,
				author = dict(
					first_name = self.author.first_name,
					last_name = self.author.last_name),
				date = self.date.strftime('%d/%m/%y'),
				)
						
class ArticlesForm(ModelForm):
		class Meta:
				widgets = {
						'content': RedactorWidget(
																			editor_options = {
																											'lang': 'es',
																											'buttons': [
																																	'html',
																																	'|', 'formatting', 
																																	'|', 'bold', 'italic', 'deleted', 'underline', 
																																	'|', 'unorderedlist', 'orderedlist', 
																																	'|', 'image', 'video', 'file', 'table', 'link',
																																	'|', 'alignleft', 'aligncenter', 'alignright', 'justify'
																																	],
																											'formattingTags': ['p', 'blockquote', 'h2', 'h3', 'h4'],
																											'linkProtocol': 'false',
																											'boldTag': 'b',
																											'pastePlainText': 'true',
																											'linkNofollow': 'true',
																											'fixed': 'true',
																											'toolbarFixed': 'true',
																											'imageUpload': '/ajax/photos/upload/',
																											'imageGetJson': '/ajax/photos/recent/',
																											'convertVideoLinks': 'true',
																											}
																			),
						'source': RedactorWidget(
																			editor_options = {
																											'lang': 'es',
																											'buttons': [
																																	'html','|',
																																	'link',
																																	],
																											'linkProtocol': 'false',
																											'pastePlainText': 'true',
																											'linkNofollow': 'true',
																											'fixed': 'true',
																											'toolbarFixed': 'true',
																											}
																			)
				}
				
class ArticlesAdmin(ModelAdmin):
		list_display = ('title', 'author', 'date', 'published')
		form = ArticlesForm
		prepopulated_fields = {"url_slug": ("title",)}
		
		def save_model(self, request, obj, form, change):
				if getattr(obj, 'author', None) is None:
						obj.author = request.user
				obj.save()
		
# Admin site
from django.contrib import admin

admin.site.register(Articles, ArticlesAdmin)