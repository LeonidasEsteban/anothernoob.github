# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Champions'
        db.create_table(u'leagueoflegends_champions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'leagueoflegends', ['Champions'])


    def backwards(self, orm):
        # Deleting model 'Champions'
        db.delete_table(u'leagueoflegends_champions')


    models = {
        u'leagueoflegends.champions': {
            'Meta': {'object_name': 'Champions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['leagueoflegends']