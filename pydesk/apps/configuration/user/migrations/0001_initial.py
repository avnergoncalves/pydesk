# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='user', unique=True, to=orm['auth.User'])),
            ('receive_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('color_system', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('auto_update_dashboard', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'user', ['UserProfile'])

        # Adding M2M table for field enterprise on 'UserProfile'
        m2m_table_name = db.shorten_name('userprofile_enterprise')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'user.userprofile'], null=False)),
            ('enterprise', models.ForeignKey(orm[u'enterprise.enterprise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'enterprise_id'])

        # Adding M2M table for field equip on 'UserProfile'
        m2m_table_name = db.shorten_name('userprofile_equip')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'user.userprofile'], null=False)),
            ('equip', models.ForeignKey(orm[u'equip.equip'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'equip_id'])

        # Adding M2M table for field project on 'UserProfile'
        m2m_table_name = db.shorten_name('userprofile_project')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'user.userprofile'], null=False)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'project_id'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('userprofile')

        # Removing M2M table for field enterprise on 'UserProfile'
        db.delete_table(db.shorten_name('userprofile_enterprise'))

        # Removing M2M table for field equip on 'UserProfile'
        db.delete_table(db.shorten_name('userprofile_equip'))

        # Removing M2M table for field project on 'UserProfile'
        db.delete_table(db.shorten_name('userprofile_project'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'equip.equip': {
            'Meta': {'object_name': 'Equip', 'db_table': "'equip'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project', 'db_table': "'project'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'user.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'userprofile'"},
            'auto_update_dashboard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'color_system': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enterprise': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['enterprise.Enterprise']", 'symmetrical': 'False'}),
            'equip': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['equip.Equip']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Project']", 'symmetrical': 'False'}),
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['user']