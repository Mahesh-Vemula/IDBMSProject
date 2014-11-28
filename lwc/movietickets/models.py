from django.db import models

# Create your models here.
class Movie(models.Model):
	"""This class stores the 
	movie details into the system"""
	movie_name =  models.CharField(max_length=200)
	release_date = models.DateField("Date Released",auto_now_add=False)
	categories = models.CharField(max_length = 200, help_text='Example : Adventure|Action|Drama')
	country = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
	actors = models.CharField(max_length=200)
	age_restriction = models.CharField(max_length = 3)
	description = models.CharField(max_length = 1000)
	rating = models.IntegerField()
	movie_length = models.TimeField("Lenght of Movie")
	ticket_cost = models.IntegerField(null = True)
	movie_image = models.CharField(max_length= 200, null = True)
	def __str__(self):
		return self.movie_name

class Theater(models.Model):
	"""This class stores the 
	theater details into the system"""	
	theater_name = models.CharField(max_length=500)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length = 100)
	established = models.DateField('Date of Establishment')
	def __str__(self):
		return self.theater_name

class Screen(models.Model):
	"""This class defines screen for 
	theater"""
	theater = models.ForeignKey(Theater)
	screen_number = models.IntegerField()
	movie_playing = models.CharField(max_length = 200)
	occupancy = models.IntegerField()
	reserved = models.IntegerField()
	def __str__(self):
		return str(self.screen_number)

class Reservation(models.Model):
	"""Store data of tickets reserved"""
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 15, null =True)
	ticket_number = models.CharField(max_length = 25, null =False, blank = False)
	screen = models.CharField(max_length = 200)
	movie = models.CharField(max_length = 200)
	theater = models.CharField(max_length = 200)
	time = models.TimeField("Show Time",null =True)
	date = models.DateField("Show Date",null =True)
	no_of_seats = models.IntegerField(null =True)
	amount_paid = models.IntegerField(null =True)
	def __str__(self):
		return self.ticket_number

class Hours(models.Model):
	"""Display show hours"""
	show_time = models.TimeField("Show Time")
	screen = models.ForeignKey(Screen)
	#time = models.CharField(max_length = 20)
	def __str__(self):
		return str(self.show_time)
