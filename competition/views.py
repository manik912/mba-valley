from django.shortcuts import render, HttpResponseRedirect
from .models import competition, prizes
from .models import prizes as Prizes
from .forms import SubmitForm, TeamForm, Register


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
	context = {
		'Competition' : Competition
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
	}
	return render(request, 'competition/submit.html', context)

def competitionRegister(request, pk):
	compe = competition.objects.filter(id=pk).first()
	user = request.user
	if request.method == 'POST':
		form = Register(request.POST)
		form.instance.event = come
		form.instance.team_leader = user
		form.save()
	else:
		form = Register()		
	context = {
		'user' : user,
		'form' : form,
	}

	return render(request, 'competition/register-competition.html', context)
