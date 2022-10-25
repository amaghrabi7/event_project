from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "image", "description", "event_date", "seats", "location", "participants", "organizer"]
