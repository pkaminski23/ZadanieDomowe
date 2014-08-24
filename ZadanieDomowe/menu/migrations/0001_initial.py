# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dish'
        db.create_table(u'menu_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default='c:\\Users\\pawel\\workspace\\ZadanieDomowe\\static/media/images/empty.jpg', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'menu', ['Dish'])

        # Adding model 'Menu'
        db.create_table(u'menu_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'menu', ['Menu'])

        # Adding M2M table for field dishes on 'Menu'
        m2m_table_name = db.shorten_name(u'menu_menu_dishes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'menu.menu'], null=False)),
            ('dish', models.ForeignKey(orm[u'menu.dish'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'dish_id'])


    def backwards(self, orm):
        # Deleting model 'Dish'
        db.delete_table(u'menu_dish')

        # Deleting model 'Menu'
        db.delete_table(u'menu_menu')

        # Removing M2M table for field dishes on 'Menu'
        db.delete_table(db.shorten_name(u'menu_menu_dishes'))


    models = {
        u'menu.dish': {
            'Meta': {'object_name': 'Dish'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': "'c:\\\\Users\\\\pawel\\\\workspace\\\\ZadanieDomowe\\\\static/media/images/empty.jpg'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        u'menu.menu': {
            'Meta': {'object_name': 'Menu'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'dishes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['menu.Dish']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['menu']