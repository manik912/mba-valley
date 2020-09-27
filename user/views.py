from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserUpdate	
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User = form.save()

            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def update(request):
	if request.method == 'POST':
		form = UserUpdate(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			form = UserUpdate(instance=request.user)
		context = {
			'form' : form,
		}
		return render(request, 'user/update_profile.html', context)
