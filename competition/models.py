from django.db import models
from django.utils import timezone
from user.models import User

# Create your models here.
class competition(models.Model):
	"""docstring for competition"""

	organiser 			= models.ForeignKey(User, related_name = 'organiser', on_delete = models.CASCADE, null = True)
	name 				= models.CharField(max_length = 20)
	about 				= models.CharField(max_length = 200)
	last_date 			= models.DateTimeField(default = timezone.now)
	begin_date 			= models.DateTimeField(default = timezone.now)
	event_date 			= models.DateTimeField(default = timezone.now)
	min_size 			= models.IntegerField(default = 1)
	max_size 			= models.IntegerField(default = 1)
	image 				= models.ImageField(default = 'competition/default.png', upload_to = 'competition/')
	registered 			= models.IntegerField(default = 0)
	competition_popular = models.BooleanField(default = False)

	def __str__(self):
		return self.name

class register(models.Model):
	"""docstring for register"""
	event 			= models.ForeignKey(competition, related_name = 'competition', on_delete = models.CASCADE, null = True)
	team_leader 	= models.ForeignKey(User, related_name = 'participants', on_delete = models.CASCADE, null = True)
	clg 			= models.CharField(max_length = 50, null=True)


class prizes(models.Model):
	"""docstring for prizes"""
	event 			= models.ForeignKey(competition, related_name = 'event', on_delete = models.CASCADE, null = True)
	title 			= models.CharField(max_length = 20)
	reward 			= models.CharField(max_length = 20)

class submit(models.Model):
	"""docstring for submit"""
	event 			= models.ForeignKey(competition, related_name= 'submit_competition', on_delete = models.CASCADE)
	leader 			= models.ForeignKey(User, related_name = 'leader', on_delete = models.CASCADE)
	file 			= models.FileField(upload_to = 'file/')