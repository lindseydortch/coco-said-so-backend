from django.db import models
from datetime import datetime 

# Create your models here.
class Agency(models.Model):
  agency_name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  agency_instagram_hadnle = models.CharField(max_length=500, blank=True)
  insta_followers = models.CharField(max_length=100, blank=True)
  digitals_required = models.CharField(max_length=5, blank=True)
  digitals_requirements = models.CharField(max_length=2000, blank=True)
  outreach = models.CharField(max_length=5, blank=True)
  date_digitals_submitted = models.DateField(auto_now=False, blank=True)
  notes = models.CharField(max_length=5000, blank=True)

  def __str__(self):
    return self.name