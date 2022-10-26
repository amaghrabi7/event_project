from email.policy import default
from django.db import models

from django.conf import settings

from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    # event date has to be in future. go over later
    event_date = models.DateField()
    start_time = models.TimeField(default='20:00')
    end_time = models.TimeField(default='20:00')
    seats = models.PositiveIntegerField()
    book_seats = models.PositiveIntegerField(default=0)
    location = models.TextField()
    organizer= models.ForeignKey(User,on_delete=models.CASCADE, related_name="org_events")

    def __str__(self):
        return self.name

    @property
    def is_future(self):
        today = date.today()
        if self.event_date > today:
            return True
        else:
            return False


    @property
    def booked_seats(self):
        bookings = self.bookings.all()
        _bookings = []
        for booking in bookings:
           _bookings.append(booking.quantity)
        q = 0
        for quantinty in _bookings:
            q = q + quantinty
        return self.seats - q

    @property
    def event_status(self): 
        bookings = self.bookings.all()
        _bookings = []
        for booking in bookings:
           _bookings.append(booking.quantity)
        q = 0
        for quantinty in _bookings:
            q = q + quantinty
        
        if q < self.seats:
            return True
        else:
            return False



    # def created_updated(model, request):
    #     obj = model.objects.latest('pk')
    #     if obj.created_by is None:
    #         obj.created_by = request.user
    #     obj.save()


class Booking(models.Model):
    quantity = models.PositiveIntegerField()
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE,
        related_name="bookings"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="bookings"
    )

