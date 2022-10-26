from django.shortcuts import render, redirect
from event.forms import EventForm
from .models import Event
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.


def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            # form["organizer"] =request.POST.get("username")
            # form["organizer"] = User.objects.get(pk=request.user.id)
            #  profile = form.save(commit=False)
            #  profile.user = request.user
            #  profile.save()
            # form.instance.orgnizer = request.user
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "create-event.html", context )

def book_event(request,event_id):
    event= Event.objects.get(event_id)
    