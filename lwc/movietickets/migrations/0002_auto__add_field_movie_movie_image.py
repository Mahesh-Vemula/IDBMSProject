# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.movie_image'
        db.add_column(u'movietickets_movie', 'movie_image',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.movie_image'
        db.delete_column(u'movietickets_movie', 'movie_image')


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
            'movie_image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
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