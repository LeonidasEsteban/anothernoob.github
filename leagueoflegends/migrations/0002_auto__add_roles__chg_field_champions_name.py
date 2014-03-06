# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Roles'
        db.create_table(u'leagueoflegends_roles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'leagueoflegends', ['Roles'])


        # Changing field 'Champions.name'
        db.alter_column(u'leagueoflegends_champions', 'name', self.gf('django.db.models.fields.CharField')(max_length=140))

    def backwards(self, orm):
        # Deleting model 'Roles'
        db.delete_table(u'leagueoflegends_roles')


        # Changing field 'Champions.name'
        db.alter_column(u'leagueoflegends_champions', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'leagueoflegends.champions': {
            'Meta': {'object_name': 'Champions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'leagueoflegends.roles': {
            'Meta': {'object_name': 'Roles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['leagueoflegends']