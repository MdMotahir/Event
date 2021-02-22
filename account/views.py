from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse,reverse_lazy
from account.forms import SignUpForm, UserUpdateForm
from django.contrib.auth import get_user_model, authenticate, login
# Create your views here.

class SignUpView(generic.CreateView):
    model=get_user_model()
    form_class=SignUpForm
    template_name = "registration/Sign Up.html"
    success_url=reverse_lazy("home")
    def form_valid(self, form):
        to_return=super().form_valid(form)
        user=authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request,user)
        return to_return
class UserUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class=UserUpdateForm
    template_name = "registration/User Update.html"
    success_url=reverse_lazy("home")

class UserDetailView(generic.DetailView):
    model=get_user_model()
    template_name = "registration/User Details.html"

def password_reset_complete(request):
    return render(request,'registration/password_reset_complete.html')