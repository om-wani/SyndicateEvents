from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

# Create your views here.

def landing_page(request):
    return render(request, 'events/landing_page.html')

def event_listings(request):
    events = Event.objects.all()

    # Filtering by date and type
    event_type = request.GET.get('event_type')
    date = request.GET.get('date')

    if event_type:
        events = events.filter(event_type=event_type)
    if date:
        events = events.filter(date=date)

    # Search functionality
    query = request.GET.get('q')
    if query:
        events = events.filter(title__icontains=query)

    return render(request, 'events/event_listings.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_listings')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})
