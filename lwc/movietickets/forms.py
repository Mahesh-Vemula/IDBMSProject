from django import forms
from .models import Reservation

class ReserveForm(forms.ModelForm):
	"""Store data of tickets reserved"""
	class Meta:
		model =  Reservation
		fields = ('name','theater','phone_number')


	