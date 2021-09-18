from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
class Photographer(models.Model):
  photographer_name = models.CharField(max_length=100)
  photographer_location = models.CharField(max_length=100)
  photographer_instagram_handle = models.CharField(max_length=500, blank=True)
  insta_followers = models.CharField(max_length=100, blank=True)
  mutual_models = models.CharField(max_length=1000, blank=True)
  outreach = models.CharField(max_length=100, blank=True)
  outreach_date = models.DateField(auto_now=False, blank=True)
  agencies_work_with = models.CharField(max_length=1000, blank=True)
  notes = models.CharField(max_length=5000, blank=True)
  owner= models.ForeignKey(User, related_name='photography_list_track', on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name