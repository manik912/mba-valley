from django import forms
from .models import submit, Team, register, competition, prizes
from django.http import request

class SubmitForm(forms.ModelForm):	
	class Meta():
		model 	= submit
		fields=['file']

class TeamForm(forms.ModelForm):	
	class Meta():
		model 	= Team
		fields=['member_name', 'college', 'contact_no', 'email']

class Register(forms.ModelForm):
	"""docstring for Register"""
	class Meta():
		"""docstring for Meta"""
		model =	register
		fields = ['College']

class competitionCreateForm(forms.ModelForm):
	event_name = forms.CharField(max_length = 20)
	about_the_event = forms.CharField(max_length = 20000)
	class Meta():
		model 	= competition
		fields=['organiser_name','organiser_email','event_name','about_the_event','registration_open','registration_deadline','submission_start','submission_close','min_size','max_size','image','file']

class AwardForm(forms.ModelForm):

	check = forms.CharField(max_length = 10, required = False)

	class Meta():
		model = prizes
		fields = ['title', 'reward', 'check']
