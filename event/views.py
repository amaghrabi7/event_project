from django.shortcuts import render, redirect
from event.forms import EventForm
from .models import Event
from django.contrib.auth import get_user_model
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()

# Create your views here.
@staff_member_required()
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

@login_required
def book_event(request, event_id):
    event= Event.objects.get(id=event_id)
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            messages.success(request, 'Booking made successfully!')
            return redirect("booking_success")
    context = {
        "event": event,
        "form": form,
    }
    return render(request, "book-event.html", context)

def booking_success(request):
    return render(request, "booking-success.html")

    