# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movietickets_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('release_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('categories', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('actors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age_restriction', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('movie_length', self.gf('django.db.models.fields.TimeField')()),
            ('ticket_cost', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'movietickets', ['Movie'])

        # Adding model 'Theater'
        db.create_table(u'movietickets_theater', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theater_name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('established', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'movietickets', ['Theater'])

        # Adding model 'Screen'
        db.create_table(u'movietickets_screen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theater', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movietickets.Theater'])),
            ('screen_number', self.gf('django.db.models.fields.IntegerField')()),
            ('movie_playing', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('occupancy', self.gf('django.db.models.fields.IntegerField')()),
            ('reserved', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'movietickets', ['Screen'])

        # Adding model 'Reserved'
        db.create_table(u'movietickets_reserved', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('screen', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('movie', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('theater', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('no_of_seats', self.gf('django.db.models.fields.IntegerField')()),
            ('amount_paid', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'movietickets', ['Reserved'])

        # Adding model 'Hours'
        db.create_table(u'movietickets_hours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show_time', self.gf('django.db.models.fields.TimeField')()),
            ('screen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movietickets.Screen'])),
        ))
        db.send_create_signal(u'movietickets', ['Hours'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movietickets_movie')

        # Deleting model 'Theater'
        db.delete_table(u'movietickets_theater')

        # Deleting model 'Screen'
        db.delete_table(u'movietickets_screen')

        # Deleting model 'Reserved'
        db.delete_table(u'movietickets_reserved')

        # Deleting model 'Hours'
        db.delete_table(u'movietickets_hours')


    models = {
        u'movietickets.hours': {
            'Meta': {'object_name': 'Hours'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'screen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movietickets.Screen']"}),
            'show_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'movietickets.movie': {
            'Meta': {'object_name': 'Movie'},
            'actors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age_restriction': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'categories': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_length': ('django.db.models.fields.TimeField', [], {}),
            'movie_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'release_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ticket_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'movietickets.reserved': {
            'Meta': {'object_name': 'Reserved'},
            'amount_paid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'no_of_seats': ('django.db.models.fields.IntegerField', [], {}),
            'screen': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'theater': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'movietickets.screen': {
            'Meta': {'object_name': 'Screen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_playing': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'occupancy': ('django.db.models.fields.IntegerField', [], {}),
            'reserved': ('django.db.models.fields.IntegerField', [], {}),
            'screen_number': ('django.db.models.fields.IntegerField', [], {}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movietickets.Theater']"})
        },
        u'movietickets.theater': {
            'Meta': {'object_name': 'Theater'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'established': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theater_name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['movietickets']