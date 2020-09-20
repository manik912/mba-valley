from django.db import models
from users.models import User

# Create your models here.
class competition(object):
	"""docstring for competition"""

	organiser 		= models.ForeignKey(User, related_name = 'organiser', on_delete = models.CASCADE, null = True)
	name 			= models.CharField(max_length = 20)
	about 			= models.CharField(max_length = 200)
	last_date 		= models.DateTimeField(default = timezone.now)
	begin_date 		= models.DateTimeField(default = timezone.now)
	min_size 		= models.IntegerField(default = 1)
	max_size 		= models.IntegerField(default = 1)
	prizes 			= models.ForeignKey(prizes, related_name = 'prize', on_delete = models.CASCADE)
	image 			= models.ImageField(default = 'competition/default.png', upload_to = 'competition/')

	def __str__(self):
		return self.name

class register(object):
	"""docstring for register"""
	event 			= models.ForeignKey(competition, related_name = 'competition', on_delete = models.CASCADE, null = True)
	team_leader 	= models.ForeignKey(User, related_name = 'participants', on_delete = models.CASCADE, null = True)

class prizes(object):
	"""docstring for prizes"""
	event 			= models.ForeignKey(competition, related_name = 'event', on_delete = models.CASCADE, null = True)
	title 			= models.CharField(max_length = 20)
	reward 			= models.CharField(max_length = 20)

