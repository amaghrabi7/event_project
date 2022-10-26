from django.shortcuts import render, redirect
from event.forms import EventForm
from .models import Event
from django.contrib.auth import get_user_model
from .forms import EventBookForm

User = get_user_model()

# Create your views here.

def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "create-event.html", context )


def book_event(request, event_id):
    event= Event.objects.get(id=event_id)
    form = EventBookForm(instance=event)
    if request.method == "POST":
        form = EventBookForm(request.POST, instance=event)
    context = {
        "event": event,
        "form": form,
    }
    return render(request, "book-event.html", context)

    