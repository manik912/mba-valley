from django import forms
from .models import submit
from django.http import request

class SubmitForm(forms.ModelForm):	
	class Meta():
		model 	= submit
		fields=['file']
