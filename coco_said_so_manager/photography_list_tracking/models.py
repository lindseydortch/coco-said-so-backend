from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime 

# Create your models here.
class Photographer(models.Model):
  photographer_name = models.CharField(max_length=100)
  photographer_location = models.CharField(max_length=100)
  photographer_instagram_hadnle = models.CharField(max_length=500, blank=True)
  insta_followers = models.CharField(max_length=100, blank=True)
  mutual_models = models.CharField(max_length=1000, blank=True)
  outreach = models.CharField(max_length=5, blank=True)
  outreach_date = models.DateField(auto_now=False, blank=True)
  agencies_work_with = models.CharField(max_length=1000, blank=True)
  notes = models.CharField(max_length=5000, blank=True)

  def __str__(self):
    return self.name