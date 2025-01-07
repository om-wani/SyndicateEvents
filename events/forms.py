from django import forms
from .models import Event

# Create your forms below this

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_type', 'date']
