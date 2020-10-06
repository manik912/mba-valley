from django.db import models
from django.utils import timezone
from user.models import User
from phone_field import PhoneField


# Create your models here.
class competition(models.Model):
    """docstring for competition"""

    organiser_name 				= models.CharField(max_length = 50, default = "Enter Organiser Name")
    organiser_email				= models.CharField(max_length = 50, default = "Enter Organiser Email")
    name 				= models.CharField(max_length = 50)
    about 				= models.CharField(max_length = 20000)
    registration_open 			= models.DateTimeField(default = timezone.now)
    registration_deadline 			= models.DateTimeField(default = timezone.now)
    submission_start 			= models.DateTimeField(default = timezone.now)
    submission_close           = models.DateTimeField(default = timezone.now)
    min_size 			= models.IntegerField(default = 1)
    max_size 			= models.IntegerField(default = 1)
    image 				= models.ImageField(default = 'competition/default.png', upload_to = 'competition/')
    team_link           = models.CharField(max_length = 100, default = '')
    registered 			= models.IntegerField(default = 0)
    competition_popular = models.BooleanField(default = False)
    file                = models.FileField(upload_to = 'file/', default = 'competition/default.png')
    is_published        = models.BooleanField(default = False) 

    def __str__(self):
        return self.name
    
    def last_year(self):
        return self.registration_deadline.strftime('%Y')

    def last_month(self):
        return self.registration_deadline.strftime('%m')

    def last_day(self):
        return self.registration_deadline.strftime('%d')

    def last_hour(self):
        return self.registration_deadline.strftime('%H')

    def last_minute(self):
        return self.registration_deadline.strftime('%M')

    def last_second(self):
        return self.registration_deadline.strftime('%S')

    def begin_year(self):
        return self.registration_open.strftime('%Y')

    def begin_month(self):
        return self.registration_open.strftime('%m')

    def begin_day(self):
        return self.registration_open.strftime('%d')

    def begin_hour(self):
        return self.registration_open.strftime('%H')

    def begin_minute(self):
        return self.registration_open.strftime('%M')

    def begin_second(self):
        return self.registration_open.strftime('%S')

    def open_year(self):
        return self.submission_start.strftime('%Y')

    def open_month(self):
        return self.submission_start.strftime('%m')

    def open_day(self):
        return self.submission_start.strftime('%d')

    def open_hour(self):
        return self.submission_start.strftime('%H')

    def open_minute(self):
        return self.submission_start.strftime('%M')

    def open_second(self):
        return self.submission_start.strftime('%S')

    def close_year(self):
        return self.submission_close.strftime('%Y')

    def close_month(self):
        return self.submission_close.strftime('%m')

    def close_day(self):
        return self.submission_close.strftime('%d')

    def close_hour(self):
        return self.submission_close.strftime('%H')

    def close_minute(self):
        return self.submission_close.strftime('%M')

    def close_second(self):
        return self.submission_close.strftime('%S')

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
	file 			= models.FileField(upload_to = 'file_submit/')

class Team(models.Model):
	"""docstring for Team"""
	event 			= models.ForeignKey(competition, related_name = 'team_event', on_delete= models.CASCADE)
	lead 			= models.ForeignKey(User, related_name = 'team_leader', on_delete= models.CASCADE)
	member_name 	= models.CharField(max_length = 50)
	college			= models.CharField(max_length = 100)
	contact_no 		= PhoneField(blank=False, null=False, help_text='Add country code before the contact no.')
	email 			= models.EmailField(max_length=254)
