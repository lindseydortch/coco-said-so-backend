from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 

# Create your models here.
class Goals(models.Model):
  goal = models.CharField(max_length=5000)
  date_date = models.DateField(auto_now=False, blank=True)
  tasks_to_complete_goal = models.CharField(max_length=5000, blank=True)
  owner= models.ForeignKey(User, related_name='goals', on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.name