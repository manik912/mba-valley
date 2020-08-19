from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User, Profile

class RegisterForm(UserCreationForm):
	email 				= forms.EmailField(help_text='Email Id used for registration cannot be changed later.')
	name 				= forms.CharField(max_length=60)
	username            = forms.CharField(max_length=100) 
	

	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'username', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data


class UpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'contact']

