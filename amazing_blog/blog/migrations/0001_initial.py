# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
            ('mas', self.gf('django.db.models.fields.TextField')()),
            ('visto', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bliblablu', to=orm['blog.Post'])),
        ))
        db.send_create_signal(u'blog', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')


    models = {
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bliblablu'", 'to': u"orm['blog.Post']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'mas': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'visto': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['blog']