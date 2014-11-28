from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponseRedirect
from .models import Movie,Theater,Screen,Hours, Reservation
from .forms import ReserveForm

# Create your views here.
def index(request):
	try:
		movie_list = Movie.objects.all()
	except Exception, e:
		raise Http404
	context={'movie_list':movie_list[:5]}
	template = 'index.html'
	return render(request,template,context)

def base2(request):
	context={}
	template = 'base2.html'
	return render(request,template,context)

def movie(request,movie_name):
	#movie = get_object_or_404(Movie, movie_name ='Bahubali')
	movie = get_object_or_404(Movie, movie_name = movie_name)
	screen_no = {}
	theaters_showing = {}
	for theaterObject in Theater.objects.all():
		screensShowing = []
		screensShowing = theaterObject.screen_set.filter(movie_playing = movie_name)
		for screen in screensShowing:
			screen_no[theaterObject.theater_name+"\t\t\t--\t\t\t"+str(screen.screen_number)] = screen.screen_number
			theaters_showing[theaterObject.theater_name+"\t\t\t--\t\t\t"+str(screen.screen_number)] = []#screen.screen_number]
			theaters_showing[theaterObject.theater_name+"\t\t\t--\t\t\t"+str(screen.screen_number)].append(screen.hours_set.all())
			theaters_showing[theaterObject.theater_name+"\t\t\t--\t\t\t"+str(screen.screen_number)].append(screen.screen_number)
	count = len(theaters_showing)
	context = {'movie':movie, 'theaters_showing': theaters_showing, 'screen_no':screen_no}
	template = 'movie.html'
	return render(request,template,context)

def movies(request):
	try:
		movie_list = Movie.objects.all()
	except Exception, e:
		raise Http404
	context={'movie_list':movie_list}
	template = 'movies.html'
	return render(request,template,context)

# def reserve(request):
# 	print request
# 	if request.method == 'POST':
# 		form = ReserveForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/ticket/')
# 	else:
# 		form = ReserveForm()
# 	context={'form':form}
# 	template='reserve.html'
# 	return render(request,template,context)

def reserve(request, movie_name, theater, screen, time):
	movie = get_object_or_404(Movie, movie_name = movie_name)
	context={'movie':movie, 'theater':theater, 'screen':screen, 'time':time}
	template = 'reserve.html'
	return render(request,template,context)

def ticket(request):
	#print request.POST
	#print request.method=="GET"
	if request.method == "POST":
		data = Reservation()
		data.name = request.POST['name']
		data.email = request.POST['email']
		data.phone_number = request.POST['phone_number']
		data.screen = request.POST['screen']
		data.movie = request.POST['movie']
		data.theater = request.POST['theater']
		data.time = request.POST['time']
		data.date = request.POST['date']
		data.no_of_seats = request.POST['no_of_seats']
		data.amount_paid = int(request.POST['price'])*int(request.POST['no_of_seats']) + int(request.POST['reservation_fee'])
		#data.amount_paid = 5
		ticket_number = (data.movie[:2]+data.theater[:2]+data.name[:2]+data.phone_number[:3]).lower()
		data.ticket_number = ticket_number
		data.save()
	#new_reserved = Reservation.objects.create( theater = request.POST["theater"],email = request.POST["email"], phone_number = request.POST["phone_number"])
	if request.method == "GET":
		print request.GET
		data = {}
		if 'ticket_number' in request.GET.keys():
			data = Reservation.objects.filter(ticket_number = request.GET['ticket_number'])
			data = data[0]
			print data
	context={'data':data}
	template='ticket.html'
	return render(request,template,context)


# def movie2(request, movie_name):
# 	movie = get_object_or_404(Movie, movie_name = movie_name)
# 	# try:
# 	# 	x = Movie.objects.get(movie_name = 'Bahubali')
# 	# except Exception, e:
# 	# 	raise Http404
	
# 	context = {'movie':movie}
# 	template = 'movie.html'
# 	return render(request,template,context)