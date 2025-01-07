from django.http import HttpResponse
from django.shortcuts import render
from views import events

def home(request):
    return HttpResponse("<h1>Welcome everybody to Syndicate Events Manager</h1>")

def events(request):
    return render(request, 'events.html')