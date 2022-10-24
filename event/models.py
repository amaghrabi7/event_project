from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    # event date has to be in future. go over later
    event_date = models.DateTimeField()
    seats = models.IntegerField()
    # 
    location = models.TextField()


