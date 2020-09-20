from django.shortcuts import render
from .models import competition

# Create your views here.
def competitionDetailView(request):
	
	Competition = competition.objects.filter(id=1) 

	context = {
		'Competition' : Competition,
	}

	return render(request, 'home/competition_detail.html', context)