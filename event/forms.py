from cProfile import label
from django import forms
from .models import Event, Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "image", "description", "event_date","start_time","end_time", "seats", "location"]
        labels = { 'name':'Event Name',
                   'image':'Event Image',
                   'description':'Descriptions',
                   'event_date':'MM-DD-YYYY',
                   'start_time':'Start Time',
                   'end_time':'End Time',
                   'seates':'Seates',
                   'location':'Location',
                  
                   
                            }
        widgets = {
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
             'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["quantity"]