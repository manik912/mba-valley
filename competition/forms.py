from django import forms
from .models import submit, Team, register
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