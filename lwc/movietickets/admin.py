from django.contrib import admin

# Register your models here.
from .models import Movie, Theater, Hours, Screen, Reservation


class HoursInline(admin.TabularInline):
	"""make hours under as inlines"""
	model = Hours
	extra = 3		

class ScreenInline(admin.TabularInline):
	"""make scree under theater"""
	model = Screen
	extra = 1
	
class MovieAdmin(admin.ModelAdmin):
	"""Puts this on admin site"""
	class meta:
		model = Movie
	list_display = ('movie_name','release_date')
	list_filter = ['release_date','movie_name']
	search_fields = ['movie_name']


class TheaterAdmin(admin.ModelAdmin):
	"""Puts theater in admin site"""
	fieldsets = [
		(None, {'fields':['theater_name']}),
		('Info', {'fields':['address','established'], 'classes':['collapse']})
	]
	inlines = [ScreenInline]
	list_display = ('theater_name', 'address')
	search_fields = ['theater_name']
	list_filter = ['theater_name']
	def __str__(self):
		return self.theater_name

class ScreenAdmin(admin.ModelAdmin):
	"""Enter screen in admin page"""
	class meta:
		model = Screen
	inlines = [HoursInline]

class ReservedAdmin(admin.ModelAdmin):
	"""Reservation in admin page"""
	class meta:
		model = Reservation

		

admin.site.register(Movie, MovieAdmin)
admin.site.register(Theater, TheaterAdmin)
admin.site.register(Screen,ScreenAdmin)
admin.site.register(Reservation, ReservedAdmin)