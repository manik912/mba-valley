from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    content = models.TextField(max_length=7000)
    date_published = models.DateTimeField(default=timezone.now)
    blog_image = models.ImageField(default='default.jpg', upload_to='blog_images', blank=True)
    latest_popular = models.BooleanField(default = False)
    mba_popular = models.BooleanField(default = False)
    startup_popular = models.BooleanField(default = False)
    latest_story = models.BooleanField(default = False)
    mba_story = models.BooleanField(default = False)
    startup_story = models.BooleanField(default = False)
    trending_story = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class chek(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)