from django.shortcuts import render
from .models import competition

# Create your views here.
def competitionDetailView(request):
	
	Competition = competition.objects.filter(id=1).first()

	context = {
		'Competition' : Competition,
	}

	return render(request, 'competition/competition_detail.html', context)