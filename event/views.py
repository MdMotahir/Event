from django.shortcuts import render, redirect
from event.models import Category,Event,BookEvent
from event.forms import ContactUsForm,EventCreateForm,EventUpdateForm
from django.views import generic,View
from django.views.generic.edit import CreateView,UpdateView,FormView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model
from datetime import datetime
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def Home(request):
    return render(request,'event/Home.html')

class EventListView(generic.ListView):
    model = Event
    template_name = 'event/Home.html'
    now=datetime.now()
    queryset = Event.objects.filter(start_date__gte=now)
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category']= category
        return context
class EventDetailView(LoginRequiredMixin,generic.DetailView):
    model = Event
    template_name = "event/Event Details.html"
    login_url=reverse_lazy('login')


class EventCreateView(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    permission_required='event.add_event'
    login_url=reverse_lazy('login')
    model = Event
    form_class= EventCreateForm
    template_name="event/Event Create.html"
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        form.instance.organiser = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    permission_required='event.change_event'
    login_url=reverse_lazy('login')
    model= Event
    form_class= EventUpdateForm
    template_name="event/Event Update.html"
    success_url=reverse_lazy("home")

    def form_valid(self,form):
        form.instance.organiser = self.request.user
        return super().form_valid(form)

    def test_func(self,*args, **kwargs):
        event= Event.objects.get(slug=self.kwargs.get('slug'))
        if event.organiser==self.request.user:
            return True
        else:
            return False

class EventDeleteView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    permission_required='event.delete_event'
    login_url=reverse_lazy('login')
    model= Event
    template_name="event/Event Delete.html"
    success_url=reverse_lazy("home")

    def test_func(self,*args, **kwargs):
        event= Event.objects.get(slug=self.kwargs.get('slug'))
        if event.organiser==self.request.user:
            return True
        else:
            return False

def thank_you(request):
    return render(request,'event/Thank You.html')


def category_page(request,slug):
    now=datetime.now()
    category=Category.objects.all()
    cat=Category.objects.get(slug=slug)
    events=Event.objects.filter(category=cat,start_date__gte=now)
    return render(request,"event/Category.html",context={"cat":cat,"events":events,"category":category})

def old_events(request):
    now=datetime.now()
    events=Event.objects.filter(start_date__lt=now)
    return render(request,"event/Old.html",context={"events":events})

def my_events(request,id):
    user=get_user_model().objects.get(id=id)
    if user.category=='Organiser':
        events = Event.objects.filter(organiser=user)
        booked_events = BookEvent.objects.filter(user=user)
        return render(request,'event/my_events.html',context={'events':events,'booked_events':booked_events})
    else:
        booked_events = BookEvent.objects.filter(user=user)
        return render(request,'event/my_events.html',context={'events':booked_events})

class BookEventView(View):
    def get(self,request,slug):        
        event = Event.objects.get(slug=slug)
        now1=timezone.now()
        if event.start_date > now1:
            if event.organiser!=request.user:
                find_events=BookEvent.objects.filter(event=event,user=request.user)
                if not find_events:
                    if event.slot_booked<event.maximum_participants:
                        slotbooks = BookEvent.objects.create(
                            event=event, user=request.user
                        )
                        event.slot_booked+=1
                        event.save()
                        return redirect(reverse_lazy('My Events', args=[request.user.id]))
                    else:
                        return HttpResponse('Sorry All the Seats are Booked')
                else:
                    return HttpResponse('You already booked for this event')
            else:
                return HttpResponse('You are the Organiser Of this events')
        else:
            return HttpResponse('Events Date was Passed')