from django.urls import path,include
from api.views import EventView, AllEventsView


urlpatterns = [
    path('upcoming_events',EventView.as_view()),
    path('all_events',EventView.as_view()),
]