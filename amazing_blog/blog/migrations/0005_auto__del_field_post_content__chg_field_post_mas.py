# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.content'
        db.delete_column(u'blog_post', 'content')


        # Changing field 'Post.mas'
        db.alter_column(u'blog_post', 'mas', self.gf('tinymce.models.HTMLField')(default=u'Escriba aqu\xc3\xad'))

    def backwards(self, orm):
        # Adding field 'Post.content'
        db.add_column(u'blog_post', 'content',
                      self.gf('tinymce.models.HTMLField')(default='foobar'),
                      keep_default=False)


        # Changing field 'Post.mas'
        db.alter_column(u'blog_post', 'mas', self.gf('django.db.models.fields.TextField')(null=True))

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
            'mas': ('tinymce.models.HTMLField', [], {}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'visto': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['blog']