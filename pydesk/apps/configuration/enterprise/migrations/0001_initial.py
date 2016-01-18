# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Enterprise'
        db.create_table('enterprise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rasao_social', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nome_fantasia', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('inscricao_estadual', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('observacao', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'enterprise', ['Enterprise'])


    def backwards(self, orm):
        # Deleting model 'Enterprise'
        db.delete_table('enterprise')


    models = {
        u'enterprise.enterprise': {
            'Meta': {'object_name': 'Enterprise', 'db_table': "'enterprise'"},
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscricao_estadual': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nome_fantasia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'observacao': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'rasao_social': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['enterprise']