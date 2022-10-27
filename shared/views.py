from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from event import models
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def home(request: HttpRequest) -> HttpResponse:
    event_items: list[models.Event] = list(models.Event.objects.all())
    context = {
        "event_items": event_items,
    }
    return render(request, "home.html", context)

@login_required 
def get_profile(request, user_id):
    user = User.objects.get(id=user_id)
    event_items: list[models.Event] = list(models.Event.objects.all())
    
    context= {
       "user":{
        "id": user.id,
        "first_name": user.first_name,
        "last_name":user.last_name,
        "email":user.email,},

        "event_items": event_items,
        

       }

    
    return render(request, "profile.html", context)




