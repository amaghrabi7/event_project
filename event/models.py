from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    # event date has to be in future. go over later
    event_date = models.DateTimeField()
    seats = models.PositiveIntegerField()
    # 
    location = models.TextField()
    
    participants = models.ManyToManyField(User, related_name="events")

    
    organizer= models.ForeignKey(User,on_delete=models.CASCADE, related_name="org_events")

    def __str__(self):
        return self.name




