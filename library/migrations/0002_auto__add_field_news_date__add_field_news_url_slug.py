# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.date'
        db.add_column(u'library_news', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'News.url_slug'
        db.add_column(u'library_news', 'url_slug',
                      self.gf('django.db.models.fields.SlugField')(default=None, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.date'
        db.delete_column(u'library_news', 'date')

        # Deleting field 'News.url_slug'
        db.delete_column(u'library_news', 'url_slug')


    models = {
        u'library.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'url_slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']