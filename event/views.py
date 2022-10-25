from django.shortcuts import render, redirect
from event.forms import EventForm

# Create your views here.

def create_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "create-event.html", context )