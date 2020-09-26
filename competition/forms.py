from django import forms
from .models import submit, Team, register, competition
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
	class Meta():
		model 	= competition
		fields=['organiser','name','about','registration_open','registration_deadline','submission_start','submission_close','min_size','max_size','image','file']