from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('events/', views.event_listings, name='event_listings'),  # Ensure this is correct
    path('add_event/', views.add_event, name='add_event'),
]
