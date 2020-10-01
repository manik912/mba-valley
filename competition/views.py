from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.urls import reverse
from .models import competition, prizes
from .models import prizes as Prizes
from .forms import SubmitForm, TeamForm, Register, competitionCreateForm


# Create your views here.
def competitionDetailView(request, pk):
	
	Competition = competition.objects.filter(id=pk).first()

	context = {
		'Competition' : Competition,
		'Prizes' : Prizes.objects.filter(event = Competition)
	}

	return render(request, 'competition/competition_detail.html', context)

def CompetitionListView(request):
	Competition = competition.objects.all()
	published = competition.objects.filter(is_published=True)
	context = {
		'Competition' : Competition,
		'published': published 
	}
	return render(request, 'competition/competition.html', context)


def submit(request, pk):
	comp = competition.objects.filter(id=pk).first()
	if request.method == 'POST':
		form = SubmitForm(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			form.instance.event = comp
			form.instance.leader = request.user
			form.save()
		# return HttpResponseRedirect(reverse('/'))
	else:
		form = SubmitForm()
	context = {
		'form' : form,
		'comp' : comp
	}
	return render(request, 'competition/submit.html', context)

def competitionCreateView(request):
	if request.method == 'POST':
		form = competitionCreateForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.organiser = request.user
			form.save()
			messages.success(
				request, 'Your submission has been sent to our team for review. In case of any query, you can contact us.')

			return HttpResponseRedirect(reverse('competition'))
	else:
		form = competitionCreateForm()
	context = {
		'form': form,
	}
	return render(request, 'competition/competition_form.html', context)


def competitionRegister(request, pk):
	compe = competition.objects.filter(id=pk).first()
	user = request.user
	if request.method == 'POST':
		form = Register(request.POST)
		form.instance.event = compe
		form.instance.team_leader = user
		compe.registered = compe.registered + 1
		compe.save()
		form.save()
		return redirect('https://docs.google.com/forms/d/1x7Wp0bHMWFMCEaq3dopv-bPU9bOFeuJJXXhfkqOw6w0/edit')
	else:
		form = Register()		
	context = {
		'user' : user,
		'form' : form,
	}

	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print(compe.registered)
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

	return render(request, 'competition/register-competition.html', context)
