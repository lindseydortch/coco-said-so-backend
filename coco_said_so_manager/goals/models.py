from django.db import models
from datetime import datetime 

# Create your models here.
class Goals(models.Model):
  goal = models.CharField(max_length=5000)
  date_date = models.DateField(auto_now=False, blank=True)
  tasks_to_complete_goal = models.CharField(max_length=5000, blank=True)

  def __str__(self):
    return self.name