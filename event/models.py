from django.db import models
from users.forms import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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
    users = models.ManyToManyField(
        User, related_name="events"
    )

    created_by= models.ForeignKey(settings.AUTH_USER_MODEL)




