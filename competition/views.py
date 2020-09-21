from django.shortcuts import render
from .models import competition, prizes
from .models import prizes as Prizes

# Create your views here.
def competitionDetailView(request):
	
	Competition = competition.objects.filter(id=1).first()

	context = {
		'Competition' : Competition,
		'Prizes' : Prizes.objects.filter(event = Competition)
	}

	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print(Competition.organiser.name)
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

	return render(request, 'competition/competition_detail.html', context)