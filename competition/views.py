from django.shortcuts import render
from .models import competition, prizes
from .models import prizes as Prizes

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


def submit(request):
	# if request.methord == 'POST':
	# 	form = SubmitForm(request.POST, request.FILES)
	# 	if form.is_valid():
	# 		form.save()
				
	return render(request, 'competition/submit.html')
