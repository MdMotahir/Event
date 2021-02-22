from django.urls import path,include
from event.views import Home, EventListView, EventCreateView,EventUpdateView, EventDeleteView, thank_you, EventDetailView, category_page, my_events, BookEventView, old_events

urlpatterns = [
    # path("",Home,name='home'),
    path("",EventListView.as_view(),name='home'),
    path("Event/<slug:slug>",EventDetailView.as_view(),name='Event Details'),
    path("Event/<slug:slug>/update",EventUpdateView.as_view(),name='Event Update'),
    path("Event/<slug:slug>/delete",EventDeleteView.as_view(),name='Event Delete'),
    path("Event/<slug:slug>/booked",BookEventView.as_view(),name='Event Booked'),
    path("create_event",EventCreateView.as_view(),name='Event Create'),
    path('thank_you',thank_you,name='Thank You'),
    path("Category/<slug:slug>",category_page,name='Category Page'),
    path("MyEvents/<int:id>",my_events,name='My Events'),
    path('old_events',old_events,name='Old Events'),
]
