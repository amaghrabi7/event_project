from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from event import models
from event.forms import EventForm



def home(request: HttpRequest) -> HttpResponse:
    event_items: list[models.Event] = list(models.Event.objects.all())
    context = {
        "event_items": event_items,
    }
    return render(request, "home.html", context)
  
