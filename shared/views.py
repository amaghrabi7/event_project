from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from event import models
from event.forms import EventForm
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request: HttpRequest) -> HttpResponse:
    event_items: list[models.Event] = list(models.Event.objects.all())
    context = {
        "event_items": event_items,
    }
    return render(request, "home.html", context)
  
def get_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context= {
       "user":{
        "id": user.id,
        "first_name": user.first_name,
        "last_name":user.last_name,
        "email":user.email,

       }

    }
    return render(request, "profile.html", context)