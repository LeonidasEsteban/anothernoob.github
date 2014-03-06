# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Champions.portrait'
        db.add_column(u'leagueoflegends_champions', 'portrait',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)

        # Adding field 'Champions.splashscreen'
        db.add_column(u'leagueoflegends_champions', 'splashscreen',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Champions.portrait'
        db.delete_column(u'leagueoflegends_champions', 'portrait')

        # Deleting field 'Champions.splashscreen'
        db.delete_column(u'leagueoflegends_champions', 'splashscreen')


    models = {
        u'leagueoflegends.champions': {
            'Meta': {'object_name': 'Champions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'rol': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leagueoflegends.Roles']", 'symmetrical': 'False'}),
            'splashscreen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'leagueoflegends.roles': {
            'Meta': {'object_name': 'Roles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['leagueoflegends']