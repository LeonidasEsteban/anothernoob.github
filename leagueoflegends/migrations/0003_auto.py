# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field rol on 'Champions'
        m2m_table_name = db.shorten_name(u'leagueoflegends_champions_rol')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('champions', models.ForeignKey(orm[u'leagueoflegends.champions'], null=False)),
            ('roles', models.ForeignKey(orm[u'leagueoflegends.roles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['champions_id', 'roles_id'])


    def backwards(self, orm):
        # Removing M2M table for field rol on 'Champions'
        db.delete_table(db.shorten_name(u'leagueoflegends_champions_rol'))


    models = {
        u'leagueoflegends.champions': {
            'Meta': {'object_name': 'Champions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'rol': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['leagueoflegends.Roles']", 'symmetrical': 'False'})
        },
        u'leagueoflegends.roles': {
            'Meta': {'object_name': 'Roles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['leagueoflegends']