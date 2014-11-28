from django.conf.urls import url

from movietickets import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^base2/', views.base2, name = 'base2'),
	url(r'^movies/',views.movies, name = 'movies'),
	url(r"^reserve/(?P<movie_name>\w.+?)/(?P<theater>\w.+?)/(?P<screen>[0-9]{1})/(?P<time>\w.+?)/",views.reserve, name = 'reserve'),
	url(r'^ticket/',views.ticket, name = 'ticket'),
	url(r'^movie/(?P<movie_name>\w.+?)/', views.movie, name='movie'),

	#url(r'^movie2/(?P<movie_name>\w+)/', views.movie2, name='movie'),
	
]