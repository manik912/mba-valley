from django.db import models
from django.utils import timezone
from user.models import User
from phone_field import PhoneField


# Create your models here.
class competition(models.Model):
    """docstring for competition"""

    organiser 			= models.ForeignKey(User, related_name = 'organiser', on_delete = models.CASCADE, null = True)
    name 				= models.CharField(max_length = 20)
    about 				= models.CharField(max_length = 200)
    last_date 			= models.DateTimeField(default = timezone.now)
    begin_date 			= models.DateTimeField(default = timezone.now)
    event_date 			= models.DateTimeField(default = timezone.now)
    event_end           = models.DateTimeField(default = timezone.now)
    min_size 			= models.IntegerField(default = 1)
    max_size 			= models.IntegerField(default = 1)
    image 				= models.ImageField(default = 'competition/default.png', upload_to = 'competition/')
    registered 			= models.IntegerField(default = 0)
    competition_popular = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    
    def last_year(self):
        return self.last_date.strftime('%Y')

    def last_month(self):
        return self.last_date.strftime('%m')

    def last_day(self):
        return self.last_date.strftime('%d')

    def begin_year(self):
        return self.begin_date.strftime('%Y')

    def begin_month(self):
        return self.begin_date.strftime('%m')

    def begin_day(self):
        return self.begin_date.strftime('%d')

    def open_year(self):
        return self.event_date.strftime('%Y')

    def open_month(self):
        return self.event_date.strftime('%m')

    def open_day(self):
        return self.event_date.strftime('%d')

    def close_year(self):
        return self.event_end.strftime('%Y')

    def close_month(self):
        return self.event_end.strftime('%m')

    def close_day(self):
        return self.event_end.strftime('%d')

class register(models.Model):
	"""docstring for register"""
	event 			= models.ForeignKey(competition, related_name = 'competition', on_delete = models.CASCADE, null = True)
	team_leader 	= models.ForeignKey(User, related_name = 'participants', on_delete = models.CASCADE, null = True)
	College 		= models.CharField(max_length = 50, default = "Enter Your College Name")


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

class Team(models.Model):
	"""docstring for Team"""
	event 			= models.ForeignKey(competition, related_name = 'team_event', on_delete= models.CASCADE)
	lead 			= models.ForeignKey(User, related_name = 'team_leader', on_delete= models.CASCADE)
	member_name 	= models.CharField(max_length = 50)
	college			= models.CharField(max_length = 100)
	contact_no 		= PhoneField(blank=False, null=False, help_text='Add country code before the contact no.')
	email 			= models.EmailField(max_length=254)
