from django.contrib import admin

from event.models import Event, Booking

# Register your models here.
admin.site.register([Event, Booking])